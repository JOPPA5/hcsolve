# HCP 1230 (cpc_1913-12-_HU__HU_Jasz Arokszalas_jolanka-116): Feri to Jolánka Tóth

Human solver: Tomáš Pavuk

**Status: deciphered in full (477 cipher signs in 26 rows, one three-letter word not fully explained); independent review 1 verdict REVISE, all findings addressed.** Report dated 2026-11-02.

## Origin and context

The cryptogram is record 1230 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1230), portal name cpc_1913-12-_HU__HU_Jasz Arokszalas_jolanka-116, part of Tobias Schrödel's collection of cryptographic postcards (private collection; see the HistoCrypt paper https://ecp.ep.liu.se/index.php/histocrypt/article/view/166). When it was captured on 2026-11-02 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, category Substitution, language Unknown, sender Unknown, recipient Tóth Jolánka, with no transcription or solution attached. No published solution of this card was found.

The picture side is printed only ("Te vagy a csillagom." and a four-line verse) and has no handwriting. The whole message is on the address side, written in violet pencil in invented signs: 26 rows filling the left half of the card, the last running along the bottom edge.

The address is in clear: Széprém[enyű] Tóth Jolánka úrleánynak, Jász Árokszállás (Jászárokszállás, Hungary). The first word is partly under the postmark. The Budapest postmark visibly reads `913 DE`, which agrees with the December 1913 in the portal's file name; its day digits and a second postmark at top left could not be read.

The card belongs to the Jolánka family of cipher postcards to the same addressee. Several are deciphered in this repository (for example HCP 1212, 1213, 1216, 1217, 1218, 1243 and 1301), and HCP 1216 has the same close, "sírig hű kedvese, Feri".

![Address side with the cipher text (source/address-large.jpg)](../source/address-large.jpg)

![Picture side, printed only (source/picture-large.jpg)](../source/picture-large.jpg)

## Method

The key was **transferred** from the finished family cards; this is not a new key recovery. That family key was reconstructed earlier by the OpenAI GPT solver and completed by Claude Opus 5.5. No earlier work exists on this number.

The transcription is manual. Each sign was read from enlargements of the un-converted scan and recorded in a sign ledger (work/ledger.txt). A blue-minus-green channel keeps the violet pencil and removes most of the black postmark, which was needed for rows 1 to 6 at the right. A script decodes the ledger with the key and checks the hashes of the image files:

```text
python3 -I ciphers/hcp-1230/work/decode.py
```

## Key

Monoalphabetic substitution; the descriptions are conventional names for the handwritten shapes. The letter c is not used on this card, and gy is written as two signs, g + y. Marks over a sign give á, é, ö, ő, ü; most are faint and are supplied in normalization.

| Sign | Plain | Sign | Plain | Sign | Plain |
|---|---|---|---|---|---|
| two bars | a | S-shaped section sign | k | F-like | r |
| six | b | wave | l | right bowl | s |
| long stroke, tick to its left | d | three short strokes | m | gamma/corner | t |
| three bars | e | two short strokes | n | plain cross | u |
| upright cross | f | cursive loop | o | chevron | v |
| open loop with descender | g | crossed curve, normally dotted | i | y-loop | y |
| inverted T | j | opposed bowls | cs | crossed x with tail | z |
| long stroke, tick to its right | h | same stroke pair | p | | |

The d, h and p signs are near-homographs, so those calls are listed under Uncertainties where they rest on word sense.

## Plaintext

Literal decipherment, row by row; [k] is a sign hidden by the postmark:

```text
01 szereretedesjolán[k]ám        14 stiklimelsimuljtöb
02 bivanomhogyaljobegezeg        15 betnemcsinalokijes
03 bentalaljasoraimensze         16 mitmertnemabüntetés
04 rencsésenmegérkeztem          17 sanálomhanemaztaz
05 igazhogynemavalavo            18 ijesmitbejegyzies
06 nattalamelikkelszá            19 haelolepteteskorazt
07 mitotottammertazcsak          20 nézikvoltemarbüntet
08 egyorávalmintszamitot         21 veeshanyszorezront
09 tamesigycsakregelhet          22 jaazelőrhaladast
10 orakkorértemhaza              23 demostmastnemirok
11 személyvonattalde             24 mivelnagyonalmos
12 talannemleszbelő              25 dakistenveleedesem
13 lesemmibajcsakeza             26 maradoksirighukedvesefer
```

### Hungarian (normalized)

Szeretett édes Jolánkám! Kívánom, hogy a legjobb egészségben találja soraim. Én szerencsésen megérkeztem. Igaz, hogy nem avval a vonattal, amelyikkel számítottam, mert az csak egy órával [előbb/később], mint számítottam, és így csak reggel hét órakor értem haza személyvonattal. De talán nem lesz belőle semmi baj. Csak ez a stiklim elsimuljon, többet nem csinálok ilyesmit, mert nem a büntetést sajnálom, hanem azt, az ilyesmit bejegyzi, és ha előléptetéskor azt nézik, volt-e már büntetve, és hányszor, ez rontja az előrehaladást. De most mást nem írok, mivel nagyon álmos [va]gyok. Isten vele, édesem. Maradok sírig hű kedvese, Fer[i].

### English

My beloved sweet Jolánka! I wish that my lines find you in the best of health. I arrived safely. True, not by the train I had counted on, because that one was just an hour [earlier or later; the word is not written] than I had reckoned, and so I got home only at seven in the morning, by passenger train. But perhaps nothing bad will come of it. If only this prank of mine gets smoothed over, I will not do anything like it again, because it is not the punishment I regret but this: he enters such a thing in the record, and if at promotion time they look at whether one has already been punished, and how many times, that spoils one's advancement. But I write nothing else now, as I am very sleepy. God be with you, my sweet. I remain, faithful unto the grave, your sweetheart, Feri.

