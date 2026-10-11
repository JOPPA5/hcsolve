#!/bin/sh
set -eu
TASK_DIR=batches/kryha-wheel-sol61
python3 "$TASK_DIR/verify_geometry.py"
python3 "$TASK_DIR/build_controls.py"
for program in wheel_mask_ic wheel_masc wheel_joint; do
 c++ -std=c++17 -O3 "$TASK_DIR/$program.cpp" -o "$TASK_DIR/$program"
done
python3 "$TASK_DIR/run_known_output_controls.py"
"$TASK_DIR/wheel_mask_ic" "$TASK_DIR/control-m26/ciphertext.txt" "$TASK_DIR/adjacent-distances.txt" 26 100 > "$TASK_DIR/control-m26/ic-mask-candidates.txt"
"$TASK_DIR/wheel_masc" "$TASK_DIR" "$TASK_DIR/control-m26/ciphertext.txt" "$TASK_DIR/adjacent-distances.txt" "$TASK_DIR/control-m26/ic-mask-candidates.txt" > "$TASK_DIR/control-m26/masc-results.txt"
python3 "$TASK_DIR/calibrate_pilot.py"
"$TASK_DIR/wheel_joint" "$TASK_DIR" "$TASK_DIR/control-m26/ciphertext.txt" "$TASK_DIR/adjacent-distances.txt" "$TASK_DIR/control-m26/joint-seed.txt" 26 > "$TASK_DIR/control-m26/joint-result.txt"
python3 "$TASK_DIR/verify_joint.py"
