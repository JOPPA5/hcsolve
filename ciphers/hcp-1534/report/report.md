# HCP 1534 (pc_hcp_215): a Czech love letter from Pepouš to Anna Tichá

Human solver: Tomáš Pavuk

**Status: deciphered in full (564 of 564 cipher signs, 567 letters).** Independent review: round 1 REJECT (four misread words), round 2 **ACCEPT** after the corrections. Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1534 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1534), portal name pc_hcp_215. It belongs to the HCPortal collection of cryptographic postcards, which is held in a private collection. The portal record was captured on 2026-10-28. At that time it listed the card as **Not solved**, with the tags Postcard and HCPortal collection, category Substitution, date 1903-10-20, language Czech, location Europe, sender Unknown and recipient Anna Tichá. It had no transcription or solution attached.

The picture side shows a seated woman in a green robe holding a winged Cupid, with a bow and a quiver at her feet. The scan is delivered sideways. Turned upright (90° counter-clockwise), the cipher text fills the card in three blocks:

- seven rows across the top (U01–U07);
- thirteen short rows down the right-hand side, beside Cupid's wing (S01–S13);
- four rows along the bottom (L01–L04).

The plain-script date **20./X. 1903** (Tuesday, 20 October 1903) is written at the left, between the side block and the bottom rows. The text reads in the order U, S, L.

The address side is in plain writing: **Velectěná Slečna / slečna Anna Tichá, / učitelka v / Žirovnici / u Počátek.** ("Honoured Miss Anna Tichá, teacher in Žirovnice near Počátky", South Bohemia). The 5-heller Austrian stamp is cancelled PRAHA. The arrival postmark ŽIROVNICE / SEROWITZ reads 21 X 03, the day after the written date. The address side carries no cipher.

