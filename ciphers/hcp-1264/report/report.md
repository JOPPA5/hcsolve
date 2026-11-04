# HCP 1264 (cpc_-02-04_HU__HU_Jasz Arokszalas_jolanka-93): Feri to Jolánka Tóth

Human solver: Tomáš Pavuk

**Status: deciphered in full (all 23 main rows and the 6 rows in the stamp box); independent review 1 verdict REVISE, all five findings addressed, no word of the normalized text changed.** Report dated 2026-11-01.

## Origin and context

The cryptogram is record 1264 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1264), part of Tobias Schrödel's collection of cryptographic postcards (private collection). When captured on 2026-11-01 the portal listed it as **Not solved**, tagged Postcard, T. Schrödel Collection, category Substitution, language Unknown, sender Unknown, recipient Tóth Jolánka, with no transcription or solution attached.

The picture side is a tinted photograph of a young couple among leafy branches, with a printed Hungarian verse, Hogyha szemedbe nézek / Lelked csak nekem virul ("When I look into your eyes, your soul blooms only for me"), the vertical words beszél suttogva ("speaks whispering") and hulló falevél ("falling leaf"), and publisher number 2203. None of this is cipher.

The address side has the address in plain writing: **Szépreményü / Tóth Jolánka / úrleánynak / Jász Árokszállás** ("To the promising Miss Jolánka Tóth, Jászárokszállás"). The cipher text fills the left half in 23 rows, and six more short rows stand in the box for the stamp, which is missing. A postmark over the stamp box reads GYÖN…, presumably Gyöngyös. A fainter, rotated postmark at upper left shows FEB with a numeral 1 before it. The month agrees with the "-02-04" in the portal name, but day and year cannot be read on the card, so no full date is claimed.

The card belongs to a family of cipher postcards to Jolánka Tóth, from a suitor who signs Feri. Several are deciphered in this repository (HCP 1212, 1213, 1216, 1217, 1218, 1243, 1301). The key was transferred from them; this is not a new key recovery. No reading of this card was supplied or consulted.

![Address side: cipher rows at left, six rows in the stamp box, plain address at right (source/address-large.jpg)](../source/address-large.jpg)

![Picture side, sideways as scanned: printed verse only, no cipher (source/picture-large.jpg)](../source/picture-large.jpg)

## Method

The transcription is manual and was made by Claude Opus 5.5 from enlarged crops of the unconverted high-resolution scan, with no OCR. Each written sign is one token in a ledger of 29 rows (work/ledger-opus.txt), and a short script decodes the ledger with the family key. The hard places were read again at up to 12× enlargement. The key needed no change and no new sign value.

The reviewer, a separate Claude Opus 5.5 agent, cut its own crops, made its own row transcription and sign table from the HCP 1216 legend, and decoded them with its own script. Its pass was not blind, since it had read the solver's ledger first. It agreed on 28 of 29 rows. The one difference is the first sign of stamp row 6, described below.

## Key

**Cipher type: MASC + Steganography** (updated 2026-11-03). The six cipher rows under the lifted stamp are a hidden message in the stamp box, so the register type is MASC + Steganography rather than plain MASC.

Hungarian, simple monoalphabetic substitution with invented graphic signs. Accents are marks over the base sign; "gy" is written g + y. The sign names are conventional labels.

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | section mark (S) | k | F-like | r |
| six | b | wave | l | hook ")" | s |
| opposed bowls | cs | three strokes | m | gamma | t |
| tick left + long stroke | d | two strokes | n | plain x | u |
| three bars | e | cursive loop (dots = ö) | o | chevron | v |
| upright cross | f | long stroke + tick right | h / p | low descender | y |
| open loop with descender | g | dotted crossed curve | i | crossed diagonal with tail | z |
| inverted T | j | | | | |

The same sign serves for h and p, so the choice rests on the word. Only pénzem (row 11) needs p here.

## Plaintext

Literal decipherment as printed by the script, row by row. Square brackets mark a blotted sign restored by sense, curly brackets a doubtful or struck sign, angle brackets the insertion above the line. The h of row 11 is the h/p sign.

