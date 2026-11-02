# hcp-1166 solution (round 1, corrected after review 1)

Solver: Claude Opus 5.5, 2026-11-02. No earlier work exists on this number and the portal attaches no solution or transcription. The HistoCrypt article the portal links was not checked for this card, so I cannot say whether it discusses it. The key starts from my reading of the finished sister cards hcp-1174, 1178 and 1179; the transcription and the new signs are from this card's pixels.

## Card

Picture postcard (couple among roses; no writing on the picture side), Mezőkövesd, dated on the card in clear "1916 IV/11", to Sziber Margitka, Szomolya, u. p. Bogács. The address is open. The message side is almost entirely enciphered in blue ink: a letter, three four-line stanzas, and a closing. The stanzas mix open words and letters with cipher signs. The enciphered signature is Árpád, as on hcp-1174.

## Cipher type and key

Register label: MASC. Each letter is one sign, a digit plus an optional mark. The comma, dot or colon is part of the sign. Hungarian digraphs have one sign. Words are divided by spaces, unlike hcp-1174.

| sign | letter | | sign | letter | | sign | letter |
|---|---|---|---|---|---|---|---|
| `0` | o, ó | | `2,` | cs | | `6` | j (new) |
| `0,` | ö, ő | | `2.` | é | | `6,` | n |
| `1` | i, í | | `3` | d | | `7` | k |
| `1.` | a | | `3,` | r | | `7,` | s |
| `1:` | e | | `3.` | v | | `7.` | sz |
| `1'` (high dot) | á | | `4,` | g | | `8` | m |
| `1,` | b | | `4.` | gy (new) | | `8,` | t |
| `:1` (dots at left) | ü, ű, ú | | `5` | h | | `8.` | ty (new) |
| `9` | p | | `5,` (and `5.`, see below) | l | | `9,` | z |

The 5 always has a short stroke over it, so it is easy to tell from other digits. 28 distinct signs occur, 391 sign tokens in all. Three signs are new on this card and come from whole words: `6` = j from párja, rája, hagyj, Adjatok; `4.` = gy from nagyon, egy, légy, hagyj, egymás; `8.` = ty from kártyát. The single `5.` (in helet) is treated in uncertainty 9.

## Plaintext (Hungarian)

Spelling normalised; the literal letters are printed by the command below. The card's `)` is used as a pause mark and is kept. In the stanzas the line beginnings are open text (Sehol nincs a világon; Ma-, Ad-, Hadd, U-, Minő, U-, Végy, M, S, Üdvözletem, S azt) and a few final letters are open too.

Mezőkövesd, 1916. IV/11.

Édes Margitkám!
Szerencsésen hazaérkeztünk, nagyon szép és meleg idő volt, egy negyed kettőre értünk haza a kertekig, danolásztunk, de aztán álmos lettünk és csak úgy mentünk némán egymás után) erről most többet nem írok) Szervusz.

Sehol nincs a világon
Margitkának párja,
Adjatok egy kis kártyát,
Hadd írom ezt rája.

Udvarlóid seregében
Minő helyet adsz nekem?
Utolsónak ne hagyj engem,
Végy elsőnek, édesem.

M betűvel ír most a tollam,
S rád gondolok, Margitkám,
Üdvözletem küldöm neked,
S azt kívánom: légy vidám!

Üdvözlettel, sok csókkal és öleléssel maradok hű kedvesed) Árpád)

Address: Őnagysága. / Rózsa reményű. / Sziber Margitka / kisasszonynak / Szomolya / u. p. Bogács.

## English translation

Sweet Margitka! We got home safely. The weather was very fine and warm. At a quarter past one we reached home as far as the gardens, we were singing, but then we grew sleepy and just walked silently one behind the other. I will not write more about this now. Servus.

Nowhere in the world / is there Margitka's equal; / give me a little card, / let me write this on it.

Among the host of your suitors / what place do you give me? / Do not leave me for last, / take me first, my sweet.

