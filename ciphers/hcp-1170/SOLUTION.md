# hcp-1170 solution (round 1, amended after review 1)

Solver: Claude Opus 5.5, 2026-11-02. No earlier work on this number. The portal lists it as Not solved and attaches no solution or transcription. No published solution was found in the repo material. The HistoCrypt article the portal links was not checked for this card, so I cannot say whether it discusses it. The transcription is my own, from `work/hires/`.

## Card

Picture postcard (studio portrait of a young woman), written Mezőkövesd 14 December 1915 to Sziber Margitka, Szomolya. Unsigned: the text ends with "maradtam" and the place and date. The hand and context match the Mezőkövesd/Szomolya family (hcp-1174, 1178, 1179). All writing is under a later brown strike-out. The strokes were suppressed with the red channel (`work/ink.py`).

## Cipher type and key

Register label: MASC. Hungarian with the first passage enciphered, one sign per Hungarian letter, digit plus mark, as on hcp-1174 and 1179. The mark is part of the sign, so `3` = d and `3,` = r. The cipher breaks once for the open word `csókollak`, and passes into open text at `írd meg`.

Family key, from FINAL hcp-1174 and 1179, all confirmed here:

| sign | letter | | sign | letter | | sign | letter |
|---|---|---|---|---|---|---|---|
| `0` | o | | `2.` | é | | `6,` | n |
| `0,` | ö, ő | | `3` | d | | `7` | k |
| `1` | i | | `3,` | r | | `7,` | s |
| `1.` | a | | `3.` | v | | `7.` | sz |
| `1:` | e | | `4,` | g | | `8` | m |
| `1'` (high dot) | á | | `5` | h | | `8,` | t |
| `:1` (two dots left) | ü | | `5,` | l | | `9,` | z |

New signs, established on this card from word sense:

| sign | letter | evidence |
|---|---|---|
| `6.` | ny | mi-nd-NY-á-j-a-tokat, once; the same word stands open at the end of the card (`mindnyájatokat`) |
| `6` | j | mindnyá-J-atokat, ú-J-ság (two words) |
| `4.` | gy | ho-GY, va-GY-tok (two words) |
| `-1` (thick lobe left of the stem) | u, ú | ú-jság, once; most simply the same sign as `.1` = u, ú on sister cards (hcp-1137, 1140, 1143), and it parallels `:1` = ü, with a mark left of the 1. The cipher does not mark length on i, o, ö, ü, so only standard spelling makes this ú and not u |

Card: 81 cipher signs, 25 distinct. 21 family signs, 4 new signs. The transcription is in `work/transcription.txt`.

## Plaintext (Hungarian; [ ] = enciphered on the card)

[Drága Margitkám]! [Üdvözöllek és] csókollak [téged és mindnyájatokat. Mi újság van ot és hogy vagytok, rosz üdő van-e ot], írd meg, hogy mikor jön kedves anyukád Kövesdre. Karácsonyig talán még le jön [card: jöm], mert ha megírod akkor bemegyek a fényképészhez és megmondom hogy mikor legyen kész biztosan a kép. Semi különös ujság nincs. Számtalanszor csókollak mindnyájatokat maradtam

Mezőkövesd 1915. XII/14.

Address: Tek. / Szépreményű / Sziber Margitka / kisasszonynak / Borsod megye / Szomolya / u. p. (Bogács). Postmark: Mezőkövesd 915 DEC 13 N9.

Spellings are the writer's: `ot` = ott, `rosz` = rossz, `Semi` = semmi, `üdő` = idő (a dialect form). `jön [card: jöm]` is an emendation, see uncertainty 7. Punctuation in the cipher passage is mine, as the card has none there.

## English translation

Dear Margitka! I greet and kiss you and all of you. What news is there, and how are you all, is the weather bad there? Write and tell me when your dear mother is coming to Kövesd. She may still come down before Christmas, because if you write it to me, I will go in to the photographer and tell him when the picture should be ready for certain. There is no special news. I kiss you all countless times, I remain. Mezőkövesd, 14 December 1915.

## Slovak translation

Drahá Margitka! Pozdravujem a bozkávam teba aj vás všetkých. Čo je tam nové a ako sa máte, je tam zlé počasie? Napíš mi, kedy príde tvoja milá mamička do Kövesdu. Možno ešte do Vianoc príde dolu, lebo ak mi to napíšeš, pôjdem k fotografovi a poviem mu, kedy má byť obrázok určite hotový. Nič zvláštne nové nie je. Nespočetnekrát vás všetkých bozkávam, zostávam. Mezőkövesd, 14. decembra 1915.

## Command

Run from the repo root:

    python3 -I ciphers/hcp-1170/work/decode.py

It checks the SHA-256 of all four scans, decodes `work/transcription.txt` with the table, asserts that the result equals the stated reading, and prints the full text. The open text is typed in the script, so the command reproduces only the cipher part. The script needs no third-party module.

## Uncertainties

Cipher:

1. The four new signs rest on word sense, not on an outside key. `6.` and `-1` occur once each. `6.` is the weakest sign physically: the 6 is written heavily and looks retraced, and the mark right of it is a short dash, read as a dot. The open `mindnyájatokat` at the end supports the word. On hcp-1175 `4.` was taken as l, but that card stalled and its reading is unconfirmed; here `4.` is gy in both of its occurrences.
2. `1'` against `1:` was checked sign by sign, since á and e differ only by the second dot. All four `1'`, in `drága`, `Margitkám`, `mindnyájatokat` and `újság`, show one high dot, and the sense agrees.
3. A brown speck stands under the 3 of `üdő`. It is the colour of foxing or the strike-out, not of the ink, so it is not read as a dot. `3.` would give `üvő`, which makes no sense.
4. `van-e` is written with `1:` alone as e. The word division is mine.
5. `rosz üdő van-e ot` could be taken as a separate question or as part of the previous one. The words do not change.

Open text, all under strike-outs:

6. `Írd meg`: the pixels show `ir` plus a round letter plus a tall stem standing slightly apart. This is this writer's detached d: the same bowl and stem stand in `anyukád`, `Kövesdre` and `Mezőkövesd` on this card. `írol` is therefore not a real alternative. `írod meg` would not change the sense.
7. `le jön`: the pixels give `jöm`. After the ö there are three downstrokes and an exit stroke, as in the final m of `mondom`, while the `jön` of the line above has two downstrokes and an exit stroke. `jön` is an emendation resting on word sense alone: the writer is in Kövesd and cannot come down there, and the mother is the subject of the sentence before. The translation depends on this choice; with `jöm` the writer would be the one coming down.
8. `mindnyá-jatokat`: the first letter of the second line is a heavy stroke without the usual j descender. The word is fixed by the fragment `mindnyá-` and by the cipher passage.
9. `maradtam`: the letters d and t are cramped and a strike-out passes through. There is no signature after it, so the sentence ends without a name, unusually. The word is alone and the rest reads.
10. Date: the card clearly says XII/14 and the postmark clearly says DEC 13. The 3 stands on the stamp and is legible. The cause is unknown (a misdated card or an unchanged postmark date). The portal's file name repeats the written date and is not independent evidence.
11. `Tek.` and the address are clear. `Szépreményű` matches the address on hcp-1174. A faint offset of a second postmark shows below the first and is not read.

## Why I believe it is correct

- The family key, taken over unchanged, decodes 21 of the 25 distinct signs into Hungarian, without any adjustment.
- The four new signs each fill one gap in a word whose other letters are given by that key, and each fills the expected Hungarian letter (ny, j, gy, u had no sign yet in the FINAL family tables).
- The passage flows grammatically into open text, with `csókollak` in clear between `Üdvözöllek és` and `téged`. `csókollak téged` is also the enciphered line of hcp-1178, and `üdvözöllek` occurs on hcp-1174.
- The card repeats itself in clear: cipher `csókollak ... mindnyájatokat` at the start, open `csókollak mindnyájatokat` at the end.
- The dialect `üdő` and the spelling `ot`, `rosz` were not expected and were not forced; they follow from the signs. The single consonants match the writer's habit (`legszeb`, `diferál` on the sisters).
- A letter in December about a picture at the photographer and Christmas fits the Mezőkövesd correspondence of 1915.

## Response to review 1

Verdict REVISE, four findings. I checked each on the reviewer's crops and all four stand. The reading of the card is unchanged, apart from one word labelled as an emendation and one spelling.

1. **major, `le jön` is an emendation.** Agreed. `review/work/zjon2.png` shows three downstrokes after the ö, `zjon1.png` shows two. Fixed: the plaintext now has `jön [card: jöm]`, uncertainty 7 says the pixels give `jöm` and that `jön` rests on word sense alone, and `work/decode.py` prints the same. The translations keep `jön` and the dependence is stated.
2. **minor, `Semmi` is written `Semi`.** Agreed. `review/work/zsem.png` shows one m. Fixed in the plaintext, in the spelling list and in the open text of `work/decode.py`.
3. **minor, `-1` too narrow and described as a separate sign.** Agreed. `review/work/z4u.png` shows a thick lobe left of the stem, not a low dash. Fixed: the value is now u, ú, and the table says it is probably the same sign as `.1`. The token `-1` stays in `work/transcription.txt` as a label for this card's shape, with its comment corrected. I print `újság` by standard spelling only, and I do not use the open `ujság` as evidence, since its accent is unclear.
4. **minor, postmark clearer than stated.** Agreed. `review/work/zpm.png` shows 13 plainly. Uncertainty 10 now states the conflict as it is, and that the portal's file name is not independent evidence.

The reviewer's narrowing of `írd` is taken over in uncertainty 6.

Re-run after the fixes: `python3 -I ciphers/hcp-1170/work/decode.py` passes all four hash checks and prints 81 signs, 25 distinct. The cipher decode is unchanged.
