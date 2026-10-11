#!/bin/sh
set -eu
cd "$(dirname "$0")/../../.."
python3 ciphers/hcp-367/work/prepare.py
c++ -O3 -std=c++17 ciphers/hcp-367/work/attack.cpp -o ciphers/hcp-367/work/attack
python3 ciphers/hcp-367/work/controls.py
for mode in full drop1 drop7; do
 ciphers/hcp-367/work/attack ciphers/hcp-367/work normal "cipher-$mode.txt" > "ciphers/hcp-367/work/results-$mode.txt"
 ciphers/hcp-367/work/attack ciphers/hcp-367/work reverse "cipher-$mode.txt" > "ciphers/hcp-367/work/results-$mode-reverse.txt"
done
