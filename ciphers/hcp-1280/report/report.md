# HCP 1280: an unsigned Hungarian love note to Jolánka Tóth, March 1912

Human solver: Tomáš Pavuk

**Status: the enciphered message is deciphered in full (15 rows). The card as a whole is partial, because one clause of the plain note in the stamp box stays unread. Independent review 1 verdict REVISE; all findings addressed, no letter value changed.** Report dated 2026-11-01.

## Origin and context

The cryptogram is record 1280 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1280), portal name cpc_1912-03-13_HU__HU_Jasz Arokszalas_jolanka-09, part of Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-11-01 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, category Substitution, language Unknown, location Europe, sender Unknown, recipient Tóth Jolánka, with no transcription or solution attached. No published solution of this card was found.

It is a picture postcard. The picture side carries only a printed Hungarian verse and a series number, with no handwriting or cipher. All writing is on the address side, in red ink: fifteen cipher rows left of the divider (row 10 runs past it), a plain address, and a short plain note written inside the stamp box.

The address reads *Szépreményű Tóth Jolánka úrleánynak, Jász Árokszállás* ("to the promising young lady Jolánka Tóth, Jászárokszállás"). The middle of the first word is lost in a pink blot, but `Szépre…` and `…yű` are visible. A postmark of Jászárokszállás reads 91[2] MÁR 13, which agrees with the date in the portal's file name, 1912-03-13. A second postmark below the stamp box shows `912-` and a place name beginning with G, otherwise illegible. It may be another office on the route or the sending office.

The card belongs to the family of cipher postcards to Jolánka Tóth. The sender does not sign this card, and no identification with a writer of other family cards is claimed.

![Address side with the fifteen cipher rows, the stamp-box note and the address (source/address-large.jpg)](../source/address-large.jpg)

![Picture side: printed verse only (source/picture-large.jpg)](../source/picture-large.jpg)

## Method

The key was not recovered from this card. It is the family key established on the finished cards HCP 1216, 1212, 1213, 1217, 1218, 1243 and 1301 by an OpenAI GPT solver (GPT-6 Astra / GPT-6.1 Sol), with HCP 1216 completed by Claude Opus 5.5. Claude Opus 5.5 took it over unchanged and needed no new letter value.

The transcription is manual, not OCR: each row was read sign by sign from 2x to 5x crops of the high-resolution address scan and recorded in a sign ledger, which the reproduction command decodes. Because the key was known, word sense was used while reading, and the places that depend on it are listed below. The first pass was corrected on the pixels in three places: wave + y is ly, not ny (*melyre, oly*); the last word of row 8 is *de*, not *ne*, because its strokes are unequal; and the dot below the section mark belongs to the k, so it is not an accent of the row beneath.

The stamp-box note was also tried with green-channel, high-pass and enlarged crops. The reviewer tried ink separation separately. Neither recovers its rows 2 and 3.

## Key

Monoalphabetic substitution with invented graphic signs. Labels describe the handwritten shapes.

| Sign | Plain | Sign | Plain |
|---|---|---|---|
| two bars | a | wave | l |
| six | b | wave + descender joined | ly |
| left + right bowl | cs | three short strokes | m |
| short stroke, then long stroke | d | two equal strokes | n |
| three bars | e | cursive loop | o |
| upright cross | f | tall stroke + short tick | p |
| open loop with descender | g | F-like sign | r |
| loop + descender joined | gy | right bowl | s |
| dotted crossed curve | i | gamma | t |
| inverted T | j | chevron | v |
| section mark, dot or tail below | k | flagged cross | z |

Two dots over o give ö, two ticks give ő, and a tick over a vowel marks an accent. Accents are mostly left unwritten. Word gaps are not written.

## Plaintext

Literal decipherment by row. {x} marks an overwritten or irregular sign whose value rests on the word. The dash in row 11 and the point in row 13 are marks, not letters.

