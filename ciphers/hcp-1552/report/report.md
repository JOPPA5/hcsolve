# HCP 1552 (pc_hcp_233): a Czech love letter from Pepouš to Anna Tichá

Human solver: Tomáš Pavuk

**Status: deciphered in full (410 of 410 cipher signs, 413 letters); independent review 1 verdict REVISE, two misread signs corrected and the records completed afterwards.** Report dated 2026-10-29.

## Origin and context

The cryptogram is record 1552 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1552), portal name pc_hcp_233, part of the HCPortal collection of cryptographic postcards (private collection). When it was captured on 2026-10-28 the portal listed it as **Not solved**, tagged Postcard, HCPortal collection, category Substitution, date 1903-05-30, language Czech, location Europe, sender Unknown, recipient Anna Tichá, with no transcription or solution attached.

It is a picture postcard with a bouquet of three red-pink roses, a rosebud and fern. The card is scanned sideways; turned upright (90° clockwise), the cipher text stands in eleven rows above and to the right of the roses (the letter and its signature) and three rows below them (a postscript), followed by the plain date **30./V. 1903.** (Saturday, 30 May 1903, the day before Whit Sunday).

The address side is in plain writing: **Velectěná Slečna / slečna Anna Tichá / učitelka t. č. v / Pelhřimově.** ("Honoured Miss Anna Tichá, teacher at present in Pelhřimov"), with **Vlastnoručně dodati** ("to be delivered into her own hands"). It carries an Austrian 5-heller stamp cancelled PRAHA and a second, partly legible postmark (year 03). Printed: "Post-Karte" in several languages, "Serie 2273".

