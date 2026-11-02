# hcp-1155 solution (round 1, with response to review 1)

Solver: Claude Opus 5.5, 2026-11-02. No earlier work on this number. The portal attaches no solution or transcription, status Not solved. The HistoCrypt article the portal links was not checked for this card, so I cannot say whether it discusses it. No published solution turned up. Transcription made by me from work/hires/ (work/transcription.txt).

## Cipher type and key

Register label: MASC. Unlike most Mezőkövesd cards, the whole message is enciphered; only "Sokszor üdvözöl és", the place and date, and the address are open. A letter is a digit plus its mark, so a comma or dot is part of the sign. Hungarian digraphs have one sign. Accents are mostly not marked: 0 serves o and ó, 1 serves i and í, and .1 serves u, ú and ű.

Family key (hcp-1174), all confirmed here:

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| 0 | o, ó | 2. | é | 6, | n |
| 0, | ö, ő | 3 | d | 7 | k |
| 1 | i, í | 3, | r | 7, | s |
| 1. | a (rarely á) | 3. | v | 7. | sz |
| 1: | e | 4, | g | 8 | m |
| 1' (high dot) | á | 5 | h | 8, | t |
| :1 (dots left) | ü | 5, | l | 9 | p |
| 2, | cs | | | 9, | z |

Added to the hcp-1174 table from this card, established from word sense (occurrences in brackets). `1,` = b is already in the hcp-1179 table and `4` = f is reported there from hcp-1175, so this card confirms those two independently; the other six need this card alone (hcp-1179 has `5.` only as l):

| sign | letter | fixed by |
|---|---|---|
| 1, | b (10) | jobb, jobban, birtam, boldogságom, üzletbe |
| 2 | c (1) | nyolckor only |
| 4 | f (4) | falutól, fagyva, fél, hófúvássok |
| 4. | gy (10) | hogy, nagyon, vagyok, egy |
| 5. | ly (1) | olyan only |
| 6 | j (7) | jobb, jó, jött, párjára |
| 6. | ny (3) | Nyúllápáig, nyolckor, nyakam |
| .1 (dot left) | u, ú, ű (9) | út, után, fúvás, haragudott, hű |

The table has 31 signs and the card 527 cipher signs. All 527 decode by it, with no exception list. Seven signs are flagged below as resting on word sense or needing a note.

## Plaintext (Hungarian)

The normalised text below adds accents, spaces and punctuation; spelling is otherwise as written, including `jöt` for jött. `work/decode.py` prints the letter-for-letter form too. All is enciphered except where stated.

Édes Margitkám!

Értesítlek, hogy szerencsésen leértem. Az út sokkal jobb volt, mint mikor mentem, csak a falutól a Nyúllápáig rosz volt, de onnat a telepig nagyon jó volt. A kövesdi határba jobban meg volt fagyva a sár, de a teleptől Kövesdig alig bírtam bemenni, térdig érő hó volt és nagy hófúvássok. Jó hogy nem vártam kocsi után, mert nem láttam, hogy jöt volna utánnam, talán nem is jöt Kövesdre Kovács Imre. Fél nyolckor értem az üzletbe. Lúbin agyon haragudott, de én egy szót sem szóltam.

III Ha körül ölleled nyakam
boldogságom határtalan.

IV Olyan vagyok, mint a madár,
ha a párjára rátalál.

Sokszor üdvözöl [open] és [open] csókol hű kedvesed (Árpád).

(Édes Margitkám, arra kérlek, hogy azt a levelet ne kérd vissza tőllem.) Mezőkövesd. 1916. II/22. [place and date open]

Open address: Őnagysága / Rózsa reményű / Sziber Margitka kisasszonynak / Szomolya / (Borsod m.) u. p. Bogács.

Printed verse on the picture side (red, part worn, not cipher, standard card text): Csókolom a kis kezedet / Írtam Neked egy szerelmes levelet / Egy szó nem sok, az is elég / Csak azt mondd meg szeretsz-e még.

## English translation