With the letter M my pen writes now, / and I think of you, Margitka, / I send you my greetings, / and I wish you this: be cheerful!

With greetings, many kisses and an embrace, I remain your faithful sweetheart, Árpád.

Address: To Her Ladyship, the rose-hopeful Miss Margitka Sziber, Szomolya, post office Bogács.

## Slovak translation

Moja sladká Margitka! Šťastne sme došli domov. Bolo veľmi pekné a teplé počasie. Štvrť na dve sme došli domov po záhrady, spievali sme si, ale potom sme ospaleli a len sme išli mlčky jeden za druhým. O tom teraz viac nepíšem. Servus.

Nikde na svete / niet Margitkinej rovne; / dajte mi malú pohľadnicu, / nech na ňu napíšem toto.

V zástupe tvojich ctiteľov / aké miesto mi dáš? / Nenechávaj ma ako posledného, / vezmi ma ako prvého, moja sladká.

Písmenom M píše teraz moje pero, / a myslím na teba, Margitka, / posielam ti pozdrav / a želám ti: buď veselá!

S pozdravom, mnohými bozkami a objatím zostávam tvoj verný milý, Árpád.

Adresa: Jej Milosti, ružovo sľubnej slečne Margitke Sziberovej, Szomolya, pošta Bogács.

## Command

Run from the repo root:

    python3 -I ciphers/hcp-1166/work/decode.py

It checks the SHA-256 of all four scans, decodes every sign of `work/transcription.txt` by the key, stops if any line differs from the stated literal reading, prints the sign count and the line-by-line literal decode, then the normalised text. The normalised text is written into the script; only the literal decode is computed.

## Uncertainties

Sign-level points, none affecting more than one letter:

1. Four signs are taken by word sense against the shape as written (marked `~` in the transcription; 387 of 391 decode as written). Three of them are a t or l whose comma is missing, so dropped commas on 5 and 8 are a habit of this writer:
   - Margi-**t**-kám (stanza 3): the 8 has no visible comma, so as written it is m. Word sense gives t; the same name is spelled with `8,` in the salutation and in stanza 1.
   - kü-**l**-döm: the 5 has no separate comma, so as written it is h. A short tick stands above and to the right, over the following 3, and may be the misplaced comma. Word sense gives l.
   - üdvözlette-**l** (closing): this 5 has no comma, so as written it is h. The stroke to its lower right stands under the next sign and is the comma of `7,` in sok. Word sense gives l.
   - mara-**d**-ok (closing): the sign is abraded and what survives (a closed top loop with a pointed left corner, a stem to the lower right, a ghost of a lower bowl) looks more like 8 than 3. Literal m gives maramok, not a word. "maradok hű kedvesed" is certain, so this d rests on the word and not on the shape.
