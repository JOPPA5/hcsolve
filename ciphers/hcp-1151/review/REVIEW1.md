REVISE

# Review 1 of hcp-1151 (Claude Opus 5.5, reviewer, 2026-11-02)

The reading stands: this is the Mezőkövesd digit-plus-mark key and the card is continuous Hungarian with no unread word or clause. Concrete fixes are needed: two signs are mistranscribed (they produce false misspellings in the plaintext), one by-sense sign is uncounted, one "no mark visible" claim is wrong, and the key's "new" signs conflict with filed sister tables without saying so.

## What I verified and how

- Ran `python3 -I ciphers/hcp-1151/work/decode.py`: hashes OK; 574 signs, 119 words, 5 by sense; output equals the claimed plaintext word for word (punctuation aside). The accents and the printed text come from a hard-coded list in the script, as SOLUTION.md says.
- Wrote my own decoder, `review/work/indep.py`, which takes only the signs in `work/transcription.txt` and ignores the `~` overrides and the solver's word list. 574 signs, 30 distinct signs, all in the table. The output is the same text apart from accents and the disclosed `~` letters (`hapodat`, `köke`). The other three overrides do not change the letter. Run: `python3 -I review/work/indep.py work/transcription.txt` from the cipher directory.
- Read every row, heading to signature, on the un-converted scan in `work/hires/`: green channel, contrast stretched, 2.2x (`review/work/tiles.py`, tiles `t*.png`), then 3x to 6x on every disputed sign (`review/work/zoom.py`, `z2.py`; crops `z_*.png`, `y_*.png`). Apart from the findings below the transcription agrees with the pixels. This covers all five `~` signs and rows 20 to 27 under the printed `1386` and the underlining.
- Open text checked on the scan: `Mezőkövesd, 1916. V/13`, `Őnagysága / Sziber Margitka / Kisasszonynak / Szomolya / (u. p. Bogács.) / (Borsod m.)`.
- Picture side (`review/work/crops/pic.png`): waterfall view, no writing, no hidden cipher visible at this scale.
- Language and context: real Hungarian of the period, with a coherent content (no card for a month, conscription date, photograph, fortune-telling, prisoner in Siberia, eight-syllable quatrain, the close of hcp-1174). Nothing looks forced. English and Slovak translations checked against the Hungarian: faithful, apart from finding 6.
- `soroznak`, `meghányattam a kártyát`, `kapt is`, `é igaz`, `tőlled`, `aszt`, `semi`, `let`: the signs are as transcribed. `é` is a clear `2.` with nothing after it. Disclosed.
- 1151 is in neither `skip.txt` nor `register-exclusions.json`.

## Findings

1. **major: `ellatok` is `ellátok`, the mark is the high dot.** Row 21, fourth sign group: the dot after the 1 stands in the upper part of the digit, level with the upper dot of a `1:`, not at the foot like the `1.` later in the same row (`review/work/crops/y_r21.png`). The sign is `1'`, not `1.`. The solver's note `ellatok = ellátok` lists a spelling error that the card does not have. Fix the transcription, READ, plaintext, the list of normal forms.

2. **major: `soka` is `soká`, same error.** Row 12, last sign: the dot stands at the upper third of the digit, well above the foot (`review/work/crops/y_soka.png`); true `1.` dots on the card sit at foot level (row 11 `1.` in `z_soka.png`). Read `1'`. Slightly less sharp than finding 1 but the same call. Remove `soka = soká`. Sign counts become `1.` 51, `1'` 17. While at it, re-check the height of the dot on the other `1.` signs; I found no others in the tiles.

3. **minor: `szőke` has its dot; the "no dot visible" claim is wrong.** Row 22: there is a heavy lobe at the lower right of the first 7, merged with the end of the crossbar; the next 7 of the same word has none (`review/work/crops/y_r22b.png`). It reads as `7.` with the dot run into the bar. This should go from "by sense" to "as read, dot merged", which strengthens the reading. The solver's note that the sign lies over `1386` is also imprecise: the print is below and between, not over the dot.

