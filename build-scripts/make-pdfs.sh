#!/usr/bin/env bash
# Generate PDFs for every Markdown doc in BOLTE using pandoc (md->HTML) + Chrome headless (HTML->PDF).
set -euo pipefail
ROOT="/home/garba-the-analyst/Desktop/Projects/BOLTE"
CSS="$ROOT/build-scripts/pdf-style.css"
OUTROOT="$ROOT/pdf"
TMPDIR=$(mktemp -d)
trap 'rm -rf "$TMPDIR"' EXIT
mkdir -p "$OUTROOT"
count=0; failed=0
while IFS= read -r -d '' md; do
  rel="${md#$ROOT/}"
  out="$OUTROOT/${rel%.md}.pdf"
  mkdir -p "$(dirname "$out")"
  html="$TMPDIR/doc.html"
  title=$(basename "${md%.md}")
  pandoc "$md" -f markdown -t html5 --standalone \
    --metadata title="$title" \
    --css "$CSS" \
    -V margin-top=20mm -V margin-bottom=22mm \
    -o "$html"
  # Inject BOLTE header/footer + link CSS inline for print
  python3 - "$html" "$CSS" <<'EOF'
import sys
html_path, css_path = sys.argv[1], sys.argv[2]
css = open(css_path).read()
h = open(html_path).read()
banner = '<div class="pdf-header"><span class="brand">BOLTE</span><span class="sub">Indigenous Technology for Nigeria &amp; Africa</span></div>'
footer = '<div class="pdf-footer"><span>BOLTE Corporate Documentation — template/draft (requires review where noted)</span><span>NASS Rulebook takes precedence for competition matters</span></div>'
h = h.replace('</head>', '<style>' + css + '</style></head>', 1)
h = h.replace('<body>', '<body>' + banner, 1)
h = h.replace('</body>', footer + '</body>', 1)
open(html_path, 'w').write(h)
EOF
  if google-chrome --headless --no-sandbox --disable-gpu --print-to-pdf="$out" --print-to-pdf-no-header "$html" >/dev/null 2>&1; then
    echo "OK  $rel -> ${out#$ROOT/}"
    count=$((count+1))
  else
    echo "FAIL $rel"; failed=$((failed+1))
  fi
done < <(find "$ROOT/docs" "$ROOT/README.md" "$ROOT/CHANGELOG.md" -name '*.md' -print0 | sort -z)
echo "---"
echo "Generated: $count PDFs, failed: $failed. Output: $OUTROOT"
