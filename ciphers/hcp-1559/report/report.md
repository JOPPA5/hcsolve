# HCP 1559 (pc_hcp_240): Pepouš writes to Anna Tichá about a visitor

Human solver: Tomáš Pavuk

**Status: deciphered (221 cipher signs). 216 signs are read directly from the scan. One more is a faint trace read with low confidence. At the ends of two smudged words, four letters are restored from context and marked as such. Independent review 1 gave the verdict REVISE. The findings concerned record keeping and the marking of restorations, and all of them are addressed. The reading did not change.** Report dated 2026-10-29.

## Origin and context

The cryptogram is record 1559 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1559). Its portal name is pc_hcp_240, and it belongs to the HCPortal collection of cryptographic postcards (private collection). When it was captured on 2026-10-28, the portal listed it as follows:

- status **Not solved**
- tags Postcard and HCPortal collection
- category Substitution
- date 1903-03-29, language Czech, location Europe
- sender Unknown, recipient Anna Tichá
- no transcription or solution attached

It is an Art Nouveau picture postcard: a young couple and a winged child (a cupid) in a floral frame with clover ornaments. The card bears a printed red four-line verse in Czech that begins "V mém srdci pouze jedno přání". The verse is ordinary print, not cipher. The scan lies sideways; turned upright (90° counter-clockwise), the card shows the plain handwritten date **29./III. 1903.** (Sunday, 29 March 1903) beside the verse, and below the picture five rows of cipher text.

The address side is in plain writing: **Velectěná Slečna / slečna Anna Tichá / učitelka v / Žirovnici / u Počátek.** ("Honoured Miss Anna Tichá, teacher in Žirovnice near Počátky", South Bohemia). It carries a stamp and overlapping PRAG and ŽIROVNICE / SEROWITZ postmarks. No other cipher text was found on either side.

