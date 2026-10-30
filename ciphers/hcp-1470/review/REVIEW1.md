ACCEPT

# Review 1 — hcp-1470 (pc_hcp_151), reviewer Claude Opus 5.5, 2026-10-30

## What I verified and how

1. **Solver command.** `python3 -I ciphers/hcp-1470/work/decode.py` (repo root):
   `source hashes OK`; `cipher : 13-1-18-9-13-1-18-18-1-14-4-5-15-20 (14 numbers)`;
   `literal: MARIMARRANDEOT`; `segmented (editorial): MARI MARRANDEOT`.
   Matches the plaintext claimed in SOLUTION.md. I also recomputed SHA-256 of both
   images with `shasum -a 256`; they match work/source-sha256.json.
2. **Independent transcription.** I read the single numeric line on the address side
   myself from my own crops of source/address-large.jpg (review/work/r-a.png,
   r-b.png, r-c.png at 4x; r-head-rot.png and r-tail-rot.png rotated ~22–25 deg,
   3–4x, autocontrast; r-14-4.png and r-18-1.png at 7–8x). My reading:
   `13-1-18-9-13-1-18-18-1-14-4-5-15-20` — identical to work/transcription.txt
   sign for sign. Dashes separate every number except that the sign at position 11
   sits directly on the printed double divider line.
   - Pos. 1 and 5 "13": both are a long 1 with the same flat-topped cursive 3; in
     the 9-13-1 cluster the 1 of "13" overlaps the 3 but the 3's loop is clear.
     The earlier GPT doubt (12) is rightly rejected.
   - Pos. 3, 7, 8 "18": tall 1 + looped 8, unambiguous.
   - Pos. 10 "14": 1 followed by a looped 4, no dash between them.
   - Pos. 11 "4": a long diagonal stem with a crossbar at its lower part, partly
     under the printed divider. No top bar is visible, which argues against a
     crossed French 7. 4 is the better reading; 7 cannot be ruled out because the
     divider covers the upper junction. The solver discloses exactly this.
   - Pos. 12–14 "5-15-20": clear.
3. **Independent decode.** review/work/indep_decode.py (own reading, own A1Z26
   table): 14 numbers, range 1..20, `MARIMARRANDEOT`; alternative pos. 11 = 7 gives
   `MARIMARRANGEOT`; solver transcription identical = True.
4. **Key coverage.** All 14 numbers are in 1..26 and decoded by one key; no
   number left over. The picture side carries no handwritten cipher (checked
   source/picture-large.jpg; only the printed caption "Anniversaire", no. 1158 and
   the stamp/postmark).
5. **Context.** Address side shows postmark TOURS A VIERZON 30-3-09 and a plain
   French address to Mademoiselle Valentine ... (Indre et Loire), as stated. The
   cipher line occupies the otherwise empty correspondence half, so a coded
   signature is a sensible interpretation. The same plain A1Z26 key is used on
   accepted sister cards (hcp-1098, 1463, 1492, 1496 — checked their SOLUTION.md).
6. **Alternatives.** The GPT screen (work/numeric-attempts.txt: 26 shifts +
   reverse) shows nothing pronounceable except offset 0. The repeated 13-1-18 =
   MAR in both halves is internal evidence the direct mapping is right.
7. **Sources/honesty.** SOURCES.md and SOLUTION.md state no published or attached
   solution; portal metadata says Not solved. Earlier GPT work is credited.

## Findings

1. (minor) **The name is unverified and slightly odd.** `MARRANDEOT` is not an
   attested surname that I know of either; close forms (Marandeau, Marandet) exist
   in central France. The solver reports the output literally and lists this as
   uncertainty 1 — correct handling. The report should keep "Mari(e)
   Marrandeot" framed as a literal decode, not as an identified person, and may
   mention the possibility of a misspelling/mis-encoding by the writer (e.g. for
   Marandeau) without adopting it.
2. (minor) **Position 11 (4 vs 7).** My crops agree with 4 but the divider covers
   the upper part of the sign; MARRANGEOT remains a disclosed alternative. No
   change needed beyond keeping it in the report.
3. (minor) **Date inconsistency.** SOLUTION.md says the round was done
   2026-10-30, while DONE1 reads `2026-10-29T23:17Z` (local vs UTC date). Use the
   UTC date consistently in the report.
4. (minor) **Segmentation/language.** MARI | MARRANDEOT and "French" are
   editorial; they are labelled as such. The translation "Mari(e) Marrandeot
   [signature]" is fine; the alternative gloss *mari* "husband" is speculative and
   should stay marked as such.

## What I could not verify

- The identity of the sender or any record of a person named Marrandeot / Marie
  Marrandeot around Tours/Lacroix in 1909.
- The original card at higher resolution; only the 1024 px portal image was
  available, which limits the decision on position 11.
- The recipient's surname (Poudechat/Paudechat) — irrelevant to the decoding.
