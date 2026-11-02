# hcp-1163 solution (round 1, revised after review 1)

Solver: Claude Opus 5.5, 2026-11-02. No earlier work on this number. The portal shows status Not solved and attaches no solution or transcription. No published solution of this card turned up. The HistoCrypt article the portal links was not checked for this card, so I cannot say whether it discusses this card. The transcription is my own, from `work/hires/`.

## Card

Picture postcard of a couple, sent to Sziber Margitka at Szomolya. The whole message side is in figures, so unlike hcp-1174 there is no open running text. Open parts are only the date line `Mezőkövesd, 1916. II/26.` (it fits the portal file name) and the address.

## Cipher type and key

Register label: MASC. Each letter is one digit, or a digit with a mark. Comma, dot and colon belong to the sign, and they are not punctuation. There are no regular word gaps; I added the word boundaries. The key comes from FINAL sister cards hcp-1174, 1178 and 1179. Five signs marked below are new and one is confirmed here.

| sign | letter | | sign | letter | | sign | letter |
|---|---|---|---|---|---|---|---|
| `0` | o, ó | | `2.` | é | | `6,` | n |
| `0,` | ö, ő | | `3` | d | | `6.` | ny (new) |
| `1` | i, í | | `3,` | r | | `7` | k |
| `1.` | a | | `3.` | v | | `7,` | s |
| `1:` | e | | `4` | f (confirmed, was tentative on 1175) | | `7.` | sz |
| `1'` (dot at upper right, no low dot) | á | | `4,` | g | | `8` | m |
| `:1` (two dots at left) | ü, ű | | `4.` | gy (new) | | `8,` | t |
| `1,` | b | | `5` | h | | `9` | p |
| `2` | c (new) | | `5,` | l | | `9,` | z |
| `2,` | cs | | `6` | j (new) | | `.1` (one dot at left) | u, ú (new) |

The new values came from words: `5 0 4.` = hogy (it occurs 3 more times in `hogyha`, 4 in all), `2 2. 3 .1 5, 1' 8,` = cédulát, `4 1: 5, 1: 5, 6` = felelj, `1 3, 6 1' 5,` = írjál, `1: 6. 2. 8` = enyém. `.1` = u from `8, .1 3 0 8` = tudom and `.1 4.` = úgy, as well as cédulát. There is no u/ü merger, as my first version wrongly said: the left-dot sign has two forms that split by sound, two dots for ü, ű (csütör-, küldtem, üdvözölve, hűséges) and one dot for u, ú (cédu-, tudom, úgy), 7 of 7. In csütör- and küldtem the upper dot touches the flag of the 1, so it looks forked. The sisters attest `:1` only for ü. Whether `.1` is also on the sister cards I did not check; that is a lead only.

Marks written high on the 5 are a part of how this writer makes the 5. They do not change the sign; only the comma below does.

## Plaintext (Hungarian)

All of it is enciphered except the date and the address. Punctuation is mine except the `!` after the salutation and after `Istenem` and the stop after `enyém`, as on the card. The `:` after `gondolok` is mine: the two small marks there look like the top of a dashed frame line (uncertainty 12).

    Édes Margitkám!

    Értesítlek, hogy csütörtökön küldtem egy cédulát, nem tudom megkaptad-e.
    Ha igen, akkor írd meg és felelj valamit a tartalmáról, aztán írjál sokat.

    V   Boldog csak úgy lehetek én,
        hogyha te leszel az enyém.
    VI  Nem szeretek mást, csak téged,
        csókkal teszek rá pecsétet.

    Hogyha rád gondolok: boldogságom álma!
    Istenem! ha egykor ez valóra válna.
    Hogyha magaménak mondhatnálak téged,
    megáldanám érte a nagy mindenséget.

    Számtalanszor csókolva és üdvözölve maradok hűséges kedvesed és imádód (Árpád)

    Mezőkövesd, 1916. II/26.

Address (open): Őnagysága / Szépreményű / Sziber Margitka / kisasszonynak / (Borsodmegye) / Szomolya / u. p. (Bogács.)

## English translation

Sweet Margitka! I let you know that on Thursday I sent a slip of paper; I do not know whether you received it. If so, then write and tell me, and answer something about its contents, and then write a lot.

