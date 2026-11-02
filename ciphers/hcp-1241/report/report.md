# HCP 1241 (cpc_1912-05-12_HU__HU_Jasz Arokszalas_jolanka-20): Feri to Jolánka Tóth, "destroy my lines"

Human solver: Tomáš Pavuk

**Status: complete reading of 20 cipher rows (290 written signs in the ledger; one restored and one doubtful), plus the plain-script parts; independent review 1 verdict ACCEPT, no change to the decoded letters.** Report dated 2026-11-02.

## Origin and context

The cryptogram is record 1241 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1241), portal name cpc_1912-05-12_HU__HU_Jasz Arokszalas_jolanka-20, part of Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-11-02 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, category Substitution, language Unknown, sender Unknown, recipient Tóth Jolánka, with no transcription or solution attached. The portal links a HistoCrypt article (https://ecp.ep.liu.se/index.php/histocrypt/article/view/166), which was not opened for this work. No published solution of this card is known to us.

It is a Hungarian picture postcard of a couple embracing, with swallows, the printed heading "Fecském hova szállsz?" and a printed four-line verse beginning "Valamikor réges-régen". The picture side has no handwriting.

All the writing is on the address side, in red ink. The left half holds twenty rows of invented graphic signs. The last row runs on into plain script along the bottom edge and up the right edge ("tiszteltetem a kedves mamáját"). The square meant for the stamp holds a plain farewell, and the address is plain too: **Szép reményű / Tóth Jolánka / úrleánynak / Jász Árokszállás** ("to Miss Jolánka Tóth, of fair promise", Jászárokszállás, Hungary).

The card belongs to the Jolánka family of postcards to the same addressee. Several are finished in this repository: HCP 1216 (fullest legend), 1212, 1213, 1217, 1218, 1243 and 1301. This card was therefore read with a **known, transferred key**. It is not a new key recovery. The writer signs as Feri on the sister card HCP 1216 and in abbreviated form here. His full identity is not known.

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side: twenty cipher rows at the left, plain text in the stamp square, along the bottom and up the right edge (source/address-large.jpg)](../source/address-large.jpg)

## Method

The transcription is **manual**. The solver read each row sign by sign from 2x to 5x crops of the un-converted original scan (3445 × 2210 pixels, kept in work/hires/) and recorded one token per written sign in work/ledger.txt. No OCR was used and the portal supplied no transcription. The key was taken unchanged from HCP 1216. All identifiable signs fall into its classes, and no sign needed a new value.

The ledger names tokens by their plaintext letters, so the reproduction command below **reproduces the reading but does not prove it**. The evidence lies elsewhere. A key fixed on other cards gives continuous grammatical Hungarian here. And the reviewer read the whole card independently, under neutral sign names, and decoded it with a key rebuilt from the HCP 1216 files. That pass agreed with the solver in all 20 rows, leaving aside the two open signs and treating h/p as one class. It was not blind, because the reviewer had read the solution first.

Two pairs of signs are near-homographs. h and p share a sign class, and p was chosen only in megkaptam and vasárnap, on word sense. d and h/p use the same two strokes in opposite order, and the d calls were made on the strokes.

## Key

Simple monoalphabetic substitution with invented graphic signs (register label MASC). Descriptions are conventional names for the handwritten shapes.

| Sign | Plain | Sign | Plain | Sign | Plain |
|---|---|---|---|---|---|
| two bars | a | section mark | k | F-like | r |
| six | b | wave | l | right bowl | s |
| left bowl | c | three short strokes | m | gamma/corner | t |
| short stroke then long stroke | d | two short strokes | n | plain cross x | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross + | f | long stroke then short stroke | h / p | low descender | y |
| open loop with descender | g | dotted crossed curve | i | crossed diagonal with tail | z |
| inverted T | j | joined loop + descender | gy | opposed bowls | cs |

Two dots over o give ö. An acute stroke is often visible on e, a and o. Most accents are not written; those in the normalized text are editorial.

