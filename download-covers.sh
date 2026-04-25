#!/bin/bash
# Download real book cover images for connorrobertsonbooks.com
# Run this script from the repo root: bash download-covers.sh

set -e
mkdir -p images/covers

echo "Downloading book covers..."

# 1. Buying Wealth - from Google Books (high-res)
echo "  -> Buying Wealth..."
curl -L -o images/covers/buying-wealth-cover.jpg \
  "https://books.google.com/books/content?id=Dw2HEQAAQBAJ&printsec=frontcover&img=1&zoom=3" 2>/dev/null \
  || curl -L -o images/covers/buying-wealth-cover.jpg \
  "https://books.google.com/books/content?id=Dw2HEQAAQBAJ&printsec=frontcover&img=1&zoom=1" 2>/dev/null \
  || curl -L -o images/covers/buying-wealth-cover.jpg \
  "https://www.drconnorrobertson.com/wp-content/uploads/2025/11/Buying-Wealth-by-Dr-Connor-Robertson-1.jpeg" 2>/dev/null

# 2. Creative Acquisitions - from author website
echo "  -> Creative Acquisitions..."
curl -L -o images/covers/creative-acquisitions-cover.png \
  "https://www.drconnorrobertson.com/wp-content/uploads/2026/02/Creative-Acquisitions-The-Playbook-for-Modern-Dealmakers-By-Dr.-Connor-Robertson-scaled.png" 2>/dev/null

# 3. The 7 Minute Phone Call - from author website
echo "  -> The 7 Minute Phone Call..."
curl -L -o images/covers/the-7-minute-phone-call-cover.jpg \
  "https://www.drconnorrobertson.com/wp-content/uploads/2025/11/the-7-minute-phone-call-with-dr-connor-robertson-1.jpeg" 2>/dev/null

# 4. Built to Run - search multiple sources
echo "  -> Built to Run..."
# Try Google Books search first
BUILT_ID=$(curl -s "https://www.googleapis.com/books/v1/volumes?q=intitle:Built+to+Run+inauthor:connor+robertson" 2>/dev/null | python3 -c "
import sys, json
try:
    data = json.load(sys.stdin)
    if data.get('totalItems', 0) > 0:
        print(data['items'][0]['id'])
except: pass
" 2>/dev/null)

if [ -n "$BUILT_ID" ]; then
  curl -L -o images/covers/built-to-run-cover.jpg \
    "https://books.google.com/books/content?id=${BUILT_ID}&printsec=frontcover&img=1&zoom=3" 2>/dev/null
fi

# If no cover found for Built to Run, try drconnorrobertson.com
if [ ! -s images/covers/built-to-run-cover.jpg ]; then
  # Try to find it on the author's website
  curl -L -o images/covers/built-to-run-cover.jpg \
    "https://www.drconnorrobertson.com/wp-content/uploads/2026/02/Built-to-Run-By-Dr.-Connor-Robertson-scaled.png" 2>/dev/null || true
fi

# Verify downloads
echo ""
echo "Download results:"
for f in images/covers/*-cover.*; do
  if [ -s "$f" ]; then
    SIZE=$(wc -c < "$f")
    echo "  OK: $f ($SIZE bytes)"
  else
    echo "  MISSING: $f (empty or failed)"
    rm -f "$f"
  fi
done

echo ""
echo "Done! Now commit and push:"
echo "  git add images/covers/"
echo "  git commit -m 'Add real book cover images'"
echo "  git push"
