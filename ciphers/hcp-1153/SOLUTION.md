# hcp-1153 solution (round 1, revised after review 1)

Solver: Claude Opus 5.5, 2026-11-02. No earlier work on this number. The portal attaches no solution or transcription and gives the status Not solved. The HistoCrypt article the portal links was not checked for this card, so I cannot say whether it discusses it. The transcription was made from the pixels of `work/hires/`. No transcription was attached, so `work/transcription.txt` is my own.

## Cipher type and key

Hungarian text in a digit cipher (register label: MASC), to Margitka Sziber, Szomolya. Almost the whole message is enciphered; only `Ha ibolyát látok`, `Eszembe`, the place and date, and the address are in clear. Each letter is one sign: a digit, or a digit with a mark. The mark is part of the sign. The key is the Mezőkövesd family key of FINAL cards hcp-1174, 1178, 1179 (reviewed), with `4.`, `5.`, `6`, `6.`, `.1` as filed on sister cards hcp-1170 to 1173 and others of this batch. Nothing was invented for this card.

Key status of the five added signs: `4.`, `5.`, `6`, `6.`, `.1` are on no FINAL table, and two conflict with FINAL cards: hcp-1178 and 1179 file `5.` as a variant of l (here ly), and the review of hcp-1178 dropped `.1` from that key (here u). They stand as values of this card and of not-yet-FINAL sisters. On this card `oly` twice settles `5.` = ly, and `jutsz` alone carries `.1` (see uncertainty 6).

| sign | letter | | sign | letter | | sign | letter |
|---|---|---|---|---|---|---|---|
| `0` | o, ó | | `2,` | cs | | `6` | j |
| `0,` | ö, ő | | `2.` | é | | `6,` | n |
| `1` | i, í | | `3` | d | | `6.` | ny |
| `1,` | b | | `3,` | r | | `7` | k (crossed) |
| `1.` | a, á | | `3.` | v | | `7,` | s |
| `1°` (raised ring) | á | | `4,` | g | | `7.` | sz |
| `1:` | e | | `4.` | gy | | `8` | m |
| `.1` | u | | `5` | h | | `8,` | t |
| `:1` | ü, ű | | `5,` | l | | `9` | p |
| | | | `5.` | ly | | `9,` | z |

The dot height of `1.` varies. The family separates `1'` (high dot, á) from `1.` (a), but this card does not do so reliably, so all are transcribed `1.` and the accent in the plaintext comes from the word. `0`/ó, `1`/í and the like are likewise not told apart. The card also has a slanted hooked stroke, shown `)` in the transcription, which behaves as punctuation (after `leértem`, `írni`, `imádód`, `Árpád`).

## Plaintext (Hungarian; [ ] = enciphered on the card)

Mezőkövesd. VI/9

[Édes Margitkám! Értesítlek, hogy szerencsésen leértem. Most pedig itt vagyok az állomáson, várom a vonatot, a vonat még soká jön, tehát ráérek írni, drága Margitkám, itt látok síró asszonyokat, amint válnak el az övéiktől, és most én is iszonyodva gondolok az elválásra, mert még ha mást lát is az ember, még az is könnyet csal a szemébe.]

Boxed verse:

Ha ibolyát látok [lányka]
Eszembe [jutsz én nékem]
[Oly szerény vagy te épen]
[És oly szép is édesem]

[Most pedig szá(m)talanszor ölel és csókol hű imádód Árpád]

Address (clear): Őnagysága / Sziber Margitka / kisasszonynak / Szomolya / u. p. Bogács. The picture side (violets) has no writing. The postmark was not read.

The punctuation is mine, except `!` after the salutation. Word divisions are mine; the writer leaves only small gaps.

## English translation

Sweet Margitka! I inform you that I got down safely. Now I am here at the station, waiting for the train; the train will not come for a long time yet, so I have time to write, dear Margitka. Here I see weeping women as they part from their own, and now I too think with horror of the parting, for even when one sees someone else [part], even that brings a tear to one's eye.

When I see a violet, little girl,
You come to my mind;
You are just as modest
And just as lovely too, my sweet.

And now, countless times, your faithful adorer Árpád embraces and kisses you.

## Slovak translation

Moja sladká Margitka! Oznamujem ti, že som šťastne došiel dolu. Teraz som tu na stanici, čakám na vlak, vlak ešte dlho nepríde, takže mám čas písať, drahá Margitka. Vidím tu plačúce ženy, ako sa lúčia so svojimi, a teraz aj ja s hrôzou myslím na rozlúčku, lebo aj keď človek vidí niekoho iného, aj to mu vženie slzu do oka.

Keď vidím fialku, dievčatko,
spomeniem si na teba;
si práve taká skromná
a aj taká pekná, moja milá.

A teraz ťa nespočetnekrát objíma a bozkáva tvoj verný ctiteľ Árpád.

## Command

Run from the repo root:

    python3 -I ciphers/hcp-1153/work/decode.py

It checks the SHA-256 of all four scans, decodes every sign of `work/transcription.txt` by the table, asserts that the whole decoded string equals the stated reading letter for letter (accents folded), and prints each row and the full text. The clear words and the address are printed from the script.

## Uncertainties

One sign is flagged `?` in the transcription and takes its value by sense. Of 348 signs (the script prints the count) all the others decode by the table as written, though points 2 to 4 rest on a comma that collides with the row below.

1. L11, `ha`: the 5 is clear, but no dot is visible after the following 1 at the line end (`work/crops/x2.png`). The table gives `hi`; `mert még ha ... is` fixes a.

Points that decode by the table but deserve a note:

