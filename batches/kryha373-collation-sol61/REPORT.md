# HCP373 published context: independent offline collation

HCP373 is already public **Solved**, message 80172/1944, Országh to Madrid, 17 May 1944. The plaintext here is transcribed from its published archival attachment; this is not a new decipherment or key recovery. Parent collected all three rendered portal tabs. Provenance and observed attachment URLs remain in `../solved-context-main/373/SOURCES.md`; SHA-256 source hashes are in `manifest.json`. No immutable source, cipher directory, or marker was changed.

The source header is **650** and the body physically contains **130 five-letter groups = 650 letters**. The first group clearly reads **KIDAH**, unlike the SOSOL beginnings of 350/351. This is a reading, not evidence that the first group is an indicator or independently encrypted prefix. Top block has 64 groups; bottom block has 64 plus two final groups. The complete declared preferred input is `ciphertext650.txt`, with 1-based group/letter positions in `groups-indexed.tsv`.

`ciphertext-groups.txt` preserves the initial manual pass. Pixel reinspection changed its group47 XXEZT to preferred **XXAZT** (letter233 A/E) and group54 HVAJA to preferred **HVEJE** (letters268 and270 E/A); alternatives remain explicitly available in `glyph-branches.json`. No decipherment or target score was consulted to select these readings. Other source uncertainties include group11 CDLVW, group18 ELDNE/ELDNA, group26 PMOWJ/LMOWJ, annotated group31 HDEUI, group96 CDFBS/CDIRS/CDFRS, and group101 IMVES/IMVAS. Watermark interference prevents an unqualified exact-transcription claim. The recorded coordinates are original 1024×1365 image coordinates; diagnostic crops are nearest-neighbour enlargements only.

Last15 groups (116–130) are:

`OJGEC NCJHP NFIRI ZGAHM XAJYY ALRWG SKYSK BTRQK RTJUJ KQQKS HJSYQ XUROU ZBLTW YDJUQ FNPBV`

The full published typed plaintext, including original line breaks, punctuation and numbers, is in `plaintext-typed.txt`. Preserve **oznamil, celuloziek, dľa, Asociacion Papelera, pozdejšiu, španielské, protidodávky** as printed. First-line Ústredni has an apparent handwritten d correction above the typed word; transcription includes that correction, not an extra character. The outside heading and Országh signature are excluded from the body. End-of-line hyphens in rekla-/mácie, ob-/jednávku, nebie-/lenú, lacnej-/šiu are line division, not additional lexical letters.

The six literal numerical tokens are **6.000, 1900, 1470, 4.000, 1.651, 1.264** (24 digits). Removing diacritics/spaces/punctuation and excluding numbers gives **536 letters**. Spelling each digit with frozen `nula jedna dva tri styri pat sest sedem osem devat` gives **640 letters**, preserved in `plaintext-digitwise640.txt`. Using DVE instead of DVA for digit2 leaves the length unchanged, but changes the inventory. These are preparatory hypotheses, not an established machine input.

There are four sentence-ending full stops, excluding thousands separators. Therefore **640 + four J separators + five initial characters + one filler = 650** is a concrete length-compatible hypothesis. It does not establish the separator rule, initial-five semantics, filler, numeral wording or placement. Cardinal readings and comma encoding remain open; fitting a length does not validate them. `counts.json` records the exact counts and inventories; plaintext/ciphertext inventories are not expected to match under a mixed-ring machine. An independent full inverse/re-encryption with a recovered or transferred ring/key is needed before treating any preparation as known.

Reproduce counting and declared-input generation:

`python3 batches/kryha373-collation-sol61/analyze.py`

The next useful test is the parent's declared same-ring transfer on the complete 650-character input, retaining source glyph branches and inspecting the resulting number/separator preparation. This report itself performs no transfer or cryptanalysis of the already published solution.
