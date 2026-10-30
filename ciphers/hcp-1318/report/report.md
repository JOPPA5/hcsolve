# HCP 1318 (cpc_1913--_HU__HU_Jasz Arokszalas_jolanka-111): Feri to Jolánka Tóth

Human solver: Tomáš Pavuk

**Status: deciphered in full (398 written signs in 21 main rows and 7 rows under the stamp; a few signs under a stain are restored from word sense, see Uncertainties); independent review 1 verdict REVISE, findings addressed, no word of the normalized text changed.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1318 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1318), portal name cpc_1913--_HU__HU_Jasz Arokszalas_jolanka-111, part of Tobias Schrödel's collection of cryptographic postcards. When it was captured on 2026-10-30 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, category Substitution, date Unknown, language Unknown, location Europe, sender Unknown, recipient Tóth Jolánka, with no transcription or solution attached. The year 1913 appears only in the file name; the postmarks on the card could not be read.

The picture side, scanned sideways, is a tinted studio photograph of a young couple standing beside a wicker chair. It carries no cipher text. The whole message is on the address side, written in red ink in invented signs: 21 rows across the left half of the card and 7 short rows in the space under the stamp, which has been torn off. A purple stain covers a few signs in rows 7–9.

The address is in plain writing: Szépremény[ű] (running into the postmark) / Tóth Jolánka / úrleánynak / Jászárokszállás, that is, "To the promising young lady Jolánka Tóth, Jászárokszállás".

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side with the cipher text, the stain, the stamp space and the plain address (source/address-large.jpg)](../source/address-large.jpg)

The card belongs to the "Jolánka" family of Hungarian cipher postcards addressed to Jolánka Tóth, several of which are deciphered in this repository (HCP 1212, 1213, 1216, 1217, 1218, 1243, 1301). They share one key, and this card is signed Feri, as HCP 1216 is. The card was therefore read with a **known, transferred key**, not by a new key recovery. No reading of this particular card was supplied or consulted, and no published solution was found.

## Method

The key was taken unchanged from HCP 1216. The work was a careful transcription of the signs.

- **Solution (2026-10-30), Claude Opus 5.5:** every row was read from 3–4× enlargements of the un-converted original scan (3445 × 2210 pixels) and recorded by hand as a sign ledger, one token per written sign (`work/ledger.txt`). No OCR was used, and the reading was not blind, since word expectations guided the difficult signs. The command `python3 -I ciphers/hcp-1318/work/decode.py` checks the hashes of the image files and prints the literal text and the normalized text.
- **Review (2026-10-30), a separate Claude Opus 5.5 agent:** re-ran the command, made its own crops and its own transcription by sign class, and decoded it through the family key file of HCP 1216 rather than the solver's table. Its transcription was made knowing the solver's text, so it is a check and not a blind reading. It differed in one sign of 398 (see Review).

There was no earlier GPT work on this number.

The writer spells carelessly and drops letters. The literal decipherment is kept as written; the normalized Hungarian below is editorial.

## Key

Hungarian simple monoalphabetic substitution with invented signs. The names are conventional descriptions of the handwritten shapes.

| Sign | Letter | Sign | Letter | Sign | Letter |
|---|---|---|---|---|---|
| two bars | a | section mark (S / 8 forms) | k | F-like | r |
| six | b | wave | l | right bowl | s |
| opposed bowls | cs | three short strokes | m | gamma (arm sometimes detached) | t |
| tick + long stroke | d | two short strokes | n | plain X | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross + | f | long stroke + tick at right | h / p (here also d) | low looped sign | y |
| ς-shaped descender | g | dotted crossed curve | i | X with long arm or tail | z |
| inverted T | j | | | | |

On this card gy is written as two signs (g + y) and sz as s + z. Accents are marks over the base sign; only the acutes on e and the two dots of többet were clearly seen.

## Plaintext

