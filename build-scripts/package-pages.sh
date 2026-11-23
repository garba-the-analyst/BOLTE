#!/usr/bin/env bash
# Package the GitHub Pages bundle from website/. The site is self-contained
# (fonts, logos and styles all live under website/assets), so this only copies
# the folder and strips internal documentation.
# Usage: ./build-scripts/package-pages.sh [out-dir]   (default: <root>/_pages)
# Preview: python3 -m http.server -d _pages 8080
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="${1:-$ROOT/_pages}"
rm -rf "$OUT"
mkdir -p "$OUT"
cp -r "$ROOT/website/." "$OUT/"
rm -f "$OUT/FUNCTIONAL-SPEC.md" "$OUT/README.md"
touch "$OUT/.nojekyll"
echo "Pages bundle ready: $OUT"
du -sh "$OUT"
