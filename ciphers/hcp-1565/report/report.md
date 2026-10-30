# HCP 1565 (pc_hcp_246): a Czech love letter from Pepouš to Anna Tichá

Human solver: Tomáš Pavuk

**Status: deciphered in full.** All 395 cipher signs are read (396 letters), with no unread sign. Independent review 1 gave the verdict REVISE. Its four sign corrections were verified on the scan and adopted. The report is dated 2026-10-29.

## Origin and context

The cryptogram is record 1565 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1565), portal name pc_hcp_246. It belongs to the HCPortal collection of cryptographic postcards (private collection). When it was captured on 2026-10-28 the portal listed it as follows:

- status **Not solved**, category Substitution;
- date 1903-02-19, language Czech, location Europe;
- sender Unknown, recipient Anna Tichá;
- no transcription or solution attached.

**Picture side.** The postcard shows Cupid with wings watering a flower in a pot marked "RR" with a large watering can. It is scanned sideways. Two groups of cipher text are written on it:

- **Bottom rows H01–H04.** Four long rows along the bottom edge of the scan as delivered.
- **Margin rows M01–M05.** Five shorter rows below the picture once the card is turned 90° counter-clockwise. A circular postmark is printed over the starts of these rows. The last margin row is followed by the plain date **19./II 1903** (19 February 1903). This date agrees with the portal date.

**Address side.** It is in plain writing: **Velectěná Slečna / slečna Anna Tichá / učitelka v / Žirovnici / u Počátek** ("Honoured Miss Anna Tichá, teacher in Žirovnice near Počátky", South Bohemia).

