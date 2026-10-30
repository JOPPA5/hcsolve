# HCP 1406 / pc_hcp_87 — Caesar −1 postcard (complete reading)

**Status: the whole message is read. Handed to review (DONE1).** Three abbreviation groups (`E. L.` twice, `N. & L.` once) are kept literal, as on the sister cards. No letter is restored.

## Source and context

- Portal record https://crypto.hcportal.eu/dashboard/cryptograms/1406 (name pc_hcp_87), rendered 2026-10-26: status **Not solved**, language Unknown, recipient "W. Abboú", no transcription or solution attached (see `SOURCES.md`, `source/metadata.md`). No published solution of this card was found.
- Picture side: Tuck's "Oilette" postcard 7280, *Scottish Rough Seas*, Barra Head; no handwriting.
- Address side (read on `work/crops/addr.png`, ordinary writing): Mr. Abbott, Stokelake Farm, Chudleigh, S. Devon. (The earlier partial reading "Whiteway Farms" is wrong; the word is the same "Stokelake" as on hcp-1397.) The portal field "W. Abboú" is left as recorded. Halfpenny Edward VII stamp, postmark WIMBORNE … 10 PM; day/month/year not legible (`work/crops/pm.png`).
- Heading in ordinary writing: "C. H. Sunday." The card belongs to the run of cards to W. Abbott (hcp-1386…1407, 1907–08) written with the same shift and the same formulas (e.g. hcp-1386: "My own E. L. boy … My N. & L. from your own E. L. girl").

## Cipher and key

Monoalphabetic Caesar shift: each plaintext letter is written as the **next** letter of the alphabet. Decryption subtracts one.

