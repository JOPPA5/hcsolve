#!/bin/bash
PY=/Users/tomaspavuk/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3
args=""; for t in 0 1 2; do y=$((60+t*690)); for c in 0 1 2 3; do x=$((60+c*400)); args="$args t$t$c $x $y $((x+430)) $((y+720)) 3"; done; done
$PY -I review/work/crop.py $args
