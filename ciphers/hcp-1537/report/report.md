# HCP 1537 (pc_hcp_218): a Czech love note from Pepouš to Anna Tichá

Human solver: Tomáš Pavuk

**Status: deciphered in full (289 of 289 cipher signs); independent review 1 verdict ACCEPT, with one literal correction (OPED, a writer's slip for OPĚT).** Report dated 2026-10-28.

## Origin and context

The cryptogram is record 1537 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1537), portal name pc_hcp_218, part of the HCPortal collection of cryptographic postcards (private collection). When it was captured on 2026-10-28 the portal listed it as **Not solved**, tagged Postcard, HCPortal collection, category Substitution, date 1903-09-17, language Czech, location Europe, sender Unknown, recipient Anna Tichá, with no transcription or solution attached.

It is a picture postcard of the "Flora-Serie II No. 17" (an original nature photograph in Photochrom by Theodor Eismann, Leipzig): a bunch of pink and yellow roses with a peacock butterfly. The card is scanned sideways; turned upright (90° clockwise), the cipher is written in thirteen rows to the right of and below the roses. The last three rows run the full width of the card under the plain date **17/IX 1903.** (Thursday, 17 September 1903), which stands at the left.

The address side is in plain writing: **Velectěná Slečna / slečna Anna Tichá. / učitelka v / Žirovnici / u Počátek.** ("Honoured Miss Anna Tichá, teacher in Žirovnice near Počátky", South Bohemia). It carries an Austrian 5-heller stamp with a cancellation at the top right whose place name is only partly legible, and a stamp ŽIROVNICE / SEROWITZ whose day and month are only partly legible (year 03).

