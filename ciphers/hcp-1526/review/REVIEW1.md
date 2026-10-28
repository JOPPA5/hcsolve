REVISE

# Review 1 — HCP 1526 (pc_hcp_207), round DONE1

Reviewer: claude-opus-5-5, 2026-10-28.

In short, **the decipherment is right and the transferred family key is right.** I re-read all 16 rows sign by sign from `source/picture.jpg`. I get the same Czech love letter from Pepouš to Anna/Andulka, with the same row order (left fragment, then right continuation, for rows 1–6).

The verdict is REVISE because the frozen transcription differs from the scan in **10 places**:

- **Two signs were missed** in one word (finding 1).
- In **eight places** the writer's own slip was silently normalized to the expected letter (findings 2–5). This happened even though the solver keeps the comparable slip SECONA literal.

None of this changes the sense of the message. The name form ANDULKA → ANDULIČKA and the literal record do change.

## What I verified and how

1. **The documented command.** `python3 -I ciphers/hcp-1526/work/decode.py` runs and passes its hash and round-trip checks. It prints the 16 rows exactly as in "Literal base-letter candidate" (495 units, 502 letters, 7 CH). The script is read-only. I did not run `make-record.py` or `make-controls.py`, because they write files.
2. **Independent decoder.** `review/work/my_decode.py` holds my own sign-by-sign transcription and my own statement of the key; it imports nothing from the solver. It reads the solver's `transcription.txt` only as data, to print a diff. Run it with `python3 -I ciphers/hcp-1526/review/work/my_decode.py`:
   ```
   R03 VANOCNI SECONA JIZ V PRNEM PROUDU. MAM
   R06 SVE CRDECKO, KDERE NYNI ZACE MISTO
   R09 HODNE SETRIDI, JAKO MNE DO MA ANDULICKA
   R10 SAMA TAK DUTKLIVA RADILA. PROSIM JI O TO.
   R13 VZDIT JSEM BYL TEMER STALE SAM. VZPOMINAL
   R15 PUS POSILA TI TVUJ PEPOUS, KDERY SE VELICE
   (all other rows identical to the solver)
   rows=16 units=497 base_letters=504 CH=7 F=1
   ```
   The key is one-to-one, and every sign on the card resolves under it. No sign needs two values. The 23 labels (22 family classes plus the singleton v) all occur. My differences all come from the transcription, not from the key.
3. **Reading the scan.** The image is rotated 90° counter-clockwise with `ffmpeg -vf transpose=2` (`review/work/up.png`). I made row crops for all 16 rows (`row01a/b … row16a/b.png`, `v-r*.png`, 4×–4.5×) and detail crops of every disputed word (`z-*.png`, 7×–14×). Equal-scale comparison sheets are in `cmp-TD-final.png`, `cmp-kz.png` and `cmp-1-4.png`. `profile.py` locates rows from an ink profile. `ascii.py` (in `../../hcp-1527/review/work/`) prints pixel-darkness dumps. Both need a raw dump made first: `ffmpeg -i up.png -f rawvideo -pix_fmt gray up.gray`.
4. **Search for missed cipher text.** The picture side has the 16 rows and the plain date `12./XII.1903.`. The address side is ordinary script plus postal printing. I found no cipher region the solver missed. Two signs *inside* a word were missed (finding 1).
5. **Context.** 12 December 1903 was a **Saturday**, so "ode středy opět v úřadě" means since Wednesday 9 December. This fits HCP 1529 (1 Dec 1903). There the same writer is at home with flu and expects to return "ve čtvrtek nebo v pátek". It also fits the follow-up HCP 1527 (19 Dec, Christmas wishes). "Vánoční sezona" in mid-December fits as well.
6. **Prior solutions.** The portal attached no solution. The published Egorov key (`batches/easy-2026-10-28/published-anna-ticha-key.txt`) is generic and disclosed, and it lists no reading of pc207. I found no undisclosed use of a published reading.

## Findings

1. **major (missed signs): R09 `ANDULKA` is `ANDULICKA` (Andulička).** See `review/work/z-andulicka-final.png` and `z-andulicka-ctx.png`. After `6 m t 2 8` the card has the digit-4 I-form and then the angular s (= C), followed by g and 6: `6mt284sg6`. The solver's `6mt28g6` drops `4s`. The diminutive Andulička is the natural form in this letter. Fix the transcription, the literal and editorial text ("má Andulička"), the Slovak translation, and the counts (497 units, 504 letters).

