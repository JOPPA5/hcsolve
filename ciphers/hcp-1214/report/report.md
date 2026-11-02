# HCP 1214 (cpc_--_HU__HU_helyben (locally) Budapest_jolanka-63): Feri's farewell to Jolánka Tóth

Human solver: Tomáš Pavuk

**Status: deciphered in full (all 18 rows); two signs of one word (fájdalom) are read by sense and disclosed below. Independent review 1 verdict REVISE; all six findings addressed, one letter removed from the salutation.** Report dated 2026-11-02.

## Origin and context

The cryptogram is record 1214 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1214), portal name cpc_--_HU__HU_helyben (locally) Budapest_jolanka-63. It belongs to Tobias Schrödel's cryptographic postcard collection (private collection). When captured on 2026-11-02 the portal listed it as **Not solved**, tagged Postcard, T. Schrödel Collection, category Substitution, language Unknown, sender Unknown, recipient Tóth Jolánka, with no transcription or solution attached.

The address is in plain writing: **Szépreményű Tóth Jolánka kisasszonynak, Helyben** ("To the promising Miss Jolánka Tóth, Local"). The word Helyben means the card was posted for delivery in the same town; which town is not stated on the card. A green Hungarian 5 fillér stamp is in place and its postmark is not legible, so the card has no date. The picture side has only printed matter (no. 2541) and the collection stamp; nothing shows around the stamp edges.

The whole message is on the left of the address side, in 18 rows of invented signs, and it is signed Feri. The card belongs to the family of cipher postcards addressed to Jolánka Tóth, several of which were deciphered earlier in this repository (HCP 1212, 1213, 1216, 1217, 1218, 1243, 1301).

![Address side with the 18 cipher rows on the left (source/address-large.jpg)](../source/address-large.jpg)

![Picture side, with no cipher text (source/picture-large.jpg)](../source/picture-large.jpg)

## Method

The key was **transferred unchanged** from the finished sister card HCP 1216; it is not a new key recovery for this card. The rows slope about 3.5 degrees, so the un-converted original scan was deskewed and cut into enlarged bands before the rows could be separated. Each sign was then read by eye and recorded in a manual sign ledger (work/ledger.txt, 18 rows, 233 tokens). There is no OCR, and sense guided the h/p calls, as stated below. A small script checks the hashes of the image files and decodes the ledger.

The family key turned every row into continuous Hungarian. The only sign outside the family classes is the upright T at the end of row 10. No key letter was changed for this card.

## Key

Simple monoalphabetic substitution with invented graphic signs (type MASC); the labels are conventional names for handwritten shapes.

| Sign | Letter | Sign | Letter | Sign | Letter |
|---|---|---|---|---|---|
| two bars | a | section mark | k | F-like | r |
| six | b | wave | l | right bowl | s |
| left bowl | c | three short strokes | m | gamma/corner | t |
| long stroke + short tick on its left | d | two short strokes | n | plain heavy x | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross + | f | tall stroke + tick on its right | h / p | low descender | y |
| open loop with descender | g | dotted crossed curve | i | crossed diagonal with tail | z |
| inverted T | j | joined loop + descender | gy | opposed bowls | cs |

Dots or ticks over o and u give ö and ü. Other accents are mostly not visible and are supplied in normalization.

## Plaintext

