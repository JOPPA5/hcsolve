# HCP 1309 (cpc_1912--_HU__HU_Jasz Arokszalas_jolanka-99): Feri to Jolánka Tóth

Human solver: Tomáš Pavuk

**Status: deciphered with the known family key; every row is read except one struck-out stretch and one smeared patch under the stamp, both disclosed below. Independent review 1 verdict REVISE; all findings addressed, no decoded letter changed.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1309 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1309), portal name cpc_1912--_HU__HU_Jasz Arokszalas_jolanka-99, part of Tobias Schrödel's collection of cryptographic postcards. When it was captured on 2026-10-30 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, category Substitution, date and language Unknown, location Europe, recipient Tóth Jolánka, with no transcription or solution attached. The date 1912 is suggested only by the portal file name.

It is a picture postcard of a young woman with a lace headband. The printed green words read “Találkozhatnánk?” and “Csütörtökön” ("Could we meet?", "On Thursday"); they are the card's printed text, not part of the message. The address side has in clear, in red ink: “Szépreményű Tóth Jolánka úrhölgynek, Jász Árokszállás”. The message fills the left half of that side in red cipher, nineteen rows, with a further six short rows written in the stamp field. The return address is in clear at the foot: “Rákos Palota, Tavasz u. 2 sz.”

The card belongs to the family of cipher postcards to Jolánka Tóth of Jászárokszállás, written by a man who signs Feri. Several are finished in this repository, among them HCP 1212, 1213, 1216, 1217, 1218, 1243 and 1301. The key was transferred from those cards, so this is **a known, transferred key, not a new key recovery**. No reading of this card was supplied or consulted, and no published solution was found.

![Address side: cipher message at the left, more cipher inside the stamp field, address and return address in clear (source/address-large.jpg)](../source/address-large.jpg)

![Picture side with the printed words Találkozhatnánk? and Csütörtökön (source/picture-large.jpg)](../source/picture-large.jpg)

Two postmarks are on the card, both unread. A ring right of the stamp shows three capitals, read as ?AL with a closed O/D-like first letter; PAL(OTA) would need a P whose stem cannot be seen, so it is not claimed. A faint strike at top centre shows only broken characters and a barred block. Neither gives a place or a date.

## Method

The transcription is manual. Every sign was read from enlarged crops of the un-converted scan and recorded in a sign ledger, one token per written sign; there was no OCR. The key of HCP 1216 was then applied unchanged, by script. The opening formula (“Szeretet[t] édes Jolá[n]kám, kívánom, hogy jó egés[z]ség…”) confirmed the key at once. Several first readings were corrected on the enlargements before handover, always by rereading the shape and never by changing the key: the bars at the end of row 7 are two, giving “la|kom”, and the bars in rows 16–17 are two, giving “Árokszállásba”.

Three parts of the cipher text agree with independent clear text on the same card. “Rákospalotán” in row 6 matches the return address, “Árokszállás” in rows 16–17 matches the address block, and “czím” in row 18 stands directly before the name and the clear return address, where the label is expected.

## Key

Hungarian, simple monoalphabetic substitution with invented graphic signs. The names below are conventional descriptions of handwritten shapes.

| Sign | Plain | Sign | Plain | Sign | Plain |
|---|---|---|---|---|---|
| two bars | a | section mark | k | F-like | r |
| six | b | wave | l | right bowl | s |
| left bowl | c | three short strokes | m | gamma/corner | t |
| long + short stroke | d | two short strokes | n | plain cross | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross + | f | long + short stroke | h / p | low descender | y |
| open loop with descender | g | dotted crossed curve | i | crossed diagonal with tail | z |
| inverted T | j | opposed bowls | cs | | |

Dots or a double tick over o give ö/ő, and a single tick over bars gives é/á. “gy” is written as two signs, g + y. There are 361 cipher signs of 22 types on the card, and none falls outside the key. The long + short stroke class covers d, h and p, which this hand does not separate reliably: each is chosen by the word it makes. The letters c and f each occur only once here, so this card alone does not confirm those two values; they come from the family key.

## Plaintext

Literal decipherment, row by row. `[x]` is a sign overwritten or partly lost, `{del}` the writer's deletion, `{smear}` the smeared stretch.

