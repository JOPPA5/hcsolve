# HCP 1316 (cpc_1912-06-30_HU__HU_Jasz Arokszalas_jolanka-27): Feri to Jolánka Tóth

Human solver: Tomáš Pavuk

**Status: the live text is deciphered in full (19 rows and the 5 rows in the stamp box, 337 signs). A short passage struck out by the writer is not decoded, and the sense of one clause (rows 15–17) stays tentative. Independent review 1: REVISE; all findings addressed.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1316 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1316), portal name cpc_1912-06-30_HU__HU_Jasz Arokszalas_jolanka-27, part of Tobias Schrödel's collection of cryptographic postcards. When it was captured on 2026-10-30 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, category Substitution, date 1912-06-30, language Unknown, recipient Tóth Jolánka, with no transcription or solution attached.

The picture side is a tinted photograph of a young man sitting by a lake with a couple in the background, with a printed Hungarian verse headed Szebb a pipasos mezőn…. It carries no cipher. The message is on the address side, in red ink: 19 rows on the left half and 5 small rows in the stamp box, under the place where the stamp was. The stamp is gone and has left a stain. The address is in clear: **Szépreményű Tóth Jolanka úrleánynak, Jász Árokszállás** ("To the promising young lady Jolanka Tóth, Jászárokszállás").

![Address side with the cipher text in red ink, the stamp box at top right and the clear address (source/address-large.jpg)](../source/address-large.jpg)

![Picture side, with printed verse and no cipher (source/picture-large.jpg)](../source/picture-large.jpg)

The card belongs to the "Jolánka" family of Hungarian cipher postcards to Jolánka Tóth, signed Feri (HCP 1212, 1213, 1216, 1217, 1218, 1243, 1301). They share one key, established on those cards by an OpenAI GPT solver and completed by Claude Opus 5.5. This card was therefore read with a **known, transferred key**, not by a new key recovery. Its own transcription and reading are by Claude Opus 5.5 (2026-10-30); there is no earlier work on this number. The portal's language "Unknown" can now be given as Hungarian.

## Method

The address side was enlarged 2–4× from the un-converted original scan, and each row was read sign by sign into a manual ledger (`work/ledger.txt`, one token per written sign, no OCR). Row 1 gave édes szerelmem drága with the family key at once. The script `work/decode.py` checks the hashes of the images and applies the key to the ledger.

In review a separate Claude Opus 5.5 agent made its own crops (2× rows, 4–7× details), read the signs itself into shape classes, and decoded them with its own table taken from HCP 1216's key file. It found no conflict in any clearly read sign.

## Key

Hungarian, simple monoalphabetic substitution with invented graphic signs. The names are conventional descriptions of handwritten shapes.

| Sign | Letter | Sign | Letter | Sign | Letter |
|---|---|---|---|---|---|
| two bars | a | section mark, open S | k | F-like | r |
| six | b | wave | l | right bowl | s |
| left bowl | c | three short strokes | m | gamma / corner | t |
| short + long stroke | d | two short strokes | n | arched x | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross + | f | tall + short stroke | h / p | low descender | y |
| open loop with descender | g | dotted crossed curve | i | arched x with long rising tail | z |
| inverted T | j | | | | |

On this card cs and sz are spelt c+s and s+z, and gy is g+y. Dots or a double mark over a sign give ü and ű. Acute accents are mostly unwritten and are supplied in normalization.

## Plaintext

Literal decipherment, row by row (`?` = doubtful sign, `{x|y}` = read x, y not excluded, `[ ]` = stain-damaged sign restored from the formula):

```text
01 edesszerelmemdraga          11 adsemitmegragal
02 jolankamtudatomhogy         12 mazobeszedekrecsak
03 szerencsesenmeg             13 legyenkitartoszerel
04 erkeztemmegatancz           14 memugymintszeretem
05 iskolaisvoltam              15 m?a?gatmitbarmar
06 kedvesemaboldogsag          16 tetem?is  + struck-out passage
07 kertjebenegyfokal           17 {b|d}ebizonyithatnak
08 m?egintbeljeb               18 ezelbez{e|a}tomsoraim
09 kerültemboldogit            19 istenveatavolbol
10 azatudathogynem
stamp: cso[k][o]lom / szamta / lanszor / hű kedves / se feri
```

Normalized Hungarian (word division, accents, punctuation and doubled consonants are editorial):

**Édes szerelmem, drága Jolánkám! Tudatom, hogy szerencsésen megérkeztem, meg a tánciskola is volt ám. Kedvesem, a boldogság kertjében egy fokkal megint beljebb kerültem. Boldogít az a tudat, hogy nem ad semmit [a] megrágalmazó beszédekre. Csak legyen kitartó, szerelmem, úgy, mint szeretem magát, mit bár már tettem is bebizonyíthatnák. Ezzel be[zár]om soraim. Isten ve[le] a távolból.**

**Under the stamp: Csókolom számtalanszor. Hű kedvese, Feri.**

English translation: **My sweet love, dear Jolánka! I let you know that I arrived safely, and the dancing school took place too. My darling, in the garden of happiness I have once again got one step further in. I am made happy by the knowledge that you give nothing for slanderous talk. Only stay steadfast, my love, just as I love you, which I wish my deeds too could already prove (sense tentative). With this I close my lines. God be with you, from afar.**

**Under the stamp: I kiss you countless times. Your faithful sweetheart, Feri.**

