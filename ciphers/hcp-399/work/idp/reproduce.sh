#!/bin/sh
set -eu
cd "$(dirname "$0")/../../../.."
w=ciphers/hcp-399/work/idp
out="$w/reproduced"
mkdir -p "$out"
python3 "$w/controls.py"
python3 "$w/w16-controls.py"
for name in idp idp-physical single refine trigram-beam multigram-beam multigram-beam-v2; do
 clang++ -O3 -std=c++17 "$w/$name.cpp" -o "$w/$name"
done
python3 "$w/reference.py"
for label in authored-240 heldout-240 authored-245 heldout-245; do
 "$w/idp-physical" ciphers/hcp-363/work/segmented/bigrams.tsv "$w/$label.txt" 20 17 4000 > "$out/$label.physical-results.txt" 2> "$out/$label.physical-progress.txt"
 "$w/single" batches/scoring-sol61 ciphers/hcp-363/work/segmented/bigrams.tsv "$w/$label.true-middle.txt" 20 > "$out/$label.true-middle.single-results.txt" 2> "$out/$label.true-middle.single-progress.txt"
done
python3 "$w/pipeline.py" reproduced > "$out/pipeline-progress.txt"
for label in authored-240 heldout-240; do
 "$w/multigram-beam-v2" batches/scoring-sol61 "$w/$label.true-middle.txt" 20 17 score > "$out/$label.multigram-v2b16-true-middle.txt"
 "$w/multigram-beam-v2" batches/scoring-sol61 "$w/$label.txt" 20 17 80 "$out/$label.physical-results.txt" > "$out/$label.multigram-v2-results.txt" 2> "$out/$label.multigram-v2-progress.txt"
done
