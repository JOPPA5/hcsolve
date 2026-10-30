# HCP 1543 (pc_hcp_224): a Czech love letter from Pepouš to Anna Tichá

Human solver: Tomáš Pavuk

**Status: deciphered in full: 361 of 363 cipher signs read directly, two blotted signs restored from context and marked. Independent review 1 verdict REVISE; all findings fixed.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1543 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1543), portal name pc_hcp_224. It belongs to the HCPortal collection of cryptographic postcards (private collection). When it was captured on 2026-10-28 the portal listed it as **Not solved**: tags Postcard, HCPortal collection; category Substitution; date 1903-08-17; language Czech; location Europe; sender Unknown; recipient Anna Tichá. No transcription or solution was attached.

The picture side is a printed landscape: a cottage among birch trees, a field path with flowers, a lily-of-the-valley border, and the artist's signature dated 1903. The scan lies sideways. Turned upright (90° clockwise), the cipher fills fourteen handwritten rows across the sky above the landscape; the last four rows are short. Below the picture is the plain date **17./VIII. 1903.** (Monday, 17 August 1903).

The address side is in plain writing: **Velectěná Slečna / slečna Anna Tichá, / učitelka t. č. / v Jindřichově Hradci / u slečny K. Jankové, učitelky.** ("Honoured Miss Anna Tichá, teacher, at present in Jindřichův Hradec, at the home of Miss K. Janková, teacher"). It has an Austrian 5-heller stamp cancelled **PRAHA 7**, and a second, inverted circular postmark whose town and date are not clearly legible on the scan.

