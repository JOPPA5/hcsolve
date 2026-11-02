# HCP 1222 (cpc_1913-01-_HU__HU_Jasz Arokszalas_jolanka-113): Feri to Jolánka Tóth from Gyöngyös

Human solver: Tomáš Pavuk

**Status: deciphered in full (20 main rows and 6 rows under the stamp, 381 written signs); independent review 1 verdict REVISE, all eleven findings addressed.** Report dated 2026-11-02.

## Origin and context

The cryptogram is record 1222 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1222), portal name cpc_1913-01-_HU__HU_Jasz Arokszalas_jolanka-113, part of Tobias Schrödel's collection of cryptographic postcards (private collection; see the HistoCrypt paper https://ecp.ep.liu.se/index.php/histocrypt/article/view/166). When it was captured on 2026-11-02 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, category Substitution, language unknown, sender unknown, recipient Tóth Jolánka, with no transcription or solution attached.

The picture side is a tinted photograph of a man at a candle with a woman's face in a vision above him, printed sideways, with no writing. The whole message is on the address side, in invented signs: twenty rows on the left half and six short rows in the stamp corner, where the stamp itself is lost. The right half is in plain hand: **Szépreményű Tóth Jolánka úrleánynak, Jász-Árokszállás** ("To the promising young lady Jolánka Tóth, Jászárokszállás"; the first word is read from the cursive).

Two postmarks survive. The left one shows a date block with 13 and JAN, and rim letters that look like part of Jászárokszállás, an inference from a few letters. The right one shows a G on the rim and 13, which suits Gyöngyös but is only an initial. The portal filename gives January 1913. The day cannot be read.

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side with the cipher text, both postmarks and the plain address (source/address-large.jpg)](../source/address-large.jpg)

The card belongs to the "Jolánka" family of Hungarian cipher postcards addressed to Jolánka Tóth in Jászárokszállás, several of which are deciphered in this repository (for example HCP 1212, 1213, 1216, 1217, 1218, 1243, 1301). They share one key. This card was therefore read with a **known, transferred key**, not by a new key recovery. No published reading of this card was found or used.

## Method

- **Transcription:** Claude Opus 5.5 identified the family from the sign set and the address, read every row on enlargements of the un-converted high-resolution address side and recorded a sign ledger, one token per written sign (`work/ledger.txt`). The ledger is manual; no OCR was used.
- **Layout:** the baseline rises strongly to the right, so first contact sheets split rows 15 to 17 wrongly. A joint crop settled the count of twenty main rows.
- **Decoding:** the family key was applied by a short script. No new sign value was needed. One plain digit, 7, stands in clear in row 5.
- **Review:** a separate Claude Opus 5.5 agent re-ran the command, read all rows on its own enlargements and decoded its own sign reading with its own script. Its findings led to the corrections summarized below.

## Key

Hungarian simple monoalphabetic substitution with invented signs. The names are conventional descriptions of the handwritten shapes. Word spaces are only partly kept. Accents are marks over the signs and are often not visible.

| Sign | Letter | Sign | Letter | Sign | Letter |
|---|---|---|---|---|---|
| two bars | a | section mark / 5-shape | k | F-like | r |
| six | b | wave | l | right bowl | s |
| left bowl | c | three short strokes | m | gamma / corner | t |
| short stroke + long stroke | d | two short strokes | n | plain heavy cross | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross | f | tall stroke + short tick at right | h / p | low descender | y |
| open loop with descender | g | dotted crossed curve | i | tall crossed sign with long arm | z |
| inverted T | j | g + descender | gy | opposed bowls | cs |

One sign serves for both h and p, so each such call rests on the word. The d of this hand has its short stroke on the left, which HCP 1216 describes as "long stroke + short tick"; it is the same sign. Here d and h are visibly distinct, with the exceptions listed under Uncertainties.

## Plaintext