```text
01 szeretetédesjolan      13 önisbefogjalatni
02 kámkivanomhogya        14 édesemhogyijenhej
03 legjobbkedvebenta      15 zetbe<vagy>nemtehetek
04 laljasoraimszerel      16 roladeeztnemfogja
05 memneharagudjon        17 észrevennirolammajd
06 r[a]mhogynemmehet-     18 senkicsakmagaédesem
07 temletud[a]tomhogy     19 dragacsillagomlegyen
08 csütötökönokvet        20 türelemmeledesem
09 lenlemegyekamulat      21 csütörtökigistenve
10 ságbaigazhogykevés     22 leédesemviszontla
11 ahénzemdemajdsze       23 tasraimadojaferi
12 rényenköltekez{struck e}ve
stamp box: csokol{t?}m szamta lanszor sirihü kedvesse {u/f}eri
```

Normalized Hungarian (word division, punctuation, accents and spelling are editorial):

**Szeretet[t] édes Jolánkám! Kívánom, hogy a legjobb kedvében találja soraim. Szerelmem, ne haragudjon rám, hogy nem mehettem le. Tudatom, hogy csütö[r]tökön okvetlen lemegyek a mulatságba. Igaz, hogy kevés a pénzem, de majd szerényen költekezve, Ön is be fogja látni. Édesem, hogy ilyen helyzetbe[n] vagy[ok], nem tehetek róla, de ezt nem fogja észrevenni rólam majd senki, csak maga, édesem. Drága csillagom, legyen türelemmel, édesem, csütörtökig. Isten vele, édesem, [a] viszontlátásra. Imádója Feri.**

**In the stamp box: Csókol[o]m számtalanszor. Síri[g] hű kedvese, Feri.**

English translation: **My beloved sweet Jolánka! I wish that my lines find you in the very best of spirits. My love, do not be angry with me that I could not come down. I let you know that on Thursday I will definitely come down to the party. True, I have little money, but by spending modestly you too will come to understand. My sweet, that I am in such a position I cannot help, but nobody will notice this about me except you, my sweet. Dear star of mine, be patient, my sweet, until Thursday. God be with you, my sweet, until we meet again. Your adorer, Feri.**

**In the stamp box: I kiss you countless times. Your sweetheart, faithful unto the grave, Feri.**

Slovak translation: **Moja milovaná sladká Jolánka! Želám si, aby Vás moje riadky zastihli v čo najlepšej nálade. Moja láska, nehnevajte sa na mňa, že som nemohol prísť dolu. Oznamujem Vám, že vo štvrtok určite prídem dolu na zábavu. Pravda, peňazí mám málo, ale budem míňať skromne, aj Vy to uznáte. Drahá, že som v takej situácii, za to nemôžem, ale nikto to na mne nezbadá, iba Vy, drahá. Moja drahá hviezdička, majte trpezlivosť, drahá, do štvrtka. S Bohom, drahá, dovidenia. Váš ctiteľ Feri.**

