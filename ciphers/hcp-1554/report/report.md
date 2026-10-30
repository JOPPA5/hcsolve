# HCP 1554 (pc_hcp_235): Pepouš to Anna Tichá about a Wednesday meeting

Human solver: Tomáš Pavuk

**Status: the card is read in full.** It has 570 read cipher signs giving 575 letters. Two further signs were inked over by the writer, and one word (mne, "me") is a weaker reading. The independent review in round 1 returned REVISE; all of its findings are addressed below. Report dated 2026-10-29.

## Origin and context

The cryptogram is record 1554 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1554), portal name pc_hcp_235. It belongs to the HCPortal collection of cryptographic postcards, held in a private collection.

When captured on 2026-10-28, the portal listed it as **Not solved**, with these details:

- tags: Postcard, HCPortal collection;
- category: Substitution;
- date: 1903-05-22;
- language: Czech;
- location: Europe;
- sender: Unknown;
- recipient: Anna Tichá.

No transcription or solution was attached.

The picture side shows a young woman in a large feathered hat inside a frame of stylised daisies; the printer's mark reads "Serie 15". The cipher text fills the space to the right of the portrait in sixteen rows. Two short insertions are written above rows 4 and 12, and three further rows run up the left margin. The plain date **22/V. 1903.** stands beside the portrait. 22 May 1903 was a Friday.

The address side is in plain writing: **Velectěná Slečna / slečna Anna Tichá / učitelka v / Žirovnici / u Počátek.** That is, "Honoured Miss Anna Tichá, teacher in Žirovnice near Počátky", in South Bohemia. The card carries an Austrian 5-heller stamp and two partly legible cancellations; one of them reads ŽIROVNICE / SEROWITZ.

![Picture side (source/picture.jpg)](../source/picture.jpg)

![Address side (source/address.jpg)](../source/address.jpg)

