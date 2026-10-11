# Segmented single-columnar search — GPT-6.1 Sol

This is a conditional ordinary incomplete single-columnar family. No historical R identification is made. Cipher length400 exceeds cited recommended R maximum250; that is a historical caution, not mathematical exclusion.

Existing controls.json and all earlier scripts/results remain unchanged. The new method enumerates ciphertext chunk-length patterns independently of physical column order. If n=h*w+r, exactlyr ciphertext chunks have lengthh+1 andw-r have lengthh. Only columns0..r-1 in the physical plaintext rectangle may receive long chunks. For395letters,width19 has3,876 possible patterns andwidth22 only22. For each pattern the ciphertext boundaries are fixed; order mutations stay within long/short physical classes. Thus they cannot accidentally move every following boundary when a short and long chunk swap.

bigrams.py builds a frozen pairwise row-adjacency helper from read-only primary UD Slovak SNK training sentences. It never uses control text. Pairwise chunk costs include consecutive physical columns and last-to-first next-row wrap, including incomplete final row. Every length pattern gets5 seeded bigram annealing starts ×1,500 swap/reverse/relocation proposals. Best40 patterns are retained by their optimized bigram score. Their order is refined with unchanged Slovak3/4/5gram models from batches/scoring-sol61 (weights.15,.4,.8). Within-class swaps, reversals, one-column moves and contiguous-block moves get100,000 proposals per pattern; temperature1+100*(1-t)^2 reheats every20,000 proposals. No control key, crib, plaintext or target-specific words are supplied to search.

Initial search.cpp separated lengths but remained too cold for long-text order basins and failed exact controls. search-v2 adds block moves and appropriate temperature; both395-letter width19/22 controls recover whole plaintext and exact planted key. search-v3 retains40 instead of200 patterns for bounded target work; both controls still exact. validate.py independently decodes and re-encrypts the recovered keys, recorded control-v3-validation.json. search-v4 avoids copying immutable chunk strings per proposal, keeping identical parameters/RNG/objective; its complete output matches v3 byte-for-byte on both controls before target runs. These controls use a previously planted synthetic message; they are not historical plaintext and not inserted into model training. Model development elsewhere used short unrelated controls, disclosed in that batch README.

run-targets.py preserves checkpoints and searches six explicit readings at widths19,22,16,17,18,20,21:400letters X/A, omitgroup3 X/A and omitgroup25 X/A. Raw digits4→A,8→B and unknown?→X/A are hypotheses. Neither omission is proved to remove an indicator. Outputs state the ciphertext reading-order key as zero-based physical column numbers; pattern and physical_chunk_order are diagnostics. Key+full candidate always re-encrypts within its hypothesized input family, but that alone does not make an incoherent candidate a decipherment.

Reproduce from root:

```
python3 ciphers/hcp-363/work/segmented/bigrams.py
c++ -O3 -std=c++17 ciphers/hcp-363/work/segmented/search-v4.cpp -o ciphers/hcp-363/work/segmented/search-v4
```

Invoke the binary as:

```
ciphers/hcp-363/work/segmented/search-v4 batches/scoring-sol61 ciphers/hcp-363/work/segmented/bigrams.tsv ciphers/hcp-363/work/control-19.txt 19
```

Saved control22-v4-results.txt and control19-v3-results.txt are prerequisites for run-targets.py's equivalence assertions. It rebuilds no existing source or historical input and reproduces target diagnostics, not a target decryption. All previous outputs remain preserved under their original names.

This enumerates length patterns, not all column permutations. At most40 segmentation hypotheses receive full language refinement, so negative output cannot exclude unretained patterns, optimizer misses, other widths, different direction/fill rules, double/triple transposition or another family. Modern model mismatch and scan errors also remain open. No DONE for unresolved ciphertext.
