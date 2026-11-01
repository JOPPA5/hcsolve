# HCP1280 — to Jolánka Tóth: "Your long-awaited lines have relieved me"

**Status: the enciphered message is read completely (15 rows). The card as a whole is partial, because a clause of the unenciphered note in the stamp box stays unread: its rows 2–3 are under stamp print and a wet ink blot (see Uncertainties 1). No register entry is written (see Response to review 1, finding 1).** Claude Opus 5.5, 2026-11-01. No earlier work exists on this number. The portal shows status *Not solved* with no transcription or solution; no published solution of this card was found. The key comes from the finished cards of the family (credited below).

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented graphic signs: the "Jolánka" family key of finished cards HCP1216 (sign table in its SOLUTION.md), 1212, 1213, 1217, 1218, 1243, 1301, established there by the OpenAI GPT solver (GPT-6 Astra / GPT-6.1 Sol) and completed by Claude Opus 5.5. It was taken over unchanged; no new letter value was needed.

Signs used here: two bars a; six b; left + right bowl cs; short stroke left + long stroke d; three bars e; upright cross f; open loop with descender g; loop + descender joined gy; dotted crossed curve i; inverted T j; section mark with a dot or tail below k; wave l; wave + descender joined ly; three short strokes m; two equal strokes n; cursive loop o; tall stroke + short tick p; F-like r; right bowl s; gamma t; chevron v; flagged cross z. Dots over o give ö, two ticks ő, a tick over a vowel an accent. The section mark's dot below is part of the sign, not an accent of the row beneath. 
Layout: 15 rows left of the divider in the upright position of the card; row 10 runs past the divider. Picture side: only a printed verse (no cipher; not transcribed).

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1280/work/decode.py
```

It checks the SHA-256 of all four scans, decodes the manual sign ledger `work/ledger.txt` and prints the literal rows and the normalized text `work/normalized.txt`.

## Literal decipherment

```
01 édesjolankamvar
02 va{r}tsoraimegkap
03 tamme{ly}igazan
04 sokgyötrelemtől
05 mentetfelfogad
06 jaérteko{s}zőnete
07 metmelyrelevél
08 benvá{l}aszolokde
09 mostnincsidőm
10 istenveleaviszont
11 látasraakitisz-
12 taszivébolésoly
13 foron{s}zereti.
14 akaralvaakarébren
15 tevagyazeszembe
```

{x} marks an overwritten or irregular sign whose value rests on the word. The dash in row 11 and the point in row 13 are marks, not letters.

## Hungarian (normalized)

Édes Jolánkám! Vár[va] várt sorai[t] megkaptam, mely igazán sok gyötrelemtől mentett fel. Fogadja érte köszönetemet, melyre levélben válaszolok, de most nincs időm. Isten vele, a viszontlátásra, aki tiszta szívéből és oly forrón szereti. Akár alva, akár ébren, te vagy az eszembe[n].

## English

My sweet Jolánka! I have received your long-awaited lines, which have truly relieved me of much torment. Please accept my thanks for them; I shall answer them by letter, but now I have no time. God be with you, until we meet again, [from the one] who loves you from a pure heart and so ardently. Whether sleeping or waking, you are on my mind.

## Slovak

Moja sladká Jolánka! Dostal som Vaše dlho očakávané riadky, ktoré ma naozaj zbavili veľkého trápenia. Prijmite za ne moju vďaku; odpoviem na ne listom, ale teraz nemám čas. S Bohom, dovidenia, [od toho,] kto Vás z čistého srdca a tak vrúcne miluje. Či v spánku, či bdejúc, si v mojej mysli.

## Unenciphered text on the address side

- **Stamp box (plain hand, six rows):** `nem is(?)` / `v a k/h e … t o(?)` / `l e t é … k(?)` / `hogy` / `szeretlek` / `csokolom`. Rows 1, 4, 5, 6 are read; the last word of row 1 runs into a blot; rows 2–3 are not read. Only *hogy szeretlek, csókolom* ("that I love you, I kiss you") is firm.
- **Address:** *Szépreményű(?) Tóth Jolánka úrleánynak, Jász Árokszállás*. The first word is under a postmark and a blot; only `Szépren` or `Széprem` shows before the blot and `yű` after it, so *Szépreményű* is supported by the card, with the middle lost; the family's address form agrees.
- **Postmark:** Jászárokszállás, 91[2] MÁR 13, agreeing with the portal file name 1912-03-13; a second postmark below the stamp box shows `912-`, confirming the year, and a place name beginning with G that is not otherwise legible. As the first postmark is the addressee's own town, the second may be another office on the route or the sending office; I do not guess the town. Top right, a pink smear looking like "24" is not relied on.

## Uncertainties

1. **Stamp box rows 2–3 (largest open point).** A whole run of plain handwriting is unread: wreath print covers the middle and a wet pink blot the right end, and green-channel and high-pass enhancement (`work/crop3.py`, `crop4.py`) did not recover it. I offer no reconstruction. This is not ciphertext, and it does not touch the cipher reading, but it is an unread part of the card.
2. **Row 2 `{r}` (word sense).** The sign is overwritten: F strokes (r) and a chevron (v) are superimposed; the order of the strokes cannot be proved from the scan. Read as r, probably a v corrected to r, giving `var|vart` = *vár[va] várt*, with the middle *va* lost by the writer. The normalization supplies it.
3. **Row 3 `{ly}` (word sense).** The sign is a thick left bow, then a wave and y. Wave + y alone is ly (row 7, row 12); bow + y alone is gy (row 15). Read *mely*, with the bow as an unexplained extra, perhaps a false start of gy. *Megy* gives no sense.
4. **Row 6 `{s}` and row 13 `{s}` (word sense).** Both signs are overwritten and neither form is a clean right bowl: row 6 is a wide top hook over a closed loop, with a side tick and a foot; row 13 is a thick stem with a foot bar. They stand in *ko{s}zőnete|met* and *foron {s}zereti*, and no other letter makes a word in either place. The first o of *köszönetemet* shows no dots, and the o of *szívéből* (row 12) shows no ticks at 6x; both are supplied in normalization.
5. **Row 8 `{l}` (word sense).** The sign has a loop with descender running into a wave, not the plain wave; it is read l in *válaszolok*. The loop's purpose is unexplained. In the same word the o before l has a straight tail ending in a dot; read o.
6. **Row 8 first sign:** the 6 (b) of *levélben* lies under the printed imprint "Bromüra" but its strokes are visible.
7. **Row 8, final `de` (d/n call).** The two strokes are clearly unequal (short then long), matching d in *fogad-* (row 5); equal strokes would give *ne*. *De most nincs időm* also gives the sense. The first sign of *időm* (row 9) shows no dot, and its loop is angular; read i by the word.
8. **Row 11 final dash.** A short low dash beside the z of *tisz-* is treated as a line-break hyphen; other row breaks have none. It may be a stray stroke. Row 13 also ends with a short low mark after the final i of *szereti*; it is not a sign of the cipher and is taken as punctuation, which supports the sentence break.
9. **Writer's spelling, normalized:** *sorai* → sorai[t]; *mentet* → mentett; *foron* → forrón; *akar* → akár (both); *eszembe* → eszembe[n] (colloquial form, kept in sense); accents are mostly unwritten and supplied. There is no p/h conflict: the only p is in *megkap|tam* (tall stroke plus separate tick at the divider, partly crossing it).
10. **Address form.** The cipher text uses polite third person (*fogadja, szereti*), and the last sentence switches to *te vagy*. This looks like a quoted lovers' tag and is kept as written.
11. **Sender:** the card is unsigned. No identification with Feri of other family cards is claimed.

## Why it is correct

- The unchanged family key turns all 15 rows into continuous Hungarian with no leftover cipher sign (the only other marks are the possible hyphen in row 11 and the point after row 13); no value was invented for this card.
- Repeats decode consistently (*akar… akar*, *viszont-*, the z-sign in *igazán, köszönet, szereti*), and the formulas *Isten vele, a viszontlátásra*, *édes Jolánkám* and *tiszta szívéből* match the family.
- The plain stamp-box words *szeretlek, csókolom* agree in tone with the deciphered love letter.
- Five signs rest on word sense (items 2–5); each is disclosed, and each sits inside a word otherwise fully read.

## Response to review 1

Verdict REVISE. No letter value changed; the English and Slovak translations stay as they were. I rechecked each point on the reviewer's crops in `review/work/crops/` and agree with findings 2 to 7. `python3 -I ciphers/hcp-1280/work/decode.py` was rerun after the fixes: all four hashes pass and the output matches the literal block and normalized text above.

1. **Unread stamp-box clause: accepted, card treated as partial.** One further attempt (`work/crop5.py`, 5x crop and green channel) also left rows 2–3 unread, so I offer no reconstruction. The run's rule says "a card" with a whole unread clause is partial and does not limit this to enciphered text, and *hogy szeretlek* depends on the lost words. I therefore read it as covering this card. The cipher is solved in full and the 15 rows are unaffected, but I write **no register entry**. A human may decide otherwise, since the unread part is not ciphertext.
2. **Fixed.** *Álva* was my error: `normalized.txt` and the text above now have *Akár alva, akár ébren*, and the sentence claiming otherwise in item 9 is removed.
3. **Fixed.** At 6x the o of row 12 (`r12o2.png`) shows no ticks. The ledger token is now `O`, the literal is `-bo-`, and the ő is disclosed as supplied in item 4.
4. **Fixed.** The mark after the final i of row 13 (`r13s2.png`, `r13end.png`) is real. It is a new ledger token `.` (`decode.py` updated to pass it through), disclosed in item 8 and in "Why it is correct".
5. **Fixed.** Items 2 and 4 now describe the forms as seen and say that the stroke order in row 2 cannot be proved. The values are unchanged.
6. **Fixed.** The address section now reports `912-` and the G of the second postmark, and the visible parts of the first address word.
7. **Fixed.** The imprint is given as "Bromüra" in item 6.