```text
01 szeretetedesjolakamki          11 lankamhogymulat[o]t
02 vanomhogyjoegéseg              12 vasarnapénbenvoltam
03 bentaljasoraimtu               13 pesten{del}bélval
04 datomhogymárél                 14 töltöltötemad[e]lutant
05 jötemszentmihajrol             15 kedvesjolankamirjon
06 ésmostrakospalota[n]           16 hogymiujság[a]rok
07 dolgozomésittisla              17 szalasbaedesebecses
08 komerölmegbövennemir           18 soraitvarva[c]zim
09 hatokmertcsakszomba            19 holesferi   + in clear: Rakos Palota
10 tontudoktobetkedvesjo          20 in clear: Tavasz u 2 sz
stamp field: is[t]enve / le{smear}leéde / sem / csoko / lomszam / talanszor
```

Normalized Hungarian (word division, accents, spelling and punctuation are editorial):

**Szeretett édes Jolánkám! Kívánom, hogy jó egészségben találja soraim. Tudatom, hogy már eljöttem Szentmihályról, és most Rákospalotán dolgozom, és itt is lakom. Erről meg bőven nem írhatok, mert csak szombaton tudok többet. Kedves Jolánkám, hogy mulatott vasárnap? Én benn voltam Pesten, Bélával töltöttem a délutánt. Kedves Jolánkám, írjon, hogy mi újság Árokszállásba[n]. Édes, e becses sorait várva. Cím: Holes Feri, Rákos Palota, Tavasz u. 2 sz.**

**Under the stamp: Isten vele … édesem! Csókolom számtalanszor.**

English:

> My beloved sweet Jolánka! I wish that these lines of mine find you in good health. I am letting you know that I have already left Szentmihály, and I now work at Rákospalota and live here too. I cannot write at length about this, because only on Saturday can I [write/tell] more. Dear Jolánka, how did you enjoy yourself on Sunday? I was in town, in Pest, and spent the afternoon with Béla. Dear Jolánka, write and tell me what is new in Árokszállás. Sweet one, awaiting these precious lines of yours. Address: Holes Feri, Rákospalota, Tavasz utca 2.
>
> Under the stamp: Farewell … my darling! I kiss you countless times.

Slovak:

