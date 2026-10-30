# HCP 1374 / pc_hcp_55 — Caesar (+1) love postcard, 18 Oct 1907

Status: **whole message read; review 1 addressed.** One key covers all 39 enciphered letters: 38 read, 1 emended by the word (the literal s-shaped sign in `Wfs[z]`). 6 abbreviation letters are kept literal. The residual points are disclosed under Uncertainties.

Solver: Claude Opus 5.5, 2026-10-30. There is no earlier work on this number. No published solution of this card was found or used; the portal attaches none and shows status Not solved.

## Origin

Picture side: printed view "Royal Pump Room and Baths. Leamington", no cipher. Address side: halfpenny Edward VII stamp, postmark WIMBORNE / OC 18 / 07, addressed to Mr W. Abbott, Stokelake Farm, Chudleigh, S. Devon (the portal spells the recipient "W. Abboú"). The plain heading "Friday" and the plain date "Oct. 18th 1907" agree with the postmark and the portal date; 18 Oct 1907 was a Friday. The message runs along the left of the address side (rotate 90° counter-clockwise, `work/reading.png`).

The card comes from the same correspondence as hcp-1386…1407: same recipient, same Wimborne postmark, same hand and the same formulas (compare hcp-1386). Those cards were used as a hypothesis for key and letter forms. The reading below was made from this card's pixels.

## Cipher and key

Monoalphabetic Caesar shift: each plaintext letter is written as the **next** letter of the alphabet. Decrypt by subtracting one (A→Z).

```
Cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

The heading "Friday. G. H." and the date are ordinary writing, not shifted. `E. L.` (twice) and `N & L.` are abbreviations kept literal, as on hcp-1386 (their shifted values D. K. and M & K. are printed by the script). They are not expanded.

## Transcription and plaintext

| Ciphertext | Literal plaintext |
|---|---|
| Nz. Pxo E. L. Cpz. | MY. OWN [E. L.] BOY. |
| Wfs[z] jemf. tupsn | VER[Y] IDLE. STORM |
| up. Ebz. | TO. DAY. |
| Nz. N & L. zpvs Pxo | MY. [N & L.] YOUR OWN |
| E. L. Hjsm (a single long stroke is drawn under `L. Hjsm`) | [E. L.] GIRL |

`[z]`: the sign on the card is s-shaped; z is an emendation (Uncertainty 2).

English: *"My own E. L. boy. Very idle. Storm to-day. My N. & L., your own E. L. girl."*

Slovak: *„Môj vlastný E. L. chlapec. Veľmi nečinne. Dnes búrka. Moje N. & L., tvoje vlastné E. L. dievča."*

The stop after IDLE is the preferred punctuation, not a proved one. This writer's dots are not firm word-boundary marks (`up. Ebz.`), so "Very idle storm to-day" (*Veľmi nečinná búrka dnes*) remains a possible but less natural alternative. The letters are the same in both.

(English is the plaintext language; the portal lists the language as Unknown. "FROM", present in the same slot on hcp-1386, is not written here and is not supplied.)

## Command (from the repo root)

```sh
python3 -I ciphers/hcp-1374/work/decode.py
```

It checks the SHA-256 of the source scans and of the originals in `work/hires/`, decodes `work/transcription.json`, checks the round trip and prints the plaintext.

## Uncertainties

1. **Punctuation of `jemf. tupsn`.** The letters j, e, m, f read cleanly as IDLE, and the j matches `Hjsm` here and `wjsfe` on hcp-1386. A separate dot stands after `jemf`, so the preferred reading is "Very idle. Storm to-day.", which parallels "I have been very busy to-day" on hcp-1405 with its opposite. The card does not say who or what was idle. The dot does not prove the division, because this writer also puts dots inside `up. Ebz.`.
2. **Fourth sign of `Wfs[z]` (Y): an emendation, not a reading of the pixels.** The ink is faded at the top of this sign and the one before it. Literally the sign is s-shaped: the stroke descends to the right into a dark foot with a beak pointing left, the same construction as the preceding s, whereas this writer's z descends to the left and its foot runs right (`Cpz`, `Ebz`). Literal `Wfss` gives VERR, which is no word. VERY is taken from the word, which recurs across this correspondence. The dark beak is part of the sign, and no dot stands after it.
3. **Last sign of `tupsn` (M).** It has two strokes, and n and u are not separable in this hand. `tupsu` gives STORT, so n is chosen by the word. `z` (STORY) is excluded: this writer's z is 2-shaped, as in `Cpz` and `Ebz`.
4. **Initials.** The heading initial may be G or C (the same shape is read C on hcp-1386). `E. L.` and `N & L.` are not expanded, and the N could be another capital with similar legs. None of these affects the enciphered text.

## Why this is believed correct

- One key decodes every enciphered word on the card into English once the single sign in `Wfs[z]` is emended, with the points above disclosed.
- The key and formulas match the finished cards of the same correspondence: "My own … boy", "your own … girl", E. L., N & L.
- Heading, date, postmark and weekday agree.
- "Very idle. Storm to-day." is natural English and the opposite of the "very busy to-day" of hcp-1405. The weakest points are the emended sign and the n of `tupsn`, and neither has a competing word.

## Response to review 1

Verdict REVISE, with no re-review needed if only these points change. I rechecked `review/work/jemf.png`, `s4.png` and `l5.png` and agree with all four findings. The decoded letters are unchanged.

1. **Finding 1 (major), sentence misparsed: fixed.** The dot after `jemf` is real and separate. English and Slovak now read "Very idle. Storm to-day." with the unpunctuated form given as an alternative. Uncertainty 1 and the last line of "Why this is believed correct" are rewritten, and the slip suggestion and VILE/WILD are dropped from them. (Those two were dead ends and stay in NOTES.md.)
2. **Finding 2 (minor), emended z: fixed.** The sign is `Wfs[z]` in the table and in `work/transcription.json`, and the status line says 38 read, 1 emended. `work/decode.py` now counts and reports the emendation, and "Why this is believed correct" states the condition.
3. **Finding 3 (minor), dot after `Wfsz`: fixed.** `s4.png` shows no separate dot, only the foot's beak. It is removed from the table and from `work/transcription.json`.
4. **Finding 4 (minor), underline: fixed.** The stroke under `L. Hjsm` is recorded in the table. The sense is unaffected.

The command was re-run after these changes. It passes the hash checks and prints `39 enciphered letters decoded (38 read, 1 emended, in square brackets) + 6 abbreviation letters kept literal`.
