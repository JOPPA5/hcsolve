# hcp-1144 solution (round 1, corrected after review 1)

Solver: Claude Opus 5.5, 2026-11-02. No earlier work on this number. The portal lists the card as Not solved with no solution attached. The HistoCrypt article the portal links was not checked for this card, so I cannot say whether it discusses it. No published solution of this card turned up.

## Card

Picture postcard of a park pond, 1916-05-19 by the collection's file name; the card's own date reads Mezőkövesd, 1916. V/19 in open script. Addressed in open script to Őnagysága Sziber Margitka kisasszonynak, Szomolya (u.p. Bogács), (Borsod m.). The whole message is in cipher, unlike hcp-1174, 1178 and 1179 where only key words are. It is signed Árpád, in cipher, as on hcp-1174.

The pixels were read from the hires address side; the transcription is `work/transcription.txt`, 25 cipher rows in the order read. The block at bottom right is set off by a drawn curve: the main line "érzem én" runs along the bracket to "magamat" at bottom left, and the rows right of the curve are the closing formula.

## Cipher type and key

Register label: MASC. One letter is one digit plus an optional mark, and the mark is part of the sign. Hungarian digraphs have one sign. There are no word divisions; `)` occurs a few times as a separator.

| sign | letter | sign | letter | sign | letter |
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

Key source: the table on FINAL card hcp-1174, plus hcp-1175's suggestion 4 = f. New on this card and fixed by its own words: 2 = c (címét), 4. = gy (hogy, légy, nagy, nagyon, úgy, egyebet), 6 = j (lejösz, ajkam, jöjetek, Jani), 6. = ny (fényképész, enyém), 5. = ly (milyen), `.1` = u (szervusz, úgy; this value rests on this card alone, since `.1` = u was removed from the reviewed key on hcp-1178), and 1, = b already on hcp-1179 (nagyobb, egyebet, országban). One difference from the family: hcp-1179 reads `5.` as l in "legszeb(b)"; here `5.` occurs once, in milyen, where l would not fit.

## Plaintext (Hungarian, card's own spelling; word division, punctuation and accents on o, i, u are mine)

Open heading: Mezőkövesd, 1916. V/19.

Édes Margitkám!
Ha e lapot megkapod, légy szíves értesíteni, hogy lejösz, avagyis lejöttök-e kedves ángyikával vasárnap a fényképészhez, mert azt montad, mikor ott voltam, hogy most vasárnap fogtok lejönni. Tehát hacsak lehet, jöjetek, mert úgy is soká lesz kész, az enyém is csak pünkösdre lesz meg. Janinak még most sem írtam, mert nem lá[s?]ninol a címét. Most egyebet nem írok. Szervusz.

Milyen nagyon nagy a tenger,
De nagyobb a szerelem,
A tengernek van határa,
A szerelem végtelen.

Hogy ha ajkam ajkadra rátapad,
menyországban érzem én magamat.

Számtalanszor ölel, csókol és üdvözöl hű kedvesed (Árpád)

Normal spelling would give mondtad, jöjjetek, mennyországban. The ! after Margitkám and the hyphens at line ends (for example after értesíte-) are drawn on the card and are not cipher signs; all other punctuation is mine.

## English translation

Sweet Margitka!
When you get this card, please let me know whether you are coming down, that is, whether you are coming down with your dear ángyika (sister-in-law or aunt by marriage) on Sunday to the photographer, because you said when I was there that you would come down this Sunday. So if at all possible, come, because it will take long to be ready as it is; mine too will only be done by Whitsun. I still have not written to Jani, because [unread word: "lá[s?]ninol"] his address. I write nothing more now. Cheerio.

How very great is the sea,
But greater is love;
The sea has its bounds,
Love is endless.

When my lips press onto yours,
I feel myself in heaven.

Countless times embraced, kissed and greeted by your faithful sweetheart (Árpád)

## Slovak translation

Moja sladká Margitka!
Keď dostaneš tento lístok, buď taká dobrá a daj mi vedieť, či prídeš dolu, teda či prídete s milou ángyikou (švagrinou alebo tetou) v nedeľu k fotografovi, lebo si povedala, keď som tam bol, že prídete túto nedeľu. Takže ak sa len dá, príďte, lebo aj tak to bude dlho hotové; aj moja bude až na Turíce. Janimu som ešte stále nenapísal, lebo [neprečítané slovo: „lá[s?]ninol“] jeho adresu. Teraz už nič iné nepíšem. Servus.

Aké veľmi veľké je more,
ale väčšia je láska;
more má svoju hranicu,
láska je nekonečná.

Keď sa moje pery prilepia na tvoje,
cítim sa ako v nebi.

Nespočetnekrát ťa objíma, bozkáva a pozdravuje tvoj verný milý (Árpád)

## Command

Run from the repo root:

    python3 -I ciphers/hcp-1144/work/decode.py

It checks the SHA-256 of all four scans, decodes `work/transcription.txt` sign by sign with the key above, asserts that every row equals the stated reading, and prints the plaintext and the address. The verified rows are the sign-for-sign reading; the printed clean text with punctuation and the open address are held in the script.

## Uncertainties

