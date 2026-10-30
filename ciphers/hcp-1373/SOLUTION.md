# HCP 1373 / pc_hcp_54 — Caesar (+1) love postcard, 4 Nov 1907

Status: **whole message read; review 1 verdict ACCEPT, four minor findings addressed (see the end).** Residual points are listed under Uncertainties. The main ones are a letter-order slip in one word (`odjfmz`) and the elliptical phrase "try usual for Friday".

## Origin

HC Portal cryptogram 1373 (`pc_hcp_54`), portal status *Not solved*, no attached transcription or solution (`SOURCES.md`, `source/metadata.md`). Picture side: printed "Guildford Castle", no handwriting. Address side: halfpenny Edward VII stamp, postmark WIMBORNE / 10 PM / NO 4 / 07, agreeing with the portal date 1907-11-04, which was a Monday, matching the plain heading "G. H. Monday". Addressed to Mr W. Abbott, Stokelake Farm, Chudleigh, S. Devon (the portal spells the recipient "W. Abboú"; metadata left unchanged). The message is on the address side, written sideways (`work/reading.jpg`). Same couple, hand and cipher as hcp-1386…1407 and the neighbouring Wimborne cards hcp-1374…1385. No published solution of this card was found or used.

## Cipher and key

Monoalphabetic Caesar shift: each plaintext letter is written as the **next** letter of the alphabet. Decrypt by subtracting one (A→Z).

