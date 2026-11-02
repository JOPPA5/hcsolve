# HCP 1167 (cpc_1916-03-11_HU_Mezokovesd_HU_Szomolya_szomolya-22): Árpád's message in digits to Margitka Sziber

Human solver: Tomáš Pavuk

**Status: the whole message is deciphered (345 cipher signs: 341 by the key as written, 4 by word sense); independent review 1 verdict REVISE, findings addressed, one word corrected.** One short word of the open greeting remains a reading by parallel. Report dated 2026-11-02.

## Origin and context

The cryptogram is record 1167 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1167), portal name cpc_1916-03-11_HU_Mezokovesd_HU_Szomolya_szomolya-22, from Tobias Schrödel's cryptographic postcards collection (private collection). When captured on 2026-11-02 the portal listed it as **Not solved**, tagged Postcard, T. Schrödel Collection, category Substitution, language Unknown, sender Unknown, recipient Margitka Sziber, with no transcription or solution attached. The portal links a HistoCrypt article (https://ecp.ep.liu.se/index.php/histocrypt/article/view/166). That article was not checked, so it is not known whether it discusses this card. No published solution was found or used.

It is a wartime picture postcard showing a couple embracing, with no writing on the picture side. The left half of the message side is 18 lines of figures. Under them stand two lines of open greeting and the open place and date, Mezőkövesd, 1916. III/11. (11 March 1916). The address is in plain writing: **Őnagysága / Rózsa reményű / Sziber Margitka / kisasszonynak / Szomolya / Borsod m. u. p. Bogács**. The first words are a courtesy formula, roughly "To the honoured, rose-promising young lady". The stamp is a Hungarian 5-fillér issue; the date strip of its postmark is too broken to read, so the date rests on the writer's own line, which agrees with the portal's file name.

The card belongs to the correspondence of a suitor, Árpád, with Margitka Sziber of Szomolya, from which several cards have been read: hcp-1174, 1178, 1179 and 1165 among them. Unlike those, where single tender words are put into digits, nearly the whole message of this card is enciphered.

![Message and address side (source/address-large.jpg)](../source/address-large.jpg)

![Picture side, no cipher text (source/picture-large.jpg)](../source/picture-large.jpg)

## Method

The transcription is manual, made from the un-converted high-resolution scan (work/hires/) enlarged 2 to 4 times. No OCR was used. Key and hand were not assumed from the sister cards but tested: the table from hcp-1174, 1179 and 1165 was applied to this card's own reading, and only the signs this card needs were kept.

The cipher turns on the marks after a digit. A digit with a comma, a dot or a colon is a different sign from the bare digit, and the mark belongs to the sign, so `3` is d, `3,` is r and `3.` is v. Marks left of a 1 also count. The card shows visible gaps between groups, but they do not settle every word boundary, so the final word division is the solver's.

With the key applied, 341 of the 345 signs give connected, ordinary Hungarian as written. The other 4 are a mark left off the right digit in a very common word; they are listed under Uncertainties.

The decoding can be reproduced from the repository root with `python3 -I ciphers/hcp-1167/work/decode.py`. It checks the hashes of the four scans, decodes work/transcription.txt and prints the text line by line, marking the signs read by sense.

## Key

Monoalphabetic substitution (MASC), one sign per letter or per digraph (cs, gy, ny, sz, ly). Vowel length is mostly not shown.

| Sign | Plain | Sign | Plain | Sign | Plain |
|---|---|---|---|---|---|
| `0` | o, ó | `2.` | é | `6` | j |
| `0,` | ö, ő | `3` | d | `6,` | n |
| `1` | i, í | `3,` | r | `6.` | ny |
| `1.` | a | `3.` | v | `7` | k |
| `1:` | e | `4` | f | `7,` | s |
| `1'` (high dot) | á | `4,` | g | `7.` | sz |
| `1,` | b | `4.` | gy | `8` | m |
| `:1` (dots at left) | ü | `5` | h | `8,` | t |
| `.1` (dot at left) | u, ú, ű | `5,` | l | `9` | p |
| `2,` | cs | `5.` | ly (see below) | `9,` | z |

## Plaintext

Everything from Édes to the signature is enciphered. The output of the decoder, line by line as on the card, with accents as the cipher gives them. `[x<y]` means the sign as written gives y and word sense requires x.

```text
édes margitkám!
értesitelek hogy rozátol
most kaptam egy lapot melyben
azt irja hogy irt nektek egy
levelet már három hete
és választ még nem kapot rá
nem tudja mi oka [l<h]ehet
most pedig értesitlek
édesem ho[gy<f] ha csak lehe[t<m]
minden bizonyal fel megyek
most többet nem irok majd
szo[v<d]al többet már ugyis
régen nem beszélgettünk
soraimat bezárva adig
is maradok üdvözölve és
számtalanszor csokolva
huséges kedvesed és
imádod a sirig (árpád)
```

