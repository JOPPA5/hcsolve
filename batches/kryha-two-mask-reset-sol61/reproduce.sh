#!/bin/sh
set -eu
cd /Users/tomaspavuk/Desktop/hcsolve
B=batches/kryha-two-mask-reset-sol61
clang++ -O3 -std=c++17 "$B/enumerate-profile.cpp" -o "$B/enumerate-profile"
clang++ -O3 -std=c++17 "$B/enumerate-language.cpp" -o "$B/enumerate-language"
clang++ -O3 -std=c++17 "$B/masc.cpp" -o "$B/masc"
python3 "$B/generate-control.py"
# Preserve the original failed pooling heuristic and its blind language seed.
python3 "$B/run-profile-original.py" "$B/control-input.json" control-profile.txt
python3 "$B/project.py" "$B/control-input.json" control-profile.txt control-projected.txt 10
"$B/masc" "$B/dummy-pair.txt" "$B/zero-schedule.txt" batches/kryha-mask-sol61 ciphers/hcp-350/work "$B/control-projected.txt" > "$B/control-masc.txt"
python3 "$B/neighbors.py" "$B/control-input.json" control-masc.txt control-projected.txt control-neighbors.json
python3 "$B/refine-control.py"
python3 "$B/verify-control.py" control-refine2
python3 "$B/run-profile.py" "$B/control-input.json" control-corrected-profile.txt
python3 "$B/project.py" "$B/control-input.json" control-corrected-profile.txt control-corrected-projected.txt 10
"$B/masc" "$B/dummy-pair.txt" "$B/zero-schedule.txt" batches/kryha-mask-sol61 ciphers/hcp-350/work "$B/control-corrected-projected.txt" > "$B/control-corrected-masc.txt"
python3 "$B/neighbors.py" "$B/control-input.json" control-corrected-masc.txt control-corrected-projected.txt control-corrected-neighbors.json
python3 "$B/actual-profiles.py"
python3 "$B/actual-masc.py"
python3 "$B/full-candidates.py"
clang++ -O3 -std=c++17 "$B/path-refine.cpp" -o "$B/path-refine"
clang++ -O3 -std=c++17 "$B/masc-warm.cpp" -o "$B/masc-warm"
clang++ -O3 -std=c++17 "$B/rerank.cpp" -o "$B/rerank"
python3 "$B/run-warm.py" control
python3 "$B/verify-control.py" control-warm
python3 "$B/run-warm.py" pixel-strong-row5
python3 "$B/run-warm.py" pixel-strong-plus-moderate-row5
python3 "$B/warm-full-candidates.py"
python3 "$B/warm-best-full.py"
