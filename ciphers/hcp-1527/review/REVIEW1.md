REVISE

# Review 1 — HCP 1527 (pc_hcp_208), round DONE1

Reviewer: claude-opus-5-5, 2026-10-28.

In short, **the decipherment and the transferred family key are right**, and the twelve rows give the solver's Czech letter. The verdict is REVISE because the transcription differs from the scan in **six places**. Two of them change the editorial text:

- A missed sign turns **Sedláčková** into "Sedláková" (finding 1).
- A misread I/Y produced the solver's explicit claim about archaic "posýlá" (finding 2).

The other differences are writer's slips that were silently normalized.

## What I verified and how

1. **The documented command.** `python3 -I ciphers/hcp-1527/work/decode.py` runs, and all source and record hashes pass. It prints the 12 rows exactly as in "Literal base plaintext" (414 units, 2 CH, 416 letters). It is read-only. I did not run `build-record.py` or `make-controls.py`.
2. **Independent decoder.** `review/work/my_decode.py` holds my own transcription and my own statement of the key; it imports nothing from the solver. It reads the solver's `transcription.json` only to print a diff. Run it with `python3 -I ciphers/hcp-1527/review/work/my_decode.py`:
   ```
   R02 JSEM CASTECNE VELMI PREKVAPEN. CLECNA SEDLAC-
   R03 KOVA SE ASI MNOHO PRESLECHLA; NEMAM O TETO NME
   R10 VPOLEDNE DOMU. TISIC VRELYCH PUS A POZDRAVU POSILA
   R11 TI TVUJ PEPOUS, KTERY SVEMU CRDECKU PREJE, ABY
   (all other rows identical to the solver)
   rows=12 units=415 base_letters=417 CH=2
   ```
   The key is one-to-one, and all 22 classes are used. Every sign on the card resolves under it, so the differences come only from the transcription.
3. **Reading the scan.** The picture is rotated 90° counter-clockwise (`review/work/up.png`). Crops:
   - all rows, at 4×: `row01a/b … row12a/b.png`
   - three rows per crop, at 3.2×: `w0a … w3b.png`
   - every disputed word, at 6×–14×: `z-*.png`
   - equal-scale comparison sheets: `cmp-cs.png` (S/C), `cmp-mne-mnoho.png`, `cmp-1-4.png`, `cmp-jinymi-3.png`, `cmp-td.png`

   Pixel dumps come from `review/work/ascii.py` (it needs `ffmpeg -i up.png -f rawvideo -pix_fmt gray up.gray`).
4. **Search for missed cipher text.** Below the portrait are the 12 rows and the plain date `19.XII.1903`; the address side is plain. I found no further cipher region. One sign inside a word was missed (finding 1).
5. **Context.** 19 December 1903 was a **Saturday**, and the wishes for "hezké svátky" fit the week before Christmas. The card continues the series after HCP 1526 (12 Dec), and "Vřelý dík za drahé psánko" answers that card's closing "těší na slíbené psánko". This was not noted by the solver, but it supports both readings.
6. **Prior solutions.** None was attached on the portal. The generic Egorov key is disclosed and lists no pc208 reading.

## Findings

1. **major (missed sign; proper name): R02 `SEDLA-` is `SEDLAC-`, i.e. Sedláčková.** See `review/work/z-sedlac10.png`, `cmp-cs.png` (panel 3), `w0b.png`. Between the final 6 (= A) and the hyphen stands a clear angular s-sign (= C): `c5t86s-`. The name is **SEDLAC-/KOVA = Sedláčková** (from Sedláček), not Sedláková. Fix the transcription, the counts (415 units, 417 letters), the editorial text, the Slovak translation and the uncertainty section.

2. **major (misread; contradicts an explicit claim): R10 `POSYLA` is `POSILA`.** See `review/work/z-pozdravu-posyla.png`. The fourth sign of `b3c?86` is the underbarred digit-4 I-form, the same as the I in `6m4` (ANI) and `d4c4s` (TISIC). It is not the footed 1 of `p18` (BYL) or `m1m4` (NYNI) (`cmp-jinymi-3.png`, panels 2–3). The literal is **POSILA**, so the editorial reading is the ordinary *posílá*. Remove the sentence about archaic *posýlá*.

3. **major (literal layer silently normalized): R03's final `MNE` is written `mn5`, literally NME.** See `review/work/cmp-mne-mnoho.png`. The first sign has three humps (m = N) and the second has two (n = M). In `MNOHO` in the same row the writer has the correct order, n then m. The intended *mně* is certain, but the transposition is on the card and should be recorded as `[NM→MN]E` or listed as a writer's slip.

4. **major (same issue, S/C): the angular C-sign is written for S twice.**
   - R02 `SLECNA`: the first sign is the angular s-form, identical to the 4th sign (the real C) of the same word. It is not the round c used for S in `JSEM` and `CASTECNE` (`cmp-cs.png` panels 1–2 vs 6–7; `z-slecna10.png`). Literal **CLECNA**.
   - R11 `SRDECKU`: the first sign is the angular s-form (`z-srdecku-r11.png`), whereas R07 `SRDECKA` correctly begins with the round c (`z-srdecka-r07.png`). Literal **CRDECKU**.

   The same writer makes the same slip on HCP 1526 (CRDECKO, ZACE). The report should state this tendency.

5. **minor: R06 `JINYMI`, 4th sign.** See `review/work/z-jinymi10.png`, `cmp-jinymi-3.png` panel 1. The sign is heavily inked and has a closed, 2-like loop at the top. Its height and foot match the footed 1 (Y) better than the x-height 2 (U), so I accept JINYMI. It should still be listed as a retraced, less certain sign.

6. **minor (agreement, for the record).** I confirm several readings:
   - PSANKO (`bc6mg3`)
   - NENALEZIM TEZ: both Z are the 9-with-hook q-form; the K of `K TEM` and `KDOZ` is the looped g (`z-nenalezim-tez.png`, `z-k-tem-kdoz.png`)
   - CTVRT ROKEM (`sdfhd h3g5n`, `v-r08a.png`)
   - the underlined PRED
   - the CH caron in VRELYCH

   Leaving "před čtvrt rokem" unexplained is the right choice.

## Required for closing

- R02: add the C of SEDLAČKOVÁ, and record SLECNA's first sign as the C-form (literal CLECNA).
- R03: record the final word as written (m-n-5).
- R10: change `1` to `4` in POSILA, and drop the *posýlá* remark.
- R11: record SRDECKU's first sign as the C-form.
- Update the counts (415/417), `positions.csv`, the record hashes, the literal and editorial text, the Slovak translation and the writer's-slip list.

The reading and the key stand. If these corrections are made as listed, I see no need for another round.

## What I could not verify

- Whether the slips in findings 3–4 look different at higher resolution than the portal's 1024 px.
- The identity of Slečna Sedláčková, or the intended sense of "před čtvrt rokem".
- Worldwide novelty. I relied on the solver's bounded register and Egorov-index checks.
