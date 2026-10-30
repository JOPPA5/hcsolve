# HCP 1549 (pc_hcp_230): a Czech love letter from "P." to Anna Tichá, 2 July 1903

Human solver: Tomáš Pavuk

**Status: deciphered in full with the known Anna Tichá family key; two ink-blotted signs inside one word are restored (DOKONCE), five writer's slips are kept literally and repaired only editorially. Independent review 1 verdict REVISE; all twelve findings addressed (four words corrected by rereading the scan), no change of key.** Report dated 2026-10-29.

## Origin and context

The cryptogram is record 1549 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1549), portal name pc_hcp_230, part of the HCPortal collection of cryptographic postcards (private collection). When captured on 2026-10-28 the portal listed it as **Not solved**, tagged Postcard, HCPortal collection, category Substitution, date 1903-07-02, language Czech, location Europe, sender Unknown, recipient Anna Tichá, with no transcription or solution attached.

It is a picture postcard with a spray of white daisies. The cipher text fills the card around the picture: five rows across the top and five across the bottom (one continuous message, the sentence running on from the top block to the bottom block), an eleven-row addition to the left of the flowers and a three-row addition to the right, both written sideways (turn the card 90° clockwise to read them). The plain date **2/7 1903** (2 July 1903) is written sideways at the right edge.

The address side is in plain writing: **Velectěná Slečna / slečna Anna Tichá / učitelka v / Žirovnici / u Počátek** ("Honoured Miss Anna Tichá, teacher in Žirovnice near Počátky", South Bohemia). It carries an Austrian 5-heller stamp with a PRAHA cancellation and an ŽIROVNICE / SEROWITZ arrival postmark (day and month only partly legible); the printer's line reads "1203 Carl H. Odemar, Magdeburg".

