# hcp-1139 solution (round 1, with response to review 1)

Solver: Claude Opus 5.5, 2026-11-02. No earlier work on this number. The portal lists the card as Not solved and attaches no solution or transcription. The HistoCrypt article the portal links was not checked for this card, so I cannot say whether it discusses it. The transcription is my own, made from `work/hires/`.

## Card

Picture postcard (a girl's portrait, printed in Saxony), to Sziber Margitka, Szomolya. All of the message is enciphered, including the boxed signature. Only the place and date (up the margin) and the address are open. The portal's main category is Substitution and its language Unknown; the language is Hungarian.

## Cipher type and key

Register label: MASC. It is the digit cipher of the Mezőkövesd cards. One letter is one digit plus an optional mark; there are no word divisions. The key was transferred from FINAL cards hcp-1174, 1178, 1179; the signs `4.`, `6`, `6.`, `2`, `.1` come from hcp-1148 and 1160 (awaiting review when this was first written, FINAL now), and all five are confirmed by words here. For `2` (only in `tubicám`) and `6.` (only in `aranyos`) that is one word each, and `2` comes from hcp-1148 alone, not from hcp-1160. No value was invented for this card.

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| `0` | o, ó | `2,` | cs | `6,` | n |
| `0,` | ö, ő | `2.` | é | `6.` | ny |
| `1` | i | `3` | d | `7` | k |
| `1.` | a | `3,` | r | `7,` | s |
| `1:` | e | `3.` | v | `7.` | sz |
| `1'` (high dot) | á | `4,` | g | `8` | m |
| `1,` | b | `4.` | gy | `8,` | t |
| `.1` (dot left) | u, ú, ű | `5` | h | `9` | p |
| `:1` (two dots left) | ü | `5,` | l | `9,` | z |
| `2` | c | `6` | j | | |

`work/transcription.txt` holds every sign, line by line. The script reports 366 signs: 364 by the table (using all 29 signs above) and 2 by sense.

## Plaintext (Hungarian; punctuation and word division mine, spelling as on the card)

(open) Mezőkövesd 1916 I/6

Kedves Margitkám!
Hogy múlt el az új év neked, jól-e vagy rosszul? Mert nekem nagyon rosszul, egyrészt mer [= mert] nem veled tölthettem, az tán [= aztán] meg máskép [= másképp] is egy kicsit beütöt [= beütött] a krak [= krach].
Aranyos babuskám, szeressél igazán.

Boldog csak úgy lehetsz,
hogy ha engem szeretsz.

Üdvözletem küldöm, édesem, tenéked,
úgy szeressél engem, mint ahogy én téged.
Nem kérek Istentől kincset, gazdagságot,
csak téged, tubicám, s hozzád boldogságot.

Sokszor csókolva és üdvözölve téged maradok hű kedvesed
Árpád

Address (open, as written): Őnagysága / Sziber Margitka / ur-leánynak / Szomolya / u. p. Bogács

## English translation

Mezőkövesd, 6 January 1916

Dear Margitka of mine!
How did the New Year go for you, well or badly? For me very badly: first, because I could not spend it with you, and then in other ways too the crash has struck a bit. My lovely little darling, love me truly.

You can only be happy
if you love me.

I send you my greeting, my sweet,
love me as I love you.
I ask of God no treasure, no riches,
only you, my little dove, and with you happiness.

Kissing and greeting you many times, I remain your faithful sweetheart
Árpád

Address: Her Ladyship, Miss Margitka Sziber, Szomolya, post office Bogács.

## Slovak translation

Mezőkövesd, 6. januára 1916

Moja drahá Margitka!
Ako ti prešiel Nový rok, dobre alebo zle? Mne veľmi zle: po prvé preto, že som ho nemohol stráviť s tebou, a potom aj inak ma trochu postihol krach. Moja milá bábika, miluj ma naozaj.

Šťastná môžeš byť len tak,
ak miluješ mňa.

Posielam ti svoj pozdrav, moja sladká,
miluj ma tak, ako ja teba.
Nežiadam od Boha poklad ani bohatstvo,
len teba, moja hrdlička, a k tebe šťastie.

Mnohokrát ťa bozkávam a pozdravujem, zostávam tvoj verný milý
Árpád

Adresa: Jej Milosť, slečna Margitka Sziberová, Szomolya, pošta Bogács.

## Command

Run from the repo root:

    python3 -I ciphers/hcp-1139/work/decode.py

It checks the SHA-256 of all four scans, decodes every sign of `work/transcription.txt` with the key in the script, asserts each decoded word against the stated reading, prints the sign counts and the decoded card lines, then the reading text. The reading text with its punctuation and the open address is typed in the script.

## Uncertainties

Signs resting on word sense (2 of 366, `ODD` in the script):

1. `téged` in `mint ahogy én téged`: the first sign is a plain 8 with no comma (`work/crops/y_meged.png`), so the key gives `méged`. Rhyme with `tenéked` and the same word at two other places fix `téged`. I take it as a dropped comma.
2. First `rosszul` (line 3): under the 7 stands a heavy ink blot with a thin tail to the lower left (`review/work/crops/l3blot.png`). The pixels do not separate `7.` (sz) from `7,` (s), so I read `7.` by sense. The same word has a clear `7, 7.` in line 4. `rossul` would only be a spelling variant.

Other points:

3. `tölthettem` and `üdvözölve` (lines 5 and 20): the ö is a round 0 with a comma touching it, written tight, and I now count both as plain `0,` (see the response to review 1). In line 5 the stroke entering from above is the comma tail of the `5,` in line 4 (`review/work/crops/l5end.png`, `l20o.png`). A 9 alone would be p, but neither sign has the diagonal stem of the true `9,` beside it in line 20.
4. `tubicám`: the third sign is crossed by the comma tail of line 17, so it can look like a crossed `7,`, which would give `tusicám`. On `work/crops/y_tub.png` I read an entry stroke and one straight stem, the shape of a 1, with the comma under it, so `1,` = b. `tubicám` ("my little dove") is a normal endearment; `tusicám` is no word I know. This call leans partly on sense.
5. `krak`: the signs are clear (`7 3, 1. 7`). I take the word as the loanword krach, spelled by ear, in "beüt a krach" (a crash, a disaster strikes). This meaning is from my own knowledge, not checked in a dictionary. What the crash was (money, the war) the card does not say.
6. `hozzád`: the dot on the 1 is large and stands at mid to upper height (`work/crops/x_hozzad.png`). I read `1'` (á); `1.` would give `hozzad`, which does not fit.
7. `hű`: written `5 .1`, with the sign for u, as `.1` covers the long vowels here. No separate sign for ű is attested on this card.
8. `ha` in line 11: the `1.` lies in a blue blot, but its stem and dot are visible.
9. A dot stands left of the 5 in the first `hogy` (line 2). `.5` is not a known sign; I treat it as a stray, since `hogy` is plain 5 in line 11. The word is `hogy` either way.
10. Line 3 `jól e vagy`: the `e` stands alone, read as the question particle `-e`. The dot under the 3 of `vagy` is clear on `work/crops/y_ev.png`.
11. Curved ruled lines separate the sections of the message (after lines 7, 11, 15, 19) and a frame encloses the last two lines. A `>`-shaped stroke stands before `maradok`; it is unexplained, perhaps the end of that frame. These are not treated as cipher signs.
12. The postmarks are too weak to read a date. The date is the writer's own `1916 I/6`, which agrees with the portal's file name.
13. The source of the verses was not searched. They may be popular rhymes.

## Why I believe it is correct

- A key taken from other cards gives continuous Hungarian over 364 of 366 signs, with no adjusted value and no forced word.
- The verses rhyme with no help from me: `lehetsz` / `szeretsz`, `tenéked` / `téged`, `gazdagságot` / `boldogságot`, and the four long lines are all regular 6+6 syllables, which holds for the decoded text without any adjustment.
- The boxed signature decodes to `Árpád`, the signature of hcp-1174 and hcp-1148. The salutation decodes to `Kedves Margitkám`, the family formula and the addressee.
- The address repeats the recipient, and the New Year subject fits the date 6 January 1916.
- The closing formula matches the family (`hű kedvesed`, hcp-1148).

## Response to review 1

Verdict ACCEPT, five minor findings. All are addressed. No decoded letter or word changed. I looked at the reviewer's close-ups for findings 1 and 2 myself.

1. Blot in the first `rosszul`: fixed. On `review/work/crops/l3blot.png` the mark is a blot with a comma-like tail, as the reviewer says. The sign is now `7~sz` in `work/transcription.txt` and in `ODD`, and it is uncertainty 2.
2. "9-shaped ö": fixed, and further than the reviewer asked. On `l5end.png` and `l20o.png` I see a 0 with a comma touching it and no diagonal stem. The two signs are now plain `0,`, not `9~ö`. With finding 1 the count is 364 by the table and 2 by sense (it was 363 and 3; the reviewer's 4 assumed the old count was kept).
3. English nuance: fixed, now "has struck a bit".
4. Provenance of `2` and `6.`: stated under the key table. hcp-1148 has since become FINAL, so the earlier wording "awaiting review" is corrected there too.
5. Address: now given as written, `ur-leánynak`, in this file and in the script.

The command was re-run after these changes: hashes OK, every word assert passed, `cipher signs: 366, distinct: 31; 364 decode by the table, 2 rest on sense (ODD)`.
