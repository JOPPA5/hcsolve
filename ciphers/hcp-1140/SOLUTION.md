# hcp-1140 solution (round 1, amended after review 1)

Solver: Claude Opus 5.5, 2026-11-02. No earlier work exists on this number. The portal lists the card as Not solved and attaches no solution. The HistoCrypt article the portal links was not checked for this card, so I cannot say whether it discusses it. The transcription is my own, made from `work/hires/`; there is no attached transcription.

## Card

Picture postcard (girl's head, print number 672/5, Printed in Saxony), written Mezőkövesd, 10 December 1915, signed Sz. A., to Sziber Margitka, Szomolya, u. p. Bogács. Part of the Mezőkövesd family (hcp-1135…1179). A faint pencil X crosses the message, and the name on the address is struck through in blue; neither hides any sign.

## Cipher type and key

Register label: MASC. Hungarian with chosen passages enciphered, one sign per Hungarian letter, a digit plus its mark. The mark is part of the sign, so `3` = d and `3,` = r. The key is the family key of FINAL hcp-1174 and 1179; `4.` = gy, `6` = j and `.1` = u also stand on FINAL hcp-1152, 1168 or 1170 (see below). Word spaces are visible and were followed, though `8 1 4,` and a few others are close-set.

| sign | letter | | sign | letter | | sign | letter |
|---|---|---|---|---|---|---|---|
| `0` | o | | `3` | d | | `6` | j |
| `1` | i, í | | `3,` | r | | `6,` | n |
| `1.` | a | | `3.` | v | | `7` | k |
| `1:` | e | | `4,` | g | | `7,` | s |
| `1'` (one high dot) | á | | `4.` | gy | | `7.` | sz |
| `.1` (dot to the left) | u | | `5` | h | | `8` | m |
| `1,` | b | | `5,` | l | | `8,` | t |
| `2.` | é | | | | | | |

The card has 125 cipher signs and 22 distinct key signs. By this table 123 decode as written; 2 are read by sense (below). No sign falls outside the table.

`.1` = u is not in the tables of hcp-1174 and 1179, but it stands on FINAL hcp-1168, where it was first found, and hcp-1152 (`csak ugyan`). Here it gives `ugy` and `ugysem`, each with a clear dot left of the 1. The card thus has plain u; `úgy`, `úgysem` in the plaintext are the normal spellings. hcp-1152 keeps `-1` = ú apart, while hcp-1170 after its review reads `-1` as u, ú and probably the same sign as `.1`; this card does not settle that, since `-1` does not occur here. `1,` = b comes from hcp-1179.

## Ciphertext

    7 1: 3 3. 1: 7, 8 1. 3, 4, 1 8, 7 1' 8 !
    (open text)
    7 1: 3 3, 1: 7, 8 1. 3, 4, 1 8, 7 1' 8 8 1' 3,
    .1 4. 5, 1' 8, 7. 1 7 5 0 4. 5 1 1' 1, 1. 7 2. 3,-
    5, 1: 7 5 0 4. 1 3, 6 1' 5, . 8 1' 3, 6, 1: 8 1 3, 7.
    6, 0 2. 6, 1 3, 0 7 8 1 4, 2. 5, 1: 7 5 1 7
    1: 7 8, .1 4. 7, 1: 8 7, 0 7 1' 1 4, 1, 1 3, 0 8
    1: 5, 3. 1 7, 1: 5, 6, 1 >
    (open verse) Igazán 7. 1: 3, 1: 8, 6, 1 !

## Plaintext (Hungarian; [ ] = enciphered on the card, punctuation inside is editorial)

[Kedves Margitkám]!
A legtisztább szívből üdvözöllek mindnyájatokat

[Kedres (= Kedves) Margitkám! Már úgy látszik, hogy hiába kérlek, hogy írjál. Már nem írsz, no én írok, míg élek, hisz eszt (= ezt) úgysem sokáig bírom elviselni.]

Féld az Istent, szeresd a dalt,
Növelj virágokat!
Isten emel, dal vigasztal,
Virág illatot ad!

Hiába, hiába
Nem tudlak feledni...
Csak tégedet foglak
Örökké keresni,
Igazán [szeretni]!

Sz. A.

Számtalanszor csókollak maradtam) Mezőkövesd, 1915. XII/10