> Moja milovaná, sladká Jolánka! Želám si, aby Vás moje riadky zastihli v dobrom zdraví. Oznamujem Vám, že som už odišiel zo Szentmihályu a teraz pracujem v Rákospalote a aj tu bývam. Obšírne o tom nemôžem písať, lebo až v sobotu budem môcť [napísať] viac. Milá Jolánka, ako ste sa zabávali v nedeľu? Ja som bol v meste, v Pešti, a popoludnie som strávil s Bélom. Milá Jolánka, napíšte, čo je nové v Árokszállási. Sladká, čakajúc na tieto Vaše vzácne riadky. Adresa: Holes Feri, Rákospalota, Tavasz utca 2.
>
> Pod známkou: S Bohom … moja drahá! Bozkávam Vás nespočetnekrát.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1309/work/decode.py
```

The command checks the SHA-256 of both scans in source/ and both originals in work/hires/, decodes work/ledger.txt with the key above, and prints the literal rows and then work/normalized.txt. The ledger is a manual transcription and the normalized text is editorial.

## Uncertainties

**Unread**

- **Row 13.** The writer struck out a stretch with two lines. It begins j, o and is not read. The dotted i at its end is crossed by the lower line and is treated as deleted; kept, it would give “ibélval”, no word.
- **Stamp field, row S2.** After “le” (completing “vele”) a red smear covers a stretch, and “le” is then written again before “édesem”. I cannot say what stood there or whether the second “le” is a repeat. An enhanced channel also shows a hook-like sign and a long bar lower down, between S2 and S3: remains of further signs or set-off, unread. The normalization shows an ellipsis.

**The surname**

- **Holes (row 19).** On this card the first sign is only the d/h/p class. H comes from HCP 1303, another Feri card, which has in plain pencil “cím Holes” followed by a faint word. The review of HCP 1303 sees that word beginning “Fe…” and notes that the capital of “Holes” is not a textbook H and looks somewhat like this hand's J. The sign on this card excludes J, since cipher j is the inverted T, so the two cards support each other. HCP 1296 is signed in plain writing [H?]al[o/e]s Ferenc, a weaker parallel. That these are one man is likely, not proved.

**Calls that rest on word sense**

- **d/h/p.** “dolgozom” (row 7), “délutánt” (row 14), “Rákospalotán”, “Pesten” and “Szentmihály” (h written with the short stroke first) are each decided by the word.
- **Row 6, last sign.** Two strokes, the second short: n by sense (“Rákospalotán”), though the shape is close to the d/h/p class, neither of which gives a word.
- **Row 3, s of “soraim”.** A right bowl touched by the loop of the i in the row above, so that it resembles a k. “találja soraim” is the family formula (HCP 1213, 1217, 1315, 1317).
- **Row 7, final a of “la|kom”.** Two bars, but a red dot on the divider rule sits where a third would fall. Three bars would give “lekom”, no word.

**Overwritten or damaged signs**

- **Row 11, o of “mulatott”.** Loop visible under a heavy overwrite.
- **Row 14, e of “délutánt”.** Three bars over an earlier sign, apparently o. A pale blot touches the a of “-tánt”.
- **Row 16, a of “Árokszállás”.** Not a clean a: two bars with slanted strokes between them, a #-like block. A similar block stands in “számtalanszor” (S6), where a is required. The g before it is written over another sign, probably a six.
- **Row 18, c of “czím”.** An over-inked left bowl with a dot to its left, recovered from sense. HCP 1303 has the same word in clear before a name.
- **Stamp field.** The t of “Isten” is smeared, the lower part of the last o of “számtalanszor” is rubbed off, and the r stands on the perforation line.

**Language and facts**

- The writer's spelling is normalized, for example “jolakam” → Jolánkám (n omitted), “talja” → találja, “bövennem” → bőven nem, “bélval” → Bélával, “töltöltötem” → töltöttem (dittography), and “szalasba” → (Árok)szállásba[n], which he may have meant as written in spoken Hungarian.
- “Szombaton tudok többet” has no infinitive on the card; “írni” or similar is understood, and is bracketed in the translations.
- “Édes e becses sorait várva”: taken as “Édes, e becses sorait várva”. The alternative is a stray e before “becses”, with the same sense.
- Szentmihály is presumably Rákosszentmihály, next to Rákospalota, but the card does not say which one.
- The date is not legible, and no year is claimed from the card itself.

## Review summary

Reviewer: Claude Opus 5.5 (Anthropic), a separate agent, round 1, verdict **REVISE**. It confirmed the command's output and all hash checks, and decoded its own sign transcription from its own crops with a key retyped from HCP 1216: 25 rows, 0 differences, 361 signs. That comparison was not blind, since it had read the ledger first. It also confirmed each restoration against enlargements, the language, and the absence of an attached solution on the portal. It did not search further for a published solution.

Seven findings, and what changed:

- **Surname (major).** The handover wrongly said no sister card gives the surname and reported {H|P|D}oles. It is now “Holes”, with its basis stated as above.
- **Row 7, final a.** Now listed as resting on sense.
- **Stamp field.** The residue below S2 is now disclosed.
- **Accents.** The tick of “már” was added to the ledger and the literal row; the é of “eljöttem” was added to the spelling list.
- **Formula citation.** HCP 1212 was dropped, since “találja soraim” does not occur there.
- **Postmarks.** Both strikes are now described as unread.
- **Normalization.** “bőven nem” replaces “bővebben nem”, closer to the card, and the translations follow it.

Two descriptions were also corrected from the review's checks: the sign touching the s in row 3 is the i of row 2, and the row 16 sign is a #-like block rather than a plain over-inked a. No decoded letter changed. The reviewer could not verify what stood under the deletion, the smear or the overwrites, the date, either postmark, or which Szentmihály is meant.

## Credits

- **Claude Opus 5.5, 2026-10-30:** transcription (sign ledger), decipherment, response to review and this report. Source capture for this card was done by a Claude Opus 5.5 orchestrator.
- **Family key:** from the finished Jolánka cards, on which earlier work was done by the OpenAI GPT solver and completed by Claude Opus 5.5 where stated on those cards.
- **Claude Opus 5.5, separate reviewer agent:** independent review.

## Sources

- HC Portal record 1309, General, Description and Attachments tabs, captured 2026-10-30: https://crypto.hcportal.eu/dashboard/cryptograms/1309 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/3987/conversions/cpc_1912--_HU__HU_Jasz-Arokszalas_jolanka-99_pic-large.jpg (source/picture-large.jpg); original https://api.hcportal.eu/media/3987/cpc_1912--_HU__HU_Jasz-Arokszalas_jolanka-99_pic.jpg.
- Address side: https://api.hcportal.eu/media/3988/conversions/cpc_1912--_HU__HU_Jasz-Arokszalas_jolanka-99_adr-large.jpg (source/address-large.jpg); original https://api.hcportal.eu/media/3988/cpc_1912--_HU__HU_Jasz-Arokszalas_jolanka-99_adr.jpg.
- Family key: ciphers/hcp-1216/SOLUTION.md.
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-30: no record for this card.
