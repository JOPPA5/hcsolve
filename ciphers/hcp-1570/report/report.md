# HCP 1570 (pc_hcp_251): a Czech Christmas letter from Pepouš to Anna Tichá

Human solver: Tomáš Pavuk

**Status: deciphered in full (523 of 523 cipher signs, 529 letters). Independent review 1 gave the verdict REVISE. All seven findings were accepted and fixed; four signs in rows R08 to R11 were corrected.** Report dated 2026-10-29.

## Origin and context

The cryptogram is record 1570 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1570), portal name pc_hcp_251. It belongs to the HCPortal collection of cryptographic postcards (private collection). When the record was captured on 2026-10-28, the portal listed it as **Not solved**: category Substitution, date 1902-12-27, language Czech, location Europe, sender Unknown, recipient Anna Tichá. No transcription or solution was attached.

The card is a picture postcard. It was scanned sideways, and turned 90° counter-clockwise the cipher stands in fifteen rows in the upper part of the picture side. Two items on the card are written in plain and are not cipher: the greeting **Veselé vánoce!** ("Merry Christmas!") beside the third row, and the date **27/XII 1902** after the last row. That date agrees with the portal's date. The address side is also in plain: **Anna Tichá, učitelka t.č. v Pelhřimově** ("teacher, currently in Pelhřimov", South Bohemia), with the note **Vlastnoručně dodati!** ("to be delivered into her own hands").