## Plaintext

Literal decipherment, row by row. A point is a written point; {b?} is the doubtful sign and [s] the restored one.

```text
01 dragacsillagombecses
02 soraitmegkaptammely
03 nagyörömemszol
04 galtmelymeggyöz
05 tefajoszivemet
06 arrolhogyszeret
07 semisitsemegso
08 raiméstegyen
09 ugyminthanem
10 tortetvolna
11 semiésénisugy
12 teszekezekutan
13 megnagyóbbsze
14 retettelfordulok
15 önhözédesegyetlen
16 reményem.hogytelt
17 elvasárnap.tavol
18 {b?}ogondolenéha
19 ramtalándudasju
20 li[s]kabeszélteteleafejét
```

Plain script after row 20: tiszteltetem a kedves mamáját

Plain script in the stamp square: Isten vele / édesem / továbbra / is hűke[d] / vese cso- / kolom / szamtalan- / szor Fe[ri]

Normalized Hungarian (punctuation and most accents are editorial; square brackets mark letters not on the card):

**Drága csillagom! Becses sorait megkaptam, mely nagy örömem[re] szolgált, mely meggyőzte fájó szívemet arról, hogy szeret. Semmisítse meg soraim[at] és tegyen úgy, mintha nem törté[n]t volna semmi. És én is úgy teszek. Ezek után még nagyobb szeretettel fordulok önhöz, édes egyetlen reményem. Hogy telt el vasárnap? Távolbó[l] gondol-e néha rám? Talán Dudás Juliska beszélte tele a fejét. Tiszteltetem a kedves mamáját.**

**Isten vele, édesem. Továbbra is hű ke[d]vese. Csókolom számtalanszor. Fe[ri]**

English translation: **My dear star! I have received your valued lines, which gave me great joy and convinced my aching heart that you love me. Destroy my lines and act as if nothing had happened. I will do the same. After this I turn to you with even greater love, my sweet only hope. How did Sunday go? From afar, do you think of me sometimes? Perhaps Juliska Dudás has filled your head with talk. Give my respects to your dear mother.**

**God be with you, my darling. Still your faithful sweetheart. I kiss you countless times. Feri**

Slovak translation: **Moja drahá hviezda! Vaše vzácne riadky som dostal a urobili mi veľkú radosť a presvedčili moje boľavé srdce o tom, že ma ľúbite. Zničte moje riadky a správajte sa, akoby sa nič nestalo. Aj ja urobím to isté. Po tomto sa na Vás obraciam s ešte väčšou láskou, moja sladká jediná nádej. Ako ste prežili nedeľu? Myslíte niekedy z diaľky na mňa? Azda Vám Juliska Dudásová nahovorila plnú hlavu. Pozdravujte odo mňa Vašu milú mamu.**

