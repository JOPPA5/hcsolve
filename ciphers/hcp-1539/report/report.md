# HCP 1539 (pc_hcp_220): Pepouš declines a concert in Vamberk, a Czech cipher postcard to Anna Tichá

Human solver: Tomáš Pavuk

**Status: deciphered in full (406 cipher signs in 13 rows); one letter of a given name remains uncertain (L[o]la). Independent review 1 verdict REVISE; all eight findings addressed, five transcription errors corrected.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1539 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1539), portal name pc_hcp_220, part of the HCPortal collection of cryptographic postcards (private collection). When captured on 2026-10-28 the portal listed it as **Not solved**, tagged Postcard, HCPortal collection, category Substitution, date 1903-09-10, language Czech, location Europe, sender Unknown, recipient Anna Tichá, with no transcription or solution attached.

It is a picture postcard with a painted rural landscape (a cottage, a path between flowering meadows, birch trees) and a sprig of lily of the valley, scanned sideways. Turned upright (90° clockwise), eleven cipher rows fill the sky above the landscape, and two further cipher rows stand below it, followed by the plain date **10./IX. 1903.** (Thursday, 10 September 1903). The top of a printed birch tree crosses several signs of rows 8–9.

The address side is in plain writing: **Velectěná Slečna / slečna Anna Tichá / učitelka t.č / v Pelhřimově / Vlastnoručně / Dodati.** ("Honoured Miss Anna Tichá, teacher at present in Pelhřimov; to be delivered into her own hands"). The postmarks were not fully transcribed.