2. L04, the t of the second `vonat`: the 8 is rubbed and its comma runs down onto the top of the 3 on L05 (`review/work/von.png`). A 3 has no ascender, so the stroke can only be the comma of the 8. Without it the word would be `vonam`.
3. `szá(m)talanszor`: the card has one 8 only, `7. 1. 8, 1. 5,` (`review/work/szamal.png`). A stroke rises right of the 8 from the 0 of `csókol` on L15, above that 0's body. A 0 has no ascender, so I take the stroke as the comma of the 8, as at `vonat` and `lát`: `8,` = t, with the m left out by the writer. The pixels are less clean here, because the printed `nach` and the crossed 7 lie on the same spot. If the stroke is not a comma, the sign is `8` and the lost letter is the t instead. Either way one letter is missing and the word is certain; hcp-1174 spells it in full.
4. `lát`, L12: `5, 1. 8,`. The comma of the 8 is not clean. It runs down into the top of the 6 of `könnyet` on L13 (`review/work/lat6.png`, `lat10.png`): a steep upper part, a thick join with a sideways tick, then the 6's ascender at a lower angle. The next 6 on the row has a shorter ascender with no such upper piece. Height alone would not decide it, as 6 ascenders vary; the join, the change of angle and the grammar do. Round 1 read `lám`, wrongly.
5. `mást lát is az ember`: `mást` stands alone and the writer does not say what the others are doing; the bracketed "[part]" in the English supplies that from the sentence before. `az ember` is the subject of `lát`.
6. `jutsz`: the dot between 6 and 1 sits at the foot of the 1 (`work/crops/e1.png`), read as `6 .1`. Read as `6. 1` it gives `nyitsz`, which does not fit `Eszembe`.
7. `lányka`: the raised ring after the 1 (`work/crops/e2.png`) is read as a form of the high mark, á. It is not a digit 0: `lionka` is no word.
8. `szemébe`: the last two signs stand at the margin. `1,` has a long comma running to the ruled line and `1:` opens with a hook, so it looks like a 7 at first sight, but it has two dots and no cross (`work/crops/z2.png`).
9. `ráérek`, `3,`: the comma runs down and touches the 0 of `látok` on the next row (`work/crops/y2.png`). It sits at the usual lower right of the 3, so I take it as this sign's comma. `ráédek` is no word.
10. `csal`: two dots sit close together after the 1, read as `1.` with a doubled or smeared dot (`work/crops/z1.png`).
11. `csókol hű`: L15 and L16 run under the printer's logo and the `Farben-Aufnahme` line; the violet signs are still legible (`work/crops/f1.png`, `f2.png`, `y6.png`). The ó and ű have no accent of their own in the cipher.
12. `Értesítlek`: the card has no e between t and l; the usual form is `értesítelek`. Kept as written. `épen` is the older spelling of `éppen`.
13. The date gives VI/9 with no year. The portal filename says 1916-06-09. The stamp's year was not read.

## Why I believe it is correct

- A key built on other cards and this batch's sisters, turns all 348 signs into continuous Hungarian, apart from the one flagged sign. Long, unforced words appear: `szerencsésen`, `asszonyokat`, `iszonyodva`, `elválásra`, `állomáson`.
- The clear words fit the cipher around them: `Ha ibolyát látok [lányka]`, `Eszembe [jutsz én nékem]`. The verse closes on near-rhymes (`nékem`, `épen`, `édesem`) and the card's picture is violets.
- The opening is the 13-sign heading of hcp-1174, and the signature `Árpád` is that of hcp-1174, with the same signs apart from the dot height of the 1.
- Weeping women parting from their men at a station fits Hungary in 1916, though the card does not say the men are soldiers.

The key values `5.` = ly, `6` = j, `.1` = u, `4.` = gy, `6.` = ny are not on the table of hcp-1174 and were taken from cards of this batch. Each is confirmed here by clean words: `oly` twice, `jön`, `jutsz`, `vagyok`, `vagy`, `hogy`, `asszonyokat`, `szerény`, `iszonyodva`, `lányka`.

## Response to review 1

Verdict REVISE, seven findings. All addressed; the reproduction command was re-run and passes (348 signs, 1 flagged).

1. `lám` / `lát` (major): fixed. I looked at `review/work/lat6.png` and agree: a stroke leaves the lower right of the 8 and joins the top of the 6 below, with a visible join and change of angle. L12 now has `8,`. The clause is `mert még ha mást lát is az ember, még az is könnyet csal a szemébe`, and my old items on `lám` and on loose syntax are withdrawn. Plaintext, `PLAIN`, both translations and uncertainty 4 and 5 are changed. The English adds "part", because `mást` alone leaves the object unfinished; this is disclosed in uncertainty 5.
2. `vonat` (minor): fixed. On `review/work/von.png` the stroke ends on a 3, which has no ascender, so my stated reason was wrong. The `?` is removed and the reason corrected; the flagged count goes from 2 to 1.
3. `ha`: no change needed, as the review says.
4. `szá(m)talanszor` (minor): adopted. On `review/work/szamal.png` the stroke rises above the body of the 0, so it fits a comma of the 8. Transcription `8,`, literal `szátalanszor`, printed `szá(m)talanszor`. The alternative stays disclosed in uncertainty 3.
5. Key table (minor): `9,` = z added.
6. `5.` = ly and `.1` (minor): disclosed in the key section, and the sentence "All values fit here without change" removed.
7. Stroke after the signature (minor): recorded as `)` at the end of L16 (`review/work/l14b.png`). It is not a comma of the 3; `Árpár` is excluded by hcp-1174.

Not resolved, as the reviewer could not settle them either: the postmark and the year (1916 rests on the portal filename), and the HistoCrypt article, which was not opened.
