# HCP1260 — Feri to Jolánka Tóth: apology for rare letters, a matter to settle by word of mouth

**Status: complete reading, one clause of uncertain syntax; review 1 (REVISE) addressed.** Claude Opus 5.5, 2026-11-01. No earlier work exists on this number. The portal catalogue row shows *Not solved* and lists no transcription or solution (the detail page timed out at capture, so the three tabs of this number were not read one by one; see `source/metadata.md`); no published solution was found or used. The key was transferred from the finished family cards (HCP1216 and sisters); the transcription in `work/ledger.txt` is my own, made from enlarged crops of `work/hires/*_adr.jpg` (`work/crops/`, script `work/crop.py`). It was not blind: I formed word expectations as I read.

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented graphic signs, written in red ink: the Jolánka family key of HCP1216, unchanged.

*Type note (2026-11-03):* the corner block is written in the stamp box, under the (now lifted) stamp, so the card is typed **MASC + Steganography** (see the stamp-box section below).

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | section mark | k | F-like | r |
| six | b | wave | l | right bowl | s |
| opposed bowls | cs | three short strokes | m | gamma/corner | t |
| short tick left + long stroke (see items 2, 9, 15) | d | two short strokes | n | plain cross x | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross + | f | tall stroke + short tick right | h (p) | y-loop | y |
| open sign with descender | g | dotted crossed curve | i | crossed diagonal with tail | z |
| inverted T (also a foot-left variant) | j | | | | |

On this card *gy* is written as the two signs g + y. Dots over o/x give ö/ü, two ticks over o give ő. The card has no separate mark for ű: *hű* is written with the two dots (*hü*) in rows 22 and C4. Acute accents are not reliably visible and are supplied.

**Not enciphered:** the address, in clear: *Szépreményű / Tóth Jolánka / úrleánynak / Jász Árokszállás*. "Szépreményű" sits at the end of cipher row 6 but belongs to the address, not the message. In the corner block, *7 het* is written in clear (digit and Latin letters).

The picture side carries no handwriting; only its printed verse (Lári-Fári, Cigányprímás).

## Stamp-box message (2026-11-03)

Stamp-box audit by Claude Opus 5.5, 2026-11-03, on crops of `work/hires/*_adr.jpg` (`work/stamp-2026-11-03/box.png`, 2x; `block4x.png` and `block4x_g.png`, 4x, green channel).

- **State: stamp lifted, writing under it.** The block that this solution calls the "corner block" fills the stamp box at the top right of the address side. The stamp itself is gone; a pink dye bleed over the upper and middle rows (typical of a soaked-off red stamp), a grey residue strip below the block, and the dark postmark stroke that stops at the block's lower-left edge mark where the stamp sat. The writing was therefore hidden under the stamp when the card was posted.
- **Script: cipher signs**, same key as the main text, with *7 het* in clear (digit and Latin letters). No plain-Hungarian writing was found elsewhere in the box.
- **Reading:** this is the 8-row corner block already in the ledger (`work/ledger.txt`, corner rows C1-C8) and decoded by `work/decode.py`; it was re-checked against the crops today and no sign changed. Literal: *istenve / leveede / semsirig / hükedve / jeviszont / latasra / 7hetmul / va*.
- **Hungarian (normalized):** Isten vele [ve] édesem, sírig hű kedvese. Viszontlátásra 7 hét múlva.
- **English:** God be with you, my darling, your sweetheart, faithful unto the grave. Until we meet again in 7 weeks.
- **Slovak:** S Bohom, drahá, Váš do hrobu verný milý. Dovidenia o 7 týždňov.
- **What stays uncertain:** the surplus *ve* in C1-C2 (item 11), the d of *kedve-* in C4 (item 15) and the s of *kedvese* in C5 (item 7). No clause is unread.

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1260/work/decode.py
```

It checks the SHA-256 of all four image files, decodes `work/ledger.txt` (one token per sign; 22 main rows plus 8 corner rows) and prints the literal rows and `work/normalized.txt`.

## Literal decipherment

```
01 szeretetedesjolan        12 erölirasbantargyal
02 kamegyetlenremenyemne    13 nideitlesznemsoka
03 haragudjonramhogyijen    14 raazidőhogyszoval
04 ritkanirokmitmagamis     15 beszelhetemagaval
05 restelekdeanyiraideges   16 edesemmitaligva
06 vagyokdenecsodelkozon    17 rokhogymulatot
07 rajtaedesemhogyhogy      18 vasarnapremelem
08 volnajobbdeerölnem       19 jolhogyszolgal
09 irokmajdszovalfo         20 jaazegesegremelem
10 gomelinteznieztaz        21 jolezelzaromso
11 ügyetmertnemakarok       22 raimmaradoksirighükedeseferi

