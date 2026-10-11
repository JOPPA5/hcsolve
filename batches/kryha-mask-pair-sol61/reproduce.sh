#!/bin/sh
set -eu
cd "$(dirname "$0")"
python3 prepare.py
for source in pair-profile pair-masc pair-joint pair-mask pair-cycle pair-mask-profile pair-bridge-masc; do
 clang++ -O3 -std=c++17 "$source.cpp" -o "$source"
done
python3 run.py
./pair-cycle ciphertexts.txt 26 2 32 20000 > pair-cycle.tsv
python3 run-cycle.py
./pair-mask-profile ciphertexts.txt coordinates.txt ../../ciphers/hcp-350/work/ring-unigrams.tsv pair-cycle.tsv > mask-profiles.tsv
python3 run-bridge.py
python3 verify.py
python3 run-targets.py
python3 verify-targets.py
python3 framing355-control/prepare.py
python3 target-case.py "$PWD/framing355-control"
python3 verify-framing355.py
python3 column-profile-diagnostic.py
clang++ -O3 -std=c++17 pair-local-mask.cpp -o pair-local-mask
python3 run-local355.py
python3 verify-local355.py
clang++ -O3 -std=c++17 shared-template/latent.cpp -o shared-template/latent
python3 shared-template/diagnose.py
clang++ -O3 -std=c++17 shared-template/refine.cpp -o pair-template
python3 run-template355.py
python3 verify-template-latents.py
python3 verify-template355.py
python3 run-local-template355.py
python3 verify-local-template355.py
