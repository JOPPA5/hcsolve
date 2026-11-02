# HCP 1144: a Hungarian love letter in cipher from Árpád to Margitka Sziber

Human solver: Tomáš Pavuk

**Status: deciphered, one word unread (456 cipher signs; 445 by the table, 10 taken by sense, 1 blot); independent review 1 verdict REVISE, all findings addressed.** Report dated 2026-11-02.

## Origin and context

The cryptogram is record 1144 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1144), portal name cpc_1916-05-19_HU_Mezokovesd_HU_Szomolya_szomolya-36, part of Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-11-02 the portal listed it as **Not solved**, tagged Postcard, T. Schrödel Collection, category Substitution, language and sender Unknown, recipient Margitka Sziber, with no transcription or solution attached.

It is a picture postcard of a park pond with a small house and a bridge. The picture side carries no writing. The address side is in open script: **Őnagysága / Sziber Margitka / kisasszonynak / Szomolya / (u.p. Bogács) / (Borsod m.)**, that is, "Her Ladyship Miss Margitka Sziber, Szomolya, post office Bogács, Borsod county", in north-eastern Hungary. The open heading reads **Mezőkövesd, 1916. V/19.** (19 May 1916, wartime). The card carries a 5-fillér stamp.

The whole message on the left half of the address side is in cipher, 25 rows of digits with small marks. This differs from the sister cards hcp-1174, 1178 and 1179 in the same correspondence, where only key words are enciphered inside plain Hungarian. The writer signs Árpád, in cipher, as on hcp-1174.

![Address side with the cipher rows at left and the open address at right (source/address-large.jpg)](../source/address-large.jpg)

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