Address: Tek. Szépreménnyü Sziber Margitka kisasszonynak, Szomolya, u. p. Bogács. Postmark: MEZŐK[ÖVESD], 915 DE[C], day illegible, printed stamp 5 fillér.

## English translation

[Dear Margitka]!
With the purest heart I greet you all.

[Dear Margitka! It already seems that I beg you in vain to write. You no longer write; well, I will write as long as I live, since I cannot bear this for long anyway.]

Fear God, love song,
Grow flowers!
God lifts up, song consoles,
A flower gives fragrance!

In vain, in vain,
I cannot forget you...
You alone I shall
Seek for ever,
Truly [love]!

Sz. A.

Countless times I kiss you, I remain) Mezőkövesd, 10 December 1915

## Slovak translation

[Milá Margitka]!
Z najčistejšieho srdca vás všetkých pozdravujem.

[Milá Margitka! Už to vyzerá tak, že ťa márne prosím, aby si písala. Už nepíšeš, no ja budem písať, kým budem žiť, veď toto aj tak dlho neznesiem.]

Boj sa Boha, miluj pieseň,
Pestuj kvety!
Boh povznáša, pieseň utešuje,
Kvet dáva vôňu!

Márne, márne,
Nemôžem ťa zabudnúť...
Len teba budem
Naveky hľadať,
Naozaj [milovať]!

Sz. A.

Nespočetnekrát ťa bozkávam, zostal som) Mezőkövesd, 10. decembra 1915

## Command

Run from the repo root:

    python3 -I ciphers/hcp-1140/work/decode.py

It checks the SHA-256 of the four scans, decodes every sign, asserts each word, reports the sign counts and prints the full text with the address. The open text is hard-coded in the script, so the command reproduces only the decoding of the cipher signs.

## Uncertainties

Cipher signs:

1. `hisz eszt` (end of row 6, start of row 7): both 7s are plain crossed 7s with no dot (`work/crops/z_h.png`, `z_e.png`), so the table alone gives `hik ekt`, which is not Hungarian. I read `7` as a dropped-dot `7.` = sz by word sense. Precedent: hcp-1152 has `hisz` and `haragszol` with the same lost dot, hcp-1151 `szőke`, hcp-1174 `szerető`. `eszt` is then the phonetic spelling of `ezt`; the family writer spells `aszt` for `azt` (hcp-1151, 1154). `hisz ezt` also fits the sentence, but the two signs rest on sense alone. The rest of the sentence does not depend on them.
2. `Kedres` (row 3): the second 3 clearly carries a comma (`work/crops/z_kd.png`), so it decodes to r. The same word on the top line has `3.`, so this looks like the writer's slip. It is printed as written, with the normal form beside it.
3. Top line, `Margitkám`: the 3, and the following 4, overlap and the sign is overwritten in part, but the short comma under the 3 and the 4's comma can both be seen (`work/crops/top3.png`).
4. `.1`: the round dot left of the 1 is clear on row 4 at 6x (`review/work/dot4.png`) and on row 7 (`work/crops/r7a.png`). Both are read as written. I no longer treat `így` as a live alternative in row 4.
5. Dots: `1'` against `1:` was checked at 4x or more at `már` (`work/crops/z_3.png`, `r5b.png`). A single high dot was seen each time.
6. Marks off the key: a dot before the 8 on row 5 is taken as a full stop after `írjál`; a small dot left of the first 7 on row 3 is taken as a speck or stop; the hyphen at the end of row 4 is a word-break (`kér-lek`); `>` closes the cipher block, meaning unknown. `no` could be `nó`; I read it as the interjection.

