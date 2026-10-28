# HCP 1533 (pc_hcp_214): a Czech letter of sympathy from Pepouš to Anna Tichá

Human solver: Tomáš Pavuk

**Status: deciphered in full (236 of 236 cipher signs, 240 letters); independent review 1 verdict ACCEPT.** Report dated 2026-10-28.

## Origin and context

The cryptogram is record 1533 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1533), portal name pc_hcp_214, part of the HCPortal collection of cryptographic postcards (private collection). When it was captured on 2026-10-28 the portal listed it as **Not solved**, tagged Postcard, HCPortal collection, category Substitution, date 1903-10-28, language Czech, location Europe, sender Unknown, recipient Anna Tichá, with no transcription or solution attached.

It is an Art Nouveau picture postcard (Meissner & Buch, Leipzig, Künstler-Postkarten series 1228, "Stimmungs-Landschaften"): a landscape in a vase-shaped frame between red poppies and four-leaf clovers. The card is printed sideways; turned upright, the cipher is written in two blocks to the left and right of the lower part of the picture, eleven rows on the left and eight on the right. An arrow after the last left row points up to the right block. Below the right block is the plain date **28./X.1903** (Wednesday, 28 October 1903).

The address side is in plain writing: **Velectěná Slečna / slečna Anna Tichá / učitelka v Žirovnici / u Počátek** ("Honoured Miss Anna Tichá, teacher in Žirovnice near Počátky", South Bohemia). It carries an Austrian 5-heller stamp cancelled PRAHA and an arrival stamp ŽIROVNICE / SEROWITZ whose day is only partly legible. The card thus went from Prague to Žirovnice at the end of October 1903.

