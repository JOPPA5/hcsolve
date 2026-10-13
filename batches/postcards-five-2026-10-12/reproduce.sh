#!/bin/sh
set -eu
cd "$(dirname "$0")/../.."
TASK_DIR=batches/postcards-five-2026-10-12
python3 "$TASK_DIR/prepare.py"
clang++ -O3 -std=c++17 "$TASK_DIR/mono.cpp" -o "$TASK_DIR/mono"
"$TASK_DIR/mono" "$TASK_DIR/models/hu" "$TASK_DIR/control.txt" 40 30000 9171243 > "$TASK_DIR/control-result.txt"
for TASK_CIPHER in 1243 1301 917; do
  "$TASK_DIR/mono" "$TASK_DIR/models/hu" "ciphers/hcp-$TASK_CIPHER/work/scout.txt" 40 30000 9171243 > "ciphers/hcp-$TASK_CIPHER/work/scout-hu-result.txt"
done
"$TASK_DIR/mono" batches/scoring-sol61/german ciphers/hcp-917/work/scout.txt 40 30000 9171244 > ciphers/hcp-917/work/scout-de-result.txt
"$TASK_DIR/mono" "$TASK_DIR/models/hu" ciphers/hcp-917/work/scout-body.txt 40 30000 9171245 > ciphers/hcp-917/work/scout-body-hu-result.txt
"$TASK_DIR/mono" "$TASK_DIR/models/hu" ciphers/hcp-917/work/scout-reverse.txt 40 30000 9171246 > ciphers/hcp-917/work/scout-reverse-hu-result.txt
python3 ciphers/hcp-975/work/decode.py
python3 ciphers/hcp-1000/work/decode-fragment.py
