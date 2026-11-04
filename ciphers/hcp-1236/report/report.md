# HCP 1236 (cpc_1912--22_HU__HU_Jasz Arokszalas_jolanka-102): Feri to Jolánka Tóth

Human solver: Tomáš Pavuk

**Status: deciphered in full (18 rows, 295 written signs); independent review 1 verdict REVISE, all six findings addressed. One letter value changed.** Report dated 2026-11-02.

## Origin and context

The cryptogram is record 1236 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1236), part of Tobias Schrödel's collection of cryptographic postcards (private collection). When captured on 2026-11-02 the portal listed it as **Not solved**, tagged Postcard, T. Schrödel Collection, category Substitution, language Unknown, sender Unknown, recipient Tóth Jolánka, with no transcription or solution attached. I found no published solution.

The picture side carries the printed verse "Sorrentói ábránd", a six-line sentimental poem beginning "Ez a levél az utolsó, amit hozzád irok". It has no handwriting and is not part of the message.

The address side, in pink ink, has the cipher message in 18 rows on the left and a plain address on the right: **Szeretett Tóth Jolánka kisasszonynak, Jász Árokszállás** ("To the beloved Miss Jolánka Tóth, Jászárokszállás"). The stamp has been removed, and on the bare patch stands a plain note: **csokolja tavolba szamtalanszor Feri** ("Feri kisses you from afar countless times"). This is a hidden stamp-box message: the right postmark's ring stops at the edge of the stamp patch, so the stamp covered the note when the card was posted. It is plain Hungarian (no cipher signs), and every letter is legible.

The date 1912 and day 22 come from the portal file name. The left postmark, rotated and contrast-stretched, agrees with a year ending in 912 and a day beginning with 2, but the month cannot be read. The pencil "18" at the top right is a collector's or later mark.

The card belongs to the "Jolánka" family of Hungarian cipher postcards to Tóth Jolánka, deciphered in this repository as HCP 1212, 1213, 1216, 1217, 1218, 1243 and 1301. The name Feri also signs HCP 1216 and the closing formula is the same, but this report claims no more than that.

![Address side: 18 cipher rows, plain address, plain note on the stamp patch (source/address-large.jpg)](../source/address-large.jpg)

![Picture side with the printed verse (source/picture-large.jpg)](../source/picture-large.jpg)

## Method

The transcription is **manual**, not OCR: each row was read sign by sign from enlarged crops of the high-resolution original of the address side and recorded in a ledger (work/ledger.txt). The rows slope upward by up to about 3.7 degrees, so rows 3–8 had to be read from taller crops. The reading was not blind in the later rows, because word sense was used to test doubtful signs; those calls are listed under Uncertainties.

This is a **known, transferred key**, not a new key recovery. The family key of HCP 1216 fits unchanged, and no new sign was needed.

## Key

**Cipher type: MASC + Steganography** (updated 2026-11-03). The message body is a simple monoalphabetic substitution with invented graphic signs; a plain Hungarian note was hidden in the stamp box under the stamp. The labels are descriptions of handwritten shapes.

| Sign | Letter | Sign | Letter | Sign | Letter |
|---|---|---|---|---|---|
| two bars | a | section mark (dot below) | k | F-like | r |
| six | b | wave | l | bowl, either facing | s |
| short + long stroke | d | three short strokes | m | gamma/corner | t |
| three bars | e | two short strokes | n | plain cross x | u |
| cross, high bar, long descender | f | cursive loop | o | chevron | v |
| open loop with descender | g | long + short stroke | h / p | crossed diagonal | z |
| dotted crossed curve | i | joined loop + descender | gy | opposed bowls | cs |
| low bar, short stub below | j | | | | |

Accents are separate ticks above the sign (two bars + tick = á, two ticks over the loop = ö/ő). The cipher has one sign for h and p, so these are told apart by word sense. Letters c and y do not occur alone on this card.

The f and j signs differ only in where the bar sits, and this mattered in row 2:

![f and j compared, reviewer crops: the first panel is row 2 with the low bar and pale upper stem; the last panels show the high bar and long descender of f (review/work/fj_compare.png)](../review/work/fj_compare.png)

## Plaintext

Literal decipherment by written row (h stands for the h/p sign; punctuation is left out):

```text
01 szeretettédesjolan          10 edesemhogyérzi
02 kámkivánomhogylegjobb       11 magátgoadoleneha
03 kedvebentaláljasora         12 atavolbanönert
04 imhogymulatottafar          13 ehedöszivtulajdo
05 sangbaamiengemill           14 nossaraéncsakakkor
06 lethetfötátdolgoz           15 vagyokigazánbol
07 tamkeddenhedigelmen         16 dogdaaszéhszemébe
08 temazegyletbeahol           17 nézhetekistenveleaviszoat
09 szineöadasvolt              18 latasra
```

**Hungarian (normalized):** Szeretett édes Jolánkám! Kívánom, hogy legjobb kedvében találja soraim. Hogy mulatott a farsangba[n], a mi engem illet, hétfőt átdolgoztam, kedden pedig elmentem az egyletbe, ahol színe[l]őadás volt. Édesem, hogy érzi magát? Gondol-e néha a távolban önért epedő szív tulajdonosára? Én csak akkor vagyok igazán boldog, ha a szép szemébe nézhetek. Isten vele, a viszontlátásra.

Plain stamp-box message (hidden under the stamp): Csókolja távolba számtalanszor Feri.

**English:** My beloved sweet Jolánka! I wish that my lines may find you in the best of spirits. How did you enjoy yourself at the carnival? As for me, I worked all through Monday, and on Tuesday I went to the club, where there was a theatrical performance. My darling, how are you feeling? Do you sometimes think of the owner of the heart that pines for you in the distance? I am truly happy only when I can look into your beautiful eyes. Farewell, until we meet again.