2. be-**t**-űvel: I assign the long stroke under the 8 as its comma. It runs down towards the top of a 4 in the next line and could be read as part of that 4. Only one of the two dots of `:1` is visible, next to that stroke. Without the comma the word would be bemüvel, which means nothing; "betűvel" fits, so this rests on word sense.
3. Rubbed or abraded signs: in gondolok the `0` is thin on its right side and the `6,` is a smudge with only its top and comma visible (the word is sure from the surrounding g, d, o, l, o, k; the d is a plain 3 with its middle in the rubbed patch). In the bottom two rows the `3.`, `9,` and `5,` of üdvözlettel are faint and crossed by the printed "Import"; the `1.` of maradok is abraded at the card edge. No sign is restored from nothing: each has visible ink.
4. Spelling as written, normalised above: `ketöre` for kettőre, `danolaztünk` for danolásztunk (z for sz, plain a), `helet` for helyet (but see uncertainty 9), `csokkal` for csókkal, `szervüsz` for szervusz. The writer does not mark long vowels on o, i, u, and ő/ű have the same signs as ö/ü.
5. `izt` (Hadd írom ... rája): the sign is a plain 1 with a long flag, no dots, so `1 9, 8,` gives izt. I take it as a dialect or loose form of ezt ("this"). The alternative ízt ("taste") does not fit.
6. "M betűvel" reads literally "with the letter M". I take this as a play on Margitka's initial. Only the capital M is written; it could conceivably abbreviate something else, but the line reads as it stands.
7. "Rózsa reményű" in the address is an open adaptation of the usual Szépreményű; the translation is a loose one. The postmark is partial (…VESD), its date not readable, so the date rests on the card's own "1916 IV/11" and the portal's file name. "egy negyed kettőre" I take as a quarter past one (negyed kettő); the bare wording would allow nothing else natural.
8. The closing marks: `)` after után, írok, kedvesed and Árpád have no opening bracket. The sign after nekem that looks like `2.` is a question mark, read as punctuation by its position after the end of the word and the sense. The printed firm lines in the lower left (Vero Art, No 3745, No 3845, Import, Germany) are the card's own imprint and not part of the message.
9. `5.` in helet: the mark is a clear round dot, and this is the only `5.` on the card. Two explanations remain. On this card `4,`/`4.` are g/gy and `8,`/`8.` are t/ty, so `5.` could be a deliberate ly, giving helyet exactly. Against that, hcp-1179 uses `5.` for plain l (csókollak, legszeb). One token cannot settle it. The script gives `5.` the family value l and prints `helet`; the word is helyet either way.

## Why I believe it is correct

- The whole card reads: every word of all 22 lines decodes to Hungarian, with no gap, by one key.
- The sister key, applied unchanged, gives the salutation and most of the text at once. Only three signs needed new values, and each is fixed by several independent words or by a very constrained one.
- The verses rhyme and scan in the expected way: párja / rája, nekem / engem / édesem, Margitkám / vidám.
- The stanzas are verified by words that split across open and cipher: Ma|rgitkának, Ad|jatok, U|dvarlóid, U|tolsónak.
- Context: same writer's habit and addressee as hcp-1174 (Árpád, Édes Margitkám, cipher for intimacy), place and year in the same range.
- `8.` = ty is worth noting for the family: it would make the hard word on hcp-1179 kar + `8.` + i + m read kártyim, "my cards", in place of the uncertain `kartim`. I changed nothing there.

## Response to review 1

Verdict REVISE. I re-read each doubtful place on the reviewer's enlargements of the hires scan (`review/work/d_adnatok.png`, `e_tel.png`, `f_3.png`, `e_mar.png`, `d_helet.png`). All seven findings are accepted. The message is unchanged except for one word form, and the key is unchanged.

1. **Major, Adjatok: fixed.** There is no comma on the 6; the strokes under it belong to the d's of Hadd in the next row, and the comma of the 8 attaches at its lower right, unlike anything at the 6. The transcription is now `=Ad 6 1. 8, 0 7`. Literal line, plaintext, uncertainty 4 and the note in "Why I believe it is correct" are changed. `6` = j now has 4 tokens. The translations already said "give".
2. **Major, üdvözlette-l: fixed.** Confirmed: the 5 has no comma, and the nearest stroke is the comma under the next sign, `7,` of sok. Marked `5~l` and listed in uncertainty 1, with the dropped comma stated as a habit.
3. **Minor, gon-d-olok: fixed.** The dot-like blob is lower left, under the start of the sign, and not where a `3.` has its dot. Now a plain `3`, removed from uncertainty 1.
4. **Minor, mara-d-ok: fixed.** I agree the survivor has the closed top of an 8. Marked `8~d` and stated in uncertainty 1.
5. **Minor, `5.`: fixed.** Both options are given in uncertainty 9 and the key table no longer simply merges it.
6. **Minor, csókkal: fixed.** The script's reading now prints csókkal, the same as this file.
7. **Minor, Slovak: fixed.** Now "Nenechávaj ma ako posledného".

Result: 4 of 391 signs are taken by word sense. `python3 -I ciphers/hcp-1166/work/decode.py` was re-run after these changes and passes (hashes, 391 signs, 387 as written, all literal lines match).
