# hcp-1158 solution (round 1)

Solver: Claude Opus 5.5, 2026-11-02. No earlier work on this number. The portal attaches no solution. The HistoCrypt article the portal links was not checked for this card, so I cannot say whether it discusses it. The key is transferred from the FINAL sister cards hcp-1174, 1178 and 1179 and extended here with two new signs.

## Cipher type and key

Register label: MASC. Hungarian monoalphabetic substitution by digit plus mark; the mark (none, `.`, `,`, `:`, high dot) belongs to the sign, and Hungarian digraphs have one sign. Almost the whole message is enciphered (316 signs, 26 distinct): the salutation, a four-stanza verse and the closing. Only a five-line request at the top, the place and date in the margin and the address are in clear. Word gaps are mostly kept on the card, but not everywhere.

| sign | letter | | sign | letter | | sign | letter |
|---|---|---|---|---|---|---|---|
| `0` | o, ó | | `2.` | é | | `5,` | l |
| `0,` | ö, ő | | `3` | d | | `6` | j (new) |
| `1` | i, í | | `3,` | r | | `6,` | n |
| `1.` | a | | `3.` | v | | `7` | k |
| `1:` | e | | `4,` | g | | `7,` | s |
| `1'` (high dot) | á | | `4.` | gy (new) | | `7.` | sz |
| `:1` (dots left) | ü, ű | | `5` | h | | `8` | m |
| `1,` | b | | `2,` | cs | | `8,` | t |
| `9` | p | | `9,` | z | | | |

The two new signs fit the pattern of the family, where a mark on a digit gives a second letter: `4.` = gy occurs 4 times (`vagy`, `egymáshoz`, `hogyha`, `légy`) and `6` = j once (`gondolj`). They are not in the tables of hcp-1174 or hcp-1179. Both were obtained here from word sense; `6` = j rests on that single occurrence.

## Plaintext (Hungarian)

Clear note at the top, normalised (the card has `szeretnek` with no accent, read as `szeretnék` by sense):

Ha lapomat megkapod és válaszolni fogsz légyél szíves megirni a Pista címét mert szeretnék már neki is irni.

The same note literally, with the card's five lines and its line-end hyphens:

    Ha lapomat megkapod és
    válaszolni fogsz légyél szíves-
    megirni a Pista címét
    mert szeretnek már neki-
    is irni.