Stamp box: Feri kisses you from afar countless times.

**Slovak:** Moja milovaná, sladká Jolánka! Želám si, aby Vás moje riadky zastihli v najlepšej nálade. Ako ste sa zabavili na fašiangoch? Čo sa mňa týka, celý pondelok som pracoval a v utorok som išiel do spolku, kde bolo divadelné predstavenie. Drahá moja, ako sa cítite? Myslíte niekedy na majiteľa srdca, ktoré za Vami v diaľke túži? Ja som naozaj šťastný len vtedy, keď sa môžem pozerať do Vašich krásnych očí. S Bohom, dovidenia.

V poli pre známku: Bozkáva Vás z diaľky nespočetnekrát Feri.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1236/work/decode.py
```

It checks the SHA-256 of both scans and both high-resolution originals, decodes work/ledger.txt with the key, and prints the literal rows and the normalized text.

## Uncertainties

None of these changes the sense.

**Calls that rest on word sense**

- **Written a for n, twice.** Row 11 "goadol" and row 17 "viszoat" have clear horizontal two bars where "gondol" and "viszont" need n. Read as slips: a and n differ only in stroke direction.
- **Row 16, "ha" written with d.** The sign has the d shape. Literal "da a szép".
- **Row 13, "szív tulajdonosára".** After "szí" stands one merged sign, read as v and t sharing a stroke. If it is t alone, the v of "szív" was omitted; the reading is the same.
- **Row 17, i of "Isten".** A heavy sign with no visible dot. Only "Isten vele" fits, and it closes HCP 1216 too.
- **Row 9, "színe[l]őadás".** Literal "szineöadas"; the l is not on the card.
- **k without its dot, twice.** The first k of "csak" (row 14) and the k of "nézhetek" (row 17). Both are forced by the word.
- **h/p.** p in "pedig", "epedő", "szép"; h in "hogy", "hétfőt", "ahol", "néha", "nézhetek". d and n do not collide on this card.

**Condition of the card**

- Row 2: the j has a pale upper stem where the pen ran dry.
- Row 8: the a of "az" is re-inked thickly; what lies under it cannot be seen, but no other reading competes.
- Rows 10, 11, 14: overwritten or blotted gy, t and o, all legible.
- Row 18: the last a is slightly clipped at the card edge. Row 17 runs over the printer's logo, and no sign is lost.

**Spelling and normalization**

- "farsangba[n]" has no final n on the card (colloquial form).
- "illet" is written "ill-let" across rows 5–6, and "tulajdonosára" has two s signs.
- "hétfőt átdolgoztam": the card has one continuous run; the word division is editorial.
- Accents are marked only where seen, others are supplied in normalization, and ticks between rows may belong to either row.
- Punctuation is not in the ledger: hyphens after "Jolán-" and "sora-", full stops after "soraim" and "volt", and a comma stroke after "farsangba".
- Address line 4 looks like "Jósz"; read as "Jász" from the town in the portal file name and on the sister cards.

**Date.** The month is not legible. As an inference only: Shrove Tuesday 1912 was 20 February, so a card of Thursday 22 February would fit the carnival question and "on Tuesday". This is not established.

## Review summary

Reviewer: Claude Opus 5.5 (Anthropic), a separate agent, round 1, verdict **REVISE**. It re-ran the command, read all rows from its own crops and decoded them with its own script. Seventeen of 18 rows matched. It checked the disclosed calls one by one, the plain parts, the language and the context, and found no sign of an undisclosed solution. Its reading was not blind, since it had read the solution first.

Findings and what changed:

1. **major, row 2.** The sign is j, not f, so "legjobb", not "legfőbb". Its bar is low with a short stub, and sister cards repeatedly have "legjobb kedvében". Ledger, literal text and Hungarian corrected; the translations already said "best". The f/j difference was added to the key.
2. **minor, row 6.** "hétfőt átdolgoztam" replaces "hétfőt át dolgoztam".
3. **minor, date.** The card was called undated; it now gives 1912 and day 22, from file name and postmark.
4. **minor, dotless k.** Two cases disclosed.
5. **minor, punctuation.** Marks left out of the ledger are now listed, and the lone stroke in row 5 is explained as a comma.
6. **minor, bracket.** "szín[el]őadás" became "színe[l]őadás".

The reviewer could not verify the month, what lies under the re-inked a of row 8, or whether the row 13 sign is v+t or t alone, and did not rule on every accent tick.

## Credits

- **Claude Opus 5.5, 2026-11-02:** source capture, transcription (sign ledger), key transfer, decipherment, response to review and this report. No earlier work exists on this number.
- **Claude Opus 5.5, separate reviewer agent:** independent review.

## Sources

- HC Portal record 1236, all three tabs, captured 2026-11-02: https://crypto.hcportal.eu/dashboard/cryptograms/1236 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/3768/conversions/cpc_1912--22_HU__HU_Jasz-Arokszalas_jolanka-102_pic-large.jpg (source/picture-large.jpg); original https://api.hcportal.eu/media/3768/cpc_1912--22_HU__HU_Jasz-Arokszalas_jolanka-102_pic.jpg.
- Address side: https://api.hcportal.eu/media/3769/conversions/cpc_1912--22_HU__HU_Jasz-Arokszalas_jolanka-102_adr-large.jpg (source/address-large.jpg); original https://api.hcportal.eu/media/3769/cpc_1912--22_HU__HU_Jasz-Arokszalas_jolanka-102_adr.jpg.
- Family key: ciphers/hcp-1216/work/graphic-key.json.
- HC Portal source reference: https://ecp.ep.liu.se/index.php/histocrypt/article/view/166.
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-11-02 by the orchestrator: no record for this number.