### Slovak

Moja milovaná, sladká Jolánka! Želám si, aby Vás moje riadky našli v najlepšom zdraví. Šťastne som dorazil. Pravda, nie tým vlakom, s ktorým som počítal, lebo ten išiel len o hodinu [skôr alebo neskôr; slovo nie je napísané], než som počítal, a tak som domov prišiel až o siedmej ráno, osobným vlakom. Ale azda z toho nebude nijaká nepríjemnosť. Len nech sa mi tento kúsok urovná, viac už nič také neurobím, lebo neľutujem trest, ale to, že sa také niečo zapíše, a ak sa pri povyšovaní pozerajú na to, či už bol človek trestaný a koľkokrát, to kazí postup. Ale teraz už nič iné nepíšem, lebo som veľmi ospalý. S Bohom, drahá. Zostávam do hrobu Váš verný milý, Feri.

The word "stikli" means a prank or escapade. The writer seems to be a soldier or someone else in a service with a disciplinary record who came back late, but the card does not say so outright. Nothing beyond the shared close identifies this Feri.

## Uncertainties

- **Row 25 `dak`.** This is the one word not fully explained. The sentence needs "I am" after "álmos", so it is normalized "[va]gyok", but that is an inference. "álmosodok" ("I am getting sleepy") is an alternative with the same sense. The word stands alone and the rest of the card reads.
- **Row 8, the missing word.** The writer left out the comparative and the verb. Nothing is missing on the card. "[előbb]" (earlier, so he missed the train) and "[később]" (later) both fit, so both are kept.
- **Row 1, k of Jolánkám.** This is a restoration under a postmark blot. The name is in clear in the address.
- **Row 26, final i of Feri.** This is an editorial supply. The paper is blank after "Fer", and he may have stopped there. The supplied i is not counted among the 477 signs.
- **Row 2, first sign.** This is clearly b, so the literal is "bivanom", normalized "kívánom" as a slip.
- **Calls resting on word sense only.** Row 19, p of "előléptetés" (d shape). Row 23, d of "de" (h shape). Row 21, first sign, a v with extra strokes across it. Row 2, g of "egezeg", under the postmark. Row 26, s of "sirig", shaped nearer k.
- **Row 17, á of "sajnálom".** Two heavy bars joined by a connector, the least clean of the signs corrected in review.
- **Row 14 "elsimulj"** is taken as "elsimuljon", and rows 15 and 18 "ijes mit" as "ilyesmit". "bejegyzi" is kept, though "bejegyzik" ("they enter") is possible.
- **Spelling.** The writer mostly drops letters: szereret, aljob egezeg, regel, orakkor, sanálom, büntetes. Word division and accents are editorial, and the ledger does not record every faint mark.

## Review summary

Reviewer: Claude Opus 5.5, a separate agent, round 1, verdict **REVISE**. It ran the command, decoded the ledger with its own table, and read the whole text block again at 2x to 7x. It confirmed the key, the language and the story, but found that the ledger was not a faithful transcription. Its 14 findings were all accepted:

- **Eight sign corrections.** Row 7: "mert ez" became "mert az" and "mitotottem" became "mitotottam". Row 3: "talelja" became "talalja". Row 8: "orável" became "orával". Row 17: "sanélom" became "sanálom". Row 21: "romt" became "ront". Row 26: "seríg" became "sirig". Row 15: a faded six was added at the start, giving "töb|bet".
- **Effect of these.** Six of them had been presented as the writer's misspellings. They were misreadings, so the description of the writer's habits changed from swapped vowels to mostly dropped letters. Only "ez" to "az" changed a word of the normalized text ("this one" became "that one").
- **Disclosure.** The word-sense calls listed above were added, and h and p were added to the key table.
- **Row 8.** The first version supplied "[később]" as if it were settled; both options are now kept.
- **Row 26.** The final i had been called a restoration of a smudge. It is now an editorial supply and was removed from the ledger, so the count stays 477 (one six added, one supplied i removed).
- **Marks and date.** Two marks were added to the ledger, its record of marks is now declared selective, and the postmark `913 DE` is used for dating.

The key, the story and the reading as a whole did not change, so no second review round was needed. The reviewer could not verify the sign under the row 1 blot, the word behind `dak`, whether row 8 meant earlier or later, or the second postmark.

## Credits

- **Claude Opus 5.5, 2026-11-02:** transcription, transfer of the family key, decipherment, response to review and this report.
- **Claude Opus 5.5, separate reviewer agent:** independent review.
- **OpenAI GPT (GPT-6 Astra / GPT-6.1 Sol) and Claude Opus 5.5, on earlier family cards:** reconstruction of the Jolánka key. Neither worked on this card before 2026-11-02.

## Sources

- HC Portal record 1230, General, Description and Attachments tabs, captured 2026-11-02: https://crypto.hcportal.eu/dashboard/cryptograms/1230 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/3750/cpc_1913-12-_HU__HU_Jasz-Arokszalas_jolanka-116_pic.jpg (work/hires/; conversion in source/picture-large.jpg).
- Address side: https://api.hcportal.eu/media/3751/cpc_1913-12-_HU__HU_Jasz-Arokszalas_jolanka-116_adr.jpg (work/hires/; conversion in source/address-large.jpg).
- Family key: ciphers/hcp-1216 and sister cards in this repository.