The card belongs to a family of cipher postcards to Anna Tichá. They are all in the same hand and the same cipher, and signed by "Pepouš", a pet form of Josef. Many of them have been deciphered in this repository (for example HCP 1520–1527, 1537, 1545 and 1556). The key was transferred from those cards. Maxim Egorov / Cipher-Atelier had already published a partial key for the family and eleven partial readings (https://maxim-egorov.dev/research/anna-ticha-postcards/), but card 215 is not among them. This card was therefore read with a **known, transferred key**. It is not a new key recovery. No published reading of this card was used.

![Picture side as scanned (source/picture.jpg)](../source/picture.jpg)

![Picture side turned upright: seven rows at the top, thirteen down the right beside Cupid's wing, the date 20./X. 1903 at the left, four rows at the bottom (work/upright.png)](../work/upright.png)

![Address side: Anna Tichá, teacher in Žirovnice near Počátky; PRAHA cancellation on the stamp, ŽIROVNICE / SEROWITZ arrival postmark of 21 X 03 (source/address.jpg)](../source/address.jpg)

## Method

The transcription is **manual**. No OCR was used, and the portal supplies no transcription. The scan was rotated upright, and each of the 24 rows was cut out as an enlarged crop and read sign by sign. Each row's crop box and its signs are recorded in work/transcription.json, and each of the 564 signs is indexed by row and position in work/indexed-units.csv.

The work went through several stages:

- **Earlier sessions (2026-10-28).** An OpenAI GPT solver captured the source, transferred the key and made the first transcription. That reading stayed partial: one overwritten cluster in U02 was left unresolved.
- **Completion (2026-10-29).** Claude Opus 5.5 completed the reading and handed it to review.
- **Review 1.** The reviewer found four misread words.
- **Re-check (2026-10-30).** The solver made fresh 3× crops of every row and 6–10× zooms of every disputed word, and re-read the whole card against the scan.
- **Review 2.** The reviewer accepted the corrected reading.

The signs are a mixture of digit-like shapes and Latin-like cursive letters. Each stands for one plaintext letter, except one special sign for the digraph CH. The family key decodes every sign on the card into connected Czech. No sign is unknown and no sign is left over.

## Key

The cipher is a monoalphabetic substitution. The shape labels are conventional names for the handwritten forms, not exact copies. Some labels are easy to mix up:

- `m` stands for N and `n` for M.
- `t` (crossed stem) stands for D and `d` (looped) for T.
- `c` (round) stands for S and `s` (short teardrop, no ascender) for C.
- `b` stands for P and `p` (with a descender) for B.
- `h` (tall looped ascender) stands for R.
- `q` (written like a 9) stands for Z.
- `H` is the ř-like special sign for CH, not an ordinary H.
- `F` is the shallow v-shaped sign for F.

| Shape | Plain | Shape | Plain | Shape | Plain | Shape | Plain |
|---|---|---|---|---|---|---|---|
| 1 | Y | 2 | U | 3 | O | 4 | I |
| 5 | E | 6 | A | 7 | J | 8 | L |
| b | P | c | S | d | T | f | V |
| g | K | h | R | m | N | n | M |
| p | B | q | Z | r | H | s | C |
| t | D | H | CH | F | F | | |

Czech diacritics are not encoded. The cipher writes base letters only, so Č is written as C, Ř as R, Í as I, and so on. The F sign occurs once, in DOUFAL. It was first inferred from context and then compared with the photographed F of the published family card 199 (RUDOLFINA). The two forms agree.

Frequency of each sign on the card (564 in all): 1:9, 2:25, 3:45, 4:40, 5:76, 6:41, 7:16, 8:20, b:16, c:52, d:25, f:24, g:26, h:24, m:32, n:23, p:8, q:11, r:8, s:19, t:20, H:3, F:1.

## Plaintext

Ciphertext as transcribed, row by row (punctuation and line-end hyphens as on the card):

```text
U01 cht5sg3 n375 75t4m5, fh581 t4g q6 fs5h57c4 th6r1 84cd5g,
U02 75mq nm5 b3d5c48. 86cg6 df375 nm5, th6r32cg2, m5cn4hm5
U03 p86q4 6 75 n4 m57n4857c4 2d5r32, gt1q m57c5n c6n c5
U04 c5p32 6 c5 cf5d5n nm5 3pg83b274s4n cb3g375m. fqb3n4-
U05 m6n m6 cf374 r382p4sg2 s4cd32 d6g h6t 6 d6g s6cd3.
U06 cd1cg6 c5 n4 b3 m4 f584s5. 3t5 tm5cg6 q6 n5c4s b375t2
U07 m6 f1h3sm4 cH2q4 s5s48cg32, g m4q c5 d5md3gh6d5
S01 c75t32 f6cg5h4
S02 2t3f5 f5 cf5d5
S03 c4h5n h3qdh32-
S04 c5m4. t32F68
S05 7c5n, q5 t3 d5
S06 t3p1 p2t2
S07 6cb3m c g3m-
S08 s5hd5n cf5
S09 bh6s5 r3d3f,
S10 6fc6g bh3 m6-
S11 f68 bh6s5 g6m-
S12 s586hcg5 c3df6
S13 d3r3 t3s484n.
L01 cf5 d6g f6cm4f5 n486f6m5 cht5sg3 fh585 g c3p5
L02 d4cgm5 6 d4c4s t832r1H, 2bh4nm1H b2c n2 b3c486,
L03 f5sm5 75r3 b5b32c, gd5h1 c5 m6 c84p5m32 t58c4
L04 qbh6f2 m5cn4hm5 d5c4.
```

Literal Czech, as decoded, line for line (base letters only, no accents):

```text
U01 SRDECKO MOJE JEDINE, VRELY DIK ZA VCEREJSI DRAHY LISTEK,
U02 JENZ MNE POTESIL. LASKA TVOJE MNE, DRAHOUSKU, NESMIRNE
U03 BLAZI A JE MI NEJMILEJSI UTEHOU, KDYZ NEJSEM SAM SE
U04 SEBOU A SE SVETEM MNE OBKLOPUJICIM SPOKOJEN. VZPOMI-
U05 NAM NA SVOJI HOLUBICKU CISTOU TAK RAD A TAK CASTO.
U06 STYSKA SE MI PO NI VELICE. ODE DNESKA ZA MESIC POJEDU
U07 NA VYROCNI SCHUZI CECILSKOU, K NIZ SE TENTOKRATE
S01 SJEDOU VASKERI
S02 UDOVE VE SVETE
S03 SIREM ROZTROU-
S04 SENI. DOUFAL
S05 JSEM, ZE DO TE
S06 DOBY BUDU
S07 ASPON S KON-
S08 CERTEM SVE
S09 PRACE HOTOV,
S10 AVSAK PRO NA-
S11 VAL PRACE KAN-
S12 CELARSKE SOTVA
S13 TOHO DOCILIM.
L01 SVE TAK VASNIVE MILAVANE SRDECKO VRELE K SOBE
L02 TISKNE A TISIC DLOUHYCH, UPRIMNYCH PUS MU POSILA,
L03 VECNE JEHO PEPOUS, KTERY SE NA SLIBENOU DELSI
L04 ZPRAVU NESMIRNE TESI.
```

Normalized Czech. The diacritics, capitals, punctuation and the joining of words split across lines are editorial. VASKERI is normalized to *veškeří* and MILAVANE to *milované*.

**Srdéčko moje jediné, vřelý dík za včerejší drahý lístek, jenž mne potěšil. Láska tvoje mne, drahoušku, nesmírně blaží a je mi nejmilejší útěchou, když nejsem sám se sebou a se světem mne obklopujícím spokojen. Vzpomínám na svoji holubičku čistou tak rád a tak často. Stýská se mi po ní velice. Ode dneška za měsíc pojedu na výroční schůzi cecilskou, k níž se tentokráte sjedou veškeří údové ve světě širém roztroušení. Doufal jsem, že do té doby budu aspoň s koncertem své práce hotov, avšak pro nával práce kancelářské sotva toho docílím.**

**Své tak vášnivě milované srdéčko vřele k sobě tiskne a tisíc dlouhých, upřímných pus mu posílá věčně jeho Pepouš, který se na slíbenou delší zprávu nesmírně těší.**

English translation: **My one and only little heart, warm thanks for yesterday's dear note, which pleased me. Your love, darling, makes me immensely happy and is my dearest comfort when I am not content with myself and with the world around me. I think of my pure little dove so gladly and so often. I miss her very much. A month from today I am going to the annual Cecilian meeting, to which this time all the members scattered across the wide world will gather. I had hoped to be finished at least with the concerto of my work by then, but with the rush of office work I will hardly manage it.**

**His so passionately loved little heart he presses warmly to himself and sends it a thousand long, sincere kisses: forever its Pepouš, who is immensely looking forward to the promised longer message.**

Slovak translation: **Moje jediné srdiečko, vrúcna vďaka za včerajší drahý lístok, ktorý ma potešil. Tvoja láska ma, drahúšik, nesmierne blaží a je mi najmilšou útechou, keď nie som spokojný sám so sebou a so svetom, ktorý ma obklopuje. Na svoju čistú holubičku spomínam tak rád a tak často. Veľmi sa mi za ňou cnie. O mesiac odo dneška pôjdem na výročnú cecíliánsku schôdzu, na ktorú sa tentoraz zídu všetci členovia roztrúsení po šírom svete. Dúfal som, že dovtedy budem hotový aspoň s koncertom svojej práce, ale pre nával kancelárskej práce to sotva dosiahnem.**

**Svoje tak vášnivo milované srdiečko vrúcne k sebe tisne a tisíc dlhých, úprimných bozkov mu posiela naveky jeho Pepouš, ktorý sa nesmierne teší na sľúbenú dlhšiu správu.**

Notes on the reading:

- **Third person at the close.** The closing paragraph switches to the third person ("his little heart he presses … forever its Pepouš"). The same closing formula, *věčně jeho Pepouš*, appears on other cards of the family.
- **schůze cecilská.** This is the annual meeting of a Cecilian society. Such societies promoted Catholic church music, and they fit a writer who speaks of a "concerto" of his work. The card itself does not confirm this, so the identification is plausible but unproven.
- **údové** is the period plural of *úd*, "member" (of a society). **pus** is the genitive plural of *pusa*, "kiss".

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1534/work/decode.py
```

The script uses only the Python standard library and writes no files. It does the following:

- checks the SHA-256 hashes of both scans, the manual record (work/transcription.json, work/key.json, work/indexed-units.csv) and two reference files;
- decodes every row and checks each of the 564 indexed positions;
- re-encodes the decoded text with the inverse key and checks the result against the transcription.

It then prints the literal text and the line `CHECK: … 24 rows; 564 indexed marks; 564 assigned units; 0 unresolved overink; 3 CH units; 567 assigned base letters; token round-trip OK.` The script does not read the image. The transcription step is manual and was confirmed independently in review. Because the script verifies reference files outside ciphers/hcp-1534 (in batches/easy-2026-10-28/), it runs only in a full checkout of the repository.

## Uncertainties

- **Two vowel slips, kept as written.**
  - S01 VASKERI. The second sign has a short curled top flag. It is shorter than the clear 6 (A) in MILAVANE, and it cannot be told apart from 5 (E) with certainty. It is read literally as 6. Reading 5 would give VESKERI directly. The editorial word *veškeří* ("all") is the same either way.
  - L01 MILAVANE. The fourth sign is a clear 6 (A) where *milované* needs 3 (O). It is kept literally as a writer's slip.
- **Corrections in the writer's hand.** Each is read as the final ink. The abandoned signs are not reconstructed, and no letter is added for them.
  - U02 MNE (after TVOJE): the n (M) is written over an earlier sign with a descender, perhaps a p (B) begun too early. The word has three positions, like the clean MNE earlier in the same row.
  - S10 AVSAK: the third sign is a c written over an f-like stroke.
  - L03 SLIBENOU: the first sign, c, is heavily blotted.
  - U04 OBKLOPUJICIM: the g is overinked, and the 7 is written over another stroke.
- **Accents and punctuation.** These are editorial. Diacritic marks are not cipher units.
- **Identities.** The sender is known only as Pepouš (Josef). His civil identity is not established, and neither is the meaning of "koncert své práce" ("the concerto of my work").
- **Transferred key.** The key comes from the earlier family cards and the published partial key. It was not recovered blind from this card, but it decodes every sign here without change.
- **Prior publication.** The search was limited to three checks: the portal status (Not solved), the AI Decipherment Register (no entry for this card on 2026-10-29) and the Cipher-Atelier family readings (card 215 absent).

## Review summary

The reviewer was a separate Claude Opus 5.5 agent, who worked independently of the solver.

**Round 1: REJECT.** The reviewer decoded the record with its own script, which builds the key from scratch, and re-read the card from 4–16× crops. It found four misread words:

| Row | First reading | Corrected reading |
|---|---|---|
| L04 | ZABAVU | ZPRAVU |
| L02 | ULIBNYCH | UPRIMNYCH |
| S13 | DOSAHNU | DOCILIM |
| L03 | VERNE | VECNE |

It also raised four further points:

- the unresolved `[?]` mark in U02;
- conflicting status lines and counts, and a duplicated Slovak paragraph;
- the 6/5 doubt in VASKERI;
- several overinks that had not been disclosed.

The solver confirmed all four misreadings on fresh crops and corrected the record. The U02 cluster turned out to be the n of MNE written over an abandoned sign, so it now counts as one unit. SOLUTION.md was rewritten with a single consistent status, text and translation, and the overinks and the VASKERI doubt were disclosed.

**Round 2: ACCEPT.** The reviewer's own decoder and the solver's command now give identical output: 564 units, every key sign used, nothing unknown. The reviewer re-read every corrected row sign by sign at 5–12× and confirmed them. It raised three minor points, and all have been addressed:

- the outdated paragraphs in the working notes are now marked as superseded;
- the VASKERI caveat is repeated in this report;
- the overink corrections are listed in this report.

What changed because of the review: four words of the literal text (now *zprávu*, *upřímných*, *docílím*, *věčně*), with the translations changed to match, and the U02 overink, which is now read as MNE. The rest of the reading is unchanged.

Credits: the source capture, key transfer, first transcription and partial reading were made by an OpenAI GPT solver (GPT-6 Astra) on 2026-10-28. The completion, the round-2 re-check, this report and the closing steps were done by Claude Opus 5.5.

## Sources

- HC Portal record 1534, General, Description and Attachments tabs, captured 2026-10-28: https://crypto.hcportal.eu/dashboard/cryptograms/1534 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/4662/conversions/pc_hcp_215_pic-large.jpg (source/picture.jpg).
- Address side: https://api.hcportal.eu/media/4663/conversions/pc_hcp_215_adr-large.jpg (source/address.jpg).
- Family key: earlier Anna Tichá family cards in this repository (ciphers/hcp-1520/work/key.json, ciphers/hcp-1545/work/key.json).
- Maxim Egorov / Cipher-Atelier, Anna Tichá postcards, published partial family key: https://maxim-egorov.dev/research/anna-ticha-postcards/
- Photographed F reference: published family card pc_hcp_199, https://api.hcportal.eu/media/4614/pc_hcp_199_pic.JPG
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-29.
