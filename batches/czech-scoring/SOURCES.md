# Czech language alternative, 2026-10-11

Main solver: OpenAI GPT.

Primary corpus repository: https://github.com/UniversalDependencies/UD_Czech-CAC . Public TRAIN and TEST files downloaded unchanged from its master branch on 2026-10-11; SHA-256 checksums are recorded by build.py. The corpus contains written administrative, journalistic and scientific Czech, predominantly from the 1970s and 1980s. It is a language proxy, not a historical diplomatic corpus or evidence that a target is Czech. See the original repository README and license.

URLs:
- https://raw.githubusercontent.com/UniversalDependencies/UD_Czech-CAC/master/cs_cac-ud-train.conllu
- https://raw.githubusercontent.com/UniversalDependencies/UD_Czech-CAC/master/cs_cac-ud-test.conllu

Models use only normalized TRAIN sentence text. TEST is reserved for independent generated controls; it is never added to scoring models. Solver source is adapted from ciphers/hcp-369/work/mono-c28.cpp; all ciphertext-source files remain unchanged. The 28-letter alphabet retains Č/Š while folding them only for scoring, and cannot establish their exact orthography from folded controls.