**The family.** The card belongs to a family of cipher postcards to Anna Tichá in the same hand and the same cipher, signed "Pepouš" (a pet form of Josef). Several of these cards are deciphered in this repository (for example HCP 1520–1527, 1537, 1544 and 1556). The key was transferred unchanged from those cards (ciphers/hcp-1520/work/key.json). A partial key for the family was published earlier by Maxim Egorov / Cipher-Atelier (https://maxim-egorov.dev/research/anna-ticha-postcards/). This card was therefore read with a **known, transferred key**; the key was not recovered anew. No reading of this particular card was supplied or consulted.

![Picture side turned 90° counter-clockwise: the four bottom rows run up the right edge; the five margin rows are below the picture, with the postmark over their starts, followed by the date 19./II 1903 (work/picture-ccw.png)](../work/picture-ccw.png)

![Address side: Anna Tichá, teacher in Žirovnice near Počátky (source/address.jpg)](../source/address.jpg)

## Method

The transcription is **manual**. No OCR was used and the portal supplied no transcription.

1. **First reading.** An OpenAI GPT solver (GPT-6 Astra / GPT-6.1 Sol) read the nine rows sign by sign from enlarged row crops. It left six places under the postmark (and the closing heart) unread.
2. **Postmark spans.** Claude Opus 5.5, as solver, read those places on enlargements. The signs beneath the postmark are legible through the overprint.
3. **Independent review.** A separate Claude Opus 5.5 reviewer re-read every row on 3–12× enlargements and decoded with its own, independently typed key. It found four ordinary signs that had been misread (see the review summary). After those corrections the solver's reading and the reviewer's reading are identical in every position.

**The cipher.** The signs are digit-like and Latin-like cursive shapes. Each sign stands for one plaintext letter, and one marked sign stands for the digraph CH. The family key decodes every sign into connected Czech, with no unknown or unused sign.

## Key

Monoalphabetic substitution. The labels are conventional names for the handwritten shapes. Several shapes stand for a different letter from the one they resemble:

- `m` = N and `n` = M;
- crossed `t` = D and looped `d` = T;
- round `c` = S and small `s` = C;
- `b` = P and `p` = B;
- `y` = J, and `H` (an r with a small cap) = CH.

| Shape | Plain | Shape | Plain | Shape | Plain | Shape | Plain |
|---|---|---|---|---|---|---|---|
| 1 | Y | 2 | U | 3 | O | 4 | I |
| 5 | E | 6 | A | y | J | 8 | L |
| b | P | c | S | d | T | f | V |
| g | K | h | R | m | N | n | M |
| p | B | q | Z | r | H | s | C |
| t | D | H | CH | | | | |

Czech diacritics are not encoded: the cipher writes base letters only. All 22 signs occur on this card. Frequencies (395 in all):

| Sign | Count | Sign | Count | Sign | Count | Sign | Count |
|---|---|---|---|---|---|---|---|
| 1 | 9 | 2 | 20 | 3 | 33 | 4 | 29 |
| 5 | 44 | 6 | 35 | 8 | 22 | H | 1 |
| b | 15 | c | 22 | d | 16 | f | 26 |
| g | 14 | h | 10 | m | 22 | n | 17 |
| p | 7 | q | 14 | r | 8 | s | 10 |
| t | 15 | y | 6 | | | | |

## Plaintext

Ciphertext as transcribed (♡ is a drawn heart, not a cipher sign):

```text
H01 fh581 b6s 6 b2c2 q6 th6r5 h3qd3n485 bc6mg3 df3y5, y5r3q 3pc6r nm5 f584s5 3p86q48.
H02 cg3t6, q5 d5 m5n3r2 q6 m5 f6cm4f5 qb2c3f6d4? 3tb3f4n t3b4c5n t85 n3qm3cd4 s3 m5y-
H03 th4f5: n6n y4d4 bh4cd4 d1t5m t3 cd6f4d58cg5r3 f5m5sg2 f r3d582 n3m3b382. 3p5tf6n
H04 c m5g384g6 s85m1 f1p3h2, gd5h4 nm5 t2dg84f5 qf32. t32f6n fc6g, q5 c5 f5m5sg2 f1rm2.
M01 b3c486n 6n3hg6, 6p1 ct5848 n5 6m2ms5,
M02 q5 y4 n6n f6cm4f5 h6t 6 6p1 b48m5
M03 q685f68 gf5d4mg2 m6c4 p86q4s4 86cg1.
M04 d4c4s. b3qth6f2 6 t832r1H b2c b3c486
M05 f5sm5 df2y b5b32♡.
```

Literal Czech, as decoded:

```text
H01 VRELY PAC A PUSU ZA DRAHE ROZTOMILE PSANKO TVOJE, JEHOZ OBSAH MNE VELICE OBLAZIL.
H02 SKODA, ZE TE NEMOHU ZA NE VASNIVE ZPUSOVATI? ODPOVIM DOPISEM DLE MOZNOSTI CO NEJ-
H03 DRIVE: MAM JITI PRISTI TYDEN DO STAVITELSKEHO VENECKU V HOTELU MONOPOLU. OBEDVAM
H04 S NEKOLIKA CLENY VYBORU, KTERI MNE DUTKLIVE ZVOU. DOUVAM VSAK, ZE SE VENECKU VYHNU.
M01 POSILAM AMORKA, ABY SDELIL ME ANUNCE,
M02 ZE JI MAM VASNIVE RAD A ABY PILNE
M03 ZALEVAL KVETINKU NASI BLAZICI LASKY.
M04 TISIC. POZDRAVU A DLOUHYCH PUS POSILA
M05 VECNE TVUJ PEPOU♡.
```

Normalized Czech (diacritics, capitals and punctuation are editorial; *doufám* is an editorial correction of the card's DOUVAM; the final Š of Pepouš is supplied from the sister cards):

**Vřelý pac a pusu za drahé roztomilé psánko Tvoje, jehož obsah mne velice oblažil. Škoda, že Tě nemohu za ně vášnivě zpusovati! Odpovím dopisem dle možnosti co nejdříve: mám jíti příští týden do stavitelského věnečku v hotelu Monopolu. Obědvám s několika členy výboru, kteří mne důtklivě zvou. Doufám však, že se věnečku vyhnu.**

**Posílám amorka, aby sdělil mé Anunce, že ji mám vášnivě rád a aby pilně zaléval květinku naší blažící lásky. Tisíc pozdravů a dlouhých pus posílá věčně Tvůj Pepouš ♡.**

English translation: **A warm handshake and a kiss for your dear, sweet little letter, whose contents delighted me greatly. What a pity I cannot smother you with kisses for it! I will answer by letter as soon as possible: next week I am supposed to go to the builders' dance at the Hotel Monopol. I am having lunch with several members of the committee, who are urging me to come. But I hope I will avoid the dance.**

**I am sending a little Cupid to tell my Anunka that I love her passionately, and to diligently water the little flower of our blissful love. A thousand greetings and long kisses, forever your Pepouš ♡.**

Slovak translation: **Vrelé podanie ruky a bozk za Tvoj drahý, milý lístoček, ktorého obsah ma veľmi potešil. Škoda, že Ťa zaň nemôžem vášnivo vybozkávať! Odpoviem listom podľa možnosti čo najskôr: budúci týždeň mám ísť na staviteľský venček v hoteli Monopol. Obedujem s niekoľkými členmi výboru, ktorí ma naliehavo pozývajú. Dúfam však, že sa venčeku vyhnem.**

**Posielam amorka, aby oznámil mojej Anunke, že ju mám vášnivo rád, a aby usilovne polieval kvetinku našej blaživej lásky. Tisíc pozdravov a dlhých bozkov posiela navždy Tvoj Pepouš ♡.**

Notes on the reading:

- **Pac a pusu** ("a paw and a kiss") is a common affectionate Czech formula. *Pac* is a child's word for a hand or handshake.
- **Zpusovati** is a colloquial verb formed from *pusa* ("kiss"): "to cover with kisses".
- **Stavitelský věneček** is a "věneček" (a small ball or dance) of the builders' association. Such dances were a usual part of the Carnival season in February. The writer is invited by the committee but hopes to stay away.
- **Amorek** (little Cupid) and the watering of the flower describe the picture on the card itself, where Cupid waters a potted flower.
- **Anunka** is a pet form of Anna. *Pus* is the genitive plural of *pusa*.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1565/work/decode.py
```

The script uses only the Python standard library and writes no files. It performs these checks:

- the SHA-256 hashes of the source scans and the metadata;
- that the key is byte-identical to the family key in ciphers/hcp-1520/work/key.json;
- it decodes the manual transcription (work/transcription.txt) and re-encodes every row with the inverse key;
- it checks the result against work/transcription.json, work/literal-czech.txt, the indexed positions in work/glyph-index.csv and the literal block in SOLUTION.md.

It prints the nine literal rows and the line `PASS: 9 rows; 395 cipher signs (1 CH, 396 letters); 22/22 classes; 0 unknown; ...`. It does not read the image: the transcription step is manual, and it was confirmed independently in review.

## Uncertainties

- **DOUVAM / doufám (H04).** The fourth sign of the word is read as the V sign. A small stroke at x-height on it might be a crossbar, which would make it a separate F sign, or it might be the joining stroke from the preceding letter. The scan does not decide this. The card literally reads DOUVAM, and *doufám* ("I hope") is an editorial correction.
- **POSILAM (M01).** The first sign lies under heavy postmark dots, and the S is partly blackened by a stamp dot. The visible shapes fit P and S, but this word relies partly on context.
- **The closing heart.** PEPOU is followed by a drawn heart, which is not a cipher sign and is not counted. Whether the heart stands in for the final Š or is pure decoration cannot be decided. The name Pepouš follows the other cards of the family.
- **Close calls checked on the scan by both solver and reviewer:** PAC (H01), the P of ZPUSOVATI under the watermark band (H02), and the final U of KVETINKU and the C of BLAZICI (M03). See the review summary.
- **Editorial choices.** Accents, capitals and punctuation of the normalized Czech are editorial, because the cipher encodes base letters only.
- **Unidentified people and places.** The Hotel Monopol and the builders' dance are not identified historically, and the town is not named on the card. The sender is known only as Pepouš.
- **Transferred key.** The key was transferred from the family, not recovered blind from this card. It decodes every sign here without change.

## Review summary

Reviewer: Claude Opus 5.5 (Anthropic), a separate agent. Round 1 verdict: **REVISE**.

**What the reviewer checked.** It made its own rotated enlargements of every row and of every postmark span, and decoded with an independently typed key.

**What it confirmed.**
- The key is a consistent one-to-one key covering all 22 classes.
- The five postmark-span readings (POSILAM, ZALEVAL, TISIC, POZDRAVU, VECNE) are correct.
- The date agrees with the portal date.

**Its findings, and what changed:**

1. **Broken reproduction.** The previous command failed on a stale hash of an edited notes file and still contained placeholders for the postmark spans. The records now carry the complete transcription, and the command was rewritten. It passes and gives the full plaintext.
2. **DIK → PAC (H01).** The word reads `b6s` (PAC), not `t4g` (DIK). "Dík" had been supplied from context. Corrected.
3. **ZLUSOVATI → ZPUSOVATI (H02).** The second sign is the P sign, partly under the watermark. An invented editorial "zlíbati" was removed.
4. **K VETINKE → KVETINKU (M03).** There is no word space, and the last sign is U, not E. Corrected.
5. **BLAZISI → BLAZICI (M03).** The sixth sign is the small C sign, not the round S sign. Corrected, which closes a previously stated alternative.
6. **Disclosures.** The reliance of POSILAM on context, the non-cipher status of the heart and the editorial status of *doufám* are now disclosed.
7. **Contradictory solution file.** SOLUTION.md had kept an old partial text beside the new one. It now gives one consistent reading.

**Whether the reading changed.** The four corrections change single words. They do not change the key or the sense of the letter. After the corrections the solver's and the reviewer's readings are identical in every position.