Slovak translation: **Moja sladká láska, drahá Jolánka! Oznamujem Vám, že som šťastne docestoval a bola aj tanečná škola. Drahá, v záhrade šťastia som sa zasa o stupeň dostal hlbšie. Teší ma vedomie, že nedáte nič na ohováračské reči. Len zostaňte vytrvalá, moja láska, tak ako ja ľúbim Vás, čo by, kiež, už mohli dokázať aj moje skutky (zmysel neistý). Týmto končím svoje riadky. S Bohom z diaľky.**

**Pod známkou: Bozkávam Vás nespočetnekrát. Váš verný milý, Feri.**

## Uncertainties

Points marked **context** rest on word sense, not on a clean sign match.

- **Rows 15–17, sense.** The main reading, mit bár már tettem is bebizonyíthatnák, takes bár + conditional as "if only" and tettem (written tetem) as "my deed". It is the only version found in which the clause is grammatical, but the plural ending does not agree with a singular tettem. The translation is tentative.
- **Row 17, first sign (context).** A blot with a stem, a closed bowl and a thin stroke rising on the right. The bowl fits b, the rising stroke fits d, and neither shape explains everything. Read d, the words are de bizonyíthatnak/-nák, "but they can/could prove it". The ending may be -nak or -nák; two bars exclude -nék.

![Row 17, first sign: original and green channel, with the bowl and the rising stroke (review/work/crops/r17_blob.png)](../review/work/crops/r17_blob.png)

- **Row 16, m of tetem (context).** A retouched three-stroke zigzag with a closing top line; a z retouched into it cannot be excluded (tetéz is). The reviewer could not confirm m.
- **Row 16, struck-out passage.** Several heavy lines, running past the column rule, with a raised 6 and a dotted sign above and a large loop below, so it was overwritten in layers. It is **not decoded and not used**. Only as a hypothesis, it may be a false start of bizo-.
- **Row 15 (context).** The m of magát is retouched and looks like four strokes; the vowel after it is blotted, so a against e is not settled from the pixels.
- **Row 18, bez{e|a}tom.** The card does not literally say bezárom. The sign before t has two bars and a speck, so e or a; the gamma after it is a t and lacks the crossbar of the F (r) in soraim. be[zár]om is an editorial correction from the formula ezzel bezárom soraim.
- **Row 5, division.** volt ám ("took place, you know") is printed; voltam ("I was") is possible if a case ending is supplied (tánciskolá[ban]).
- **Rows 4, 8 (context).** The m of meg (row 4) is heavily overwritten, and the m of megint (row 8) looks like a retouched Latin form; both are read from the words.
- **Row 11, semit.** A blacked-out hatched sign between i and t is taken as cancelled, with no value. There is no written a before megrágalmazó.
- **Row 19, ve a.** The card has v, e, a: vele lacks l e, a writer's omission supplied in brackets.
- **Stamp box.** The k and o of csókolom lie in the stain, only traces remain, and they are restored from the formula. kedvese is written with the s twice, across a line end.
- **u against z.** Both are arched crosses, told apart by the long tail of z; every decision gives a word, but they rest partly on context.
- **h/p.** One sign serves for both; the h of -hat- rests on context.
- **Date.** The postmark clearly shows the day 30. The month and year are not read with confidence, so the portal's 1912-06-30 is only partly confirmed.
- The sender is known only as Feri. No web search for a prior publication of this card was made beyond the portal status and the AI Decipherment Register (no record, checked 2026-10-30).

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1316/work/decode.py
```

The script uses only the standard library. It checks the SHA-256 of both source images and both original scans, decodes the manual ledger and prints the 24 rows, the sign count (337) and the normalized text. It does not read the images: the transcription step is manual and was checked independently in review.

## Review summary

Reviewer: a separate Claude Opus 5.5 agent, round 1, verdict **REVISE**, no blockers. It ran the command, read all 24 rows itself, confirmed the key and almost all of the reading, and raised seven findings:

- **Row 17, first sign (major).** It was described as a formless blot read d. It has a bowl, so the sign is now marked b or d, and the main reading changed from de bizonyíthatnak to bebizonyíthatnák.
- **Row 18, sign 8.** Now marked e or a; the slip against bezárom is restated.
- **Row 5.** The alternative voltam is now stated.
- **-nak / -nák.** Both are now given, and the conditional is used.
- **Row 15, first sign.** Now marked doubtful.
- **Row 16.** The description of the zigzag and the struck passage was corrected.
- **Status line.** "Read letter by letter" was removed.

One sign value changed as the main reading (d to b); the sense of that clause was already tentative and stays so. Everything else in the reading stands. The change to the bár interpretation came after the review and has not itself been re-reviewed.

## Sources

- HC Portal record 1316, General, Description and Attachments tabs, captured 2026-10-30: https://crypto.hcportal.eu/dashboard/cryptograms/1316 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/4008/conversions/cpc_1912-06-30_HU__HU_Jasz-Arokszalas_jolanka-27_pic-large.jpg (source/picture-large.jpg); original https://api.hcportal.eu/media/4008/cpc_1912-06-30_HU__HU_Jasz-Arokszalas_jolanka-27_pic.jpg
- Address side: https://api.hcportal.eu/media/4009/conversions/cpc_1912-06-30_HU__HU_Jasz-Arokszalas_jolanka-27_adr-large.jpg (source/address-large.jpg); original https://api.hcportal.eu/media/4009/cpc_1912-06-30_HU__HU_Jasz-Arokszalas_jolanka-27_adr.jpg
- Family key: ciphers/hcp-1216 and sister cards HCP 1212, 1213, 1217, 1218, 1243, 1301 in this repository.
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-30.
