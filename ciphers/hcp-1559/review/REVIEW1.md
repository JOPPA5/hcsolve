REVISE

# Review 1 – HCP1559 (pc_hcp_240), Anna Tichá / Pepouš family

Reviewer: Claude Opus 5.5, 2026-10-29. Only `review/` was written; everything I made is in `review/work/`.

## What I verified and how

1. **The command runs.** `python3 ciphers/hcp-1559/work/decode.py` exits with 0 and writes nothing. It prints 5 rows, 214 mapped units, 5 CH, 219 letters and 4 unknown spans. Its output still contains `<UNK:U01>` … `<UNK:U04>` (see finding 1).
2. **Independent decryption.** `review/work/mydecode.py` is my own substitution script. It uses the family key from `ciphers/hcp-1545/work/key.json`, with labels mapped onto this card's class labels. I ran it on `work/transcription.txt` (output: `review/work/mydecode.out`). The output matches `work/literal.txt` letter for letter. There is one apparent difference: 1545 labels J as `7`, while this card (like 1520) labels it `y`. Once the label is translated, J = J. `work/key.json` is byte-identical to `ciphers/hcp-1520/work/key.json` (checked with `cmp`). It covers every class in the transcription. The only sign it does not cover is the k-shaped G in U02.
3. **Transcription against the scan.** I rotated `source/picture.jpg` 90° CCW myself and made my own crops: `rows_left.png` and `rows_right.png` at 4x, `R02a.png` at 6x, `R05a.png` at 4x, `U01.png`/`U01b.png`/`U02.png`/`U03.png`/`U03b.png`/`U04.png` at 8x, and red-channel contrast crops `U02c.png`/`U03c.png` at 12x. I compared all five rows sign by sign at 4x, and found no discrepancy in the resolved material. I checked these readings in particular:
   - `b6m` PAN against `ph6dh6` BRATRA
   - `c4n28g6` SIMULKA
   - `6m2ms5` ANUNCE
   - `q6c486` ZASILA
   - the underlined `q4dh6` ZITRA
   - the closing `b5b32c` PEPOUS

   The root QA correction KDE→ZDE (R02 initial q/Z, not g/K) is supported: the R02 initial has the open hooked tail of the ZE/ZITRA q, not the closed lower loop of the SIMULKA/DRAHOUSKU g.
4. **Language and context.** The plaintext is fluent Czech of about 1903 with the typical accent-less spelling of this family. *jest zde*, *neodeslal jsem* and *psánko* match the period and the family: PSANKO occurs on HCP1525 and HCP1526, SPOLECNOST on HCP1525, and SVAGRA with the same k-shaped G on HCP1541. The sender (Pepouš), the recipient (Anna Tichá, teacher in Žirovnice, "Anunce"), the date 29.III.1903 and the Prague / Žirovnice postmarks fit the family.
5. **Disclosure.** The known-key transfer, the Maxim Egorov partial study and the earlier GPT plus Claude collaboration are credited. I found no target-specific published solution.

## The four completed spans, judged on the pixels

- **U01 → NEODESLA[L]** (`review/work/U01b.png`): **supported.** After `c86` there is a fourth sign with two stacked lobes, the same as this hand's `8`. It is smudged but clearly an 8/L. The reading is visible, not forced.
- **U02 → SVA G [R]** (`U02.png`, `U02c.png`): **G supported, R restored.** The k-shaped sign is clearly visible and matches the family G on HCP1541 (SVAGRA). After it, the smear contains one dark lower stroke that cannot be identified. R comes from context only (*švagr mého bratra*). That is plausible, but it is a restoration.
- **U03 → SPOLECN[OST]** (`U03b.png`, `U03c.png`): **largely restored.** Three sign positions can be seen.
  - The first trace looks about as much like `4`/`5` as like `3`.
  - The second is a small, apparently closed loop, not clearly this hand's open `c` hook.
  - The third is a `6`/`b`/`d`-like form with a stem.

  The count of three fits OST, and *dělám společnost* is the only idiomatic completion. Even so, the letters are chosen from context, not read.
- **U04 → PSANK[O]** (`U04.png`): **plausible.** A small 3/2-like trace stands before the dot. One sign is consistent with O, and PSANKO is a family word. Treat it as read with low confidence.

## Findings

1. **[major] The single command does not reproduce the claimed plaintext.**
   - The "Completion and handover" section claims a complete reading: NEODESLAL, SVAGR, SPOLECNOST, PSANKO.
   - None of this reached `work/transcription.txt`, `transcription.json`, `literal.txt`, `key.json` or `decode.py`. The command still prints four `<UNK>` spans, and the counts (214/219) are those of the partial reading.
   - The k-shaped G is not in `key.json`, although the solution now relies on it.
   - The earlier sections of SOLUTION.md still say "partial", "no DONE / no handover" and "not filling the four spans". This contradicts the closing section.

   Fix:
   - Encode the completions in the records, marking readings as read or restored (for example `868`, `cf6G[h]`, `cb385sm[3cd]`, `bc6mg(3)`).
   - Add G to the key with the HCP1541/1553/1554/1570 attestation.
   - Make the command print the final text.
   - Reconcile the status text and counts.
2. **[major] Restorations are not marked in the presented plaintext.** The editorial Czech and the Slovak give "švagr", "společnost" and "psánko" as plain text. The table does call R and OST "restored", but the plaintext itself must bracket the restored letters. At least these should be bracketed: švag[r], společn[ost], and psánk(o) (low confidence). The reader then sees what is read and what is supplied. U01's L can stay unbracketed.
3. **[minor] Name accents added silently.** The completion section writes "Šimulka" with Š, but the earlier sections explicitly kept "simulka" with no inferred accents. Either justify the Š (nothing in the cipher marks it) or keep "Simulka" and state that the accent is editorial.
4. **[minor] Unclear U03 glyph classes.** The note "traces fit `3 c d`" is stronger than the pixels allow (see above). Say that the three positions are seen but that their classes are inferred.
5. **[minor] Stale wording.** The "Uncertainty" table and the reproduction paragraph still describe the four spans as unknown and say that "no full-card percentage" applies. Update them together with finding 1.

## What I could not verify

- The identity of "Simulka/Šimulka" and of the brother. No external source was checked.
- Whether the smudges in U01–U04 are accidental smears or deliberate erasures by the writer. The pixels cannot decide this.
- The address side was checked at overview scale only (ordinary cursive and postal print, no cipher seen).

The reading as a whole is correct. Only the record keeping and the marking of restorations need fixing, so the verdict is REVISE, not REJECT.