The card belongs to a family of cipher postcards to Anna Tichá in the same hand and the same cipher. The sender signs PEPOUSE (Pepouše, genitive of the pet name Pepouš, a diminutive of Josef), as on HCP 1532 and HCP 1535. The key used here was established on the earlier family cards HCP 1520–1527 in this repository, and a partial key for the family was published earlier by Maxim Egorov / Cipher-Atelier (https://maxim-egorov.dev/research/anna-ticha-postcards/). That publication's index did not include pc_hcp_213–215 when checked on 2026-10-28. This card was therefore read with a **known, transferred key**; it is not a new key recovery.

![Picture side as scanned, rotated 90° (source/picture.jpg)](../source/picture.jpg)

![Picture side turned upright; the cipher blocks are left and right of the lower picture, the date 28./X.1903 below the right block (work/upright.png)](../work/upright.png)

![Address side: Anna Tichá, teacher in Žirovnice near Počátky; PRAHA stamp at the top right, arrival stamp ŽIROVNICE / SEROWITZ at the top left (source/address.jpg)](../source/address.jpg)

Other marks on the card, none of them cipher: the printed publisher's line along the left edge of the picture, the HCPortal watermark on both sides, the plain date, the continuation arrow, the address and the postmarks.

## Method

The transcription is **manual**: the solver turned the scan upright (a lossless 90° clockwise rotation), read the nineteen rows sign by sign from enlarged crops, and recorded each row with its pixel box in work/transcription.json. No OCR was used and the portal supplied no transcription. Focused crops of the difficult places (work/C01–C10) are exact enlargements of the original pixels, without contrast or stroke editing.

The signs are a mixture of digit-like shapes (1–8) and Latin-like cursive letters, each standing for one plaintext letter, plus one special sign for the Czech digraph CH. The key of the family cards HCP 1520–1527 decodes every sign of this card into connected Czech, with no unknown or unused sign: 236 cipher signs, four of them CH, giving 240 letters.

In review the reviewer made its own upright frame and enlarged strips, read all nineteen rows independently before comparing, and decoded them with its own script. Its reading agrees with the solver's in all 236 positions.

## Key

Monoalphabetic substitution; the labels are conventional names for the handwritten shapes, not exact reproductions. Note that the shape labelled `m` stands for N and the shape labelled `n` for M.

| Shape | Plain | Shape | Plain | Shape | Plain | Shape | Plain |
|---|---|---|---|---|---|---|---|
| 1 | Y | 2 | U | 3 | O | 4 | I |
| 5 | E | 6 | A | 7 | J | 8 | L |
| b | P | c | S | d | T | f | V |
| g | K | h | R | m | N | n | M |
| p | B | q | Z | r | H | s | C |
| t | D | ř (special sign) | CH | | | | |

`ř` is only a label for the special CH sign (an r-like shape with a tilde- or caron-like stroke above it); it does not mean the Czech letter Ř. Letters F, G, Q, W and X do not occur in the text and have no sign on this card. Czech diacritics are not encoded: the cipher writes base letters only (Š as S, Ř as R, Í as I, and so on).

Frequency of each sign on the card: 1:6, 2:14, 3:12, 4:16, 5:29, 6:16, 7:6, 8:10, b:8, c:15, d:13, f:9, g:9, h:14, m:13, n:10, p:5, q:7, r:1, s:6, t:13, ř:4.

## Plaintext

Ciphertext as transcribed, row by row (A01–A11 left block, B01–B08 right block; punctuation and line-end hyphens as on the card):

```text
A01 fh5832 c32cdh6cd,
A02 t2c4sg3 n375 75t4m6,
A03 f q6hn2dg2, 75mq
A04 m6 d5p5 t385r8.
A05 s4d4n 2bh4nm5
A06 c5 cht5sg5n cf1n.
A07 6fc6g p2t, 6m2mg3,
A08 g84tm6, fqt4d b6m
A09 ph6dh 75 n86t 6 q6-
A10 74cd5 ř3h3p2
A11 f4d5qm5 bh5n2q5.
B01 gt1 bh475t5
B02 c85sm6 t3 q4-
B03 h3fm4s5? d4c4s
B04 fh581ř 2bh4nm1ř
B05 b2c 3t b5b32c5,
B06 gd5h1 f n1c85m-
B07 g6ř cd685 t84 2
B08 d5p5.
```

Literal Czech, as decoded, line for line (base letters only, no accents):

```text
VRELOU SOUSTRAST,
DUSICKO MOJE JEDINA,
V ZARMUTKU, JENZ
NA TEBE DOLEHL.
CITIM UPRIMNE
SE SRDECKEM SVYM.
AVSAK BUD, ANUNKO,
KLIDNA, VZDIT PAN
BRATR JE MLAD A ZA-
JISTE CHOROBU
VITEZNE PREMUZE.
KDY PRIJEDE
SLECNA DO ZI-
ROVNICE? TISIC
VRELYCH UPRIMNYCH
PUS OD PEPOUSE,
KTERY V MYSLEN-
KACH STALE DLI U
TEBE.
```

Normalized Czech (diacritics, capitals and joining of the three split words are editorial; "vždiť" keeps the writer's I):

**Vřelou soustrast, dušičko moje jediná, v zármutku, jenž na tebe dolehl. Cítím upřímně se srdéčkem svým. Avšak buď, Anunko, klidná, vždiť pan bratr je mlád a zajisté chorobu vítězně přemůže. Kdy přijede slečna do Žirovnice? Tisíc vřelých upřímných pus od Pepouše, který v myšlenkách stále dlí u tebe.**

English translation: **Heartfelt sympathy, my one and only darling, in the sorrow that has come upon you. I sincerely feel with my sweetheart. But be calm, Anunka, for your brother is young and will surely overcome the illness. When will the young lady come to Žirovnice? A thousand warm, sincere kisses from Pepouš, who in his thoughts is always with you.**

Slovak translation: **Vrúcnu sústrasť, dušička moja jediná, v zármutku, ktorý na teba doľahol. Úprimne cítim so svojím srdiečkom. Avšak buď, Anunka, pokojná, veď pán brat je mladý a iste chorobu víťazne premôže. Kedy príde slečna do Žirovnice? Tisíc vrúcnych úprimných bozkov od Pepouša, ktorý je v myšlienkach stále pri tebe.**

Notes on the reading:

- **ANUNKO** is the vocative of Anunka, the writer's pet name for Anna. The family card HCP 1535 (same writer, 13 October 1903) has the nominative ANUNKA ("Anunka mi určitě slíbila …"). The third sign is clearly the U-shape 2, the same as in BUD, not the I-shape 4, so the reading is not ANINKO or ANIČKO.
- **VZDIT** really has the I-shape 4, while SVYM two rows above has the Y-shape 1. Standard Czech is "vždyť"; the I is the writer's spelling and is kept in the literal text and in "vždiť".
- "Vřelou soustrast" is an elliptic formula (accusative, with "I express" or "accept" understood). "Soustrast" here is sympathy over the brother's illness, not over a death.
- "Srdéčko" ("little heart") in "Cítím upřímně se srdéčkem svým" is most naturally an endearment for Anna ("I sincerely feel with my sweetheart"); a literal "with my own little heart" is possible.
- "Pan bratr" ("Mr. brother") is a respectful period form for the addressee's brother; "mlád" is the short (predicative) adjective form, ordinary in 1903.
- "Kdy přijede slečna do Žirovnice?" names no one. On HCP 1535 the writer speaks of Anna in the third person; the "slečna" here may be Anna herself, perhaps away with her sick brother, or another young lady. This is not resolved.

## Reproduction

From the repository root:

```sh
python3 ciphers/hcp-1533/work/decode.py
```

The script uses only the Python standard library and writes no files. It checks the SHA-256 hashes of both scans, the metadata and the three record files, decodes the manual transcription in work/transcription.json with the key above, prints the nineteen literal rows, checks all 236 indexed positions in work/positions.csv, and checks that every row re-encodes exactly to its transcription. It does not read the image; the transcription step is manual (and was confirmed independently in review).

## Uncertainties

- The accents, punctuation and word joins of the normalized Czech are editorial. The cipher encodes base letters only. Apart from the stroke that belongs to the special CH sign and the cross-strokes that belong to the D and T shapes, no accent marks above signs could be identified at the resolution of the scan, and none was used to choose the editorial accents; they follow standard Czech orthography.
- The writer's spellings ANUNKO and VZDIT are kept literally; "vždyť" would be the standard form.
- The sender is known only as Pepouš (Josef); his civil identity and his relationship to Anna Tichá beyond what the cards say are not established. The brother and his illness, and the "slečna" who is to come to Žirovnice, are not identified.
- The day on the arrival stamp is only partly legible; the date rests on the plain 28./X.1903 on the card and the portal metadata.
- The over-inked first sign of MYSLEN- (row B06) is read as one M-shaped sign; no cancelled letter is recoverable.
- The key was transferred from the earlier family cards, not recovered blind from this card; it decodes every sign here without change.
- No search for a prior publication of this card was made beyond the portal status (Not solved), the AI Decipherment Register (158 contributions, this card absent) and the index of the Egorov / Cipher-Atelier family page (pc_hcp_213–215 absent), all on 2026-10-28.

## Review summary

Reviewer: Claude Opus 5.5 (Anthropic), round 1, verdict **ACCEPT**. The reviewer ran the reproduction command, made its own upright frame and enlarged strips of the scan, read all nineteen rows independently, decoded them with its own script, and found no difference from the solver's reading in any of the 236 positions. It confirmed ANUNKO and VZDIT as the writer's own spellings, the E of SRDECKEM, the single over-inked sign in MYSLEN-, all four CH signs, and that neither side carries any other cipher text. Its three findings were minor and are reflected here:

- The report now states that no visible mark was used to choose the editorial accents, and which marks above signs do occur (the CH sign's stroke, the cross-strokes of D and T).
- ANUNKO is now supported by the nominative ANUNKA on HCP 1535, as the writer's pet name, rather than described only as an unusual form.
- The solver's status text from before review is superseded by the response to review in SOLUTION.md and by this report.

No change to the decoded letters resulted from the review. The closing steps (response to review, this report, the register entry) were prepared by Claude Opus 5.5 on the solver's behalf at the human's request; the transcription and decipherment were made by the solver, OpenAI GPT (GPT-6 Astra).

## Sources

- HC Portal record 1533, General, Description and Attachments tabs, captured 2026-10-28: https://crypto.hcportal.eu/dashboard/cryptograms/1533 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/4659/conversions/pc_hcp_214_pic-large.jpg (source/picture.jpg).
- Address side: https://api.hcportal.eu/media/4660/conversions/pc_hcp_214_adr-large.jpg (source/address.jpg).
- Family key: this repository, ciphers/hcp-1520 to hcp-1527 (key copied from HCP 1527); related family cards HCP 1532 and HCP 1535.
- Maxim Egorov / Cipher-Atelier, Anna Tichá postcards, published partial family key: https://maxim-egorov.dev/research/anna-ticha-postcards/
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-28.
