# Conditional X/Q lexical reranking — main solver, OpenAI GPT

This generic diagnostic enumerates identity, all 325 global plaintext-letter swaps and all 5,200 three-letter cycles. Each whole text is scored using the independently frozen Slovak morphological vocabulary/frequencies in batches/scoring-sol61/frequency/words.tsv. X is treated conditionally as a sentence boundary; paired Q encloses an unknown proper name. Neither convention is proved for Kryha target messages.

Initial lexical scoring gave a proper-name span length−4 versus dictionary-word reward3×length−4+frequency bonus. This unfairly discourages unknown proper names compared to ordinary words; the final implementation instead uses the same base3×length−4 for names (without frequency bonus). Both changes are disclosed because these calibration controls have already been inspected. A fresh independent control would be necessary before interpreting an improved result as held-out validation.

The original score fails both near-exact known-output-ring controls: true text ranks39/65. The corrected name reward also fails the365-letter control (truth rank32). The resulting highest texts are incomplete false readings. Truth was accessed only after sorting for diagnostic ranks; it never selected a candidate. Final JSON files preserve the current implementation's results. No target attack or exclusion is justified from these control failures, and no historical plaintext is claimed.

Reproduce: `python3 batches/marker-lexical/rerank.py batches/kryha-framing-sol61/control365-sign-1/phase11/result.json` and the analogous control355-sign1/phase8/result.json command. This only writes batches/marker-lexical/; source and cipher directories stay unchanged. Input result includes plaintext candidates from the separate frozen 4-gram attack, not the planted control as a search seed.

The corrected name reward also fails the355-letter control: truthrank34; wrong full texts remain best. No target search followed.
