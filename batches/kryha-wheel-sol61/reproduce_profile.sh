#!/bin/sh
set -eu
TASK_DIR=batches/kryha-wheel-sol61
# Existing geometry, controls and baseline IC results are inputs; do not rerun them.
python3 "$TASK_DIR/profile_diagnostic.py"
c++ -O3 -std=c++17 "$TASK_DIR/wheel_mask_profile.cpp" -o "$TASK_DIR/wheel_mask_profile"
"$TASK_DIR/wheel_mask_profile" "$TASK_DIR/control-m26/ciphertext.txt" "$TASK_DIR/adjacent-distances.txt" 26 100 "$TASK_DIR/unigram-sorted-logprobs.txt" > "$TASK_DIR/control-m26/profile-mask-candidates.txt"
"$TASK_DIR/wheel_masc" "$TASK_DIR" "$TASK_DIR/control-m26/ciphertext.txt" "$TASK_DIR/adjacent-distances.txt" "$TASK_DIR/control-m26/profile-mask-candidates.txt" > "$TASK_DIR/control-m26/profile-masc-results.txt"
python3 "$TASK_DIR/calibrate_profile_pilot.py"
"$TASK_DIR/wheel_joint" "$TASK_DIR" "$TASK_DIR/control-m26/ciphertext.txt" "$TASK_DIR/adjacent-distances.txt" "$TASK_DIR/control-m26/profile-joint-seed.txt" 26 > "$TASK_DIR/control-m26/profile-joint-result.txt"
python3 "$TASK_DIR/verify_profile_joint.py"
