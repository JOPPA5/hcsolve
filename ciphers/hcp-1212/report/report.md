# HCP 1212 (cpc_1912-02-17_HU__HU_Jasz Arokszalas_jolanka-05): Feri to Jolánka, a love verse and a dinner

Human solver: Tomáš Pavuk

**Status: all cipher text on the card deciphered (17 main rows and one short address-side annotation); independent review 1 verdict ACCEPT, with one letter corrected afterwards (row 12, *a* → *e*).** Report dated 2026-10-29.

## Origin and context

The cryptogram is record 1212 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1212), portal name cpc_1912-02-17_HU__HU_Jasz Arokszalas_jolanka-05, from Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-10-12 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, category Substitution, date 1912-02-17, language Unknown, recipient Tóth Jolánka, sender Unknown, with no transcription or solution attached.

The picture side is a tinted photographic card of a young couple embracing at a window with roses, above a black field with flying swallows; it carries no handwriting. The address side is written in red ink. The left half holds seventeen rows of cipher signs; the right half carries the plain-hand address **Szépreményű Tóth Jolánka kisasszonynak, Jász-Árokszállás** ("To the promising Miss Jolánka Tóth, Jászárokszállás", Hungary), a JÁSZÁROKSZÁLLÁS postmark dated **1912 FEB 17**, a second partly legible postmark (probably GYÖNGYÖS), and two short plain-hand notes: above the postmark, probably *"Egy kis nefelejcsnek"* ("To a little forget-me-not"), and in the stamp corner, in five short lines, *"számtalanszor csókol szeretettel Feri"* ("kisses you countless times, with love, Feri"). Right of "kisasszonynak" there is one more short group of cipher signs (called N01 below).

The card belongs to a family of cipher postcards from a young man signing himself **Feri** to Jolánka Tóth in Jászárokszállás, all in the same hand and the same graphic cipher. Several are deciphered in this repository (for example HCP 1213, 1216, 1217, 1218, 1243 and 1301). The key was transferred from those cards; this is not a new key recovery. No published reading of this card was found.

![Address side with the seventeen cipher rows on the left, the address and postmarks on the right (source/address.jpg)](../source/address.jpg)

![Picture side, printed image only (source/picture.jpg)](../source/picture.jpg)

## Method

The transcription is **manual**. The scan of the address side was enlarged row by row (4–10×) and every sign was entered by hand as a shape token (two bars, three bars, corner, wave, inverted T, …) into a ledger, one line per row, plus one line for N01. A short script checks the SHA-256 of both source scans and maps the tokens to letters with the family key. No OCR was used, and the transcription is not blind: earlier readings were known while it was revised.

The work went through several passes. Passes 1–5 (2026-10-12/13) were done by an OpenAI GPT solver (GPT-6 Astra / GPT-6.1 Sol): capture of the portal record, key transfer from the sister cards and a reading of most of the text. Pass 6 by Claude Opus 5.5 re-checked every row on enlargements. It corrected three rows: row 12 *mindennel* instead of the non-word *mindenemél*, row 14 *kedéjes* (an inverted T, j) and row 17 *szeretetel* (two corner+bars groups). It also read the address-side annotation N01, which had been left open. After review 1 two more tokens in row 12 and the accents in row 1 were corrected (see the review summary).

## Key

Hungarian **graphic monoalphabetic substitution**: one sign per letter, word spaces mostly kept, accents written as ticks or dots above the sign. Digraphs are written with two signs (gy, cs, sz). The writer spells *ly* as *j*, as it is pronounced.

| Sign | Letter | Sign | Letter |
|---|---|---|---|
| two bars `=` | a | wave `~` | l |
| six-like loop `6` | b | three short strokes `III` | m |
| left bowl `(` | c | two short strokes `II` | n |
| short + long stroke | d | cursive loop | o |
| three bars `≡` | e | tall + short stroke | p |
| upright cross `+` | f | F-like sign | r |
| open loop with descender | g | right bowl `)` | s |
| two tall strokes | h | corner / gamma `Γ` | t |
| dotted crossed curve | i | x | u |
| inverted T `⊥` | j | chevron `ʌ` | v |
| section-like sign `§` | k | low descender | y |
| crossed diagonal | z | | |

