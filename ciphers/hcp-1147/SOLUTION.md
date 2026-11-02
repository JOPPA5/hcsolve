# hcp-1147 solution

Solver: Claude Opus 5.5, 2026-11-02. No earlier work on this number. The portal lists the card as Not solved and attaches no solution or transcription. The HistoCrypt article the portal links (https://ecp.ep.liu.se/index.php/histocrypt/article/view/166) was not checked, so I cannot say whether it discusses this card. The transcription is my own, read from `work/hires/` enlarged 3 to 8 times. The key starts from the sister cards hcp-1174, 1178 and 1179 (FINAL); this card adds new signs (below).

## Card

Picture postcard (couple with lilacs, no writing on the picture side), Mezőkövesd to Szomolya, by Árpád to Margitka Sziber. Postmarks Mezőkövesd, APR 20 legible, year not. Two stamps. Three days before Easter Sunday 1916 (23 April), which fits the text.

Open (unenciphered) text only: the address, "Őnagysága. / Rózsa Reményü / Sziber Margitka / Kisasszonynak / Szomolya / u.p. (Bogács)", and the date "(Mezőkövesd, 1916. IV/20.)". The rest of the message side is cipher: a letter, then ruled boxes with verses and the closing.

## Cipher type and key

Register label: MASC. Each letter is one sign: a digit alone, or a digit with a mark. The mark is part of the sign. Latin `a` and `az` are written openly among the signs in places. Vowel length of o, i, u, ö, ü is not marked. A slanted stroke, dot or colon that follows the digit is the mark; a dot or colon left of 1 also counts (`·1`, `:1`).

| sign | letter | | sign | letter | | sign | letter |
|---|---|---|---|---|---|---|---|
| `0` | o, ó | | `2,` | cs | | `6` | j |
| `0,` | ö, ő | | `2.` | é | | `6,` | n |
| `1` | i, í | | `3` | d | | `6.` | ny |
| `1.` | a | | `3,` | r | | `7` | k |
| `1:` | e | | `3.` | v | | `7,` | s |
| `1'` (high dot) | á | | `4` | f | | `7.` | sz |
| `1,` | b | | `4,` | g | | `8` | m |
| `·1` (dot left) | u, ú | | `4.` | gy | | `8,` | t |
| `:1` (colon left) | ü, ű | | `5` | h | | `8.` | ty |
| `9` | p | | `5,` | l | | `9,` | z |

New against the sister-card tables: `6` = j (majd, újság), `6.` = ny (nyugaton), `8.` = ty (kártya), `4.` = gy (hogy, angyalom, nagyon, egy, vagy), `·1` = u (húsvét, falu, tudok, újság, nyugaton). `4` = f was marked tentative on hcp-1175 and is confirmed here (falu, fér). Key recovery: the salutation `2. 3 1: 7, 8 1. 3, 4, 1 8, 7 1' 8 !` is letter for letter the Édes Margitkám! of hcp-1174, and the table carried over gave the first words at once; the new signs each came from a word they alone complete. `6`, `4.` and `·1` recur; `6.` (nyugaton) and `8.` (kártya) occur once each on this card, so each rests on that one word, which no other value completes.

## Plaintext (Hungarian; all cipher except the date; capitals and punctuation mine)

Édes Margitkám!

Ha Pista húsvétra kap szabadságot, légy szíves írd meg neki, hogy hacsak lehet, nálatok töltse el a húsvétot, mert nagyon szeretnék vele találkozni, hátha többet nem beszélhetek vele. Most egyéb újságot nem írok, majd szóval többet.

Hozzád repül a távolból / kis angyalom, a madárka, / oda száll az ablakomra, / csőrében egy képes kártya.

Északon és délen / képed itt van vélem, / keleten, nyugaton / te vagy gondolatom.

Kicsi házban, falu végén, / hogy ha laknám veled én, / azt mondanám: ottan lakom / a világ közepén.

Most többet nem tudok írni, mert nem fér. Sok csókkal és öleléssel maradok hozzád mindig hű imádód (Árpád)

## English translation

Sweet Margitka! If Pista gets leave for Easter, please write to him that, if it is at all possible, he should spend Easter at your place, because I would very much like to meet him; who knows, I may never speak with him again. I am not writing any other news now; more by word of mouth later.

To you from afar, my little angel, flies / the bird; / there it alights on my window, / in its beak a picture card.

("kis angyalom" is taken as a vocative to Margitka. Apposition to the bird, "my little angel, the bird", is grammatically possible. "My window" is what the card says, though "hozzád" and "oda" would lead one to expect "your window"; see the uncertainties.)

North and south / your image is here with me; / east and west / you are my thought.

In a little house at the end of the village, / if I lived with you, / I would say: there I live, / at the centre of the world.

I cannot write more now, because it will not fit. With many kisses and embraces I remain ever your faithful adorer (Árpád)

## Slovak translation

Moja sladká Margitka! Ak Pišta dostane na Veľkú noc dovolenku, buď taká dobrá a napíš mu, aby, ak je to len možné, strávil Veľkú noc u vás, lebo by som sa s ním veľmi rád stretol; ktovie, či sa s ním ešte niekedy porozprávam. Teraz inú novinu nepíšem, viac potom ústne.

K tebe z diaľky, môj anjelik, letí / vtáčik; / tam sadá na moje okno, / v zobáku obrázková pohľadnica.

Na severe i na juhu / tvoj obraz je tu so mnou; / na východe, na západe / ty si mojou myšlienkou.

V malom domčeku na konci dediny, / keby som býval s tebou, / povedal by som: tam bývam, / v strede sveta.

Viac teraz nemôžem písať, lebo sa to nezmestí. S mnohými bozkami a objatiami zostávam navždy tvoj verný ctiteľ (Árpád)

## Command

Run from the repo root:

    python3 -I ciphers/hcp-1147/work/decode.py

It checks the SHA-256 of all four files, decodes `work/transcription.txt` sign by sign with the table, stops on any mismatch with the stated reading, reports the sign counts (475 signs: 469 by the table, 6 by sense), and prints the full text. The address and date are open text and are hard-coded. Word breaks and line labels in the transcription are mine; the card has few gaps.

## Uncertainties

All six points where a sign is not taken at face value (marked `~` in the transcription):

1. **egyéb (L7).** The 1 after `4.` stands on the printed divider; a round dot lies at its foot on the line and a dash high to the right, read together as a stretched colon, `1:` = e. The word then is literally egyeb for egyéb (é has its own sign `2.`, so this is a slip or short spelling). If the two marks are not one colon, the sign is `1.` and the word is egyab, which is still only sensible as egyéb. Word sense decides.
2. **most (L7).** The final 8 has no visible comma, so literally it is m, not t. The same word in R1 has `8,`. Read as t by sense.
3. **nagyon (L4).** The first 6 has no comma, so literally it is j; the single stroke in that spot sits under the preceding `8,`. The same word's last 6 has one. Read as n by sense.
4. **többet (L8).** The ö is a 9 shape, read as `0,` with the comma joined to the 0, the same graph hcp-1174 has in üdvözöllek. In L6 and R1 the same word is written with plain `0,`.
5. **mondanám (N3).** The sign before `1.` is abraded and partly under the printed word "Import". What remains (a stem and a low curve) does not settle the digit; `3` = d is taken by word sense, and it is the one letter that makes the word. The `1.` after it is faint but visible.
6. **légy (L2).** After `5, 2. 4` a large ink blot sits where the dot of `4.` falls and hides the mark. gy is taken from the word and from every other `4.` on the card.

Other points:

- Reading of the ink over print or postmark needed care in N1 to N3 (printed "Voro matt / Voro gélatiné / Import" table) and L2 to L6 (postmark). Signs there were checked on enlarged colour and red-channel crops. In N2 the high dot that makes `1'` (laknám, not laknem) is clear on the enlargement; `laknám` is also required by the verse.
- **ablakomra (M3).** The 8 is the most heavily blotted sign on the card: the join of the loops is a solid mass, with a tick hanging into the lower loop and the comma of the row above running into the top. Both loops are closed, so the sign is 8 = m, not 3 = d, and the reading stands. But the sense sits badly: the bird flies to you and alights there, so "ablakodra" (your window) would be the natural word. The blot may be a correction or the writer's slip; the scan cannot show ink order, and the verse was not traced to a printed source.
- The 7 of közepén (N4) is abraded, leaving the foot, the bar and a piece of the top. It is still a 7.
- Latin `a` closes madárka; `a` in M1 and M2 and `az` in M3 are also plain Latin letters in the cipher lines. They are not counted as signs.
- The stroke that I take as the comma of `7,` in `újság` (L8) runs down into the 8 of the line below and could be a flourish of it. Bare 7 would give újkágot, so it is the comma.
- "Pista" is not identified. "Szabadságot kap" is military leave, so he is presumably a soldier, and "hátha többet nem beszélhetek vele" reads as wartime worry; that is my reading, not stated on the card.
- Order of the boxes (letter, bird verse, compass verse, village verse, closing) is by sense and layout. The closing runs in the right box, top to bottom. Nothing else depends on it.
- The verses may be quoted or popular; I did not trace them.
- The card carries no second cipher and no unread clause.

## Why I believe it is correct

- The same table reads the whole card, 469 of 475 signs at face value, with no forced word.
- It yields three rhymed quatrains (távolból/madárka block with ablakomra/kártya, délen/vélem with nyugaton/gondolatom, végén/én with közepén) and a letter that fits the date: card of 20 April 1916 asking about Easter, 23 April 1916.
- It reproduces the correspondence: Édes Margitkám as on hcp-1174 and hcp-1178, the same `2, 0 7 ...` (csók-) stem, and the signature Árpád in the same signs as hcp-1174, here `1' 3, 9 1' 3`.
- New signs recur consistently: `4.` in eight words, `·1` in six. `6.` and `8.` occur once each.

An observation for the family, not used here: `8.` = ty on this card (kártya) may bear on the `8.` that hcp-1179 reads as t? in kar[t?]im. That is a hypothesis for that card.

## Response to review 1

Verdict ACCEPT. All three minor findings are taken up; no letter of the Hungarian changes. Rerun after the edits: `python3 -I ciphers/hcp-1147/work/decode.py` gives hashes OK, 475 signs, 469 by the table, 6 by sense, every line matching.

1. **ablakomra blot: fixed.** I looked at the reviewer's enlargement (`review/work/crops/ablakc.png`) and agree: both loops are closed, so the sign is 8. The transcription stays, and the blot and the tension with "hozzád ... oda" are now listed under the uncertainties and noted under the English translation.
2. **Tally: fixed.** `work/transcription.txt` now marks légy as `4.~gy`, so the count is 469 + 6 and the list has six points. The abraded 7 of közepén (`review/work/crops/n4k.png`) is listed. The "each recurs" sentence now says that `6.` and `8.` occur once on this card.
3. **kis angyalom: fixed.** English and Slovak now take it as a vocative to Margitka, and the note mentions the apposition reading.
