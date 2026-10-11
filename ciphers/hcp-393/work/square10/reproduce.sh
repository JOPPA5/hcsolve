#!/bin/sh
set -eu
cd "$(dirname "$0")/../../../.."
w=ciphers/hcp-393/work/square10
out="$w/reproduced"
mkdir -p "$out"
python3 "$w/controls.py"
python3 "$w/build-phrases.py"
for model in search search-phrase; do
 clang++ -O3 -std=c++17 "$w/$model.cpp" -o "$out/$model"
 for label in heldout-0 heldout-1 authored-0 authored-1 target; do
  input="$w/$label.txt"
  if [ "$label" = target ]; then input=ciphers/hcp-393/work/cipher.txt; fi
  "$out/$model" batches/scoring-sol61 ciphers/hcp-363/work/segmented/bigrams.tsv "$input" "$w" > "$out/$label.$model.txt" 2> "$out/$label.$model.progress.txt"
 done
done
python3 "$w/triple-control.py"
clang++ -O3 -std=c++17 "$w/search-wide.cpp" -o "$out/search-wide"
for label in target target-transposed triple-control-transposed; do
 input="$w/$label.txt"
 if [ "$label" = target ]; then input=ciphers/hcp-393/work/cipher.txt; fi
 "$out/search-wide" batches/scoring-sol61 ciphers/hcp-363/work/segmented/bigrams.tsv "$input" "$w" > "$out/$label.search-wide.txt" 2> "$out/$label.search-wide.progress.txt"
done
