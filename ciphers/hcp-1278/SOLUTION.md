# HCP1278 — a card to Jolánka Tóth signed, as read, Holes F.: safe arrival, consolation in sad days

**Status: complete reading of the message; small disclosed points only (see Uncertainties). The signature is the weakest part: its first sign is blotted, its last is interpreted, and the surname comes from sister cards, not from this card alone.** Solver: Claude Opus 5.5, 2026-11-01. There is no earlier work on this number. The portal shows status *Not solved* and attaches no transcription or solution. No published solution of this card was found or used. The transcription below is my own, from enlarged crops of the card; it was not a blind reading, since the family key and sister wording were known.

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented graphic signs: the "Jolánka" family key, as in HCP1216 (sign table there), 1212, 1213, 1217, 1218, 1243, 1301. All 17 rows stand in red ink on the left of the address side. Key as used on this card:

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | section mark / S / 8 shape | k | F-like | r |
| six | b | wave | l | right bowl | s |
| left bowl, often with a bar (€) | c | three short strokes | m | gamma/corner | t |
| short stroke left + long stroke (separate or joined, 4-like) | d | two short strokes | n | plain cross x | u |
| three bars | e | cursive loop, arched arm | o | chevron | v |
| open C with a tail at the foot | g | tall stroke + tick on the right (high = h, low = p) | h / p | crossed diagonal | z |
| same loop, straight arm, dot above | i | inverted T | j | C + y joined | gy |

