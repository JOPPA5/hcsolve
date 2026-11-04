# HCP 1255 (cpc_1912-03-11_HU__HU_Jasz Arokszalas_jolanka-08): Feri writes to Jolánka Tóth

Human solver: Tomáš Pavuk

**Status: deciphered, with one unexplained run of three syllables and one unread ink blot; independent review 1 verdict REVISE, all findings addressed.** Report dated 2026-11-01.

## Origin and context

The cryptogram is record 1255 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1255), from Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-11-01 the portal listed it as **Not solved**, tagged Postcard, T. Schrödel Collection, category Substitution, language Unknown, location Europe, sender Unknown, recipient Tóth Jolánka, with no transcription or solution attached. The portal's file name gives the date 1912-03-11 and the place Jász-Árokszállás, in Hungary.

The cipher text fills the left half of the address side, in red ink: twenty rows of invented graphic signs. The picture side carries a printed verse, which is not cipher. The address is in plain writing: Szépreményű(?) Tóth Jolánka úrleánynak, Jász-Árokszállás (the first word is an uncertain reading of the script). In the stamp box, also in plain writing, stands csokolom szamta lan szor szerető sziv. The stamp has been lifted (a torn green fragment remains just below the box), so this message was hidden under the stamp: the card combines a cipher with steganography (checked on the original scan on 2026-11-03). The postmarks partly support the date: the left one shows day 11 clearly and the right one shows 912. The month could not be verified on the card.

The card belongs to the "Jolánka" family of cipher postcards to Tóth Jolánka, several of which are deciphered in this repository (for example HCP 1212, 1213, 1216, 1217, 1218, 1243 and 1301). The key was **transferred unchanged** from those cards; it was not recovered from this card alone. All transcription and decipherment of this number was done by Claude Opus 5.5 on 2026-11-01. There was no earlier work on it, and no published solution was found or used.

![Address side, with the cipher text at the left (source/address-large.jpg)](../source/address-large.jpg)

![Picture side, with the printed verse (source/picture-large.jpg)](../source/picture-large.jpg)

## Method

The first row, which decodes to keves Jolánkám becses, identified the family. The transcription is **manual**: each sign was read from enlarged crops of the un-converted original scan and recorded as one token in a sign ledger of 20 rows. Signs that run past the printed rule on rows 5, 8, 11 and 18 were checked separately, and the sign at the start of row 12, which lies under the printed word "Bromüra", was separated from the print with a red-minus-green map. The family key then turned every sign into Hungarian. No new sign value was needed.

The reviewer made its own transcription of all 20 rows, compared it with the ledger position by position, and measured bars and stroke proportions by machine. That comparison found five places to correct, listed under Review summary.

## Key

Type: **MASC + Steganography** (updated 2026-11-03). Monoalphabetic substitution with invented signs, plus a plain-Hungarian message hidden under the stamp. The labels are conventional names for the handwritten shapes.

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | section mark | k | F-like | r |
| six | b | wave | l | right bowl | s |
| opposed bowls | cs | three short strokes | m | gamma/corner | t |
| tall stroke + short | d / h / p | two short strokes | n | plain cross x | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross + | f | low descender | y | crossed diagonal | z |
| open loop with descender | g | dotted crossed curve | i | inverted T | j |
| joined loop + descender | gy | | | | |

Two marks over o or u give ö/ő or ü/ű. The tall + short sign is a near-homograph for d, h and p, so the choice among them rests on word sense.

## Plaintext

Literal decipherment, row by row. `[?]` is the ink blot.

```text
01 kevesjolankambecses
02 soraitköszönattel
03 megkaptammelyetepe
04 dőszivelvartamiga
05 zan[?]sajnalomhogynem
06 vigyazotmagarade
07 azmegnyugtathogymar
08 mulobavanitninsemi
09 utságedesjolankam
10 vasarnapokvetlenlen
11 lenlanlemegyekazthi
12 szeedesapamislemegy
13 ezelbezaromsoraim
14 istenveleaviszont
15 latásrüdvözlomata
16 volbolsirighütisz
17 telőjeferiedesjolan
18 markesorejarazidi
19 töbetnemirokmajd
20 vasarnapbovaban
```

Normalized Hungarian (accents, spelling and punctuation are editorial; {…} marks the unexplained run):

**Kedves Jolánkám! Becses sorait köszönettel megkaptam, melyet epedő szívvel vártam. Igazán [blot] sajnálom, hogy nem vigyázott magára, de az megnyugtat, hogy már múlóba van. Itt nincs semmi újság. Édes Jolánkám, vasárnap okvetlen {len len lan} lemegyek. Azt hiszem, édesapám is lemegy. Ezzel bezárom soraimat. Isten vele, a viszontlátásra. Üdvözlöm a távolból. Sírig hű tisztelője, Feri. Édes Jolán, már későre jár az idő, többet nem írok. Majd vasárnap bővebben.**

Plain writing in the stamp box, under the lifted stamp: **Csókolom számtalanszor. Szerető szív.**

English translation: **Dear Jolánka! I received your esteemed lines with thanks; I had awaited them with a yearning heart. I am truly sorry that you did not take care of yourself, but it reassures me that it is already passing. There is no news here. Sweet Jolánka, on Sunday I will definitely {len len lan} come down. I think my father is coming down too. With this I close my lines. God be with you, until we meet again. I greet you from afar. Your admirer, faithful unto the grave, Feri. Sweet Jolán, it is getting late, I will write no more. More on Sunday.**

