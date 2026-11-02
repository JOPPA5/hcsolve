# hcp-1143 solution (round 1)

Solver: Claude Opus 5.5, 2026-11-02. No earlier work exists on this number. The portal lists the card as Not solved and attaches no solution or transcription. The HistoCrypt article linked by the portal was not checked for this card, so I cannot say whether it discusses it. The base key comes from the FINAL cards hcp-1174, 1178 and 1179 (also Claude Opus 5.5). The transcription and the new signs are from this card.

## Card

Picture postcard to Sziber Margitka, Szomolya, u.p. Bogács. Open text: the address (Őnagysága / Sziber Margitka / Kisasszonynak / Szomolya / u.p. (Bogács)) and the dateline "Mezőkövesd, 1916, V/4" at the bottom left. The date agrees with the portal file name (1916-05-04). Everything else is in cipher: the whole message side and a poem on the printed sheet of the picture side (card turned 90 degrees). Unlike hcp-1174, nothing in the message is in clear.

## Cipher type and key

Register label: MASC. Each letter is one digit with an optional mark. No word division. On the address side a large `)` stands for a sentence end, and in the closing the signature stands in `( )`. A `-` at a line end is a line-break hyphen. The flag over a 5 is part of the digit, not a mark.

| | no mark | `,` | `.` | other |
|---|---|---|---|---|
| 0 | o, ó | ö, ő | | |
| 1 | i, í | b | a | `1:` e; `1'` (high dot) á; `:1` (dots left) ü, ű; `.1` (dot left) u, ú |
| 2 | c | cs | é | |
| 3 | d | r | v | |
| 4 | f | g | gy | |
| 5 | h | l | ly | |
| 6 | j | n | ny | |
| 7 | k | s | sz | |
| 8 | m | t | | |
| 9 | p | z | | |

Signs new to the family on this card: `2` c, `4.` gy, `5.` ly, `6` j, `6.` ny, `.1` u. `4` f was only suggested on hcp-1175 and is now attested (`fehér`, `fizetésem`). The mark logic makes the digraphs regular: 2 c/cs, 4 g/gy, 5 l/ly, 6 n/ny, 7 s/sz.

Key recovery: the salutation `2. 3 1: 7, 8 1. 3, 4, 1 . 7 1' .` equals the heading of hcp-1174 (Édes Margitkám). With the transferred table most words decoded at once, and each new sign was fixed by several words (`hogy`, `egy`, `vagyok` for `4.`; `oly` twice for `5.`; `jó`, `teljes` for `6`; `nyílik`, `lányka` for `6.`).

## Plaintext (Hungarian)

As written, with word division, punctuation and capitals added. `[= ]` gives the normal form.

Édes Margitkám!

Bocsás [= Bocsáss] meg, hogy még csak most írok, de hamarabb nem tehettem. Most pedig értesítlek [= értesítelek], hogy kedden este szerencsésen leértem, nagyon jó idő volt, és már szerda óta alkalmazásba [= alkalmazásban] vagyok itt, ebbe a kis parasztboltba [= ebben ... boltban] a hentesek háta mögött. Ezt az egy hónapot kitöltöm itt, aztán megyek tovább. Fizetésem negyven korona és teljes ellátás. Most egyebet nem írok. Ha írsz, egyeb [= egyéb] cím nem kell, csak az én nevem, mint szokás szerint.

Most pedig üdvözöl számtalanszor, ölel és csókol hű imádód (Árpád)

Mezőkövesd, 1916, V/4 (in clear)

Poem on the picture side:

Margit virág után
Margit lett a neved,
s mint e virág fehér,
s szép a lelked neked.

Kertben a kis virág
csak tavaszkor nyílik,
szerelem virága
virágzik a sírig.

Liliom a te virágod,
oly fehér a világod,
oly tiszta vagy te is, lányka,
te életem boldogsága.

Szeretettből [= Szeretetből]

## English translation

Sweet Margitka! Forgive me for writing only now, but I could not do so sooner. Now I inform you that on Tuesday evening I got down safely, the weather was very good, and since Wednesday I have been employed here in this small peasant shop behind the butchers. I will serve out this one month here, and then I move on. My pay is forty crowns and full board. I write nothing else now. If you write, no other address is needed, only my name, as usual.

And now your faithful admirer (Árpád) greets you countless times, embraces and kisses you.

After the daisy [Margit flower] your name became Margit, and white as this flower, and fair is your soul. // In the garden the little flower blooms only in spring; the flower of love blooms until the grave. // The lily is your flower, so white is your world; so pure are you too, girl, you the happiness of my life. // With love.

## Slovak translation

Moja sladká Margitka! Odpusť, že píšem až teraz, ale skôr som nemohol. Teraz ti oznamujem, že v utorok večer som šťastne došiel dolu, bolo veľmi pekné počasie, a už od stredy som zamestnaný tu, v tomto malom sedliackom obchodíku za mäsiarmi. Tento jeden mesiac tu dokončím a potom pôjdem ďalej. Môj plat je štyridsať korún a plné zaopatrenie. Teraz už nič iné nepíšem. Ak napíšeš, iná adresa nie je potrebná, len moje meno, ako obyčajne.

A teraz ťa nespočetnekrát pozdravuje, objíma a bozkáva tvoj verný ctiteľ (Árpád).

Podľa margarétky [kvetu Margit] dostala si meno Margita, a biela ako tento kvet, a krásna je tvoja duša. // V záhrade malý kvet kvitne len na jar, kvet lásky kvitne až do hrobu. // Ľalia je tvoj kvet, taký biely je tvoj svet, taká čistá si aj ty, dievča, ty šťastie môjho života. // S láskou.

