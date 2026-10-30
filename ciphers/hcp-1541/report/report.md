# HCP 1541 (pc_hcp_222): a Czech letter from Pepouš to Anna Tichá, 19 August 1903

Human solver: Tomáš Pavuk

**Status: deciphered; 550 visible cipher signs read with the family key, two letters hidden under the printed picture restored from context, one visible sign of uncertain shape. Independent review 1 verdict REVISE; all five findings addressed, the reading of the letter unchanged.** Report dated 2026-10-29.

## Origin and context

The cryptogram is record 1541 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1541), portal name pc_hcp_222, part of the HCPortal collection of cryptographic postcards (private collection). When it was captured on 2026-10-28 the portal listed it as **Not solved**, tagged Postcard, HCPortal collection, category Substitution, date 1903-08-19, language Czech, location Europe, sender Unknown, recipient Anna Tichá, with no transcription or solution attached.

It is a picture postcard with a painted landscape with dark trees. The card is scanned sideways; turned upright (90° clockwise), the cipher text stands in nineteen rows, and the plain date **19./VIII.1903.** is written below it. The last rows run into the dark printed trees, and in two places a green patch of the picture covers the writing.

The address side is in plain writing: **Velectěná Slečna / Anna Tichá / učitelka t.č. / v Pelhřimově / Vlastnoručně / dodati.** ("Honoured Miss Anna Tichá, teacher at present in Pelhřimov. To be delivered into her own hands.")