Sweet Margitka! I let you know that I got down safely. The road was much better than when I went up, only from the village to the Nyúllápa was it bad, but from there to the settlement [telep] it was very good. In the Kövesd fields the mud was frozen harder, but from the settlement to Kövesd I could hardly get in: there was knee-deep snow and big snowdrifts. It is good that I did not wait for the cart, because I did not see it coming after me; perhaps Imre Kovács did not come to Kövesd at all. I reached the shop at half past seven. Lúbin was furious, but I did not say a word.

III When you put your arms round my neck / my happiness has no bounds.
IV I am like the bird / when it finds its mate.

Many greetings and kisses from your faithful sweetheart (Árpád).

(Sweet Margitka, I ask you not to ask for that letter back from me.) Mezőkövesd, 22 February 1916.

Address: Her Ladyship, the rosy-hoped Miss Margitka Sziber, Szomolya, Borsod county, post office Bogács.

## Slovak translation

Sladká Margitka! Oznamujem ti, že som šťastne došiel dolu. Cesta bola oveľa lepšia, než keď som išiel hore, len od dediny po Nyúllápu bola zlá, ale odtiaľ až po osadu [telep] bola veľmi dobrá. V kövesdskom chotári bolo blato lepšie zamrznuté, ale od osady do Kövesdu som sa ledva dostal, bol sneh po kolená a veľké záveje. Dobre, že som nečakal na povoz, lebo som nevidel, že by šiel za mnou, možno ani neprišiel do Kövesdu Imre Kovács. O pol ôsmej som prišiel do obchodu. Lúbin sa strašne hneval, ale ja som nepovedal ani slovo.

III Keď ma objímeš okolo krku, / moje šťastie nemá hraníc.
IV Som ako vták, / keď nájde svoju družku.

Veľa pozdravov a bozkov od tvojho verného milého (Árpád).

(Sladká Margitka, prosím ťa, aby si odo mňa nežiadala ten list späť.) Mezőkövesd, 22. februára 1916.

Adresa: Jej Milosť, Rózsa reményű (ružových nádejí) slečna Margitka Sziberová, Szomolya, župa Borsod, pošta Bogács.

## Command

Run from the repo root:

    python3 -I ciphers/hcp-1155/work/decode.py

It checks the SHA-256 of all four scans, decodes `work/transcription.txt` by the key, asserts each line against the stated reading, reports the sign counts, and prints the text. The normalised paragraph and the open text are fixed strings in the script. Word breaks in the transcription are mine.

## Uncertainties

Signs resting on word sense or needing a note (marked `~` in the transcription, seven in all):

1. `Lúbin` (`5, .1 1, 1 6,`): the third sign is read as `1,` (b); its bar resembles 7, so `Lúsin` is not excluded. It is the only unknown name, taken as a person at the shop, perhaps the employer. No other card in hcp-113x to 117x has it. Whether the vowel is short is unknown, since .1 also stands for u.
2. `láttam` (`5, 1' 8, 8, 1. 8`): the first t is deformed and could be taken for 9 with a tail. `láttam` is the only reading that makes sense.
3. `arra` (foot block): the second r looks at first like a 9 with a comma (z), but on enlargement it is the writer's closed-top 3 with a bottom hook, as in `kövesdre`, not the straight tail of his 9; the comma is separate. So 3, = r is supported by the shape and also by the phrase `arra kérlek hogy`. Of the seven, this is the best supported. The final 1 has a low dot.
4. `kérlek` (foot block): the l is faint, under the mark of the collector's stamp; its top bar and comma fit 5,.
5. `tér-` (end of L10): the sign given as 2. has no separate dot. A wavy ligature runs from the foot of the 2 into the 3, with only a swelling where the dot should be, so strictly the sign is unmarked. `é` is fixed by the word `térdig`.
6. `talán`, first sign: the same low-loop deformation of 8, as in `láttam`.
7. `talán`, third sign: given as 5, but it has a filled closed bowl, unlike the open 5 elsewhere. Only its bar and comma support 5,. A first pass read the word as `Marán`; `talán` is what the sentence requires.