2. **major (literal layer silently normalized): the crossed D-sign is written where T is needed, four times.** See `review/work/cmp-TD-final.png`. The writer separates the two signs clearly: STŘEDY (R02, `cdh5t1`) has the looped d-sign for T and the crossed t-sign for D in the same word (panels 1–2). The crossed form appears in:
   - R06 `KTERE` 2nd sign (panel 3, also `v-r06b.png`) → literal **KDERE**
   - R09 `SETRITI` 2nd T (panel 6; the 1st T, panel 5, is a correct looped d) → literal **SETRIDI**
   - R09 `TO` in `MNE TO MA` (panel 7, `z-to-r09.png`) → literal **DO**
   - R15 `KTERY` 2nd sign (`v-r15b.png`) → literal **KDERY**

   The intended words are certain. But the solver keeps SECONA literal on exactly this kind of evidence (a same-hand sign comparison), and the same rule must apply here. Record them literally and mark the intended letters editorially, e.g. `K[D→T]ERE`.

3. **major (same issue, S/C): the angular C-sign is written where S is needed, twice in R06.**
   - R06 `SRDECKO`: the first sign is the angular s-shape (= C), identical to the 5th sign of the same word (`z-srdecko-final.png`, `v-r06a.png`). Literal **CRDECKO**. Compare R08 `SRDECKO`, which correctly begins with the round c (`z-andulicka-ctx.png`, upper line).
   - R06 `ZASE`: the third sign is the angular s, not the round c (`z-zase-final.png`, `z-zase10.png`). Literal **ZACE**.

   This is the same distinction the solver uses to justify literal SECONA. That makes the uneven treatment more visible: SECONA is kept, CRDECKO and ZACE are normalized.

4. **minor: R03 `PLNEM` is literally `PRNEM`.** See `review/work/z-plnem-proudu2.png`. The second sign has a tall looped ascender and a hump. It is the h-sign (= R), identical to the h in `PROUDU` (`bh32t2`) right next to it, and not the 8-digit L. The literal is **PRNEM**; the intended *plném* is certain.

5. **minor: R10 `DUTKLIVE` ends in 6, literally `DUTKLIVA`.** See `review/work/v-r10b.png`, `z-dutklive-end.png`. The final sign is the closed 6 (= A), not 5 (= E). Literal **DUTKLIVA** for *důtklivě*.

6. **minor: R13 `VZDYT` has the digit-4 I-form, literally `VZDIT`.** See `review/work/z-vzdyt-final.png`. The 4th sign of `fqt4d` has the same underbarred 4-shape as the I in ANDULIČKA. It is not the footed 1 of `BYL` in the same row. This is an i/y spelling slip of the kind HCP 1529 keeps literally (MISLENI). It should be recorded the same way.

7. **minor (agreement, for the record).** I agree with the two disclosed points:
   - **SECONA.** The third sign is the angular C-form (`z-secona-r03.png`).
   - **DOUFAM.** The shallow open v in `t32v6n` is a distinct singleton, unlike the tall looped f = V (`z-avsak-doufam-r04.png`). F is the only value that makes Czech, and it is disclosed as a contextual assignment. That disclosure is adequate.

   I also agree with ODE, OPET, TAZE (q = Z with long descender, `cmp-kz.png`), the seven capped CH units, and the uncapped H in BEHEM.

8. **minor (method).** Findings 2–6 show a pattern: this writer often slips between his paired signs (t/d, c/s, 1/4). The report should say this in one sentence and keep a "writer's slips" list, as was done for HCP 1017. The reproduction command only replays the manual transcription. The solver says so correctly, and the round trip cannot catch any of findings 1–6.

## Required for closing

- Transcription R09: insert `4s` in ANDULICKA. Update counts (497 units / 504 letters) and `positions.json`.
- Record literally, with editorial marking: PRNEM, CRDECKO, KDERE, ZACE, SETRIDI, DO (for TO), DUTKLIVA, VZDIT, KDERY.
- Update the literal text, editorial text ("Andulička"), Slovak translation and the uncertainty/writer-slip section.

These are corrections of the record. The reading and the key stand. If they are made as listed, I see no need for another review round.

## What I could not verify

- Whether the slips in findings 2–6 would look different on the physical card or a higher-resolution scan. At the portal's 1024 px they are as described.
- The postmark text and dates on the address side. I did not read them.
- Whether the shallow v = F is the same class as the published G16. No glyph photographs are available. I agree it remains a contextual singleton.
- Worldwide novelty. I relied on the solver's bounded checks of the register and the Egorov index.
