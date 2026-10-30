# HCP 1361 / pc_hcp_42 — Caesar (+1) love postcard to W. Abbott, 6 July 1907

Status: **whole message read; review 1 verdict ACCEPT, no decoded letter changed.** Two abbreviation groups are kept literal. One word is a proper name (GAUNT) that the card itself cannot confirm.

## Origin

HC Portal cryptogram 1361 (`pc_hcp_42`), portal status *Not solved*, no attached transcription or solution (`SOURCES.md`, `source/metadata.md`). No published solution of this card was found or used. Portal language is Unknown; the text is English.

Picture side: printed "Houses of Parliament Westminster, London", no handwriting. Address side: halfpenny Edward VII stamp, postmark WIMBORNE 10 PM, day 6, year 07 (the month is not clear under the stamp cancel); addressed in clear to Mr W. Abbott, Stokelake Farm, Chudleigh, Devon. The portal spelling "W. Abboú" comes from the writer's tt with a bar over it. The message is on the left half (rotate 90 degrees anticlockwise, `work/crops/reading.png`). The heading "G. H. Saturday" and the date "July 6th 07" are in clear; 6 July 1907 was a Saturday. The circular disc and building logo are a scanning overlay. The hand, formulae and key are those of the accepted sister cards hcp-1386…1407.

## Cipher and key

Monoalphabetic Caesar shift: each plaintext letter is written as the **next** letter of the alphabet; decrypt by subtracting one (A→Z).