Open text:

7. `maradtam)`: written over the printed copyright mark and `672/5`, so the letters are cramped. It is read with FINAL hcp-1170 of 14 December 1915, which also closes `Számtalanszor csókollak mindnyájatokat maradtam`. On the red channel the reviewer saw m-a-r-a, an `ol`-shaped d, a crossed t and `am`; the cramped middle is partly leaned on that sister card. The closing `)` has no opening partner and is unexplained. The sentence ends without a following name, as on hcp-1170, and Sz. A. stands above.
8. `Féld`: the d looks like `ol`, which is this hand's usual d. `Hiába` and `tudlak`, `tégedet` read clearly; the first `Hiába` line has a faint line above it.
9. Date: the writer's last year digit is a looped 5. The postmark shows 915 DE, and the filename date on the portal is 1915-12-10.
10. Verses: no printed source was searched or found; I do not know whether they are the writer's own.
11. `üdvözöllek`: the card breaks the word as `üdv-` / `vözöllek` (`review/work/udv.png`, `udv2.png`), so the v is written twice. The plaintext prints the normal form; the doubled v is a slip of the line break.
12. Marks with no text value: rule lines between the sections (above the verses, under `Sz. A.`, above `Számtalanszor`); thin diagonal strokes down the right of the second verse and beside `Sz. A.`; a `>`-like curve at the right end of the `dalt` line, under the t, which is most likely a large comma; the `>` ending row 8 and the closing `)` after `maradtam`, which look like the same kind of flourish. None of them carries a sign. Their purpose is unknown.

## Why I believe it is correct

- A key fixed on other cards decodes 123 of 125 signs as written into continuous, correct Hungarian with no adjustment.
- The two salutations decode to the same two words but for one sign; the `szeretni` at the end completes the open verse and its sense (`Igazán szeretni`).
- `hogy`, `hiába`, `kérlek`, `írjál`, `elviselni`, `sokáig`, `bírom` are long words with repeated signs, not forced fits.
- Content agrees with the correspondence: the same complaint that she does not write and that he cannot bear it runs through hcp-1152 and 1161 of the same writer (`elviselni hisz` stands on hcp-1161); the signature Sz. A. and the address agree.

## Response to review 1

Verdict ACCEPT, six minor findings. I checked each on the crops and all stand. No sign and no word of the reading changed.

1. **Doubled v in `üdv-vözöllek`.** Agreed; `review/work/udv.png` shows `üdv` and a hyphen at the margin, `udv2.png` shows `vözöllek`. Noted as uncertainty 11 and in a comment in `work/decode.py`. The plaintext keeps the normal form.
2. **`ú` against `u`.** Agreed. The table now gives `.1` = u, and the note under it says the card has `ugy`, `ugysem`, cites hcp-1168 and 1152, and records that hcp-1170 treats `-1` differently from hcp-1152.
3. **Sign count.** Agreed. `work/decode.py` counted its internal token `7~sz` as a sign. It now folds that token back to the `7` written on the card and prints 22 distinct.
4. **Uncertainty 4.** Agreed; `review/work/dot4.png` shows a round dot clear of the stem. The `így` alternative is dropped.
5. **Undisclosed marks.** Agreed; listed as uncertainty 12. On `review/work/dalt.png` the curve under the t of `dalt` looks like a large comma, so I read it as punctuation, though `>` on row 8 and `)` remain unexplained.
6. **Register entry.** Type MASC. The `hisz eszt` and `Kedres` notes are carried into the report.

The reviewer's point that `maradtam` leans in part on hcp-1170 is added to uncertainty 7. hcp-1170 has since reached FINAL, so the references to it as in review are corrected.

Re-run after the fixes: `python3 -I ciphers/hcp-1140/work/decode.py` passes all four hash checks and prints 125 signs, 22 distinct; 123 by the table, 2 by sense. The decoded text is unchanged.
