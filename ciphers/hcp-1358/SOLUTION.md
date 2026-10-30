# HCP 1358 / pc_hcp_39 — Caesar +1 love postcard, March 1907

Status: whole message read; review 1 verdict ACCEPT, no decoded letter changed. Two signs are disclosed writer's slips. No state before this was recorded; this is new work by Claude Opus 5.5 as solver (2026-10-30), which used the sister cards in this repo for hand comparison.

## Origin

Portal 1358 (`pc_hcp_39`), status Not solved, no transcription or solution attached (`source/metadata.md`). No published solution of this card turned up; no separate web search was run beyond the portal record and the orchestrator's AI-register check. Picture side: Raphael Tuck "Illustrated Hymns" card, Series 5534, printing the hymn verse "We love the place, O God" with a church view; no handwriting. Address side: Mr W. Abbott, Stokelake Farm, Chudleigh, Devon (portal spelling "W. Abboú"), halfpenny Edward VII stamp, postmark WIMBORNE 10 PM MR 1? (second digit of the day unclear; the portal gives 1907-03-18). Same recipient and hand-style as the Caesar cards hcp-1386…1407.

## Cipher and key

Monoalphabetic Caesar: each plaintext letter is written as the next letter of the alphabet. Decrypt by −1.

```
cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

## Transcription and plaintext

The message is on the address side, turned 90° counter-clockwise (`work/crops/all_ccw.png`).

| Ciphertext | Literal decode |
|---|---|
| Nz. Pxo. Efbsftu Cpz. | MY. OWN. DEAREST BOY. |
| uijt jt Tpnfuijoh ofx. | THIS IS SOMETHING NEW. |
| boe. pof. pg. oz. | AND. ONE. OF. NY. [MY] |
| gpwpvsjuf. Iznot | FOVOURITE. [FAVOURITE] HYMNS |
| Mpwf. Gspn. Zpvst. | LOVE. FROM. YOURS. |
| Hjsm. | GIRL. |

Plain, not enciphered, at the foot beside `Hjsm`: "March 8th" (or 18th; see uncertainty 8) followed by a year that is not read.

74 enciphered letters, all decoded by the one key.

English: *"My own dearest boy, this is something new and one of my favourite hymns. Love from yours, Girl."* (March; the year 1907 comes from the portal record, not from a reading of the card)

Slovak: *„Môj vlastný najdrahší chlapec, toto je niečo nové a jedna z mojich obľúbených piesní. S láskou tvoje dievča."* (marec; rok 1907 pochádza zo záznamu portálu, nie z čítania pohľadnice)

## Command (from the repo root)

```sh
python3 -I ciphers/hcp-1358/work/decode.py
```

It checks the SHA-256 of the four image files, decodes `work/transcription.json`, checks the round trip, prints the slips and the intended text.

## Uncertainties

1. **`oz` = NY, not MY** (`work/crops/z_my.png`). The sign is a closed, hollow o, not this writer's n. `nz` is plainly intended (cf. `Nz` at the start). Literal decode kept in the table; treated as a writer's slip.
2. **`gpwpvsjuf` = FOVOURITE** (`work/crops/z_favo.png`). The second sign has a stem running below the line with a bowl: this writer's p. His b has no descender (`Efbsftu`, `boe` on row 3, and `uibolt` on hcp-1386). Intended `gbwpvsjuf`. Slip, not silently corrected.
3. **First sign of `uijt`** (`work/crops/z_first.png`) looks like h. It is this writer's word-initial u, a tall stroke with an arch, as in `uibolt` and `Up` on hcp-1386 (`ciphers/hcp-1386/work/crops/thanks.png`, `compare_u_w.png`). Because h and u are close in this hand, the final sign of `Tpnfuijoh` is taken as h on the word.
4. **`Tpnfuijoh`**: the initial looks like a T with a detached bar; the descenders of line 1 cross this word, so `f` and `j` were separated from them by stroke direction (`work/crops/z_some.png`).
5. **`Iznot`** third sign: an n whose first leg is the join from z (`work/crops/z_hymns.png`).
6. **`Zpvst`**: the final t has a detached bar and is followed by a stop, which can look like a colon. YOURS is the reading; "Yours" on sister cards is usually `Zpvs`.
7. **`Hjsm`** (`work/crops/z_date.png`, `l6b.png`): H with crossed bar, then a long j crossing the date, s, m. The long stroke is taken as j, not as part of the year.
8. **Plain date**: the hand alone reads 8th: the stroke before the 8 joins it as a lead-in and no separate 1 can be seen (`review/work/z_date2.png`). The postmark shows MR, a clear 1 and a broken second digit that merges with the stamp design (`review/work/z_pm.png`), and the portal gives the 18th, so 18th is possible but neither source confirms it. **Year not read; 1907 from portal.** The strokes after the date overlap the printing and the j of `Hjsm` (`review/work/y_year.png`), and the postmark year falls off as a bare arc.
9. The address-side stop marks follow the manuscript and are not significant.

## Why it is correct

One fixed shift gives English for all 74 letters apart from the two disclosed one-letter slips, with long words (DEAREST, SOMETHING, FAVOURITE, HYMNS). Not every sign is independent evidence: at least three signs are settled by context, because this hand does not separate them on form alone. These are the final sign of `Tpnfuijoh` and the first sign of `uijt` (h and u share a form) and the third sign of `Iznot` (fits n only on the word). The content matches the card: it is a printed hymn card from a Tuck "Illustrated Hymns" series, and the writer calls it "one of my favourite hymns". The formulae "My own", "Love from yours", "Girl" and the shift match accepted sister cards (hcp-1386, 1397, 1398). Context only, since that card has not been reviewed yet: hcp-1357, on the same Tuck series 5534 and postmarked MR 22 07, opens the same way and says "this will make the pair for album", which fits "something new" here.

## Credits

Solved by Claude Opus 5.5 as solver. Hand comparison uses the accepted sister cards in this repo, which earlier solvers worked on.

## Response to review 1

Verdict ACCEPT; no decoded letter changed. All four minor findings are addressed, and I checked the date crops myself before rewording.

1. **Independence of the letters: fixed.** "Why it is correct" now says that at least three signs (final sign of `Tpnfuijoh`, first sign of `uijt`, third sign of `Iznot`) are settled by context.
2. **Date: fixed.** I agree with the reviewer. On `review/work/z_date2.png` the stroke before the 8 runs into it as a lead-in, and on `review/work/y_year.png` the strokes after the date cannot be read as secure digits. Uncertainty 8 and the translation lines now carry "year not read; 1907 from portal", and `plain_not_enciphered` in `work/transcription.json` no longer contains "19[07]". On the postmark crop (`review/work/z_pm.png`) I also see MR, a 1 and a broken digit, so the day stays open.
3. **Citation: fixed.** Uncertainty 2 now says `boe` on row 3.
4. **Context: done.** The hcp-1357 remark is in "Why it is correct" and the report, marked as context only.

`python3 -I ciphers/hcp-1358/work/decode.py` was re-run after these changes: hashes and round trip pass, 74 letters, same plaintext.
