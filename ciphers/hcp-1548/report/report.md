# HCP 1548 (pc_hcp_229): a Czech cipher postcard to Anna Tichá, 6 July 1903

Human solver: Tomáš Pavuk

**Status: deciphered in full: 296 of 296 cipher signs, 297 letters.**

- Two signs lie under a printed flower stem and are recorded as a restoration.
- Independent review 1 gave the verdict REVISE. The reading did not change; the records were corrected.
- Report dated 2026-10-29.

## Origin and context

The cryptogram is record 1548 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1548), portal name pc_hcp_229. It belongs to the HCPortal collection of cryptographic postcards, held in a private collection. When it was captured on 2026-10-28, the portal listed:

- status **Not solved**;
- tags Postcard, HCPortal collection; category Substitution;
- date 1903-07-06; language Czech;
- sender Unknown; recipient Anna Tichá;
- no transcription or solution attached.

It is a picture postcard showing a bouquet of forget-me-nots tied with a white bow, with long green stems hanging down. Below the bouquet, nine rows of cipher run across the card, and the stems cross them. The text ends with the underlined sign `b` (P, the writer's initial), followed in plain writing by the date **6./VII. 1903.** The card was scanned sideways; the figure below shows it turned upright (a lossless 270° rotation).

The address side is in plain writing: **Velectěná Slečna / slečna Anna Tichá / učitelka v / Žirovnici / u Počátek.** ("Honoured Miss Anna Tichá, teacher in Žirovnice near Počátky", South Bohemia). It also carries:

- an Austrian 5-heller stamp;
- Prague and Žirovnice postmarks;
- the printed publisher's line C.H. Odemar, Magdeburg, 1215.

There is no cipher on the address side.

The card belongs to a large family of cipher postcards to Anna Tichá, in the same hand and the same cipher. Several are signed in full "Pepouš" (a pet form of Josef), for example HCP 1556. Many are deciphered in this repository (HCP 1520–1556). Maxim Egorov published a partial key for the family earlier (https://maxim-egorov.dev/research/anna-ticha-postcards/). This card was read with that **known, transferred key**; it is not a new key recovery. No earlier reading of this particular card was found or used.

![Picture side turned upright: forget-me-nots, nine cipher rows below, the signature b and the date 6./VII. 1903 (work/upright.png)](../work/upright.png)

![Address side: Anna Tichá, teacher in Žirovnice near Počátky (source/address.jpg)](../source/address.jpg)

## Method

**Transcription.** The transcription is manual. No OCR was used, and the portal supplied no transcription. The solver read the nine rows (R01–R09) sign by sign from enlarged per-row crops (work/R01.png to R09.png). The records are:

- work/transcription.json – each row with its crop box;
- work/positions.csv – each sign with its row and index.

**Difficult places.** These were checked against other occurrences of the same shapes on the card:

- the K/Z pair: a first reading JIK was corrected to JIZ (work/q-g-controls.png);
- r versus barred r, i.e. H versus CH (work/h-ch-initial-controls.png);
- the signs crossed by the green stem (work/stem.png).

**Decoding.** The signs are a mix of digit-like and cursive Latin-like shapes. Each stands for one plaintext letter, and one special sign stands for the digraph CH. The family key, used unchanged, decodes every sign of this card into connected Czech.

**The hidden span in row 2.** In row 2, a short stretch after N and before STALE lies under the darkest part of the green stem. The first handover, by an OpenAI GPT solver, left it as a span of unknown length. On 8× enlargements:

- after the `m` (N) there is a small dark sign with a short hooked top, consistent with a small `5` (E) as in `m5` elsewhere on the card;
- then a clearly visible `2` (U);
- then `cd685` (STALE).

There is room for exactly these two signs. The word is **neustále**, "constantly". The U is read from the ink. The E is only partly visible, but it is also the only letter that makes a word. The pair is therefore recorded as a restoration.

![R02 under the stem, enlarged: m, a faint small sign, a 2, then cd6… (work/claude/neustale.png)](../work/claude/neustale.png)

## Key

The cipher is a monoalphabetic substitution. The labels are conventional names for the handwritten shapes. Note these pairs:

- `m` = N and `n` = M;
- `d` (looped) = T and `t` (crossed) = D;
- `c` (round) = S and `s` (angular) = C;
- `b` = P and `p` = B.

`ř` labels an r-shape with a separate bar or cap, which stands for CH.

| Shape | Plain | Shape | Plain | Shape | Plain | Shape | Plain |
|---|---|---|---|---|---|---|---|
| 1 | Y | 2 | U | 3 | O | 4 | I |
| 5 | E | 6 | A | 7 | J | 8 | L |
| b | P | c | S | d | T | f | V |
| g | K | h | R | m | N | n | M |
| p | B | q | Z | r | H | s | C |
| t | D | ř | CH | | | | |

Czech diacritics are not encoded; the cipher writes base letters only. The family key also has signs for F and G, which do not occur on this card.

Frequency of each sign on the card (296 in all): 1:9, 2:8, 3:23, 4:19, 5:27, 6:31, 7:7, 8:13, b:8, c:25, d:18, f:17, g:7, h:12, m:20, n:14, p:5, q:10, r:9, s:4, t:9, ř:1.

## Plaintext

Ciphertext as transcribed, row by row. The restored pair is the `52` after `m` in R02.

```text
R01 d4c4s5h1 t4g q6 3p6 th6r5 84cdg1 6 q6 fqb3-
R02 n4mg2. 76 fqb3n4m68 m52cd685. 74q c5 n5
R03 cht5sg3 m5rm5f6? - 3 c86fm3cd4 7c5n d5md3-
R04 gh6d5 m5n58 qt5 q6tm5 m6fcd5f1. p18 7c5n
R05 c5 t4f6d m6 bh2f3t 4 m6 f86cdm4 c86fm3cd
R06 m6 cd6h3n5cdcg5n m6n5cd4. fc3p3d2 p18 7c5n
R07 m6 bh3n3s4 ph6dh6 3m3r3 qm6n5r3 n5r3 g3n4c6h5
R08 q 74r86f1. d4c4s fh581r b3qth6f2 6 t832r1r f6cm4-
R09 f1ř b2c b3c486 df27 b.
```

Literal Czech as decoded, line for line. Base letters only, without accents; the plain date 6./VII. 1903 follows.

```text
R01 TISICERY DIK ZA OBA DRAHE LISTKY A ZA VZPO-
R02 MINKU. JA VZPOMINAL NEUSTALE. JIZ SE ME
R03 SRDECKO NEHNEVA? - O SLAVNOSTI JSEM TENTO-
R04 KRATE NEMEL ZDE ZADNE NAVSTEVY. BYL JSEM
R05 SE DIVAT NA PRUVOD I NA VLASTNI SLAVNOST
R06 NA STAROMESTSKEM NAMESTI. VSOBOTU BYL JSEM
R07 NA PROMOCI BRATRA ONOHO ZNAMEHO MEHO KOMISARE
R08 Z JIHLAVY. TISIC VRELYH POZDRAVU A DLOUHYH VASNI-
R09 VYCH PUS POSILA TVUJ P.
```

Normalized Czech. Diacritics, punctuation and word division are editorial. So is the CH in *vřelých, dlouhých*; the card has VRELYH and DLOUHYH.

**Tisícerý dík za oba drahé lístky a za vzpomínku. Já vzpomínal neustále. Již se mé srdéčko nehněvá? – O slavnosti jsem tentokráte neměl zde žádné návštěvy. Byl jsem se dívat na průvod i na vlastní slavnost na Staroměstském náměstí. V sobotu byl jsem na promoci bratra onoho známého mého komisaře z Jihlavy. Tisíc vřelých pozdravů a dlouhých vášnivých pus posílá tvůj P[epouš?].**

English translation: **A thousand thanks for both dear cards and for remembering me. I have been thinking of you constantly. Is my little heart no longer angry? – This time I had no visitors here for the celebration. I went to watch the procession and the celebration itself on Old Town Square. On Saturday I was at the graduation of the brother of that commissioner from Jihlava whom I know. A thousand warm greetings and long passionate kisses are sent by your P.**

Slovak translation: **Tisícoraká vďaka za oba drahé lístky a za spomienku. Ja som spomínal neustále. Už sa moje srdiečko nehnevá? – Počas slávnosti som tentoraz nemal žiadne návštevy. Bol som sa pozrieť na sprievod aj na samotnú slávnosť na Staromestskom námestí. V sobotu som bol na promócii brata toho môjho známeho komisára z Jihlavy. Tisíc vrúcnych pozdravov a dlhých vášnivých bozkov posiela tvoj P.**

Notes on the reading:

- **VRELYH, DLOUHYH.** Both words end with a plain r-shape (H) without a bar. Compare the barred `ř` (CH) that opens R09 and completes VASNIVYCH. The writer left out the bar twice. The literal text keeps H; the normalized text reads *vřelých, dlouhých*.
- **VSOBOTU** is *v sobotu*, "on Saturday", written as one word. 6 July 1903 was a Monday, so this Saturday was 4 July.
- **srdéčko** ("little heart") is a term of endearment for the addressee, as on other family cards. **pus** is the genitive plural of *pusa*, "kiss".
- **promoce** is a university graduation ceremony. **komisař** ("commissioner") is an official title. Neither person is named.
- **Slavnost na Staroměstském náměstí.** A celebration on Old Town Square in Prague around 6 July fits the yearly commemoration of Jan Hus (6 July). This is context only; it was not used to read any sign.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1548/work/decode.py
```

The script uses only the Python standard library and writes no files. It:

- checks the SHA-256 hashes of both scans, the metadata, the record files and the credited reference files;
- decodes the manual transcription in work/transcription.json with the key in work/key.json;
- checks all 296 indexed positions in work/positions.csv;
- re-encodes every plaintext row with the fixed key and compares it with the transcribed cipher row;
- checks that exactly two units, R02 positions 18–19, are flagged as restored;
- prints the nine literal rows above.

It does not read the image, since the transcription step is manual. It verifies files in batches/easy-2026-10-28/, so it runs only in a checkout that contains them.

## Uncertainties

- **NEUSTÁLE (R02, signs 18–19).** This pair is a restoration under the printed stem: the U is visible and the E partly visible. The scan is only 1024×674 pixels. A sharper image of the original would settle the pair.
- **Two missing CH bars** in VRELYH and DLOUHYH. These are a writer's omission; the literal text keeps H.
- **Signs crossed by the stem** in DRAHE (R01), SLAVNOSTI (R03) and NAVSTEVY (R04). Their strokes are still readable, and both solver and reviewer checked them.
- **The signature** is the single letter P. The expansion to Pepouš rests on the family of cards, not on this card. The civil identities of the writer, the brother and the commissioner from Jihlava are not established.
- **Editorial choices.** The accents, punctuation and word joins of the normalized Czech are editorial.
- **The key** was transferred from the earlier family cards and the published partial key, not recovered blind from this card. It decodes every sign here without change.
- **Prior publication.** The search was limited to three places: the portal status (Not solved), the AI Decipherment Register (no entry for this card on 2026-10-29), and the Cipher-Atelier Anna Tichá readings (card 229 absent).

## Review summary

Reviewer: a separate Claude Opus 5.5 agent (Anthropic), round 1, verdict **REVISE**. The reviewer:

- ran the reproduction command;
- checked that the key is identical to the family key;
- read all nine rows against the scan, including its own 3× and 8× crops, and found agreement row by row;
- decoded the transcription with its own script, with the same result: 296 units, no unmapped sign, the same plaintext;
- accepted the NEUSTALE restoration on its own red-channel enlargement.

Its findings and what changed:

1. **Records out of date (major).** At handover, the reproduction command and record files still showed the hidden span as unknown (N⟦U1⟧STALE). The transcription now carries the restored pair `5 2`, flagged as restored. All record files were regenerated, and the command now prints NEUSTALE and asserts 296 units.
2. **Self-contradictory SOLUTION.md (major).** It mixed the earlier "partial" statement with the completion. It was rewritten as one current statement, with the history kept separately.
3. **Signature expansion (minor).** "P[epouš]" was presented as read. It is now marked as a family inference.
4. **VRELYH/DLOUHYH (minor).** These are now stated plainly as a writer's omission.
5. **Partly visible E (minor).** The E is now described as partly visible rather than purely inferred.

No decoded letter changed as a result of the review.

Who did what:

- **OpenAI GPT (GPT-6 Astra):** source capture, manual transcription, key transfer and the first, partial reading.
- **Claude Opus 5.5:** restoration of the hidden span, the revision after review, and this report.
- **A separate Claude Opus 5.5 agent:** the independent review.

## Sources

- HC Portal record 1548, General, Description and Attachments tabs, captured 2026-10-28: https://crypto.hcportal.eu/dashboard/cryptograms/1548 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/4704/conversions/pc_hcp_229_pic-large.jpg (source/picture.jpg).
- Address side: https://api.hcportal.eu/media/4705/conversions/pc_hcp_229_adr-large.jpg (source/address.jpg).
- Family key: earlier Anna Tichá family cards in this repository, e.g. ciphers/hcp-1545/work/key.json.
- Maxim Egorov, Anna Tichá postcards, published partial family key: https://maxim-egorov.dev/research/anna-ticha-postcards/
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-29.
