# HCP 1528 (pc_hcp_209): a Czech letter from Pepouš to Anna Tichá, 5 December 1903

Human solver: Tomáš Pavuk

**Status: deciphered in full (562 cipher signs, 570 letters), with three small marked gaps. Independent review: round 1 REJECT, round 2 REVISE. All findings have been fixed.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1528 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1528), portal name pc_hcp_209. It belongs to the HCPortal collection of cryptographic postcards (private collection). When it was captured on 2026-10-28, the portal listed it as **Not solved**, with these metadata: tags Postcard and HCPortal collection, category Substitution, date 1903-12-05, language Czech, location Europe, sender Unknown, recipient Anna Tichá. No transcription or solution was attached.

The picture side is an engraved mountain landscape with a lake, rocks and trees. Across it the writer wrote 18 rows of cipher, followed by the plain date **5./XII.1903.** The lower rows run over the dark engraving and a printed tree, which hide a few signs.

![Picture side (source/picture.jpg)](../source/picture.jpg)

The address side is in plain cursive: **Velectěná Slečna / slečna Anna Tichá, / učitelka t. č. v / Trhových Svinech / u slečny Karly Jankové, učitelky.** In English: "Honoured Miss Anna Tichá, teacher, at present in Trhové Sviny, care of Miss Karla Janková, teacher". Trhové Sviny is a small town in south Bohemia, near České Budějovice. The card has an Austrian 5-heller stamp with a PRAHA cancellation. The arrival postmark is bilingual, TRHOVÉ SVINY / SCHWEINITZ IN BÖHMEN, and is only partly legible (a "6" and "03" can be read).

![Address side (source/address.jpg)](../source/address.jpg)