Literal decipherment, row by row (`[x]` = seen only through the stain or hidden, `x?` = value rests on word sense; rows s1–s7 stand under the stamp):

```text
01 kedvesjolankamtudatom
02 hogyszerencsésenmegér
03 keztem.ijenkorérzém
04 csakhogymitvesztek
05 enjolankambaelijenkor
06 ismikorelkelvalaunk
07 egymast?[o]lszeretném
08 szivemé[r][z]elmeitbeol
09 tanieze[n][é]desjolankamszi
10 vebéakorjolankamisugy
11 vonzodnah?ozammint?én
12 magahozacsomakotat
13 adtamsand?ornakabéla
14 valnembeszelhetem
15 mertnemvoltidom
16 d?emostnemirok
17 többetmertmeral
18 mosvagyokisten
19 velédesem
20 mindenkielhitte
21 hogykatonavagyok
s1 csokol
s2 lom
s3 szam
s4 talan
s5 szor
s6 imado
s7 jaferi
```

Normalized Hungarian (`[n]` = letter supplied by the editor):

Kedves Jolánkám! Tudatom, hogy szerencsésen megérkeztem. Ilyenkor érzem csak, hogy mit vesztek én Jolánkámba[n] el. Ilyenkor is, mikor el kell válnunk egymástól, szeretném szívem érzelmeit beoltani ezen édes Jolánkám szívébe, akkor Jolánkám is úgy vonzódna hozzám, mint én magához. A csomagot átadtam Sándornak, a Bélával nem beszélhettem, mert nem volt időm. De most nem írok többet, mert álmos vagyok. Isten vele, édesem. Mindenki elhitte, hogy katona vagyok.

Under the stamp: Csókolom számtalanszor. Imádója Feri.

## Translation

**English.** My dear Jolánka! I let you know that I have arrived safely. Only at such times do I feel what I am losing in my Jolánka. Even at times like this, when we must part from each other, I would like to implant the feelings of my heart into this sweet Jolánka's heart; then my Jolánka too would be as drawn to me as I am to you. I handed the parcel over to Sándor; I could not speak with Béla, because I had no time. But I will not write more now, because I am sleepy. God be with you, my sweet. Everyone believed that I am a soldier.

Under the stamp: I kiss you countless times. Your adorer, Feri.

**Slovak.** Moja milá Jolánka! Oznamujem Vám, že som šťastne docestoval. Až v takých chvíľach cítim, čo v mojej Jolánke strácam. Aj v takejto chvíli, keď sa musíme rozlúčiť, by som chcel vštepiť city svojho srdca do srdca tejto sladkej Jolánky; potom by aj moja Jolánka ku mne tak inklinovala, ako ja k Vám. Balík som odovzdal Šándorovi, s Bélom som sa nemohol porozprávať, lebo som nemal čas. Ale teraz už viac nepíšem, lebo som ospalý. S Bohom, moja sladká. Všetci uverili, že som vojak.

Pod známkou: Bozkávam Vás nespočetnekrát. Váš ctiteľ Feri.

## Uncertainties

Signs resting on word sense, or hidden:

- **The h-form as d.** The tall stroke with a tick at right is normally h, but must be d in Sándornak (row 13) and de (row 16). The regular d has the tick at left. HCP 1216 has the same de.
- **Stain, row 7.** One sign between t and l is covered and restored as o (egymástól); a faint top arc fits a cursive o, weakly. The t has a tiny stub under its arm. If the stub were a real bar the sign would be F, giving egymásról ("about each other"), which does not fit the sentence.
- **Stain, row 8.** Two signs are covered and restored as r, z (érzelmeit), the only fitting word before -elmeit. Enhanced crops show an arm and stem consistent with F (r) and a vertical consistent with z, but the z could not be identified from it alone.
- **Stain, row 9.** Two faint strokes (n of ezen) and two faint bars (read é of édes, a contextual value, since no acute or third bar is seen) show through the stain. The d after them has its long stroke and left tick. A short mark above the e of eze- may be an acute or a stray and changes nothing.
- **Row 11.** The h of hozzám is an overwritten bold 8-like sign with a separate tick; as it stands it looks like k. The t of mint is cramped and looks like a chevron. In both the sense is secure but the sign is not clean.
- **Row ends.** The final i of row 9 and of the signature Feri show no visible dot. The first signs of row s4 are tangled with row s5. The wave at the start of row s2 is faint, but the word is csókolom either way.