**S Bohom, drahá. Naďalej Váš verný milý. Bozkávam Vás nespočetnekrát. Feri**

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1241/work/decode.py
```

The script uses only the Python standard library. It checks the SHA-256 hashes of both scans in source/ and both originals in work/hires/, decodes the manual ledger work/ledger.txt with the family key, prints the twenty literal rows and prints the normalized text from work/normalized.txt. It does not read the images.

## Uncertainties

- **Row 20, third sign (restored).** A blot-filled oval with a light interior and a crescent outline bulging to the lower right. That suits a bled right bowl (s, giving Juliska), the likeliest form. It is also about as wide as the opposed-bowl cs, so a diminutive like "Julicska", unattested here, cannot be excluded on the pixels. The person is a Julia either way.
- **Row 20, second sign.** The dotted i looks like a cross because the ink has spread, but the dot is clear and the blot shows a light spot where the loop of the i sign would be. The plain cross in fejét has neither.
- **Row 18, first sign (doubtful).** A thin diagonal with a flag at the top and a loop at the base. The four sixes on this card have a curved stem and no flag, so b is a call from sense, not from shape. It completes row 17 as távol|bó[l], "from afar", with the final l dropped. That l-drop is known in Hungarian dialects, but its attribution to this writer is an interpretation. The sentence still reads if the sign is left open.
- **The name Dudás Juliska.** Read from the signs and context. In Dudás the sense does not help, so the two d signs rest on the stroke order. She appears on no other finished card in this repository and nobody is identified.
- **Writer's omissions and spellings.** örömem[re] (the -re is supplied), soraim[at], törté[n]t (the card has t o r t e t, so only the n is missing, plus the ö dots and the é accent), semi for semmi, semisitse for semmisítse, nagyóbb for nagyobb.
- **Plain script.** The d of ke[d]vese is smeared, and only F and e of the signature are visible, the rest lying under a pink blot; it is restored as the signature on HCP 1216. The final t of mamáját lies in a pink blot and the final n of "szamtalan" runs into one. "hű" and "reményű" are written with two dots, like ü, and are normalized to ű. The middle of "továbbra" is written loosely, and the phrase "továbbra is" fixes it. The end of "Jolánka" runs into the postmark.
- **Date.** The portal file name gives 1912-05-12. The postmarks show MÁJ and a year ending 12, but the day is not established: one mark ends in a clear 0 with something obscured before it, the other shows 1 and a second digit that may be 9, 3 or 7. "vasárnap" therefore cannot be tied to a date.
- **Sense.** The card does not say what must be destroyed or what happened before. "Destroy my lines" is the literal reading of semmisítse meg soraim; the reason is unknown.
- **Prior publication.** The check rests on the portal status and the AI Decipherment Register as of 2026-11-02. The linked HistoCrypt article was not opened.

## Review summary

Reviewer: a separate Claude Opus 5.5 agent, round 1, verdict **ACCEPT**. The reviewer ran the reproduction command, read the whole card from its own crops under neutral sign names, decoded that reading with a key rebuilt from the HCP 1216 files (no row differed), checked every row and the word-deciding signs on the pixels, and checked the language, translations and sources. Its seven findings were all minor:

- **Row 17 point.** A written point after vasárnap was missing from the ledger. Added; it supports the sentence break.
- **Row 20 blot.** The cs alternative is now disclosed and Juliska is presented as the likeliest form.
- **Row 18 first sign.** Now stated as a call from sense, and kept marked as doubtful.
- **törté[n]t.** Corrected: only the n is restored, not "én".
- **Key table.** The d and h/p rows now give the stroke order that these calls rest on.
- **Plain-text restorations.** The t of mamáját, the n of szamtalan and the ü-to-ű normalization are now listed.
- **Decoder.** It is close to an identity map, as the Method section here says. No change.

**No decoded letter changed as a result of the review.** The solver also looked at the postmarks again and recorded what each one shows, without settling the day. Transcription, key transfer, decipherment and this report are by Claude Opus 5.5; there was no earlier work on this number.

## Sources

- HC Portal record 1241, General, Description and Attachments tabs, captured 2026-11-02: https://crypto.hcportal.eu/dashboard/cryptograms/1241 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/3783/conversions/cpc_1912-05-12_HU__HU_Jasz-Arokszalas_jolanka-20_pic-large.jpg (source/picture-large.jpg); original https://api.hcportal.eu/media/3783/cpc_1912-05-12_HU__HU_Jasz-Arokszalas_jolanka-20_pic.jpg
- Address side: https://api.hcportal.eu/media/3784/conversions/cpc_1912-05-12_HU__HU_Jasz-Arokszalas_jolanka-20_adr-large.jpg (source/address-large.jpg); original https://api.hcportal.eu/media/3784/cpc_1912-05-12_HU__HU_Jasz-Arokszalas_jolanka-20_adr.jpg
- Family key: ciphers/hcp-1216 and the other finished Jolánka cards in this repository.
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-11-02.
