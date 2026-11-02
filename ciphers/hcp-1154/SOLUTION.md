# hcp-1154 solution (round 1, with response to review 1)

Solver: Claude Opus 5.5, 2026-11-02. No earlier work on this number; the transcription and reading are mine, from `work/hires/`. The portal attaches no solution and lists the card as Not solved. No published solution turned up, but the HistoCrypt article the portal links was not checked for this card.

## Card

Picture postcard (a couple on a birch bench; no writing on the picture side) to Sziber Margitka, Szomolya, u. p. Bogács, signed Sz. A. Date note top right 1915 XI/29; postmark Mezőkövesd 915 NOV 2-, last day digit not legible. The message is Hungarian plain text. The heading and the passage after `ne menjek.` are enciphered. The closing verse under the signature is in clear.

## Cipher type and key

Register label: MASC. It is the digit-plus-mark alphabet of the Mezőkövesd family: a digit with an optional mark is one letter, with no word division. The key was transferred from FINAL cards hcp-1174, 1178 and 1179; no key was built here. Four signs below are not in those three tables. Each is taken from the sister cards hcp-1161, 1162, 1163, 1164, 1166, 1168, 1169, of which 1163, 1164, 1166, 1168 and 1169 are now FINAL, and each makes a word here.

| sign | letter | | sign | letter | | sign | letter |
|---|---|---|---|---|---|---|---|
| `0` | o | | `3` | d | | `6,` | n |
| `1` | i | | `3,` | r | | `7` | k |
| `1.` | a | | `3.` | v | | `7,` | s |
| `1:` | e | | `4` | f (sisters) | | `7.` | sz |
| `1'` (single high dot) | á | | `4,` | g | | `8` | m |
| `.1` (dot at left) | u (sisters) | | `4.` | gy (sisters) | | `8,` | t |
| `2.` | é | | `5` | h | | `9` | p |
| | | | `5,` | l | | `9,` | z |
| | | | `6` | j (sisters) | | | |

Only signs on this card are listed: 24 distinct signs as written (the script counts 25 because it keeps the `3.` read as r apart), 116 sign tokens. Of the 116, 110 use the FINAL-card table, 5 use the four sister signs (`4.` twice) and 1 is read by sense (point 1 below). In this hand the 7 is always crossed, and the 5 carries a short top stroke.

## Plaintext (Hungarian; [ ] = enciphered on the card; inside it, me[r]t marks the one sign not read as written)

[Kedves Margitkám]!

Szerencsésen haza értem, épen a hat órát ütötte a toronyóra mikor a piacra értem nagyon hideg volt már talán nem is igen megyek ‹one deleted word› Karácsonyig, de más-különben nem is tudnám megálni, hogy ne menjek. [Kedves Margitkám nem hiszem hogy nem haragudnál ne is tagad me[r]t tegnap észre vettem aszt pedig el se képzeled hogy fáj ez nekem.] Sz. A.

Hiába jártam utánad
Reményeim mind elfogytak.
Olyan lett a szívem mint a
jégvirágos téli ablak.
Mindnyájatokat csókollak

Normal spelling of the cipher part: Kedves Margitkám, nem hiszem, hogy nem haragudnál, ne is tagadd, mert tegnap észrevettem, azt pedig el se képzeled, hogy fáj ez nekem.

Address: Tek. Szépreményű Sziber Margitka kisasszonynak / Szomolya / u. p. Bogács.

## English translation

[Dear Margitka]!

I got home safely; the tower clock was just striking six when I reached the marketplace. It was very cold already. Perhaps I will hardly go ‹deleted word› until Christmas, but otherwise I could not keep from going. [Dear Margitka, I do not believe you would not be angry, do not even deny it, because I noticed it yesterday, and you cannot even imagine how this hurts me.] Sz. A.

In vain I went after you,
all my hopes have run out.
My heart has become like
a frost-flowered winter window.
I kiss you all.

## Slovak translation

[Milá Margitka]!

Šťastne som došiel domov, vežové hodiny práve odbíjali šiestu, keď som prišiel na námestie. Bola už veľká zima. Možno ani veľmi nepôjdem ‹škrtnuté slovo› do Vianoc, ale inak by som ani nevydržal nejsť. [Milá Margitka, neverím, že by si sa nehnevala, ani to nepopieraj, lebo včera som si to všimol, a ani si nevieš predstaviť, ako ma to bolí.] Sz. A.

Márne som za tebou chodil,
všetky moje nádeje sa minuli.
Moje srdce je ako
zimné okno s ľadovými kvetmi.
Bozkávam vás všetkých.

## Command

Run from the repo root:

    python3 -I ciphers/hcp-1154/work/decode.py

It checks the SHA-256 of all four scans, decodes `work/transcription.txt` with the key, asserts the stated cipher reading and prints the sign counts, the raw decode and the full card. The clear text is hard-coded in the script, so the command reproduces only the decoding of the cipher signs.

## Uncertainties