The card belongs to a family of cipher postcards to Anna Tichá, all in the same hand and the same cipher. They are signed "Pepouš", a pet form of Josef, and many of them are deciphered in this repository (for example HCP 1520–1527 and 1537–1556). The key used here was transferred from those cards (ciphers/hcp-1520/work/key.json). Maxim Egorov had earlier published a partial key for the family (https://maxim-egorov.dev/research/anna-ticha-postcards/). This card was therefore read with a **known, transferred key**; it is not a new key recovery. No reading of this particular card was supplied or consulted.

![Picture side turned upright: the red printed verse, the plain date 29./III. 1903 and the five cipher rows below the picture (work/upright.png)](../work/upright.png)

![Address side: Anna Tichá, teacher in Žirovnice near Počátky (source/address.jpg)](../source/address.jpg)

## Method

The transcription is **manual**. The solver read the five rows sign by sign from enlarged crops (work/R01.png to R05.png). No OCR was used.

The first working record left four smudged places as unknown spans of unknown length: the ends of the words NEODESLA-, SVA-, SPOLECN- and PSANK-. These places were then examined on 4–12× enlargements:

| Place | What the scan shows | Reading |
|---|---|---|
| R01 after NEODESLA | A further two-lobed sign, the same shape as this hand's L. It is smudged but clearly visible. | NEODESLA**L** (read) |
| R02 after SVA | A clear k-shaped sign followed by a smear holding one dark stroke that cannot be identified. | SVA**G[R]**: G read, R restored |
| R03 after SPOLECN | Three sign positions before the full stop. Their shapes are too damaged to classify. | SPOLECN**[OST]** (restored) |
| R04 after PSANK | A small O-like trace before the full stop. | PSANK**(O)** (low confidence) |

![The four smudged places and the other control crops, enlarged (work/controls.png)](../work/controls.png)

The k-shaped sign stands for G in this family. That value was not invented for this card: it is attested on other family cards, in SVAGRA (HCP 1541), TELEGRAM(Y) (HCP 1553, 1554) and KOLEGY (HCP 1570).

The restorations follow from the sentences:

- *švagr mého bratra*, "my brother's brother-in-law"
- *dělám společnost*, "I keep [him] company", the only idiomatic completion of *dělám společn…*
- *psánko*, "little letter", a word the writer also uses on HCP 1525 and 1526

A first reading of the R02 opening as KDE was corrected to ZDE. The correction came from comparing the shape against the Z of ZE and ZITRA and the K of DRAHOUSKU and SIMULKA on the same card (work/qg-root-control.png). It did not come from grammar.

## Key

Monoalphabetic substitution with one digraph sign. The labels are conventional names for the handwritten shapes, not exact reproductions. Several pairs are swapped against their look:

- `m` stands for N and `n` for M
- `t` (crossed) stands for D and `d` (looped) for T
- `c` (round) stands for S and `s` (angular) for C
- `b` stands for P and `p` for B

`y` labels the J-shaped sign, `H` the capped r-shape that stands for CH, and `G` the k-shaped sign.

| Shape | Plain | Shape | Plain | Shape | Plain | Shape | Plain |
|---|---|---|---|---|---|---|---|
| 1 | Y | 2 | U | 3 | O | 4 | I |
| 5 | E | 6 | A | y | J | 8 | L |
| b | P | c | S | d | T | f | V |
| g | K | h | R | m | N | n | M |
| p | B | q | Z | r | H | s | C |
| t | D | H | CH | G | G | | |

Czech diacritics are not encoded: the cipher writes base letters only.

Frequency of each sign (221 in all, restored positions included):

| Sign | Count | Sign | Count | Sign | Count | Sign | Count |
|---|---|---|---|---|---|---|---|
| 1 | 4 | 2 | 10 | 3 | 15 | 4 | 14 |
| 5 | 25 | 6 | 17 | 8 | 12 | y | 6 |
| b | 10 | c | 20 | d | 7 | f | 8 |
| g | 4 | h | 10 | m | 12 | n | 9 |
| p | 1 | q | 7 | r | 3 | s | 5 |
| t | 16 | H | 5 | G | 1 | | |

## Plaintext

The transcription uses this notation:

- a plain sign is read from the scan
- `[..]` marks positions where ink is visible but the letters are restored from context
- `(..)` marks a faint trace read with low confidence

```text
R01 bh3n4m, th6r32cg2, q5 t3c2t m53t5c868 yc5n t3b4c. y5cd
R02 qt5 3t cdh5t1 b6m c4n28g6, cf6G[h] n5r3 ph6dh6, y5n2q
R03 f bh6qtm1H Hf484H t586n cb385sm[3cd]. tm5c f5s5hm4n
R04 f86g5n 3ty5t5. q4dh6 3t5c82 bc6mg(3). d4c4s fh581H, t832r1H
R05 b2c cf5 y5t4m5 6m2ms5 q6c486 cd685 fqb3n4m6y4s4 b5b32c.
```

Literal Czech, as decoded:

```text
R01 promin, drahousku, ze dosud neodeslal jsem dopis. jest
R02 zde od stredy pan simulka, svag[r] meho bratra, jemuz
R03 v prazdnych chvilich delam spolecn[ost]. dnes vecernim
R04 vlakem odjede. zitra odeslu psank(o). tisic vrelych, dlouhych
R05 pus sve jedine anunce zasila stale vzpominajici pepous.
```

The ZITRA of R04 is underlined on the card.

Normalized Czech (diacritics, capitals and punctuation are editorial):

**Promiň, drahoušku, že dosud neodeslal jsem dopis. Jest zde od středy pan Simulka, švag[r] mého bratra, jemuž v prázdných chvílích dělám společn[ost]. Dnes večerním vlakem odjede. _Zítra_ odešlu psánk(o). Tisíc vřelých, dlouhých pus své jediné Anunce zasílá stále vzpomínající Pepouš.**

English translation: **Forgive me, darling, for not having sent the letter yet. Since Wednesday Mr Simulka, my brother's brother-in-[law], has been staying here, and I keep him [company] in my idle moments. He leaves by the evening train today. _Tomorrow_ I will send a little letter. A thousand warm, long kisses to his one and only Anunka from her ever-remembering Pepouš.**

Slovak translation: **Prepáč, drahúšik, že som ešte neodoslal list. Od stredy je tu pán Simulka, švag[or] môjho brata, ktorému v prázdnych chvíľach robím spoloč[nosť]. Dnes večerným vlakom odíde. _Zajtra_ odošlem list(ok). Tisíc vrúcnych, dlhých bozkov svojej jedinej Anunke posiela stále spomínajúci Pepouš.**

Notes on the reading:

- **Jest zde od středy** ("has been here since Wednesday"): the card is dated Sunday 29 March 1903, so the visitor had stayed since 25 March.
- **Simulka** is kept without a háček. The cipher marks no diacritics, so a form such as Šimulka would be an editorial guess. The visitor's identity was not researched.
- **Anunce** is the dative of Anunka, a pet form of Anna. **Pepouš** is a pet form of Josef. **pus** is the genitive plural of *pusa*, "kiss". **jest** is the older, formal form of *je*.
- **ZASILA** keeps the cipher's I (*zasílá*, "sends").

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1559/work/decode-final.py
```

The script uses only the Python standard library and writes no files. It does the following:

1. Checks that work/key-final.json is exactly the family key of ciphers/hcp-1520 plus the one family sign `G`.
2. Decodes the manual transcription in work/transcription-final.txt, carrying the `[..]` and `(..)` marks through to the output.
3. Checks the decoded text against the final block in SOLUTION.md.
4. Prints the five literal rows and the line `CHECK: 5 rows; 221 cipher units = 216 read + 1 low-confidence (..) + 4 restored [..]; unknown spans: 0`.

The earlier verifier, work/decode.py, still checks the round-1 partial record with its four unknown spans (214 signs). It is kept for traceability. Neither script reads the image: the transcription step is manual.

## Uncertainties

- **Restored letters.** R in ŠVAGR and OST in SPOLEČNOST are supplied from context. The sign positions are visible, but their shapes cannot be classified. The final O of PSÁNKO is a faint trace. The sense of the letter does not depend on any of them.
- **The cipher G.** The k-shaped sign occurs once here. Its value G rests on four other family cards, not on this card alone.
- **Smudges.** It cannot be decided from the pixels whether the four smudged places are accidental smears or the writer's own wiping. They are read as text, not as cancellations.
- **Identities.** "Simulka", the writer's brother and Pepouš himself are not identified.
- **Editorial choices.** Accents, punctuation and capitals in the normalized Czech are editorial.
- **Key.** The key was transferred from the earlier family cards and the published partial key, not recovered blind from this card. It decodes every legible sign here without change.

## Review summary

The reviewer was Claude Opus 5.5 (Anthropic), in a separate session from the solver. Round 1 gave the verdict **REVISE**.

**What the reviewer checked:**

- It ran the round-1 command.
- It decoded the transcription with its own script and the family key; the result agreed letter for letter.
- It made its own rotated crops and compared all five rows sign by sign; it found no discrepancy in the legible material.
- It confirmed the KDE→ZDE correction.
- It judged the four smudged places on 8–12× crops. It found NEODESLAL and the k-shaped G visible on the scan, R and OST restored from context, and the O of PSÁNKO plausible.
- It concluded that the reading as a whole is correct.

**The five findings and what was done:**

1. **(major) The command did not produce the claimed final text.** A final transcription with the four completions, a key containing the family G, and a new command (work/decode-final.py) were added. The status text in SOLUTION.md was reconciled.
2. **(major) Restorations were not marked.** All versions of the plaintext now bracket švag[r], společn[ost] and psánk(o).
3. **(minor) A háček had been added silently to the name.** The name is now Simulka, with a note.
4. **(minor) The U03 signs were described too confidently.** They are now described as seen but not classified.
5. **(minor) Stale "partial / unknown" wording.** It is superseded by a status note and a final section.

No decoded letter changed as a result of the review. The work was done in this order:

- The first, partial transcription and decipherment (four unknown spans) was made by OpenAI GPT (GPT-6 Astra / GPT-6.1 Sol).
- Claude Opus 5.5 completed the four spans and handed the card to review.
- After the review, Claude Opus 5.5 made the corrections, wrote this report and prepared the register entry.

## Sources

- HC Portal record 1559, General, Description and Attachments tabs, captured 2026-10-28: https://crypto.hcportal.eu/dashboard/cryptograms/1559 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/4737/conversions/pc_hcp_240_pic-large.jpg (source/picture.jpg).
- Address side: https://api.hcportal.eu/media/4738/conversions/pc_hcp_240_adr-large.jpg (source/address.jpg).
- Family key: earlier Anna Tichá family cards in this repository, ciphers/hcp-1520/work/key.json; family G from ciphers/hcp-1541, 1553, 1554 and 1570.
- Maxim Egorov, Anna Tichá postcards, published partial family key: https://maxim-egorov.dev/research/anna-ticha-postcards/
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-29: no entry for this card.