The card belongs to a family of cipher postcards to Anna Tichá in the same hand and the same cipher, signed "Pepouš" (a pet form of Josef), many of which are deciphered in this repository (for example HCP 1520–1527, 1533, 1535, 1544, 1545, 1556). On other cards of the family Anna is addressed in Žirovnice, her home town; here she is teaching in Pelhřimov. The key was transferred unchanged from those cards (ciphers/hcp-1520/work/key.json); a partial key for the family was published earlier by Maxim Egorov (https://maxim-egorov.dev/research/anna-ticha-postcards/). This card was therefore read with a **known, transferred key**; it is not a new key recovery. No reading of this particular card was supplied or consulted.

![Picture side as scanned (source/picture.jpg)](../source/picture.jpg)

![Picture side turned upright: eleven cipher rows above the roses, three postscript rows below, and the date 30./V. 1903 (work/picture-upright.png)](../work/picture-upright.png)

![Address side: Anna Tichá, teacher in Pelhřimov; PRAHA stamp cancellation at the top right (source/address.jpg)](../source/address.jpg)

None of the other marks on the card is cipher: the plain date, the address, the printed postcard headings, the stamp and postmarks, and the HCPortal watermark on both sides.

## Method

The transcription is **manual**, with no OCR and no portal transcription. The first solver (OpenAI GPT-6 Astra / GPT-6.1 Sol, 2026-10-28) turned the scan upright, cut one crop per row (work/line01.png to line14.png), read every row sign by sign and recorded it in work/transcription.txt. Each row's position and each sign's row, word and index are in work/inventory.json. Doubtful places were compared with other occurrences of the same shapes on the card (work/native-controls.png). The first solver left one heavily overinked word in row 7 open as an unknown span.

Claude Opus 5.5 completed the reading on 2026-10-29. Enlarged 9–10 times (work/overink-wide.png), the overinked word reads sign by sign as `m 6 f h 6 d 2 .` = NAVRATU, "(after your) return". The `h` and the second `6` are written over in heavier ink, but their shapes stay separate.

![Row 7: the retraced word NAVRATU after "po tvem" (work/overink-wide.png)](../work/overink-wide.png)

The signs are a mixture of digit-like shapes and Latin-like cursive letters, each standing for one plaintext letter, plus one special sign for the digraph CH. The family key decodes every sign of this card into connected Czech, with no unknown or unused sign.

In review an independent reviewer made its own 4× crops of all fourteen rows and 6–10× crops of the difficult places, read them against the transcription, and decoded the transcription with its own key table and script. It found two signs misread (see Review summary). Both were corrected.

## Key

Monoalphabetic substitution; the labels are conventional names for the handwritten shapes, not exact reproductions. Note that the shape labelled `m` stands for N and `n` for M, `t` (crossed) for D and `d` (round, looped) for T, `c` (round) for S and `s` (angular) for C, and `b` for P and `p` for B. `y` labels the J sign (it looks like a 7 on this card; other family key files write it `7`), and `H` the r-shape with a small cap, which stands for the digraph CH (written `ř` in other family key files).

| Shape | Plain | Shape | Plain | Shape | Plain | Shape | Plain |
|---|---|---|---|---|---|---|---|
| 1 | Y | 2 | U | 3 | O | 4 | I |
| 5 | E | 6 | A | y | J | 8 | L |
| b | P | c | S | d | T | f | V |
| g | K | h | R | m | N | n | M |
| p | B | q | Z | r | H | s | C |
| t | D | H | CH | | | | |

The family key also has a shallow v-shaped sign for F; it does not occur on this card. Czech diacritics are not encoded: the cipher writes base letters only (Ř as R, Í as I, and so on).

Frequency of each sign on the card (410 in all): 1:14, 2:16, 3:24, 4:41, 5:41, 6:35, y:10, 8:21, b:16, c:35, d:20, f:19, g:13, h:15, m:25, n:16, p:6, q:11, r:6, s:8, t:15, H:3.

## Plaintext

Ciphertext as transcribed, row by row (punctuation and line-end hyphen as on the card):

```text
01 d4c4s5h1 d4g, t2c4mg3 n3y5 bh5th6r6, q6 84cd5g
02 tm5cm4. fqb3n4m6n m52cd685 c d32q5pm3cd4 6
03 bh5y4 c4 fh585, 6p1 c5 6m2mg6 2g84tm486 6 n5q4
04 cf1n4 th6r1n4 r3tm5 f5c585 cf6dg1 q6q486. d5c4n
05 c5 f584s5 m6 c84p5m1 84cd5g q b58rh4n3f6.
06 t3b4c c b3t3p5mg6n4 q6c82 4rm5t b3 cf6ds4H
07 b3 df5n m6fh6d2. gt1 r3t86c c5 t6d4 f1b3t3p-
08 m4d4 c g6h82c32? - b6s
09 6 d4c4s fh581H, 2bh4nm1H
10 b2c b3c486 d4 f5sm5
11 df2y b5b32c.
12 n58 yc5n f1ph6m1 y4m1 84cd5g, m6bc68
13 yc5n fc6g 3n185n m6 m5y q4h3fm4sg32 df3y4
14 6th5c2. q6c82 d4 y5y t3 q4h3fm4s5?
```

Literal Czech, as decoded, line for line (base letters only, no accents):

```text
01 TISICERY TIK, DUSINKO MOJE PREDRAHA, ZA LISTEK
02 DNESNI. VZPOMINAM NEUSTALE S TOUZEBNOSTI A
03 PREJI SI VRELE, ABY SE ANUNKA UKLIDNILA A MEZI
04 SVYMI DRAHYMI HODNE VESELE SVATKY ZAZILA. TESIM
05 SE VELICE NA SLIBENY LISTEK Z PELHRIMOVA.
06 DOPIS S PODOBENKAMI ZASLU IHNED PO SVATCICH
07 PO TVEM NAVRATU. KDY HODLAS SE DATI VYPODOB-
08 NITI S KARLUSOU? - PAC
09 A TISIC VRELYCH, UPRIMNYCH
10 PUS POSILA TI VECNE
11 TVUJ PEPOUS.
12 MEL JSEM VYBRANY JINY LISTEK, NAPSAL
13 JSEM VSAK OMYLEM NA NEJ ZIROVNICKOU TVOJI
14 ADRESU. ZASLU TI JEJ DO ZIROVNICE?
```

Normalized Czech (diacritics, capitals, punctuation and the joining of VYPODOB-/NITI are editorial; dík is an editorial correction of the card's TIK):

**Tisícerý dík, dušinko moje předrahá, za lístek dnešní. Vzpomínám neustále s toužebností a přeji si vřele, aby se Anunka uklidnila a mezi svými drahými hodně veselé svátky zažila. Těším se velice na slíbený lístek z Pelhřimova. Dopis s podobenkami zašlu ihned po svátcích po tvém návratu. Kdy hodláš se dáti vypodobniti s Karlušou? – Pac a tisíc vřelých, upřímných pus posílá ti věčně tvůj Pepouš.**

**Měl jsem vybraný jiný lístek, napsal jsem však omylem na něj žirovnickou tvoji adresu. Zašlu ti jej do Žirovnice?**

English translation: **A thousand thanks, my dearest darling, for today's card. I think of you constantly and with longing, and I warmly wish that Anunka would calm down and spend a very merry holiday among her dear ones. I am very much looking forward to the promised card from Pelhřimov. I will send the letter with the photographs right after the holidays, after your return. When do you intend to have your picture taken with Karluša? – A paw, and a thousand warm, sincere kisses your Pepouš sends you for ever.**

**I had chosen a different card, but by mistake I wrote your Žirovnice address on it. Shall I send it to you in Žirovnice?**

Slovak translation: **Tisícoraká vďaka, dušička moja predrahá, za dnešný lístok. Neustále s túžbou spomínam a vrúcne si želám, aby sa Anunka upokojila a medzi svojimi drahými prežila veľmi veselé sviatky. Veľmi sa teším na sľúbený lístok z Pelhřimova. List s podobizňami pošlem hneď po sviatkoch, po tvojom návrate. Kedy sa mieniš dať odfotografovať s Karlušou? – Labku a tisíc vrúcnych, úprimných bozkov ti naveky posiela tvoj Pepouš.**

**Mal som vybraný iný lístok, ale omylom som naň napísal tvoju žirovnickú adresu. Mám ti ho poslať do Žirovnice?**

Notes on the reading:

- **svátky** ("the holidays") are Whitsun: the card is dated Saturday 30 May 1903, and Whit Sunday fell on 31 May 1903. The writer will send the photographs after the holidays, when Anna is back.
- **Anunka** is the pet form of Anna used throughout the family; here the writer speaks of her in the third person ("that Anunka would calm down"), an affectionate turn.
- **podobenky** are photographs (portraits); **dáti se vypodobniti** is "to have one's portrait taken". **Karluša** is not otherwise identified.
- **Pac** ("paw", the hand offered in greeting) is a playful closing; **pus** is the genitive plural of pusa, "kiss".
- **TIK / dík.** The second word of row 1 starts with the round d-shape (T), the same as in the first word and in DATI, not the crossed t-shape (D) of DUSINKO and DOPIS. The card literally reads TIK; dík ("thanks") is clearly meant. The same slip occurs on the sister card HCP 1556.
- The postscript explains a mix-up: the card he had first chosen he addressed by mistake to Anna's Žirovnice address, so he offers to send it there.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1552/work/decode.py
```

The script uses only the Python standard library and writes no files. It checks the SHA-256 hashes of both scans, the metadata, the credited reference files and the six record files; checks that the key equals the family key; rebuilds the per-sign inventory from the transcription; checks the literal against work/literal.txt; re-encodes the whole literal with the inverse key; and prints `14 rows; 410 recognized cipher units; 413 recognized base letters; 3 CH units; 0 unknown spans`, followed by the fourteen literal rows. It does not read the image; the transcription step is manual and was checked independently in review. It runs only in a checkout that also contains ciphers/hcp-1520/work/ and batches/easy-2026-10-28/.

## Uncertainties

- **NAVRATU (row 7).** The `h` and the second `6` are retraced in heavier ink. The signs are read as retraced, not cancelled. Whether an earlier, different word lies under the heavier ink cannot be decided from a 1024×674 scan; nothing suggests one. Both the completing solver and the reviewer read NAVRATU from the shapes, and it fits the sentence.
- **SLIBENY (row 5).** The fifth sign is read as the writer's 5 (E): it has the top bar and lower bowl of the 5 and lacks the tall left loop of his 6. This is at the resolution limit; the alternative 6 would give SLIBANY, a non-standard form.
- **TIK** is a writer's slip for dík (see above); one sign of 410.
- **Printed stems.** In the postscript, JINY and OMYLEM cross printed flower stems; no letters are supplied behind them.
- The accents, punctuation and word join of the normalized Czech are editorial. The cipher encodes base letters only.
- The sender is known only as Pepouš (Josef); his civil identity and that of Karluša are not established.
- The key was transferred from the family, not recovered blind from this card; it decodes every sign here without change.

## Review summary

Reviewer: a separate Claude Opus 5.5 agent, round 1, verdict **REVISE**. The reviewer ran the reproduction command, decoded the transcription with its own key table and script (identical output), checked the key against the family key class by class, read all fourteen rows against its own enlargements of the scan, and confirmed NAVRATU from the pixels, the literal TIK, the three CH signs, PODOBENKAMI and VYPODOB-/NITI, and that the address side carries no cipher. It raised six findings, all addressed:

- **ANINKA → ANUNKA (row 3).** The third sign is the U-shaped 2, identical to the 2 that opens the next word, not the I-shaped 4. Corrected; Anunka is the pet name used throughout the family.
- **SLIBANY → SLIBENY (row 5).** The fifth sign is more probably 5 than 6. Corrected; the literal now agrees with the normalized "slíbený".
- **Records still partial.** The transcription, inventory, literal and decoder still carried the row-7 word as an unknown span. They now contain `fh6d2` (NAVRATU), and the decoder reports 410 signs and no unknown span.
- **Contradictory status in SOLUTION.md.** Rewritten to state the complete reading, with the earlier caution kept as history.
- **Translation slips.** One Czech, one Slovak and one English version remain, all corrected.
- **Labels.** The key table now explains that `y` and `H` correspond to `7` and `ř` in other family key files.

The corrections change two letters of the plaintext and none of the key.