Edited, with accents added and the card's spelling kept:

Édes Margitkám! Értesítelek hogy Rózától most kaptam egy lapot melyben azt írja hogy írt nektek egy levelet már három hete és választ még nem kapot rá nem tudja mi oka lehet. Most pedig értesítlek édesem hogy ha csak lehet minden bizonyal fel megyek. Most többet nem írok majd szóval többet már úgyis régen nem beszélgettünk. Soraimat bezárva adig is maradok üdvözölve és számtalanszor csókolva hűséges kedvesed és imádód a sírig (Árpád)

Open text: Sokszor csókolom ángyikát is / és [a?] kis Mariskát is. / Mezőkövesd, 1916. III/11.

Normal spelling of three forms: kapot = kapott, bizonyal = bizonnyal, adig = addig.

## English translation

Sweet Margitka! I let you know that I have just received a card from Róza, in which she writes that she wrote you all a letter three weeks ago and has still had no reply to it; she does not know what the reason can be. And now I let you know, my sweet, that if at all possible I will certainly come up. I will not write more now, more by word of mouth; we have not talked for a long time anyway. Closing my lines, until then I remain, greeting you and kissing you countless times, your faithful sweetheart and your adorer to the grave (Árpád)

Open: Many kisses to ángyika too, and to little Mariska too. Mezőkövesd, 11 March 1916.

"ángyika" is a kin word (sister-in-law or aunt); the exact relation is not established.

## Slovak translation

Moja sladká Margitka! Oznamujem ti, že som práve dostal od Rózy pohľadnicu, v ktorej píše, že vám napísala list už pred tromi týždňami a ešte na to nedostala odpoveď; nevie, čo môže byť príčinou. A teraz ti oznamujem, moja zlatá, že ak to len bude možné, určite prídem hore. Teraz už viac nepíšem, viac potom ústne; aj tak sme sa už dlho nerozprávali. Končiac svoje riadky, zatiaľ ostávam, pozdravujúc ťa a nespočetnekrát bozkávajúc, tvoj verný milý a tvoj ctiteľ až do hrobu (Árpád)

Otvorený text: Mnohokrát bozkávam aj ángyiku a aj malú Marišku. Mezőkövesd, 11. marca 1916.

## Uncertainties

Four cipher signs are read by sense. Each is a true omission of the mark, confirmed by the reviewer on enlargements:

- `lehet` in `mi oka lehet` (line 7): the first sign is a plain `5`, so the table gives `hehet`.
- `hogy` (line 9): the last sign is a plain `4`, so the table gives `hof`. The same word has `4.` twice elsewhere on the card.
- `lehet` in `ha csak lehet` (line 9): the last sign is a plain `8`, so the table gives `lehem`.
- `szóval` (line 12): the third sign is a plain `3`, so the table gives `szodal`.

Smaller calls:

- `5.` = ly rests on one word, `melyben`. On hcp-1178 and 1179 `5.` is l, so it may be l with the spelling `melben`. The word is the same either way.
- `.1` occurs three times: `tudja`, `úgyis`, `hűséges`. Vowel length in the last two is by word sense.
- `megyek`: the upper dot of the last `1:` touches the following 7. The alternative `1.` would give `megyak`.
- The `6,` in `számtalanszor` and in `nem` on line 13 has its comma run into the tail of the 6. This is the writer's habit; the plain 6 has no such tail.
- `fel | megyek` has a clear gap on the card; one word, `felmegyek`, is the grammar. Punctuation is the solver's, and `majd szóval többet` is taken as "more by word of mouth".
- `imádód` ("your adorer") rather than `imádod` ("you adore"), since `0` covers o and ó and the word follows `kedvesed és`.
- Open text: the short word in `és [a?] kis Mariskát is` is badly formed and printed over by a green number, and the k of `kis` is blotted. It is read as `a` by parallel with `és a kis Mariskával` on hcp-1178. It is one word alone and the clause reads. The mark over `Mariskát` is the accent of á.

Not established: the postmark date, the identity of Róza, the exact kin sense of ángyika, and whether the HistoCrypt article treats this card.

## Review and what changed

An independent reviewer (a separate Claude Opus 5.5 agent) ran the decoder, decoded with its own script and a retyped key, and read all 18 cipher lines from its own crops, blind to the solver's. It confirmed the key, the signature, the four by-sense signs and the address. Verdict **REVISE**, with one major and six minor findings:

- Major: the first sign of the last word on line 12 has a firm dot at its left, so it is `.1` and not `1`. The word is **úgyis** ("anyway"), not `így is`. Corrected in the transcription, plaintext and translation.
- Minor, all addressed: the count of `.1` corrected to three; the `megyek` vowel and the fused commas now disclosed; the description of word gaps corrected, since the card does have gaps; `[a?]` stays disclosed as a reading by parallel; hcp-1165, open at the time of review, has since been finished.

The rest of the reading did not change, and the sign counts stayed at 345 and 341.
