# HCP 1223 (jolanka-114): a Hungarian love letter to Jolánka Tóth, excusing a missed visit

Human solver: Tomáš Pavuk

**Status: deciphered in full (414 of 414 cipher signs), with one contracted phrase read by sense; independent review 1 verdict REVISE, findings addressed, normalized text unchanged.** Report dated 2026-11-02.

## Origin and context

The cryptogram is record 1223 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1223), portal name cpc_1913-01-_HU__HU_Jasz Arokszalas_jolanka-114, from Tobias Schrödel's cryptographic postcards collection (private collection). When captured on 2026-11-02 the portal listed it as **Not solved**, category Substitution, language Unknown, sender Unknown, recipient Tóth Jolánka, with no transcription or solution attached.

The picture side is a printed photograph numbered 1012 and carries no writing. The address side has a plain address, "Szépreményű Tóth Jolánka úrleánynak, Jász-Árokszállás" (to the young lady Jolánka Tóth, of fair promise, at Jászárokszállás, Hungary). The rest of that side is filled with 22 rows of invented graphic signs, and six more short rows stand in the place under the removed stamp. The postmark survives only in fragments: GY and the year 913 (1913). The portal file name suggests January 1913.

The card belongs to the family of cipher postcards to Jolánka Tóth, whose key was reconstructed on earlier cards in this repository (hcp-1216, which has the fullest table, and 1212, 1213, 1217, 1218, 1243, 1301). Several of those cards are signed Feri. The key was therefore **transferred, not recovered blind from this card**. No reading of this card was supplied or consulted.

