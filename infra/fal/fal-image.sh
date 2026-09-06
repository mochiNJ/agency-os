#!/usr/bin/env bash
# fal.ai image generation helper (direct-API — no MCP settings file touched).
# Usage:
#   ./fal-image.sh <model-id> "<prompt>" <output.png> [image_size] [extra-json]
#
# Examples:
#   ./fal-image.sh fal-ai/flux/schnell "a red coffee cherry" out.jpg square
#   ./fal-image.sh fal-ai/flux/dev "brand hero, cinematic" hero.jpg landscape_16_9
#   ./fal-image.sh fal-ai/flux-pro/v1.1 "poster" p.jpg square_hd '{"num_images":1}'
#
# image_size options (fal): square, square_hd, portrait_4_3, portrait_16_9,
#                           landscape_4_3, landscape_16_9   (default: square_hd)
# You can also pass exact pixels via extra-json, e.g. '{"image_size":{"width":1080,"height":1350}}'
#
# Reads FAL_KEY from infra/fal/.env (gitignored). Downloads the first image to
# <output> and prints the result URL. Exit non-zero on any HTTP error.
# Depends on: curl, python (no jq needed).
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck disable=SC1091
set -a; source "$HERE/.env"; set +a

if [ -z "${FAL_KEY:-}" ] || [[ "$FAL_KEY" == key_PASTE* ]]; then
  echo "ERROR: FAL_KEY not set in $HERE/.env" >&2; exit 2
fi

MODEL="${1:?model-id required, e.g. fal-ai/flux/schnell}"
PROMPT="${2:?prompt required}"
OUT="${3:?output path required}"
SIZE="${4:-square_hd}"
EXTRA="${5:-}"   # default handled in python (empty -> {}); avoid ${5:-{}} brace trap

PY="$(command -v python || command -v python3 || command -v py)"

# Build request body with python (handles escaping + merges extra JSON).
# Values are passed via env vars (not argv) to avoid Windows-native arg mangling.
BODY="$(FAL_PROMPT="$PROMPT" FAL_SIZE="$SIZE" FAL_EXTRA="$EXTRA" "$PY" -c '
import json,os,sys
body={"prompt":os.environ["FAL_PROMPT"],"image_size":os.environ["FAL_SIZE"]}
try:
    body.update(json.loads(os.environ.get("FAL_EXTRA","{}") or "{}"))
except Exception as e:
    sys.stderr.write("bad extra-json: %s\n"%e); sys.exit(3)
print(json.dumps(body))
')"

RESP="$(curl -s -w $'\n%{http_code}' -X POST "https://fal.run/$MODEL" \
  -H "Authorization: Key $FAL_KEY" -H "Content-Type: application/json" \
  -d "$BODY")"

CODE="$(printf '%s' "$RESP" | tail -n1)"
JSON="$(printf '%s' "$RESP" | sed '$d')"

if [ "$CODE" != "200" ]; then
  echo "fal HTTP $CODE" >&2; echo "$JSON" >&2; exit 1
fi

URL="$(printf '%s' "$JSON" | "$PY" -c '
import json,sys
d=json.load(sys.stdin)
u=(d.get("images") or [{}])[0].get("url") or (d.get("image") or {}).get("url") or ""
print(u)
')"

if [ -z "$URL" ]; then
  echo "No image URL in response:" >&2; echo "$JSON" >&2; exit 1
fi

curl -s -o "$OUT" "$URL"
echo "OK  model=$MODEL  size=$SIZE  saved=$OUT"
echo "url=$URL"

# AUTO-LOG the spend (can't be forgotten — logging is a side-effect of spending).
# Caller labels it via env: FAL_BRAND / FAL_CAMPAIGN / FAL_ASSET / FAL_KEPT / FAL_NOTES.
# Set FAL_NOLOG=1 to skip (pure debugging only).
if [ -z "${FAL_NOLOG:-}" ]; then
  LOG_MODEL="$MODEL" LOG_SIZE="$SIZE" "$PY" "$HERE/_log.py" || echo "warn: ledger log failed" >&2
fi