The card belongs to the family of cipher postcards to Anna Tichá in the same hand and cipher, signed "Pepouš" (a pet form of Josef), many of which are deciphered in this repository (for example HCP 1520–1527, 1537, 1544, 1556). The key was transferred unchanged from those cards (ciphers/hcp-1520/work/key.json); a partial key for the family was published earlier by Maxim Egorov (https://maxim-egorov.dev/research/anna-ticha-postcards/). This card was therefore read with a **known, transferred key**, not a new key recovery. No reading of this particular card was supplied or found.

![Picture side as scanned (source/picture.jpg)](../source/picture.jpg)

![Picture side turned upright: eleven cipher rows at the top, two closing rows and the date 10./IX. 1903 at the bottom (work/upright.png)](../work/upright.png)

![Address side: Anna Tichá, teacher at present in Pelhřimov, "Vlastnoručně dodati" (source/address.jpg)](../source/address.jpg)

## Method

The transcription is **manual**: the scan was turned upright and each row read sign by sign from enlarged crops (work/row01.png … row13.png). Each row, its crop box and each of the 406 signs with its row and index are recorded in work/inventory.json; the plain row list is work/transcription.txt. No OCR was used. The first transcription and decipherment were made by an OpenAI GPT solver (GPT-6 Astra / GPT-6.1 Sol) on 2026-10-28; Claude Opus 5.5 completed it on 2026-10-29 and, after review, corrected five signs on enlargements (see Review summary).

The signs are digit-like and Latin-like cursive shapes, each standing for one plaintext letter, plus one special sign for CH. The family key decodes every sign of the card into connected Czech; no sign is unknown.

## Key

Monoalphabetic substitution. The labels are conventional names for the handwritten shapes. Note the swapped pairs: `m`→N and `n`→M, `t`→D and `d`→T, `c`→S and `s`→C, `b`→P and `p`→B. `y` labels the 7/J-shaped sign, `H` the ř-shaped sign for the digraph CH.

| Shape | Plain | Shape | Plain | Shape | Plain | Shape | Plain |
|---|---|---|---|---|---|---|---|
| 1 | Y | 2 | U | 3 | O | 4 | I |
| 5 | E | 6 | A | y | J | 8 | L |
| b | P | c | S | d | T | f | V |
| g | K | h | R | m | N | n | M |
| p | B | q | Z | r | H | s | C |
| t | D | H | CH | | | | |

Czech diacritics are not encoded (Č as C, Ř as R, Í as I, and so on).

Frequency of each sign (406 in all, one of them the uncertain `{3|5}`): 1:10, 2:16, 3:25, 4:37, 5:41, 6:42, 8:18, H:1, b:15, c:30, d:20, f:15, g:17, h:19, m:25, n:17, p:8, q:11, r:8, s:14, t:11, y:5.

## Plaintext

Ciphertext as transcribed (`{3|5}` marks the one uncertain sign):

```text
P01 cht5sm1 t4g q6 tm5cm4 84cd5g, y5mq gh4q3f68
P02 c n1n. qdh6d481 c3 3bh6ft2 3p6 n5 84cdg1 q5
P03 tm5 th2r5r3 6 dh5d4r3 d3r3d3 n5c4s5?
P04 p18 yc5n f1qf6m, 6p1H cb3822s4mg3f68 m6 r32c85
P05 bh4cd4 n5c4s f5 f6np5hg2, gt5 p2t5 2cb3h6t6m6
P06 6g6t5n45 m6 b6n6dg2 q5nh585r3 g6b58m4g6
P07 f1cg3s486, bh4 m4q n6 2s4mg3f6d4 d5q
P08 b6m4 n6d2h3f6 6 b46m4cdg6 8{3|5}86 p5h6m3f6
P09 6 ph6dh6m5s f1cg3s48. m5n3r8 yc5n fc6g m4s
P10 2hs4d5r3 c84p4d4 6 m5ycb4c5,
P11 q5 c5 m5c2s6cdm4n.
P12 d4c4s b2c q6c486 d4 b5b32c. f1h4t
P13 bh3c4n c85sm5 y6mg3f5 n5 b3h2s5m4.
```

Literal Czech, as decoded (base letters only):

```text
P01 SRDECNY DIK ZA DNESNI LISTEK, JENZ KRIZOVAL
P02 S MYM. ZTRATILY SO OPRAVDU OBA ME LISTKY ZE
P03 DNE DRUHEHO A TRETIHO TOHOTO MESICE?
P04 BYL JSEM VYZVAN, ABYCH SPOLUUCINKOVAL NA HOUSLE
P05 PRISTI MESIC VE VAMBERKU, KDE BUDE USPORADANA
P06 AKADEMIE NA PAMATKU ZEMRELEHO KAPELNIKA
P07 VYSKOCILA, PRI NIZ MA UCINKOVATI TEZ
P08 PANI MATUROVA A PIANISTKA L{O|E}LA BERANOVA
P09 A BRATRANEC VYSKOCIL. NEMOHL JSEM VSAK NIC
P10 URCITEHO SLIBITI A NEJSPISE,
P11 ZE SE NESUCASTNIM.
P12 TISIC PUS ZASILA TI PEPOUS. VYRID
P13 PROSIM SLECNE JANKOVE ME PORUCENI.
```

Normalized Czech (accents, capitals and punctuation editorial; SO is normalized to *se* and NESUCASTNIM to *nezúčastním*):

**Srdečný dík za dnešní lístek, jenž křižoval s mým. Ztratily se opravdu oba mé lístky ze dne druhého a třetího tohoto měsíce? Byl jsem vyzván, abych spoluúčinkoval na housle příští měsíc ve Vamberku, kde bude uspořádána akademie na památku zemřelého kapelníka Vyskočila, při níž má účinkovati též paní Maturová a pianistka L[o]la Beranová a bratranec Vyskočil. Nemohl jsem však nic určitého slíbiti a nejspíše, že se nezúčastním. Tisíc pus zasílá ti Pepouš. Vyřiď prosím slečně Jankové mé poručení.**

English translation: **Hearty thanks for today's card, which crossed with mine. Have both my cards of the 2nd and 3rd of this month really been lost? I have been asked to take part, playing the violin, next month in Vamberk, where an academy (a memorial concert) is to be held in memory of the late bandmaster Vyskočil; Mrs Maturová, the pianist L[o]la Beranová and cousin Vyskočil are also to perform there. But I could not promise anything definite, and most likely I shall not take part. Pepouš sends you a thousand kisses. Please give Miss Janková my regards.**

Slovak translation: **Srdečná vďaka za dnešný lístok, ktorý sa skrížil s mojím. Naozaj sa stratili oba moje lístky z druhého a tretieho dňa tohto mesiaca? Bol som vyzvaný, aby som budúci mesiac vo Vamberku spoluúčinkoval na husliach; bude tam usporiadaná akadémia na pamiatku zosnulého kapelníka Vyskočila, na ktorej má účinkovať aj pani Maturová, klaviristka L[o]la Beranová a bratranec Vyskočil. Nemohol som však nič určité sľúbiť a najskôr sa nezúčastním. Tisíc bozkov ti posiela Pepouš. Odovzdaj, prosím, slečne Jankovej môj pozdrav.**

Notes on the reading:

- **křižoval s mým** ("crossed with mine"): Anna's card and his own passed each other in the post.
- **lost cards of the 2nd and 3rd:** a recurring complaint in this family of cards (compare HCP 1556).
- **akademie** is the usual period word for a festive concert-and-recitation evening; *kapelník* is a bandmaster. Vamberk is a town in eastern Bohemia.
- **mé poručení** is the period formula for "my respects/regards".
- **Pepouš** is the family's usual signature.

## Reproduction

From the repository root (read-only, standard library only):

```sh
python3 -I ciphers/hcp-1539/work/decode.py
```

The script checks the SHA-256 hashes of both scans and the metadata, of the credited reference files (ciphers/hcp-1520/work/key.json and files in batches/easy-2026-10-28/) and of the manual record files; checks every indexed position, applies the key in work/key.json, re-encodes every token and prints the 13 literal rows with the line `13 rows; 406 indexed glyphs; 1 bounded alternatives`. It does not read pixels: the transcription is manual and was checked against the scan in review. SOLUTION.md gives the machine-specific Python path; plain `python3 -I` gives the same result. The script runs only in a checkout that also contains the referenced files outside this directory.

## Uncertainties

- **The pianist's given name.** The name has four signs `8 ? 8 6`, crossed by the printed tree. The second sign is a closed loop, read 3/O (**Lola**, preferred) with 5/E (**Lela**) possible.

![Given name in row 8, red channel, 12× (work/r8-name-12x-red.png): four signs 8, closed loop, 8, 6](../work/r8-name-12x-red.png)

- **Writer's spellings:** row 2 has `c3` = SO where *se* is meant; row 11 has NESUCASTNIM (s for z) for *nezúčastním*. Both are kept in the literal text.
- Accents, punctuation and capitals of the normalized Czech are editorial.
- The persons (bandmaster Vyskočil and his cousin, Mrs Maturová, the pianist Beranová, Miss Janková) and the Vamberk academy were not identified in historical sources. The sender is known only as Pepouš.
- The key was transferred from the family, not recovered blind from this card; it decodes every sign here without change.
- The postmarks were not fully transcribed; the date rests on the plain 10./IX. 1903 and the portal metadata.

## Review summary

Reviewer: Claude Opus 5.5 (Anthropic), a separate agent, round 1, verdict **REVISE**. The reviewer ran the reproduction command, decoded the transcription with its own independent script and key (identical output, no unmapped sign), rotated the scan itself and checked every row at 3× and the difficult places at 6–16×. It confirmed the key and the content, but found five transcription errors and unsupported editorial forms. All were checked again on enlargements and accepted:

1. Row 2: `c m4n` (S NIM) → `c n1n` = **S MYM** ("crossed with mine").
2. Row 4: a second `2` was missing → **SPOLUUCINKOVAL**.
3. Row 8: the given name has four signs, not three; the earlier adoption of "Ela" was withdrawn → **L{O|E}LA**.
4. Row 9: `ph6dh6 m6s` (BRATRA NAC) → `ph6dh6m5s` = **BRATRANEC** (the sign is the flat-topped 5, not the tall 6).
5. Row 11: `q` → `c`, literal **NESUCASTNIM** (writer's spelling).
6. Editorial forms "Výškocil", "Ela" and "bratr" were removed and one consistent normalized text and translation built from the corrected literal text.
7. Signature PEPOUS and the literal SO were confirmed; the old `{5|c}` alternative in the signature was removed.
8. Status, counts (406 signs) and all working records were regenerated.

The substance of the message did not change; the corrections made it better Czech (s mým, spoluúčinkoval, bratranec) and reduced the open points to one letter of a name.

## Sources

- HC Portal record 1539, General, Description and Attachments tabs, captured 2026-10-28: https://crypto.hcportal.eu/dashboard/cryptograms/1539 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/4677/conversions/pc_hcp_220_pic-large.jpg (source/picture.jpg).
- Address side: https://api.hcportal.eu/media/4678/conversions/pc_hcp_220_adr-large.jpg (source/address.jpg).
- Family key: earlier Anna Tichá family cards in this repository, ciphers/hcp-1520/work/key.json.
- Maxim Egorov, Anna Tichá postcards, published partial family key: https://maxim-egorov.dev/research/anna-ticha-postcards/
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-29: no entry for this card.
