# HCP 1143 (cpc_1916-05-04_HU_Mezokovesd_HU_Szomolya_szomolya-33): a new job and a poem in digit cipher

Human solver: Tomáš Pavuk

**Status: all 586 cipher signs are deciphered (581 by the key as written, 5 by word sense or restoration); independent review 1 verdict REVISE, findings addressed, two misread words corrected.** Report dated 2026-11-02.

## Origin and context

The cryptogram is record 1143 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1143), portal name cpc_1916-05-04_HU_Mezokovesd_HU_Szomolya_szomolya-33, from Tobias Schrödel's collection of cryptographic postcards (private collection). When captured on 2026-11-02 the portal listed it as **Not solved**, tagged Postcard, T. Schrödel Collection, category Substitution, language Unknown, sender Unknown, recipient Margitka Sziber, with no transcription or solution attached. The portal links a HistoCrypt article, which was not checked for this card, so it is not known whether the article discusses it.

It is a picture postcard printed with daisies, pink roses and a blank paper sheet. The sender filled that sheet with three four-line stanzas and a closing word, all in cipher; to read them the card is turned 90 degrees. The address itself is clear text: **Őnagysága / Sziber Margitka / Kisasszonynak / Szomolya / u.p. (Bogács)**, with the dateline **Mezőkövesd, 1916, V/4** at the bottom left. The date agrees with the portal file name. Everything else is in cipher, and nothing of the message is in clear. The language proves to be Hungarian.

The card belongs to the family of Mezőkövesd cards to Margitka Sziber of Szomolya (1915 to 1916), several already deciphered in this repository. The sender signs Árpád, as on hcp-1174. It was 1916, during the First World War; the card itself says only that he took a job in a small shop.

![Address side: the letter in cipher, the address and dateline in clear (source/address-large.jpg)](../source/address-large.jpg)

![Picture side turned upright: the poem on the printed sheet (work/crops/p_rot.png)](../work/crops/p_rot.png)

## Method

The transcription is **manual**, made by Claude Opus 5.5 from enlarged crops of the un-converted originals (work/hires/). No earlier work on this number existed and no OCR was used. The starting key came from the finished sister cards hcp-1174, 1178 and 1179. The salutation has the same signs as the heading of hcp-1174, Édes Margitkám, and with the transferred table most words decoded at once. Six signs absent from those tables were fixed on this card, each by words of its own: `4.` gy (hogy, egy, vagyok), `5.` ly (oly, twice), `6` j (jó, teljes), `6.` ny (nyílik, lányka), `2` c (cím) and `.1` u (után). The plain `4` f, only suggested on hcp-1175, is attested here by fehér and fizetésem.

The script work/decode.py checks the hashes of the scans, decodes work/transcription.txt with work/key.json, and asserts that each decoded word equals the stated reading (long vowels folded, since the key does not separate most of them). Command, from the repository root:

```
python3 -I ciphers/hcp-1143/work/decode.py
```

It prints only the enciphered parts. The address and the dateline are clear text and are not in the transcription.

## Key

Monoalphabetic substitution (register label MASC). Each letter is a digit with an optional mark, and digit plus mark is one sign. There is no word division. On the address side a large `)` marks a sentence end and the signature stands in `( )`. A `-` at a line end is a line-break hyphen. The flag over a 5 belongs to the digit and is not a mark.

| Digit | no mark | `,` | `.` | other |
|---|---|---|---|---|
| 0 | o, ó | ö, ő | | |
| 1 | i, í | b | a | `1:` e; `1'` (high dot) á; `:1` (dots left) ü, ű; `.1` (dot left) u, ú |
| 2 | c | cs | é | |
| 3 | d | r | v | |
| 4 | f | g | gy | |
| 5 | h | l | ly | |
| 6 | j | n | ny | |
| 7 | k | s | sz | |
| 8 | m | t | | |
| 9 | p | z | | |

The marks give a regular pattern for the digraphs: c/cs, g/gy, n/ny, s/sz. The value of `5.` is not settled across the family (see below).

## Plaintext

With word division, punctuation and capitals added. `[= ]` gives the normal form.

Édes Margitkám!

Bocsás [= Bocsáss] meg, hogy még csak most írok, de hamarabb nem tehettem. Most pedig értesítlek [= értesítelek], hogy kedden este szerencsésen leértem, nagyon jó idő volt, és már szerda óta alkalmazásba [= alkalmazásban] vagyok itt, ebbe a kis parasztboltba [= ebben ... boltban] a hentesek háta mögött. Ezt az egy hónapot kitöltöm itt, aztán megyek tovább. Fizetésem negyven korona és teljes ellátás. Most egyebet nem írok. Ha írsz, egyeb [= egyéb] cím nem kell, csak az én nevem, mint szokás szerint.

Most pedig üdvözöl számtalanszor, ölel és csókol hű imádód (Árpád)

Mezőkövesd, 1916, V/4 (in clear)

Poem on the picture side:

Margit virág után / Margit lett a neved, / s mint e virág fehér, / s szép a lelked neked.

