# HCP 1153: a Hungarian postcard from Árpád to Margitka Sziber, Mezőkövesd, 9 June

Human solver: Tomáš Pavuk

**Status: deciphered in full (348 of 348 cipher signs, one sign read by word sense); independent review 1 verdict REVISE, findings addressed, one word corrected.** Report dated 2026-11-02.

## Origin and context

The cryptogram is record 1153 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1153), portal name cpc_1916-06-09_HU_Mezokovesd_HU_Szomolya_szomolya-38, part of Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-11-02 the portal listed it as **Not solved**, category Substitution, language Unknown, sender Unknown, recipient Margitka Sziber, with no transcription or solution attached. The portal links a HistoCrypt article on the collection; it was not opened for this card, so we cannot say whether it discusses it.

The picture side shows violets and carries no writing. The address side is in clear: **Őnagysága / Sziber Margitka / kisasszonynak / Szomolya / u. p. Bogács** ("Her Ladyship, Miss Margitka Sziber, Szomolya, post office Bogács"). The clear heading gives **Mezőkövesd. VI/9**, with no year. The year 1916 comes only from the portal filename, because the postmark is too faint to read.

Almost all of the message is in digits. Only the words Ha ibolyát látok, Eszembe, the place and date, and the address are in clear. The card belongs to a family of postcards from Árpád at Mezőkövesd to Margitka Sziber in 1915 and 1916, several of which are deciphered in this repository.

![Address side with the cipher text (source/address-large.jpg)](../source/address-large.jpg)

![Picture side: violets, no writing (source/picture-large.jpg)](../source/picture-large.jpg)

## Method

The card was read with a **known key from sister cards**; it is not a new key recovery. The base key was reconstructed on the finished cards HCP 1174, 1178 and 1179. Five further signs were taken from sister cards of the same batch, and each is tested here by clean words.

The transcription is manual. The solver read every row from enlarged crops of the un-converted original scan, one card row at a time, sign by sign. A script (work/decode.py) checks the scan hashes, decodes the whole transcription by the key table, and asserts that the result equals the stated reading letter for letter. Reproduce it from the repository root with:

    python3 -I ciphers/hcp-1153/work/decode.py

The reviewer read all rows again in its own crops, wrote its own key table and decoder, and compared the two readings token by token.

## Key

A monoalphabetic substitution: each letter is one sign, either a digit alone or a digit with a mark, and the mark is part of the sign. The words run together with only small gaps.

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| 0 | o, ó | 2, | cs | 6 | j |
| 0, | ö, ő | 2. | é | 6, | n |
| 1 | i, í | 3 | d | 6. | ny |
| 1, | b | 3, | r | 7 (crossed) | k |
| 1. | a, á | 3. | v | 7, | s |
| 1 with raised ring | á | 4, | g | 7. | sz |
| 1: | e | 4. | gy | 8 | m |
| .1 | u | 5 | h | 8, | t |
| :1 | ü, ű | 5, | l | 9 | p |
|  |  | 5. | ly | 9, | z |

Accents in the plaintext come from the words, as this card does not separate them reliably. A slanted hooked stroke appears four times and behaves as punctuation, not as a letter: after leértem, írni, imádód and Árpád.

Status of the added signs: 4. (gy), 5. (ly), 6 (j), 6. (ny) and .1 (u) are on no finished card's table. Two conflict with finished cards: HCP 1178 and 1179 file 5. as a variant of l, and the review of HCP 1178 dropped .1 from that key. On this card oly (twice) settles 5. = ly, and jutsz alone carries .1, so these two values stand on this card and on unfinished sisters only.

## Plaintext

Square brackets mark what is enciphered on the card. Punctuation and word division are editorial, except the exclamation mark after the salutation.

Mezőkövesd. VI/9

[Édes Margitkám! Értesítlek, hogy szerencsésen leértem. Most pedig itt vagyok az állomáson, várom a vonatot, a vonat még soká jön, tehát ráérek írni, drága Margitkám, itt látok síró asszonyokat, amint válnak el az övéiktől, és most én is iszonyodva gondolok az elválásra, mert még ha mást lát is az ember, még az is könnyet csal a szemébe.]

Boxed verse:

Ha ibolyát látok [lányka]

