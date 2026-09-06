#!/usr/bin/env bash
# fal.ai storage upload helper — gets a PUBLIC URL for a LOCAL file without generating anything.
# Usage: ./fal-upload.sh <local-file>
# Prints the public URL on the last line.
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
set -a; source "$HERE/.env"; set +a

FILE="${1:?local file path required}"
[ -f "$FILE" ] || { echo "ERROR: file not found: $FILE" >&2; exit 2; }

CT="image/png"
case "$FILE" in
  *.jpg|*.jpeg) CT="image/jpeg" ;;
esac
NAME="$(basename "$FILE")"
PY="$(command -v python || command -v python3 || command -v py)"

INIT="$(curl -s -X POST "https://rest.alpha.fal.ai/storage/upload/initiate?content_type=$CT&file_name=$NAME" \
  -H "Authorization: Key $FAL_KEY")"

UPLOAD_URL="$(printf '%s' "$INIT" | "$PY" -c 'import json,sys;print(json.load(sys.stdin)["upload_url"])')"
FILE_URL="$(printf '%s' "$INIT" | "$PY" -c 'import json,sys;print(json.load(sys.stdin)["file_url"])')"

curl -s -X PUT "$UPLOAD_URL" -H "Content-Type: $CT" --data-binary "@$FILE" -o /dev/null

echo "$FILE_URL"