V. I can be happy only if you will be mine. VI. I love no one else but you; with a kiss I set a seal on it.

When I think of you: the dream of my happiness! My God! if only this came true one day. If I could call you my own, I would bless the whole universe for it.

Kissing and greeting you countless times, I remain your faithful sweetheart and adorer (Árpád).

Mezőkövesd, 26 Feb 1916. Address: Her Ladyship, the promising Miss Margitka Sziber, (Borsod county), Szomolya, post office Bogács.

## Slovak translation

Moja sladká Margitka! Oznamujem ti, že vo štvrtok som poslal lístok; neviem, či si ho dostala. Ak áno, tak mi to napíš a odpovedz niečo k jeho obsahu, a potom píš veľa.

V. Šťastný môžem byť len tak, ak budeš moja. VI. Nemilujem nikoho iného, len teba; bozkom na to dávam pečať.

Keď na teba myslím: sen môjho šťastia! Bože môj! keby sa to raz stalo skutočnosťou. Keby som ťa mohol nazývať svojou, požehnal by som zaň celý vesmír.

Nespočetnekrát ťa bozkávam a pozdravujem a zostávam tvoj verný milý a ctiteľ (Árpád).

Mezőkövesd, 26. 2. 1916. Adresa: Jej Milosť, nádejná slečna Margitka Sziberová, (župa Boršod), Szomolya, pošta Bogács.

## Command

Run from the repo root:

    python3 -I ciphers/hcp-1163/work/decode.py

It checks the SHA-256 of all four scans, decodes `work/transcription.txt` by the fixed key with no per-word exceptions, prints the raw decode row by row, asserts that the stated reading equals the decode letter for letter (only vowel length folded: ó/o, ő/ö, í/i, ú/u, ű/ü; á/a and é/e are not folded, and u/ü is no longer folded), and prints the text. The accented, spaced reading and the open lines are hard-coded in the script. Expected count: 391 signs, 30 distinct (the `5~l` sign counts as `5,`).

## Uncertainties

No word is unread. The remaining points are at sign level:

1. `üdvözölve`, the `5`: the comma is not visible, so the key alone gives `üdvözöhve`. A stroke rises towards the 5 from the row below (`kedvesed`, row E3, not `hűséges` as I first said; `work/crops/z1.png`), but it is the long tip of that 7, a shape it has elsewhere, and nothing shows a comma. The sign is marked `5~l` in the transcription and is the only sign not taken from the table as seen. It is fixed by sense alone.
2. `hűséges`, final `7,`: the tail of the 7 hooks left and the comma appears merged into it; `work/crops/e975r.png`. Sense needs s.
3. `lehetek`, first `1:` is under a blot. The stem and both dots show through; `work/crops/b0r.png`. The following 5 is retraced. No restoration is needed for the letters.
4. `1'` dots are sometimes at mid-height rather than high (`tartalmáról`, `mondhatnálak`, `megáldanám`, first sign of `Árpád`). I take them as `1'`. A low dot would give a, and these spots rest on word sense as well as on position; the dots stand clearly above the baseline, where the `1.` dot sits.
5. Marks on the 0 in `csütörtökön`: both have a comma, and also a small high dash on the first; I treat the dash as a flourish. The second comma is thin but visible.
6. Sense: `cédula` may mean a note or a slip, or a ticket; the card does not say which. `Őnagysága` and `Szépreményű` are address formulas (a title and "of fair promise"). The `V` and `VI` are Roman numerals on the card, with ruled lines between the sections. Why the numbering starts at V is unknown; it may continue the numbering of verses on the slip or an earlier card, but that is a guess. The word `Hogyha` is written as two groups with no reliable gap, and I join it as one word.
7. Row order: `8, 2. 4, 1: 3` (téged) stands raised above the end of the row `csókkal ... pecsétet`, at the right edge. I read it as the overflow of the row above it (`Nem szeretek mást csak`), because that gives the sense and the rhyme téged / pecsétet. The other order does not give a sentence.
8. Punctuation in cipher: small marks at the row ends (`-` hyphens, `!`, the free comma after `én,` and the stop after `enyém`) are read as punctuation, not as signs. The hyphens fall at breaks inside words (csütör-tökön, cédu-lát, megkaptad-e, tar-talmáról), which supports this.
9. Spelling as written: `valora`, `csokkal`, `Irjál` show no long marks, since the key has one sign for o/ó and i/í.
10. Printed matter: a faint reddish printed publisher's line (it looks like `Lepo...nd`) and a triangle mark with `143` sit under the last rows. I could not read the line. It is a printed mark under the ink, not part of the message.
11. Postmark: damaged, Mezőkövesd rim letters visible, date not certain. I rely on the written date.
12. The marks after `gondolok` stand in line with further dashes running down to the solid right edge of the box around the quatrain (`review/work/crops/p31.png`). I take them as the top of a dashed frame line, not as a colon; the point is doubtful and changes no letter.
13. `mindenséget`: a very small dot follows the 3 at the foot. Counted as a sign mark it would give `3.` = v, `minvenséget`. It is far smaller than the writer's real dots, so I read `3`, but this rests partly on sense.
14. `imádód`: a long thin stroke runs from under the last 3 up across the opening bracket. It starts right of the 3 and lacks the place and hook of a sign comma, so I do not read `3,` (r), which would give no word. It may be a free comma or a slip.
15. Dashed underlines (under the `pecsétet` row, parts of `hűséges`, `(Árpád)`) and rule lines round the sections look like ornament and are not counted as signs.