Other points:

- `bemenni`: an ink blot sits between 6, and 6,; I do not count it as a sign.
- Single-occurrence values: `2` = c and `5.` = ly each occur once (nyolckor, olyan). Both words are certain. Sister cards write `5.` where the word gives l (hcp-1178, 1179), so this sign may be a looser variant of l/ly.
- `1.` stands for á in `vartam` (vártam); elsewhere á is 1'. So the split between 1. and 1' is not perfectly strict.
- Spelling as written: `rosz`, `onnat`, `jöt`, `hofúvássok`, `utánnam`, `ölleled`, `tőllem`. These look like the writer's habits (doubling is frequent), not errors of reading. `Értesítlek` has no e before the l, as written.
- `Nyúllápa` is read as a local field name. I have not confirmed it in a gazetteer. `telep` could be a railway or farm settlement; which one is unknown. Letters are clear.
- `III` and `IV` in boxes before the two couplets are copied as seen; no `I` or `II` occurs on this card. Their purpose is unknown; they may number couplets of a song.
- Underlines run under `nem is jöt kövesdre kovács imre`, under `szót sem szóltam`, and under parts of the verse. A curved arrow joins the end of the `Kovács Imre` line to the end of the `üzletbe` line, and a thin line leads from the verse to the foot block. I copy these as marks; the text reads in order and their purpose is unknown.
- `Rózsa reményű` in the address is the open title (compare `Szépreményű` on hcp-1174). The postmark date is partly illegible and is not used.
- The ending sentence about "that letter" has no context on this card.

## Why I believe it is correct

- The hcp-1174 table plus 8 added values decodes all 527 signs, with no exception list, into continuous Hungarian with no gaps. Two of the 8 (`1,` = b, `4` = f) are attested on sister cards; the other six (`2`, `4.`, `5.`, `6`, `6.`, `.1`) rest on this card, and the added values are used consistently across up to 10 occurrences each.
- Two rhyming couplets come out: `nyakam` / `határtalan` and `madár` / `rátalál`.
- The content is coherent: a walk in snow from Szomolya down to Mezőkövesd, with place order village, Nyúllápa, telep, Kövesd, then arrival at work.
- It continues hcp-1174, dated 15 February 1916, where Árpád promises to come up "next Sunday". 20 February 1916 was a Sunday and this card is dated Tuesday 22 February. The signature `Árpád` and `Édes Margitkám` match that card.
- The signature, `(Árpád)` with its parentheses, and `csókol hű kedvesed` are the formula of hcp-1174 (`szerető kedvesed`).

## Response to review 1

Verdict ACCEPT. All four findings were minor and all are fixed. No letter of the reading changed. I rechecked the crops of findings 1 and 3 myself (`review/work/zA.png`, `zD.png`, `zG.png`) and agree with the reviewer.

1. **Count of signs read by sense: fixed.** `tér-` (2.) and the 5, of `talán` now carry `~` and are items 5 and 7 under Uncertainties. The reviewer's statement that the first sign of `talán` has the same deformation as the t of `láttam` adds one more, so I also flagged it (item 6). The count is now seven, in `work/transcription.txt`, here and in the output of `decode.py`.
2. **"New on this card": fixed.** The table heading and "Why I believe it is correct" now say that `1,` and `4` are attested on hcp-1179 and hcp-1175, and six values rest on this card. The script comment and label were changed to match.
3. **Note on `arra`: fixed.** The sign has the closed top and bottom hook of the writer's 3, as `zG.png` shows; the note now says so.
4. **`jöt`: fixed.** The normalised text here and in `decode.py` now keeps `jöt` twice, as written. The translations are unaffected.

I also took the reviewer's remark in item 8 and restored the brackets of `(Borsod m.)` in the address.

After these edits `python3 -I ciphers/hcp-1155/work/decode.py` still exits 0 with hashes OK, 527 signs, 31 distinct, now 7 flagged, and no change to any decoded line.