## Command

Run from the repo root:

    python3 -I ciphers/hcp-1143/work/decode.py

It checks the SHA-256 of all four scans, decodes `work/transcription.txt` by `work/key.json`, asserts that every decoded word equals the stated reading (long vowels folded, since the key does not separate them), and prints the text. It reports 581 signs by the table and 5 by sense or restoration. It prints only the enciphered parts: the address and the dateline are clear text and are not in the transcription. Word division and punctuation in the plaintext above are mine; the script keeps `le értem`, `paraszt boltba`, `tavasz kor` as separate rows.

## Uncertainties

Signs not given by the table (5, marked `{sign|x}` in the transcription):

1. `Margitkám`, two signs: ink blots cover the t and the final m. The comma of the t still shows. These are restorations; the same word is in clear signs on hcp-1174.
2. `ezt` (A10): the sign is a plain `1`, so the table gives `izt`. A pale smear sits on it, but no dots of `1:` show on the right. Read by sense.
3. `ellátás`, last sign: plain `7` with no comma, so the table gives `ellátak`. Read by sense after `teljes`.
4. `liliom`, third letter: a clear `4`-like shape with a rounded left stroke, no comma, so the table gives `lilfom`. It could be a malformed 1. Read by sense.

Read with a note:

- `nem` in `egyeb cím nem kell` (A16): the loop of the first sign is filled with ink. I read `6,` because the upstroke is continuous with the body; a `5,` would give `lem`, no word. The sense rests partly on the context.
- Writer's forms kept as the signs give them: `Bocsás` (one s), `értesítlek`, `egyeb` (no high dot), `Szeretettből` with `8, 8,`.
- `sírig` (stanza 2) is in faded ink: the upper strokes are pale and the feet dark, as the pen ran dry on the printed sheet. I first took two dark spots for marks; they are the stem feet of a plain `1` and of the `4,` (see review response 3). The table now gives the word.
- `ebbe ... boltba`, `alkalmazásba` are the colloquial -ba for -ban, not misreadings.
- A blue blot stands before the first word of the poem, on the left of `Margit`. It may be a slip, a decoration or a covered sign; no sign can be seen in it.
- `5.` is ly here (`oly` twice). The family is split: hcp-1142, 1151, 1153 and 1162 print it as ly, while FINAL hcp-1178 and 1179 file it as an l variant (`csókollak`, `legszeb`) and hcp-1149 as l, perhaps ly. Since this writer also spells `melnek` (hcp-1160, as reported there), `oly` could stand for a spelled `ol`, and the word is the same either way. The table keeps ly for this card.
- `.1` (u) occurs once, in `után`. The dot is single and clearly left of the stem, and no other sign fits the word.
- `leértem`: "got down" is my rendering; where from and to is not stated. `Kedden`, `szerda` give no calendar date. If the card is of Thursday 4 May 1916, Tuesday and Wednesday would be 2 and 3 May, but this is inference.
- The dateline's day is read 4; a stroke before it is taken as the slash.

## Why I believe it is correct

- One fixed table gives 581 of 586 signs as written, and the 586 signs make grammatical Hungarian from first to last, with no gap and no forced word.
- The new signs are not ad hoc: they fill a regular digit-and-mark grid, each by several independent words.
- The poem rhymes: neved/neked, nyílik/sírig, virágod/világod, lányka/boldogsága. The first stanza plays on her name and the daisies printed on the card itself.
- Names and setting fit the family: the recipient and the Mezőkövesd dateline are in clear, and the signature `Árpád` decodes exactly as on hcp-1174. The practical content (a job, pay of forty crowns, full board, only his name needed on a letter) reads as a real letter.
- No published solution was found or used.

## Response to review 1

Verdict REVISE. All seven findings are accepted. After the fixes I re-ran the command: hashes ok, all word assertions pass, 581 signs by the table, 5 by sense, 586 in all.

1. `alkalmazásba`: fixed. On `review/work/alk.png` the sign has one high dot and clean paper right of the foot, so it is `1'` = á, not `1:`. Transcription row, plaintext and the false note on `1:` are changed.
2. `lányka`: fixed. On `review/work/lanyka.png` the second sign has only the high dot. The row is `5, 1' 6. 7 1.`, a normal word that also stands on hcp-1137, 1146, 1150, 1151 and 1153. The `[= leányka]` gloss, the "oddest form" remark and the old rhyme form are removed.
3. `sírig`: fixed, I agree. On `review/work/sirig.png` the two dark spots lie on the line of their stems, and the neighbouring `3.` shows the same pale top and dark foot. They are stem feet, not marks; the comma of the `4,` is separate. The row is now `1 4,` from the table. Counts go from 579 + 7 to 581 + 5, and the word leaves the list of signs not given by the table. It is no longer the weakest word.
4. "Why correct" section: updated with the new counts and the rhyme form. The list of writer's forms loses `alkalmazesba` and `lenyka`.
5. `5.` wording: fixed, with the family split stated. One correction to the finding: hcp-1149 files it as l, perhaps ly, and hcp-1142 itself says it cannot separate the two. The key cell stays ly for this card; the words do not change.
6. Translations: fixed. Slovak now has "iná adresa nie je potrebná". English and Slovak drop the "so fair" comparison in stanza 1, and the line now reads "white as this flower, and fair is your soul" (Slovak likewise).
7. Command: SOLUTION.md now says that the script prints only the enciphered parts, and that address and dateline are clear text not in the transcription.

