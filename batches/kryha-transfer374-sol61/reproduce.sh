#!/bin/sh
set -eu
cd "$(dirname "$0")/../.."
b=batches/kryha-transfer374-sol61
clang++ -O3 -std=c++17 "$b/beam.cpp" -o "$b/beam"
clang++ -O3 -std=c++17 "$b/beam-v2.cpp" -o "$b/beam-v2"
clang++ -O3 -std=c++17 "$b/beam-jdelimiter.cpp" -o "$b/beam-jdelimiter"
python3 "$b/prepare.py"
for n in 0 1; do
 "$b/beam" "$b/known-rings-coordinates.txt" "$b/control$n.txt" 23 128 "$PWD" "$b/control$n-beam128.txt"
done
python3 "$b/run.py"
python3 "$b/count-controls.py"
python3 "$b/run-counts.py"
python3 "$b/count-controls-v2.py"
python3 "$b/prepare-j.py"
for n in 0 1; do
 "$b/beam-jdelimiter" "$b/known-rings-coordinates.txt" "$b/control-j$n.txt" 23 128 "$PWD" "$b/control-j$n-beam128.txt"
done
python3 "$b/run-j.py"
python3 "$b/verify-planted.py"

clang++ -O3 -std=c++17 "$b/beam-direction.cpp" -o "$b/beam-direction"
python3 "$b/direction.py"
