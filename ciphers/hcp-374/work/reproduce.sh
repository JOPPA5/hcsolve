#!/bin/sh
set -eu
cd "$(dirname "$0")/../../.."
c++ -O3 -std=c++17 ciphers/hcp-374/work/columnar.cpp -o ciphers/hcp-374/work/columnar
c++ -O3 -std=c++17 ciphers/hcp-374/work/substitution.cpp -o ciphers/hcp-374/work/substitution
ciphers/hcp-374/work/columnar ciphers/hcp-374/work
ciphers/hcp-374/work/substitution ciphers/hcp-374/work
ciphers/hcp-374/work/substitution ciphers/hcp-374/work reverse