The card belongs to a large family of cipher postcards to Anna Tichá in the same hand and the same cipher, signed "Pepouš", a pet form of Josef. Many of them are deciphered in this repository, for example HCP 1520–1527, 1537, 1541, 1553 and 1556. A partial key for the family was published by Maxim Egorov (https://maxim-egorov.dev/research/anna-ticha-postcards/).

This card was therefore read with a **known, transferred key**; the key was not recovered from this card. No reading of this particular card was found or consulted.

## Method

**Transcription.** The transcription is manual. No OCR was used, and the portal supplied no transcription. The rows were cut out, enlarged 3–6× and read sign by sign:

- main rows M01–M16;
- insertions I04 and I12;
- margin rows L01–L03, read after rotating the strip.

**Confusable pairs.** Doubtful signs were compared with clear occurrences of the same shapes elsewhere on the card. In this hand the important pairs are:

- Z and K: Z is a compact "9" with a short open hook; K has a long returning descender loop.
- C and I: C is angular; I has a crossbar.
- I and Y: I has a crossbar; Y has a flag and a foot.

**Earlier work.** The first transcription and the known-key decoding were made by OpenAI GPT (GPT-6 Astra / GPT-6.1 Sol) as a partial candidate. That candidate left two overinked places open: U4 in TELE?RAM and U6 before BUDE. Claude Opus 5.5 completed them and handed the card to review. After the review it corrected the transcription and wrote this report.

**Reproduction.** From the repository root:

```sh
python3 -I ciphers/hcp-1554/work/decode2.py
```

The script uses only the standard library and writes no files. It checks the hashes of the source files and checks that the key equals the family key plus F and G. It then decodes the manual transcription (work/transcription-v2.tsv), compares the result with the saved literal (work/literal-v2.txt) and prints the 21 rows and the counts.

The transcription uses three marks:

- `{x}` marks a sign whose class is uncertain.
- `⟨…⟩` marks signs that were read but are presumed abandoned by the writer.
- `[9:40]` is ordinary numerals, not cipher.

## Key

The cipher is a monoalphabetic substitution with one special sign for the digraph CH. Czech diacritics are not encoded. The labels are conventional names for the handwritten shapes. Note that the shape `m` stands for N and `n` for M; `t` (crossed) for D and `d` (looped) for T; `c` (round) for S and `s` (angular) for C; `b` for P and `p` for B; and `r` for H and `h` for R.

| Shape | Plain | Shape | Plain | Shape | Plain | Shape | Plain |
|---|---|---|---|---|---|---|---|
| 1 | Y | 2 | U | 3 | O | 4 | I |
| 5 | E | 6 | A | 8 | L | y (7-like) | J |
| q | Z | g | K | f | V | h | R |
| t | D | r | H | c | S | s | C |
| n | M | m | N | p | B | b | P |
| d | T | H (capped r) | CH | v (shallow) | F | G (k-shaped) | G |

The shallow-v sign for F is part of the family key but does not occur on this card. The k-shaped G sign occurs once, in TELEGRAM. The same sign stands for G on HCP 1541, 1553 and 1570 of the same family.

## Plaintext

Literal decoding, row by row. These are base letters only, exactly as printed by the command:

```text
M01: vrely dik, anunko moje jedina, za drahou vzpo-
M02: minku z hradce. tazes se, kda se tesim na
M03: schuzku? - tesim se nevyslovne! vzdit opet
M04: budu po tak dlouhem case k sobe privinouti
I04: moci
M05: roztomilou divenku, jez stala se mi tak drahou!
M06: navrhuji, drahousku, abychom si oba navzajem
M07: zaslali jeste v pondeli listky, tak aby-
M08: chom je kazdy z nas v utery obdrzeli a
M09: pripadne snad nove okolnosti nasi schuzky
M10: se t{i}kajici si sdelili, ano anunko?!
M11: kdo by snad z nas proti nadani ujednanym
I12: ve stredu
M12: vlakem prijesti nemohl, zasle telegram
M13: restante do vesel{y}. sjedeme se za
M14: kazdeho pocasi. prijedu rychlikem v [9:40]
M15: rano a srdecko ⟨mo⟩mn{e} bude jiz ocekavati
M16: vid?!
L01: tisic pus zasila a na stredu se
L02: nesmirne tesi stale vzpominajici
L03: a vecne tvuj pepous
```

Normalized Czech. Diacritics, capitals and punctuation are editorial, and the two insertions are placed where the writer marked them. The writer's forms KDA, VZDIT, TIKAJICI and PRIJESTI are normalized to kdy, vždyť, týkající and přijeti.

**Vřelý dík, Anunko moje jediná, za drahou vzpomínku z Hradce. Tážeš se, kdy se těším na schůzku? – Těším se nevýslovně! Vždyť opět budu moci po tak dlouhém čase k sobě přivinouti roztomilou dívenku, jež stala se mi tak drahou! Navrhuji, drahoušku, abychom si oba navzájem zaslali ještě v pondělí lístky, tak abychom je každý z nás v úterý obdrželi a případně snad nové okolnosti naší schůzky se týkající si sdělili, ano, Anunko?! Kdo by snad z nás proti nadání ujednaným ve středu vlakem přijeti nemohl, zašle telegram restante do Veselí. Sjedeme se za každého počasí. Přijedu rychlíkem v 9:40 ráno a srdéčko [mne?] bude již očekávati, viď?! Tisíc pus zasílá a na středu se nesmírně těší stále vzpomínající a věčně tvůj Pepouš.**

English translation: **Warm thanks, my one and only Anunka, for the dear souvenir from Hradec. You ask when I look forward to our meeting? – I look forward to it unspeakably! For after such a long time I shall again be able to hold close the charming girl who has become so dear to me! I suggest, darling, that we both still send each other cards on Monday, so that each of us receives them on Tuesday, and that we tell each other any new circumstances concerning our meeting, yes, Anunka?! Should either of us unexpectedly be unable to come by the train agreed for Wednesday, he will send a telegram poste restante to Veselí. We shall meet whatever the weather. I shall arrive by the express at 9:40 in the morning, and my sweetheart will already be waiting for [me?], won't she?! Sending a thousand kisses and looking forward immensely to Wednesday, ever remembering and eternally your Pepouš.**

Slovak translation: **Vrúcna vďaka, Anunka moja jediná, za drahú pamiatku z Hradca. Pýtaš sa, kedy sa teším na stretnutie? – Teším sa nevýslovne! Veď opäť budem môcť po takom dlhom čase privinúť k sebe roztomilé dievčatko, ktoré sa mi stalo takým drahým! Navrhujem, drahúšik, aby sme si obaja navzájom poslali ešte v pondelok lístky tak, aby sme ich každý z nás v utorok dostali, a prípadné nové okolnosti týkajúce sa nášho stretnutia si oznámili, áno, Anunka?! Kto by z nás azda proti očakávaniu nemohol prísť dohodnutým vlakom v stredu, pošle telegram poste restante do Veselí. Stretneme sa za každého počasia. Prídem rýchlikom o 9:40 ráno a srdiečko [ma?] už bude očakávať, však?! Tisíc bozkov posiela a na stredu sa nesmierne teší stále spomínajúci a večne tvoj Pepouš.**

Notes on the reading:

- **The timetable fits the date.** The card is dated Friday 22 May 1903. Cards sent on Monday (25 May) would arrive on Tuesday (26 May), the day before the Wednesday meeting (27 May).
- **Restante** is poste restante. Veselí is Veselí nad Lužnicí, a railway junction on the line towards Jindřichův Hradec. Hradec is presumably Jindřichův Hradec, the district town near Žirovnice.
- **Rychlík** is an express train.
- **Pus** is the genitive plural of pusa, "kiss".
- **Anunka** is a pet form of Anna. **Srdéčko**, "little heart", is used as an endearment.
- **The writer's spellings.** KDA (kdy), VZDIT (vždyť) and PRIJESTI (přijeti) are kept literally. Both solver and reviewer checked them on the scan.

## Uncertainties

- **[mne?] in M15 is the weakest point.** The word is overinked. In order, it shows a heavy n-shape (M), a 3 (O) with a loop above it, a lighter n (M), an m (N), and a heavy final sign read as 5 (E), though 6 (A) is possible. Read straight through, that is "momne" or "momna", which is not a word. The reading mne assumes that the writer abandoned "mo-" and inked it over. Other possibilities are an abandoned "moje" or a pet name. The sense "my sweetheart will be waiting for me" is natural, but this word is a guess.
- **TELEGRAM (M12).** There is room for exactly one sign between TELE and RAM. It is the family's k-shaped G, written over an earlier stroke whose shape cannot be recovered. The reading TELEGRAM is certain from the sentence.
- **TIKAJICI (M10).** The second sign is an ink blob over an I-like stem. It may be the writer's correction to Y (týkající). The literal marks it `{i}`.
- **VESELI (M13).** The final sign lacks the crossbar of I seen in ZASLALI and PONDELI, and looks more like the Y of VRELY. The literal is therefore vesel{y}. The place meant is clearly Veselí.
- **Insertions.** I04 (moci) and I12 (ve středu) are written above the line. Their placement in the normalized text is editorial. Connecting strokes are not read as cancellations.
- **Scan resolution.** The scan is only 1024 pixels wide, so the signs are 10–20 pixels high. Distinctions such as I/Y and E/A under heavy ink rest on few pixels.
- **Identities.** The sender is known only as Pepouš; his civil identity is not established. The postmark dates are not fully legible.
- **Prior publication.** Nothing was found beyond the portal status (Not solved), the published partial family key, and the AI Decipherment Register. The register had no entry for 1554 or pc_hcp_235 when checked on 2026-10-29.

## Review summary

The reviewer was a separate Claude Opus 5.5 agent (Anthropic), round 1, verdict **REVISE**. It ran the reproduction command and decoded the transcription with its own script and its own copy of the key; all 21 rows agreed. It confirmed that the key is consistent and that the letter frequencies fit Czech. It also checked the transcription against the scan sign by sign in most rows, including a Z/K comparison panel, and judged the text to be fluent Czech of about 1900 that fits the place and the family.

Its findings and what changed:

- **"k hradce" is really "z hradce" (major).** The standalone sign in M02 has the compact Z-shape, not the looped K. This was corrected, and the literal now reads z hradce ("from Hradec").
- **TELEGRAM and MNE were not produced by the command (major).** The G sign was added to the key. U4 and U6 are now in the transcription, with the uncertain and abandoned signs marked, and a new command produces them. SOLUTION.md had contradicted itself because older partial-candidate texts remained in it; it now states one current position.
- **U4 is overwritten (minor).** This is now disclosed.
- **U6 is a guess (minor).** It is shown as [mne?], with the alternatives listed.
- **TIKAJICI overinking (minor).** This is now disclosed and marked uncertain.
- **Stale administrative text and the VESELI final sign (minor).** The stale text was updated. The VESELI sign was compared with the card's I and Y signs and is now marked as a probable Y.

The decoded letters changed in two places: K→Z in M02, and I→Y (uncertain) in M13. The two open spans were filled as proposed before the review.

## Sources

- HC Portal record 1554, General, Description and Attachments tabs, captured 2026-10-28: https://crypto.hcportal.eu/dashboard/cryptograms/1554 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/4722/conversions/pc_hcp_235_pic-large.jpg (source/picture.jpg).
- Address side: https://api.hcportal.eu/media/4723/conversions/pc_hcp_235_adr-large.jpg (source/address.jpg).
- Family key: ciphers/hcp-1520/work/key.json. The G sign comes from ciphers/hcp-1541, hcp-1553 and hcp-1570 in this repository.
- Maxim Egorov, Anna Tichá postcards, partial family key: https://maxim-egorov.dev/research/anna-ticha-postcards/
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-29.
