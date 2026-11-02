# hcp-1135 solution (round 1)

Solver: Claude Opus 5.5, 2026-11-02. No earlier work on this number. The portal lists the card as Not solved with no solution attached. The HistoCrypt article the portal links was not checked for this card, so I cannot say whether it discusses it. A web search for the two verse lines found no published text. The transcription is mine, made from `work/hires/` (`work/transcription.txt`).

## Cipher type and key

Register label: MASC. It is the Mezőkövesd family key of hcp-1174, 1178 and 1179: each letter is a digit with an optional mark, and the mark is part of the sign. Unlike those cards, here almost the whole message is enciphered, with word spaces mostly kept. In clear stand only the first word of each verse line (Te, Te, U-, Be-, A, Te, Fogadd, S), a few letters inside it (b, g, m twice, l, d; see Uncertainties), the place and date, and the address.

| sign | letter | | sign | letter | | sign | letter |
|---|---|---|---|---|---|---|---|
| `0` | o, ó | | `2.` | é | | `6,` | n |
| `0,` | ö, ő | | `3` | d | | `6` | j (new) |
| `1` | i, í | | `3,` | r | | `6.` | ny (new) |
| `1.` | a | | `3.` | v | | `7` | k |
| `1:` | e | | `4,` | g | | `7,` | s |
| `1'` (high dot) | á | | `4.` | gy (new) | | `7.` | sz |
| `1,` | b | | `5` | h | | `8` | m |
| `:1` (dots left) | ü, ű | | `5,` | l | | `8,` | t |
| `.1` (one dot left) | u, ú (new) | | `5.` | l | | `9` | p |
| `2,` | cs | | | | | `9,` | z |

Key transfer: the first line, `2. 3 1: 7, 8 1. 3, 4, 1 8, 7 1' 8`, is the same salutation as on hcp-1174. All family signs were applied unchanged. The four new signs came out of this card: `.1` from husvét (twice), `4.` from hogy, vágyik, `6` from majd, jobbat, `6.` from szárnyán, lánykám. `.1` rests on one word, húsvét (twice); `6.` also stands twice in bájjá, read j by sense (see Uncertainties).

## Plaintext (Hungarian)

Spelling as on the card, accents normalised only where the key does not separate them. The punctuation is added by me: commas on the card belong to signs, so only `!`, `)`, the brackets around Árpád, the final point after lelked and the date are written. The whole text except the words noted above is enciphered.

Édes Margitkám!

Kívánom a leg boldogabb húsvéti ünepeket neked a leg tisztább szívből, az igaz hogy ez nem valami boldog húsvét, no de majd ad még az isten jobbat is)

Te testté vált tündérrege,
Te bájjá lett virág,
Utánad vágyik csak szívem,
Becsül, szeret, imád.

A szerelem szárnyán küldöm
Te hozzád a lelkem,
Fogadd lánykám szerelemmel
S küld helette lelked.

Soraimat zárva üdvözöl és sokszor csókol hű kedvesed (Árpád)

Mezőkövesd. 1916. IV/22.

Address, in clear: Őnsg. / Szépreményű Sziber Margitka Kisasszonynak / Szomolya / u. p. (Bogács).

Normal forms: ünepeket = ünnepeket, helette = helyette, küld = küldd, Te hozzád = tehozzád.

## English translation

Sweet Margitka of mine! I wish you the happiest Easter holidays from the purest heart; true, this is not much of a happy Easter, but God will yet give a better one too)

You fairy tale become flesh, / you flower become charm, / my heart longs only for you, / it esteems, loves, adores.

On the wings of love I send / my soul to you; / accept it, my girl, with love, / and send your soul in its place.

Closing my lines, your faithful sweetheart greets you and kisses you many times (Árpád)

Mezőkövesd, 22 April 1916.

## Slovak translation

Moja sladká Margitka! Želám ti najšťastnejšie veľkonočné sviatky z najčistejšieho srdca; pravda, toto nie je bohvieaká šťastná Veľká noc, ale Boh ešte dá aj lepšiu)

Ty rozprávka, čo sa stala telom, / ty kvet, čo sa stal pôvabom, / len za tebou túži moje srdce, / váži si ťa, miluje, zbožňuje.

Na krídlach lásky posielam / k tebe svoju dušu; / prijmi ju, dievčatko moje, s láskou / a pošli namiesto nej svoju dušu.

Na záver mojich riadkov ťa pozdravuje a mnohokrát bozkáva tvoj verný milý (Árpád)

Mezőkövesd, 22. apríla 1916.

## Command

Run from the repo root:

    python3 -I ciphers/hcp-1135/work/decode.py

It checks the SHA-256 of all four scans, decodes every sign of `work/transcription.txt`, asserts each decoded line against the stated reading, and prints line by line the raw decode and the reading, the sign counts, and Easter 1916 by the computus. The accents and the `SIGN~letter` readings come from the transcription and the reading list, not from the key.

## Uncertainties