Enciphered (accents normalised where the key does not mark them; the card's spelling `szivvel`, `ird`, `szeretö`, `csokol`):

Édes Margitkám!

Terem virág kis kertemben,
Terem künn a réten,
De a legszebb virág te vagy
Édes mindenségem.

Ha egymáshoz kincsem
Igaz szívvel leszünk
A boldogság révébe
Meglásd beevezünk.

Írd meg nékem édes szentem
Drága virágszálom
Leszel-e hogyha megkérlek
A szerető párom.

Ezt a pár sort küldöm
Neked szép babám
Légy boldog és gondolj
Néha-néha rám.

Számtalanszor üdvözöl és csókol hű kedvesed Árpád

Each verse line above is one written line of the card (card lines 1-16); the stanzas are card lines 1-4, 5-8, 9-12 and 13-16. The salutation (with a plain `!`) stands on the top line and the closing fills card lines 17-18. The writer rules a stroke under certain words. A heavy `)` follows `kedvesed` and another follows `Árpád`, with no opening bracket visible. These marks are not cipher signs and are recorded as a comment in `work/transcription.txt`.

Clear margin note: Mezőkövesd: 1916, I/11.

Address: Őnagysága / Rózsareményü / Sziber Margitka / kisasszonynak / (Borsod m.) Szomolya / u. p. Bogács

## English translation

If you get my card and are going to answer, please be so kind as to write me Pista's address, because I would like to write to him too.

Sweet Margitka!

Flowers grow in my little garden, / they grow out on the meadow, / but the loveliest flower is you, / my sweet everything.

If to each other, my treasure, / we are true of heart, / into the harbour of happiness, / you'll see, we will row.

Write and tell me, my sweet saint, / my dear flower-stem, / will you, if I ask you, / be my loving partner.

These few lines I send / to you, my pretty darling; / be happy and think / of me now and then.

Countless times your faithful sweetheart Árpád greets and kisses you.

## Slovak translation

Ak dostaneš môj lístok a budeš odpovedať, buď taká láskavá a napíš mi Pištovu adresu, lebo by som mu chcel tiež napísať.

Sladká Margitka!

Rastie kvet v mojej záhradke, / rastie vonku na lúke, / no najkrajší kvet si ty, / moje sladké všetko.

Ak k sebe, môj poklad, / budeme úprimného srdca, / do prístavu šťastia, / uvidíš, doveslujeme.

Napíš mi, moja sladká svätá, / drahý môj kvietok, / či budeš, ak ťa požiadam, / mojou milujúcou družkou.

Týchto pár riadkov ti posielam, / moja pekná milá; / buď šťastná a mysli / na mňa občas.

Nespočetnekrát ťa pozdravuje a bozkáva tvoj verný milý Árpád.

## Command

Run from the repo root:

    python3 -I ciphers/hcp-1158/work/decode.py

It checks the SHA-256 of all four scans, decodes every sign of `work/transcription.txt` through the key, asserts each line against the stated reading and prints the text plus the open parts (those are hard-coded). It reports 316 signs: 314 by the table, 2 by sense.

## Uncertainties

Signs that do not give the letter by the key (marked `<x>` in the transcription):

1. `virágszálom` (line 10): the first sign is a plain `3` (d) with no dot visible (`work/crops/t_virag.png`); sense needs `3.` (v). Literal: `dirágszálom`. Probably a dropped dot, since `virág` is written correctly twice.
2. `szentem` (line 9): the last sign has a clear comma, so the key gives `8,` = t (`szentet`); the vocative needs m. The comma is on the card (`work/crops/w_ent.png`). It may be a slip, or an ordinary line-end comma; the card has no other punctuation comma in the cipher.

Signs read by the key but partly dependent on word sense:

3. `kincsem`: the first sign's lower part is under a blot (`work/crops/t_blot.png`). The crossed 7 shows, but any dot or comma would be hidden. k rests on the word.
4. `hű`: the lower dot stands left of the 1 and the upper dot is not separate; the thickened flag tip may hold it (`work/crops/w_hu.png`). If the dot went with the 5 the signs would give no word (`li`, `hi`), and `csókol hű kedvesed` is a clean formula. This also fits third-person `üdvözöl`. No comma on the 5, so it is h.
5. `meglásd`: the upper dot of `1:` coincides with the printed vertical text "Printed in Germany"; only the lower dot is plain. `1.` would give `maglásd`, not a word.
6. `ezt a pár`: the `a` sign is uncrossed, so I read it as `1.`, not `7.`. This writer crosses every 7 seen here, and `7.` would give no word.
7. `üdvözöl`: the 0 before `5,` looks 9-like because its comma touches it, like the 9-shaped ö of hcp-1174; the sign shape alone could be `9,` (`üdvözzl`), so ö rests on sense.
8. The first word of the third stanza `Írd`, like other words, is `ird` by the key, which does not mark length. Word divisions in `hogyha meg` and `ezt a` are normalised.
8a. `egymáshoz`: the `8` carries a heavy extra stroke through its upper loop, like a correction (`review/work/z_em.png`). It still reads as 8 and the word is secure.

Open text and context:

9. `légyél szíves`: there seems to be an accent on the first e; normal form `legyél`. No effect on the cipher.
10. `Rózsareményü` is read from the normal-size address; it looks like a play on the usual title `Szépreményű`.
11. Postmark: Mezőkövesd is legible in part. Turned about 56 degrees (`review/work/z_pm56.png`) the date strip shows a group ending in 6 and a day group beginning with 1, which would suit 916 and January, but this is not a secure reading. The margin gives 1916, I/11 while the catalogue file name says 1915--12; I take the writer's date, and it rests on that note alone.
12. `Pista` is not identified. The verse was not traced to a printed source, and no search was made.

## Why I believe it is correct

- The transferred key turned the digits straight into Hungarian on the first pass: 316 signs, 314 by the table.
- The text scans and rhymes: réten/mindenségem, leszünk/beevezünk, virágszálom/párom, babám/rám. The rhyme is independent of the key.
- The signature `Árpád`, the salutation `Édes Margitkám` and the signs for `csókol`, `kedvesed`, `számtalanszor` are the same as on hcp-1174, whose key was not fitted to this card.
- The address (Sziber Margitka, Szomolya, u. p. Bogács) and the open note agree with the Mezőkövesd correspondence.
- The new signs fill gaps in the system (g/gy on 4, n/j on 6) and do not collide with any established value.

## Response to review 1

Verdict ACCEPT, five minor findings. No word of the reading changed. I rechecked findings 2, 4 and 5 on my own enlargements of the hires scan (`work/crops/note_a.png`, `note_b.png`, `end.png`, `margin.png`).

1. Count of `4.`: fixed. It occurs 4 times, as the transcription shows, and the example now reads `hogyha`.
2. Closing marks: agreed and fixed. Both `)` are visible in `work/crops/end.png`. They and the salutation `!` are now in the text above and in a comment line of `work/transcription.txt`. The comment leaves the sign count unchanged.
3. Overwritten `8` in `egymáshoz`: added as uncertainty 8a.
4. Clear note: agreed. `szeretnek` has no accent on the second e on the card. The note is now given both normalised and literally, with the hyphens after `szíves` and `neki`. `work/decode.py` prints both forms.
5. Verse layout and postmark: the sentence is rewritten (each verse line is one card line), and uncertainty 11 now reports the partial postmark evidence without claiming a date. I also corrected the margin to `1916, I/11.`, as the review quotes it; the comma is visible in `work/crops/margin.png`.

After these edits `python3 -I ciphers/hcp-1158/work/decode.py` still passes all hashes and line assertions: 316 signs, 314 by the table, 2 by sense.
