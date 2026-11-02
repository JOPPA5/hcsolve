# hcp-1162 solution (round 1, revised after review 1)

Solver: Claude Opus 5.5, 2026-11-02. No earlier work on this number. The portal shows status Not solved and attaches no solution or transcription. The HistoCrypt article the portal links was not checked for this card, so I cannot say whether it discusses it. No published solution of this card was met.

The transcription is my own, read from the hires address-side scan (`work/transcription.txt`). The picture side has no writing.

## Cipher type and key

Register label: MASC. The whole message is in digit cipher, unlike hcp-1174 where only key words are. Each letter is one sign: a digit, or a digit with a mark. The comma, dot or colon belongs to the sign. Words are mostly spaced, but not always (`81:3,8,` and so on run into their neighbours). Only the date line and the address are open.

| plain digit | comma | dot | other |
|---|---|---|---|
| `1` i, í | `1,` b | `1.` a | `1:` e, `1'` (high dot) á, `.1` (one dot left) u, `:1` (two dots left) ü |
| `0` o, ó | `0,` ö, ő | | |
| `2` c | `2,` cs | `2.` é | |
| `3` d | `3,` r | `3.` v | |
| `4` f | `4,` g | `4.` gy | |
| `5` h | `5,` l | `5.` ly | |
| `6` j | `6,` n | `6.` ny | |
| `7` k | `7,` s | `7.` sz | |
| `8` m | `8,` t | | |
| `9` p | `9,` z | | |

The scheme is regular: the plain digits 2 to 9 run through the consonants c, d, f, h, j, k, m, p; the dot marks digraphs (gy, ly, ny, sz) and the vowels a, é.

Key transfer: the table of hcp-1174 / 1178 / 1179 decoded the bulk at once. New on this card, fixed by word sense and each used in several words or a clear one: `4` f (`fájt`, `fuvaros`, `filért`), `4.` gy (`hogy`, `nagyon`, `gyalog`, `negyed`, `egy`), `6` j (`fájt`, `muszáj`, `majd`), `6.` ny (`nyolcra`, `édesanyám`), `5.` ly (`olyan`), `2` c (`nyolcra`), `.1` u (`muszáj`, `tudod`, `fuvaros`, `után`), `3.` v in more words. The words with `1,` (`betartani`, `ebe`, `pokolba`, `többet`, `beszélt`, `hamarab`) confirm the b of hcp-1179. The `1,` is an uncrossed stroke with a comma; the writer always crosses his 7.

One difference from a sister: hcp-1178 transcribes `5.` in `csókollak` and treats it as l. Here `5.` occurs only once, in `olyan`, as ly.

## Plaintext (Hungarian)

Spelling and the `)` marks are as on the card. Commas, capitals and the line layout are mine. `[= ...]` gives the normal form. The cipher folds i/í, o/ó, ö/ő, so those accents are restored by me.

Édes Margitkám!

Nagyon fájt a szívem, hogy olyan kevés időt tölthettem veled, de máskép [= másképp] nem tehettem, már a pontosságot muszáj betartani, míg ebe [= ebbe] a pokolba [= pokolban] leszek, mert tudod, hogy ez valóságos pokol) Tudod-e, édesem, hogy gyalog hamarab [= hamarabb] haza értem volna, mint kocsin, három negyed nyolcra értünk le) A fuvaros két koronát kért tőlem, de csak egy korona hatvan filért [= fillért] adtam neki) Most többet nem írok, ha majd írsz, írd meg, hogy mit beszélt az után édesanyám.

Számtalanszor ölel és csókol szerető kedvesed (Árpád)

Open: Mezőkövesd, 1916 [III]/28.

Address (open): Őnsg. / Szépreményű / Sziber Margitka / kisasszonynak / Szomolya / (Borsodm.) u. p. Bogács.

A long pen ruling runs under most of card line 19, turns down in a hook before `számtalanszor` on line 20 and continues left under `anyám` with a second stroke there. It sets the closing formula apart from the body. It carries no signs.

## English translation

Sweet Margitka! My heart ached badly that I could spend so little time with you, but I could not do otherwise, since punctuality has to be kept as long as I am in this hell, for you know this is a real hell. Do you know, my sweet, that I would have got home sooner on foot than by carriage? We got down by a quarter to eight. The carter asked two crowns of me, but I gave him only one crown sixty fillér. I will not write more now; when you write, tell me what my mother said afterwards [see Uncertainties].

Countless times your loving sweetheart embraces and kisses you (Árpád)

Mezőkövesd, 28 [March] 1916.

## Slovak translation

Moja sladká Margitka! Veľmi ma bolelo srdce, že som s tebou mohol stráviť tak málo času, ale nemohol som inak, veď presnosť treba dodržiavať, kým budem v tomto pekle, lebo vieš, že je to skutočné peklo. Vieš, moja milá, že pešo by som bol doma skôr než povozom? Dolu sme prišli o trištvrte na osem. Povozník odo mňa pýtal dve koruny, ale dal som mu len jednu korunu šesťdesiat halierov. Teraz už viac nepíšem; keď budeš písať, napíš mi, čo potom hovorila moja mama [pozri Uncertainties].