## Why I believe it is correct

- A key built on other cards, with five new signs and `4` confirmed from this card's words, decodes all 391 signs into continuous Hungarian with one sign (point 1) not as seen. No word is forced, and 30 distinct signs across 391 positions leave very little freedom.
- Internal control: after the new values were fixed from the first rows, `4.` recurs correctly in úgy, egykor, nagy, and `6` in írjál, and `.1` gives u three times. `2`, `4` and `6.` occur once each, so they have no independent check; each is fixed by a word that leaves no alternative (cédulát, felelj, enyém).
- The verse scans and rhymes: én / enyém, téged / pecsétet, álma / válna, téged / mindenséget, in a form that fits a suitor's poem.
- The signature `Árpád` comes out of the digits with the same signs as on hcp-1174, and the recipient is the same.
- The writer's words `csókolva`, `kedvesed`, `számtalanszor` and the sign strings for them agree with hcp-1174.
- Context: the writer asks about an earlier message and is writing love verses to a young woman on an open postcard, which is why he enciphers everything.

## Response to review 1

Verdict REVISE. All findings are addressed. No word of the reading changed, and the raw decode now gives `cédu`, `tudom`, `ugy` directly. `python3 -I ciphers/hcp-1163/work/decode.py` re-run after the changes: hashes OK, 391 signs, 30 distinct, reading matches the decode.

1. major, u/ü merger. Accepted and fixed. I checked the seven signs on the reviewer's sheet (copied to `work/crops/u_split_from_review.png`). `üdvözölve` and `hűséges` have two free dots; `csütör` and `küldtem` have a free lower dot and an upper dot merged with the flag, which gives the forked look; `cédu`, `tudom`, `úgy` have the flag and one lower dot. New sign `.1` = u, ú in the key and decoder, `:1` restricted to ü, ű, `work/transcription.txt` corrected at L2, L3, V1, the folding of u to ü removed from `norm`, the merger paragraph rewritten, and five new signs stated.
2. minor, `Őnagysága`. Accepted: `review/work/crops/o.png` shows two long parallel strokes. Fixed in the script and here.
3. minor, uncertainty 1. Accepted: on `review/work/crops/l2.png` the stroke is the tip of the 7 below, which is in `kedvesed`. Uncertainty 1 rewritten: comma not visible, fixed by sense. It stays the only such sign.
4. minor, `:` after `gondolok`. Accepted: on `review/work/crops/p31.png` the marks line up with the dashes running to the box edge. No longer listed as on the card; the colon in the plaintext is mine. See uncertainty 12.
5. minor, undisclosed marks. Accepted: on `review/work/crops/minden.png` and `review/work/crops/imadod.png` both are as the reviewer describes. Added as uncertainties 13, 14, 15. The readings `3` stay.
6. minor, factual slips. Fixed: `5 0 4.` occurs 3 more times, 4 in all. The script no longer counts `5~l` as a type, so 30 distinct is now the true count with `.1` included. The control paragraph no longer claims a check for `2`.

The HistoCrypt article is still unchecked, so I cannot say whether it discusses this card.