![Picture side: printed photograph, no writing (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side with the cipher rows; the signs under the stamp are in the top right corner (source/address-large.jpg)](../source/address-large.jpg)

## Method

The solver read every sign by hand from 2x to 5x enlargements of the un-converted original scan, and wrote one token per written sign into a ledger. No OCR was used. The key from the sister cards gave Hungarian at once on row 1 (szeretet édes Jolán-), and no sign needed a new value.

The reviewer read all rows again from separate crops and decoded the ledger with an independently written mapping. That second reading found the ledger error described under "Review summary".

## Key

Simple monoalphabetic substitution with invented graphic signs. Accents are small marks over the base sign and are often invisible.

| Plain | Sign | Plain | Sign |
|---|---|---|---|
| a | two bars | l | wave |
| b | a figure 6 | ly | wave joined to a descender |
| cs | opposed bowls | m | three strokes |
| d | short stroke to the left of a long one | n | two strokes |
| e | three bars | o | cursive loop |
| f | upright cross | r | F-like sign |
| g | open loop with descender | s | right bowl |
| h, p | long stroke with a separate short tick on its right (one sign) | t | gamma |
| i | dotted loop | u, ü | plain cross |
| j | inverted T | v | chevron |
| k | section mark | y | low descender |
|  |  | z | tailed cross |

## Plaintext

Literal decipherment, row by row (S1 to S6 are the rows under the stamp):

```text
01 szeretetédesjolan
02 kamvárvavártsora
03 itmegkaptammelynek
04 nagyonmegörültem
05 kivanomhogyaleg
06 jobbkedvebentalal
07 jasoraim.nehara
08 godjonrámédesem
09 ho.gymanemmehettem
10 ledelekéstemavonat
11 rolamitigazan.
12 sajnalokszamittot
13 temkeddenreggelle
14 mennideaztgondol
15 temhétköznapnem
16 alkalmatlankodok
17 szerelmemésminde
18 nemazértnemmehet
19 temmalemertatüz
20 oltottestületne
21 vanaközgyülése.hogymulatotgondolt
22 enéhrmimadojaraistenveleédesem
S1 isten
S2 vele
S3 édesem
S4 csokol
S5 jahüked
S6 vessefr
```

Normalized Hungarian (accents, word division and punctuation are editorial; square brackets mark letters the writer left out):

**Szeretet[t] édes Jolánkám! Várva várt sorait megkaptam, melynek nagyon megörültem. Kívánom, hogy a legjobb kedvében találja soraim. Ne haragudjon rám, édesem, hogy ma nem mehettem le, de lekéstem a vonatról, amit igazán sajnálok. Számítottam kedden reggel le menni, de azt gondoltam, hétköznap nem alkalmatlankodok. Szerelmem és mindenem, azért nem mehettem ma le, mert a tűzoltó testületne[k] van a közgyűlése. Hogy mulatott? Gondolt-e néh[a] r[á]m, imádójára? Isten vele, édesem!**

**Under the stamp: Isten vele, édesem! Csókolja hű kedvese, Fr…**

English translation: **My beloved sweet Jolánka! I have received your long-awaited lines, which made me very glad. I hope my lines find you in the best of moods. Do not be angry with me, my darling, that I could not come down today, but I missed the train, which I truly regret. I had counted on going down on Tuesday morning, but then I thought that on a weekday I would not trouble you. My love and my all, the reason I could not come down today is that the fire brigade has its general meeting. How did you enjoy yourself? Did you sometimes think of me, your admirer? God be with you, my darling!**

**Under the stamp: God be with you, my darling! Kisses from your faithful sweetheart, Fr…**

Slovak translation: **Moja milovaná sladká Jolánka! Dostal som Vaše dlho očakávané riadky, z ktorých som sa veľmi potešil. Želám si, aby Vás moje riadky zastihli v najlepšej nálade. Nehnevajte sa na mňa, drahá, že som dnes nemohol prísť dole, ale zmeškal som vlak, čo naozaj ľutujem. Počítal som s tým, že pôjdem dole v utorok ráno, ale pomyslel som si, že cez všedný deň nebudem obťažovať. Moja láska a moje všetko, dnes som nemohol prísť dole preto, lebo hasičský zbor má valné zhromaždenie. Ako ste sa zabávali? Spomenuli ste si niekedy na mňa, svojho ctiteľa? S Bohom, drahá!**

**Pod známkou: S Bohom, drahá! Bozkáva Vás Váš verný milý, Fr…**

The writer uses the formal address (Ön) throughout, even in this intimate letter. Isten vele, édesem is written twice, at the end of row 22 and again under the stamp, each on its own signs.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1223/work/decode.py
```

The script uses only the Python standard library. It checks the SHA-256 of all four scans, decodes the manual sign ledger work/ledger.txt, prints the literal rows above and the sign count (414 signs, none without a value), and then prints the normalized text. It does not read the image: the transcription step is manual and was checked independently in review.

## Uncertainties

- **Row 22, néh[a] r[á]m.** This is the weakest point. The signs are clear (e, n, é, the h/p sign, r, m) and no vowel stands between h, r and m, so two vowels are supplied by sense. Literally the row has only néhrm. The sentence around it reads without doubt, so this contracted phrase does not make the card partial.
- **Row 21, van a.** The signs are v, two bars, n, then two bars and a slanting dash. The reviewer confirmed that the dash lies below the bars, directly above the é of row 22, and is slanted like the accent ticks. It is taken as that accent.
- **Signature.** Only f, r can be seen, at the edge of the surviving stamp fragment. Other cards of the family are signed Feri, so that is a likely expansion, but it is not on this card, and whether anything follows under the remnant cannot be seen.
- **d written in the h/p shape.** In de (rows 10, 14) and gondolt (row 21) the sign has the h/p form rather than the usual d. It is read d because only d gives a word.
- **h/p calls.** Every h and p is one sign. P was chosen by word sense in kaptam (row 3) and hétköznap (row 15), h elsewhere.
- **Writer's spellings, normalized:** szeretet for szeretett; haragodjon for haragudjon; szamittottem for számítottam; mulatot for mulatott; oltottestület for tűzoltó testület, with one t too many; testületne with the final k omitted; vessefr with a doubled s in kedvese; and reggelle for reggel le.
- **Damage.** Ink blots touch nagyon (row 4), the p of -nap (row 15) and the u of mulatot (row 21). The postmark crosses the ends of rows 3 and 4, and the first sign under the stamp is smeared by glue. All are legible or confirmed by repetition. The stroke after édesem in row 22 is treated as a point.
- **Accents.** Most accents are not visible and are supplied in normalization. Two dots are not distinguished for ü and ű.
- **Non-blind reading.** The key and the family's formulas were known while reading, for both solver and reviewer. The reviewer's reading tests the pixels but is not a blind one.
- **Postmark.** The place beyond GY and the date beyond 913 are lost.

## Review summary

Reviewer: a separate Claude Opus 5.5 agent, round 1, verdict **REVISE**. It ran the command, decoded the ledger with its own mapping (same letters), and read all rows and the stamp area from its own crops. It upheld the reading, including néhrm, van a, de, imádójára and the blot in testület, and found no sign of a published solution. Its findings, all accepted:

- **Major: row 19 had a sign that is not on the card.** The first ledger had an extra n, giving "ma len". There are three strokes after the e of le, not five, because two had been counted twice at the seam of two overlapping crops. The n was deleted, the sign count fell from 415 to 414, and the claimed slip of the writer was withdrawn. The normalized text already had ma le and did not change.
- **Minor: d of gondolt in row 21.** It has the h/p shape, and this was not disclosed. It is now marked in the ledger and listed above, and the key states which side the short stroke is on: left for the usual d, right for h/p.
- **Minor: signature.** "Feri" in the title was stronger than the card, and it now says Fr… (probably Feri).
- **Minor: descriptions.** The note on oltottestület was corrected, kedvese was named properly, and the count of the word nem was corrected to three.

![Row 19 after correction: te m m a l e m e r ... (review crop, review/work/crops/row19.png)](../review/work/crops/row19.png)

The reading and translations did not change because of the review; only the literal text of row 19 and the record of uncertainties did.

Transcription, key transfer and decipherment by Claude Opus 5.5. The key was reconstructed earlier on the sister cards by an OpenAI GPT solver, with later Claude Opus 5.5 completion.

## Sources

- HC Portal record 1223, captured 2026-11-02: https://crypto.hcportal.eu/dashboard/cryptograms/1223 (source/metadata.md).
- Scans: https://api.hcportal.eu/media/3729/ (picture) and https://api.hcportal.eu/media/3730/ (address); the full URLs and hashes are in SOURCES.md.
- Family key: ciphers/hcp-1216/SOLUTION.md and the sister cards named above.