```
Cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

Not enciphered: the heading "G. H. Monday", "No 1", the word "Friday" in the body, and the "&". `E. L.` (twice) and `N. & L.` are the couple's abbreviations, kept literal as on the sister cards (their shifted values would be D. K. and M. & K.).

## Transcription and plaintext (all ciphertext on the card)

| Row | Ciphertext | Literal plaintext |
|---|---|---|
| heading | G. H. Monday. No 1 | plain writing |
| 1 | Nz. Pxo. E. L. Cpz. | MY. OWN. [E. L.] BOY. |
| 2 | J. bn. hpjoh. po. | I. AM. GOING. ON. |
| 3 | odjfmz. & bcpvu | NCIELY [= NICELY]. & ABOUT |
| 4 | Nz. Sppn. usz. Vtvbm | MY. ROOM. TRY. USUAL |
| 5 | gps. Friday. Nz. N. & | FOR. Friday. MY. [N. & |
| 6 | L. Gspn. Zpvs. Pxo. E. L. | L.] FROM. YOUR. OWN. [E. L.] |
| 7 | Hjsm | GIRL |

63 enciphered letters, all decoded by the one key; 6 abbreviation letters kept literal.

English (the plaintext language; the portal lists Unknown; punctuation editorial):

> G. H. Monday. No. 1. My own E. L. boy. I am going on nicely & about my room. Try usual for Friday. My N. & L. from your own E. L. girl.

Slovak:

> G. H. pondelok. Č. 1. Môj vlastný E. L. chlapec. Darí sa mi pekne a chodím po svojej izbe. Skús to obvyklé na piatok. Moje N. & L. od tvojho vlastného E. L. dievčaťa.

## Command (from the repo root)

```sh
python3 -I ciphers/hcp-1373/work/decode.py
```

It checks the SHA-256 of the files in `source/`, decodes every token of `work/transcription.json`, checks the inverse round trip and prints the literal plaintext with letter counts.

## Uncertainties

1. **`odjfmz` (row 3) = NCIELY, read as NICELY.** The signs in `work/crops/w_nicely.png` are: o; a bowl with a slanted stem (d, as in `Nvdi` on hcp-1387); a slash with hooked foot (j, with a dot above it); a looped long f; m; z. Literally the d stands before the j: the top of the j lies to the right of the top of the d stem, and at the baseline the j crosses just right of the bowl. The hooked foot does run back under the d, as j feet in this hand run under the preceding letter (`sjoh` on hcp-1376). I transcribe the order as seen and take the word as the writer's slip for `ojdfmz`. The decoder prints NCIELY unchanged. No other English word uses these letters, and the phrase "going on nicely" fits.
2. **`Vtvbm` = USUAL (row 4, last word).** This is the hardest word on the card; see `work/crops/w_end.png`. The strokes are heavy and run together, and the capital V has the writer's starting hook. The tall stroke with the flag running right is this writer's crossed t: compare `qptufe` and `Nztufsz` on hcp-1376, also written in November 1907. Then come a v (down, up), a b with a tall stem, and m ending in a tail that reaches the card edge. The first sign alone is close to a capital U; with U the word would be TSUAL, not a word, so V is preferred. Earlier candidates THANK (`Uibol`), VITAL (`Wjubm`) and TRIAL (`Usjbm`) do not match the signs: none has a crossed t in second place. The m has no visible cut-off letter after it, but the card edge is close, so a lost terminal mark cannot be excluded.
3. **Meaning of "try usual for Friday".** The words are read, but the phrase is elliptical. Presumably it refers to some regular arrangement known to the couple, perhaps a post or meeting time; the card does not say. `usz` is clearly u, s, z (u is tall stroke with a rising second stroke, not this writer's looped w).
4. **Meaning of "about my room".** Read as literal; I take it as "up and about in my room", i.e. recovering, but the card does not name an illness.
5. **`Nz` in row 1.** The z is a compressed short third stroke set close after the N, so the group could be taken for a capital M with a third stem. It is weaker than on hcp-1376, where the z is a clearly detached 7-shaped sign. MY here rests partly on the formula and on the fuller 2-shaped z of `Nz` in rows 4 and 5.
6. **Abbreviations.** `E. L.` and `N. & L.` are not expanded. Sister cards leave them literal too, and nothing on this card proves an expansion.
7. **Heading.** The first initial is printed G: the capital has a small rising foot stroke at its lower right, a G tail (`review/work/h.png`), and hcp-1374, 1375 and 1376 have G. H. C is not excluded, because the sign has a C body and sister solutions divide (hcp-1379 and 1386 keep C; hcp-1377 prints "G. (or C.)"). The sign after "No" is an upright stroke over an underline: read as 1, an exclamation mark is possible. Sister hcp-1376 (9 Nov) has a similar numbered heading, supporting the numeral.
8. **Dots.** A dot in row 5 between `Sppn` and "Friday" is the i-dot of Friday, not a separate sign. A speck left of `gps` is not read as a sign. Word-separating dots have no meaning.
9. **Two sign shapes.** The P of `Pxo` in rows 1 and 6 has a very long flat bowl and looks like a T at first sight; `Txo` is no word, and the form is the big-bowled P of hcp-1376 and 1386. The L opening row 6 has a top flag (`review/work/z_L.png`), unlike the plain L of `E. L.` in row 1; it is still read L of `N. & L.`, split across rows 5 and 6.
10. **`Hjsm`.** The last row overlaps the printed "No 15…" of the publisher's line and the H sits on it, but all four letters are readable (`work/crops/w_girl.png`).

## Why it is correct

One fixed shift turns the enciphered text into English with no per-word adjustment, including long words (GOING, ABOUT, ROOM, FROM, YOUR, GIRL, and USUAL, which is the hardest word on the card; see uncertainty 2), with one transposed pair in NCIELY. The opening and closing are the couple's formulae, seen on accepted sister cards ("My own E. L. boy … My N. & L. from your own E. L. girl"; hcp-1386, 1403). The heading weekday and the postmark agree. Leaving a word plain in the body has a precedent ("2 hrs." on hcp-1376).

## Credits

All work on this card (transcription, decipherment) by Claude Opus 5.5 as solver, 2026-10-30. Key and hand comparisons rest on the accepted sister cards listed above; no earlier work on this number exists.

## Response to review 1

Verdict ACCEPT. All findings are minor; the 63 decoded letters did not change.

1. **Heading initial: fixed.** I checked `review/work/h.png`: the capital has the small rising foot stroke the reviewer describes. The title, table, translations and `work/transcription.json` now print G. H.; the doubt stays in uncertainty 7. "Sister cards differ" is true of the sister solutions, though not of the three the reviewer read: hcp-1374, 1375 and 1376 have G, while hcp-1379 and 1386 keep C and hcp-1377 prints "G. (or C.)". Uncertainty 7 now says this exactly.
2. **`Nz` in row 1: fixed.** On `review/work/r1.png` the third stroke is short and close to the N. Uncertainty 5 now calls it a compressed form weaker than on hcp-1376, resting partly on the formula.
3. **Undescribed sign shapes: fixed.** The P of `Pxo` and the flagged L are described in the new uncertainty 9 (`review/work/z_L.png` shows the flag) and in the report.
4. **USUAL in "Why it is correct": fixed.** The sentence now marks it as the hardest word and points to uncertainty 2.

The reproduction command was re-run after these changes: hashes pass, and it reports 63 enciphered and 6 abbreviation letters with the same message. The reviewer's "could not verify" points (the sense of the elliptical phrase and of the abbreviations; a possible mark lost at the card edge) stay open and are not claimed.
