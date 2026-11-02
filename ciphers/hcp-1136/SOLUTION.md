# hcp-1136 solution (round 1, after review 1)

Solver: Claude Opus 5.5, 2026-11-02. No earlier work on this number. The portal lists the card as Not solved and attaches no solution or transcription. No published solution was found; the HistoCrypt article linked by the portal was not checked for this card, so I cannot say whether it discusses it. The transcription is my own, made from `work/hires/`.

## Card

Picture postcard (couple with flowers; no writing on the picture side), Mezőkövesd, 24 March 1916, to Sziber Margitka, Szomolya. Unlike its sisters, almost the whole message is enciphered. Only the address, the place and date, and some letters at the start and end of verse lines are in clear.

## Cipher type and key

Register label: MASC. Hungarian, one sign per letter or Hungarian digraph; a sign is a digit plus its mark, so a comma, dot or colon is part of the sign and not punctuation. The key starts from the table on FINAL card hcp-1174 (also hcp-1178, 1179). Signs marked * are new to this card; the rest agree with those cards.

| sign | letter | | sign | letter | | sign | letter |
|---|---|---|---|---|---|---|---|
| `0` | o, ó | | `2,` | cs | | `5,` | l |
| `0,` | ö, ő | | `2.` | é | | `6` * | j |
| `1` | i, í | | `3` | d | | `6,` | n |
| `1.` | a | | `3,` | r | | `6.` * | ny |
| `1:` | e | | `3.` | v | | `7` | k |
| `1'` (dot high) | á | | `4` * | f | | `7,` | s |
| `:1` (dots left) | ü, ű | | `4,` | g | | `7.` | sz |
| `1,` | b | | `4.` * (also written with a short dash) | gy | | `8` | m |
| `9` | p | | `5` | h | | `8,` | t |
| `9,` | z | | | | | | |

The card has 291 cipher signs of 28 kinds, plus 21 letters in clear. 289 decode by the table as written; 2 are read by sense (see Uncertainties). The four signs new here were fixed on this card: `6` by majd (twice), Minjárt, átadják; `4.` by hogy, megyek, egy; `4` by fel only; `6.` by annyi only. Together they are 9 of the 291 signs. No value of the key on the FINAL sister cards hcp-1174, 1178, 1179 had to be changed. (The stalled analysis on hcp-1175 is not part of that key and differs from it.)

## Plaintext (Hungarian; spelling as written, long vowels ó, ő, í, ű restored from the sense since the cipher does not mark them)

Édes Margitkám!
Most különös írni valóm nincs, csak annyi, hogy szombaton fel megyek és akkor majd ketecskén sokat beszélgetünk. Addig is írok egy kis verset.

I
Mikor ezt a lapom
Hirtelen megláttam,
Gondolatba édes
Minjárt neked szántam.

II
Gondoltam — majd örülsz,
Ha átadják neked,
S végtelen boldogság
Fogta el szívemet.

Üdvözölve öleléssel és sok csókkal maradok szerető kedvesed és hű imádód (Árpád)

In clear: Mezőkövesd, 1916. III/24.
Address, in clear: Őnsg. / Szépreményű / Sziber Margitka / kisasszonynak / Szomolya / (Borsod m.) u. p. Bogács.
Postmark: Mezőkövesd, [9]16, month damaged and consistent with MÁR, day 24.

Punctuation in the plaintext is mine, because a comma on the card is part of a sign. Non-standard forms kept as written: `ketecskén` (standard kettecskén), `Minjárt` (mindjárt), `Gondolatba` (gondolatban).

## English translation

Sweet Margitka of mine!
I have nothing special to write now, only that on Saturday I am coming up, and then the two of us will have a long talk. Until then I am writing a little verse.

I. When I suddenly saw this card of mine, in my thoughts, sweet one, I at once meant it for you.

II. I thought: how glad you will be when they hand it to you, and endless happiness seized my heart.

Greeting you with an embrace and many kisses, I remain your loving sweetheart and faithful adorer (Árpád)

Mezőkövesd, 24 March 1916.

## Slovak translation

Moja sladká Margitka!
Teraz ti nemám čo zvláštne napísať, len toľko, že v sobotu prídem hore a potom sa spolu vo dvojici veľa pozhovárame. Dovtedy ti píšem malý verš.

I. Keď som zrazu uvidel túto svoju pohľadnicu, v myšlienkach, moja sladká, som ti ju hneď určil.

II. Pomyslel som si: ako sa potešíš, keď ti ju odovzdajú, a nekonečné šťastie sa zmocnilo môjho srdca.

S pozdravom, objatím a mnohými bozkami zostávam tvoj milujúci milý a verný ctiteľ (Árpád)

Mezőkövesd, 24. marca 1916.

## Command

Run from the repo root:

    python3 -I ciphers/hcp-1136/work/decode.py

It checks the SHA-256 of all four scans, decodes every sign of `work/transcription.txt` with `work/key.json`, asserts each line against the stated reading, reports the counts, and prints the whole text. The address and the date line are in clear and are hard-coded in the script.

## Uncertainties

