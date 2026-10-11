#!/bin/sh
set -eu
cd "$(dirname "$0")/../../.."
python3 ciphers/hcp-393/work/train.py
c++ -O3 -std=c++17 ciphers/hcp-393/work/attack.cpp -o ciphers/hcp-393/work/attack
ciphers/hcp-393/work/attack ciphers/hcp-393/work
ciphers/hcp-393/work/attack ciphers/hcp-393/work reverse