Literal decipherment, row by row. `{a|e}` is a blotted bar sign, `{d?}` a sign read as d from context, and `{t>r}` a corner sign without its mid bar where the word needs r.

```text
01 szerétetédesjolan             11 esmérkiadtaédeapam
02 kámtudatomhogyszeren          12 ajelszothogyhol
03 csesenmegerkeztembár          13 goz{a|e}kmernemadeni
04 lekéstemavonatrol             14 {d?}emostnemíroktöb
05 escsak7oraraértemgyön         15 betmajdestéraböve
06 gyösre.edesemmegnem           16 benistenveleédesem
07 tudommijansorsvá              17 vigyazonegésségére
08 rámmégcsakhelutan             18 adjaatiszteletemkedves
09 nezekmunka.utanota            19 mamajanakestestvé{t>r}einek
10 honisvanmunka                 20 tiszteltetemamanczikatis
stamp corner: csoko / lom / szam / talan / szo{t>r} / feri
```

Normalized Hungarian (word division, accents, spelling and punctuation are editorial; letters in square brackets are not on the card):

**Szeretett édes Jolánkám! Tudatom, hogy szerencsésen megérkeztem, bár lekéstem a vonatról, és csak 7 órára értem Gyöngyösre. Édesem, még nem tudom, milyen sors vár rám. Még csak hely után nézek, munka után; otthon is van munka. És mér? Kiadta éde[s]apám a jelszót, hogy dolgozzak, mer[t] nem ad enni. De most nem írok többet, majd estére bővebben. Isten vele, édesem, vigyázzon egészségére. Adja át tiszteletem kedves mamájának és testvéreinek. Tiszteltetem a Manczikát is.**

**Stamp corner: Csókolom számtalanszor. Feri**

English translation: **My beloved sweet Jolánka! I let you know that I arrived safely, although I missed the train and only reached Gyöngyös at 7 o'clock. My darling, I do not yet know what fate awaits me. For now I am only looking for a place, for work; there is work at home too. And why? My dear father has given out the word that I should work, for he will not feed me. But I will not write more now; by this evening [I will write] at more length. Farewell, my darling, take care of your health. Give my respects to your dear mother and your brothers and sisters. My regards to Manczika too.**

**In the stamp corner: I kiss you countless times. Feri**

Slovak translation: **Moja milovaná, sladká Jolánka! Oznamujem Vám, že som šťastne dorazil, hoci som zmeškal vlak a do Gyöngyösa som sa dostal až o 7. hodine. Drahá moja, ešte neviem, aký osud ma čaká. Zatiaľ len hľadám miesto, hľadám prácu; aj doma je práca. A prečo? Môj drahý otec vydal heslo, aby som pracoval, lebo mi nedá jesť. Ale teraz už viac nepíšem, do večera napíšem podrobnejšie. S Bohom, drahá, dávajte si pozor na zdravie. Odovzdajte moju úctu Vašej milej mamičke a súrodencom. Pozdravujem aj Manciku.**

**V rohu pod známkou: Bozkávam Vás nespočetnekrát. Feri**

Notes on the reading:

