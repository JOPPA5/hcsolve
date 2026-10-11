# GPT-6.1 Sol audit: a concrete search defect, not a decipherment

Read README fully and inspected NOTES and attack code for 399,395,396,393,345,350,351,334,363,367,369 and analysis-395-396. Cipher directories and sources unchanged. No target solution searched externally. No recovered key/plaintext claimed.

The promising new lead is **separate irregular column-length assignment from permutation optimization**. Existing columnar routines invert their own planted controls correctly; their key proposals nevertheless mix two different operations: ordering fixed chunks and changing chunk boundaries. For N mod w nonzero, exchanging a long and a short column changes parsing boundaries throughout the intervening ciphertext. A nominal two-column swap can therefore destroy most of an otherwise correct decryption. This is an attack-neighborhood limitation, not an incorrect inverse.

Tiny reproducible test: `python3 batches/sol61-audit/landscape.py`. It uses the existing invented 240-letter triple control and its disclosed keys (19,17,22), independently decodes correctly, enumerates every single swap of each stage while other stages remain correct, and scores with the existing fourgrams. Only 538 swaps and 200 random controls; no hill-climb/search. Output: batches/sol61-audit/landscape.json.

True score696.51; random-key median−478.92. Median score for same-length versus different-length swaps:

| Stage | Width | Same length | Different length |
|---|---:|---:|---:|
|1|19|414.42|−15.48|
|2|17|368.68|−120.11|
|3|22|430.54|−54.98|

Corresponding median correct letters are216/153,214/158,218/163.5 of240. Worst individual swaps leave17,54,34 correct respectively. A near-correct key can be separated from a better length pattern by a severe score cliff. This is relevant to the failed single19/22 controls in363 as well as triple failures in399. These measurements do not establish that this is the only, or dominant, cause of search failure.

**Concrete next test:** implement a two-level irregular-columnar control attack. Outer state explicitly chooses the sequence of long/short ciphertext chunks; inner state permutes columns only within equal-length classes, leaving chunk boundaries fixed. For width22 and N395 the remainder is21, so there are only22 outer length patterns: enumerate them and optimize inner permutations per pattern. For width19 and N395 there are choose(19,15)=3876 patterns: use a bounded beam/outer search instead of unstructured boundary-changing swaps. Compare exact recovery against the existing363 19/22 controls with independent seeds and the same evaluation budget. Include regular-length controls and a near-key test; success must mean full plaintext recovery, not higher heuristic score. Only after this gate passes should the same machinery attack ambiguous363 variants or be nested inside triple search. This is substantially more informative than another undifferentiated million-step run.

Other audit boundaries: joint395/396 models only n,n,n alignment, although its local primary-method paper also describes n,n+1,n+2. That is a genuine unimplemented family, not evidence it occurred in these telegrams. Shared dispatch dates do not establish shared daily keys. Published worked-example reconstruction remains tentative and cannot validate historical conventions. UD-training-corpus controls are optimistic; X/Q separators and old diplomatic orthography are absent from that training preparation.350/351 fixed17-step diagnostics constrain only their explicit same-plaintext/shared-ring hypotheses, not general adjustable Kryha.334 appropriately preserves erasure positions.345 exact crib exclusions are narrow and valid only for the documented conventions and strings. No negative heuristic target result excludes a family when positive key-recovery controls fail.

## Follow-up implementation: control gate failed

Implemented two-level single-width22 search in batches/sol61-audit/twolevel.cpp. On the363 synthetic395-letter width22 ciphertext, it explicitly enumerates all22 possible positions of the sole17-letter short chunk; every other chunk has18 letters. Inner mutations swap/reverse/rotate only long-column assignments, with the short column fixed to plaintext column21. Search seed610111 is independent of the planted key. Budget22 patterns×10 restarts×20,000 proposals=4,400,000 evaluations. Score remains the previously used Slovak fourgrams.

`python3 batches/sol61-audit/check_control22.py` independently verifies known-key inverse correctness and reports exact comparison. Search best672.678 versus true971.558646;103/395 plaintext letters match; plaintext and key both fail exact recovery. Full diagnostic candidate/key retained in control22-seed610111.txt. Known-key inversion is exact, but **new attack has not demonstrated key-recovery power**. No363 target attack or width19 expansion was run: the prescribed positive-control gate failed. The length-boundary cliff is a real measured effect; fixing that proposal class alone was insufficient at this budget. No cipher-family exclusion follows.