```text
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

Normalized Hungarian (accents, capitals, punctuation and the bracketed letters are editorial):

**Édes Jolánkám! Vár[va] várt sorai[t] megkaptam, mely igazán sok gyötrelemtől mentett fel. Fogadja érte köszönetemet, melyre levélben válaszolok, de most nincs időm. Isten vele, a viszontlátásra, aki tiszta szívéből és oly forrón szereti. Akár alva, akár ébren, te vagy az eszembe[n].**

English translation: **My sweet Jolánka! I have received your long-awaited lines, which have truly relieved me of much torment. Please accept my thanks for them; I shall answer them by letter, but now I have no time. God be with you, until we meet again, [from the one] who loves you from a pure heart and so ardently. Whether sleeping or waking, you are on my mind.**

Slovak translation: **Moja sladká Jolánka! Dostal som Vaše dlho očakávané riadky, ktoré ma naozaj zbavili veľkého trápenia. Prijmite za ne moju vďaku; odpoviem na ne listom, ale teraz nemám čas. S Bohom, dovidenia, [od toho,] kto Vás z čistého srdca a tak vrúcne miluje. Či v spánku, či bdejúc, si v mojej mysli.**

### The plain note in the stamp box

Six rows of plain handwriting, not enciphered:

```text
nem is(?)
v a k/h e … t o(?)
l e t é … k(?)
hogy
szeretlek
csokolom
```

Only *hogy szeretlek, csókolom* ("that I love you, I kiss you") is firm. Rows 2 and 3 are not read; the letters shown are fragments, and no reconstruction is offered.

## Uncertainties

- **Stamp box, rows 2–3 (largest open point).** Wreath print covers the middle and a wet pink blot the right end. This is an unread clause, and *hogy szeretlek* depends on it. It is not ciphertext and does not touch the cipher reading. Because of it the card is treated as partial and no register entry is written; a human may decide otherwise.
- **Signs resting on word sense (five).** Row 2 `{r}`: F strokes and a chevron are superimposed, stroke order not provable, read r in *vár[va] várt*, with the writer's *va* lost. Row 3 `{ly}`: wave and y with an unexplained thick bow before them; *mely* makes sense and *megy* does not. Rows 6 and 13 `{s}`: both overwritten, neither form a clean right bowl, but no other letter gives a word in *köszönetemet* or *szereti*. Row 8 `{l}`: a loop with descender runs into the wave, read l in *válaszolok*.
- **Accents supplied.** The first o of *köszönetemet* shows no dots and the o of *szívéből* shows no ticks at 6x. Both are supplied in normalization, as are most other accents. Faded accent marks cannot be ruled out in the pale ink of row 12.
- **Row 8, final *de*.** The strokes are clearly unequal, as in *fogad-*; equal strokes would give *ne*. The sense agrees. The first sign of *időm* (row 9) shows no dot and is read i by the word.
- **Marks that are not letters.** A short dash at the end of row 11 is taken as a hyphen, though no other row break has one; it may be a stray stroke. A short low mark after *szereti* is taken as punctuation.
- **Writer's spelling.** *sorai* → sorai[t], *mentet* → mentett, *foron* → forrón, *akar* → akár, *eszembe* → eszembe[n] (colloquial).
- **Address form.** The cipher text uses the polite third person (*fogadja, szereti*), and the last sentence switches to *te vagy*. It looks like a quoted lovers' tag and is kept as written.
- **Sender and second postmark.** The card is unsigned, and the town of the second postmark is not read.

## Review and what changed

An independent Claude Opus 5.5 reviewer checked all 15 rows sign by sign on crops of the high-resolution scan, up to 7x at disputed signs, and decoded its own transcription of 213 signs with the key typed separately. It had read the solver's text first, so this was a check against the pixels, not a blind reading. Fourteen rows agreed letter for letter; row 12 differed by one mark. The reviewer found no misread word and returned REVISE. It judged the text to be natural Hungarian love-letter prose of the period.

Changes made because of the review (none changes a letter value or the translations):

- The normalized text had *álva*, the solver's own added accent; it is now *alva* (asleep).
- The ő claimed in row 12 is not on the card; the literal now has o and the ő is disclosed as supplied.
- The mark after *szereti* is now recorded and disclosed.
- The descriptions of the overwritten signs were softened to what the pixels show.
- The `912-` and initial G of the second postmark and the visible parts of the first address word are now reported.
- The imprint at the left edge is given as "Bromüra".
- The status now states that the unread clause of the stamp-box note makes the card partial.

Reproduction, from the repository root: `python3 -I ciphers/hcp-1280/work/decode.py`. It checks the hashes of the four scans, decodes the sign ledger `work/ledger.txt` and prints the literal rows and the normalized text.