The card belongs to a family of cipher postcards to Anna Tichá. They are written in the same hand and the same cipher and signed "Pepouš" (a pet form of Josef). Many are deciphered in this repository (for example HCP 1520–1527, 1537, 1545 and 1556). The key was transferred unchanged from those cards (ciphers/hcp-1520/work/key.json). A partial key for the family was published earlier by Maxim Egorov (https://maxim-egorov.dev/research/anna-ticha-postcards/). This card was therefore read with a **known, transferred key**; it is not a new key recovery. No reading of this card was published or consulted.

![Picture side as scanned (source/picture.jpg)](../source/picture.jpg)

![Picture side turned upright, with the fourteen cipher rows and the plain date 17./VIII. 1903 (work/picture-upright.png)](../work/picture-upright.png)

![Address side: Anna Tichá, teacher, in Jindřichův Hradec, at Miss K. Janková's; stamp cancelled PRAHA 7 (source/address.jpg)](../source/address.jpg)

## Method

The transcription is **manual**. The scan was turned upright, cut into one enlarged crop per row (work/R01.png to R14.png), and each row was read sign by sign. The rows are recorded in work/transcription.json, and every sign position is listed in work/positions.csv. No OCR was used.

The signs are a mixture of digit-like shapes and Latin-like cursive letters. Each sign stands for one plaintext letter, and one special sign stands for the digraph CH. The family key decodes every readable sign of this card into connected Czech. No sign is left unknown or unused.

Two positions are covered by ink blots (R04 and R06). Their letters were not read; they are restored from context and printed in square brackets (see Uncertainties).

The reviewer made its own upright crops at 4–8× and its own statement of the key, and decoded the record with its own script. All fourteen rows matched. The reviewer also found one sign that the record had missed (the C in ANIČKO), which is now included.

## Key

Monoalphabetic substitution. The labels are conventional names for the handwritten shapes. Note the swapped pairs: `m` = N and `n` = M, crossed `t` = D and looped `d` = T, round `c` = S and narrow hooked `s` = C, `b` = P and `p` = B. `y` labels the J sign, which looks like a 7 on this card. `H` labels the capped r-shape that stands for CH.

| Shape | Plain | Shape | Plain | Shape | Plain | Shape | Plain |
|---|---|---|---|---|---|---|---|
| 1 | Y | 2 | U | 3 | O | 4 | I |
| 5 | E | 6 | A | y | J | 8 | L |
| b | P | c | S | d | T | f | V |
| g | K | h | R | m | N | n | M |
| p | B | q | Z | r | H | s | C |
| t | D | H | CH | | | | |

Czech diacritics are not encoded: the cipher writes base letters only (Č as C, Ř as R, and so on). The letters F, G, Q, W and X do not occur in this text.

Frequency of each read sign on the card (361 in all): 1:8, 2:13, 3:33, 4:27, 5:43, 6:26, y:13, 8:15, b:14, c:28, d:15, f:21, g:10, h:24, m:14, n:10, p:3, q:7, r:4, s:11, t:19, H:3.

## Plaintext

Ciphertext as transcribed, row by row, with the 7-shaped J sign written as `y` and the capped CH sign as `H`. `{U1}` and `{U2}` are the two blotted positions.

```text
R01 h3qn486 n6 6m4sg3, fh581 t4g q6 th6r1 84cd5g. bh686
R02 yc4 c4 tm5c y4q 3tb3f5t,6fc6g y6 d5bhf5 tm5c yc5n
R03 84cd5g df2y t3cd68. p18 d5bhf5 fs5h6 3t5c86m
R04 q rh6t{U1}5 6 t3c58 fs5h6 f5s5h t3 bh6r1,gt1
R05 c5 y4q m5t3h2s3 f683. hn32d4 nm5,q5 n3y5
R06 cht5{U2}g3 3b5d cd2m5. bh4 f3t486 yc4 c3p5
R07 H3h3p2 d2 c3t3f32 f3t32,gd5h5 y6 m5f5h4n.
R08 c5dh4 c5 s3 m5yf4s5 th6r32cg2. d4c4s
R09 fh581H,f6cm4 f1H b2c b3c486 d4 cd685
R10 fqb3n4m6y4s4 b5b32c.
R11 c85sm5 y6mg3f5
R12 f1h4t,bh3c4n,
R13 n3y5 b3-
R14 h2s5m4.
```

Literal Czech, as decoded (base letters only; `[C]` is an editorial restoration under a blot):

```text
R01 ROZMILA MA ANICKO, VRELY DIK ZA DRAHY LISTEK. PRALA
R02 JSI SI DNES JIZ ODPOVED,AVSAK JA TEPRVE DNES JSEM
R03 LISTEK TVUJ DOSTAL. BYL TEPRVE VCERA ODESLAN
R04 Z HRAD[C]E A DOSEL VCERA VECER DO PRAHY,KDY
R05 SE JIZ NEDORUCO VALO. RMOUTI MNE,ZE MOJE
R06 SRDE[C]KO OPET STUNE. PRI VODILA JSI SOBE
R07 CHOROBU TU SODOVOU VODOU,KTERE JA NEVERIM.
R08 SETRI SE CO NEJVICE DRAHOUSKU. TISIC
R09 VRELYCH,VASNI VYCH PUS POSILA TI STALE
R10 VZPOMINAJICI PEPOUS.
R11 SLECNE JANKOVE
R12 VYRID,PROSIM,
R13 MOJE PO-
R14 RUCENI.
```

Normalized Czech (diacritics, capitals, punctuation and word joins are editorial):

**Rozmilá má Aničko, vřelý dík za drahý lístek. Přála jsi si dnes již odpověď, avšak já teprve dnes jsem lístek tvůj dostal. Byl teprve včera odeslán z Hradce a došel včera večer do Prahy, kdy se již nedoručovalo. Rmoutí mne, že moje srdečko opět stůně. Přivodila jsi sobě chorobu tu sodovou vodou, které já nevěřím. Šetři se co nejvíce, drahoušku. Tisíc vřelých, vášnivých pus posílá ti stále vzpomínající Pepouš. Slečně Jankové vyřiď, prosím, moje poručení.**

English translation: **My dearest Aničko, warm thanks for your dear card. You wished to have an answer already today, but I only received your card today. It was only sent off yesterday from Hradec and arrived in Prague yesterday evening, when there were no more deliveries. It grieves me that my little heart is ill again. You brought that illness on yourself with soda water, which I do not trust. Spare yourself as much as you can, darling. A thousand warm, passionate kisses are sent to you by your ever-remembering Pepouš. Please give Miss Janková my regards.**

Slovak translation: **Moja premilá Anička, vrúcna vďaka za milý lístok. Želala si si odpoveď už dnes, ale ja som tvoj lístok dostal až dnes. Odoslaný bol až včera z Hradca a do Prahy prišiel včera večer, keď sa už nedoručovalo. Trápi ma, že moje srdiečko zase stoná. Tú chorobu si si privodila sódovou vodou, ktorej ja neverím. Čo najviac sa šetri, miláčik. Tisíc vrúcnych, vášnivých bozkov ti posiela stále spomínajúci Pepouš. Slečne Jankovej, prosím, odovzdaj moje pozdravy.**

Notes on the reading:

- **Aničko** is the vocative of Anička, a pet form of Anna. **srdečko** ("little heart") is a term of endearment for Anna herself, so "my little heart is ill again" means that she is ill.
- **z Hradce**: from (Jindřichův) Hradec, where Anna was staying, according to the address. The writer explains that her card left Hradec only the day before and reached Prague after the last delivery, so he could not answer as soon as she wished.
- **stůně** is the older form of *stoná*, "is ill". **poručení** is the period formula for "regards, compliments" (literally "commendation"). **pus** is the genitive plural of *pusa*, "kiss".
- **Slečna Janková** is the K. Janková, teacher, named on the address side as Anna's host.
- The writer splits several words with gaps or line breaks (NEDORUCO VALO, PRI VODILA, VASNI VYCH, PO-RUCENI); the normalized text joins them.

## Reproduction

From the repository root:

```sh
python3 ciphers/hcp-1543/work/decode.py
```

The script uses only the Python standard library and writes no files. It checks the SHA-256 hashes of the scans and metadata, of the record files, and of the credited reference files. These are the family key in ciphers/hcp-1520/work/ and files in batches/easy-2026-10-28/, so the command runs only in a checkout that contains them. It checks that the key equals the family key and decodes the manual transcription. It re-encodes each row with the inverse key, and checks every indexed position and the saved plaintext. It prints the fourteen literal rows and the line `CHECKS OK: 14 rows; 361 read units; 2 editorial restorations shown as [C]; 363 sign positions.` It does not read the image; the transcription step is manual and was checked against the scan in review. The record files are regenerated by work/build-record.py.

## Uncertainties

- **HRAD[C]E (R04).** After HRA, a crossed `t` (D) is clearly visible. The next position is an ink blot one sign wide, followed by E. The C is restored from context only: *z Hradce* names the recipient's town, and no other letter gives a word. No stroke of the blotted sign can be recovered at the scan's resolution.
- **SRDE[C]KO (R06).** Between E and KO there is one heavy sign: a closed round bowl crossed by a long oblique stroke, like a struck or overwritten sign. Its shape does **not** match the narrow hooked C of this card. *srdečko* is almost certain from the sentence and fits one sign position, so the C is restored editorially. A suggestion that the stroke is a háček (Č) is speculative and is not relied on.
- **Small marks over CH and PUS** in R07 and R09 are not interpreted. All accents in the normalized Czech are editorial and follow standard orthography.
- The sender is known only as Pepouš (Josef); his civil identity is not established.
- The second postmark on the address side is not legible enough to give the arrival date. The date rests on the plain 17./VIII. 1903 on the card and the portal metadata.
- The key was transferred from the earlier family cards and the published partial key, not recovered blind from this card. It decodes every readable sign here without change.

## Review summary

Reviewer: a separate Claude Opus 5.5 agent, round 1, verdict **REVISE**. The reviewer ran the reproduction command and an independent decoder of its own, which agreed on all fourteen rows. It confirmed that the key covers the whole text with no unmapped sign, and that the plaintext is continuous, idiomatic Czech of 1903 that fits the address and the family. It checked most rows sign by sign against its own enlarged crops. Its findings and what changed:

1. **A missed sign in the name (major).** The record had `6m4g3` (ANIKO), with a doubt about whether the fourth sign was K or Z. At 8× the reviewer found a narrow hooked `s` (C) between I and K. The record now reads `6m4sg3` = **ANIČKO**, and the K/Z doubt is gone.
2. **The command did not print the claimed reading (major).** The record still printed placeholders `[UNK1]`/`[UNK2]` while the text claimed HRADCE and SRDEČKO. The blotted positions are now one-sign restorations, and the command prints `Z HRAD[C]E` and `SRDE[C]KO`. SOLUTION.md now gives a single status.
3. **The C of SRDEČKO had been claimed as read from its shape (major).** The reviewer showed that the sign under the blot does not look like the card's C. The claim was withdrawn; the C is now labelled an editorial restoration, and the háček idea is marked speculative.
4. **HRADCE (minor).** The visible D is now in the record as a read sign; only the C is restored.
5. **Editorial inconsistencies (minor).** One spelling, *poručení*, and one Slovak translation are now kept.
6. **Counts (minor).** Updated to 361 read signs + 2 restored = 363 positions (366 letters, as CH occurs three times).

The decoded text changed in one letter (ANIKO → ANIČKO), and the two restorations are now shown as such. The reading was not otherwise changed.

Credits: the initial transcription and first reading were made by an OpenAI GPT solver (GPT-6 Astra) on 2026-10-28. The completion, the corrections after review and this report were made by Claude Opus 5.5 (2026-10-29/30). The review was made by a separate Claude Opus 5.5 agent.

## Sources

- HC Portal record 1543, General, Description and Attachments tabs, captured 2026-10-28: https://crypto.hcportal.eu/dashboard/cryptograms/1543 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/4689/conversions/pc_hcp_224_pic-large.jpg (source/picture.jpg).
- Address side: https://api.hcportal.eu/media/4690/conversions/pc_hcp_224_adr-large.jpg (source/address.jpg).
- Family key: earlier Anna Tichá family cards in this repository, ciphers/hcp-1520/work/key.json.
- Maxim Egorov, Anna Tichá postcards, published partial family key: https://maxim-egorov.dev/research/anna-ticha-postcards/
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-29: no entry for this card.
