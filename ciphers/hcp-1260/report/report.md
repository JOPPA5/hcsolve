# HCP 1260 (cpc_--25_HU__HU_Jasz Arokszalas_jolanka-90): Feri to Jolánka Tóth, a matter to settle by word of mouth

Human solver: Tomáš Pavuk

**Status: complete reading, with one clause of uncertain syntax; independent review 1 verdict REVISE, all nine findings addressed.** Report dated 2026-11-01.

## Origin and context

The cryptogram is record 1260 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1260), portal name cpc_--25_HU__HU_Jasz Arokszalas_jolanka-90, from Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-11-01 the catalogue row listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, category Substitution, language Unknown, location Europe, sender Unknown, recipient Tóth Jolánka, with no transcription or solution listed. The detail page timed out at capture, so its three tabs were not read one by one for this number. The portal cites https://ecp.ep.liu.se/index.php/histocrypt/article/view/166 as a reference.

It is a tinted photographic picture postcard of a young couple cheek to cheek. The printed titles are Lári-Fári and Cigányprímás, with a printed four-line verse. The picture side carries no handwriting. The address side is in clear, in red ink: **Szépreményű / Tóth Jolánka / úrleánynak / Jász Árokszállás** ("to the young lady of fair promise, Jolánka Tóth, Jászárokszállás", Hungary).

The postmark is too faint to give a place or date, so the card is undated. It belongs to the family of cipher cards addressed to Jolánka Tóth, several of which are deciphered in this repository (for example HCP 1216, 1212, 1213, 1217, 1218, 1243 and 1301). HCP 1216 has the same sender name and closing formula. No published solution of this card was found or used.

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side: 22 cipher rows on the left, a corner block at the top right, and the address in clear (source/address-large.jpg)](../source/address-large.jpg)

## Method

The key was **transferred** from the finished family card HCP 1216, not recovered from this card. The card was read sign by sign from 3x to 5x enlargements of the un-converted original scan. Every written sign was entered as one token in a ledger of 22 main rows and 8 corner rows (work/ledger.txt). A script (work/decode.py) checks the image hashes and decodes the ledger, and it runs from the repository root with one command:

```sh
python3 -I ciphers/hcp-1260/work/decode.py
```

The transcription was not blind, because word expectations formed during reading. Signs whose shape does not cleanly match their value are marked `?` in the ledger, and there are ten of them. The reading order is the main block, then the corner block.

## Key

**Cipher type: MASC + Steganography** (updated 2026-11-03). Hungarian, simple monoalphabetic substitution with invented graphic signs, in red ink; the corner block was hidden in the stamp box under the stamp. The family key applied unchanged:

| Sign | Plain | Sign | Plain | Sign | Plain |
|---|---|---|---|---|---|
| two bars | a | section mark | k | F-like | r |
| six | b | wave | l | right bowl | s |
| opposed bowls | cs | three short strokes | m | gamma/corner | t |
| short tick left + long stroke | d | two short strokes | n | plain cross x | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross + | f | tall stroke + short tick right | h, p | y-loop | y |
| open sign with descender | g | dotted crossed curve | i | crossed diagonal with tail | z |
| inverted T (with variants) | j | | | | |

On this card gy is written as g + y. Dots over o and x give ö and ü, and two ticks over o give ő. The card has no separate mark for ű, so hű is written hü. Acute accents are not reliably visible and are supplied. In the corner block 7 het is written in clear.

## Plaintext and translation

Literal decipherment, row by row:

```text
01 szeretetedesjolan        12 erölirasbantargyal
02 kamegyetlenremenyemne    13 nideitlesznemsoka
03 haragudjonramhogyijen    14 raazidőhogyszoval
04 ritkanirokmitmagamis     15 beszelhetemagaval
05 restelekdeanyiraideges   16 edesemmitaligva
06 vagyokdenecsodelkozon    17 rokhogymulatot
07 rajtaedesemhogyhogy      18 vasarnapremelem
08 volnajobbdeerölnem       19 jolhogyszolgal
09 irokmajdszovalfo         20 jaazegesegremelem
10 gomelinteznieztaz        21 jolezelzaromso
11 ügyetmertnemakarok       22 raimmaradoksirighükedeseferi

corner: istenve / leveede / semsirig / hükedve / jeviszont / latasra / 7hetmul / va
```

**Hungarian, normalized** (square brackets mark what is not on the card):

Szeretett édes Jolánkám, egyetlen reményem! Ne haragudjon rám, hogy ilyen ritkán írok, mit magam is restellek. De annyira ideges vagyok. De ne csodálkozzon rajta, édesem, hogy hogy volna jobb, de erről nem írok; majd szóval fogom elintézni ezt az ügyet, mert nem akarok erről írásban tárgyalni. De itt lesz nemsokára az idő, hogy szóval beszélhete[k] magával, édesem, mit alig várok. Hogy mulatott vasárnap? Remélem, jól. Hogy szolgálja az egés[zs]ég[e]? Remélem, jól. Ezzel zárom soraim, maradok sírig hű ked[v]ese, Feri.

