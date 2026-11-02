# hcp-1173 solution: PARTIAL

Solver: Claude Opus 5.5, 2026-11-02. No earlier work on this number. The portal attaches no solution or transcription. The HistoCrypt article linked by the portal was not checked for this card.

Status: the cipher is fully read, but two words of the open (unenciphered) text are unread. By the brief's standard this card is not complete, so no DONE marker and no register entry.

## Cipher type and key

Hungarian plain text with only the salutation and the signature enciphered (MASC): the digit-plus-mark key of hcp-1174, used here as a transfer, not rebuilt. Attested here:

`1` i, `1.` a, `1:` e, `1'` (high dot) á, `:1` (dots left) ü/ű, `3` d, `3,` r, `3.` v, `4,` g, `5` h, `7` k, `7,` s, `8` m, `8,` t, `9` p.

## Ciphertext (read at 3-4x from work/hires)

- Top line: `7 1: 3 3. 1: 7, 8 1. 3, 4, 1 8, 7 1' 8 !` = Kedves Margitkám!
- Last line, after open `maradok`: `5 :1 7 1: 3 3. 1: 7, 1: 3 ) 1' 3, 9 1' 3 )` = hű kedvesed) Árpád)

All 30 signs decode by the table as written, with no exception.

## Plaintext (Hungarian; [ ] = enciphered; punctuation partly editorial)

[Kedves Margitkám]!

Szerencsésen haza értem, nagyon szép idő volt, jól meg volt fagyva a sár, kocsira nem <UNREAD WORD 1> de még jobb, mert szét rázott volna. Elég hamar haza értem, hat óra után tíz perccel. Egész úton egy élő lénnyel sem találkoztam. Most midőn e lapot írom, este három negyed tíz óra van, a gyerekek alszanak, én pedig a kis asztal mellett gondolkodva ülök és írok. Pistának is most írok egy lapot. (Mezőkövesd) 1916. V/25.

Itt, benn e szívbe lész te zárva,
S itt senki másnak nincs helye,
Hő szerelmem sugarába
Senki más nem fürödhete.

Számtalanszor csókollak <UNREAD WORD 2> és mindnyájatokat maradok [hű kedvesed]) [Árpád])

Address: Őnsg. / Rózsa reményű / Sziber Margitka / kisasszonynak / Szomolya / u. p. (Bogács).

## English translation

[Dear Margitka]! I got home safely, the weather was very fine, the mud was well frozen, on a cart I did not [unread word], but even better, for it would have shaken me to pieces. I got home soon enough, ten minutes past six. On the whole way I did not meet a single living being. Now as I write this card it is a quarter to ten in the evening [literally three quarters of ten], the children are asleep, and I sit at the little table thinking and writing. I am writing a card to Pista now too. (Mezőkövesd) 25 May 1916.

Here, inside this heart you will be locked, / and here no one else has a place; / in the rays of my ardent love / no one else may bathe.

Countless times I kiss you [unread word] and all of you, I remain [your faithful sweetheart]) [Árpád])

## Slovak translation

[Drahá Margitka]! Šťastne som došiel domov, bolo veľmi pekné počasie, blato bolo dobre zamrznuté, na voz som ne[neprečítané slovo], ale ešte lepšie, lebo by ma bol rozdrvil natriasaním. Domov som prišiel dosť skoro, desať minút po šiestej. Po celej ceste som nestretol ani živú dušu. Teraz, keď píšem tento lístok, je večer trištvrte na desať, deti spia a ja sedím pri stolíku, rozmýšľam a píšem. Aj Pistovi teraz píšem lístok. (Mezőkövesd) 25. mája 1916.

Tu, v tomto srdci budeš zamknutá / a nikto iný tu nemá miesto; / v lúčoch mojej vrúcnej lásky / sa nikto iný nesmie kúpať.

Nespočetnekrát ťa bozkávam [neprečítané slovo] a všetkých vás, zostávam [tvoj verný milý]) [Árpád])

## Command

From the repo root:

    python3 -I ciphers/hcp-1173/work/decode.py

It checks the four hashes, decodes every sign with asserts, and prints the text. The open text is hard-coded.

## Uncertainties

Blocking:

1. Word 1 (line 4, after `kocsira nem`). `work/crops/z_k1.png`, `i_k.png`. Seen: a round letter, a descender, a tall k-like letter, one or two small letters, then an ending `-ltam` or `-dtam`. Compared with the card's `gondol-` it is not `gondoltam`, because of the k (`work/crops/cmp_g.png`). `akadtam`, `kapkodtam` and `kapaszkodtam` were tried; none fits the letter count, though the last two would suit the sense (getting onto a cart). A brown stroke covers the area where a first letter k could stand. Its first-person past ending is reasonably sure; the verb is not.
2. Word 2 (line after `Számtalanszor csókollak`). `work/crops/z_w1.png`, `i_u.png`. Seen: tall letter, e-like, a descender (z or g), e-like, o-like, two tall letters, and a final letter with a long top bar, most like t. It looks like `legeollet`, which is not a word. `üdvözöllek` would give the best grammar (it would govern `mindnyájatokat`) but the letters do not match in count and the end is not k. `üdvözlet` also fails. If this word is the verb, the clause's meaning is not secured; my translation assumes `csókollak` covers it.

Minor:

3. `jobb`: first letter j-like and the two b are blurred under strokes; the sense settles it, and the shape alone is weak.
4. `1'` in the first letter of Árpád has its dot at mid-height, not high. The rest of the word and sister hcp-1174 fix it.
5. The `)` after `kedvesed` and after `Árpád` have no opening partner on the card, and are much longer than the comma on `3,`. They are taken as punctuation, as on hcp-1174.
6. `hű`: `:1` stands for ű here; the sign is ü on hcp-1174. The long vowel is not marked.
7. Date: `1916` is under strokes. Postmark fragments show 5 and 2-like digits and are not fully read. `1916. V/25` agrees with the file name in the portal image.
8. The large brown loops and letters over both sides, and the strike-outs, are later and not part of the message; I did not try to read them.
9. `fürödhete` is read as written; normal `fürödhet` plus an -e, likely for the rhyme with `helye`.

## Why the reading is right so far

The one fixed key gives Kedves Margitkám, hű kedvesed and Árpád, all without exception, and hcp-1174 has the same salutation pattern and signature. The open text is coherent, and the writer's verse rhymes (zárva / sugarába, helye / fürödhete).
