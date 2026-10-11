#!/bin/sh
set -eu
cd /Users/tomaspavuk/Desktop/hcsolve
B=batches/kryha-forensic-sol61
clang++ -O3 -std=c++17 "$B/rerank.cpp" -o "$B/rerank"
python3 "$B/prepare.py"
"$B/rerank" batches/kryha-two-mask-refine-sol61 "$B/projected.txt" "$B/seed.txt" > "$B/generic325.txt"
"$B/rerank" batches/kryha-two-mask-refine-sol61 "$B/projected.txt" "$B/rare120-seeds.txt" > "$B/rare120-plus325.txt"
python3 "$B/audit.py"