Stamp box: **I kiss you countless times. Loving heart.**

Slovak translation: **Milá Jolánka! Vaše vzácne riadky som s vďakou dostal, očakával som ich s túžiacim srdcom. Naozaj ľutujem, že ste si nedávali pozor, ale upokojuje ma, že to už prechádza. Tu nie je nič nové. Sladká Jolánka, v nedeľu určite {len len lan} prídem dolu. Myslím, že aj môj otec príde dolu. Týmto končím svoje riadky. S Bohom, dovidenia. Pozdravujem Vás z diaľky. Váš až do hrobu verný ctiteľ, Feri. Sladká Jolán, už je neskoro, viac nepíšem. Viac v nedeľu.**

Políčko na známku: **Bozkávam Vás nespočetnekrát. Milujúce srdce.**

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1255/work/decode_opus.py
```

The script checks the SHA-256 hashes of the four image files, decodes the sign ledger work/ledger-opus.txt, and prints the literal rows and the normalized text. It does not read the images; the transcription step is manual and was checked independently in review.

## Uncertainties

- **The run {len len lan}, rows 10–11, is unexplained.** After okvetlen come three groups of wave + bars + two strokes, then lemegyek. The signs are clear, except that one wave lies partly under the printed word "Bromüra" and the wave of lan has an ink spot (read as a wave because it dips and has a rising tail; as a chevron the group would be van, which gives no sentence either). An isolated slanted mark stands above the l of the final -len of okvetlen. The run may be a false start on le-, but that is a guess. The sentence reads without it.
- **Row 5, Igazán and the blot.** Row 4 ends iga; row 5 opens with z, a and two nearly equal strokes, read as n, followed by a large blot and sajnálom. The blot cannot be read: it may hide a sign, or be a correction or a spill. The alternative Igaza, d[e] sajnálom ("You are right, but I am sorry") needs the pair to be d, against its proportions, and a restored e, and gives two de in a row. The choice of n rests on stroke shape plus sense from a small sample of measured pairs. It is strong evidence, not proof.
- **d, h and p** share one tall + short sign and are chosen by word sense throughout.
- **Writer's forms, normalized on sense:** köszönattel (r2, two-bar e), bovaban (r20, read bővebben: all signs clear, the word reconstructed), `utság` (r9, a gamma where újság needs j), hi|sze (r11–12, m omitted), keves (r1, no d), idi (r18, for idő), viszontlatásr (r14–15, final a missing). Most accents are supplied. múlóba van is left as written, a colloquial form of múlóban.
- **Row 15, fourth sign:** two full bars with a short mark high on the right, taken as a with an acute mark. If the mark were a short third bar the sign would be e. The word does not change.
- **Unusual or damaged signs:** the first sign of row 12 lies under print; the t of megkaptam (r3) is smudged and read by sense; the s of sírig (r16) has an unusual form, read within the family formula sírig hű.
- **Paratext:** the first address word is an uncertain reading of plain script. The month of the date is not verified on the card.
- **People:** the sender is known only as Feri, from the signature. It is not established that he is the Feri of HCP 1216, although the formula sírig hű recurs.

## Review summary

Reviewer: a separate Claude Opus 5.5 agent, round 1, verdict **REVISE**. The reviewer ran the reproduction command, transcribed all 20 rows itself from its own crops, diffed the result position by position (sign counts agreed in all rows, with six differences at five places), measured bars and stroke pairs by machine, confirmed that every sign fits the family key, and judged the language as period Hungarian with the family's formulas. It saw no sign that a published solution had been used. All seven findings were accepted after rechecking the crops:

- **Row 5.** The pair before the blot was changed from d to n, and the restored e was dropped. Igaza, d[e] sajnálom ("You are right, but I am sorry") became Igazán sajnálom ("I am truly sorry"), with the blot stated as unread. This is the only change of meaning.
- **Rows 10–11.** The last group of row 10 has three bars, so the unexplained run is {len len lan}, not {lan len lan}. The mark above -len is now recorded.
- **Row 12.** Both signs have three bars, so the literal word is lemegy, not lamagy.
- **Rows 7 and 15.** Row 7 is literally megnyugtat. The fourth sign of row 15 is now a with an acute mark, with e stated as the alternative.
- **Two-bar e.** The claim that this writer often uses it was cut down to the two cases that survive.
- **Key table.** The gy sign was added.
- **Date.** The postmark evidence (day 11, 912) is now stated.

No key value changed. Solver and reviewer were both Claude Opus 5.5, as separate agents.

## Sources

- HC Portal record 1255, General, Description and Attachments tabs, captured 2026-11-01: https://crypto.hcportal.eu/dashboard/cryptograms/1255 (source/metadata.md).
- Scans: https://api.hcportal.eu/media/3825/ and https://api.hcportal.eu/media/3826/ (picture and address sides, converted and original versions; full URLs and hashes in SOURCES.md).
- Family key: ciphers/hcp-1216 in this repository, with HCP 1212, 1213, 1217, 1218, 1243 and 1301.
- Portal attachment reference: https://ecp.ep.liu.se/index.php/histocrypt/article/view/166
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-11-01: no record for this card.
