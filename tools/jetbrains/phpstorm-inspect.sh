#!/usr/bin/env bash
# Usage: phpstorm-inspect.sh <project-dir> [-changes | -d <dir>]
set -euo pipefail

DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT="$(cd "${1:?Usage: phpstorm-inspect.sh <project-dir> [-changes | -d <dir>]}" && pwd)"
shift

INSPECT="${PHPSTORM_INSPECT:-$(ls -d "/c/Program Files/JetBrains/PhpStorm"*/bin/inspect.bat "${LOCALAPPDATA:-/none}"/Programs/PhpStorm*/bin/inspect.bat \
  /Applications/PhpStorm*.app/Contents/bin/inspect.sh "$HOME"/Applications/PhpStorm*.app/Contents/bin/inspect.sh 2>/dev/null | sort -V | tail -1 || true)}"
[ -n "$INSPECT" ] || { echo "Không tìm thấy PhpStorm, set PHPSTORM_INSPECT=<đường dẫn bin/inspect.bat hoặc inspect.sh>" >&2; exit 127; }
KEY="$(ls "${APPDATA:-/none}"/JetBrains/PhpStorm*/phpstorm.key "$HOME/Library/Application Support/JetBrains"/PhpStorm*/phpstorm.key 2>/dev/null | sort -V | tail -1 || true)"
PY="$(command -v python || command -v python3)"
PROFILE="${INSPECT_PROFILE:-$DIR/language-inspection.xml}"

winpath() { if command -v cygpath >/dev/null; then cygpath "$1" "$2"; else echo "$2"; fi; }

# Separate config/system dirs so inspect can run while the IDE is open; license key is copied over
HOME_DIR="${PHPSTORM_INSPECT_HOME:-$HOME/.cache/phpstorm-inspect}"
mkdir -p "$HOME_DIR/config"
if [ -n "$KEY" ]; then cp "$KEY" "$HOME_DIR/config/"; else echo "Cảnh báo: không thấy phpstorm.key, PhpStorm có thể đòi license" >&2; fi
H="$(winpath -m "$HOME_DIR")"
printf 'idea.config.path=%s/config\nidea.system.path=%s/system\nidea.plugins.path=%s/config/plugins\nidea.log.path=%s/log\n' "$H" "$H" "$H" "$H" > "$HOME_DIR/idea.properties"

OUT="${TMPDIR:-/tmp}/phpstorm-inspect/$(basename "$PROJECT")"
rm -rf "$OUT" && mkdir -p "$OUT"
had_idea=0; [ -d "$PROJECT/.idea" ] && had_idea=1

PHPSTORM_PROPERTIES="$(winpath -w "$HOME_DIR/idea.properties")" \
  "$INSPECT" "$(winpath -w "$PROJECT")" "$(winpath -w "$PROFILE")" "$(winpath -w "$OUT")" -v0 -format json "$@"

[ "$had_idea" = 1 ] || rm -rf "$PROJECT/.idea"
"$PY" "$DIR/inspect-summary.py" "$OUT" "$PROJECT"
