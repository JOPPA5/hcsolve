REVISE

# Review 1 — HCP 1529 (pc_hcp_210), round DONE1

Reviewer: claude-opus-5-5, 2026-10-28.

In short, **the decipherment and the transferred family key are right.** Of the 417 signs I read on the card, my reading matches the solver's in all but one. That one is a whole word: the one-sign preposition before ÚSTÍ is **Z**, not K (finding 1). It changes the sense from "on the way *to* Ústí" to "on the way *from* Ústí", so the verdict is REVISE. The weak points the solver disclosed (PRI, MISLENI) are handled correctly.

## What I verified and how

1. **The documented command.** `python3 -I ciphers/hcp-1529/work/decode.py` runs, and all source and record hashes pass. It prints the 8 rows exactly as in "Literal Czech base reading" (417 units, 3 CH, 420 letters). It is read-only. I did not run `build-record.py` or `make-controls.py`.
2. **Independent decoder.** `review/work/my_decode.py` holds my own transcription and my own statement of the key; it imports nothing from the solver. It reads the solver's `transcription.txt` only to print a diff. Run it with `python3 -I ciphers/hcp-1529/review/work/my_decode.py`:
   ```
   R02 NEBYL JSEM PRESTO UPLNE ZDRAVEM A NACHLADIL JSEM SE OPET NA CESTE Z USTI
   (all other rows identical to the solver)
   rows=8 units=417 base_letters=420 CH=3
   Differences: R02 solver['g'] -> reviewer['q']  ('K' -> 'Z')
   ```
   The key is one-to-one, all 22 classes are used, and every sign resolves.
3. **Reading the scan.** The picture is used upright. Crops:
   - every row in fifths, at 6×: `q01_0 … q08_4.png`
   - disputed words, at 6×–12×: `z-*.png`
   - all K and Z signs on the card at equal scale: `cmp-KZ-all.png`, `cmp-isolated-K-Z.png`, `cmp-gq.png`

   I also made pixel dumps of PRESTO/ZDRAVEM, the two KDE, PRI and the K/Z signs, using `../../hcp-1527/review/work/ascii.py` on `ffmpeg -i source/picture.jpg -f rawvideo -pix_fmt gray pic.gray`.
4. **Search for missed cipher text.** The card has the seven upper rows, the full bottom marginal row R08, and the plain date at the right edge. The address side has the ordinary address and two postmarks: a PRAHA dispatch stamp, and an arrival stamp SEROWITZ/ŽIROVNICE with the year `03` legible (`z-postmarks.png`). I found no further cipher.
5. **Context.**
   - **Dates.** 1 December 1903 was a **Tuesday**. "Od čtvrtka" means since Thursday 26 Nov, and "přijdu ve čtvrtek nebo v pátek" means 3/4 Dec. The next card, HCP 1526 (Sat 12 Dec), has him back in the office "ode středy" and still with a cold. The series is consistent.
   - **The záložna.** The Prague dispatch postmark fits a writer attending a hearing ("líčení") on the bankruptcy of the Svatováclavská záložna. To my knowledge this was a Prague credit cooperative whose 1902 collapse led to a much-reported criminal trial in late 1903. I state this from general knowledge and did not verify it against a source in this review. If confirmed, it is strong independent support for the reading and belongs in the report's context section.
6. **Prior solutions.** None was attached on the portal. The generic Egorov key is disclosed, and pc210 is not in its index.

## Findings

1. **major (misread word): R02 `K USTI` is `Z USTI`.** See `review/work/z-k-usti.png`, `cmp-isolated-K-Z.png` and `cmp-KZ-all.png`.
   - **The two forms.** On this card the writer separates the two signs consistently:
     - **K** (g-sign) has a long descender that makes an open loop back to the right. This holds in every K on the comparison sheet: ANICKO, CTVRTKA, KTERA, VSAK, UPADKU, KDE ×2, VELKY, SKORO, PROTOZE … VSAK, JAKO, SRDECKO.
     - **Z** (q-sign) is a compact closed 9 with a short tail hooking left (ZDRAVEM, ZALOZNY ×2, HROZNE, LEZIM, JIZ, VZKAZAL, ZE, VZPOMINAM).
   - **The isolated sign.** The one-sign word between `s5cd5` (CESTE) and `2cd4` (USTI) is the compact 9-with-hook. In `cmp-isolated-K-Z.png` (K, K, *this sign*, Z, Z at equal scale) it matches the two Z on the right, not the two K on the left.
   - **The fix.** Read **NA CESTE Z USTI**, *na cestě z Ústí* ("on the way from Ústí"). This is also the more natural Czech: a journey "to" a town would usually be *do Ústí*, not *k Ústí*. Fix the transcription, the literal and editorial text and the Slovak translation ("na ceste z Ústí"). Also change NOTES/SOLUTION, which mention "k Ústí".

2. **minor (agreement): R03 PRI.** See `z-pri.png`, `z-pri12.png`. The b and the tall h are visible before the heavy blot, and a following 4 is consistent with it. The disclosure as the least clear sign is adequate.

3. **minor (agreement): R05 MISLENI, R02 ZDRAVEM, R06 PROTOZE … LEPE, R06 VZKAZAL.**
   - MISLENI: the sign is the underbarred 4 = I (`z-misleni.png`).
   - ZDRAVEM: confirmed by the pixel dump.
   - PROTOZE … LEPE: the region is dark (`z-protoze.png`, `z-protoze-c.png`), but `bh3d3q5 fc6g tm5c y4q 85b5` is legible. No letters are hidden that would fill the ellipsis.
   - VZKAZAL: confirmed (`z-vzkazal.png`).

   I also agree with ANICKO, USTI (`2cd4`) and the bottom-row reading.

4. **minor (presentation).** The family's shape labels differ between cards: here `y` = J and `H` = CH, while HCP 1526 and 1527 use `7` and `ř`. In HCP 1529, `H` sits next to `r` = H. This is internally consistent, but the PDF report should present one family table so readers do not mistake the label H for the plaintext letter H.

5. **minor (context not used).** The solver says the záložna reference is "not independently researched". A short check (see verification 5) would turn it into evidence for the decipherment. The weekday and series consistency with HCP 1526/1527 should also be in the report.

## Required for closing

- R02: change `g` to `q` before `2cd4` (Z ÚSTÍ), regenerate the record hashes, `positions.csv` and `plaintext.txt`, and update the editorial text and translation.
- Optionally add the záložna context and the weekday/series check to the report.

If finding 1 is corrected, I see no need for another round.

## What I could not verify

- Which Ústí is meant.
- The day digits of the postmarks. The year `03` is legible; the day and month are only partly legible at this resolution.
- The historical date of the Svatováclavská záložna trial. It comes from general knowledge, not checked against a source here.
- Worldwide novelty. I relied on the solver's bounded register and Egorov-index checks.
