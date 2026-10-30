# HCP 1386 / pc_hcp_67 — Caesar (+1) love postcard, 26 Nov 1907

Status: **whole message read; review 1 verdict ACCEPT; closed (FINAL).** Two abbreviation groups are kept literal and one letter of the final quoted word is a disclosed residual (see Uncertainties).

## Origin

HC Portal cryptogram 1386 (`pc_hcp_67`), portal status *Not solved*, no attached transcription or solution (see `SOURCES.md`, `source/metadata.md`). Picture side: printed Frith's view "Princess Gardens, Torquay", no cipher. Address side: halfpenny Edward VII stamp, postmark WIMBORNE / NO 26 / 07 (agrees with the portal date 1907-11-26; 26 Nov 1907 was a Tuesday, matching the plain heading "C. H. Tuesday"); addressed to Mr W. Abbott, Stokelake Farm, Chudleigh, S. Devon (portal spells the recipient "W. Abboú"; metadata left unchanged). The message is on the address side (rotate 270°, `work/reading.jpg`). It belongs to the same couple as the Caesar cards hcp-1386…1407 (sister cards hcp-1390, 1397, 1398, 1403 use the same key and the same phrases "My own", "from your own … Girl"). No published solution of this card was found or used.

## Cipher and key

Monoalphabetic Caesar shift: each plaintext letter is written as the **next** letter of the alphabet. Decrypt by subtracting one (A→Z).

```
Cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

The heading "C. H. Tuesday" is ordinary writing and is not shifted. The groups `E. L.` (twice) and `N. & L.` are abbreviations; they are kept literal (their shifted values D. K. and M. & K. are printed alongside), as on sister card hcp-1403.

## Transcription and plaintext (all ciphertext on the card)

| Ciphertext | Literal plaintext |
|---|---|
| Nz. Pxo. E. L. Cpz. | MY. OWN. [E. L.] BOY. |
| uibolt-wfsz. | THANKS-VERY. |
| nvdi gps. mfuufs | MUCH FOR. LETTER |
| Up—Ebz. Nz. | TO—DAY. MY. |
| N. & L. gspn. zpvs. | [N. & L.] FROM. YOUR. |
| Pxo. E. L. Hjsm | OWN. [E. L.] GIRL |
| "wfsz. wjsfe." | "VERY. VIRED." (probably *tired*, see below) |

62 enciphered letters, all decoded by the one key; 6 abbreviation letters kept literal.

Reading: *"My own E. L. boy, thanks very much for letter to-day. My N. & L. from your own E. L. girl. 'Very tired.'"*

Slovak: *„Môj vlastný E. L. chlapec, veľmi pekne ďakujem za dnešný list. Moje N. & L. od tvojho vlastného E. L. dievčaťa. ‚Veľmi unavená.'"*

(English is the plaintext language; the portal lists the language as Unknown.)

## Command (from the repo root)

```sh
python3 -I ciphers/hcp-1386/work/v2/decode.py
```

It checks the SHA-256 of all three files in `source/`, decodes every token of `work/v2/transcription.json`, checks the inverse round trip, and prints the plaintext above with the letter counts. (The older `work/decode.py` / `work/transcription.json` are the earlier partial transcript, kept for history.)

## Uncertainties

1. **Final quoted word `wjsfe`.** The letters j, s, f, e are clear (j is the writer's dotless x-height slash with hooked foot, as in `Hjsm`; f has an ascender; e has an eye). The first sign is built like this writer's **w** (tall stroke closing in a loop, as in `wfsz` immediately before it on the same line), not like his **u** (tall stroke with an arch, as in `uibolt` and `Up`) — `work/crops/tired.png`, `very2.png`, `compare_u_w.png`. The literal decode is therefore VIRED, which is not a word; the only one-letter change giving English is `ujsfe` = TIRED, which suits the quoted phrase "very tired". I report VIRED as read and TIRED as the probable intended word (writer's slip or u/w confusion in his hand); it is not substituted in the output. The earlier reading `wjtf` = WISE does not fit the pixels (there are five letters, the third is s, the last is e).
2. **`E. L.`** (salutation and closing) and **`N. & L.`** (before "from your") are abbreviations, kept literal. Plain-text readings such as "ever loving" for E. L. are possible, but nothing on the card proves them, and their status (shifted or not) is undecided. The middle sign of `N. & L.` is an ampersand-like form, read as "&" (same shorthand on hcp-1403).
3. Heading initials C or G (sister card hcp-1397 prefers G. H.); heading not enciphered. The farm name in the address reads Stokelake Farm, as on sister cards hcp-1387, 1388, 1397, 1403. Separator dots follow the manuscript but are not significant.

## Why it is correct

One fixed shift turns every enciphered token into English (62/62 letters), including long words (THANKS, LETTER, FROM, YOUR, GIRL) and the couple's recurring formulae known from accepted sister cards (hcp-1397: "Your own girl"; hcp-1390: "many thanks … to day … from your own … girl"). The message fits a 1907 sweetheart postcard and the dated postmark. The only non-word is the single disputed first letter of the last word.

## Credits

Earlier partial work (download, 54-letter partial transcript, key identification) by the OpenAI GPT solver (GPT-6 Astra / GPT-6.1 Sol), 2026-10-26. Completion (full re-transcription from the pixels, reading of `Cpz`, `N. & L.`, the second `E. L.` and the final word, new decoder) by Claude Opus 5.5 acting as solver, 2026-10-29.

## Response to review 1

Verdict ACCEPT, four minor findings. No decoded letter changed; the reproduction command was re-run on 2026-10-29/30 and still prints the same plaintext (62 enciphered letters + 6 literal abbreviation letters, hashes OK).

1. **VIRED / TIRED (minor, disclosed).** Agreed and unchanged: VIRED is the literal decode of `wjsfe` (first sign is this writer's w, compare `wfsz` immediately before it, `work/crops/compare_u_w.png`); TIRED is stated only as the probable intended word. The report keeps this wording and does not present "very tired" as certain.
2. **E. L. / N. & L. unexpanded (minor, disclosed).** Agreed; kept literal. The report adds the reviewer's note that sister card hcp-1387 has a parallel slot ("My own D.g boy … your own D.g girl"), so the slot is a term of endearment, while E. L. stays unexpanded.
3. **Farm name (minor).** Fixed. I re-checked the rotated address (`review/work/rot.png`): the second address line reads "Stokelake Farm", as on hcp-1387, 1388, 1397, 1403 (whose SOLUTION.md files name Stokelake). Origin and Uncertainties above now say Stokelake Farm.
4. **Weekday (minor).** Fixed. `datetime.date(1907,11,26)` is a Tuesday, matching the heading "C. H. Tuesday" and the WIMBORNE NO 26 07 postmark; added to Origin.