The card belongs to a family of cipher postcards to Anna Tichá. They are written in the same hand and the same cipher, and signed "Pepouš", a pet form of Josef. Several of them are deciphered in this repository (for example HCP 1520–1527, 1545 and 1556). Maxim Egorov / Cipher-Atelier published a generic partial key for the family earlier (https://maxim-egorov.dev/research/anna-ticha-postcards/). His list of readings did not include pc_hcp_209. This card was therefore read with a **known, transferred key**. It is not a new key recovery, and no reading of this card was supplied or consulted.

## Method

1. **Key.** The family key was taken over unchanged from the earlier cards (ciphers/hcp-1545/work/key.json).
2. **Transcription.** The work was manual and sign by sign, done on 3–6x enlargements of the scan. No OCR was used, and the portal supplied no transcription. In a first pass, an OpenAI GPT solver (GPT-6 Astra / GPT-6.1 Sol) transcribed the clear passages: 492 signs, with eight gaps where the cipher crosses the dark engraving. Claude Opus 5.5 then read those passages from further enlargements. After review 1 it re-read rows R12–R14 and R16, and after review 2 it re-read row R07.
3. **Decoding.** A script decodes the transcription with the key and round-trips every sign through the inverse key. It also checks SHA-256 hashes of the source scans and of the record files.
4. **Independent check.** In review 2 the reviewer transcribed the whole card again from its own crops and decoded it with a key typed in by hand. The final decoded text is identical to the reviewer's, apart from how the gaps are written.

Reproduction, from the repository root:

```sh
python3 -I ciphers/hcp-1528/work/decode.py
```

It prints the 18 rows below and the line `562 cipher signs decoded -> 570 base letters; 3 marked gaps`.

## Key

The cipher is a simple monoalphabetic substitution (MASC). Its signs are digit-like shapes and Latin-like cursive letters, plus one capped sign for the digraph CH. Word spaces are written. Diacritics are not encoded. The labels below are working names for the handwritten shapes.

| Shape | Plain | Shape | Plain | Shape | Plain | Shape | Plain |
|---|---|---|---|---|---|---|---|
| 1 | Y | 2 | U | 3 | O | 4 | I |
| 5 | E | 6 | A | 7 | J | 8 | L |
| b | P | c | S | d | T | f | V |
| g | K | h | R | m | N | n | M |
| p | B | q | Z | r | H | s | C |
| t | D | ř | CH | | | | |

Note the paired look-alikes: m = N and n = M, t = D and d = T, b = P and p = B. All 22 signs of the key occur on this card, and no other sign does.

## Transcription and literal plaintext

{Q1} marks a visible sign whose identity is not secured. {H1} and {H2} mark ink hidden under the printed foliage.

```text
R01 fh581 t4g q6 th6r1 84cd5g. b3c85ř8 7c5n cf5 cht5sg3 6 q2cd68 7c5n
R02 75cd5 t3n6. 75 n4 74q 3 r3tm5 85b5, 6fc6g t3c2t b84s5 6 ghg{Q1} m5-
R03 7c32 2b8m5 f b3h6tg2. f b3mt584 q5bd6n c5 85g6h5, qt6 n4 t3f384
R04 74q 74d4 t3 2h6t2. 73 n4 m1m4 m5n3s f5h2c5 m5fr3t. 6p1 n5 cht5sg3
R05 cd3m683 g5 nm5, p1ř q6 q6tm32 s5m2 m5řd58. 4 p18 p1ř c4 fc6g bh68
R06 gt1q nm5 d6g r86f6 p38586, 6p1 nm5 {H1} p183 n5 cht5sg3 6cb3m
R07 m6 řf484 p183, b383q483 cf32 h2sg2
R08 m6 r86f2, p186 p1 nm5 74cd5 p385cd4
R09 bh5cd686. r5qg1 c5 f5 cf4m5ř p6f{H2}
R10 6 f1h4t, bh3c4n, c85sm6 76mg3f6
R11 n5 2sd4f5 b3h2s5m4. m5b3c84
R12 n4 fc6g q5 cf4m 3b5d d6g3f1
R13 84cd5g, 76g3 b3c85tm5, gd5h1 nm5
R14 q6hn32d48. cht5sm1 b3qth6f6
R15 d4c4s t832r1ř, f6cm4f1ř b2c
R16 b3c486 d4 df27 b5b32c,
R17 gd5h1 cd685 fh585
R18 fqb3n4m6.
```

```text
VRELY DIK ZA DRAHY LISTEK. POSLECHL JSEM SVE SRDECKO A ZUSTAL JSEM
JESTE DOMA. JE MI JIZ O HODNE LEPE, AVSAK DOSUD PLICE A KRK[Q1] NE-
JSOU UPLNE V PORADKU. V PONDELI ZEPTAM SE LEKARE, ZDA MI DOVOLI
JIZ JITI DO URADU. JO MI NYNI NEMOC VERUSE NEVHOD. ABY ME SRDECKO
STONALO KE MNE, BYCH ZA ZADNOU CENU NECHTEL. I BYL BYCH SI VSAK PRAL
KDYZ MNE TAK HLAVA BOLELA, ABY MNE [H1] BYLO ME SRDECKO ASPON
NA CHVILI BYLO, POLOZILO SVOU RUCKU
NA HLAVU, BYLA BY MNE JISTE BOLESTI
PRESTALA. HEZKY SE VE SVINECH BAV[H2]
A VYRID, PROSIM, SLECNA JANKOVA
ME UCTIVE PORUCENI. NEPOSLI
MI VSAK ZE SVIN OPET TAKOVY
LISTEK, JAKO POSLEDNE, KTERY MNE
ZARMOUTIL. SRDECNY POZDRAVA
TISIC DLOUHYCH, VASNIVYCH PUS
POSILA TI TVUJ PEPOUS,
KTERY STALE VRELE
VZPOMINA.
```

## Czech with editorial accents

**Vřelý dík za drahý lístek. Poslechl jsem své srdéčko a zůstal jsem ještě doma. Je mi již o hodně lépe, avšak dosud plíce a krk[u] nejsou úplně v pořádku. V pondělí zeptám se lékaře, zda mi dovolí již jíti do úřadu. Jo [= Je] mi nyní nemoc věru se nevhod. Aby mé srdéčko stonalo ke mně [= kvůli mně], bych za žádnou cenu nechtěl. I byl bych si však přál, když mne tak hlava bolela, aby mne [H1] bylo mé srdéčko aspoň na chvíli bylo, položilo svou ručku na hlavu, byla by mne jistě bolest přestala. Hezky se ve Svinech bav[ila?] A vyřiď, prosím, slečna Janková [= slečně Jankové] mé uctivé poroučení. Nepošli mi však ze Svin opět takový lístek jako posledně, který mne zarmoutil. Srdečný pozdrav a tisíc dlouhých, vášnivých pus posílá ti tvůj Pepouš, který stále vřele vzpomíná.**

## English translation

**Warm thanks for the dear card. I listened to my sweetheart and stayed at home a little longer. I am already much better, but my lungs and throat are still not quite right. On Monday I will ask the doctor whether he will let me go back to the office. Illness really comes at a bad time for me just now. I would not for any price want my sweetheart to fall ill because of me. And yet, when my head ached so, I would have wished that my sweetheart had been with me at least for a moment and laid her little hand on my head; the pain would surely have stopped. Have a nice time in Sviny! And please give Miss Janková my respectful regards. But do not send me from Sviny another card like the last one, which made me sad. A heartfelt greeting and a thousand long, passionate kisses are sent to you by your Pepouš, who always remembers you warmly.**

## Slovak translation

**Vrelá vďaka za drahý lístok. Poslúchol som svoje srdiečko a zostal som ešte doma. Je mi už oveľa lepšie, ale pľúca a hrdlo ešte nie sú celkom v poriadku. V pondelok sa spýtam lekára, či mi už dovolí ísť do úradu. Choroba mi teraz naozaj prichádza nevhod. Za nič na svete by som nechcel, aby moje srdiečko kvôli mne ochorelo. Predsa by som si však bol prial, keď ma tak bolela hlava, aby moje srdiečko aspoň na chvíľu bolo pri mne a položilo mi rúčku na hlavu; bolesť by iste bola prestala. Pekne sa vo Svinoch zabávaj! A vyrieď, prosím, slečne Jankovej moju úctivú poklonu. Ale nepošli mi zo Svín znova taký lístok ako naposledy, ktorý ma zarmútil. Srdečný pozdrav a tisíc dlhých, vášnivých bozkov ti posiela tvoj Pepouš, ktorý stále vrelo spomína.**

Notes on the reading:

- The content fits the address side. Anna is staying in Trhové Sviny (Czech colloquial *Sviny*, hence *ve Svinech*, *ze Svin*) with Miss Janková, who is greeted in the cipher.
- **JO** (R04) and **slečna Janková** (R10) are kept as written. Standard Czech would have *je* and the dative *slečně Jankové*.
- **bylo … bylo** (R06–R07): the writer repeats *bylo*. The sentence is colloquial and imperfect but coherent, and it is not repaired.
- **pus** is the genitive plural of *pusa*, "kiss". **srdéčko** ("little heart") is the writer's pet name for Anna.

![Rows R06–R08: BYLO after the foliage blot (R06) and NA CHVILI BYLO (R07), the passage corrected after review 2 (work/claude/r2/r06_08.png)](../work/claude/r2/r06_08.png)

## Uncertainties

| Place | Issue |
|---|---|
| Q1, R02 | The last sign of KRK? is g-like, with a trailing hook, not a clear U loop. The word is *krk* or *krku* ("throat"), so the meaning is the same either way. |
| H1, R06 | A printed foliage blot follows ABY MNE. It cannot be shown whether it hides a short word (for instance *u*). |
| H2, R09 | BAV… : the visible ink ends with p6f, and the rest runs into the tree at the card edge. The ending (*bavila*, *bav se* …) is a restoration. |
| R09 HEZKY | The two middle signs sit on dark engraving. The reading is probable. |
| R07 POLOZILO | The second sign is smudged. It looks like O, and the word is secure in context (probable). |
| R05 I | A small sign, partly in foliage, before BYL. Its shape fits I better than J (probable). |
| Diacritics | The cipher has none. All accents in the Czech text are editorial. |

The sender is known only as Pepouš. His civil identity is not established.

## Review summary

The reviewer was a separate Claude Opus 5.5 agent.

- **Round 1: REJECT.** The handed-over reading (DONE1) had misread rows R12–R14. They had been read as "svým zlatoučkovi" and "kde bys mne zarmoutíš", but the card has *mi však ze Svin opět takový lístek, jako posledně, který mne zarmoutil*. TVOJ was corrected to TVUJ. The uncertain places (KRK?, the blot, BAV…) were turned into marked gaps, and the record and the decoder were rebuilt.
- **Round 2: REVISE.** One more word was wrong, in R07. It had been read as PRISLO ("came"), an error that went back to the first GPT transcription. The card has the four-sign word BYLO, the same shape as BYLO in R06. This was corrected, and the translations were changed from "come" to "been with me". POLOZILO was marked as probable. Rows R01–R09 were re-checked against the scan sign by sign. The final transcription (562 signs) is identical to the reviewer's independent one.

## Credits

The first, partial transcription (2026-10-28) was made by an OpenAI GPT solver (GPT-6 Astra / GPT-6.1 Sol). Completion, decipherment and the corrections after review were done by Claude Opus 5.5 (2026-10-29/30). Independent review was done by a separate Claude Opus 5.5 agent. The family key comes from the earlier family cards and the generic partial key of M. Egorov / Cipher-Atelier.