1. The one unread word: `5, 1' ?7, 6, 1 | 6, 0 5,` at a line end, read "lá[s?]ni-nol", followed by "a címét". The dot on the second sign is a single high one, so á stands; the 6, and 5, of "nol" are clear, so it is not a misread "hol". The third sign is a heavy blot with a flat top, a notch at right and a separate tail; 7, and 3, are about equally likely and 8, (t) is not excluded. With 8, the signs give "látni", and with a slip "nem látni, hol" ("not to be seen where"), but that is only a hypothesis and címét would be the wrong case for it. The group may be one word or two. The sense is clear only as a reason concerning Jani's address (the expected verb, such as "tudom", is not what the signs give). I did not find a reading and do not force one. The word stands alone; the rest of the card reads.
2. Signs that are not clean, taken by sense (those drawn as another sign are marked ~ in the transcription):
   - értesíteni, the 7, sits under the postmark and could look like 3,; only s makes the word.
   - fényképészhez, the é after p looks close to 9. but 2. makes the word. The mark on the first 2 of this word is short and slanted; é is sound.
   - szervusz, the 1: is a heavy overwritten blot; its upper dot shows.
   - menyországban, the second sign is a 1 followed by a short thick stroke, taken as a smeared colon (1:). The n is spelled once.
   - csókol, the second sign looks like a tall 6 (j); 0 expected. Only ó makes the word, and csókol is on the sisters as 2, 0 7 0 5,.
   - üdvözöl, the first sign shows one dot left of the 1, so it is written like the u of szervusz and úgy; literally udvözöl. The two ö-signs are the 9-shaped joined 0, also seen on hcp-1174, not table shapes.
   - pünkösdre, the mark on the 7 is a short oval, between the long tail of 7, and the dot of 7.; only s makes the word. In the same word the left marks of :1 merge into one blob with the foot of the 1, and ü is taken by sense.
3. `hű` depends on two dots left of a 1 whose top joins the flag of the 5; the lower dot could also be read as the 5's comma, which would give "l" + a. hű kedvesed is the only reading that makes a word, so the sign is counted as by sense. The 5 1. in "hogy ha" has an extra left stroke on the 1.
4. Which words are one: "hogy ha" may be the single word hogyha; "ha e lapot" could be read otherwise only with nonsense.
5. Whether the lovers' verse has a printed source was not investigated. "ángyika" is rendered generally; the relation is not known, and who Jani is (an ordinary pet name for János, male) is not known either; no other Mezőkövesd card checked names him. "lejösz" (come down) refers to going down to Mezőkövesd from Szomolya, consistent with hcp-1174's "felmegyek" for the opposite direction.
6. Portal language and sender fields are Unknown; Hungarian and Árpád come from this reading.

## Why I believe it is correct

The key was carried over from hcp-1174 and earlier, and the running text of 456 signs decodes into connected Hungarian with very few exceptions. The new signs were each fixed by words that recur, and each gives further words elsewhere (gy in six words, b in three, j also in the name Jani). The text fits the context: the same Árpád and the same pet name as hcp-1174, the card's date of 19 May 1916 before Whitsun (11 June 1916), a planned Sunday trip from the Szomolya side down to Mezőkövesd to the photographer, and rhymed love verse (szerelem/végtelen, rátapad/magamat) as on hcp-1174.

## Response to review 1

Verdict REVISE. I re-read every cited spot on the crops at 3 to 6x. All six findings are accepted and fixed. The reading is not substantially changed: two signs change, one word and one name, and no key value changes. After the fixes `python3 -I ciphers/hcp-1144/work/decode.py` reports 4 hashes OK, "all 25 rows match; 456 cipher signs, 445 by the table, 11 by sense or doubtful".

1. Jani, not Nani: fixed. On `review/work/crops/nan2.png` and `nani.png` the first 6 of the word is a plain closed 6 with empty paper below it, while the next 6 of the same word has its long tail. The word is `6 1. 6, 1 6, 1. 7` = janinak. Transcription row 10, the READ list and held text of decode.py, the plaintext and both translations are corrected. Since Jani is a man's pet name, "her address" became "his address" and Slovak "jej adresu" became "jeho adresu", "Nani som" became "Janimu som". Uncertainty 1 no longer mentions Naninól, and Jani is added to the attestations of 6 = j. My first reading was simply wrong.
2. úgy, not így: fixed. On `crops/igy.png` a clear round dot stands left of the 1, under its flag, the same mark as in szervusz. Row 8 is now `.1 4.`, the plaintext reads "mert úgy is soká lesz kész", and the key list cites úgy for gy. The translations already fit ("as it is", "aj tak").
3. Counts: fixed. The two 9-shaped ö of üdvözöl are marked `0,~ö` and the sign `.1~ü` was already marked, so the 450 no longer includes them.
4. Soft calls: fixed. pünkösdre's s and ü are marked `~` and listed in uncertainty 2, with the slanted mark in fényképészhez. I also marked the ü of hű `~`, since uncertainty 3 already says it rests on sense. These with finding 3 account for the change from 450 to 445 clean signs.
5. Unread word: fixed in wording. Uncertainty 1 now gives 7,, 3, and 8, as candidates for the blot, the "látni, hol" hypothesis with its case problem, the possibility of two words, and why "nol" is not a misread "hol". On `crops/blot.png` I agree: it looks overwritten and cannot be decided. I still force no reading. The word stands alone and the rest of the card reads.
6. Punctuation: fixed. The plaintext note and the note printed by decode.py now say that the ! after Margitkám and the line-end hyphens are on the card and are not cipher signs.

Still not verified, as the reviewer says: the HistoCrypt article linked from the portal was not read, so whether it treats this card is unknown; the source of the verse; the meaning of ángyika here; the identity of Jani. The reviewer's caution that a few single-mark slips could remain among the 456 signs stands: the signs were not all checked at 3x or more.