The card belongs to a family of cipher postcards to Anna Tichá, a teacher in South Bohemia, in the same hand and the same cipher, signed by "Pepouš" (a pet form of Josef). Many of them are deciphered in this repository (for example HCP 1520–1527, 1545, 1552, 1556). The key was transferred from those cards; a partial key for the family was published earlier by Maxim Egorov (https://maxim-egorov.dev/research/anna-ticha-postcards/). This card was therefore read with a **known, transferred key**; it is not a new key recovery. No reading of this particular card was supplied or consulted.

![Picture side turned upright: nineteen cipher rows and the plain date 19./VIII.1903 (work/upright.png)](../work/upright.png)

![Address side: Anna Tichá, teacher in Pelhřimov (source/address.jpg)](../source/address.jpg)

## Method

The transcription is **manual**: the scan was turned upright, and each of the nineteen rows was read sign by sign from enlarged crops (work/row01.png to work/row19.png); no OCR was used and the portal supplied no transcription. Early guesses that did not match the signs (PANVE, ZNAMY, KRATIL) were rejected on the enlargements in favour of what is written (PAMETNI KNIHY, ZHATIL). The transcription and its sign-by-sign inventory are in work/transcription.txt and work/inventory.json (round-0 state) and work/transcription-final.txt (final state).

The family key decodes every sign except one: a **k-shaped sign** (an ascender with a loop and a kicked leg) in row 11, in the word SVA?RA. It is clearly distinct from the looped sign that means K (as in KTEREHO on the same row). Only G makes a word, *švagra* ("brother-in-law", genitive), and the same sign stands where only G fits on sister cards: SVAGROVA and KOLEGY on HCP 1570 (identified there by that card's independent reviewer) and TELEGRAM- on HCP 1553/1554. The k-shaped sign is therefore read as **G**, the one sign added to the published partial key.

![SVAGRA in row 11: the k-shaped G sign (4th sign), followed by the looped K sign that begins KTEREHO (work/svagra.png)](../work/svagra.png)

The full plaintext is produced by one read-only command, run from the repository root:

```
python3 -I ciphers/hcp-1541/work/decode_final.py
```

It verifies the hashes of the source images and records, checks that the final transcription differs from the audited round-0 transcription only by four documented relabels, applies the key in work/key-final.json, checks that every key sign is used, and prints the literal plaintext.

## Key

Simple monoalphabetic substitution (MASC). The labels name the shape of each cipher sign; most are letters or digits used for a different letter.

| sign | plain | sign | plain | sign | plain | sign | plain |
|---|---|---|---|---|---|---|---|
| 1 | Y | 7 | J | f | V | p | B |
| 2 | U | 8 | L | g | K | q | Z |
| 3 | O | b | P | h | R | r | H |
| 4 | I | c | S | k | G | s | C |
| 5 | E | d | T | m | N | t | D |
| 6 | A | H | CH | n | M | | |

The key swaps several letter pairs (S/C, T/D, P/B, M/N); the cipher does not mark diacritics, so S also stands for Š, C for Č, and so on. CH has its own sign (a capped h).

## Plaintext

Literal output of the command, with the original line breaks. `(x)` marks a letter hidden under the printed picture and restored from context; `<x>` marks a visible sign of uncertain shape, given its best-matching value.

```
vrely dik, holubicko moje, za drahy listek, jenz
se s nim krizoval. dostala jsi jeste muj listek
v hradci? - tesi mne, ze je srdecko moje opet zdra-
vo jako diblik. mel jsem velkou starost. vzpo-
minam, zlato moje, stale. chtel jsem nastoupiti
dovolenou svoji koncem tohoto mesice, abych
se mohl podivati jeste do ustecke pametni
knihy dekanske, avsak zhatil se muj plan.
nas vrchni spravec, ktery nechtel jiti na dovole-
nou, nastoupi ji nasledkem choroby sveho
svagra, ktereho bude provazeti
do lazni, presto zitra, nasled-
kem cehoz musim odloziti ja
svoji dovolenou az na druhy
mesic. tisic dlouhych, vrelych
pus posila ti vecn(e)tvuj
pepous, ktery se (t)e<c>i na
opetnou brzkou zpravu
od sveho srdecka.
```

**Czech, with accents and punctuation restored** (restorations in square brackets):

> Vřelý dík, holubičko moje, za drahý lístek, jenž se s ním křižoval. Dostala jsi ještě můj lístek v Hradci? — Těší mne, že je srdéčko moje opět zdrávo jako diblík. Měl jsem velkou starost. Vzpomínám, zlato moje, stále. Chtěl jsem nastoupiti dovolenou svoji koncem tohoto měsíce, abych se mohl podívati ještě do ústecké pamětní knihy děkanské, avšak zhatil se můj plán. Náš vrchní správce [literally *spravec*], který nechtěl jíti na dovolenou, nastoupí ji následkem choroby svého švagra, kterého bude provázeti do lázní, přesto zítra, následkem čehož musím odložiti já svoji dovolenou až na druhý měsíc. Tisíc dlouhých, vřelých pus posílá ti věčn[ě] tvůj Pepouš, který se [t]ě[š]í na opětnou brzkou zprávu od svého srdéčka.

**English:**

> Warm thanks, my little dove, for the dear card, which crossed with mine. Did you still get my card in Hradec? — I am glad that my little heart is well again, as lively as a little imp. I was very worried. I think of you all the time, my treasure. I wanted to take my holiday at the end of this month, so that I could also look into the deanery memorial book in Ústí, but my plan has fallen through. Our chief administrator, who did not want to go on leave, is taking it after all, tomorrow, because of the illness of his brother-in-law, whom he will accompany to a spa; as a result I must put my holiday off until next month. A thousand long, warm kisses are sent to you by your forever [restored] Pepouš, who is looking forward [partly restored] to a new, early message from his little heart.

**Slovak:**

> Vrelá vďaka, holubička moja, za drahý lístok, ktorý sa minul s mojím. Dostala si ešte môj lístok v Hradci? Teší ma, že je moje srdiečko opäť zdravé ako diablik. Mal som veľkú starosť. Stále na teba spomínam, zlato moje. Chcel som nastúpiť na dovolenku koncom tohto mesiaca, aby som sa mohol ešte pozrieť do ústeckej dekanskej pamätnej knihy, môj plán sa však zmaril. Náš vrchný správca, ktorý nechcel ísť na dovolenku, na ňu predsa zajtra nastúpi pre chorobu svojho švagra, ktorého bude sprevádzať do kúpeľov, a preto musím svoju dovolenku odložiť až na budúci mesiac. Tisíc dlhých, vrelých bozkov ti posiela navždy [doplnené] tvoj Pepouš, ktorý sa teší [čiastočne doplnené] na opätovnú skorú správu od svojho srdiečka.

The text is ordinary Czech of around 1900 (*nastoupiti*, *jíti*, *následkem čehož*, *pamětní kniha děkanská*), and its tone and closing match the other cards of the family: *holubičko*, *srdéčko*, *tisíc … pus*, the signature Pepouš.

## Uncertainties

- **[T]Ě[Š]Í (row 17).** After SE a green patch hides one sign. Three signs are visible after it: an E (sign 5), a tall slanted stroke with a small foot, and an I (sign 4). The stroke is not the round sign that this writer uses for S/Š everywhere else; it best matches the angular sign for C, so the literal decode is *(t)e<c>i*. The sentence ("který se … na opětnou brzkou zprávu") allows only *těší* ("looks forward"). The reading therefore assumes either a slip — writing the plain letter of a swapped pair, the same kind of slip as TIK for *dík* on HCP 1556 — or an unrecorded variant of the S sign. TĚŠÍ is an editorial reading for the T and the Š; only E and I are read from visible signs.

![Row 17 after SE at 7x: the green patch, then 5, the tall slanted stroke, 4, and NA (work/review1/u03_7x.png)](../work/review1/u03_7x.png)

- **VĚČN[Ě] TVŮJ (row 16).** The patch covers about one sign between VECN and TVUJ, and no ink of it can be identified. E (*věčně tvůj*, "forever yours") follows the family's closing formula (also on HCP 1552 and 1554); *věčný tvůj* is equally possible from the pixels, with the same meaning.
- **G.** The k-shaped sign is read as G because only G makes a word here and on the sister cards; it occurs once on this card.
- **SPRAVEC** (row 9) is what is written; *správce* is an editorial correction of the writer's spelling, not a change of key.
- The accents, punctuation and word division of the Czech text are editorial; the cipher encodes base letters only.
- The places Hradec and Ústí, the "chief administrator", and the civil identity of Pepouš are not identified. Nothing else is visible under the printed trees; writing entirely covered by the picture cannot be excluded from a 674×1024 scan.

## Review summary

Reviewer: a separate Claude Opus 5.5 agent, round 1, verdict **REVISE**. The reviewer ran the reproduction command, decoded the transcription with an independently written table (identical text letter for letter, every key sign used), compared rows 3, 7–9 and 13–16 sign by sign with its own enlargements of the scan (no discrepancy), confirmed the k-shaped sign in SVAGRA as distinct from K, and confirmed that the address, date and vocabulary fit the context and that no published solution was used without disclosure. Its five findings and what changed:

1. **(major) Row 17.** The completion had claimed that the signs E-Š-I were visible after the patch; the reviewer showed that the middle sign is a tall stroke matching C, not the round S/Š sign. Agreed after re-cropping the passage at 7x. The transcription now records the visible signs as they are, and TĚŠÍ is labelled an editorial reading with the C/Š discrepancy stated.
2. **(major) Reproduction command.** The old command still printed placeholders. A new command, work/decode_final.py, prints the final text with restorations marked and checks that the final transcription differs from the reviewed one only by documented relabels; the solution's literal, editorial and translated texts were made consistent with it.
3. **(minor) VĚČN[Ě]** is now marked as a restoration, with *věčný* noted as possible.
4. **(minor) The J sign** is now labelled 7, as on the scan and in the family key.
5. **(minor) Evidence for G** now rests first on HCP 1570, whose independent review found the same sign in two G-only places.

No letter of the reading changed. Earlier work on this card (manual transcription, the round-0 decoder and the partial reading with three open places) was done by OpenAI GPT (GPT-6 Astra / GPT-6.1 Sol); the completion of the three open places, the response to review and this report were done by Claude Opus 5.5.

## Sources

- HC Portal record 1541, General, Description and Attachments tabs, captured 2026-10-28: https://crypto.hcportal.eu/dashboard/cryptograms/1541 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/4683/conversions/pc_hcp_222_pic-large.jpg (source/picture.jpg).
- Address side: https://api.hcportal.eu/media/4684/conversions/pc_hcp_222_adr-large.jpg (source/address.jpg).
- Family key: earlier Anna Tichá family cards in this repository, ciphers/hcp-1545/work/key.json.
- Maxim Egorov, Anna Tichá postcards, published partial family key: https://maxim-egorov.dev/research/anna-ticha-postcards/
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-29: no entry for this card.