The card belongs to a family of cipher postcards to Anna Tichá. They are in the same hand and the same cipher, and they are signed "Pepouš" (a pet form of Josef). Many of them are deciphered in this repository (for example HCP 1520–1527, 1537, 1541, 1553–1556). The key was transferred from those cards (ciphers/hcp-1520/work/key.json). A partial key for the family was published earlier by Maxim Egorov (https://maxim-egorov.dev/research/anna-ticha-postcards/). This card was therefore read with a **known key**; it is not a new key recovery. No reading of this particular card was supplied or consulted.

![Picture side turned upright: fifteen cipher rows above the picture; Veselé vánoce! and 27/XII 1902 in plain (work/picture-upright.png)](../work/picture-upright.png)

![Address side: Anna Tichá, teacher in Pelhřimov, "Vlastnoručně dodati!" (source/address.jpg)](../source/address.jpg)

## Method

The transcription is **manual**: no OCR was used. The scan was rotated upright and cut into per-row crops (work/R01.png to R15.png, enlarged 3× without filtering). Each row was read sign by sign. Signs that look alike (K and Z, D and T, S and C, M and N, I and Y) were compared with other occurrences of the same shapes on the same card. The rows and the signs (with row, position and crop box) are recorded in work/transcription.json and work/positions.csv.

The OpenAI GPT solver (GPT-6 Astra / GPT-6.1 Sol) made the first transcription and left one sign in row R11 unassigned. Claude Opus 5.5 completed the reading and handed it to review. After review, Claude Opus 5.5 corrected four signs in rows R08 to R11 (see the review summary below). The earlier version is kept in work/v1/.

## Key

Monoalphabetic substitution of base letters (Czech accents are not encoded), with one sign for the digraph CH. The labels are names for the handwritten shapes, not exact reproductions. The shape labelled `m` stands for N and `n` for M; `t` (crossed) for D and `d` (looped) for T; `c` (round) for S and `s` (angular) for C; `b` for P and `p` for B. `y` is the 7-like J sign, and `H` is the capped r-shape for CH.

| Shape | Plain | Shape | Plain | Shape | Plain | Shape | Plain |
|---|---|---|---|---|---|---|---|
| 1 | Y | 2 | U | 3 | O | 4 | I |
| 5 | E | 6 | A | y | J | 8 | L |
| b | P | c | S | d | T | f | V |
| g | K | h | R | m | N | n | M |
| p | B | q | Z | r | H | s | C |
| t | D | H | CH | **G** | **G** | | |

**G** is the family's rare k-shaped sign: an ascender with a loop and a kicked leg. It is clearly different from the looped-descender `g` (K) and from h (R). It occurs twice on this card, in **švagrová** (sister-in-law) and **kolegy** (colleagues). The same sign stands for G on three other family cards: švagra (HCP 1541), telegramy (HCP 1553) and telegram (HCP 1554). G is rare in Czech of the time and occurs mostly in loanwords such as *kolega* and *telegram*.

Frequency of the signs (523 in all): 1:10, 2:17, 3:34, 4:38, 5:67, 6:49, 8:16, G:2, H:6, b:15, c:41, d:31, f:28, g:20, h:27, m:24, n:22, p:8, q:12, r:8, s:13, t:22, y:13.

![Rows R08 to R11 (left part): the k-shaped G in cf6Gh3f6 (švagrová, row 1) and g385G1 (kolegy, row 4); dh4 (tři) in row 2; ycn5 (jsme) in row 3 (work/v2-rows-R08-R11.png)](../work/v2-rows-R08-R11.png)

## Plaintext

Ciphertext as transcribed, row by row:

```text
R01 d4c4s5h1 t4g, 6m4sg3 n3y5 bh5th6r6, q6 r5q32mg1
R02 84cd5g. n58 p1H fc6g 3bh6ft2 bh4y5d4 c n5d832 m6
R03 d5p5, b3m5f6tq c4 cf5 qth6f4 d6g
R04 t832r1n pt5m4n g6q4c. d3 m5cn4c f4s5, th6r32cg2,
R05 t586d4. gt1q y5 H2h6f6, m5b4c5 n4 d6g t832r3 6
R06 y6 c5 d6g hn32d4n 3 cf5 cht5sg3. y6g t6h4 c5 d4
R07 m6 cf6ds4H? 85d3c m5cdh6f48 yc5n cd5th1 f5s5h
R08 2 ph6dh6ms5. cf6Gh3f6 y5 H2h6f6 6, 6sg384f
R09 yc5n n58 y5cd5 dh4 b3qf6m4, m5c58 yc5n m4g6n,
R10 m1phq cdh6f484 ycn5 f5s5h d5m y5cd5 c tf5n6
R11 g385G1 f r3cd4ms4, g6n H3t4n m6 3p5t 6 m6
R12 f5s5h4. fqb3n586 yc4 c3p5 t3n6 d5q f cg2dg2 m6
R13 b5b32c5, gd5h1 m6 d5p5 cd685 fqb3n4m6? d4c4s b2c
R14 6 fh581H b3qth6f2 3t df5r3 m6 3tb3f5t m5cn4hm5 c5
R15 d5c4s4r3 b5b32c5.
```

Literal Czech, as decoded (base letters only):

```text
tisicery dik, anicko moje predraha, za hezounky
listek. mel bych vsak opravdu prijeti s metlou na
tebe, ponevadz si sve zdravi tak
dlouhym bdenim kazis. to nesmis vice, drahousku,
delati. kdyz je churava, nepise mi tak dlouho a
ja se tak rmoutim o sve srdecko. jak dari se ti
na svatcich? letos nestravil jsem stedry vecer
u bratrance. svagrova je churava a, ackoliv
jsem mel jeste tri pozvani, nesel jsem nikam,
nybrz stravili jsme vecer ten jeste s dvema
kolegy v hostinci, kam chodim na obed a na
veceri. vzpomela jsi sobe doma tez v skutku na
pepouse, ktery na tebe stale vzpomina? tisic pus
a vrelych pozdravu od tveho na odpoved nesmirne se
tesiciho pepouse.
```

Normalized Czech. Accents, capitals and punctuation are editorial. *v skutku* is joined to *vskutku*, and *vzpomněla* restores an N that the writer left out (the card has VZPOMELA):

**Tisícerý dík, Aničko moje předrahá, za hezounký lístek. Měl bych však opravdu přijeti s metlou na tebe, poněvadž si své zdraví tak dlouhým bděním kazíš. To nesmíš více, drahoušku, dělati. Když je churavá, nepíše mi tak dlouho a já se tak rmoutím o své srdéčko. Jak daří se ti na svátcích? Letos nestrávil jsem Štědrý večer u bratrance. Švagrová je churavá a, ačkoliv jsem měl ještě tři pozvání, nešel jsem nikam, nýbrž strávili jsme večer ten ještě s dvěma kolegy v hostinci, kam chodím na oběd a na večeři. Vzpomněla jsi sobě doma též vskutku na Pepouše, který na tebe stále vzpomíná? Tisíc pus a vřelých pozdravů od tvého na odpověď nesmírně se těšícího Pepouše.**

English translation: **A thousand thanks, my dearest Anička, for the lovely little card. I really ought to come at you with a broom, since you are ruining your health by staying up so long. You must not do that any more, darling. When she is ill, she does not write to me for so long, and I worry so about my little sweetheart. How are you getting on over the holidays? This year I did not spend Christmas Eve at my cousin's. My sister-in-law is ill and, although I still had three invitations, I went nowhere; instead we spent that evening with two colleagues in the inn where I go for lunch and supper. Did you really think of Pepouš at home, who thinks of you all the time? A thousand kisses and warm greetings from your Pepouš, who looks forward immensely to your reply.**

Slovak translation: **Tisícorá vďaka, Anička moja predrahá, za krásnučký lístok. Mal by som však naozaj prísť na teba s metlou, pretože si svoje zdravie takým dlhým bdením kazíš. To už nesmieš, drahúšik, robiť. Keď je chorá, tak dlho mi nepíše a ja sa tak trápim o svoje srdiečko. Ako sa ti darí počas sviatkov? Tento rok som nestrávil Štedrý večer u bratranca. Švagriná je chorá a hoci som mal ešte tri pozvania, nešiel som nikam, ale ten večer sme ešte strávili s dvoma kolegami v hostinci, kam chodím na obed a na večeru. Spomenula si si doma naozaj aj na Pepouša, ktorý na teba stále spomína? Tisíc bozkov a vrúcnych pozdravov od tvojho Pepouša, ktorý sa nesmierne teší na odpoveď.**

Notes on the reading:

- **s metlou** ("with a broom") is a playful threat. Pepouš scolds Anička for ruining her health by staying up late.
- **Když je churavá, nepíše mi** is literally in the third person ("when she is ill, she doesn't write to me"). It probably refers teasingly to Anička herself, but it is kept as written.
- **Štědrý večer** is Christmas Eve (24 December). The card, dated 27 December, reports how the writer spent it: not with his cousin as usual, because his sister-in-law was ill, but at his regular inn with two colleagues.
- **pus** is the genitive plural of *pusa*, "kiss". **přijeti** and **dělati** are the older infinitives in *-ti*, usual in 1902.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1570/work/decode.py
```

The script uses only the Python standard library and writes no files. It checks the SHA-256 hashes of both scans, the metadata and the record files. It checks that the key equals the family key (ciphers/hcp-1520/work/key.json) plus the G sign. It decodes the manual transcription in work/transcription.txt, re-encodes the whole plaintext through the inverse key, and checks all 523 indexed positions, the counts and the literal block in SOLUTION.md. It prints the fifteen literal rows and a CHECKED line (523 signs, 0 unknown, 6 CH, 2 G, 529 letters). It does not read the image: the transcription step is manual, and in review it was confirmed independently.

## Uncertainties

- **kolegy or kolegi (R11).** The sign after G is read as `1` (Y): it has the lead-in and closed foot of `1` in tisícerý and nýbrž. Its foot is faint over the printed background, however, and `4` (I) would give the spelling *kolegi*. The meaning is the same either way.
- **VZPOMELA (R12).** The writer left out the N of *vzpomněla*. The normalized text adds it.
- **Writer corrections.** In R04 dlouhým, the `1` (Y) is written over another stroke. In R10 strávili, the `8` (L) is darker and appears to have been retraced. Neither changes the reading.
- **The G sign** is not part of the published partial key. Its value rests on its distinct shape and on four cards (this one and HCP 1541, 1553 and 1554) where only G gives a word.
- The accents, punctuation and word joins of the normalized Czech are editorial.
- The key was transferred from earlier family cards, not recovered blind from this card.
- Pepouš (Josef) and the people he mentions (cousin, sister-in-law) are not identified further.
- The postmarks on the address side were not used for dating. The date rests on the plain 27/XII 1902 and the portal metadata.
- Novelty check only: portal status Not solved, and no entry for this card in the AI Decipherment Register (checked 2026-10-29).

## Review summary

Reviewer: a separate Claude Opus 5.5 agent, round 1, verdict **REVISE**. The reviewer ran the reproduction command and decoded the transcription with its own table. It rotated and re-read all fifteen rows against the scan, and zoomed 5 to 10× wherever a reading was doubtful. It confirmed the key, METLOU, TEN, DVEMA, the six CH signs, the dropped N in VZPOMELA, and the exclusion of the plain greeting and date. Its findings, and what changed:

1. **švagrová, not "svakrová" (R08).** The fourth sign is the k-shaped G, not the K sign. The earlier version read it as K and called the word a spelling slip. It is now transcribed as G.
2. **tři, not "tvé" (R09).** The word is D-R-I (`dh4`), not T-V-E. The sentence is "although I still had **three** invitations". The translation changed accordingly.
3. **jsme, not "jsem" (R10).** The signs are J-S-M-E. "strávili jsme" ("we spent") is therefore regular Czech, and the earlier editorial deletion of the final I of strávili was dropped.
4. **kolegy (R11).** The sign left unassigned in the first version is the same k-shaped G. The sign after it is Y, not I. The faint foot is disclosed above.
5. **G as a key entry.** G now rests on visual evidence (two occurrences here, three other family cards) rather than on word fit. The earlier claim that the sign was unique was withdrawn. The reproduction command now prints the complete plaintext.
6. **Overwritten signs** in R04 and R10 are now disclosed.
7. **Stale status text** in SOLUTION.md was replaced by a single current state.

The solver confirmed each correction on enlarged crops before applying it. After the corrections, the solver's transcription is identical, sign for sign, to the reviewer's. The key, the number of signs and the overall content of the letter are unchanged. Three words in rows R08 to R10 changed, and the one unassigned sign in R11 was resolved.

## Sources

- HC Portal record 1570, General, Description and Attachments tabs, captured 2026-10-28: https://crypto.hcportal.eu/dashboard/cryptograms/1570 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/4770/conversions/pc_hcp_251_pic-large.jpg (source/picture.jpg).
- Address side: https://api.hcportal.eu/media/4771/conversions/pc_hcp_251_adr-large.jpg (source/address.jpg).
- Family key: earlier Anna Tichá family cards in this repository, ciphers/hcp-1520/work/key.json; G sign: ciphers/hcp-1541, hcp-1553, hcp-1554.
- Maxim Egorov, Anna Tichá postcards, published partial family key: https://maxim-egorov.dev/research/anna-ticha-postcards/
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-29.