The 301 cipher signs: 294 decode by the table as written, 7 are read by sense. All seven are marked `~` in `work/transcription.txt`:

1. and 2. **`a` before `leg`, twice.** Both are a plain `1` with no dot, checked at 4x (`work/crops/z1.png`, `y1.png`), so the key gives `i`. `a lelkem` on the same card has a clear `1.`. Word sense only: `i` is not a word here.
3. **Becsül.** One blot left of the 1, so literally `.1` = u; `becsul` is not a word, and this may be `:1` with the dots merged (`z7.png`).
4. **üdvözöl, second ö.** The end of the line is cramped against the margin: 0 has no comma of its own, because the comma of the 9 runs under it, and the 5, is squeezed (`z5.png`). The word is fixed by the signs around it and by `hű kedvesed` as subject.
5. **szerelemmel, first sign.** Transcribed `7.`, but no detached dot stands under it, unlike the other `7.` signs of the card. The right end of the crossbar curls down into a blob, probably the dot tied in by the pen (`review/work/crops/sz7.png`). Literally it could be `7` (kerelemmel) or a hooked `7,` (serelemmel). Word sense gives sz.
6. and 7. **bájjá, the two j.** Both signs are a clear `6.`, which is ny in szárnyán and lánykám, while plain `6` is j in majd, jobbat. `Te bájjá lett virág` is the only sense, so this is a homophone or a slip.

Other points:

- The `5` of hozzád is closed at the bottom, like a 6, but it carries the top bar that only 5 has here (`y5.png`). `6 0 9, 9, 1' 3` would be `jozzád`.
- Clear letters inside cipher words: b (bájjá), g (virág), m (lelkem, lánykám), d (lelked) and final l of szerelemmel. The last has a thick stem with a small lobe and could be taken for b or `6,` (`z4.png`); `szerelemmel` is by sense, though that is the only word. A comma-shaped tick stands after that l and after the g of virág (`review/work/crops/endl.png`, `b3.png`). It is either punctuation or the comma of the sign, in which case the l is a badly formed `5,` (same value) and the g a deformed `4,`. Neither changes the reading. Both letters are counted as clear, outside the 301.
- `zárva`: a blot sits on the dot of `3.` and it is clear that a dot is there; plain `3` would give `zárda`, which is a real word (convent) but makes no sense here.
- `)` after `is` has no opening bracket on the card. I do not know where the aside begins; `az igaz` is the natural start.
- The postmark shows a partial date with 22; month and year are not legible. The date in the text is the writer's.
- The faint red marks at the right edge of the picture side (`work/crops/picred.png`) are specks, not read as writing.
- The verse is not traced to a printed source; it may be a quotation or the writer's own.
- The signature `Árpád` matches the enciphered signature of hcp-1174.

## Why I believe it is correct

- A key built on other cards decodes 294 of 301 signs as written into continuous Hungarian. Of the four new signs, `4.`, `6` and `6.` = ny each stand in two words; `.1` stands in one word, húsvét, twice. The seven readings by sense are listed above; the decoder takes them from the `~` marks, so those are choices, not checks.
- The verse scans and rhymes: virág / imád, lelkem / lelked.
- Independent date check: the card is dated IV/22 in 1916 and wishes a happy Easter. Easter Sunday 1916 was 23 April (computed in the script). The picture is an Easter scene as well, and `nem valami boldog húsvét` fits wartime.
- Same sender, salutation, addressee and closing as hcp-1174.

## Response to review 1

Verdict ACCEPT, with six minor findings. No word of the reading changed. I checked findings 2, 3 and 6 on the reviewer's crops at the stated enlargements and agree with all of them. `python3 -I ciphers/hcp-1135/work/decode.py` was re-run after the edits: hashes OK, every line asserted, 301 signs, 294 by the table, 7 by sense.

1. **Overstated correctness argument: fixed.** The closing section now says that `.1` rests on húsvét alone and no longer claims "no free choices". `decode.py` no longer picks ny or j by looking at the expected reading: `6.` is now ny in the key, and the two j of bájjá are marked `6.~j` in `work/transcription.txt`.
2. **szerelemmel, first sign: fixed.** The enlargement shows no detached dot, only the blob at the end of the bar. Now marked `7.~sz` and listed under Uncertainties.
3. **Tick after l and g: fixed.** Both are in the note on clear letters. The tick after the l and the one after the g are real marks; they change no letter.
4. **Punctuation: fixed.** The plaintext section now says it is added and lists what is written on the card.
5. **`5.` label: fixed.** The table gives plain l. The single instance, in helette, happens to stand where normal spelling has ly.
6. **lánykám: fixed, in the reviewer's favour.** The dot stands about a quarter of the way down the stem, as on the other `1'` of this card, and no low dot is there. It is now a table reading `1'` and leaves the list of readings by sense.

Net effect on the count: +1 (sz), +2 (j twice), -1 (lánykám), so 7 by sense instead of 5. The HistoCrypt article remains unchecked, as the review notes.