The card belongs to the large family of cipher postcards to Anna Tichá in the same hand and the same cipher (in this repository, e.g. HCP 1520–1556). The writer usually signs "Pepouš"; on this card he signs only with the initial **P.** The key was transferred unchanged from the earlier family cards (ciphers/hcp-1520/work/key.json); a partial key for the family was published by Maxim Egorov (https://maxim-egorov.dev/research/anna-ticha-postcards/). This card was therefore read with a **known key**, not by new key recovery. No reading of this particular card was published or consulted.

![Picture side (source/picture.jpg)](../source/picture.jpg)

![Left addition turned upright (work/left-view.png)](../work/left-view.png)

![Address side (source/address.jpg)](../source/address.jpg)

## Method

The transcription is **manual** (no OCR; the portal supplied none). The first solver (OpenAI GPT, GPT-6 Astra / GPT-6.1 Sol, 2026-10-28) cut the card into four regions and 24 row crops (work/T01.png … R03.png), labelled every sign with the conventional family shape names and decoded them with the family key. Claude Opus 5.5 completed the open places on 2026-10-29. An independent reviewer (a separate Claude Opus 5.5 agent) then decoded the record with its own script, compared all 24 rows with 4–12× enlargements of the scan and found several signs that had been read as the expected Czech word rather than as written; these were corrected in round 2 (see Review summary). The corrected record is work/transcription-r2.json.

## Key

Monoalphabetic substitution of Czech base letters (diacritics are not written), with digit shapes for the vowels, several swapped consonant shapes, and one extra sign (an r with a tilde) for the digraph CH.

| Shape | Plain | Shape | Plain | Shape | Plain | Shape | Plain |
|---|---|---|---|---|---|---|---|
| 1 | Y | 2 | U | 3 | O | 4 | I |
| 5 | E | 6 | A | 8 | L | y (7-shape) | J |
| b | P | c | S | d (looped) | T | f | V |
| g | K | h (tall looped) | R | m | N | n | M |
| p | B | q (9-shape) | Z | r (short) | H | s | C |
| t (crossed) | D | H (r with tilde) | CH | | | | |

The labels are names for handwritten shapes, not printed characters. Note that m stands for N and n for M, crossed t for D and looped d for T, round c for S and angular s for C, b for P and p for B, tall looped h for R and short r for H.

## Plaintext

Ciphertext as transcribed (shape labels; [t], [s] = restored signs under ink blots):

```text
T01 y5 n4 m5f1c83fm5 84d3, q5 c5 t3cd683 n5n2 t3b4c2 d6g3f5r3 f1g86t2! Hd58 yc5n t3b4c
T02 bh5bc6d4, b3m5f6tq 3p6f68 yc5n c5, q5 p2t5 m5cbh6fm5 4md5hbh5d3f6m. p3r2q58 m5qp1-
T03 f683 n4 y4q g d3n2 s6c2. - y5 n4 qf6cd5 84d3, q5 6m2mg6 b3g86t6 nm5 q6 cH3bm6,
T04 6p1H f5t3n5 2h6q58 t4fg2 f2p5s 6 [t]3g3m[s]5 t4fg2, gd5h5 c4 m6t5 fc5 f6q4n, gd5h6
T05 y5 n4 m6t5 fc5 th6r6 6 gd5h32 qp3qm2y4. bh6f5 bh3d3, b3m5f6tq d5 n6n m5f1c83fm5
B01 h6t 6 b3m5f6tq c5 3 d5p5 p3y4n, bc68 yc5n c83f6 d6 6 d3 c4s5 d4n cb4c5, b3m5f6tq
B02 qm6n f38m5 m6q3h1 n3t5hm4H b6m2 3 b3n5h2 g t6n6n. rd58 yc5n q6c86d4 m3f1 t3b4c
B03 6fc6g n1c84n, y584g3q bc6m5 c83f3 t3b32cd4 d6g h2qm5h3 f1g86t2, q5 p2t5 85b5 b3m5H6d4
B04 h3qbh6f2 t2 6q g 3c3pm4n2 c5dg6m4, 6s p2t5-84 c5 Hd4d4 m1m4 6m2mg6 y5cd5
B05 c5 nm32 c5y4d4.
L01 q5 2t5868 b6m ph6dh c f1p3h-
L02 m1n bh3cb5H5n n6d2h4d2
L03 nm5 m5y5m3n p6f483, m1phq
L04 4 d5c483. bh5y4 cf5n2 y5t4-
L05 m5n2 cht5sg2, 6p1 c3 3
L06 b85c2 t3ph5 p6f483. d5c483
L07 p1 nm5 f584s5, gt1p1 bh4
L08 d3n m5q6b3nm583 2b8m5 m6
L09 cf5r3 q6hn32s5m5r3 b.,
L10 gd5h1 n2 b3c486 fh5832 2bh4nm32
L11 b2c2.
R01 rm5f6c c5 m6 nm5 3bh6ft2
R02 6m4sg3 n6? y5 n4 f584s5
R03 cn2dm3 f t2c4!
```

Literal Czech as decoded (base letters; [X] = letter restored under an ink blot):

```text
```text
JE MI NEVYSLOVNE LITO, ZE SE DOSTALO MEMU DOPISU TAKOVEHO VYKLADU! CHTEL JSEM DOPIS
PREPSATI, PONEVADZ OBAVAL JSEM SE, ZE BUDE NESPRAVNE INTERPRETOVAN. BOHUZEL NEZBY-
VALO MI JIZ K TOMU CASU. - JE MI ZVASTE LITO, ZE ANUNKA POKLADA MNE ZA SCHOPNA,
ABYCH VEDOME URAZEL DIVKU VUBEC A [D]OKON[C]E DIVKU, KTERE SI NADE VSE VAZIM, KTERA
JE MI NADE VSE DRAHA A KTEROU ZBOZNUJI. PRAVE PROTO, PONEVADZ TE MAM NEVYSLOVNE
RAD A PONEVADZ SE O TEBE BOJIM, PSAL JSEM SLOVA TA A TO SICE TIM SPISE, PONEVADZ
ZNAM VOLNE NAZORY MODERNICH PANU O POMERU K DAMAM. HTEL JSEM ZASLATI NOVY DOPIS
AVSAK MYSLIM, JELIKOZ PSANE SLOVO DOPOUSTI TAK RUZNERO VYKLADU, ZE BUDE LEPE PONECHATI
ROZPRAVU DU AZ K OSOBNIMU SETKANI, AC BUDE-LI SE CHTITI NYNI ANUNKA JESTE
SE MNOU SEJITI.
ZE UDELAL PAN BRATR S VYBOR-
NYM PROSPECHEM MATURITU
MNE NEJENOM BAVILO, NYBRZ
I TESILO. PREJI SVEMU JEDI-
NEMU SRDECKU, ABY SO O
PLESU DOBRE BAVILO. TESILO
BY MNE VELICE, KDYBY PRI
TOM NEZAPOMNELO UPLNE NA
SVEHO ZARMOUCENEHO P.,
KTERY MU POSILA VRELOU UPRIMNOU
PUSU.
HNEVAS SE NA MNE OPRAVDU
ANICKO MA? JE MI VELICE
SMUTNO V DUSI!
```

Writer's slips, kept literally and repaired editorially: ZVASTE → zv**l**áště (L omitted);
HTEL → **ch**těl (CH tilde omitted, T01 has a proper CHTEL); RUZNERO → různé**h**o (R-shape for H);
ROZPRAVU DU → rozpravu **t**u (D-shape for T); ABY SO → aby **se** (O for E; a faint mark above the sign).
```

Writer's slips, kept in the literal text and repaired in the editorial text: ZVASTE → zv**l**áště (L omitted); HTEL → **ch**těl (tilde of CH omitted; the same word is written correctly in the first row); RUZNERO → různé**h**o (R-shape written for H); ROZPRAVU DU → rozpravu **t**u (D-shape for T); ABY SO → aby **se** (O for E; a faint mark above the sign may be a correction).

Editorial Czech (accents, punctuation and word joins are editorial):

> Je mi nevýslovně líto, že se dostalo mému dopisu takového výkladu! Chtěl jsem dopis přepsati, poněvadž obával jsem se, že bude nesprávně interpretován. Bohužel nezbývalo mi již k tomu času. — Je mi zvláště líto, že Anunka pokládá mne za schopna, abych vědomě urážel dívku vůbec a [d]okon[c]e dívku, které si nade vše vážím, která je mi nade vše drahá a kterou zbožňuji. Právě proto, poněvadž tě mám nevýslovně rád a poněvadž se o tebe bojím, psal jsem slova ta, a to sice tím spíše, poněvadž znám volné názory moderních pánů o poměru k dámám. Chtěl jsem zaslati nový dopis, avšak myslím, jelikož psané slovo dopouští tak různého výkladu, že bude lépe ponechati rozpravu tu až k osobnímu setkání, ač bude-li se chtíti nyní Anunka ještě se mnou sejíti.
>
> Že udělal pan bratr s výborným prospěchem maturitu, mne nejenom bavilo, nýbrž i těšilo. Přeji svému jedinému srdéčku, aby se o plesu dobře bavilo. Těšilo by mne velice, kdyby při tom nezapomnělo úplně na svého zarmouceného P., který mu posílá vřelou upřímnou pusu.
>
> Hněváš se na mne opravdu, Aničko má? Je mi velice smutno v duši!

English translation:

> I am inexpressibly sorry that my letter was given such an interpretation! I wanted to rewrite the letter, because I was afraid it would be misinterpreted. Unfortunately I no longer had time for it. — I am especially sorry that Anunka thinks me capable of knowingly offending a girl at all, and even a girl whom I esteem above all, who is dearer to me than anything and whom I adore. Precisely because I love you inexpressibly and because I fear for you, I wrote those words, and all the more so because I know the loose views of modern gentlemen on their relations with ladies. I wanted to send a new letter, but I think that, since the written word allows such varied interpretation, it will be better to leave this discussion until we meet in person — if, that is, Anunka still wants to meet me now.
>
> That your brother passed his maturita (school-leaving examination) with distinction not only amused me but also pleased me. I wish my one and only little heart a good time at the ball. It would please me very much if it did not quite forget its saddened P., who sends it a warm, sincere kiss.
>
> Are you really angry with me, my Anička? I am very sad at heart!

Slovak translation:

> Je mi nevýslovne ľúto, že môj list dostal taký výklad! Chcel som list prepísať, pretože som sa obával, že bude nesprávne vyložený. Žiaľ, už mi na to nezostával čas. — Je mi zvlášť ľúto, že ma Anunka pokladá za schopného vedome urážať dievča vôbec, a dokonca dievča, ktoré si nadovšetko vážim, ktoré je mi nadovšetko drahé a ktoré zbožňujem. Práve preto, že ťa mám nevýslovne rád a že sa o teba bojím, napísal som tie slová, a to tým skôr, že poznám voľné názory moderných pánov na vzťah k dámam. Chcel som poslať nový list, ale myslím, keďže písané slovo pripúšťa taký rozličný výklad, že bude lepšie nechať tento rozhovor až na osobné stretnutie, ak sa, pravda, bude chcieť Anunka teraz ešte so mnou stretnúť.
>
> To, že pán brat zmaturoval s výborným prospechom, ma nielen zabávalo, ale aj tešilo. Želám svojmu jedinému srdiečku, aby sa na plese dobre zabavilo. Veľmi by ma tešilo, keby pritom celkom nezabudlo na svojho zarmúteného P., ktorý mu posiela vrúcnu úprimnú pusu.
>
> Naozaj sa na mňa hneváš, Anička moja? Je mi veľmi smutno na duši!

Notes on the reading: *Anunka* and *Aničko* are pet forms of Anna; *maturita* is the Central-European school-leaving examination, taken in June–July, which fits the date 2 July; *srdéčku* ("little heart") is the recipient. The letter answers a reproach: Anna had read an earlier letter of his as an insult, and he explains it and proposes to settle it in person.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1549/work/decode-r2.py
```

Standard library only, writes nothing. It checks that work/key.json equals the family key in ciphers/hcp-1520/work/key.json, decodes the 24 rows of work/transcription-r2.json, prints the literal reading and the editorial base reading (with restorations [X] and slip repairs <X> marked) and ends with `CHECKED: 24 rows; 846 plainly read cipher units (7 of them CH); 2 restored units (U1); 0 bounded alternatives; 5 editorial repairs.` The image reading itself is manual; the script does not read the scan.

## Uncertainties

- **DOKONCE (T04) is a restoration.** The word has seven sign positions: an ink blot, a heavily overinked O, K, O, N, a second blot, E. The blots' outlines are compatible with D and C but do not prove them (the second blot has a descender the normal C-sign lacks). *?okon?e* has no other good Czech completion, and "dívku vůbec a dokonce dívku, které…" is idiomatic.
- **Five writer's slips** (listed above) are repaired only editorially.
- **"mne nejenom bavilo"** ("not only amused me") is what the signs say; it is kept even though another verb may have been meant.
- Accents and punctuation of the editorial text are editorial; the cipher writes base letters only.
- The sender is known only as "P." (on other family cards "Pepouš", i.e. Josef); his civil identity and that of Anna's brother are not established.
- Only the 1024-pixel portal image was available; the postmark dates are only partly legible.
- The key was transferred from the family, not recovered blind from this card; it decodes every sign here without change.

## Review summary

Reviewer: a separate Claude Opus 5.5 agent, round 1, verdict **REVISE**. The reviewer ran the round-1 command, decoded the record with its own script (identical output, every sign mapped, key identical to the family key), and checked all 24 rows against enlargements of the scan. It confirmed the identification and overall reading but found:

- four words supplied from expectation instead of read: **ZVASTE** (a Z had been dropped; round 1 read VASTE and proposed *vážně*), **KTERE** (not KTERO), **SICE** (not SNAD), **AČ** (not AS); all four were confirmed on the scan and corrected; each improves the Czech;
- three signs better recorded literally as writer's slips: **DU** for *tu*, **RUZNERO** for *různého*, **HTEL** for *chtěl*;
- shape evidence (not only language) for **ZARMOUCENEHO**, and that **DOKONCE** must be marked as a restoration, not a reading;
- a faint mark above SO in the left addition, and that the round-1 single command still printed unresolved placeholders while the text claimed a complete reading.

In round 2 the record was corrected (work/build-record-r2.py logs each change), a new single command prints the complete literal and editorial readings with all restorations and repairs marked, and SOLUTION.md was cleaned up. The key, the order of the text and the meaning of the letter are unchanged; the corrections affect individual signs.

Credit: transcription, record and first decipherment by OpenAI GPT (GPT-6 Astra / GPT-6.1 Sol); completion, round-2 corrections and this report by Claude Opus 5.5; independent review by a separate Claude Opus 5.5 agent.

## Sources

- HC Portal record 1549, General, Description and Attachments tabs, captured 2026-10-28: https://crypto.hcportal.eu/dashboard/cryptograms/1549 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/4707/conversions/pc_hcp_230_pic-large.jpg (source/picture.jpg).
- Address side: https://api.hcportal.eu/media/4708/conversions/pc_hcp_230_adr-large.jpg (source/address.jpg).
- Family key: earlier Anna Tichá family cards in this repository, ciphers/hcp-1520/work/key.json.
- Maxim Egorov, Anna Tichá postcards, published partial family key: https://maxim-egorov.dev/research/anna-ticha-postcards/
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-29: no entry for this card.
