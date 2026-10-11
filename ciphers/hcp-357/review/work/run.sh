#!/bin/sh
# Reviewer checks for hcp-357, round 1. Run from anywhere; writes only under review/work/.
set -eu
cd "$(dirname "$0")"
rm -rf repro && mkdir repro
cp ../../work/transcription.txt ../../work/quadgrams.tsv ../../work/baseline.py ../../work/attack.cpp ../../work/multistage.cpp repro/
cd repro
python3 baseline.py > /dev/null
c++ -O3 -std=c++17 attack.cpp -o attack
c++ -O3 -std=c++17 multistage.cpp -o multistage
./attack . > results.txt
./attack . reverse > results-reverse.txt
./attack . normal cipher-full.txt > results-full.txt
./multistage . cipher.txt > multistage-results.txt
./multistage . cipher-full.txt > multistage-full-results.txt
echo "== reproduction of the solver's stored results"
for f in baseline.json cipher.txt cipher-full.txt results.txt results-reverse.txt results-full.txt multistage-results.txt multistage-full-results.txt; do
  cmp -s "$f" "../../../work/$f" && echo "IDENTICAL $f" || echo "DIFFERS   $f"
done
cd ..
echo "== planted-plaintext control"
python3 control.py
