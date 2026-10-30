# HCP 1367 / pc_hcp_48 — Caesar (+1) birthday postcard, 25 July 1907

Status: **whole message read; review 1 verdict REVISE, findings addressed (see Response to review 1).** Two letter-level slips of the writer and one abbreviation are disclosed below.

## Origin

HC Portal cryptogram 1367 (`pc_hcp_48`), status *Not solved*, no attached transcription or solution (`source/metadata.md`, `SOURCES.md`). No web search for a published solution was run; none was met. Picture side: printed "Shrine of Edward the Confessor, Westminster Abbey", no cipher. Address side (Valentine's Series): halfpenny Edward VII stamp, postmark WIMBORNE 10 PM JY 25 07; addressed in plain to Mr W. Abbott, Stokelake Farm, Chudleigh, Devon (portal spells the recipient "W. Abboú"). The message is on the left of the address side, turned 90 degrees (`work/crops/reading.png`). Recipient, place, hand and formulae match the Caesar cards hcp-1386…1407.

## Cipher and key

Monoalphabetic Caesar shift, same key as the sister cards: each plaintext letter is written as the **next** letter. Decrypt by subtracting one (A→Z).

```
Cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

Left plain by the writer: heading `G. H. Thursday.` and the date `July 25th 07`. `M-h` is kept literal as an abbreviation.

## Transcription and plaintext (all ciphertext on the card)

| Ciphertext | Literal plaintext |
|---|---|
| Nz. Pxo. Mpwjoh Cpz. | MY OWN LOVING BOY |
| Wfsz. nboz. | VERY MANY |
| Ibooz. Sfufsot. | HANNY RETERNS (intended HAPPY RETURNS) |
| Pg uif Ebz. | OF THE DAY |
| Zpvs. Pxo M-h. | YOUR OWN [M-h] |
| *July 25th 07* Hjsm. | *(plain date)* GIRL |

53 enciphered letters (`work/decode.py` prints the count); all decoded by the one key.

Plaintext (English; the portal lists the language as Unknown), with both slips normalised:

> G. H. Thursday. My own loving boy. Very many happy returns of the day. Your own M-h girl. July 25th 07.

English is also the translation. Slovak: „G. H. Štvrtok. Môj vlastný milujúci chlapec. Veľmi veľa šťastia k dnešnému dňu. Tvoje vlastné M-h dievča. 25. júla 1907."

## Command (from the repo root)

```sh
python3 -I ciphers/hcp-1367/work/decode.py
```

It checks the SHA-256 of both scans and both originals, decodes every token of `work/transcription.json`, checks the round trip, and prints the literal text and the normalised text.

## Uncertainties

1. **`Ibooz` = HANNY.** Both middle signs are closed loops without descenders, identical to the `o` of `Pxo` (`work/crops/l3a.png`). `q` would have a tail. The literal decode is therefore HANNY, and HAPPY (`Ibqqz`) is the intended word by the set phrase. Nothing on the pixels supports q; this is a writer's slip as I read it. Writing `o` for `p` would be a one-step shift the wrong way, but that explanation is a guess.
2. **`Sfufsot`, middle of RETURNS** (`work/crops/z6.png`, `review/work/z_retu.png`). S, f and the final s, o, t (crossed) are clear. Between the crossed f and the pale f stand only two minims, which on this card is one `u` (compare `uif`); `v` in `Zpvs` is a wide zigzag with a rising exit, so u + v would need about four strokes. The pale looped sign, with a dark re-inking blot on its descender, is read as f. Literal RETERNS, a slip for RETURNS. An eight-sign reading `Sfuvfsot` (RETUERNS) is the weaker alternative. The word is not in doubt, but these signs are the weakest of the card.
3. **`Mpwjoh`, first sign.** Capital M: long stem, second leg and a third leg merged into the stem of `p`, shown by the thick double ridge at the second leg (`review/work/z_mp.png`). It has the same form as the three-downstroke capital of `M-h` (`review/work/compare_signs.png`), while `Nz` on this card has two downstrokes. The exact form of the third leg cannot be seen where it merges. Read as N the word would be MOVING, which sense excludes (not the pixels alone); sister cards have LOVING in this formula. The j's long stroke runs into the top of the `C` below it, which makes `Cpz` look like `Epz` at first sight; the loop belongs to the j's hooked foot.
4. **`M-h`.** The capital has three downstrokes and matches the M of `Mpwjoh`, not the N of `Nz` (`review/work/compare_signs.png`). The second sign, after a dash, is a tall slanted stem with a low blobbed foot to the right. I read it h, comparing the final `h` of `Mpwjoh`, but its stem is taller and its foot smaller than there, and the form also resembles the sign read L in the same slot on hcp-1402 and hcp-1371. So h is preferred, L stays open. Parallels in this slot, none of them authority: `M-h` on hcp-1361 and 1369, `N. h.` on hcp-1363 and 1366 (these four are not closed), `N. L.` on FINAL hcp-1371. Sisters also close with `E. L.`. Kept literal and not expanded. Its meaning is unknown, and it is undecided whether it is enciphered (shifted by one it would give L-G, which is noted, not asserted).
5. **Word order at the end.** The plain date sits between `M-h` and `Hjsm`; the reading joins "M-h girl" by the sister formula. Heading initials G. H. as on sister cards (sender's place or initials, not established). The first capital has a large loop and a foot, so G is the better reading, but sister solutions (hcp-1355, 1386, 1397) record that it may be C.
6. **Birthday.** "Many happy returns of the day" implies a birthday or similar occasion around 25 July; no other evidence for this was checked.
7. Parts of row 2 lie under the portal's wheel watermark; it is grey and separates cleanly from the blue ink. Pale ink at `g` of `Pg` and row 3 end is readable at 5–6×.

## Why it is correct

One fixed shift, the established key of this correspondence, gives English for all 53 letters, apart from the two disclosed slips in one phrase. "My own … boy", "your own … girl" are the couple's recurring formulae; "very many happy returns of the day" is a fixed period phrase and was not assumed in advance of the shift. Heading "Thursday" agrees with the date on the card and postmark: 25 July 1907 was a Thursday.

## Credits

All work on this number by Claude Opus 5.5 as solver, 2026-10-30. Key and formulae were taken as hypotheses from the accepted sister cards (hcp-1386 and others), and then tested on this card's pixels.

## Response to review 1

Verdict REVISE, five findings. All are addressed; the sense of the message is unchanged. After the edits `python3 -I ciphers/hcp-1367/work/decode.py` reports 4 hashes OK and 53 enciphered letters, and its output matches the table above.

1. **Closing group (major): agreed, fixed, with one reservation.** I checked `review/work/compare_signs.png` and `z_nl.png`. The capital has three downstrokes, so it is M, not N; my claim "same form as `Nz`" was wrong. The table, `work/transcription.json` and the plaintext now read `M-h`. For the second sign I keep L open: the stem is taller and the foot smaller than the h of `Mpwjoh`, and the sign resembles hcp-1402's `L` (`hcp-1402/work/v2/crops/nl_salutation.png`), which FINAL hcp-1371 adopted. Uncertainty 4 gives the comparison signs and the whole parallel family, as parallels only.
2. **`Sfuvfsot` (minor): agreed, fixed.** Two minims stand there (`review/work/z_retu.png`). `Sfufsot` = RETERNS is now primary, RETUERNS the alternative, the count is 53, and `intended` in `work/transcription.json` is updated.
3. **Third leg of `Mpwjoh` (minor): agreed, fixed.** Uncertainty 3 now cites the double ridge and the comparison with the capital of `M-h`, says that sense rather than pixels excludes MOVING, and states what cannot be seen.
4. **G/C (minor): agreed, fixed.** Disclosed in uncertainty 5.
5. **Follow-on text (minor): done.** Status line, count, normalised English and Slovak are updated; the Slovak also now renders "very". The register entry and report carry `M-h`.

The items the reviewer could not verify stay open: the meaning of the group and of G. H., the birthday occasion, the cause of the two slips, and whether a published solution exists (no web search was run).
