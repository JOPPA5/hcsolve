#!/bin/sh
set -eu
cd "$(dirname "$0")/../../.."
c++ -O3 ciphers/hcp-371/work/attack.cpp -o ciphers/hcp-371/work/attack
c++ -O3 ciphers/hcp-371/work/control/attack.cpp -o ciphers/hcp-371/work/control/attack
ciphers/hcp-371/work/control/attack ciphers/hcp-371/work/control
ciphers/hcp-371/work/attack ciphers/hcp-371/work
ciphers/hcp-371/work/attack ciphers/hcp-371/work reverse
