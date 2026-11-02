REVISE

# Review 1 of hcp-1137

Reviewer: Claude Opus 5.5, 2026-11-02. The reading stands. The cipher text, key and plaintext survived every test. One open-text word is misquoted and must be corrected. The other findings are small. After these fixes the solver can go to FINAL; no second review round is needed.

## What I verified and how

1. Solver's command, `python3 -I ciphers/hcp-1137/work/decode.py`: runs, all 4 scan hashes pass, 373 signs, 4 read by sense. The printed text matches the plaintext in SOLUTION.md.
2. Own transcription: `review/work/decode_review.py` holds 21 rows I typed from my own crops of the un-converted scan (`review/work/crop.py`, `review/work/crops/`), with my own key table. It decodes the rows and compares them token by token with the solver's ROWS. Result: 373 signs, and all 373 agree. The only 4 differences are the solver's 4 ODD pseudo-tokens, where I give what is on the card (plain `1`, `5`, `5`, `8,`). Raw output: `rozsiszális`, `csokohom`, `hányka`, `szátalanszor`, everything else exactly the claimed text.
3. Pixels: all 21 rows checked at about 2x, and the following at 3x to 6x.
   - `rózsaszál` row 7 (`rose7b.png`): a plain 1 with no dot, between `9.` and `7.`. Confirmed. The same word has `1.` on row 11.
   - `csókolom` row 14 (`csok.png`): the 5 has no comma, and the printed rule does not hide one. Confirmed.
   - `lányka` row 18 (`lany.png`): 5 with no comma. Confirmed.
   - `számtalanszor` row 19 (`szam.png`, `szam2.png`): see finding 2.
   - `Azért` row 15 (`azert.png`): the long stroke left of the 8 is the comma of the 3. So `3,`, with a separate comma on the 8, as transcribed.
   - `tam` start of row 4 (`r4l.png`): the 8 has its comma, which curves into the 7 of row 5. Confirmed.
   - `távolból` (`tav.png`) and the closing row (`hu.png`, `end2.png`, and `ink.png`, which removes the brown stamp by colour): `1. 8, 1' 3. 0 5, 1, 0 5,` and `5 :1 1 8 1' 3 0 3` then a hook, then `1' 3, 9 1' 3` then a hook. All signs are present. The comma of the last `5,` runs down into the 3 of `imádód`. `hű` has two dots left of the stem.
4. Key: consistent. All 30 signs are single-valued over the card; `.1`/`:1`/`1.`/`1:`/`1'` are distinct positions of the dots and each holds across its words (`.1` in kúthoz, újságot, tudok, szervusz; the dot is clearly left of the stem, not under the preceding sign, at the start of `újságot`). The FINAL tables hcp-1174, 1178 and 1179 agree with every sign they share. `4.`, `6`, `6.`, `.1` and `9.` have the same values on sister cards of this run (hcp-1135, 1138, 1150, 1160, 1164), all from different words.
5. Language and context: natural Hungarian prose and two rhymed quatrains (dér/vér, ápolom/csókolom) plus a couplet. `Terenyén` fits the place and postmark, `Szent-kút` fits the region, `Margitkám` and `Árpád` fit the family. No sign of forced words.
6. Open address read on the scan: `Őnagysága.`, `Sziber Margitka`, `Kisasszonynak`, `Szomolya`, `(Borsod m.) u. p. Bogács`. Agrees with SOLUTION.md. I did not study the picture side.

## Findings

1. **major: the open place name is misquoted.** SOLUTION.md (sections Card and Plaintext) and decode.py print `Kisterenye, 1916 VI 10`. The card reads `Kis Terenne, 1916 VI 10` (`crops/place.png`): capital T, double n, no descender, so no y. hcp-1150 by the same writer is filed as `Kisterenne`. The modern form belongs in a note; the plaintext must give the card. It is undisclosed, and the sentence "`Terenyén` agrees with the open `Kisterenye`" rests on the wrong form. Agreement of place remains, but note that the writer spells `Terenne` in clear and `Terenyén` (with `6.`) in cipher. Fix SOLUTION.md, decode.py and the report.

2. **minor: the `számtalanszor` sign is misdescribed.** The sign is an ordinary `8,` with a long comma: 8, then the comma, then `1.` (`crops/szam2.png`). By the table that is t, so the raw text is `szátalanszor` with the m simply omitted. The pseudo-sign `8~mt` and the raw note `száta/száma-lanszor` suggest more than the card gives. The faint strokes around it do not resolve into a second 8. The word remains certain, and it is the writer's usual closing (hcp-1138, 1144). Say "m omitted, `8,` = t".

3. **minor: count.** "373 cipher signs in 33 distinct forms" counts the 3 ODD pseudo-tokens. The card has 30 distinct signs, the same 30 as in the key table.

4. **minor: "new" signs and credit.** The table marks `4.`, `6`, `6.`, `.1`, `9.` as new, and the credit line names only FINAL cards and hcp-1175. SOLUTION.md itself cites hcp-1150, whose table already has the first three with the same values, and the other cards named under "What I verified", item 4, have the rest. Say they are established on this card independently and also occur on unreviewed sister cards. This is corroboration, not a problem for the reading.

5. **minor: undisclosed small points.**
   - The final 3 of `Árpád` also carries a long hook. It is taken as a flourish or punctuation like the one after `imádód` (otherwise `3,` = r); not mentioned.
   - Row 2 ends with a hyphen inside `Tere-nyén`, not in the list of row-end hyphens; `ápolom-` ends a word and a verse line, so it is a dash, not a word-break hyphen.
   - `Értesítlek`: written without the linking vowel. As far as I know the standard form is `értesítelek`; the spelling note lists only `egyeb` and `for`. Not a misreading, the cipher is clear.

6. **minor: translations.** `Édes Margitkám` has the possessive -m: "My sweet Margitka", "Moja sladká Margitka" (as on hcp-1174). `Meleg ágyban` also suggests melegágy, a garden hotbed, which suits the rose image; a note is enough.

## What I could not verify

- The postmark date is only partly legible; I confirm the place and a compatible date, not every digit.
- Whether the verses have a printed source: not searched.
- The full text of the HistoCrypt article: not read, so I cannot exclude a published reading of this card. The solver discloses the same limit.
- The geography of Szentkút is general knowledge, not on the card.
- I relied on the sister tables as filed for sign values and did not reread those cards' pixels.