1. `mert`: the third sign is written `3.`, a short slanted dot of the same form as in `kedves`, and every comma in this hand has a long tail. So the card has `mevt`, and I call that a writer's slip for mert, read as r by word sense only. It is the one sign not read as written, and it is printed `me[r]t`.
2. Writer's spellings kept as written, not corrected: `tagad` for tagadd (one sign for a double letter, as in `legszeb` on hcp-1179), `ész-` / `re` with a hyphen at the row end, and `el-` / `se` hyphened the same way at the next row end, though el se is two words, `más-` / `különben` hyphened at a row end of the clear text, one word máskülönben, `aszt` for azt (`7.`, not `9,`, is clearly written), `megálni` for megállni in the clear text, and `épen`.
3. `hiszem`, `haragudnál`, `tegnap`: at first sight `haragudnel` and `tegnep` looked possible, so I checked at 5x. After the 6, of haragudnál there is one high dot only (`work/crops/y1.png`), so `1'` = á; the 1 in tegnap has one low dot only, so `1.` = a.
4. `ne is tagad` could in principle be another segmentation, but no word division is written; `nél ne` fails because the high dot gives á. The word division throughout is mine.
5. The four sister signs come from other cards, not from hcp-1174, 1178 or 1179. They are now on FINAL hcp-1163 and 1168. Here each occurs in a certain word: `4.` in hogy (twice), `.1` in haragudnál, `4` and `6` in fáj. `6` occurs once and shows no comma; `fáj ez nekem` depends on that.
6. Deleted word after `megyek`: inked over by the writer; only a tall opening stroke with a curved start and a small hook above it, an accent near the end, and a small closed end loop survive. It is unread, and it is a deletion, so the sentence reads without it.
7. Clear text: `Mindnyájatokat`: the j is short and looks s-like, and the accent on the á stands high, so the group can look like `isa`; the word is read by sense from the rest of the letters. `talán` has the writer's a, which looks like `oi`.
8. A small mark after `csókollak` at the card's edge (a hook with a short dash and a curl) is unexplained: a flourish or punctuation, with no letter value claimed.
9. Whether `Sz. A.` covers only the cipher passage: the signature sits at the right end of the last cipher row, above a ruled line, and the verse follows below it. Identity of Sz. A. is not established from this card; hcp-1174 signs Árpád in cipher in the same correspondence.
10. Postmark day: `2` is legible, the next digit is not. The handwritten date gives 29. That note is blue on the scan, near the colour of the ink, so my round 1 word pencil is withdrawn; I cannot tell the medium.
11. `téli` has a long stroke drawn directly under it. It looks like the writer's underline, but the card does not prove it. The word itself is secure.
12. `már` has no punctuation around it: `nagyon hideg volt már talán nem is igen megyek` can end the first clause (it was already very cold) or open the second (now perhaps I will hardly go). Both translations take the first, and the sense changes little.

## Why I believe it is correct

- A key taken from other cards, with nothing fitted to this card, decodes 115 of 116 signs as written into a continuous, grammatical Hungarian passage that follows on from the clear text.
- The heading decodes to the same `Kedves Margitkám` as the card's opening position demands, and the phrase is repeated in full at the start of the passage, as the same sign strings.
- Sense fits the clear text: he got home, says he may not come till Christmas, then accuses her of being angry; the verse in clear (`Hiába jártam utánad ... Reményeim mind elfogytak`) has the same hurt tone.
- Enciphering only the painful personal passage fits the family's habit of hiding tender words on an open card.

## Response to review 1

Verdict ACCEPT, no change to any decoded sign. I rechecked each point on the reviewer's crops of the hires scan and on the sister cards. `python3 -I ciphers/hcp-1154/work/decode.py` still runs and passes after the edits.

1. `mert`, the odd sign: agreed and fixed. In `review/work/crops/z_3b.png` the mark after the 3 is a short slanted dot, unlike the long-tailed commas beside it on the 8s. The "very short comma" argument is withdrawn, the card is said to have `mevt`, a slip, and the plaintext now prints `me[r]t` here and in the script's full-card text. The normal-spelling line keeps mert.
2. `más különben`: agreed and fixed. `review/work/crops/t4.png` shows `más-` with a row-end hyphen. It is now given as `más-különben`, one word máskülönben, and listed in uncertainty 2. Translations need no change.
3. Underline: agreed and fixed. The stroke is plain in `review/work/crops/clr3.png`. Added as uncertainty 11 and in the script's full-card text.
4. `már`: agreed and fixed. English and Slovak now both attach it to the first clause, and uncertainty 12 gives the other division.
5. Deleted word: agreed and fixed. `review/work/crops/del.png` shows the end loop and the hook; uncertainty 6 now names them. The word stays unread.

From the "could not verify" list: the date note is blue on the scan (`review/work/crops/pen.png`), so "pencil" is dropped from the card description and uncertainty 10. The sister-sign wording under the key table is brought up to date: `4`, `4.`, `.1` and `6` are now attested on FINAL cards (hcp-1163 and 1168 have all four), and uncertainty 5 is reworded. The postmark digit, the HistoCrypt article and the identity of Sz. A. stay open.
