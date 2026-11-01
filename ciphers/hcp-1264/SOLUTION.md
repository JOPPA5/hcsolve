# HCP1264 — Feri to Jolánka Tóth: "be patient until Thursday"

**Status: complete reading; review 1 verdict REVISE, all findings addressed, no word of the normalized text changed.** Written 2026-11-01 by Claude Opus 5.5. No earlier work exists on this number. The portal shows status *Not solved* and attaches no transcription or solution; no published solution was used. The transcription is my own (none attached). The key is transferred from finished sister cards.

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented graphic signs: the "Jolánka" postcard family, same key as HCP1216 (fullest legend; also 1212, 1213, 1217, 1218, 1243, 1301). No key element was changed and no new sign value was needed. Accents are marks over the base sign.

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | section mark (S) | k | F-like | r |
| six | b | wave | l | hook ")" | s |
| opposed bowls | cs | three strokes | m | gamma | t |
| tick left + long stroke | d | two strokes | n | plain x | u |
| three bars | e | cursive loop (dots = ö) | o | chevron | v |
| upright cross | f | long stroke + tick right | h / p | low descender | y |
| open loop with descender | g | dotted crossed curve | i | crossed diagonal with tail | z |
| inverted T | j | | | | |

"gy" is g + y here. The picture side carries only printed text, unenciphered: *Hogyha szemedbe nézek / Lelked csak nekem virul*, plus the vertical words *beszél suttogva* and *hulló falevél*, and publisher number 2203. The address is in clear: Szépreményű Tóth Jolánka úrleánynak, Jászárokszállás. Two postmarks: GYÖN… over the stamp box, and a fainter, rotated one at upper left showing FEB with a numeral 1 before it (`review/work/crops/pmA.png`). The month February agrees with the "-02-04" in the portal name, but day and year cannot be read on the card and I do not claim a full date.

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1264/work/decode_opus.py
```

It checks the SHA-256 of all four scans, decodes `work/ledger-opus.txt` (one token per written sign, 23 main rows plus 6 rows in the stamp box, 423 written signs plus the two insertion brackets and one line-end dash), prints the literal letters and then the normalized text `work/normalized-opus.txt`. The ledger is a manual transcription from enlarged crops (`work/crops/`), not OCR.

## Literal decipherment (as printed)

```
01 szeretetédesjolan      13 önisbefogjalatni
02 kámkivanomhogya        14 édesemhogyijenhej
03 legjobbkedvebenta      15 zetbe<vagy>nemtehetek
04 laljasoraimszerel      16 roladeeztnemfogja
05 memneharagudjon        17 észrevennirolammajd
06 r[a]mhogynemmehet-     18 senkicsakmagaédesem
07 temletud[a]tomhogy     19 dragacsillagomlegyen
08 csütötökönokvet        20 türelemmeledesem
09 lenlemegyekamulat      21 csütörtökigistenve
10 ságbaigazhogykevés     22 leédesemviszontla
11 ahénzemdemajdsze       23 tasraimadojaferi
12 rényenköltekez{struck e}ve
stamp box: csokol{t?}m szamta lanszor sirihü kedvesse {u/f}eri
```

## Hungarian (normalized)

Szeretet[t] édes Jolánkám! Kívánom, hogy a legjobb kedvében találja soraim. Szerelmem, ne haragudjon rám, hogy nem mehettem le. Tudatom, hogy csütö[r]tökön okvetlen lemegyek a mulatságba. Igaz, hogy kevés a pénzem, de majd szerényen költekezve, Ön is be fogja látni. Édesem, hogy ilyen helyzetbe[n] vagy[ok], nem tehetek róla, de ezt nem fogja észrevenni rólam majd senki, csak maga, édesem. Drága csillagom, legyen türelemmel, édesem, csütörtökig. Isten vele, édesem, [a] viszontlátásra. Imádója Feri.

In the stamp box: Csókol[o]m számtalanszor. Síri[g] hű kedvese, Feri.

## English

My beloved sweet Jolánka! I wish that my lines find you in the very best of spirits. My love, do not be angry with me that I could not come down. I let you know that on Thursday I will definitely come down to the party. True, I have little money, but by spending modestly you too will come to understand. My sweet, that I am in such a position I cannot help, but nobody will notice this about me except you, my sweet. Dear star of mine, be patient, my sweet, until Thursday. God be with you, my sweet, until we meet again. Your adorer, Feri.

In the stamp box: I kiss you countless times. Your sweetheart, faithful unto the grave, Feri.

## Slovak

Moja milovaná sladká Jolánka! Želám si, aby Vás moje riadky zastihli v čo najlepšej nálade. Moja láska, nehnevajte sa na mňa, že som nemohol prísť dolu. Oznamujem Vám, že vo štvrtok určite prídem dolu na zábavu. Pravda, peňazí mám málo, ale budem míňať skromne, aj Vy to uznáte. Drahá, že som v takej situácii, za to nemôžem, ale nikto to na mne nezbadá, iba Vy, drahá. Moja drahá hviezdička, majte trpezlivosť, drahá, do štvrtka. S Bohom, drahá, dovidenia. Váš ctiteľ Feri.

V rámčeku na známku: Bozkávam Vás nespočetnekrát. Váš do hrobu verný milý, Feri.

## Uncertainties (disclosed)

Restorations (the two signs fully hidden by blots; see also item 13 for a partly hidden one):
1. **Row 6 `r[a]m`**: arched top bar is clear, the lower bar is a solid ink blot. a or e both fit the visible strokes; *rám* is the only sense ("ne haragudjon rám").
2. **Row 7 `tud[a]tom`**: the same kind of blot under a top bar; *tudatom* is the only word.

Readings resting on word sense or on a doubtful sign:
3. **Row 15 insertion `<vagy>`** is the weakest point. Above the line, after *zetbe*, stand a caret-like chevron v, a small two-bar a, and two small cramped marks fused to the tops of the following strokes of n, which I read as g and y. v and a are clear; g and y are small and blurred, read from sense. The clause needs a verb; the writer's form is *vagy*, "you are" or a truncated *vagyok*. The surrounding clause (money, "nem tehetek róla", "rólam") makes the first person *vagy[ok]* the better sense, so the English says "I am". If *vagy* is taken literally as "you are", the clause changes meaning, though the writer otherwise uses formal address (*haragudjon, maga, Ön*). Corrected after review: the third mark is only a forked mark on the top of the n stroke, so g rests on sense alone; the fourth has an arm and a loop and is a reasonable small y. Directly after it, on the same level, stands a double blot with a small loop at its left end (`review/work/crops/blob.png`). It may be a plain blot; it also sits where *-ok* would go. It cannot be read as letters and is not counted as evidence for *vagy[ok]*.
4. **Row 12, sign after z**: a vertical stroke crossing three bars. It matches no key sign; I read it as an e struck through by the writer (*költekez(e)ve*). Normalized *költekezve*.
5. **Row 16 `de`**: the d is followed by one extra bold short stroke before the e; treated as a pen slip without letter value (it could also be taken as the tick of an h/p sign, which gives no word).
6. **Row 17 `rólam`**: the m has a short thick third stroke (cf. token `M?` of HCP1216); n would give no word.
7. **Stamp row 1**: between *csokol* and the clear three-stroke m stands a bold stem with a right arm, closest to t, not to o. Literal *csokol{t?}m*. I normalize *Csókol[o]m* by the family formula (HCP1216); *csókol[t]am* "I kissed" with a missing a is the alternative. The k here is joined to the preceding o and is less clean than elsewhere.
8. **Stamp row 4 `sirihü`**: no g sign is on the card; normalized *Síri[g]*. The mark over u appears as two faint marks (ű read in normalization).
9. **Stamp row 5 `kedvesse`**: two s hooks stand side by side, the last e is in a stain. Normalized *kedvese*.
10. **h/p**: *pénzem* (row 11) rests on word sense; every other instance is h. **d/n**: the d of *drága* (row 19), *róla de* and *majd* are told from n by the tick-plus-long form; all fit the sense and none is decisive alone.
11. **Row 8 `csütötökön`**: no r sign is written (row 21 has it). Row 1 `szeretet`: one t only. *ijen/hejzetbe* are the writer's spelling for *ilyen/helyzetbe* (cf. *ojan* on HCP1216). Accents mostly follow sense; those seen are marked in the ledger. *a* before *viszontlátásra* is editorial, not on the card.
12. Whether *mulatságba* with *költekezve, Ön is be fogja látni* means "you will understand" or stands as a loose clause is a matter of punctuation; the punctuation is editorial.
13. **Row 21 *csütörtökig***: the *i* is heavily blotted or overwritten in its upper half and no dot is visible; loop, crossing and right arm allow i but also o, so i rests on sense (*-ig* "until"). The k before it is a small closed 8, unlike the open S of the other k signs (`review/work/crops/k21b.png`).
14. **Stamp row 6, first sign**: a symmetric X of two diagonals, the plain x = u shape, not the upright cross of rows 13, 16 and 23 (`review/work/crops/feri_stamp.png`). Literally *ueri*, printed `{u/f}eri`. *Feri* is a call on word sense: the signature in row 23 is clear, and a careless f is the likely cause.

## Why it is correct

- The key, transferred unchanged from reviewed cards, turns the 423 written signs into running Hungarian. Without a clean letter value: one struck sign, one extra tick, two blots and the X of the stamp signature, all listed above.
- Repeated words decode identically in independent places: *hogy* ×5, *édesem* ×4 (plus *édes* once), *csütörtök-* ×2, *nem* ×3.
- The formulas are those of the family: *Kívánom, hogy a legjobb kedvében találja soraim* (1218), *Isten vele* (1216, 1217), *Imádója* (1301), *számtalanszor … hű kedvese* (1216). The writer's habits (dropped letters, *j* for *ly*) match. HCP1301 also promises he will come down on a later occasion.
- The addressee is Tóth Jolánka, Jászárokszállás, as on the sister cards.

No sister-card wording replaced reading of this card; they only supply the key and the comparison above.

## Response to review 1

Verdict REVISE. I looked at the reviewer's crops for findings 1, 2, 3 and 5 and agree with all five. No word of the normalized text changed, so this goes to FINAL without another round.

1. **Stamp signature (major): fixed.** The crop shows a symmetric X, not the upright cross. `work/ledger-opus.txt` now has token `X?`, `work/decode_opus.py` prints `{u/f}eri`, the literal table is updated, the sign is uncertainty 14, and *Feri* is out of the repeated-words evidence. *Feri* stays in the normalized text as a call on word sense.
2. **Ink mark after row 15 insertion (minor): fixed.** Added to uncertainty 3 as possible but unreadable. That item also now says that g rests on sense alone.
3. **Row 21 i and k (minor): fixed.** Added as uncertainty 13, and the "Restorations" heading is softened.
4. **Counts (minor): fixed.** *hogy* ×5, *édesem* ×4 plus *édes* once, 423 signs. The script now counts signs and leaves out `<`, `>` and `-`.
5. **Postmark (minor): fixed.** The second postmark with FEB and a numeral 1 is recorded. Portal name element "-02-04" noted as agreeing on the month. No full date claimed.

Re-run after the fixes: `python3 -I ciphers/hcp-1264/work/decode_opus.py` passes all four hash checks, prints 23 + 6 rows with only stamp row 6 changed (`{u/f}eri`), reports 423 signs, and prints the unchanged normalized text.
