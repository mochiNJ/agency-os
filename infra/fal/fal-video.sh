#!/usr/bin/env bash
# fal.ai video generation helper (direct-API, queue + poll — no MCP settings touched).
# Videos are long jobs, so this submits to fal's queue and polls until done.
#
# Usage:
#   ./fal-video.sh <model-id> "<prompt>" <output.mp4> [extra-json]
#
# Examples (confirm exact model slug on fal.ai/models before first use):
#   ./fal-video.sh fal-ai/wan/v2.2-a14b/text-to-video "a coffee pour, slow motion" out.mp4
#   ./fal-video.sh fal-ai/kling-video/v2/master/text-to-video "brand story shot" out.mp4 '{"duration":5}'
#
# Reads FAL_KEY from infra/fal/.env (gitignored). Prints status while polling,
# downloads the finished video to <output>. Exit non-zero on error/timeout.
# Depends on: curl, python (no jq needed).
#
# NOTE: video costs real money (~$0.05-0.20 per second). Always preflight the
# cost with the user before running this (see README.md model cheat-sheet).
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck disable=SC1091
set -a; source "$HERE/.env"; set +a

if [ -z "${FAL_KEY:-}" ] || [[ "$FAL_KEY" == key_PASTE* ]]; then
  echo "ERROR: FAL_KEY not set in $HERE/.env" >&2; exit 2
fi

MODEL="${1:?model-id required, e.g. fal-ai/wan/v2.2-a14b/text-to-video}"
PROMPT="${2:?prompt required}"
OUT="${3:?output path required}"
EXTRA="${4:-}"   # default handled in python (empty -> {})

PY="$(command -v python || command -v python3 || command -v py)"

BODY="$(FAL_PROMPT="$PROMPT" FAL_EXTRA="$EXTRA" "$PY" -c '
import json,os,sys
body={"prompt":os.environ["FAL_PROMPT"]}
try:
    body.update(json.loads(os.environ.get("FAL_EXTRA","") or "{}"))
except Exception as e:
    sys.stderr.write("bad extra-json: %s\n"%e); sys.exit(3)
print(json.dumps(body))
')"

# 1) submit to queue
SUB="$(curl -s -X POST "https://queue.fal.run/$MODEL" \
  -H "Authorization: Key $FAL_KEY" -H "Content-Type: application/json" -d "$BODY")"
REQ_ID="$(printf '%s' "$SUB" | "$PY" -c 'import json,sys;print(json.load(sys.stdin).get("request_id",""))' 2>/dev/null || true)"
if [ -z "$REQ_ID" ]; then
  echo "submit failed:" >&2; echo "$SUB" >&2; exit 1
fi
echo "submitted request_id=$REQ_ID  polling..."

# 2) poll status (up to ~10 min)
BASE="https://queue.fal.run/$MODEL"
for i in $(seq 1 120); do
  ST="$(curl -s "$BASE/requests/$REQ_ID/status" -H "Authorization: Key $FAL_KEY")"
  STATUS="$(printf '%s' "$ST" | "$PY" -c 'import json,sys;print(json.load(sys.stdin).get("status",""))' 2>/dev/null || true)"
  echo "  [$i] status=$STATUS"
  if [ "$STATUS" = "COMPLETED" ]; then break; fi
  if [ "$STATUS" = "" ]; then echo "$ST" >&2; fi
  sleep 5
done
if [ "$STATUS" != "COMPLETED" ]; then echo "timed out (last=$STATUS)" >&2; exit 1; fi

# 3) fetch result + download video
RES="$(curl -s "$BASE/requests/$REQ_ID" -H "Authorization: Key $FAL_KEY")"
URL="$(printf '%s' "$RES" | "$PY" -c '
import json,sys
d=json.load(sys.stdin)
u=(d.get("video") or {}).get("url") or (d.get("videos") or [{}])[0].get("url") or ""
print(u)
')"
if [ -z "$URL" ]; then echo "no video url:" >&2; echo "$RES" >&2; exit 1; fi

curl -s -o "$OUT" "$URL"
echo "OK  model=$MODEL  saved=$OUT"
echo "url=$URL"

# AUTO-LOG the spend (can't be forgotten — logging is a side-effect of spending).
# Caller labels it via env: FAL_BRAND / FAL_CAMPAIGN / FAL_ASSET / FAL_KEPT / FAL_NOTES.
# Set FAL_NOLOG=1 to skip (pure debugging only).
if [ -z "${FAL_NOLOG:-}" ]; then
  LOG_MODEL="$MODEL" LOG_SIZE="video" "$PY" "$HERE/_log.py" || echo "warn: ledger log failed" >&2
fi