Corner: Isten vele [ve] édesem, sírig hű kedvese. Viszontlátásra 7 hét múlva.

**Stamp-box message (audit 2026-11-03).** The corner block is written in the stamp box at the top right of the address side, under the stamp, which has since been lifted: a pink dye bleed from the soaked-off stamp, a residue strip and the postmark stroke ending at the block's edge mark its place. The hidden message is in the cipher signs (with 7 het in clear) and is the corner text above: Isten vele [ve] édesem, sírig hű kedvese. Viszontlátásra 7 hét múlva. It was re-checked on 2x to 4x crops; no sign changed and no clause is unread.

**English:**

My beloved sweet Jolánka, my only hope! Do not be angry with me for writing so rarely, which I am ashamed of myself. But I am so nervous. But do not wonder, my darling, how it would be better [exact sense of this clause uncertain], but I am not writing about this; I will settle this matter by word of mouth, because I do not want to discuss it in writing. But the time will soon be here when I can speak with you in person, my darling, which I can hardly wait for. How did you enjoy yourself on Sunday? Well, I hope. How is your health? Well, I hope. With this I close my lines; I remain, faithful unto the grave, your sweetheart, Feri.

Corner: God be with you, my darling, your sweetheart, faithful unto the grave. Until we meet again in 7 weeks.

**Slovak:**

Moja milovaná, sladká Jolánka, moja jediná nádej! Nehnevajte sa na mňa, že píšem tak zriedka, za čo sa sám hanbím. Ale som taký nervózny. Ale nečudujte sa tomu, drahá, ako by bolo lepšie [presný zmysel tejto vety je neistý], ale o tom nepíšem; túto záležitosť vybavím ústne, lebo o tom nechcem rokovať písomne. Ale čoskoro príde čas, keď sa s Vami budem môcť porozprávať osobne, drahá, na čo sa neviem dočkať. Ako ste sa zabavili v nedeľu? Dúfam, že dobre. Ako Vám slúži zdravie? Dúfam, že dobre. Týmto končím svoje riadky a zostávam do hrobu verný Váš milý, Feri.

V rohu: S Bohom, drahá, Váš do hrobu verný milý. Dovidenia o 7 týždňov.

## Uncertainties

**One uncertain clause.** Rows 7 to 8, hogy hogy volna jobb: both hogy are clear, but the syntax is not. The next word is written with the h/p shape, as de is in row 5. The preferred reading is de erről nem írok, "do not wonder how it would be better, but I am not writing about this". The alternative is ha erről nem írok, which changes a vowel, "that it would be better if I do not write about this" (or hogyhogy, "how come it would be better"). The clauses around it are clear: he will settle the matter by word of mouth, not in writing.

**Signs valued from word sense, not from a clean shape:**

- Row 1, t of szeretet-: heavily overwritten.
- Rows 5 and 8, de: tick to the right, the h/p shape, not the d shape.
- Row 14, h of hogy: stroke blotted solid.
- Row 18, p of vasárnap: tick to the left, the d shape.
- Rows 3 and 20, j: a low-cross variant. haragudjon in row 3 is certain, which supports szolgálja in row 20.
- Row 20, last sign of egeseg: overwritten, read g.
- Corner row 4, d of kedve: two nearly equal tall strokes, closer to n; kenve is no word.
- Corner row 5, first sign: read as a reduced s, kedvese. The literal kedveje is no word, and kedvese is the family closing.

**Writer's slips, normalized editorially:** kedese in row 22 has no v on the card (ked[v]ese); beszelhete magaval lacks the verb's k; az egeseg lacks zs and a final e; szeretet has one t. Other spellings are ijen, restelek, anyira, csodelkozon, ezel, mulatot, eröl for erről. The surplus ve in the corner (Isten vele ve édesem) is treated as a false start, which cannot be proved.

**Not established:** the date and place of posting; what "this matter" was; the figure read as 7 has no parallel on this card, though "in 7 weeks" reads naturally.

## Review summary

An independent Claude Opus 5.5 reviewer ran the reproduction command, read every row on the enlargements, and decoded its own shape-named transcription with its own key table. 25 of 29 compared rows were identical. It found the key right and the language credible, and returned **REVISE** with nine findings (three major, six minor). All were accepted after rechecking the scans. The key did not change.

- Row 22: a chevron (v) in the ledger was not on the card, having been supplied from expectation. It was removed, so the literal is now kedese.
- Rows 22 and C4: the mark over u was misreported in opposite directions. Both now read hü, and a position-dependent rule for ű was withdrawn.
- Row 8: the sign has the same shape as in row 5, so both are now treated alike, giving de in place of ha as the preferred reading. ha is kept as the alternative, and the translation no longer smooths the uncertain clause.
- Minor changes: the j variant in row 3 and the d in corner row 4 are flagged; the normalizations of rows 15 and 20 are corrected; the statement about the portal's attachments is qualified; two stale claims were updated.

Key transfer rests on the family work of HCP 1216, where source capture and a partial reading were done by OpenAI GPT-6 Astra / GPT-6.1 Sol and completion by Claude Opus 5.5. This card itself was transcribed and read by Claude Opus 5.5.
