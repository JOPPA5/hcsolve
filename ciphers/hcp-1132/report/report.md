# HCP 1132 (cpc_--_HU_Debrecen_HU__): a Hungarian love note in Morse code, Debrecen

Human solver: Tomáš Pavuk

**Status: read in full (21 Morse columns and one bottom line); independent review 1 verdict ACCEPT, no decoded letter changed.** Report dated 2026-11-03.

## Origin and context

The cryptogram is record 1132 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1132), portal name cpc_--_HU_Debrecen_HU__, part of Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-11-03 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, language Unknown, sender Unknown, recipient "Södy Sandoz", with no transcription or solution attached.

The picture side is a Hungarian photographic postcard, "Libapásztorleány / Gänsemädchen / Goose-herd Maid" (a girl herding geese), published by Hafa, Budapest, from a photograph by Debreczeny József, no. 173. It carries no handwriting.

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

The address side carries a 6 fillér stamp of the Magyar Királyi Posta, "Debreceni Collegium 1538-1938", the 1938 issue, cancelled DEBRECEN. The date in the postmark cannot be read, so the card was posted in 1938 or later. The address is in plain Hungarian cursive: **Tek. Sődy Sándor / fodrász m. urnak / H. / Csapó ucca 97. szám**, that is, "To Mr Sándor Sődy, master hairdresser, local (Helyben, here Debrecen), Csapó Street no. 97". Csapó utca is a street in Debrecen. A pencilled "200" is probably a dealer's price.

![Address side: Morse field on the left, address and the Debrecen Collegium stamp on the right (source/address-large.jpg)](../source/address-large.jpg)

Upside down at the top of the address half is a short plain note, **"Vigyázz a kis libákra !!!"**, "Watch out for the little geese!!!". It is a joke on the picture: "kis liba" (little goose) is also Hungarian slang for a silly young girl.

![The plain note, turned upright: "Vigyázz a kis libákra !!!" (work/crops/note_upright.png)](../work/crops/note_upright.png)

The whole left half of the address side is filled with pen dots and dashes. That is the hidden message.

## Method

The dots and dashes stand in **21 vertical columns**, and a few more marks run along the bottom edge. Turn the card 90° anticlockwise. The printed "Copyright Hafa ..." line then stands upside down along the top of the field, and the columns become lines read left to right. The right-most column of the card is read first, each column from top to bottom. When the writer ran out of room, the message went on along the bottom edge of the card, read left to right in the card's normal orientation.

![The Morse field turned 90° anticlockwise into reading orientation; the first line reads ÉDES JO KIS (work/crops/morse_reading.png)](../work/crops/morse_reading.png)

A dot is a short round blob. A dash is a stroke about 30-110 px long in the 3468 px scan. Letters are separated only by larger gaps (about 45-120 px, against 12-40 px inside a letter). Words are not separated at all and run on across columns. Every column was transcribed by eye from 3-5× enlarged crops of the original high-resolution scan. The columns on the left lean by up to 100 px, which defeated an automatic column split. The transcription was then decoded with a small script.

The code is ordinary **International Morse** with the usual Hungarian extensions. It is not a secret cipher: there is no key, and anyone who knows Morse can read it. The writer's concealment relies on the reader not recognising Morse. Hungarian digraphs are sent letter by letter (SZ as S+Z, CS as C+S, GY as G+Y, NY as N+Y), and Ó is sent as plain O. Punctuation is written as small marks in the reading orientation. A short stroke beside a column is a comma, and a stroke with a dot is an exclamation mark. One stretch of column 10 is struck through by the writer.

## Key (Morse letters used)

| Letter | Morse | Letter | Morse | Letter | Morse |
|---|---|---|---|---|---|
| A | .- | I | .. | R | .-. |
| Á | .--.- | J | .--- | S | ... |
| B | -... | K | -.- | T | - |
| C | -.-. | L | .-.. | U | ..- |
| D | -.. | M | -- | V | ...- |
| E | . | N | -. | Y | -.-- |
| É | ..-.. | O | --- | Z | --.. |
| F | ..-. | Ö | ---. | | |
| G | --. | P | .--. | | |
| H | .... | | | | |