Writer's spellings, all signs clear, normalized in the Hungarian above:

- ijen → ilyen; Jolánkámba → -ban; kel → kell; akor → akkor; hozám → hozzám; beszélhetem → beszélhettem (the sense is past); valaunk → válnunk (a where n is expected); csomakotat adtam → a csomagot átadtam (k where g is expected; the division is editorial); idom → időm (no ő marks seen).
- **Rows 17–18, `mertmeral|mos`.** Read as mert [mer] álmos: mert begun again as mer, and álmos split across the row break. Mert már álmos vagyok ("for I am already sleepy"), with e written for á in már, cannot be excluded. It would add only "already" to the translation.
- **Row 19, `velédesem`.** Read as vele, édesem, with one e serving both words.
- **Row 11, magához.** Read as formal "to you" (maga), which fits the formal address on the family's cards. A reader could take it as "to herself".

Not established: the date (1913 rests on the file name), the identities of Sándor and Béla, and whether "katona" (soldier) is a joke or literal.

## Review

The independent reviewer re-ran the command, matched every row of the literal text, decoded its own transcription through the family key file, and read all 28 rows at 2.3× with 4–5× zooms on the disputed signs. It also examined the stain in separate colour channels. It confirmed that all 398 signs decode through the key with no unassigned sign, that the text is ordinary Hungarian of this writer, and that no published solution was used. Its verdict was REVISE, with five findings, all accepted:

- **Major: row 16, sign 8.** The solver's ledger had two bars (a), giving namirok and a supposed slip. The crop shows three bars (e), so the writer wrote nem correctly. The ledger and the literal text were corrected and the slip withdrawn.
- **Minor: row 5, `el`.** The solver had bracketed it as a false start. It is the verb prefix of vesztek (mit vesztek ... el), so the brackets were dropped and the sentence boundary moved. The translations did not change.
- **Minor: rows 17–18.** The solver had rejected mert már álmos too firmly. It is now disclosed as a live alternative.
- **Minor: the stain.** The traces in rows 7–9, the tick of d and an unreported mark above eze- are now described.
- **Minor: the address.** The first line Szépremény[ű] was missing and has been added.

One sign of the literal decipherment changed. No word of the normalized text changed; one sentence boundary moved.

## Credits

- **Claude Opus 5.5, 2026-10-30:** source capture, key transfer, transcription (sign ledger), decipherment, translations, response to review and this report.
- **Claude Opus 5.5, separate reviewer agent:** independent review.

## Sources

- HC Portal record 1318, General, Description and Attachments tabs, captured 2026-10-30: https://crypto.hcportal.eu/dashboard/cryptograms/1318 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/4014/conversions/cpc_1913--_HU__HU_Jasz-Arokszalas_jolanka-111_pic-large.jpg (source/picture-large.jpg), and the un-converted original https://api.hcportal.eu/media/4014/cpc_1913--_HU__HU_Jasz-Arokszalas_jolanka-111_pic.jpg (work/hires/).
- Address side: https://api.hcportal.eu/media/4015/conversions/cpc_1913--_HU__HU_Jasz-Arokszalas_jolanka-111_adr-large.jpg (source/address-large.jpg), and the un-converted original https://api.hcportal.eu/media/4015/cpc_1913--_HU__HU_Jasz-Arokszalas_jolanka-111_adr.jpg (work/hires/).
- Family key: ciphers/hcp-1216/work/graphic-key.json (Jolánka family).
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-30: no record for this card.