- The letter uses the formal address (vigyázzon, adja át), as other cards of the family do. The idiom kiadta a jelszót is literally "gave out the password", here "gave the order"; the sentence says the father will no longer keep him.
- "Gyöngyös" came out of the signs without being sought. It fits the family: other cards connect Feri with Gyöngyös.
- "Mér" is colloquial for "miért" ("why").

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1222/work/decode.py
```

The script uses only the Python standard library and writes no files. It checks the SHA-256 hashes of the two scans and the two high-resolution originals, decodes the manual sign ledger `work/ledger.txt` with the family key, prints the 20 main rows and 6 corner rows shown above, and prints the normalized text `work/normalized.txt`. It does not read the image; the transcription step is manual.

## Uncertainties

No item changes the sense of the letter. These calls rest on word sense:

- **Row 15, `estéra` = estére ("by evening").** The signs are é, r, then two clear bars, so the writer wrote a where the word needs e. This is the one word emended against a clear sign. "Este rá" is excluded by the acute and would leave "rá" with no meaning.
- **Row 11, `édeapam` = éde[s]apám.** The s is not written. The tick over the first e is taken as an acute; if it is a stray mark the word is the same. The p is the h/p sign. Punctuating "És mér kiadta édesapám..." or taking "mér" as "mert" would change only the link with the previous sentence.
- **Rows 12/13, `hol|gozak` = hogy dolgozzak.** The first sign of the word has the h form, not this hand's d. Read as d from context, the same slip as HCP 1216 row 5. Literal "hol gozak" is not Hungarian.
- **Row 13, blotted sign in `goz?k`.** A bar sign, a or e; the count of bars cannot be fixed. "Dolgozok" would keep the sense.
- **Row 14, first sign.** Two heavy slanted strokes joined by a bar; read d from context, "De most nem írok".
- **Row 8, `hel` = hely.** The final y is missing.
- **Row 7, `sors`.** The last s has a k-like hooked form; "sors" is the only sensible word.
- **Rows 19 and c5.** The r of "testvéreinek" and "számtalanszor" has no visible mid bar (literal t).
- **Row 3.** The t of "megérkeztem" is a heavy, apparently overwritten sign.
- **Stamp corner.** The f of "Feri" is a blotted star shape; the name is safe from the family.
- **Rows 5 and 6 at the postmark.** The n of row 5 is two strokes partly over the rim, both visible. In the m of row 6 the first stroke is clear and the others stand in the postmark block.
- **Other normalized spellings:** "szerétet" → szeretett, "megnem" → még nem, "mijan" → milyen, "ota|hon" → otthon, "bőve|ben" → bővebben, "eni" → enni, "vigyazon" → vigyázzon, "egésségére" → egészségére, "mer" → mer[t]. Most acute accents are supplied.
- **People and date.** Manczika is not identified. Feri is not identified beyond the family. The date is January 1913 from the filename and postmarks; the day is not legible.
- **Prior work.** The key was transferred from the family, not recovered blind from this card. No published reading was found: the portal status is Not solved and the AI Decipherment Register had no record on 2026-11-02.

## Review summary

Reviewer: Claude Opus 5.5 (Anthropic), a separate agent, round 1, verdict **REVISE**. It confirmed the command's output, that no new key value is needed, and that the picture side has no writing. It reported that the ledger had dropped four written signs. What changed:

- **Four signs restored:** n in row 5 ("gyön|gyösre"), m in row 6 ("megnem"), an e in row 11, and s in row 18, where the vowel was also corrected ("kedves", not "kadve"). Claims that the writer had omitted n, m and s were withdrawn. All row ends were rechecked and no further drops were found.
- **Rows 12/13:** the signs `hol` had been counted twice ("hogy hol dolgozzak"). Now "hogy dolgozzak", "that I should work", with the translations and title corrected.
- **Row 11:** the restored sign resolved the weak clause. The old "Kiadta de apám", with "de" as an emphatic particle, became "Kiadta éde[s]apám". The meaning stays, "father has given the word".
- **Row 15:** the reviewer asked for "rá" to be explained. A new crop showed an acute on the preceding e, so "este rá" became "estére", with one emended sign.
- **Smaller points:** the description of d, the blotted f, the Slovak accusative and the postmark details were corrected or added.

After the changes the reviewer's decoder and the ledger agree on all 26 rows and 390 letters, accents ignored. The readings "éde[s]apám" and "estére" were made after the review and were not seen by the reviewer. Neither changes the content of the message.

## Credits

- **Claude Opus 5.5, 2026-11-02:** source capture, key transfer, transcription, decipherment, response to review and this report. No earlier work exists on this number.
- **Claude Opus 5.5, separate reviewer agent:** independent review.
- **Family key:** the solvers of the finished Jolánka cards, credited in their own directories.
