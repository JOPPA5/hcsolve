#!/bin/sh
set -eu
TASK_DIR=ciphers/hcp-351/work
c++ -std=c++17 -O3 "$TASK_DIR/selective_j_known_output_five.cpp" -o "$TASK_DIR/selective_j_known_output_five"
"$TASK_DIR/selective_j_known_output_five" "$TASK_DIR" "$TASK_DIR/selective-j-control-cipher.txt" 11 1 "$TASK_DIR/selective-j-control-output.txt" > "$TASK_DIR/selective-j-known-output-five-result.txt"
python3 "$TASK_DIR/verify_selective_j_control.py"
for variant in selective_j_ic selective_j_beam selective_j_beam_renewal selective_j_path_beam; do
 c++ -std=c++17 -O3 "$TASK_DIR/$variant.cpp" -o "$TASK_DIR/$variant"
done
"$TASK_DIR/selective_j_ic" "$TASK_DIR/selective-j-control-cipher.txt" 11 1 100 > "$TASK_DIR/selective-j-control-ic100.txt"
"$TASK_DIR/selective_j_beam" "$TASK_DIR/selective-j-control-cipher.txt" "$TASK_DIR/selective-j-unigram-weights.txt" 10000 11 > "$TASK_DIR/selective-j-control-beam10000.txt"
"$TASK_DIR/selective_j_beam_renewal" "$TASK_DIR/selective-j-control-cipher.txt" "$TASK_DIR/selective-j-renewal-weights.txt" 10000 11 > "$TASK_DIR/selective-j-control-beam-renewal10000.txt"
"$TASK_DIR/selective_j_path_beam" "$TASK_DIR/selective-j-control-cipher.txt" "$TASK_DIR/selective-j-renewal-weights.txt" 1000 11 > "$TASK_DIR/selective-j-control-pathbeam1000.txt"
for name in ic100 beam10000 beam-renewal10000 pathbeam1000; do
 "$TASK_DIR/selective_j_known_output_five" "$TASK_DIR" "$TASK_DIR/selective-j-control-cipher.txt" 11 1 "$TASK_DIR/selective-j-control-$name.txt" > "$TASK_DIR/selective-j-control-$name-masc.txt"
done
