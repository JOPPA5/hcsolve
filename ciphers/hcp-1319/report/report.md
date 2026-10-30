# HCP 1319 (cpc_1912-09-_HU__HU_Jasz Arokszalas_jolanka-107): a postponed trip, to Jolánka Tóth

Human solver: Tomáš Pavuk

**Status: all 157 cipher signs in 13 rows are assigned and the message reads as coherent Hungarian; the meaning of one word (*sorozat*) is unverified, and a plain-hand note in the stamp field is only partly read. Independent review 1 verdict REVISE; all findings addressed, with no change to the sense of the message.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1319 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1319), part of Tobias Schrödel's collection of cryptographic postcards. When it was captured on 2026-10-30 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, category Substitution, date and language Unknown, sender Unknown, recipient Tóth Jolánka, with no transcription or solution attached. No published solution of this card was met.

It is a tinted photographic picture postcard of a young couple among leaves, with printed verses (*Szerelemről, boldogságról ábrándozunk Te, meg én*, "We dream of love and happiness, you and I", and rotated lines beginning *Hulló falevél*, not fully transcribed). The picture side has no handwriting and no cipher.

The address side is in plain red-ink handwriting: **Szépreményű Tóth Jolánka úrleánynak, Jász Árokszállás** ("To the promising young lady Jolánka Tóth, Jászárokszállás", Hungary). The left half carries the cipher in thirteen rows. The postmark shows **12 SEP** with the day unread and the place unread. The scan's file name carries 1912-09, which fits if 12 is the year, and a September grape harvest in the message fits too; the year is not proved by the card alone.

The card belongs to the Jolánka family: Hungarian postcards to the same addressee in one invented sign alphabet, several of them signed Feri and finished in this repository (for example HCP 1212, 1213, 1216, 1217, 1218, 1243 and 1301). This card shows no *Feri*, so its sender is not established by the card itself.

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side: thirteen cipher rows on the left, plain address on the right, the stamp field with two handwritten lines top right (source/address-large.jpg)](../source/address-large.jpg)

Other marks, none of them cipher: the address, the printed verses, the postmark, the HCPortal watermark, and two plain-hand lines in the stamp field. Line 1 of those reads *csókolom* ("I kiss you"); line 2 is unread, and neither solver nor reviewer could read it.

## Method

The key was **transferred unchanged** from the finished family cards, above all HCP 1216; this is not a new key recovery. The transcription is new and manual. The solver enlarged each row of the un-converted high-resolution scan (3x to 6x) and recorded a sign ledger, one token per written sign, in work/ledger.txt. It was not blind: the key was known, and word sense guided the calls listed under Uncertainties. No OCR was used.

The reviewer read every row from its own crops, wrote its ledger in shape codes and not letters, and decoded it with its own script. Eleven of thirteen rows agreed sign for sign at once. Row 3 showed a solver error (see Review), and row 9 differs only in how four strokes are counted.

## Key

Simple monoalphabetic substitution with invented graphic signs. The labels are conventional names for the shapes.

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | section mark / S | k | F-like | r |
| six | b | wave | l | right bowl | s |
| short + tall stroke | d | three short strokes | m | gamma/corner | t |
| three bars | e | two strokes | n | plain cross | u |
| joined hook + descender | gy | cursive loop, hooked tail | o | chevron | v |
| tall + short stroke | h / p | crossed curve, straight tail, dot | i | crossed diagonal with tail | z |
| inverted T | j | | | | |

The tall + short sign serves both h and p and is split by sense. Dots over the cross give ü. Accents are mostly unwritten. The family's c, f, g, y and cs do not occur here.

## Plaintext

Literal decipherment, row by row ({x?} marks a value resting on word sense):

```text
01 kedvesjolankam
02 tudatomhogyel
03 utzasonelhalasz
04 tottamegyhetel
05 kesobremostszü
06 retremegyekhol
07 naaso{r?}ozatra
08 vasarnapren{d?}es
09 id{o?}ben{m?}egyekle
10 mostsietekmar
11 istenvelea
12 viszontlatas
13 ra
```

Hungarian, normalized (square brackets mark letters the writer did not write):

Kedves Jolánkám! Tudatom, hogy elut[a]zásom[at] elhalasztottam egy hét[t]el későb[b]re. Most szüretre megyek, holna[p] a sorozatra, vasárnap rendes időben megyek le. Most sietek már. Isten vele! A viszontlátásra.

English:

Dear Jolánka! I am letting you know that I have postponed my departure by a week. Now I am going to the grape harvest, tomorrow to the *sorozat* (tentatively: the army recruitment muster, normally *sorozás*; this sense is inferred, not attested), and on Sunday I am coming down at the usual time. I am in a hurry now. Farewell! Until we meet again.

Slovak:

Milá Jolánka! Oznamujem Vám, že som svoj odchod odložil o týždeň. Teraz idem na oberačku, zajtra na *sorozat* (predbežne: vojenský odvod, bežne *sorozás*; význam je odvodený, nie doložený) a v nedeľu prídem dolu v obvyklom čase. Teraz sa už ponáhľam. S Bohom! Do videnia.

## Reproduction

From the repository root:

```text
python3 -I ciphers/hcp-1319/work/decode.py
```

The script checks the SHA-256 of the two scans in source/ and the two originals in work/hires/, decodes work/ledger.txt (157 signs, row 9 counted as n + m) and prints the literal rows and the normalized text.

## Uncertainties

- **Row 7, *sorozatra*, is the weakest point, in sign and in meaning.** A pale z-class sign is overwritten by a dark stem with a long top bar. The dark ink alone is gamma-shaped (t class), with the pale z arm where an r's mid-bar would be. Only word sense gives r. Czuczor-Fogarasi lists *sorozat* only as "series, list", and two web searches found no recruitment sense. Family cards HCP 1303 and 1304 use the regular *sorozás*, and HCP 1303 has it in April. The 1912 main conscription was late (Debrecen, 12 to 19 August), but no September muster in this district was found. The clause is therefore tentative.
- **Row 3, *elut[a]zásom[at]*:** the card has u t z a s, with no a after t. The writer also wrote n for m, and the ending [at] is supplied: three editorial changes in one word. The writer drops letters elsewhere (*holna*, *hetel*, *kesobre*).
- **Rows 6/7, *holna[p] a*:** the signs are clear (h o l, n a a); the p is supplied.
- **Row 8, *rendes*:** the sign has the tall + short order of h/p, not the short + tall of d. Read d from sense; HCP 1216 has the same irregularity.
- **Row 9, *időben*:** the third sign has the straight tail of the i class and no marks; o/ő rests on sense. The first sign has a smeared dark dab where an i dot belongs and is read i.
- **Row 9, *időben megyek*:** four strokes where n + m needs five. Either n + a compressed m, or a retraced m with n omitted (*időbe megyek*). The sense is the same.
- **Row 3, *halaszt-*:** a blot may hide a third bar (a vs e); sense and the two clear bars of row 4 favour a. The l and s there are irregular in shape.
- **Row 5:** the dots of ü may be ink or spatter from the nearby stain; *szüretre* either way.
- **Accents and spelling:** accents are supplied in normalization; *hetel* → héttel, *kesobre* → későbbre.
- **Not read:** stamp line 2, the postmark place and day, the rotated printed lines. The sender is not established.

## Review summary

A separate Claude Opus 5.5 agent reviewed the handover and tried to refute it. It ran the reproduction command, decoded independently from its own crops and shape ledger, and checked the key against HCP 1216, the language and the context. Verdict: **REVISE**. The message stood; the record needed correcting.

- **Major: row 3 held a sign not on the card.** The solver's ledger had an a between t and z, forced from the word. Removed; the literal row is now `utzasonelhalasz` and the a is shown as supplied.
- **Minor: sign count.** 158 became 157, row 9 counted n + m.
- **Minor: row 9, first sign.** The solver had said no dot was visible; there is a smeared one, so the sign no longer rests on sense.
- **Minor: *sorozat*.** The solver had not checked a dictionary. It has now been checked, with a negative result, and the English and Slovak mark the sense as inferred.
- **Minor: status wording.** "Complete reading" replaced by the exact claim.

## Credits

Source capture, family identification, transcription and decipherment by Claude Opus 5.5; independent review by a separate Claude Opus 5.5 agent. The key comes from the finished Jolánka family cards. No earlier work exists on this number.

## Sources

- HC Portal record 1319, https://crypto.hcportal.eu/dashboard/cryptograms/1319 (rendered 2026-10-30).
- Czuczor and Fogarasi, *A magyar nyelv szótára*, online edition, https://czuczor.oszk.hu, entry *sorozat*.
- *A Város* (Debrecen), 3 August 1912, https://epa.hu/05500/05521/00374/pdf/EPA05521_a_varos_1912_031.pdf.
