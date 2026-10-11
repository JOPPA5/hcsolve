#!/bin/sh
set -eu
cd "$(dirname "$0")/../.."
python3 batches/scoring-sol61/build.py
python3 batches/scoring-sol61/build-pos.py
python3 batches/scoring-sol61/build-frequency.py
python3 batches/scoring-sol61/build-core.py
ln -sf ../words-pos.tsv batches/scoring-sol61/frequency/words-pos.tsv
ln -sf ../pos-transitions.tsv batches/scoring-sol61/frequency/pos-transitions.tsv
for scorer in mono mono-longword mono-pos mono-seeded mono-pos-seeded mono-frequency mono-frequency-seeded mono-frequency-strict mono-frequency-seeded-strict; do
  c++ -O3 -std=c++17 "batches/scoring-sol61/$scorer.cpp" -o "batches/scoring-sol61/$scorer"
done
python3 batches/scoring-sol61/wordseeds-small.py ciphers/hcp-332/work/mono-control.txt batches/scoring-sol61/control43-small-seeds
batches/scoring-sol61/mono-pos-seeded batches/scoring-sol61 ciphers/hcp-332/work/mono-control.txt batches/scoring-sol61/control43-small-seeds.txt > batches/scoring-sol61/control43-pos-result.txt 2> batches/scoring-sol61/control43-pos-progress.txt
python3 batches/scoring-sol61/wordseeds-small.py batches/scoring-sol61/holdout43-cipher.txt batches/scoring-sol61/holdout43-seeds
batches/scoring-sol61/mono-pos-seeded batches/scoring-sol61 batches/scoring-sol61/holdout43-cipher.txt batches/scoring-sol61/holdout43-seeds.txt > batches/scoring-sol61/holdout43-result.txt 2> batches/scoring-sol61/holdout43-progress.txt
for variant in o-40 d-40 o-43 d-43; do
  python3 batches/scoring-sol61/wordseeds-core.py "ciphers/hcp-332/work/target-$variant.txt" "ciphers/hcp-332/work/strong-$variant-seeds"
  batches/scoring-sol61/mono-pos-seeded batches/scoring-sol61 "ciphers/hcp-332/work/target-$variant.txt" "ciphers/hcp-332/work/strong-$variant-seeds.txt" > "ciphers/hcp-332/work/strong-pos-$variant-result.txt" 2> "ciphers/hcp-332/work/strong-pos-$variant-progress.txt"
done
