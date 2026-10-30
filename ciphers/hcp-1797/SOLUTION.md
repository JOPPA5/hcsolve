# HCP 1797 / pc_hcp_478 — Caesar (+1) love postcard, 29 Jan 1908

Status: **PARTIAL solution. The message is read except one three-sign group (`Wbm`, weaker alternative `Wbn`), the object of "I am sending …"; that group is reported literally and is NOT interpreted.** Handed to review as DONE1; review 1 verdict REVISE, addressed below. Solved by Claude Opus 5.5 on 2026-10-30; there was no earlier work on this number. No published solution was found or used; the portal lists status Not solved with no attached solution.

## Origin

Portal 1797, recipient "W. Abboú" [sic], date 1908-01-29. Picture side: printed Tuck's Oilette "Lynmouth. Tower and Harbour", no handwriting. Address side: Mr W. Abbott, Stokelake Farm, Chudleigh, S. Devon; halfpenny stamp; postmark WIMBORNE, 10 PM, JA 29, 08. 29 Jan 1908 was a Wednesday, agreeing with the heading. Message on the left of the address side, read after rotating 90° CCW (`work/reading.png`). Same hand and formulas as the Abbott cards; nearest in date are hcp-1402 (28 Jan) and hcp-1404 (30 Jan). Language: English.

## Cipher and key

Caesar: each plaintext letter is written as the next letter. Decrypt by subtracting one.

```
Cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

The heading and "Sat. Morning." are in clear, as this writer wrote "Sat:" and "Wimborne" in clear on hcp-1377. Initial groups are kept literal, as on the sister cards.

## Transcription and plaintext

| Written | Reading |
|---|---|
| G. H. Wednesday *(clear)* | G. H. Wednesday |
| Nz. Pxo E. L. Cpz. | MY. OWN [E. L.] BOY. |
| J. bn. Tfoejoh | I. AM. SENDING |
| **Wbm** Gps. | **[unresolved]** FOR. |
| Sat. Morning. *(clear)* | Sat. Morning. |
| Nz. Nu. & L. Gspn | MY. [Nu. & L.] FROM |
| Zpvs. Pxo. El. | YOUR. OWN. [El.] |
| Hjsm. | GIRL. |

English: *"G. H. Wednesday. My own E. L. boy, I am sending [Wbm] for Sat. morning. My [Nu. & L.] from your own [El.] girl."*

Slovak: *„G. H. Streda. Môj vlastný E. L. chlapec, posielam [Wbm] na sobotné ráno. Moje [Nu. & L.] od tvojho vlastného [El.] dievčaťa."*

## Command (from the repo root)

```sh
python3 -I ciphers/hcp-1797/work/solve.py
```

Checks SHA-256 of the images, decodes `work/transcription.json`, round-trips each enciphered token, prints the reading and the weekday check. 38 enciphered letters decode; the unresolved group is excluded from that count.

## Uncertainties

1. **`Wbm` (main residual, content word; corrected in review from `Wbn`).** Crops: `work/crops/w_ham8.png`, comparison `cmp_cap.png`, reviewer's `review/work/wbn.png`, `wbn_tail.png`.
   - The first sign is built like this writer's clear W (hook, stem, spur, second stem), compare the "W." of the address in `cmp_cap.png`; it differs from his N and his H. A pale long bar starts left of the top of the second stem and runs right over the whole group, like the bar on the W of "Wednesday". A reader could still take that bar as a T-cross on the second stem, so W is the best reading, not a certainty.
   - The second sign is closed at the base with a tall stem, like b in `bn` on line 3, but d cannot be excluded: the incoming ligature from the W closes the loop. `Wdm` gives VCL, no word, so b is preferred on sense only.
   - The rest shows three separate legs and a long exit stroke, all visible through the watermark ring; nothing is hidden. The writer's n has two small humps (`bn`, `Gspn`), his m three (`Hjsm`), so m is preferred. His minims vary, so `Wbn` stays as the weaker alternative.
   - If shifted it gives VAL (alternative VAM); if clear, it is no word I can establish (the writer does use clear names, so a clear name or abbreviation is possible). VAL could be a name, but nothing on the card proves it. I tried and rejected HAM, MEAL, MAM and JAM: each needs a first sign that is not there. Nothing is substituted. A grep of the sister SOLUTION.md files found no matching group.
2. **Initial groups.** `E. L.`, `Nu. & L.`, `El.` are literal. `Nu.` is N with a small u-like sign standing on the baseline after the stem, where sisters have N. or M. (compare `Mu` on hcp-1405 and `N.-1` on hcp-1407). `El.` could be read `E. L.` with the dot lost.
3. **"Sat. Morning." as clear.** The word has a descender as its last sign, no h ascender, and no p descender, so it is not `Npsojoh`; its "Sat" has the same form as the clear "Sat:" on hcp-1377. `Tbu` would give the same word anyway.
4. **Minims and small signs.** `bn` could look like `bu` (AT), as noted on hcp-1377; AM is the only sense. The e of `Tfoejoh` is a small c-like sign (with c: TENCING is no word; hcp-1392 has the same word). The z of `Cpz` on line 2 is a faint flat stroke; BOY is the only sense and matches the sisters. The heading initial is G or C.
5. **Watermark.** The portal's grey disc overlies parts of lines 2–6; every sign was read through it, including the end of the unresolved group.

## Why this is believed correct

One fixed shift used across this correspondence yields English for every enciphered group with no adjustment. Salutation and closing match hcp-1402 and 1405; hcp-1407 matches in its closing only (its salutation is `Nz. Pxo. Efbsftu.`); `Tfoejoh` recurs on hcp-1392; `J. bn` on hcp-1377 and 1403. The Wednesday heading agrees with the postmark date.

## Response to review 1

Verdict REVISE. All findings accepted after looking at the reviewer's crops; none changes a decoded word.

1. **Fixed (major).** `wbn_tail.png` shows three legs and an exit stroke through the ring, against two humps in `m_bn.png` and three in `m_hjsm.png`. The group is now `Wbm` in `work/transcription.json`, this file and the report. `solve.py` prints VAL and the alternative `Wbn` = VAM. Uncertainties 1 and 5 corrected. Group stays uninterpreted.
2. **Added (minor).** The pale bar over the group and the spur are in Uncertainty 1, with the T-cross caveat. HAM, MAM and JAM stay rejected.
3. **Added (minor).** b/d disclosed in Uncertainty 1, with `Wdm` = VCL and b preferred on sense only.
4. **Fixed (minor).** Uncertainty 2 no longer says "raised-looking"; `m_nul.png` shows the sign on the baseline.
5. **Fixed (minor).** The z of `Cpz` is in Uncertainty 4.
6. **Fixed (minor).** The sister claim now separates hcp-1407; its line 1 in its SOLUTION.md is `Nz. Pxo. Efbsftu.`.
7. **Accepted.** The status line and the report say partial. No `register-entry.txt` is written, as README step 7 requires for a partial solution.

Reproduction re-run after the changes: four hashes OK, 38 enciphered letters, 1908-01-29 is a Wednesday.