```
cipher: ABCDEFGHIJKLMNOPQRSTUVWXYZ
plain:  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

Punctuation, hyphen and quotation marks are written in clear.

## Transcription and plaintext (all writing on the message side)

Read after rotating `source/address.jpg` 90° counter-clockwise.

| Ciphertext | Plaintext |
|---|---|
| C. H. Sunday. *(clear)* | C. H. Sunday. |
| Nz. Pxo. E. L. Cpz. | MY. OWN. [E. L.] BOY. |
| Mfuufs uijt npsojoh | LETTER THIS MORNING |
| wfsz ojdf. | VERY NICE. |
| J. bn. joeppst | I. AM. INDOORS |
| bmm "up-Ebz." | ALL "TO-DAY." |
| Nz. N. & L. gspn. | MY. [N. & L.] FROM. |
| Pxo. E. L. Hjsm. | OWN. [E. L.] GIRL. |

64 enciphered letters, all decoded with the single key.

**English:** "C. H., Sunday. My own E. L. boy, letter this morning very nice. I am indoors all 'to-day'. My N. & L. from own E. L. girl."

**Slovak:** „C. H., nedeľa. Môj vlastný E. L. chlapec, list dnes ráno veľmi pekný. Celý ‚dnešok' som vnútri. Moje N. & L. od vlastného E. L. dievčaťa."

## Reproduction (one command, from the repo root)

```sh
python3 -I ciphers/hcp-1406/work/decode_v2.py
```

It checks the SHA-256 of every file in `source/` against `work/source-sha256.json`, decodes `work/transcript-v2.json` with the key above, prints the plaintext, and asserts that it equals the expected text. Output ends with `-- source hashes OK; 64 enciphered letters decoded with one key (shift -1); abbreviations E. L. / N. & L. kept literal`. The transcription itself is manual (from the crops in `work/crops/`), not OCR.

## Uncertainties

1. **Abbreviations `E. L.` and `N. & L.`** are kept literal. Their shifted values would be D. K. and M. & K.; their meaning (e.g. "ever loving" for E. L.) is not established and it is undecided whether they are shifted at all. Same treatment as hcp-1386/1397/1403. The `L` is a narrow slanted stroke with a small foot loop (looks like `1`/`l`), the writer's capital L on those cards (compare `ciphers/hcp-1386/work/crops/band6.png` with `work/crops/cl2.png`).
2. **`Cpz` (BOY)**: the final `z` is crossed by the printed grey "O" of the cipher-wheel overlay on the scan (`work/crops/gr3c.png`); the brown ink stroke is visible and has the writer's small `z` form, but it is the least clear letter on the card. The same greeting `Nz. Pxo. E. L. Cpz.` opens hcp-1386.
3. **`Pxo`** in both places: the `x` is a small cross on the stem of the large flourished P, so the group can look like "Fo"; this is the same construction as `Pxo` on hcp-1386 (`band6.png`).
4. **`Ebz`** resembles "E62" (cursive b like 6, z like 2); with `up-` and the quotation marks it reads "to-Day", as on hcp-1397/1407.
5. A small check-mark ("v") below the end of line 2 (`work/crops/mk.png`) is the dot and turned-up descender of the j in `npsojoh`, not a separate sign.
6. Date: only "Sunday" is written; the postmark date is illegible, so no year is claimed (the series is 1907–08).
7. Grammar of the closing ("My N. & L. from own E. L. girl", no "your") is as written.

## Why this is correct

One fixed key turns every enciphered group into English with no exceptions (64/64 letters), giving a coherent short love-note with the same salutation and closing formulas as the sister cards addressed to the same recipient, and the same quoted "to-Day" device. Long words such as `joeppst`→INDOORS and `npsojoh`→MORNING leave no room for an alternative key.

## Credit

Download, metadata capture, key identification and a 49-letter partial transcription (with MORNING, DEAR, and the closing left open) by the OpenAI GPT solver (GPT-6 Astra / GPT-6.1 Sol), 2026-10-26 (`work/transcription.json`, `work/decode.py`). Completion by Claude Opus 5.5 acting as solver, 2026-10-29: re-transcription from the pixels, the greeting `E. L. Cpz` (the earlier "Efbs/DEAR" guess was wrong), `npsojoh` frozen, the closing `Nz. N. & L.` and `Pxo. E. L.` read by comparison with hcp-1386, address corrected, new decoder `work/decode_v2.py`.

## Response to review 1

Review 1 (Claude Opus 5.5, verdict **ACCEPT**) confirmed the whole reading independently (64/64 letters, same key). Response to each finding, by Claude Opus 5.5 acting as solver, 2026-10-29/30:

1. **Unrecorded marks near lines 2/3 (minor) – accepted, recorded.** Re-checked on the reviewer's crops `review/work/q3.png` and `review/work/r2.png`/`r3.png` (rotated scan, enlarged). Two small slanted ticks stand immediately before `wfsz` at the start of line 3; they have the form of an opening quotation mark, so the line may be meant as `"wfsz ojdf.` ("very nice"), the same quoting device as `"up-Ebz."`. No matching closing mark is visible after `ojdf.` (`r3.png`), so this is recorded as a *possible* opening quote, not added to the plaintext. A further tiny dot/tick stands left of the "V" below the end of line 2 (`q2.png`); it is read as the dot of the j of `npsojoh` or a stray mark, not as a letter. Neither mark is a letter; the decoded text is unchanged.
2. **Weak `z` in `Cpz` (minor) – agreed.** Uncertainty 2 already says the `z` is the least clear letter; the wording is sharpened here: only a short ink stroke and a dot are visible under the printed grey "O" of the overlay, and the reading BOY rests partly on the identical formula `Nz. Pxo. E. L. Cpz.` of hcp-1386. The report states it this way.
3. **E. L. / N. & L. (minor) – no change.** Kept literal, as on the sister cards; disclosed in uncertainty 1 and in the report.

Re-run after the response: `python3 -I ciphers/hcp-1406/work/decode_v2.py` still prints the eight lines and ends with "source hashes OK; 64 enciphered letters decoded with one key (shift -1) …". No file in `work/` needed changing.
