#!/bin/sh
set -eu
cd "$(dirname "$0")/../../.."
p=ciphers/hcp-334/work
python3 "$p/prepare-controls.py"
python3 "$p/phase.py" > "$p/phase-results.txt"
python3 "$p/diagnostics.py" > "$p/diagnostics-compact.txt"
python3 "$p/damage-control.py" > "$p/damage-control.json"
c++ -O3 -std=c++17 "$p/vigenere-erasures.cpp" -o "$p/vigenere-erasures"
"$p/vigenere-erasures" "$p" "$p/control-vig-cipher.txt" > "$p/control-vig-results.txt"
"$p/vigenere-erasures" "$p" "$p/control-vig15-cipher.txt" > "$p/control-vig15-results.txt"
python3 "$p/control-report.py" > "$p/control-report.json"
python3 "$p/run-target.py" > "$p/target-progress.txt"