The card belongs to a family of cipher postcards to Anna Tichá in the same hand and the same cipher, signed by "Pepouš" (a pet form of Josef), several of which are deciphered in this repository (for example HCP 1520–1527, 1533, 1535, 1542 and 1544). The key used here was transferred from those earlier family cards, and a partial key for the family was published earlier by Maxim Egorov (https://maxim-egorov.dev/research/anna-ticha-postcards/), and the shallow-v sign for F is corroborated by the published card pc_hcp_199 (HCP 1518), whose proposed reading RUDOLFINA uses it. That publication's index did not include pc_hcp_216–218 when checked on 2026-10-28. This card was therefore read with a **known, transferred key**; it is not a new key recovery.

![Picture side as scanned, rotated 90° (source/picture.jpg)](../source/picture.jpg)

![Picture side turned upright: thirteen cipher rows right of and below the roses, the plain date 17/IX 1903 at the left (work/upright.png)](../work/upright.png)

![Address side: Anna Tichá, teacher in Žirovnice near Počátky; stamp and cancellation at the top right, ŽIROVNICE / SEROWITZ stamp beside it (source/address.jpg)](../source/address.jpg)

Other marks on the card, none of them cipher: the printed publisher's line along the left edge of the picture, the series line "Flora-Serie II No. 17" at the bottom left, the HCPortal watermark on both sides, the plain date, the address, the stamp and the postmarks.

## Method

The transcription is **manual**: the solver turned the scan upright, read the thirteen rows sign by sign from enlarged per-row crops (work/row-01.png to row-13.png), and recorded each row with its crop box in work/manual-records.json and each of the 289 signs with its index in work/indexed-transcription.tsv. No OCR was used and the portal supplied no transcription. The difficult places were checked against other occurrences of the same shapes on the same card (work/controls.md and the work/detail-*.png crops). Two quick first readings were wrong and were corrected on the enlargements before handover: FAMILCE (really VAMBERCE) and BRZY (really BRZKY, five signs).

The signs are a mixture of digit-like shapes and Latin-like cursive letters, each standing for one plaintext letter. The family key decodes every sign of this card into connected Czech, with no unknown or unused sign.

In review the reviewer made its own upright frame and 4–5× crops, read all thirteen rows independently before comparing, and decoded them with its own script. Its reading agrees with the solver's in 288 of the 289 positions. The one difference is the last sign of OPET in row 13, which on the card is the D-shape, not the T-shape (see Plaintext and Review summary). The reading given in this report includes that correction.

## Key

Monoalphabetic substitution; the labels are conventional names for the handwritten shapes, not exact reproductions. Note that the shape labelled `m` stands for N and the shape labelled `n` for M, and that the shape labelled `t` stands for D and the shape labelled `d` for T. `y` labels the J-shaped sign (labelled `7` in some other family records) and `F` the shallow v-shaped sign, distinct from the tall looped `f` (V).

| Shape | Plain | Shape | Plain | Shape | Plain | Shape | Plain |
|---|---|---|---|---|---|---|---|
| 1 | Y | 2 | U | 3 | O | 4 | I |
| 5 | E | 6 | A | y | J | 8 | L |
| b | P | c | S | d | T | f | V |
| g | K | h | R | m | N | n | M |
| p | B | q | Z | r | H | s | C |
| t | D | F | F | | | | |

The family key also has a special sign for the digraph CH; it does not occur on this card. Letters G, Q, W and X do not occur in the text and have no sign here. Czech diacritics are not encoded: the cipher writes base letters only (Č as C, Ř as R, Í as I, and so on).

Frequency of each sign on the card (289 in all, after the OPED correction): 1:7, 2:8, 3:21, 4:30, 5:33, 6:20, y:9, 8:14, b:11, c:20, d:12, f:10, g:14, h:12, m:23, n:7, p:2, q:8, r:4, s:10, t:13, F:1.

## Plaintext

Ciphertext as transcribed, row by row (punctuation and line-end hyphens as on the card; row 13 with the review correction `3b5t`):

```text
01 cht5sm1 t4g q6 th6r1
02 84cd5g. n1c848 yc5n
03 y4q, q5 yc4 2b8m5
04 m6 nm5 q6b3nm586.
05 gt1 q6s4m684 ycd5
06 m3f1 cg38m4 h3g?
07 f g86cd5h5 q6s4m68 h3g 6c4
08 tm5c. m5bh4yt5-84 m4s m53s5-
09 g6f6m5r3 t3 d3r3, b3y5t2 6c4 g3m-
10 s5n bh4cd4r3 d1tm5 m6 t3f385m32.
11 2s4mg3f6m4 bh4 f5s4hg2 f5 f6np5hs5 yc5n
12 y4q t5F4m4d4fm5 3th5g8. d4c4s b2c b3c486
13 d4 df2y b5b32c 6 d5c4 c5 3b5t m6 phqg1 84cd5g.
```

Literal Czech, as decoded, line for line (base letters only, no accents):

```text
SRDECNY DIK ZA DRAHY
LISTEK. MYSLIL JSEM
JIZ, ZE JSI UPLNE
NA MNE ZAPOMNELA.
KDY ZACINALI JSTE
NOVY SKOLNI ROK?
V KLASTERE ZACINAL ROK ASI
DNES. NEPRIJDE-LI NIC NEOCE-
KAVANEHO DO TOHO, POJEDU ASI KON-
CEM PRISTIHO TYDNE NA DOVOLENOU.
UCINKOVANI PRI VECIRKU VE VAMBERCE JSEM
JIZ DEFINITIVNE ODREKL. TISIC PUS POSILA
TI TVUJ PEPOUS A TESI SE OPED NA BRZKY LISTEK.
```

Normalized Czech (diacritics, capitals and joining of the two split words are editorial; *opět* is an editorial correction of the card's OPED; MYSLIL and VAMBERCE are kept as written):

**Srdečný dík za drahý lístek. Myslil jsem již, že jsi úplně na mne zapomněla. Kdy začínali jste nový školní rok? V klášteře začínal rok asi dnes. Nepřijde-li nic neočekávaného do toho, pojedu asi koncem příštího týdne na dovolenou. Účinkování při večírku ve Vamberce jsem již definitivně odřekl. Tisíc pus posílá ti tvůj Pepouš a těší se opět na brzký lístek.**

English translation: **Heartfelt thanks for your dear card. I was already thinking that you had completely forgotten me. When did you start the new school year? In the monastery the year began, I think, today. If nothing unexpected gets in the way, I shall probably go on leave at the end of next week. I have now definitively declined to perform at the evening party in Vamberk. A thousand kisses are sent to you by your Pepouš, who again looks forward to an early card.**

Slovak translation: **Srdečná vďaka za drahý lístok. Myslel som si už, že si na mňa úplne zabudla. Kedy ste začínali nový školský rok? V kláštore sa rok začínal asi dnes. Ak do toho nepríde nič neočakávané, pôjdem asi koncom budúceho týždňa na dovolenku. Účinkovanie na večierku vo Vamberku som už definitívne odmietol. Tisíc bozkov ti posiela tvoj Pepouš a opäť sa teší na skorý lístok.**

Notes on the reading:

- **OPED / opět.** The last sign of this word is the t-shape (D), the same shape as in DO (row 9), and not the left-bowl d-shape (T) of TOHO, TI, TVUJ and TESI. The card therefore literally reads OPED; the intended word is clearly *opět* ("again"). A plausible cause: the cipher gives the t-shape to D and the d-shape to T, so writing the t-shape for T is an easy slip, and in Czech a word-final D and T sound the same. The solver first recorded this sign as T without a note; the reviewer found it on the scan.
- **VAMBERCE.** *Ve Vamberce* is the older Czech locative of **Vamberk**, a town in East Bohemia (district Rychnov nad Kněžnou), formed like Žamberk → *v Žamberce*. The literal and normalized Czech keep the writer's form; the translations give the town's name. That this is the place meant is an inference from the form.
- **MYSLIL** ("I thought") is a common period and colloquial variant of standard *myslel*; it is kept.
- **Kdy začínali jste nový školní rok?** fits the recipient, a schoolteacher, and the date in mid-September. *V klášteře* ("in the monastery" or "in the convent") is not explained on the card; it may be the writer's own place of study or work.
- **Účinkování při večírku**: "performing (taking part) at an evening party or soirée", for example as a musician or actor.
- **Pepouš** is the nominative of the pet name (Josef); on other family cards the writer signs in the genitive PEPOUSE ("from Pepouš").

## Reproduction

From the repository root:

```sh
python3 ciphers/hcp-1537/work/decode.py
```

The script uses only the Python standard library and writes no files unless run with `--write-derived` (which regenerates the crops and derived displays). It checks the SHA-256 hashes of both scans and the metadata, the record files and the credited reference files, decodes the manual transcription in work/manual-records.json with the key in work/key.json, prints the thirteen literal rows, checks all 289 indexed positions in work/indexed-transcription.tsv against the records, and checks that every row re-encodes exactly to its transcription. It does not read the image; the transcription step is manual and was confirmed independently in review. SOLUTION.md names a machine-specific Python under ~/.cache/codex-runtimes; plain `python3` gives the same result.

Important: the files in work/ were left as they were at handover, so the script still prints `opet` in row 13 (from the record `3b5d`). The corrected literal reading `oped` (record `3b5t`) given in this report comes from the review and is documented in the response to review in SOLUTION.md.

## Uncertainties

- **One writer's slip.** The card has OPED (the D-shape) where *opět* is meant; one sign of 289. The cipher text is otherwise consistent, but not flawless.
- **Close calls, all checked on the scan by both solver and reviewer:** the angular 4 (I) and not the upright 1 (Y) in PRI and PRISTIHO; the eight signs of VAMBERCE, with the descending p-shape (B) and the tall h-shape (R); the five signs of BRZKY, with the open-hooked q (Z) followed by the closed-loop g (K); the single shallow-v F in DEFINITIVNE against the looped f (V) of the same word. The q/g (Z/K) distinction holds on every occurrence on the card.
- The solver's first quick readings FAMILCE and BRZY, and a t/d label slip while typing TVUJ, were corrected before handover; they are recorded in work/controls.md.
- The accents, punctuation and word joins of the normalized Czech are editorial. The cipher encodes base letters only; the accents follow standard Czech orthography.
- VAMBERCE as Vamberk is an inference from the regular older locative form; the card does not name the place otherwise.
- The sender is known only as Pepouš (Josef); his civil identity, and what the *klášter* is, are not established.
- The day and month on the ŽIROVNICE / SEROWITZ stamp and the place on the stamp's cancellation are only partly legible; the date rests on the plain 17/IX 1903 on the card and the portal metadata.
- The key was transferred from the earlier family cards and the published partial key, not recovered blind from this card; it decodes every sign here without change.
- No search for a prior publication of this card was made beyond the portal status (Not solved), the AI Decipherment Register (snapshot of 173 contributions, this card absent) and the index of the Egorov family page (pc_hcp_216–218 absent), all on 2026-10-28.

## Review summary

Reviewer: Claude Opus 5.5 (Anthropic), round 1, verdict **ACCEPT**. The reviewer ran the reproduction command (output identical to the solver's literal plaintext file), decoded the solver's cipher rows with its own independent table (identical result), made its own upright crops of the scan, and read all thirteen rows itself before comparing. Its reading agreed with the solver's in all positions but one, and it confirmed VAMBERCE, BRZKY, PRI/PRISTIHO, the F of DEFINITIVNE, the Z/K split, and that neither side carries any other cipher text. Its four findings were minor and are reflected here:

- **OPET is OPED on the card.** The last sign is the D-shape. The literal reading in this report is now OPED, and *opět* is marked as an editorial correction of a writer's slip. This is the only change to the decoded letters; the meaning is unchanged.
- **Uncertainties named.** The uncertainty section now lists the writer's slip and the close calls by name.
- **Vamberk.** VAMBERCE is identified, as an inference, as the older locative of the East Bohemian town Vamberk.
- **Portable command.** The reproduction command is given with plain `python3`.

The closing steps (response to review, this report, the register entry) were prepared by Claude Opus 5.5 on the solver's behalf at the human's request; the transcription and decipherment were made by the solver, OpenAI GPT (GPT-6 Astra).

## Sources

- HC Portal record 1537, General, Description and Attachments tabs, captured 2026-10-28: https://crypto.hcportal.eu/dashboard/cryptograms/1537 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/4671/conversions/pc_hcp_218_pic-large.jpg (source/picture.jpg).
- Address side: https://api.hcportal.eu/media/4672/conversions/pc_hcp_218_adr-large.jpg (source/address.jpg).
- Family key: earlier Anna Tichá family cards in this repository (for example ciphers/hcp-1520 to hcp-1527).
- Maxim Egorov, Anna Tichá postcards, published partial family key: https://maxim-egorov.dev/research/anna-ticha-postcards/
- Shape reference for F: pc_hcp_199 picture side, https://api.hcportal.eu/media/4614/pc_hcp_199_pic.JPG (archived in batches/easy-2026-10-28/public-reference-199/).
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-28.
