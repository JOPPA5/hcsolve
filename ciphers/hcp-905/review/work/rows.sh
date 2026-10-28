#!/bin/bash
# crop each cipher row of picture.jpg into thirds at 4x: row x_start y_top width
cd "$(dirname "$0")"
for spec in "01 300 40 670" "02 300 96 640" "03 300 142 640" "04 280 194 690" "05 275 234 692" "06 275 276 721" "07 270 320 704" "08 270 362 728" "09 305 405 659" "10 25 447 945" "11 25 489 955" "12 25 528 925" "13 25 567 935" "14 18 603 978"; do
 set -- $spec; r=$1; x=$2; y=$3; w=$4; t=$((w/3))
 for k in 0 1 2; do ./zoom.sh L$r-$k $((t+14)) 46 $((x+k*t-4)) $y 4; done
done