At this resolution h and p are near-homographs and d and n differ mainly by stroke length; context settles every case on this card. No sign on the card needs a value outside this key.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1212/work/decode.py
```

The script checks the hashes of both scans and decodes the ledger `work/as-seen-pass6.txt`. Its output is the literal plaintext (`{x?}` marks an uncertain sign):

```text
01: édesjolánkámbecses
02: soraitkösönettelmeg
03: kaptammelyekörömemre
04: szolgaltakésazala{t?}ti
05: sorokbanvalaszolok.
06: kivelbizonyitsam,
07: hogytegedszeretlek
08: tanum,kialkotéanagy
09: mindenséget.
10: hogycsakértedélek
11: sértedszenvedek,
12: ésmindenneleföldön
13: jobbanszeretlek.
14: avacsoraélégkedéjes
15: volt,éshogymitadvissza
16: aztnemértem,istenvele
17: aviszontlatasraszeretetelferi
N01: {s?}ze{r?}etetel
```

## Plaintext (Hungarian, editorial)

Spaces, punctuation, missing accents and `[ ]` restorations are editorial.

Édes Jolánkám! Becses sorait kös[z]önettel megkaptam, melyek örömemre [szolgáltak], és az alatti sorokban válaszolok.

> Kivel bizonyítsam,
> hogy téged szeretlek?
> Tanúm, ki alkoté a nagy
> mindenséget.
> Hogy csak érted élek,
> s érted szenvedek,
> és mindennél e földön
> jobban szeretlek.

A vacsora elég kedélyes volt, és hogy mit ad vissza, azt nem értem. Isten vele! A viszontlátásra szeretet[t]el Feri.

Address-side annotation: probably *szeretet[t]el* ("with love").

## English translation

My sweet Jolánka! I received your dear lines with thanks; they gave me joy, and I answer in the lines below.

> By whom shall I prove
> that I love you?
> My witness is He who created the great
> universe.
> That I live only for you
> and suffer for you,
> and love you more
> than anything on this earth.

The dinner was quite pleasant, and as for what it/he gives back, I do not understand that. Farewell! Until we meet again, with love, Feri.

Annotation by the address: (probably) with love.

## Slovak translation

Moja milá Jolánka! S vďakou som dostal Vaše vzácne riadky, ktoré ma potešili, a v nasledujúcich riadkoch odpovedám.

> Kým mám dokázať,
> že ťa ľúbim?
> Mojím svedkom je ten, kto stvoril veľký
> vesmír.
> Že len pre teba žijem
> a pre teba trpím,
> a viac než čokoľvek na tejto zemi
> ťa ľúbim.

Večera bola dosť príjemná, a čo vracia, tomu nerozumiem. S Bohom! Do videnia, s láskou Feri.

Poznámka pri adrese: (pravdepodobne) s láskou.

## Uncertainties

1. **N01 annotation.** About ten cramped signs under the portal watermark. Signs 2–3 and 5–10 read clearly as z e … e t e t e l. Sign 1 is a single hooked stroke without the bowl of this writer's s, and sign 4 is an M-shaped sign in the place of r. The reading *szeretet[t]el* rests on the sign-off of this card, on HCP 1218, and on the plain-hand *szeretettel* in the stamp corner. It is probable, not certain.
2. **Row 4 *ala{t?}ti*.** A small cramped stroke before the final t may be a second t or a false start. The word is *alatti* "below" either way.
3. **Row 12 *mindennél*.** The sign after the two n's is three plain bars with no accent tick, so the literal reading is *mindennel*; the accent is editorial.
4. **Missing accents** in *szolgaltak*, *valaszolok*, *viszontlatasra* and others are supplied in the edition.
5. **Source spellings kept literally:** *kösönettel* (köszönettel), *élég* (elég), *kedéjes* (kedélyes), *szeretetel* (szeretettel), *tanum* (tanúm), *alkoté* (archaic past, "created"). *Kivel* ("by whom") is kept as written.
6. **Row 15 "mit ad vissza"** ("what it/he gives back"): the letters are clear, but the card does not say what is meant; the translation does not invent an object.
7. **Bottom edge.** The lowest row is partly clipped by the scan; the reading of *viszontlátásra* and *Feri* relies on the upper halves of the signs and the formula. Only the 1024-pixel portal image is available.
8. The plain-hand notes (address, stamp-corner note, the line above the postmark and a short line under the address) are not cipher and are not part of the decipherment; the line above the postmark is a probable reading only.

## Review summary

Reviewer: a separate Claude Opus 5.5 agent, round 1, verdict **ACCEPT**. The reviewer ran the reproduction command (hashes matched, output identical to the solver's), compared the key with the accepted sister card HCP 1301 (all 23 sign classes agree), read every row and N01 from its own enlargements, wrote its own ledger with its own sign names and decoded it with its own script. Its reading agreed sign for sign except for accents in row 1 and two signs in row 12. It confirmed the pass-6 corrections in rows 12, 14 and 17 on the pixels and judged the text fluent Hungarian of 1912 that fits the postmark, the addressee and the sister cards. Its five minor findings were all accepted:

- **Row 12 *a földön* → *e földön*.** The sign before *földön* has three bars (e), not two (a). Fixed in the ledger; the edition now reads *és mindennél e földön* ("on this earth"). The meaning hardly changes.
- **Row 12 accent.** No accent tick is visible on *mindennel*; the accent of *mindennél* is now marked as editorial.
- **N01 qualification.** The annotation is now presented as a probable reading everywhere.
- **Stamp-corner note.** The plain-hand note was misread earlier as "… szerető[d] Feri"; it reads *számtalanszor csókol szeretettel Feri*, and the line above the postmark probably reads *Egy kis nefelejcsnek*.
- **Row 1 accents.** The accents over both a of *Jolánkám* are now recorded in the ledger.

The reviewer could not resolve the row-4 extra stroke or N01 signs 1 and 4 at this resolution, and did not search the literature beyond what is recorded here. The response to review, this report and the register entry were prepared by Claude Opus 5.5.

## Sources

- HC Portal record 1212, General, Description and Attachments tabs, captured 2026-10-12: https://crypto.hcportal.eu/dashboard/cryptograms/1212 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/3696/conversions/cpc_1912-02-17_HU__HU_Jasz-Arokszalas_jolanka-05_pic-large.jpg (source/picture.jpg).
- Address side: https://api.hcportal.eu/media/3697/conversions/cpc_1912-02-17_HU__HU_Jasz-Arokszalas_jolanka-05_adr-large.jpg (source/address.jpg).
- Family key: sister cards in this repository, ciphers/hcp-1301 and ciphers/hcp-1243.
- Portal reference article (not read): https://ecp.ep.liu.se/index.php/histocrypt/article/view/166
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-29: no record for this card.