```
Cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

The key was taken from the sister cards as a hypothesis and holds for every word classed as enciphered here. `M & L. t..` and `M-h.` are abbreviation groups kept literal. That they lie outside the cipher is an assumption, not a finding: the 50 letters exclude them, and their shifted values are given under Uncertainties.

## Transcription and plaintext (all ciphertext on the card)

| Ciphertext | Plaintext |
|---|---|
| Nz. Pxo. Mpwjoh Cpz | MY. OWN. LOVING BOY |
| Dsjdlfu . Nbudi | CRICKET . MATCH |
| up. Ebz. Hbvou | TO. DAY. GAUNT |
| xpo. M & L. [t?].. | WON. [M & L. [t?]..] |
| Zpvs Pxo. M-h. | YOUR OWN. [M-h.] |
| Hjsm. | GIRL. |

50 enciphered letters, all decoded by the one key. The `[t?]` is a doubtful identification (uncertainty 2).

English: *"G. H. Saturday. My own loving boy. Cricket match to-day. Gaunt won. M & L. [t?].. Your own M-h. girl. July 6th 07."*

Slovak: *„G. H., sobota. Môj vlastný milujúci chlapec. Dnes kriketový zápas. Gaunt vyhral. M & L. [t?].. Tvoje vlastné M-h. dievča. 6. júla 1907."*

(The groups `M & L. [t?]..` and `M-h.` are left unexpanded in both versions. A possible sense of the first is "L. & K." = love & kisses, see uncertainty 2.)

## Command (from the repo root)

```sh
python3 -I ciphers/hcp-1361/work/decode.py
```

It checks the SHA-256 of the two scans in `source/` and the two originals in `work/hires/`, decodes every enciphered token of `work/transcription.json`, checks the inverse round trip and prints the plaintext with the letter count. It decodes a manual transcription made from the pixels, not the image itself. The crops named below are in `work/crops/`.

## Uncertainties

1. **`Hbvou` = GAUNT (`l4b.png`, `compare.png`).** The H is the same crossed form as in `Hjsm`, though pale. b is a bowl with an ascender. The third sign has the tall final stroke of the v in `Zpvs` on this card (`v_word` and `v_Zpvs` in `compare.png`). o has no descender, so it is not this writer's p. The last sign is a two-stroke u whose exit stroke rises into a long flourish. Word list test (`work/gaunt_wordlist.py`): GA?N? gives only gaine, gains, gaunt, and GAINS would need j and t, which do not fit the signs. That pattern fixes the fourth letter as N before testing it, so wider patterns were run too: GA??T adds galet, gamut and gault, G?UNT adds grunt, and ??UNT adds words such as count, daunt, haunt, jaunt, mount. These fall on form. The fourth sign is a closed oval, not the tall l of GAULT (`Hbvmu`) or the u of GAMUT (`Hbnvu`), and GALET would need the sequence `mf`. The second sign is a clear b, not the s of GRUNT. The first sign is the crossed H of `Hjsm`, which rules out the other ??UNT words. GAUNT is read as a surname or a side (a person or team who won). It is not proved by anything else on the card, and no person of this name was identified. I considered that the word might be "Abbott" in clear, because the addressee's name ends in a similar flourish; it is not, since the capital here is H and not the looped A of the address, the address tt is built differently, and there are too few letters (`cmp_abbott.png`).
2. **`M & L. t..` (`ml_groups.png`).** Kept literal; the meaning is not established. The capital has a long stem and two legs, so three downstrokes: M, as on hcp-1369, not the one-legged N of `Nz` on this card. Sisters often show `N. & L.` in this slot. The signs after the L are a dot, a slanted stroke with a detached bar to its right, and two dots under the bar (`after_L.png`). Read as t by analogy with `Lt..` on hcp-1371, and marked `[t?]` because that identification is weak; it could be an exclamation mark or a flourish. Hypothesis: if the group is enciphered like the rest, `M & L` shifts to **L. & K.**, the reading accepted on hcp-1395 for ciphertext `M. & L.` in the same slot, there interpreted as "love & kisses". hcp-1368 has a clear t after `N. & L.`, shifted S and taken as a plural, so `M & L. t..` could be "L. & K.s" here. This is an interpretation by analogy; nothing on this card proves it, so the literal text stays in the table.
3. **`M-h.` (`ml_groups.png`).** Kept literal, meaning unknown. The first sign has three downstrokes, so M here, though sisters show `N-L`, `E-L`, `E. L.` and `M-h` in this slot. The second is a tall stroke with a short foot or hump: h or L; hcp-1369 has the same form. Shifted values would be L-g.
4. **`up`.** The first sign has a tall first stroke and a second stroke, the form of the capital-sized u in sister `Up`; compared with the w of `Mpwjoh` it could be mistaken for w, which would give VO. `up Ebz` is the fixed sister phrase (hcp-1364, 1368, 1374). Pale ink here.
5. **`Ebz`.** The first sign has a long entry stroke, a curve and a tall stem, and is pale. C would give BAY; E gives the sister phrase. The word shape decides it, as well as the strokes.
6. **`Dsjdlfu`.** The fourth sign (d, plain C) has a shorter ascender than the first d, and the sixth (f, plain E) is a looped f with a descender; a first look at the row suggests "a" and "g". Only d and f give a word, CRICKET, and it is confirmed by MATCH beside it.
7. **Punctuation.** The dots follow the manuscript and are not significant. A dot stands before `Nbudi` and does not divide a word. The heading initials read G. H. (the first has a large loop; sister cards vary between C. H. and G. H.). They are not part of the cipher.

## Why it is correct

One fixed shift, unadjusted, turns all 50 enciphered letters into English, including LOVING, CRICKET and MATCH, which appear on no other card checked (a repo search of the sister solutions found no CRICKET), so they are not sister formulae carried over. The closing is the couple's formula, "your own … girl". A cricket match on a Saturday in July fits the plain heading and date. Only the name is unverifiable.

## Credits

All work on this number by Claude Opus 5.5 acting as solver, 2026-10-30; the key family comes from the sister cards hcp-1386…1407, whose earlier work is credited on those cards.

## Response to review 1

Verdict ACCEPT; three minor findings, all addressed. No decoded letter changed. The reproduction command was re-run after the edits: hashes OK for 4 files, 50 enciphered letters, same plaintext words. The output line for row 4 now shows the `[t?]` mark.

1. **Shifted value of `M & L` and accepted sister work: fixed.** Uncertainty 2 now gives L. & K., cites hcp-1395 and hcp-1368 (both checked in their SOLUTION.md) and states "L. & K.s" as a hypothesis. "Meaning unknown" is gone as the whole account. The Cipher and key section now calls the classification of these groups as not enciphered an assumption.
2. **`t..` without a mark of doubt: fixed.** `work/transcription.json`, the table and both translations now show `[t?]`.
3. **Narrow word test for GAUNT: fixed.** Added `work/gaunt_wordlist.py` with the wider patterns; uncertainty 1 records its output and the exclusion of each alternative on form, which agrees with the reviewer's reading of the crops. I also re-examined the word at 3x from `work/crops/reading.png` and read the same five signs: H, b, v, o, u.

The reviewer's note that solver and reviewer are the same model and vendor is correct. The README expects a different provider, so the report states this.
