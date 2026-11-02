# HCP 1170 (cpc_1915-12-14_HU_Mezokovesd_HU_Szomolya_szomolya-11): a Hungarian Christmas-time postcard to Margitka Sziber, opening in digit cipher

Human solver: Tomáš Pavuk

**Status: deciphered in full (81 of 81 cipher signs) and the whole card reads; one open word is an emendation by word sense; independent review 1 verdict REVISE, findings addressed.** Report dated 2026-11-02.

## Origin and context

The cryptogram is record 1170 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1170), part of Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-11-02 the portal listed it as **Not solved**, tagged Postcard, T. Schrödel Collection, category Substitution, language Unknown, location Europe, sender Unknown, recipient Margitka Sziber, with no transcription or solution attached. The portal links a HistoCrypt article (https://ecp.ep.liu.se/index.php/histocrypt/article/view/166). That article was not consulted, so it is not known whether it discusses this card.

The picture side is a printed studio portrait of a young woman, with no writing on it. Everything is on the address side. The left half holds the message, the right half the address. The message begins in cipher, one sign per Hungarian letter in digits with marks, for six lines, and then passes into plain writing. A later hand has struck through most of the writing with brown strokes.

The address reads: **Tek. / Szépreményű / Sziber Margitka / kisasszonynak / Borsod megye / Szomolya / u. p. (Bogács)**, that is, "To the honoured and promising Miss Margitka Sziber, Borsod county, Szomolya, post office Bogács". The stamp is a Hungarian 5-fillér, cancelled Mezőkövesd 915 DEC 13 N9. The message is dated Mezőkövesd 1915. XII/14.

The card is unsigned. Its hand and setting match the Mezőkövesd cards to Margitka Sziber in this repository (HCP 1174, 1178, 1179), but the identity of the sender rests on that likeness alone.

![Address side with the message: six cipher lines at the top left, then plain text; address and postmark at the right (source/address-large.jpg)](../source/address-large.jpg)

![The cipher passage, from the high-resolution original (work/hires)](cipher-passage.png)

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

## Method

The transcription is manual and the solver's own, read sign by sign from enlargements of the un-converted original scan. The brown strike-outs were suppressed for reading by keeping the red channel, in which the violet-blue writing stays dark and the brown fades.

The key of the family was taken over from the finished cards HCP 1174 and 1179. It is a monoalphabetic cipher in which a digit and the mark after it form one sign, so `3` is d and `3,` is r. That key decoded 21 of the 25 distinct signs on this card at once into Hungarian, with no adjustment. The other four signs each filled a single gap in a word whose remaining letters were already given: mi-nd-NY-á-J-atokat, Ú-J-ság and ho-GY, va-GY-tok. Those four values rest on word sense on this card, and the same word stands in clear near the end of the card (mindnyájatokat).

In review the reviewer enlarged the rows itself, keyed all six independently, and decoded them with its own script. It agreed with the solver on all 81 signs. It also read all fourteen open lines on contrast-stretched strips.

The reproduction command, from the repository root, is `python3 -I ciphers/hcp-1170/work/decode.py`. It verifies the hashes of the scans, decodes work/transcription.txt, asserts the result and prints the card text. The open text is typed in the script, so the command reproduces only the cipher part.

## Key

Monoalphabetic substitution, digit plus mark. Family signs confirmed here:

| Sign | Plain | Sign | Plain | Sign | Plain |
|---|---|---|---|---|---|
| `0` | o | `2.` | é | `6,` | n |
| `0,` | ö, ő | `3` | d | `7` | k |
| `1` | i | `3,` | r | `7,` | s |
| `1.` | a | `3.` | v | `7.` | sz |
| `1:` | e | `4,` | g | `8` | m |
| `1'` (high dot) | á | `5` | h | `8,` | t |
| `:1` (two dots left) | ü | `5,` | l | `9,` | z |

Signs established on this card:

| Sign | Plain | Evidence |
|---|---|---|
| `6.` | ny | mi-nd-NY-á-jatokat, once |
| `6` | j | mindnyá-J-atokat, ú-J-ság |
| `4.` | gy | ho-GY, va-GY-tok |
| `-1` (thick lobe left of the stem) | u, ú | Ú-jság, once |

The label `-1` names the shape on this card. It is most simply the same sign as `.1` = u, ú on sister cards (HCP 1137, 1140, 1143). The cipher does not mark vowel length on i, o, ö, ü, so only standard spelling makes this ú and not u.

## Ciphertext and plaintext

Word breaks are the solver's; the card has only even spacing. Each row is one line of the card.

```text
3 3, 1' 4, 1. | 8 1. 3, 4, 1 8, 7 1' 8                 drága margitkám
:1 3 3. 0, 9, 0, 5, 5, 1: 7 | 2. 7,                    üdvözöllek és  (then open: csókollak)
8, 2. 4, 1: 3 | 2. 7, | 8 1 6, 3 6. 1' 6 1.            téged és mindnyája-
8, 0 7 1. 8, | 8 1 | -1 6 7, 1' 4, | 3. 1. 6,          -tokat mi újság van
0 8, | 2. 7, | 5 0 4. | 3. 1. 4. 8, 0 7 | 3, 0 7.      ot és hogy vagytok rosz
:1 3 0, | 3. 1. 6, | 1: | 0 8,                         üdő van e ot  (then open: írd meg)
```

Hungarian, with `[ ]` around what is enciphered on the card; punctuation in the cipher passage is the solver's:

> [Drága Margitkám]! [Üdvözöllek és] csókollak [téged és mindnyájatokat. Mi újság van ot és hogy vagytok, rosz üdő van-e ot], írd meg, hogy mikor jön kedves anyukád Kövesdre. Karácsonyig talán még le jön [card: jöm], mert ha megírod akkor bemegyek a fényképészhez és megmondom hogy mikor legyen kész biztosan a kép. Semi különös ujság nincs. Számtalanszor csókollak mindnyájatokat maradtam

> Mezőkövesd 1915. XII/14.

The spellings are the writer's: ot = ott, rosz = rossz, Semi = semmi, üdő = idő (a dialect form).

English: Dear Margitka! I greet and kiss you and all of you. What news is there, and how are you all, is the weather bad there? Write and tell me when your dear mother is coming to Kövesd. She may still come down before Christmas, because if you write it to me, I will go in to the photographer and tell him when the picture should be ready for certain. There is no special news. I kiss you all countless times, I remain. Mezőkövesd, 14 December 1915.

Slovak: Drahá Margitka! Pozdravujem a bozkávam teba aj vás všetkých. Čo je tam nové a ako sa máte, je tam zlé počasie? Napíš mi, kedy príde tvoja milá mamička do Kövesdu. Možno ešte do Vianoc príde dolu, lebo ak mi to napíšeš, pôjdem k fotografovi a poviem mu, kedy má byť obrázok určite hotový. Nič zvláštne nové nie je. Nespočetnekrát vás všetkých bozkávam, zostávam. Mezőkövesd, 14. decembra 1915.

## What remains uncertain

1. **jön [card: jöm].** The letters give jöm: after the ö there are three downstrokes and an exit stroke, as in the final m of "mondom", while the "jön" of the line above has two. The reading jön is an emendation resting on word sense alone. The writer is in Kövesd and cannot come down there, and the mother is the subject of the sentence before. The translation depends on this choice; with jöm the writer would be the one coming down.
2. **The four new signs** rest on word sense. `6.` and `-1` occur once each. The 6 of `6.` is heavy and looks retraced, and the mark right of it is a short dash, read as a dot. `4.` was taken as l on the unfinished HCP 1175; here it is gy in both occurrences. The same values appear on sister cards that are not all finished, so that support is limited.
3. **`1'` against `1:`.** á and e differ only by the second dot. All four `1'` were checked and show one high dot.
4. **A brown speck** stands under the 3 of üdő. It is brown, unlike the ink, so it is not read as a dot. `3.` would give the meaningless üvő.
5. **van-e and the question.** The e stands alone and the word division is the solver's. "rosz üdő van-e ot" could be a separate question or part of the previous one; the words do not change.
6. **írd meg.** A round letter and a stem standing slightly apart: this is the writer's detached d, as in anyukád, Kövesdre and Mezőkövesd on this card. A strict "írol" is not a real alternative. "írod meg" would not change the sense.
7. **mindnyá-jatokat, open text near the end.** The first letter of the second line is too heavily overwritten to confirm a j from the pixels. The word is fixed by the fragment before the line break and by the cipher passage.
8. **maradtam.** The word is cramped under a strike-out and nothing follows it, so the closing lacks a name, which is unusual. The word stands alone and the rest reads.
9. **Date.** The card clearly says XII/14 and the postmark clearly says DEC 13. The cause is unknown (a misdated card or an unchanged postmark date). The portal's file name repeats the written date and is not independent evidence.
10. **The accent in the open word ujság** is unclear, so its spelling is not used as evidence for `-1`.
11. **Not read:** a faint offset of a second postmark below the first. The later brown strike-outs and the portal watermark are not part of the message.

## Review and what changed

An independent reviewer (a separate Claude Opus 5.5 agent) ran the reproduction command, decoded the cipher from its own transcription, and read all the open text and the picture side. It gave verdict REVISE, with the decipherment confirmed sign for sign. Changes made as a result:

- **le jön** was first presented as a plain reading. It is now marked as an emendation of the written jöm, resting on word sense alone.
- **Semmi** became **Semi**, as written.
- **`-1`** was first given as ú and as a short dash. It is now a thick lobe with the value u, ú, probably the sisters' `.1`.
- **The postmark** DEC 13 was first called doubtful. It is now stated as clear, in conflict with the written date.
- The doubt about **írd** was narrowed, on the reviewer's evidence of the writer's d elsewhere on the card.

The reading of the card did not change otherwise. The reviewer could not verify the sender's identity, and the HistoCrypt article was not consulted by either party.