Literal decipherment row by row. Square brackets mark a restoration under a blot, curly brackets a sign discussed below, and {#} the overwritten sign in row 7.

```text
01 kedvesjolanka            10 kerülnihafa{j}
02 marlatomközel            11 {d}alommegkel
03 alokahozhogy             12 tenemsziböl
04 kiutasitnakhazok         13 kivanomlegy{e}n
05 bolbocsasonmeg           14 boldogboldogit
06 nekemmerta[z]t           15 saazatud[a]thogy
07 önitudja{#}hogy          16 megtörtegy
08 mijnehezemre             17 szivetistenvele
09 esikbecsehazokot         18 voltkedvesseferi
```

**Hungarian (normalized):** Kedves Jolánka! Már látom, közel állok ahhoz, hogy kiutasít[a]nak házukból. Bocsásson meg nekem, mert azt Ön i[s] tudja, hogy mily nehezemre esik becse[s] házukat kerülni, ha, fájdalom, meg kell tennem. Szívből kívánom, legyen boldog, boldogítsa az a tudat, hogy megtört egy szívet. Isten vele! Volt kedvese, Feri.

**English:** Dear Jolánka! I see now that I am close to being turned out of your family's house. Forgive me, for you too know how hard it is for me to keep away from your esteemed house when, alas, I must do so. I wish with all my heart that you be happy; may the knowledge that you have broken a heart make you happy. Farewell! Your former sweetheart, Feri.

**Slovak:** Milá Jolánka! Už vidím, že som blízko k tomu, že ma vykážu z vášho domu. Odpusťte mi, lebo aj Vy viete, ako ťažko mi padne vyhýbať sa vášmu ctenému domu, keď to, žiaľ, musím urobiť. Zo srdca Vám želám, aby ste boli šťastná; nech Vás teší vedomie, že ste zlomili jedno srdce. S Bohom! Váš bývalý milý, Feri.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1214/work/decode.py
```

The command checks the SHA-256 of all four image files, decodes work/ledger.txt and prints the literal rows and the normalized text.

## Uncertainties

- **Rows 10 to 11, "ha, fájdalom"** is the weakest point. The last sign of row 10 is an upright T, unique on this card, and the first sign of row 11 has the h/p shape, not the d shape. Reading them as j and d gives fájdalom, spelled out as fajdalmam on HCP 1216. By shape alone the letters are hafat halom, which makes no sentence. So two signs of this word rest on sense. "Alas" is the literary interjection use of the word; this comes from language knowledge and was not checked against a period source. If it is the noun "pain", the letters do not change.
- **Row 10 "ha":** a third short stroke stands below the two bars of the a, so the sign could be an uneven e. That gives no word; a is chosen by sense.
- **h against p** is chosen by word sense throughout (ahoz, házok-, nehezemre, hogy).
- **Row 1:** two strokes after the final a are not a letter. They are the diaeresis of the ö directly below them in row 2.
- **Blots:** the z of azt (row 6) and the a of tudat (row 15) are restorations under ink blots; only an outline and one bar show.
- **Row 7:** a sign is overwritten after tudja. It may be a separate cancelled sign or the corrected h of hogy; the word is hogy either way.
- **Row 13:** the last vowel of legyen touches the tail of the y and its bar count is unclear; e by sense. The second sign of kívánom is thick and z-like, but a separate dot makes it i.
- **Writer's spellings normalized:** i to i[s] and becse to becse[s] (the s is not on the card), kiutasitnak to kiutasít[a]nak, házok- to házuk-, alok, ahoz, kel, tenem, bocsason with single consonants, mij to mily, sziböl to szívből (v dropped), kedvesse to kedvese. "Their house" is an interpretation of házok-.
- **Word division** is editorial. The subject "you" of megtört is an interpretation: the verb is third person.
- **Sender and date:** this Feri is probably the Feri of HCP 1212, 1213 and 1216 (same key and addressee), but that is not proven. The date and the town are unknown.

## Review summary

A separate Claude Opus 5.5 reviewer ran the command, made its own sign-class transcription from the original scan, decoded it with its own script and compared it with the ledger. The two agreed except for the row 1 and row 14 points below. Its verdict was REVISE, with six findings:

1. (major) The final m of "Jolánkám" in row 1 was not on the card. The strokes are the diaeresis of the row 2 ö, so the salutation became Kedves Jolánka!
2. (minor) "ha fájdalom" was retranslated: one sentence with "alas" replaced a loose "painful though it is".
3. (minor) The third stroke under the row 10 a was added to the uncertainties.
4. (minor) The description of the row 7 overwritten sign was softened.
5. (minor) The second d of boldog in row 14 was over-flagged and is now a plain d.
6. (minor) gy and cs were added to the key table so that it matches the ledger.

The key, the 18 rows and the sense of the letter did not change, so no second review round was needed. The reviewer could not verify the identity of Feri, the place behind Helyben or the date, and it took faint specks between rows 16 and 17 to be paper marks without being able to prove it.

![Reviewer's comparison: panel 1 shows the row 1 strokes directly above the row 2 o; panel 4 shows the matching pair on the row 12 ö (review/work/umlauts.png)](../review/work/umlauts.png)

## Credits

Source capture, transcription, key transfer and decipherment by Claude Opus 5.5; independent review by a separate Claude Opus 5.5 agent. The key comes from the finished sister cards of this family, on which earlier work was done by OpenAI GPT agents and Claude Opus 5.5. No published solution of this card was found or used.

## Sources

- HC Portal record: https://crypto.hcportal.eu/dashboard/cryptograms/1214
- Collection reference given by the portal: https://ecp.ep.liu.se/index.php/histocrypt/article/view/166
- Scans and hashes: SOURCES.md in this directory
- Key: ciphers/hcp-1216/SOLUTION.md