corner: istenve / leveede / semsirig / hükedve / jeviszont / latasra / 7hetmul / va
```

## Hungarian (normalized)

Szeretett édes Jolánkám, egyetlen reményem! Ne haragudjon rám, hogy ilyen ritkán írok, mit magam is restellek. De annyira ideges vagyok. De ne csodálkozzon rajta, édesem, hogy hogy volna jobb, de erről nem írok; majd szóval fogom elintézni ezt az ügyet, mert nem akarok erről írásban tárgyalni. De itt lesz nemsokára az idő, hogy szóval beszélhete[k] magával, édesem, mit alig várok. Hogy mulatott vasárnap? Remélem, jól. Hogy szolgálja az egés[zs]ég[e]? Remélem, jól. Ezzel zárom soraim, maradok sírig hű ked[v]ese, Feri.

Corner: Isten vele [ve] édesem, sírig hű kedvese. Viszontlátásra 7 hét múlva.

## English

My beloved sweet Jolánka, my only hope! Do not be angry with me for writing so rarely, which I am ashamed of myself. But I am so nervous. But do not wonder, my darling, how it would be better [exact sense of this clause uncertain, see item 8], but I am not writing about this; I will settle this matter by word of mouth, because I do not want to discuss it in writing. But the time will soon be here when I can speak with you in person, my darling, which I can hardly wait for. How did you enjoy yourself on Sunday? Well, I hope. How is your health? Well, I hope. With this I close my lines; I remain, faithful unto the grave, your sweetheart, Feri.

Corner: God be with you, my darling, your sweetheart, faithful unto the grave. Until we meet again in 7 weeks.

## Slovak

Moja milovaná, sladká Jolánka, moja jediná nádej! Nehnevajte sa na mňa, že píšem tak zriedka, za čo sa sám hanbím. Ale som taký nervózny. Ale nečudujte sa tomu, drahá, ako by bolo lepšie [presný zmysel tejto vety je neistý, pozri bod 8], ale o tom nepíšem; túto záležitosť vybavím ústne, lebo o tom nechcem rokovať písomne. Ale čoskoro príde čas, keď sa s Vami budem môcť porozprávať osobne, drahá, na čo sa neviem dočkať. Ako ste sa zabavili v nedeľu? Dúfam, že dobre. Ako Vám slúži zdravie? Dúfam, že dobre. Týmto končím svoje riadky a zostávam do hrobu verný Váš milý, Feri.

V rohu: S Bohom, drahá, Váš do hrobu verný milý. Dovidenia o 7 týždňov.

## Uncertainties

Signs valued from word sense, not from a clean shape (`?` in the ledger):

1. **Row 1, 6th sign (t of *szeretet-*)**: heavily inked and overwritten; it looks like a t over or under a loop, or a blotted r. Read t: *szeretet-* is the only word. The card has *szeretet* with one t where *szeretett* is meant.
2. **Row 5, *de***: the sign has its tick to the **right** of the tall stroke, i.e. the h/p shape, not the d shape. *De* is word sense; HCP1216 row 5 has the same irregularity.
3. **Row 14, h of *hogy***: the tall stroke is blotted solid, and the sign looks like a thick g with a tick. *hogy* is word sense and fits the row.
4. **Row 18, p of *vasárnap***: the tick is to the **left**, the d shape. *vasárnap* is word sense; literal *vasarnad* is no word.
5. **Row 20, first sign (j of *-ja*), and row 3, j of *haragudjon***: a stroke crossing a low sloping bar with a short stub below it, between the inverted-T j and the f cross. Read j (*szolgálja*; f gives no word). The row 3 sign is the same variant and *haragudjon* is certain, which supports row 20.
6. **Row 20, last sign of *egeseg***: an overwritten sign (g with a y-like long stroke over it). Read g. The card has *az egeseg*; the normalized *egés[zs]ég[e]* brackets what is not on the card (the writer omits the z, as on HCP1216, and there is no final e).
7. **Corner row 5, first sign**: stroke with a foot to the left, nearest the foot-left j of row 1 (*jolan*); literal *kedveje*. Read as a reduced s, *kedvese*, which is the family's closing (HCP1216: *sírig hű kedvese*) and repeats row 22.

Writer's slips, read as written and normalized editorially:

8. **Rows 7–8, *hogy hogy volna jobb***: both *hogy* are clear, and the clause is the one uncertain place in the text. With *de* (item 9) I take it as an indirect question: "do not wonder how it would be better, but I am not writing about this". With *ha* it could be a repetition ("that it would be better if I do not write about this") or *hogyhogy*, "how come / how would it be better if I do not write about this". Either way the next clauses say plainly that he will settle the matter by word of mouth and not in writing.
9. **Row 8, *de* (preferred) or *ha***: the first sign has its tick to the **right** of the tall stroke, the h/p shape, exactly as in row 5 (item 2), and is followed by two distinct three-bar signs, so the strict literal is *he er-*. Read alike with row 5 it is *de erről nem írok*, "but I am not writing about this"; this needs no vowel change and only a shape slip of the kind that occurs in rows 5 and 18. The alternative is *ha erről nem írok*, "if I do not write about this", which keeps the h shape and changes the vowel (e for a). The value d rests on word sense. Spelling *-öl* for *-ről* with a single r also in row 12.
10. **Row 15, *beszelhetemagaval***: normalized *beszélhete[k] magával*, with the k of the verb supplied. The m belongs to *magával*. The definite form *beszélhetem* would not suit *magával*. The meaning is not affected.
11. **Corner rows 1–2, *Isten vele ve édesem***: a surplus *ve*, treated as a false start. Row 1's *ve* and n stand in a pink wash, but the signs are readable. The pink streak in corner row 2 is a smear, not a sign. If *ve* belongs to some other word, only that fragment is affected.
12. Other normalized spellings: *ijen* → ilyen, *restelek* → restellek, *anyira* → annyira, *csodelkozon* → csodálkozzon, *ezel* → ezzel, *mulatot* → mulatott, *hü* → hű (rows 22 and C4, two dots on the card), *jolan|kam* row break, *soka|ra* (nemsokára), *fo|gom*.
13. *7 hét*: the first sign is heavy and read as the digit 7 beside clear *het*; "in 7 weeks" reads naturally.
14. The postmark is too faint to read a place or date with confidence (a digit 2 and scattered letters only). The card is undated, and what "this matter" was is not stated.
15. **Corner row 4, d of *kedve***: two nearly equal tall strokes, closer to n than to the tick-plus-long-stroke d. *kenve* is no word; d rests on word sense.
16. **Row 22, *kedese***: the card has no chevron between d and e, so the literal is *kedese*, normalized *ked[v]ese* as an omitted letter. The word is firm: corner row 4 spells the v out and the family closing is *sírig hű kedvese*.

## Why it is correct

- The HCP1216 family key, applied unchanged, gives Hungarian for all 22 rows and all 8 corner rows; no sign is left without a value (the ten `?` signs are listed above: rows 1, 3, 5, 8, 14, 18, 20 twice, C4, C5).
- The text is coherent and idiomatic, with formal address (*haragudjon, csodálkozzon, magával*), and has an internal parallel that was not imposed: *Hogy mulatott vasárnap? Remélem jól. Hogy szolgálja az egészsége? Remélem jól.*
- Repetitions decode identically: *hogy* ×6, *szóval* ×2, *remélem* ×2, *jól* ×2, *édesem* ×2, *sírig hü* ×2 (the following word is *kedese* in row 22 and *kedve-* in C4, which are not identical).
- It fits the family: same addressee, same sender name and closing as HCP1216 (Feri, *sírig hű kedvese*).

## Response to review 1

Verdict REVISE. I rechecked every finding on the reviewer's enlargements of `work/hires/*_adr.jpg` (`review/work/crops/r22.png`, `dh.png`, `r3j.png`) and on `work/crops/corner.png`. All nine are accepted; none changes the key.

1. **R22 chevron: fixed.** Panels b and c of `r22.png` show S, three bars, tick + stroke, three bars, bowl, three bars, cross, three bars, F, i. No chevron stands between d and e; I had supplied it from expectation. The ledger token is removed, the literal is now *kedese*, normalized *ked[v]ese*, disclosed as item 16.
2. **Diacritic on u: fixed.** Two dots are clear over the x in R22 (`r22.png` panel b) and C4 (`corner.png`), the same mark as on R11 *ügyet*. Both are token `U`, literal *hü*, normalized *hű*. The `UU` token and the "in the margin" rule are removed from the ledger, `decode.py` and the key section.
3. **R8 *de*: fixed.** `dh.png` shows the R8 sign with its tick to the right, as in R5. I now read both alike as `d?` (literal *de*), offer *ha* as the alternative, and changed the normalized text, English and Slovak. *hogy hogy volna jobb* is no longer smoothed: both translations mark it uncertain, and item 8 gives the alternative constructions. The strict shape reading *he* is recorded in item 9.
4. **R3 j: fixed.** `r3j.png` shows the low-cross variant. Token now `j?`, added to item 5.
5. **C4 d: fixed.** Token now `d?`, disclosed as item 15.
6. **R15: fixed.** Normalized *beszélhete[k] magával* (item 10).
7. **R20: fixed, with one addition.** The final e is bracketed. The card has *egeseg* with a single s, so both the z and the second s are missing; I bracket both, *egés[zs]ég[e]* (item 6).
8. **Source capture: fixed.** The status line now says the claim rests on the catalogue row. I did not re-read the tabs.
9. **Stale claims: fixed.** The `?` count is ten, and the *kedve-* repetition is replaced.

After the fixes `python3 -I ciphers/hcp-1260/work/decode.py` was re-run: 4 hashes OK and the output matches the literal rows above.