1. `örülsz`, last sign. Directly after the l stands a heavily hatched blot, evidently a cancelled sign and unreadable, then a clear 7 with a mark at its lower right. The mark is comma-shaped, with two small ticks, so the sign as drawn is nearer `7,` (s, giving `örüls`) than `7.`. I read `7.` = sz by word sense (`majd örülsz`, "you will be glad"). The alternative is a misplaced dot, or a `7` plus a real punctuation comma. The word itself is not in doubt. Crops: `work/crops/z_blot2.png`, `z_blot_r.png`.
2. `maradok`, the o. This sign is an ink-filled elongated blob with a tiny light gap at its foot, the size of the writer's slanted 0 but too filled to confirm. The table cannot be applied directly; `o` is a restoration by sense (`csókkal maradok`, the normal letter close, "I remain"). Crop: `work/crops/z_marad.png`.
3. `megláttam`, the end. After `1.` the card has a heavily inked-over shape which, in form, is a figure 8, so it looks like the cipher sign `8` = m. Directly after it stand cursive m strokes in clear, with a tail. The likely account is that the writer put the cipher m and then wrote over or beside it in clear, but other accounts are possible. `=m` in the transcription is a reading of this place, not a certain single clear letter; `szántam` two lines below has `m` plainly in clear. Either way one m results and the word does not change. The hooked mark after it is taken as punctuation. Crops: `work/crops/z_lam.png`, `review/work/z_tam.png`.
4. Dot position on `1'` / `1.`. In `imádód` and in the second á of `Árpád` the dot stands about two thirds up the stem, not at its top, and I class it as high. The signature's first `1'` has a small double mark high on the right. These are read as á; if read as `1.` the words would be `imadod`, `arpad`, the same words.
5. `1` without a mark in `imádód`: the first sign is slightly blurred; no dot seen.
6. Punctuation and capitals are mine, except the brackets. The signature line on the card reads `... 1 8 1' 3 0 3 ) ( 1' 3, 9 1' 3 )`: a stray `)` stands directly after imádód, with no opening bracket before it. It carries no letter value and the plaintext leaves it out, printing `hű imádód (Árpád)`. `I` and `II` on the card sit above the first line and in the fifth verse line and are taken as stanza numbers. The bar after `Gondoltam` is on the card.
7. `4` = f here occurs only in `fel`, and `6.` = ny only in `annyi`. Both are fixed on this card by the sense of those words. hcp-1143 uses the same values, but it has the same solver and date, so it is not independent support.
8. The word `Őnsg.` in the address is an abbreviated title, as on hcp-1174, read as written.

## Why I believe it is correct

- A key built on other cards (24 of the 28 kinds of sign) decodes this card into continuous Hungarian with no change of any value, and the four signs new here are each fixed by plain common words (`4` and `6.` each rest on a single word).
- The text is coherent throughout: a short note announcing a Saturday visit, an announced verse (`egy kis verset`) which then actually follows, and a closing formula.
- The verse is regular: two stanzas, the second lines and fourth lines rhyme (`megláttam` / `szántam`, `neked` / `szívemet`), `I` / `II` on the card mark the stanzas, and each of the 8 lines has exactly 6 syllables (for example Hir-te-len meg-lát-tam; Gon-dol-tam majd ö-rülsz; Ha át-ad-ják ne-ked). This holds also for the lines with restorations and clear letters, and the reading was not built to fit it.
- The clear letters at line starts and ends (`M`, `H`, `Go`, `Gon`, `Ha`, `S`, `Fogta el`, `-m`, `-t`) join the decoded signs into words, which is an independent check within the card: `=M 1 7 0 3,` Mikor, `=H 1 3, 8, ...` Hirtelen, `=F... 7. 1 3. 1: 8 1: =t` szívemet.
- The signature decodes to `Árpád`, as on hcp-1174, and the opening is the same 13-sign `Édes Margitkám!`. Both are recognised family formulae. The signature was decoded with the key, not assumed.
- `szerető kedvesed` also closes hcp-1174, which supports the reading, though it was not used to build it.

## Response to review 1

Verdict ACCEPT, with minor findings only. All four are taken over; no sign value and no word of the plaintext changed. I rechecked findings 1 and 3 on the reviewer's crops of the hires scan (`review/work/cJL.png`, `review/work/z_tam.png`), and finding 2 against `ciphers/hcp-1175/NOTES.md`.

1. Stray `)` after imádód: agreed. The mark is on the card, directly before `(Árpád)`. Disclosed in uncertainty 6, recorded in a comment in `work/transcription.txt`, and in the report. It has no letter value, so the plaintext is unchanged.
2. Attribution of `4` = f: agreed. hcp-1175 NOTES gives `4,` = f and `4.` = l and calls bare `4` unknown, which conflicts with the FINAL key. Removed the claim from the key table and uncertainty 7. `4` = f now stands on `fel`, and `4` is marked as new to this card, which also makes four new signs, not three, in the card section and in the argument for correctness. `No value ... changed` now names the FINAL cards only.
3. End of `megláttam`: agreed. In `z_tam.png` the shape is an inked-over figure 8, followed by cursive m strokes. Uncertainty 3 now says so and treats `=m` as a reading. The word is unchanged.
4. Metre: added to `Why I believe it is correct`, after recounting all 8 lines: 6 syllables each.

Also noticed while doing this: `289 of 291` in the argument for correctness implied all 289 came from the sister key, but 9 of them are the new signs. Reworded by kinds of sign. The 289/2 count of the table remains right.

The reproduction command was re-run after these edits: hashes OK, 291 cipher signs, 28 distinct, 2 by sense, 21 letters in clear, same text.

What stays open is what the reviewer could not verify: the HistoCrypt article linked by the portal was not read, so `No published solution was found` means only that the portal attaches none; the identity of Árpád and the exact Saturday are unknown; what lies under the two blots and the filled sign is unknown.