## Plaintext

Decoded column by column (C1 is the right-most column of the card; BL is the line along the bottom edge):

```text
C1   ÉDES JO KIS          C12  BA, MAJD RÖ
C2   URAM! KEDVES         C13  VIDESEN ELMON
C3   SORAID MEG           C14  DOM, SOKAT,
C4   KAPTAM! BO           C15  GONDOLVA
C5   CSÁS MEG É           C16  RÁD, SZÁM
C6   DESEM HOGY           C17  TALANSZOR
C7   ÉN NEM VÁLA          C18  CSOKOL KI
C8   SZOLTAM SO           C19  S FELESÉGED
C9   RAIDRA DE SOK        C20  ANYA ESTE VÁ
C10  SOK MINDEN, [struck out]   C21  RLAK!! TÁNCO
C11  ÉRT MOSTANÁ          BL   LUNK
```

Hungarian as written (word breaks editorial, punctuation as on the card):

ÉDES JO KIS URAM! KEDVES SORAID MEGKAPTAM! BOCSÁS MEG ÉDESEM HOGY ÉN NEM VÁLASZOLTAM SORAIDRA DE SOK SOK MINDEN, [struck out] ÉRT MOSTANÁBA, MAJD RÖVIDESEN ELMONDOM, SOKAT, GONDOLVA RÁD, SZÁMTALANSZOR CSOKOL KIS FELESÉGED ANYA ESTE VÁRLAK!! TÁNCOLUNK

Normalised Hungarian:

**Édes jó kis uram! Kedves soraid[at] megkaptam! Bocsás[s] meg, édesem, hogy én nem válaszoltam soraidra, de sok-sok minden ért mostanába[n], majd rövidesen elmondom. Sokat gondolva rád, számtalanszor csókol kis feleséged, Anya. Este várlak!! Táncolunk.**

English translation: **My sweet, good little husband! I have received your dear lines! Forgive me, darling, for not answering your lines, but lots and lots of things have happened to me lately; I'll tell you about it soon. Thinking of you a lot, your little wife, Anya ("Mum"), kisses you countless times. I'll be waiting for you this evening!! We'll dance.**

Plain note: **Watch out for the little geese!!!**

Slovak translation: **Môj sladký, dobrý malý mužíček! Tvoje milé riadky som dostala! Odpusť mi, zlatko, že som ti na tvoje riadky neodpovedala, ale v poslednom čase sa mi stalo veľa, veľa vecí; čoskoro ti to porozprávam. S myšlienkami na teba ťa nespočetnekrát bozkáva tvoja malá manželka, Anya („mamka“). Večer ťa čakám!! Budeme tancovať.**

Plain note: **Pozor na malé husky!!!**

Notes on the reading:

- "uram" (my husband, literally "my lord") and "kis feleséged" (your little wife) show that a wife is writing to her husband, the hairdresser named in the address.
- The spellings are the writer's own: BOCSÁS for standard bocsáss, SORAID MEGKAPTAM for soraidat, MOSTANÁBA, a colloquial or eastern form of mostanában, and JO / CSOKOL for jó / csókol, because Ó is sent as O.
- ANYA ("Mum") is read as the wife's signature or pet name, as Hungarian wives often signed to their husbands. A personal name cannot be excluded.
- Three plain question marks "? ? ?" stand upright at the bottom centre of the Morse field, in the card's normal orientation. They belong to no column, and are probably a teasing "can you read it?".

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1132/work/decode.py
```

The script uses only the Python standard library. It checks the SHA-256 hashes of both portal images and both high-resolution originals. It then decodes the manual transcription in work/transcription.txt with International Morse plus the Hungarian letters É, Á and Ö, and prints the 21 columns, the bottom line and a run-on line. It does not read the image: the transcription step is manual, and the reviewer checked it independently.

## Uncertainties

- **Letter boundaries** are marked only by gap size, and the sizes overlap in places. Three splits were chosen by word sense: the É of ÉDES in C1, the Y of HOGY in C6, and ANYA in C20 (`.- -. -.-- .-`). Without word sense, the gaps in C20 would allow the non-word "ANNMA".
- **End of C13 (ELMON-DOM).** The N is a single heavy, possibly retraced stroke at the bottom edge, with a thick upper part and a thickened foot. No separate dot can be seen. It is read as a dash and a dot run together, which is an inference from the word ELMONDOM.
- **A shared stroke (MOSTANÁBA / TÁNCOLUNK).** One continuous L-shaped stroke sits in the bottom corner. Its vertical arm is read as the last dash of the Á at the end of C11, and its horizontal foot as the last dash of the final K of the bottom line. This is an inference from word sense. It is the only split that gives words: without it, C11 would end in P and the bottom line in N, and neither gives a word.
- **The struck-through section of C10.** The writer struck through about five marks with a long line. They are not read. The small hooked stroke just before it is taken as a comma.
- **"!!" in C21.** Two dots and three short strokes stand between C20 and C21. Following the "!" of C2 and C4, they are read as "!!" after VÁRLAK. Placing them after ANYA would not change the sense.
- **Under the stamp.** There is no image of the card without the stamp. The stamp lies flat, and no ink shows at its edges. Cards of some other series in this collection hide writing under the stamp. Nothing on this card points to that, but it cannot be ruled out.
- The postmark date cannot be read. The card dates from 1938 or later, the year of the stamp issue.
- No published solution was found. The portal status was Not solved, the AI Decipherment Register had no record, and a web search found nothing.

## Review summary

Reviewer: Claude Opus 5.5 (Anthropic), a separate agent, round 1, verdict **ACCEPT**. The reviewer:

- ran the reproduction command (all hash checks OK, output identical to the claimed plaintext);
- decoded the transcription with its own independent Morse table and script, and got the same text with no invalid group;
- checked columns C1-C9, C20, C21, the bottom line and the bottom corner against its own enlarged crops of the scan;
- confirmed that the picture side has no writing, and that the text is coherent 1930s-40s Hungarian that fits the address, the picture and the 1938 stamp.

Its five findings were all minor:

- **Shared L-stroke and the heavy C13 stroke.** Keep them disclosed as inferences. They are kept above.
- **The plain note has three exclamation marks, not two.** Corrected: the note reads "libákra !!!" on an upright crop of the scan.
- **Letter splits by word sense.** They stay listed.
- **Type label MASC/Morse.** Kept, with the remark that Morse has no secret key.

On re-checking, the solver also corrected one sentence of its own description. In the reading orientation the printed Copyright line is upside down, not upright. The direction of the turn and the reading order were right. The human's collaborator asked whether writing is hidden under the stamp, as on the Árokszállás Jolánka cards. This card is from a different source and shows no such sign, so the type stays MASC/Morse and the possibility is listed as a limitation. **No decoded letter changed as a result of the review.**

All work on this card was done by Claude Opus 5.5 (Anthropic): capture, segmentation, transcription, identification of the code, decoding, the response to the review and this report. No earlier solver worked on this number.

## Sources

- HC Portal record 1132, General, Description and Attachments tabs, captured 2026-11-03: https://crypto.hcportal.eu/dashboard/cryptograms/1132 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/3456/conversions/cpc_--_HU_Debrecen_HU___pic-large.jpg (source/picture-large.jpg); original https://api.hcportal.eu/media/3456/cpc_--_HU_Debrecen_HU___pic.jpg.
- Address side: https://api.hcportal.eu/media/3457/conversions/cpc_--_HU_Debrecen_HU___adr-large.jpg (source/address-large.jpg); original https://api.hcportal.eu/media/3457/cpc_--_HU_Debrecen_HU___adr.jpg (work/hires/).
- Portal reference for the collection: https://ecp.ep.liu.se/index.php/histocrypt/article/view/166
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-11-03.
