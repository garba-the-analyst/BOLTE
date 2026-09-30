#!/usr/bin/env bash
# Package a self-contained GitHub Pages bundle from website/ + shared assets.
# The repo serves the site from website/ with ../assets/... links; Pages only
# uploads one folder, so vendor the needed assets and rewrite the links.
# Usage: ./build-scripts/package-pages.sh [out-dir]   (default: <root>/_pages)
# Preview: python3 -m http.server -d _pages 8080
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="${1:-$ROOT/_pages}"
rm -rf "$OUT"
mkdir -p "$OUT"
cp -r "$ROOT/website/." "$OUT/"
rm -f "$OUT/FUNCTIONAL-SPEC.md" "$OUT/README.md"
mkdir -p "$OUT/vendor" "$OUT/forms" "$OUT/vendor/hfp"
cp -r "$ROOT/assets/logo-placeholder" "$ROOT/assets/animations" "$OUT/vendor/"
cp "$ROOT/projects/BOLTE HFP/HFP-X blueprints/dark-DWG-002.png" "$OUT/vendor/hfp/"
cp -r "$ROOT/forms/." "$OUT/forms/"
grep -rl '\.\./assets/' "$OUT" --include='*.html' | xargs sed -i 's|\.\./assets/|./vendor/|g'
grep -rl 'projects/BOLTE%20HFP' "$OUT" --include='*.html' | xargs sed -i 's|\.\./projects/BOLTE%20HFP/HFP-X%20blueprints/|./vendor/hfp/|g'
grep -rl '\.\./forms/' "$OUT" --include='*.html' | xargs sed -i 's|\.\./forms/|./forms/|g'
sed -i 's|\.\./\.\./\.\./assets/|../../vendor/|g' "$OUT/assets/css/site.css"
echo "Pages bundle ready: $OUT"
du -sh "$OUT"