Eszembe [jutsz én nékem]

[Oly szerény vagy te épen]

[És oly szép is édesem]

[Most pedig szá(m)talanszor ölel és csókol hű imádód Árpád]

## English translation

Sweet Margitka! I inform you that I got down safely. Now I am here at the station, waiting for the train; the train will not come for a long time yet, so I have time to write, dear Margitka. Here I see weeping women as they part from their own, and now I too think with horror of the parting, for even when one sees someone else [part], even that brings a tear to one's eye.

When I see a violet, little girl,

You come to my mind;

You are just as modest

And just as lovely too, my sweet.

And now, countless times, your faithful adorer Árpád embraces and kisses you.

## Slovak translation

Moja sladká Margitka! Oznamujem ti, že som šťastne došiel dolu. Teraz som tu na stanici, čakám na vlak, vlak ešte dlho nepríde, takže mám čas písať, drahá Margitka. Vidím tu plačúce ženy, ako sa lúčia so svojimi, a teraz aj ja s hrôzou myslím na rozlúčku, lebo aj keď človek vidí niekoho iného, aj to mu vženie slzu do oka.

Keď vidím fialku, dievčatko,

spomeniem si na teba;

si práve taká skromná

a aj taká pekná, moja milá.

A teraz ťa nespočetnekrát objíma a bozkáva tvoj verný ctiteľ Árpád.

## Uncertainties

- **ha (row 11).** The 5 is clear, but no dot follows the 1, so the table gives hi. The construction mert még ha ... is fixes a. This is the only sign read by sense.
- **Commas that collide with the row below.** At the second vonat, at lát and at szá(m)talanszor the comma of an 8 runs into the sign below. At vonat the stroke ends on a 3, which has no ascender, so it can only be the comma. At lát it joins the 6 of könnyet, as the crop below shows. At szá(m)talanszor the printed word nach and a crossed 7 lie on the same spot, so this one is less clean. If that stroke is not a comma, the lost letter is the t and not the m. Either way the writer dropped one letter and the word is certain.
- **mást lát.** The writer does not say what the others are doing; "[part]" in the English and the plain "someone else" in the Slovak are a reading of the sentence before.
- **Spelling.** Értesítlek has no e between t and l, where the usual form is értesítelek; it is kept as written. épen is the older spelling of éppen.
- **Harder shapes, read and accepted by both solver and reviewer.** jutsz (the dot sits at the foot of the 1; nyitsz does not fit Eszembe), lányka (a raised ring, not a 0), ráérek, csal, szemébe, and csókol hű under the printed logo and line.
- **Year and postmark.** Not read. The year 1916 rests on the portal filename.
- **Published work.** The HistoCrypt article linked by the portal was not opened. No published reading was used.

![The disputed comma at lát: the stroke from the 8 joins the top of the 6 below (review/work/lat6.png)](../review/work/lat6.png)

## Why the reading is believed

The key turns all 348 signs into continuous Hungarian, with long unforced words such as szerencsésen, asszonyokat, iszonyodva, elválásra and állomáson. The clear words fit the cipher around them (Ha ibolyát látok [lányka], Eszembe [jutsz én nékem]), the verse closes on near-rhymes, and the picture is violets. The opening and the signature Árpád match HCP 1174. Weeping women parting from their men at a station fits Hungary in 1916, though the card does not say the men are soldiers.

## Review and what changed

The independent reviewer (a separate Claude Opus 5.5 agent) confirmed the cipher type, the key and nearly all of the plaintext; its own reading differed from the solver's in two tokens. Verdict: REVISE.

- **Major, fixed: lám became lát.** The solver had called the sign certain as 8 with no comma, and had explained the resulting loose sentence as a short form and a stretched syntax. The reviewer showed the comma colliding with the row below. With it the sentence is ordinary Hungarian, and both explanations were withdrawn.
- **szám(t)alanszor became szá(m)talanszor,** with the alternative kept open.
- **vonat:** the sign is no longer flagged, and the wrong reason given for it was corrected. Flagged signs fell from two to one.
- **Bookkeeping:** 9, = z was added to the key table, the conflict over 5. and .1 with finished cards is now stated, and the stroke after Árpád is recorded.

The reviewer also tested the transcription against the pixels, and could not read the postmark.
