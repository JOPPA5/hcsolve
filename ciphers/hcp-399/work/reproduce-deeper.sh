#!/bin/sh
set -eu
cd "$(dirname "$0")/../../.."
p=ciphers/hcp-399/work
python3 "$p/controls.py"
c++ -O3 -std=c++17 "$p/multistage.cpp" -o "$p/multistage"
c++ -O3 -std=c++17 "$p/verify-known.cpp" -o "$p/verify-known"
python3 "$p/verify-known.py" > "$p/known-key-verification.txt"
"$p/multistage" "$p/quadgrams.tsv" "$p/control-240-1stage.txt" 30 30000 19 0 > "$p/control-240-1stage-result.txt"
"$p/multistage" "$p/quadgrams.tsv" "$p/control-245-1stage.txt" 30 30000 19 0 > "$p/control-245-1stage-result.txt"
"$p/multistage" "$p/quadgrams.tsv" "$p/control-245-1stage.txt" 200 100000 19 0 > "$p/control-245-1stage-extended-result.txt"
"$p/multistage" "$p/quadgrams.tsv" "$p/control-240-2stage.txt" 30 30000 19 17 > "$p/control-240-2stage-result.txt"
"$p/multistage" "$p/quadgrams.tsv" "$p/control-240-3stage.txt" 30 30000 19 17 22 > "$p/control-240-3stage-result.txt"
python3 "$p/control-report.py" > "$p/control-report.json"
python3 "$p/indicator.py" > "$p/indicator-results.txt"
python3 "$p/indicator-v2.py" > "$p/indicator-v2-results.txt"
python3 "$p/sweep.py" > "$p/sweep-progress.txt"
python3 "$p/sweep-v2.py" > "$p/sweep-v2-progress.txt"
