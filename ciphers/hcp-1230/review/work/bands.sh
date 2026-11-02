#!/bin/bash
PY=/Users/tomaspavuk/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3
args=""; y=50; i=0; while [ $y -lt 2150 ]; do n=$(printf %02d $i); args="$args a${n}L 40 $y 840 $((y+290)) 2 a${n}R 760 $y 1600 $((y+290)) 2"; y=$((y+250)); i=$((i+1)); done
$PY -I review/work/crop.py $args
