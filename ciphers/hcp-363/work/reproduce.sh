#!/bin/sh
set -eu
cd "$(dirname "$0")/../../.."
python3 ciphers/hcp-363/work/prepare.py
c++ -O3 -std=c++17 ciphers/hcp-363/work/columnar.cpp -o ciphers/hcp-363/work/columnar
c++ -O3 -std=c++17 ciphers/hcp-363/work/columnar-improved.cpp -o ciphers/hcp-363/work/columnar-improved
python3 ciphers/hcp-363/work/controls.py
python3 ciphers/hcp-363/work/validate_controls.py
for casefile in cipher-x cipher-a omit-3 omit-25; do
  ciphers/hcp-363/work/columnar ciphers/hcp-363/work "ciphers/hcp-363/work/$casefile.txt"
done
for casefile in control-19 control-22 omit-3 omit-25; do
  ciphers/hcp-363/work/columnar-improved ciphers/hcp-363/work "ciphers/hcp-363/work/$casefile.txt"
done