4. **minor: the 5-sign count is not accurate.** In `továbbá` the mark after the 3 is drawn as a short comma with a head (`z_tovabba.png`). It is `3,` in shape; the table would give r. SOLUTION.md says this is read by sense, but `work/transcription.txt` carries it as plain `3.` with no `~`, so the "569 by the table" figure counts it as table-read. Mark it `~` and restate the count (with finding 3: still 5, with different members). Also unrecorded: a small extra dot beside the comma of the `8,` opening this word. It changes nothing, but it should be noted, since this is the word called the weakest. `ott`: I see figure-8 shapes with commas under heavy ink, so `8,` is fair; the disclosure can stay. Plain `5` in `Lapodat` and the retouched sixth sign of `továbbá` are as disclosed.

5. **major: key conflicts with sister cards are not disclosed.** The table marks `5.` and `8.` as "new", but both are filed with other values: hcp-1179 has `5. / 5,` = l and `8.` = `t?`, and hcp-1178 has `5.` = l (`a legszeb(b)`, `csókollak`). So the digraph rule is not as clean as "a digraph rule, not an ad hoc choice" suggests: on those cards a dotted 5 is plain l. Here `5.` = ly is well supported by `melynek` and `fogoly`, but it rests on two occurrences on one card, against filed readings. State the conflict in the Key and Why sections and say which you take as the writer's system (the writer may be inconsistent, or the sister `5.` may be a loose comma). `8.` = ty also occurs only once here. Worth noting in the solver's text that this bears on hcp-1179's unresolved `kar[t?]im` (`kártyám`?), without changing that card. Also the closing claim that signature and heading "match the filed readings of hcp-1174 and hcp-1179" is loose: hcp-1179 is signed Sz. A. in clear and only quotes the hcp-1174 heading; cite hcp-1174 for Árpád.

6. **minor: `ezén` is better divided `ez én`.** The signs are `1: 9, 2. 6,`. `ez én lelkem üdvössége`, "this is my soul's salvation", needs no spelling correction, while `ezén = ezen` needs a wrong long vowel and leaves "ezen" (this/on this) awkward; the solver's own translation ("she is the salvation") does not fit `ezen`. The syllable count stays eight. Change the division, the normal-form note and both translations, or say why not.

7. **minor: card marks missing from the transcription.** SOLUTION.md says punctuation is the solver's, but the card has its own. (a) Row 11 ends with a writer's hyphen after `8,`, beyond the green line (`z_kapt_end.png`, `z_soka.png`), and row 11 has no `=` although `=` is defined as that hyphen. So the card has `kapt-` / `is` across the line, as `meg-ör`, `maga-mat`, `Szibériá-ba` are split. Either the word is odd or the hyphen is loose; disclose this under the `kapt is` note. (b) The two curved brackets in rows 3 and 4 around `most ... soroznak` and the `!` after the heading are the writer's. (c) A tall slash stands in row 18 between `egészséges` and `Szibériába`; it is not a digit 1 in my view (taller, no flag), but it should be stated, not left out. (d) A `)` stands before `Árpád`, compare `(szerető kedvesed) Árpád` on hcp-1174.

## What I could not verify

- The linked HistoCrypt article was not read by me either, so I cannot exclude that it discusses this card; the solver discloses the same gap. Portal status (Not solved, nothing attached) taken from `source/metadata.md`, not re-rendered.
- The postmark is unreadable on the scan, so the date rests on the written `1916. V/13`.
- `soroznak` as conscription and the fortune-telling sense: linguistically sound, no outside confirmation. Identity of the prisoner: not stated on the card.
- The pale uncrossed stroke after `Árpád`: I agree with a flourish, but cannot prove it.
- `továbbá` sixth sign: pixels alone do not choose between `1,` and `5,`; sense does.