**V rámčeku na známku: Bozkávam Vás nespočetnekrát. Váš do hrobu verný milý, Feri.**

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1264/work/decode_opus.py
```

The script uses only the standard library. It checks the SHA-256 of all four scans, decodes the ledger, prints the literal rows and the count of 423 signs, and then prints the normalized text. It does not read the image: the transcription step is manual and was checked in review.

## Uncertainties

The reading is complete, but these calls rest on word sense or on a doubtful sign.

- **Row 15 insertion `<vagy>`, the weakest point.** A caret-like v and a small two-bar a stand clearly above the line. The third mark is only a forked mark on top of the n stroke, so g rests on sense alone; the fourth is a reasonable small y. Vagy literally means "you are"; the English takes it as a truncated vagyok "I am", which fits the money, nem tehetek róla and rólam better. The writer otherwise addresses her formally, which also speaks against "you are". A double blot with a small loop follows on the same level, where -ok would go. It may be a plain blot and cannot be read as letters.
- **Blots in rows 6 and 7.** The lower bar of the a in r[a]m and tud[a]tom is a solid blot; a or e would fit the visible strokes, and only a gives the word.
- **Row 21 csütörtökig.** The i is blotted in its upper half with no dot visible, and o is also possible; the k before it is a small closed 8, unlike the other k signs. -ig "until" rests on sense.
- **Stamp row 6, first sign.** A symmetric X, the plain u shape, not the upright cross of rows 13, 16 and 23. The card literally says ueri; Feri is a call on word sense, with the clear signature of row 23 behind it.

![First sign of the stamp signature, a plain X shape (review/work/crops/feri_stamp.png)](../review/work/crops/feri_stamp.png)

- **Stamp row 1.** The sign before the m is a bold gamma, not an o. Csókol[o]m follows the family formula; csókol[t]am "I kissed", with a missing a, is the alternative.
- **Other stamp rows.** sirihü has no g on the card (Síri[g]). kedvesse has two s hooks and a stained final e (kedvese).
- **Row 12.** A vertical stroke crosses three bars after z; read as an e struck through by the writer.
- **Row 16 `de`.** The d is followed by one extra bold tick with no letter value; only de gives sense.
- **Row 17 rólam.** The third stroke of the m is short and thick; n gives no word.
- **h/p and d/n.** pénzem rests on word sense. The d of drága, róla de and majd is told from n by form, and all fit the sense.
- **The writer's spelling.** csütötökön lacks an r (row 21 has it), szeretet lacks a t, and ijen, hejzetbe stand for ilyen, helyzetbe, as with ojan on HCP 1216. The a before viszontlátásra is editorial.
- **Punctuation.** Whether költekezve, Ön is be fogja látni is one clause is an editorial matter, and the meaning of that clause is loose.
- **Context.** "Thursday" and the party cannot be tied to any outside record. The writer is known only as Feri, and the full postmark date is not legible.
- **Accents.** The dots on ö and ü were not audited one by one in review; no word here depends on them.

## Why the reading is sound

The key, unchanged from reviewed cards, turns 423 written signs into running Hungarian. Repeated words decode identically in separate places: hogy ×5, édesem ×4 (plus édes once), csütörtök- ×2, nem ×3. The formulas are those of the family: Kívánom, hogy a legjobb kedvében találja soraim (HCP 1218), Isten vele (1216, 1217), Imádója (1301), számtalanszor … hű kedvese (1216). HCP 1301 also promises that he will come down on a later occasion. Letter frequencies look like Hungarian, and the addressee agrees with the plain address.

## Review summary

Reviewer: Claude Opus 5.5, a separate agent, round 1, verdict **REVISE**. It ran the reproduction command, decoded its own transcription, went through every row on enlarged crops and judged the disputed signs at up to 10×. It could not refute the reading. Its five findings concerned the record, not the words:

- **Stamp signature (major).** The ledger had recorded the first sign as f, undisclosed, and counted Feri as evidence. It now has its own token and prints `{u/f}eri`, is listed as an uncertainty, and no longer counts as evidence.
- **Ink mark after the row 15 insertion (minor).** Now disclosed as possible but unreadable.
- **Row 21 i and k (minor).** Now disclosed; the claim that only two signs were hidden was softened.
- **Counts (minor).** Corrected to hogy ×5, édesem ×4 and 423 signs.
- **Postmark (minor).** The FEB postmark is now recorded.

No word of the normalized text changed because of the review; only stamp row 6 of the literal output changed. The transcription, key transfer and decipherment are by Claude Opus 5.5; there was no earlier work on this number.

## Sources

- HC Portal record 1264, General, Description and Attachments tabs, captured 2026-11-01: https://crypto.hcportal.eu/dashboard/cryptograms/1264 (source/metadata.md). The portal's source link: https://ecp.ep.liu.se/index.php/histocrypt/article/view/166
- Picture side: https://api.hcportal.eu/media/3852/conversions/cpc_-02-04_HU__HU_Jasz-Arokszalas_jolanka-93_pic-large.jpg and the unconverted original.
- Address side: https://api.hcportal.eu/media/3853/conversions/cpc_-02-04_HU__HU_Jasz-Arokszalas_jolanka-93_adr-large.jpg and the unconverted original.
- Family key: ciphers/hcp-1216 and the sister cards named above.
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-11-01: no record for this card.
