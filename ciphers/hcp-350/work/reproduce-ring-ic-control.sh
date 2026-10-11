#!/bin/sh
set -eu
cd "$(dirname "$0")/../../.."
python3 ciphers/hcp-350/work/ring_control.py
c++ -std=c++17 -O3 ciphers/hcp-350/work/ring_ic.cpp -o ciphers/hcp-350/work/ring_ic
c++ -std=c++17 -O3 ciphers/hcp-350/work/ring_ic_masc.cpp -o ciphers/hcp-350/work/ring_ic_masc
c++ -std=c++17 -O3 ciphers/hcp-350/work/ring_ic_refine.cpp -o ciphers/hcp-350/work/ring_ic_refine
ciphers/hcp-350/work/ring_ic ciphers/hcp-350/work/ring-control-cipher.txt 6 -1 3000 > ciphers/hcp-350/work/ring-ic-control-candidates.txt
python3 ciphers/hcp-350/work/ring_ic_calibrate.py
python3 ciphers/hcp-350/work/ring_ic_rerank.py
python3 ciphers/hcp-350/work/ring_ic_refine.py
