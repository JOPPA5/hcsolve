#!/bin/sh
set -eu
cd /Users/tomaspavuk/Desktop/hcsolve
B=batches/kryha-two-mask-language-sol61
clang++ -O3 -std=c++17 "$B/count.cpp" -o "$B/count"
clang++ -O3 -std=c++17 "$B/enumerate-profile.cpp" -o "$B/enumerate-profile"
clang++ -O3 -std=c++17 "$B/masc.cpp" -o "$B/masc"
python3 "$B/generate-control.py"
python3 "$B/run-profile.py" "$B/control-input.json" control-profile.txt
python3 "$B/project.py" "$B/control-input.json" control-profile.txt control-projected.txt 10
"$B/masc" "$B/dummy-pair.txt" "$B/zero-schedule.txt" batches/kryha-mask-sol61 ciphers/hcp-350/work "$B/control-projected.txt" > "$B/control-masc.txt"
python3 "$B/neighbors.py" "$B/control-input.json" control-masc.txt control-projected.txt control-neighbors.json
python3 "$B/verify-control.py"
python3 "$B/actual-profiles.py"
python3 "$B/actual-masc.py"
python3 "$B/full-candidates.py"
