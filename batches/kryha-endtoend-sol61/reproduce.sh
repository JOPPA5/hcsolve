#!/bin/sh
set -eu
cd "$(dirname "$0")/../.."
b=batches/kryha-endtoend-sol61
for name in fit_dp enumerate-profile masc rerank path-full; do
 clang++ -O3 -std=c++17 "$b/$name.cpp" -o "$b/$name"
done
python3 "$b/generate.py"
python3 "$b/ransac.py" "$b/pilot-pair.json" "$b/pilot-ransac.json"
python3 "$b/run.py"
python3 "$b/refine.py"
python3 "$b/save_ranked.py"
python3 "$b/audit.py"
python3 "$b/second-generate.py"
python3 "$b/ransac.py" "$b/second-pair.json" "$b/second-ransac.json"
python3 "$b/second-run.py"
python3 "$b/second-refine.py"
python3 "$b/second-save_ranked.py"
python3 "$b/second-audit.py"