Dots over o/u give ö/ü. The sign for f does not occur with certainty (see item 3). y and cs occur only as parts of gy and as c + s.

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1278/work/decode_opus.py
```

It checks the SHA-256 of the two source scans and the two hires originals, decodes the sign ledger `work/ledger-opus.txt` (one token per written sign), prints the literal letters row by row, and then prints the normalized text `work/normalized-opus.txt`. The ledger is a manual transcription from the pixels. Crops are in `work/crops/`.

## Literal decipherment (as printed by the command)

```
01 kedvesjolankatuda
02 tomhogyszerencse
03 se{blot}nmegerkeztem.
04 azútelegrövid
05 voltmivelhogy
06 ketenvoltunkhogy
07 telnekmostaniszo
08 morunapjaivig{blot}
09 gasztalodjonedesjo
10 lankamezenmarse
11 giteninemlehet.
12 nezelhogyijszomo
13 runapokbaeztalapot
14 küldökdenincsitho[n]mas
15 [ü][d]vözlömatavolbol
16 [h]oles{r=F.}tisztelemazot
17 maradtakat
```

Square brackets mark the signs discussed in items 1, 2 and 3. `{r=F.}` is a sign whose keyed value is r and which is read editorially as the initial F. (item 3).

## Hungarian (normalized)

Kedves Jolánka! Tudatom, hogy szerencsésen megérkeztem. Az út elég rövid volt, mivel hogy ketten voltunk. Hogy telnek mostani szomorú napjai? Vigasztalódjon, édes Jolánkám! Ezen már segíteni nem lehet. Nézze el, hogy ily szomorú napokba[n] ezt a lapot küldöm, de nincs itthon más. Üdvözlöm a távolból. [H]oles [F.] Tisztelem az ott maradtakat.

Plain hand in the stamp box, not enciphered: Csókolom a távolból.

Address, plain hand: Szépreményű Tóth Jolánka kisasszonynak, Jász Árokszálás. Printed verse on the picture side: *Hulló falevél … Sárgult falevél … Ajkam ajkadat érintve … Nem szól; csak szivem beszél.*

## English

Dear Jolánka! I am letting you know that I arrived safely. The journey was short enough, since there were two of us. How are your present sad days passing? Be comforted, my sweet Jolánka! This can no longer be helped. Forgive me for sending this card in such sad days, but there is no other in the house. I greet you from afar. [H]oles [F.] My respects to those who stayed there.

In the stamp box: I kiss you from afar.

## Slovak

Milá Jolánka! Oznamujem Vám, že som šťastne docestoval. Cesta bola dosť krátka, keďže sme boli dvaja. Ako plynú Vaše terajšie smutné dni? Utešte sa, sladká moja Jolánka! Tomu sa už pomôcť nedá. Prepáčte, že v takých smutných dňoch posielam túto pohľadnicu, ale doma nemám inú. Pozdravujem Vás z diaľky. [H]oles [F.] Moju úctu tým, čo tam zostali.

V poli na známku: Bozkávam Vás z diaľky.

## Uncertainties

1. **Row 15, *üd* is a restoration supported by the pixels.** The first two signs are heavily overinked, but not featureless. Two blobs stand above a clear X with both diagonals visible at lower left, and to the right a short stroke merged with a blob and a full long stroke. That is the form of ü + d in row 14. *Üdvözlöm* is also the only word found for `[..]vözlöm`, and the same greeting stands on HCP1305 and HCP1308, where the opening ü is blotted too. It stays bracketed because the blots prevent a clean reading.
2. **Row 14, n of *itthon*.** The sign has two slanted strokes crossed by two bars (#-like), so it was overwritten. n fits the two strokes, and *itthon* is the word. The n rests on word sense.
3. **Row 16, the signature.** The first sign is blotted: one, perhaps two, heavy slanted strokes left of the o loop. Its class is open among d, h, p and n. On this card the name is therefore only `[?]oles`, and *Holes* rests on two cross-references that cite each other: HCP1303 (*cím Holes Fe…*, plain, capital uncertain) and HCP1309 (*holesferi*, first letter open between d/h/p). The last sign has the form of the heavy r of rows 13 and 17, with its point inside the bars at the lower right of the arm, and its crossbar also runs left of the stem. By the key it is r; the family's f is a different sign, the upright cross. I read it as an initial, **F.** in a Latin capital amid cipher, and that is an interpretation, not a decipherment. Literal: *[?]oles r*, which is no word. No identification with "Feri" of the other cards is proved.
4. **Blots with no letter value.** Row 3: a blot between *se* and *n*; *szerencsésen* needs no letter there, and whatever is under it is not known. Row 8: after *vig* a large blot with stroke ends showing; row 9 then starts *gasztalódjon*, so *vigasztalódjon* needs no letter from it. The likely story is a started and blotted g, then a restart, which is not provable.
5. **Row 9, d of *édes*.** The sign has its tick on the right, which is the h/p shape; on this card d normally has the short stroke on the left (rows 1, 14). *édes Jolánkám* decides it, as with the *de* of HCP1216.
6. **Rows 7 and 17, m.** Row 17: the third stroke of the m of *maradtakat* is short and is overlaid by two dark foxing specks. m is by far the best reading, since *naradtakat* is no word, but it rests partly on word sense; my first working reading of rows 16–17 was *ner…* (NOTES.md). **Row 7, m of *mostani*.** Three strokes, the third longer, then a small separate tick. The tick could make the third stroke an h/p sign, giving `n + p`, *npostani*, which is no word. I read m and leave the tick without value. This rests on word sense.
7. **Row 12, *nezel*.** The signs are clear (n e z e l), with three small bright dots beside the z. I read those as spatter; they have no value. Many free marks stand on this card (over the r of row 2, after the gy of row 2, under most k signs, around z here). *Nézze el* ("overlook, forgive") is an editorial reading of *neze el* with the two e's run together. Plain *nézel* ("you look") would break the formal address used throughout, so I reject it.
8. **h/p.** The two are one class and are split only by word: h in *hogy, lehet, itthon*, p in *napjai, napokba, lapot* (these three have the tick low, as a real tendency on this card). Row 13 and row 8 show this low tick clearly.
9. **Row 16–17, *ott maradtakat*.** Literal *azot | maradtakat*. I normalize to *az ott maradtakat* ("those who stayed there"), with one t dropped. *ot* is not a word on its own in this sense, so this is an interpretation. The writer's doubled letters are often single (*ketten* → *keten*, *itthon* → *ithon*).
10. **Other writer spellings normalized:** *mivel hogy* kept as written; *ij* → *ily*; *napokba* → *napokba[n]*; *küldök* → *küldöm* (the sign is a clear k; the object is definite, so this is an editorial change). Accents other than the ú of row 4 are not transcribed from the card and are supplied, apart from ö/ü dots. The mark over row 4's u is larger than the free marks of the card, so ú is likely, not read; it changes nothing, since *út* is required. The ledger's ö in rows 4, 14, 15 and the ü in row 14 have visible dots or blobs above the sign, except the first ö of row 15: of its two "dots", one is a free blob and the other looks like the foot of row 14's d, so that ö rests on the word.
    Sentence points stand after *megérkeztem* (row 3) and *lehet* (row 11). Row 2: the c of the joined gy of *hogy* is heavily blotted or overwritten; the word is certain.
11. **Stamp box.** The plain text reads *csókolom a távol-ból*. Its first letter lies under a pink blot and is restored. To the lower right stand two small pen marks, one pale, one darker, that look like an y and an H-like or 4-like form. They are not in the row of the text, I cannot read them, and I give them no value. They are not on the cipher side and do not affect the message.
12. **Date and identity.** The postmark shows ÁROKSZÁ…, 912, and 27; the month is not legible. The portal file name gives 1912, with the month blank and day 27. A second cancellation rings the stamp box, with letters like G and V or Y and a date band containing 91 and another digit. It is seen but not read, and it is likely the departure office, so where the writer was remains unknown. The bereavement or misfortune behind "sad days" is not named on the card. *Ketten* ("two of us") is not explained either.

## Why it is correct

- The family key, taken over without change, turns all 17 rows into Hungarian with no sign left over, apart from the two blots of item 4, the small marks of items 6, 7 and the signature's last sign (item 3).
- Long stretches read with no choice: *Tudatom, hogy szerencsésen megérkeztem* (same wording as HCP1243 and 1310), *az út elég rövid volt, mivel hogy ketten voltunk, hogy telnek mostani szomorú napjai, ezen már segíteni nem lehet, ezt a lapot küldök* (as written; *küldöm* is the editorial form) *de nincs, vözlöm a távolból, tisztelem*.
- The content fits the card itself: the writer apologizes for sending a love-picture card (a kissing couple) in sad days, because he has no other in the house. This is a check independent of the key.
- Repeated signs decode the same way: *hogy* ×4 (rows 2, 5, 6, 12), *szomo|rú* ×2 (both split across a row break, rows 7–8 and 12–13), *jolánk-* ×2 (rows 1, 9–10).
- The plain stamp-box greeting (*a távolból*) repeats the cipher's *a távolból* of row 15.

Credit: key and sign classes from the finished family cards (earlier work by the OpenAI GPT solver and Claude Opus 5.5, see those directories). Transcription and decipherment of this card by Claude Opus 5.5.

## Response to review 1

Verdict REVISE. Every finding was rechecked on the reviewer's crops and addressed. The normalized Hungarian words do not change; only the bracketing of the signature is new.

1. **Row 13, a not e (major): fixed, agreed.** `review/work/crops/y13a.png` shows the gamma, two bars, then the wave, and the a of *lapot* has the same two spaced bars. My "three bars are clearly written" was wrong. Ledger token changed to `A`, literal row 13 is now `runapokbaeztalapot`, and the *ezt e* note is deleted from item 10. *ezt a lapot* now stands as written.
2. **Row 16, last sign (minor): fixed.** The ledger token is now `{r=F.}`, so the literal line shows the keyed value r and flags the reading. The normalized text and translations give *[H]oles [F.]*, and the status line and item 3 say the signature is the weakest part. HCP1296 is no longer cited, as it is unfinished and has its own doubt about H.
3. **Row 15 (minor): fixed.** Item 1 now describes what `r15L.png` shows, including the clear X and the strokes, matching ü + d of row 14.
4. **Row 16, first sign (minor): fixed.** Item 3 states the class as open, with n added, and says the surname rests on the sister cards alone.
5. **Row 17, m (minor): fixed.** Added to item 6, with the first reading *ner…*.
6. **Unlisted blots and marks (minor): fixed.** Row 2's gy blot and row 11's point are in item 10, and the point is now in the ledger as in row 3. The row 15 "dot" and the likely-not-read ú are in item 10, the free marks in item 7, the stamp box blot in item 11.
7. **Second postmark (minor): fixed.** Reported in item 12 as seen and unread. I looked at it again in `work/crops/pm2-180.png` and could not read the office either.
8. **küldök / küldöm (minor): fixed.** Item 10 and "Why it is correct" now keep the two apart.

The reproduction command was re-run after these changes and passes all four hash checks; its output is the literal block above.
