# HCP 1369 / pc_hcp_50 — Caesar (+1) love postcard, 26 Jul 1907

Status: **whole message read: 41 of 41 enciphered letters, none restored; review 1 verdict REVISE, findings addressed (see the last section).** Two abbreviation groups and the trailing `t..` are kept literal and unexplained (see Uncertainties).

## Origin

HC Portal cryptogram 1369 (`pc_hcp_50`), portal status *Not solved*, no attached transcription or solution (`SOURCES.md`, `source/metadata.md`). Picture side: printed "The Bridge, Knaresborough", no handwriting. Address side: Boots Cash Chemists "Pelham" Series card, halfpenny Edward VII stamp, postmark WIMBORNE / JY 26 / 07, agreeing with the portal date 1907-07-26. That day was a Friday, matching the plain heading "G. H. Friday". Addressed to Mr W. Abbott, Stokelake Farm, Chudleigh, Devon (the portal's "W. Abboú" is a misreading; metadata left unchanged). The message is on the address side (rotate 90° counter-clockwise, `work/crops/msg.png`). The disc and building logo on the scans are a scanning overlay. No published solution of this card was found or used.

## Cipher and key

Monoalphabetic Caesar shift: each plaintext letter is written as the **next** letter of the alphabet; decrypt by subtracting one. This is the same key and hand as the sister cards hcp-1376 and hcp-1386…1407.

```
Cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

The heading "G. H. Friday" and the date "July 26th 07" are ordinary writing. `M-h` (twice), `M. & L.` and the trailing `t..` are kept literal; whether any of them is enciphered is open.

## Transcription and plaintext (all ciphertext on the card)

| Ciphertext | Literal plaintext |
|---|---|
| Nz. Pxo [M-h] Cpz. | MY. OWN [M-h] BOY. |
| Tdippm usfbu. | SCHOOL TREAT. |
| Jo. Qbsl. up. | IN. PARK. TO. |
| Ebz. [M. & L.] [t..] | DAY. [M. & L.] [t..] |
| zpvs. Pxo [M-h] > | YOUR. OWN [M-h] > |
| (after the date on the bottom line) Hjsm | GIRL |

41 letters read and decoded, 0 restored; 7 letters kept literal (M, h twice; M, L once; t once, tentative). The ampersand, the dots and `>` are not letters.

English (original language; punctuation editorial): *"My own M-h boy. School treat in park to-day. M. & L. t.. your own M-h girl."*

Slovak: *„Môj vlastný M-h chlapec. Dnes školská slávnosť v parku. M. & L. t.. tvoje vlastné M-h dievča."*

"School treat" is the period term for an outing or party given to schoolchildren.

## Command (from the repo root)

```sh
python3 -I ciphers/hcp-1369/work/decode.py
```

It checks the SHA-256 of the two `source/` scans and the two `work/hires/` originals, decodes every token of `work/transcription.json`, checks the inverse round trip, and prints the plaintext above with the counts. Crops are regenerated with `work/crop.py` (needs PIL; run from `work/`).

## Uncertainties

1. **`M-h` is unexpanded and its letters are a visual call.** Both instances have three downstrokes in the capital (`work/crops/z_nl1.png`, `z_nl2.png`), against two in the N of `Nz` (`z_nz.png`), so I read M, the criterion used on hcp-1383. The second letter is a tall stroke with a small arch at the foot, clearly different from the capital L of `M. & L.` on this card (`z_nal.png`, `z_tail.png`), so I report it as h. Sister cards report this slot variously as `N-L`, `M-L`, `M[h]` and `N.-1`, and with an h-like second letter as `N-h.` (hcp-1349), `N. h.` (hcp-1360, 1371) and `M-h.` (hcp-1361); it is probably the same group. The same-day card hcp-1368 reports `N. L.`, but its crops (`hcp-1368/work/crops/cmp_N.png`) show the same pen forms as here, so the M/N and h/L disagreement between the two cards is a difference of transcription, not of ink. It is unresolved. None of these cards is FINAL. Shifted it would give L-G, which I do not expand. It stands before both BOY and GIRL.
2. **`M. & L.`** is the group sister cards give as `N. & L.`. The capital here has the same three-downstroke build as in `M-h`, so I report M. Its meaning is unknown, and its usual sister-card sentence has "from" after it, which is absent here.
3. **`t..` after `L` in line 4 (`review/work/a_l4b.png`, `work/crops/z_tail.png`).** A curved stem, a short dash detached at its upper right, one dot below the dash, and two dots higher, near the end of the row above. I take this as the recurring `t..` of the correspondence, kept literal (shifted t would be S). Same slot: `N. & L. t` on the same-day hcp-1368, where the same stem carries an attached bar (`hcp-1368/work/crops/z_dot_t.png`); a curved stem with a detached dash on hcp-1359 (`z_Lt.png`, the closest form); `M & L. t..` on hcp-1361; `& L t..` on hcp-1363 and `& Lt..` on hcp-1371. These cards are not FINAL, so this is a recurring pattern, not an accepted reading. Doubts: the bar is detached here, so c is not fully excluded; the dots are placed differently from hcp-1361, where two dots lie under the bar, so their role is unknown. Its meaning is unknown and no word of the message depends on it.
4. **The `>` mark** ends the penultimate line. I take it as a pointer to `Hjsm`, which sits after the date on the bottom line. The same-day card hcp-1368 ends the same way (`zpvs. Pxo. N. L.` / `Hjsm.`), which supports this order.
5. **`Hjsm`** is pale. H and the very long j are clear; s and the flattened m are faint but visible, the flattened m is also noted on hcp-1386 and hcp-1376 (`work/crops/b5.png`).
6. **`Tdippm`.** The third sign is one short downstroke with no dot visible, so i rather than u (`z_school.png`). The second p and the m are pale because the pen was running dry. A fine hairline runs from the second p to the first hump of the m (`review/work/b_ppm.png`), so the word is joined.
7. **`Qbsl`.** The capital is 9-shaped (a closed bowl with a long tail, `z_park.png`). Q is the only value that gives a word, and the shape agrees with the 9-shaped q of `qptu` on the same-day hcp-1368 (`hcp-1368/work/crops/r_l3a.png`: closed bowl, long tail, loop). hcp-1349 reads a different, 2-shaped capital as Q, so this is not the only form claimed in the series. The final l is pale, with a looped top.
8. **`zpvs`.** The first sign is the z of `Nz` and `Cpz`, which looks like a numeral 2. Unlike `2 hrs.` on hcp-1376, the rest here is p, v, s, not plain "hrs". The pale p has a long stem, and the v and s are pale but clear (`z_your.png`).

## Why it is correct

One fixed shift turns every enciphered token into English, including SCHOOL (with its double letter), TREAT and PARK, none of which is a stock formula on the sister cards. The message makes a coherent short sentence between the couple's usual salutation and closing ("My own … boy", "your own … girl"). The weekday and postmark agree with the heading and date, and the card shares the recipient, address and town of posting with the sister cards. The card hcp-1368 of the same day has the same plain heading "G. H. Friday", the same date, the same 10 PM postmark and the same closing structure.

## Response to review 1

Verdict REVISE. All five findings accepted after looking at the crops myself; no enciphered letter changed.

1. **major, `t..` omitted: fixed.** I compared `review/work/a_l4b.png` with `hcp-1368/work/crops/z_dot_t.png`, `hcp-1359/work/crops/z_Lt.png` and `hcp-1361/work/crops/after_L.png`. The stem and detached dash match hcp-1359 closely. `{t..}` is now in `work/transcription.json`, in the table, in the count (7 kept literal, was 6) and in both translations. Uncertainty 3 is rewritten with the parallels and the doubts. One addition to the review: the dots do not sit as on hcp-1361, which I record.
2. **minor, `M-h` evidence: fixed.** Uncertainty 1 now cites hcp-1349, 1360, 1361, 1371 and the same-day hcp-1368, and states the disagreement. On `cmp_N.png` the pen forms match this card, so I keep M-h here and do not claim hcp-1368 is wrong or right.
3. **minor, Q: fixed.** Uncertainty 7 cites `qptu` on hcp-1368 and the other form on hcp-1349.
4. **minor, hairline: fixed.** `b_ppm.png` shows it. Uncertainty 6 corrected.
5. **minor, same-day card: fixed.** Added under Why it is correct and in Uncertainty 4. The 10 PM on this card is confirmed on the address scan.

The reviewer also noted that "0 restored" in `work/decode.py` was a fixed string. It now comes from `restored_tokens` in the transcription (empty). `python3 -I ciphers/hcp-1369/work/decode.py` re-run: hashes OK, line 4 reads `DAY. M. & L. t..`, 41 letters decoded, 0 restored tokens, 7 kept literal.

## Credits

All work on this card by Claude Opus 5.5 acting as solver, 2026-10-30. Scans captured by the orchestrator the same day. The key and formulae were compared with sister cards hcp-1376, 1383, 1386 and others, on which earlier work is credited in their own files. No GPT work on this number exists.
