#!/bin/sh
set -eu
cd "$(dirname "$0")/../.."
b=batches/kryha-transfer373-sol61
clang++ -O3 -std=c++17 "$b/beam.cpp" -o "$b/beam"
clang++ -O3 -std=c++17 "$b/beam-direction.cpp" -o "$b/beam-direction"
python3 "$b/prepare.py"
for n in 0 1; do
 "$b/beam" "$b/known-rings-coordinates.txt" "$b/control$n.txt" 23 128 "$PWD" "$b/control$n-beam128.txt"
done
python3 "$b/verify-initial.py"
"$b/beam" "$b/known-rings-coordinates.txt" "$b/target650.txt" 23 128 "$PWD" "$b/target650-beam128.txt"
python3 "$b/experiments.py"

python3 "$b/latest-variant.py"