Kertben a kis virág / csak tavaszkor nyílik, / szerelem virága / virágzik a sírig.

Liliom a te virágod, / oly fehér a világod, / oly tiszta vagy te is, lányka, / te életem boldogsága.

Szeretettből [= Szeretetből]

## Translation

**English.** Sweet Margitka! Forgive me for writing only now, but I could not do so sooner. Now I inform you that on Tuesday evening I got down safely, the weather was very good, and since Wednesday I have been employed here in this small peasant shop behind the butchers. I will serve out this one month here, and then I move on. My pay is forty crowns and full board. I write nothing else now. If you write, no other address is needed, only my name, as usual.

And now your faithful admirer (Árpád) greets you countless times, embraces and kisses you.

After the daisy [Margit flower] your name became Margit, and white as this flower, and fair is your soul. // In the garden the little flower blooms only in spring; the flower of love blooms until the grave. // The lily is your flower, so white is your world; so pure are you too, girl, you the happiness of my life. // With love.

**Slovak.** Moja sladká Margitka! Odpusť, že píšem až teraz, ale skôr som nemohol. Teraz ti oznamujem, že v utorok večer som šťastne došiel dolu, bolo veľmi pekné počasie, a už od stredy som zamestnaný tu, v tomto malom sedliackom obchodíku za mäsiarmi. Tento jeden mesiac tu dokončím a potom pôjdem ďalej. Môj plat je štyridsať korún a plné zaopatrenie. Teraz už nič iné nepíšem. Ak napíšeš, iná adresa nie je potrebná, len moje meno, ako obyčajne.

A teraz ťa nespočetnekrát pozdravuje, objíma a bozkáva tvoj verný ctiteľ (Árpád).

Podľa margarétky [kvetu Margit] dostala si meno Margita, a biela ako tento kvet, a krásna je tvoja duša. // V záhrade malý kvet kvitne len na jar, kvet lásky kvitne až do hrobu. // Ľalia je tvoj kvet, taký biely je tvoj svet, taká čistá si aj ty, dievča, ty šťastie môjho života. // S láskou.

## What remains uncertain

Five signs are not given by the table:

- Margitkám, two signs: ink blots cover the t and the final m. The comma of the t still shows. These are restorations; the word stands in full on hcp-1174.
- ezt: the sign is a plain `1`, so the table gives izt. A pale smear lies on it, but no dots of `1:` show. Read by sense.
- ellátás, last sign: a plain `7` with no comma, so the table gives ellátak. Read by sense after teljes.
- liliom, third letter: a `4`-like shape, neither a clean `1` nor a clean `4`. Read by sense.

Other points:

- nem in egyeb cím nem kell: the loop of the first sign is filled with ink. It is read `6,` because the top is one continuous stroke with no detached flag; `5,` would give lem, no word. This rests partly on context.
- sírig stands in faded ink, where the pen ran dry on the printed sheet. Dark spots there are taken as stem feet, not marks (see the review section).
- `5.` is printed ly here (oly, twice). The family is split: hcp-1142, 1151, 1153 and 1162 print ly, while hcp-1178 and 1179 file it as an l variant and hcp-1149 as l, perhaps ly. The word is the same either way.
- The writer's own forms are kept: Bocsás, értesítlek, egyeb, Szeretettből, and the colloquial -ba for -ban.
- A blue blot stands before Margit at the head of the poem. No sign can be seen in it.
- "got down" (leértem) is a rendering; the card does not say from where to where. "peasant shop" for parasztbolt is literal. If the card was written on Thursday 4 May 1916, Tuesday and Wednesday would be 2 and 3 May, which is inference. The postmark was not read, and the day in the dateline is read 4 with a stroke before it taken as the slash.

## Why the solution is believed correct

One fixed table gives 581 of 586 signs as written, and all 586 make grammatical Hungarian of the period from first to last, with no gap. The new signs fill a regular grid. The poem rhymes (neved/neked, nyílik/sírig, virágod/világod, lányka/boldogsága), and its first stanza plays on her name and the daisies printed on the card itself. The recipient and place are in clear, and the signature Árpád decodes as on hcp-1174. The letter has a practical content: a job, forty crowns, full board. No published solution was found or used.

## Review and what changed

An independent reviewer (a separate Claude Opus 5.5 agent) ran the command, wrote its own decoder from a retyped table, and read the whole card against the transcription on enlargements. It confirmed the key, its coverage of the whole text and the sense of the card. Verdict: REVISE, with seven findings, all accepted:

- alkalmazesba was a misreading of **alkalmazásba**: the sign has a high dot only, so it is `1'`, not `1:`.
- lenyka was a misreading of **lányka**, for the same reason. A claimed oddity of the writer's spelling is withdrawn.
- sírig was first marked as the weakest word, with two signs held to carry extra dots. Those spots are stem feet, so the table now gives the word directly, and the count went from 579 + 7 to 581 + 5.
- The supporting argument and counts were updated, the `5.` note now gives the split in the family, two translation slips were fixed, and the command's scope (enciphered parts only) is now stated.

The sense of the card did not change.