No earlier work exists on this number in this repository, and no published solution of this card was found. The HistoCrypt article linked from the portal (https://ecp.ep.liu.se/index.php/histocrypt/article/view/166) was not read, so it is not known whether it discusses this card.

## Method

The card was read by hand, by an AI model, from the high-resolution original of the address side, in tiled and enlarged crops. The transcription lists every sign row by row; no OCR was used. The order of the rows needed care: at the bottom right a drawn curve routes the main line "érzem én" to "magamat" at bottom left, and the rows right of the curve are the closing formula.

The key was **transferred and extended**. Its core comes from the finished sister card hcp-1174, where it was reconstructed. New signs on this card were each fixed by words that recur: 2 = c (címét), `4.` = gy (hogy, légy, nagy, nagyon, úgy, egyebet), 6 = j (lejösz, ajkam, jöjetek, Jani), `6.` = ny (fényképész, enyém), `5.` = ly (milyen), `.1` = u (szervusz, úgy). The value 4 = f comes from a suggestion on hcp-1175 and is confirmed here (fényképész, fogtok).

The reproduction script checks the hashes of the scans, decodes the transcription sign by sign, asserts each row against the stated reading, and prints the text.

## Key

Monoalphabetic substitution (register label MASC). One letter is one digit plus an optional mark, and the mark is part of the sign; a comma, dot or colon changes the letter. Hungarian digraphs (cs, gy, ly, ny, sz) have one sign each. Long and short o, i, u are not told apart, but o/ö, a/á and e/é are. There are no word divisions; `)` occurs a few times as a separator.

| Sign | Letter | Sign | Letter | Sign | Letter |
|---|---|---|---|---|---|
| 0 | o, ó | 3 | d | 6 | j |
| 0, | ö, ő | 3, | r | 6, | n |
| 1 | i, í | 3. | v | 6. | ny |
| 1. | a | 4 | f | 7 | k |
| 1: | e | 4, | g | 7, | s |
| 1' (high dot) | á | 4. | gy | 7. | sz |
| 1, | b | 5 | h | 8 | m |
| :1 (dots left) | ü, ű | 5, | l | 8, | t |
| .1 (dot left) | u | 5. | ly | 9 | p |
| 2 | c | | | 9, | z |
| 2, | cs | | | | |
| 2. | é | | | | |

One difference from the family: hcp-1179 reads `5.` as l in one word. Here it occurs once, in milyen, where l would not fit.

## Plaintext

Open heading: Mezőkövesd, 1916. V/19.

Hungarian, in the card's own spelling. Word division, punctuation and accents on o, i, u are editorial, except that the ! after Margitkám and the hyphens at line ends are on the card (they are not cipher signs).

**Édes Margitkám!**

**Ha e lapot megkapod, légy szíves értesíteni, hogy lejösz, avagyis lejöttök-e kedves ángyikával vasárnap a fényképészhez, mert azt montad, mikor ott voltam, hogy most vasárnap fogtok lejönni. Tehát hacsak lehet, jöjetek, mert úgy is soká lesz kész, az enyém is csak pünkösdre lesz meg. Janinak még most sem írtam, mert nem lá[s?]ninol a címét. Most egyebet nem írok. Szervusz.**

**Milyen nagyon nagy a tenger,**

**De nagyobb a szerelem,**

**A tengernek van határa,**

**A szerelem végtelen.**

**Hogy ha ajkam ajkadra rátapad,**

**menyországban érzem én magamat.**

**Számtalanszor ölel, csókol és üdvözöl hű kedvesed (Árpád)**

Standard spelling would give mondtad, jöjjetek, mennyországban.

English translation:

Sweet Margitka!

When you get this card, please let me know whether you are coming down, that is, whether you are coming down with your dear ángyika (sister-in-law or aunt by marriage) on Sunday to the photographer, because you said when I was there that you would come down this Sunday. So if at all possible, come, because it will take long to be ready as it is; mine too will only be done by Whitsun. I still have not written to Jani, because [unread word: "lá[s?]ninol"] his address. I write nothing more now. Cheerio.

How very great is the sea,

But greater is love;

The sea has its bounds,

Love is endless.

When my lips press onto yours,

I feel myself in heaven.

Countless times embraced, kissed and greeted by your faithful sweetheart (Árpád)

Slovak translation:

Moja sladká Margitka!

Keď dostaneš tento lístok, buď taká dobrá a daj mi vedieť, či prídeš dolu, teda či prídete s milou ángyikou (švagrinou alebo tetou) v nedeľu k fotografovi, lebo si povedala, keď som tam bol, že prídete túto nedeľu. Takže ak sa len dá, príďte, lebo aj tak to bude dlho hotové; aj moja bude až na Turíce. Janimu som ešte stále nenapísal, lebo [neprečítané slovo: „lá[s?]ninol“] jeho adresu. Teraz už nič iné nepíšem. Servus.

Aké veľmi veľké je more,

ale väčšia je láska;

more má svoju hranicu,

láska je nekonečná.

Keď sa moje pery prilepia na tvoje,

cítim sa ako v nebi.

Nespočetnekrát ťa objíma, bozkáva a pozdravuje tvoj verný milý (Árpád)

The plan fits the place and date: "lejösz" (come down) is the trip from Szomolya down to Mezőkövesd, matching "felmegyek" for the opposite direction on hcp-1174, and 19 May 1916 falls before Whitsun, 11 June 1916. The rhymes szerelem/végtelen and rátapad/magamat stand as written.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1144/work/decode.py
```

The script checks the SHA-256 of all four scans, decodes work/transcription.txt with the key, asserts that all 25 rows match, and prints the text and the address. The current output line is "all 25 rows match; 456 cipher signs, 445 by the table, 11 by sense or doubtful". The clean text with punctuation and the open address are held in the script; the checked part is the sign-for-sign reading. The transcription step itself is manual.

## Uncertainties

- **One unread word.** Before "a címét" the card has `5, 1' ? 6, 1 | 6, 0 5,` across a line end, read lá[s?]ni-nol. The á and the "nol" are clear, so this is not a misread "hol". The third sign is an overwritten blot with a flat top, a notch and a separate tail; 7, (s) and 3, (r) are about equally likely and 8, (t) is not excluded. With t the signs give "látni", and with a slip "nem látni, hol" ("not to be seen where"), but that is a hypothesis only, and címét would be the wrong case for it. It may be one word or two. The sense is only that the reason concerns Jani's address. No reading is forced; the rest of the card reads.
- **Signs taken by sense** (10, marked ~ in the transcription): the second é of fényképészhez, close to `9.`; the e of szervusz, a blot with only its upper dot showing; the e of menyországban, a 1 with a short thick stroke; the ó of csókol, drawn like a tall 6; the ü of üdvözöl, with one dot left, so literally udvözöl; its two ö, 9-shaped joined 0 as on hcp-1174; the s and ü of pünkösdre, whose marks are a short oval and a merged blob; the ü of hű, whose lower dot could be the comma of the 5.
- **Softer but table-shaped:** the s of értesíteni under the postmark, which has a visible crossbar and tail; the short slanted mark on the first é of fényképészhez.
- `.1` = u rests on this card alone (szervusz, úgy, and the drawn form of üdvözöl); it was removed from the reviewed key on hcp-1178.
- "Hogy ha" may be the single word hogyha.
- Not established: who Jani is (an ordinary male pet name for János), what relation ángyika means here, whether the verse has a printed source, and whether the HistoCrypt article treats this card.
- Language and sender are Unknown on the portal; Hungarian and Árpád come from this reading.
- Not all 456 signs were checked at 3x or more. The review found two single-mark slips in its comparison, so a few more could remain.

## Review summary

Reviewer: a separate Claude Opus 5.5 agent, round 1, verdict **REVISE**. It ran the reproduction command, decoded with its own independently typed key (all 456 tokens keyed), compared the key with the sister cards, read all rows at 2x and doubtful places at 3 to 6x, and checked the row order and context. It judged the text real Hungarian, not forced. What changed because of it:

- **Jani, not Nani.** The first sign of the name is a plain 6 (j) with no tail. The person is therefore a man and "her address" became "his address".
- **úgy, not így.** A dot stands left of the 1, so "mert úgy is soká lesz kész". The translation hardly changes.
- **Counts.** The clean count fell from 450 to 445 because signs not drawn as in the table are now marked as taken by sense.
- **Soft calls listed.** pünkösdre, hű and fényképészhez are now listed.
- **Unread word.** The other candidates for the blot are now stated; no reading was adopted.
- **Punctuation.** The ! and the line-end hyphens are now said to be on the card.

No key value changed. Both misreadings came from the solver's transcription and were not disclosed before the review.

![The first sign of Janinak, a plain 6 with empty paper below (review/work/crops/nan2.png)](../review/work/crops/nan2.png)

![The dot left of the 1 in úgy (review/work/crops/igy.png)](../review/work/crops/igy.png)

![The blot in the unread word, third sign (review/work/crops/blot.png)](../review/work/crops/blot.png)

## Sources

- HC Portal record 1144, General, Description and Attachments tabs, captured 2026-11-02: https://crypto.hcportal.eu/dashboard/cryptograms/1144 (source/metadata.md).
- Scans: https://api.hcportal.eu/media/3492/ (picture side) and https://api.hcportal.eu/media/3493/ (address side); originals in work/hires/, listed with hashes in SOURCES.md.
- Key: finished sister cards in this repository, ciphers/hcp-1174, hcp-1178, hcp-1179, and a suggestion on hcp-1175.