Nespočetnekrát ťa objíma a bozkáva tvoj milujúci milý (Árpád)

Mezőkövesd, 28. [marca] 1916.

## Command

Run from the repo root:

    python3 -I ciphers/hcp-1162/work/decode.py

It checks the SHA-256 of all four scans, decodes `work/transcription.txt` with the key, joins `édes|anyám` and `kedve|sed` across two line ends that have no hyphen on the card, asserts that the result equals the stated plaintext word by word (accents folded as the cipher folds them, the card's word breaks kept), and prints the text and the sign counts.

## Uncertainties

Cipher signs:

1. `tölthettem`: the first sign is a plain `8` with no comma, clearly so on `work/crops/y6.png`. The key gives m (`mölthettem`, not a word). I read t by sense. This is the only sign off the table, so it is the only one in the script's sense list. A few signs on the table also rest partly on word sense: see items 2 and 3, and the comma of `többet`, which also sits close to the bowl.
2. `tölthettem`, `ölel`: the `0,` here has its comma joined to the bowl, so it looks like a 9 (`y4.png`, `y6.png`). The join is visible and hcp-1174 had the same shape; `9` alone would be p and gives no word. So these are counted as `0,` by the table, but the call rests on word sense.
3. `értünk` (line 13): the comma of `3,` is merged in a heavy tail, not separate (`z5.png`). `2. 3 8,` would give `édt`.
4. `filért`: the `5,` has a closed loop and resembles an 8, but carries the tilde stroke that all his 5s have. Single l as written.
5. `és` at the start of line 21 lies under a red printed number (`3613.`, with a further figure right of it). The `2.` and `7,` show through (`z7.png`). The red figures are not part of the message and I do not know what they are. The `7.` of `számtalanszor` and of `szerető` have blotted dots.

Reading:

- `édesanyám` is literally "my mother" and is translated so. The word is clear, but whose mother is meant is odd: he asks Margitka what she said, so it may be Margitka's mother named affectionately. The card does not settle it.
- `ebe a pokolba`, `hamarab`, `filért`, `máskép` are as written. `Tudod-e`: the `1:` stands alone, so I join it as the question particle.
- `három negyed nyolcra`: 7:45; morning or evening is not stated. `értünk le` "we got down" presumably means down from Szomolya; the destination is not named.
- `pokol` ("hell"): what he means is not stated. The context suggests military service or a strict post in Mezőkövesd in 1916, but the card does not say so.
- The `)` after `pokol`, `le` and `neki` have no opening bracket. He uses them as full stops; no opening bracket is visible anywhere before them.
- Date line: the month is overwritten. `III` comes from the portal file name (1916-03-28) and fits the blot; `1916` and `28` are legible.
- Address: `Őnsg.` is an abbreviated title with a mark above it, read as written. The postmark is partly under the stamp and I did not use its date.
- Sender Unknown on the portal. `Árpád` is the signature decoded here and on hcp-1174.

## Why I believe it is correct

- One fixed key decodes the entire card, every line, into continuous Hungarian with only one sign off the table (see the count printed by the script), a few signs on the table called partly by word sense (Uncertainties, items 1 to 3), and no unread word.
- The key came from other cards for most signs. The new signs fill a regular scheme instead of being ad hoc.
- The content is concrete and self-consistent: spending little time together, the carter asking 2 crowns and getting 1 crown 60 fillér (correct Austro-Hungarian currency), `három negyed nyolcra`, a request for news.
- Same people as the sister cards: addressed to Margitka Sziber at Szomolya, from Mezőkövesd, opening `Édes Margitkám`, closing `szerető kedvesed` and `Árpád` as on hcp-1174.

## Response to review 1

Verdict REVISE. All four findings accepted and fixed. One plaintext letter changed; the reading is otherwise unchanged, so this is not a new round. Re-run after the fixes: `python3 -I ciphers/hcp-1162/work/decode.py` passes (388 signs, 31 distinct, 1 off the table, `1.` 32, `1'` 14), and the reviewer's `review/work/decode_review.py` on the fixed transcription gives the same text.

1. **Major, `után`: fixed.** Checked on `review/work/crops/compare.png`: the dot of `1. 9,` (az) sits at the foot of the stroke, and the dot before the `6,` sits level with the upper stroke, as in the `1'` of `koronát`. So the sign is `1'`, my `1.` was a misreading, and the writer wrote normal `után`. Transcription line 19, `PT` in `decode.py`, the plaintext, the key note and the Uncertainties list corrected.
2. **Minor, hyphens: fixed.** Confirmed on `l19end.png`, `oleles.png`, `kedv.png` and `L6.png`: no stroke after `édes` (line 19), only the tilde of `5,` after `ölel` (line 20), and the stroke after `kedve` is the foot of the bracket of `(Borsodm.)`. Hyphens removed from the transcription. `decode.py` now joins the two words explicitly with an assertion and compares word by word, so `ölel és` is checked with its space.
3. **Minor, ruling: fixed.** Disclosed in a note under the plaintext; I confirmed it on `L6.png`.
4. **Minor, sense count: fixed.** Uncertainties item 1 and the closing argument now say the 1 counts signs off the table, and that some signs on the table rest partly on word sense, `többet` included. The script's output wording says the same.
