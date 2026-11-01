# HCP1253 — Feri to Jolánka Tóth: looking for work "down there", not at home

**Status: complete reading, small disclosed points only; review 1 (REVISE) addressed, see the last section.** Written 2026-11-01 by Claude Opus 5.5 (solver). There is no earlier work on this number. No published solution was found: the portal shows status *Not solved* and attaches no transcription or solution. The key comes from the finished Jolánka family cards; no plaintext of this card was available.

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented graphic signs (MASC): the "Jolánka" postcard family. The key was transferred unchanged from HCP1216 (also 1262 for the sign descriptions). This card adds two variants not in the sister key tables I searched: the left bowl used for s (item 8) and left bowl + stroke for cs (item 7). A third form, the h/p shape used for d, is a near-homograph already noted on HCP1216 (row 5), 1247 and 1255.

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | section mark S (or 8) | k | F-like | r |
| six | b | wave | l | right bowl; on this card also left bowl | s |
| opposed bowls; on this card also left bowl + stroke | cs | three short strokes | m | gamma/corner | t |
| tick on the left + long stroke | d | two short strokes | n | plain cross x | u |
| three bars | e | cursive loop (undotted) | o | chevron | v |
| upright cross + | f | tall stroke + tick on the right | h / p (rarely d, by word sense) | crossed diagonal | z |
| open loop with descender | g | dotted crossed curve (same loop with a dot) | i | low-crossed T | j |
| g + low descender | gy | | | | |

Marks: dots over the loop give ö, two ticks give ő, dots on the cross give ü, a tick gives an acute. Most acutes are not written or not visible and are supplied in normalization. Only marks actually seen are in the ledger.

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1253/work/decode.py
```

It checks the SHA-256 of all four image files, decodes the sign ledger `work/ledger.txt` (one token per written sign, 20 main rows plus 7 rows in the stamp box) and prints the literal letters and then the normalized text `work/normalized.txt`. The ledger is a manual transcription from enlarged crops of the un-converted scan in `work/hires/`; none is attached on the portal. `work/crop.py`, `strip.py` and `low.py` rebuild the crops in `work/crops/`. The picture side has no handwriting, only the printed series number 3601/02.

## Literal decipherment (as printed by the command)

`{}` marks a call on an unclear sign, `[]` a restoration.

```
01 sszeretetédesjolánkám          15 lentszeretnékdolgoz
02 kivanomhogyjoegeszég           16 niésmarkezdődia
03 bentaláljasoraim               17 munkaesithonnem
04 hogymulatnakoda                18 akarokdolgozni
05 hazaremélemjol                 19 masujsagitnincsugyanézis
06 bejönhéntekenva                20 régiistenveédesem
07 romhanemjönleéde               S1 [cs]okolom
08 semésírjameghale               S2 szamtalan
09 kellenevinnvala                S3 szorima
10 mitszivesenle                  S4 {d}o{j|t}aés
11 viszemitnincs                  S5 irighü
12 semiujsagmunkam                S6 kedvese
13 nincsamit{n}emisna             S7 fer{i}
14 gyokeresekmertcsak
```

## Hungarian (normalized)

Szeretett édes Jolánkám! Kívánom, hogy jó egészségben találja soraim. Hogy mulatnak oda haza? Remélem, jól bejön pénteken, várom. Ha nem jön le, édesem, és írja meg, ha le kellene vinni valamit, mit szívesen leviszem. Itt nincs semmi újság, munkám nincs, amit nem is nagyon keresek, mert csak lent szeretnék dolgozni, és már kezdődik a munka, és itthon nem akarok dolgozni. Más újság itt nincs, ugyanez is régi. Isten ve[le], édesem.

Stamp box: [Cs]ókolom számtalanszor. Imádója és sírig hű kedvese, Feri.

## English

Beloved sweet Jolánka! I wish that my lines may find you in good health. How are you all enjoying yourselves at home? I hope you will come in safely on Friday; I am waiting for you. If you are not coming down, my sweet, then write and tell me whether anything should be taken down, which I will gladly take. There is no news here. I have no work, and I am not looking very hard for any, because I would only like to work down there; the work is already starting, and I do not want to work at home. There is no other news here, and even this is old. Farewell, my sweet.

Stamp box: I kiss you countless times. Your adorer and sweetheart faithful unto the grave, Feri.

## Slovak

Milovaná sladká Jolánka! Želám si, aby Vás moje riadky našli v dobrom zdraví. Ako sa zabávate doma? Dúfam, že v piatok dobre prídete, čakám Vás. Ak neprídete dolu, drahá, napíšte mi, či by bolo treba niečo zaniesť dolu, rád to zaveziem. Tu nie je nič nové. Prácu nemám a ani ju veľmi nehľadám, lebo by som chcel pracovať len tam dolu; práca sa už začína a doma pracovať nechcem. Inej novinky tu niet, aj táto je stará. Zbohom, drahá.

V rámčeku známky: Bozkávam Vás nespočetnekrát. Váš zbožňovateľ a do hrobu verný milý, Feri.

## Uncertainties

Restoration:

1. **S1, *[cs]ókolom***: the first position is a heavy blot at the edge of the stamp residue. Only one thick stroke survives, so *cs* is a restoration; *o k o l o m* is clean, and *csókolom* opens the box on sister cards (HCP1216, 1262 family).

Calls that rest on word sense, not on a clean shape:

2. **Row 13, the sign before *em***: two strokes crossed by two bars, an overwritten sign (`#` in the ledger). Read n, giving *nem*. The t before it is also overwritten, with a thin extra stroke.
3. **S4 *{d}o{j|t}a***: the first sign has its tick on the right, the h/p shape, and is read d as in HCP1216 row 5, because *imádója* needs d. The next sign is an undotted loop with a crossing tail, the o of S1 and S3, while the i of S3 and S5 carries its dot; no sign is dropped. The heavy third sign is an inverted T and a gamma superimposed, so the writer corrected one to the other; j gives *imádója*, and the alternative t gives no word. *Imádója* is the closing word of the family (HCP1250, 1251, 1257, 1301).
4. **S4–S5, *és sírig***: the written signs are *é s i r i g*, one s shared by *és* and *sírig*. The normalization supplies the second s.
5. **Row 6 *héntek***: the sign is the h/p near-homograph, read p for *pénteken*. Likewise h in *hanem*, *hogy*, *meg ha*, *itthon*, *hű*, all by word sense.
6. **S6 *kedvese***: the d here is two longish strokes, so close to n; *kenvese* is no word. The d/n call rests on word sense. The final sign of S7 is an undotted loop, the same shape as the o of S1 and S4, so literally *fero*; *Feri* rests on word sense and the family signature. Undotted o and i are therefore not separated by shape at that one spot.
7. **Rows 11 and 19, *cs* of *nincs***: left bowl + stroke instead of opposed bowls, a variant of this card; I found it in no sister key table. Row 19 is closer to "six + stroke" than the row 11 form. The final s of *is* in row 19 is retouched with heavy ink. Both by word sense.
8. **Left bowl as s**: in rows 12 (*semmi*) and 15 (*szeretnék*) a left bowl stands where only s makes sense, although the family assigns it c. Row 1 opens left bowl + right bowl + z: *cs* gives no word, so this is read as a corrected false start for *sz*; the literal doubled s is not meaningful.

Spelling normalized (nothing below is hidden; the signs simply are not on the card):

9. *szeretet* → szeretett; *egeszég-ben* → egészségben (the writer has one s; the g and the acute on é are on the card, row 2 past the printed divider); *semi* → semmi; *itnincs*, *ithon* → itt nincs, itthon; *ugyanéz* → ugyanez; *vinn* → vinni (final i not written); *nagyo* → nagyon (n omitted); *kezdődi a* → kezdődik a (k omitted).
10. **Row 20 *Isten ve[le]***: the signs read *v e é d e s e m*; *le* is not on the card and no sign is hidden there. Writer's omission, supplied in brackets. Sister cards have *Isten vele*.

Interpretation, not affecting the letters:

11. **Rows 5–8**: word division here is editorial. *jól* may go with *remélem, jól [van]* ("I hope you are well", then a new sentence *Bejön pénteken?*) or, as printed, with *bejön*. Likewise *hanem jön le* could be *ha nem jön le* (printed) or *hanem jön le* ("but do come down"); the following *és* fits the second somewhat better, while *ha* fits the rest of the plan. The translation gives one choice and these are the alternatives.
12. **The meaning of *le*, *lent* and *bejön***: it is not settled what place "down there" or "in" means. The card does not name one.
13. **Row 19 *ugyanéz is régi***: printed as *ugyanez is régi*, "even this is old". *Ugyan ez is régi*, "though this too is old", is equally possible.
14. **Row 11, stray mark**: a heavy tick stands on the baseline after the m of *viszem*. See the response to finding 4. It carries no letter.
15. The cancellation is only partly legible (*GYÖ…*, *913 F…*, a second strike with *…ÁROKSZ…* and *22*); the date 1913-02-22 comes from the portal file name. The handwritten address, not enciphered, reads *Szépreményű Tóth Jolánka úrleánynak, Jászárokszállás*; the first word is overlapped by postmarks.

## Why it is correct

- The key was transferred unchanged and gives continuous Hungarian across all 20 rows and the 7 box rows. Every sign has a value. Two variants extend the table: left bowl = s (item 8, three positions) and left bowl + stroke = cs (item 7, two positions).
- Long unforced stretches decode cleanly: *hogy mulatnak oda haza*, *írja meg ha le kellene vinni valamit*, *szívesen leviszem*, *mert csak lent szeretnék dolgozni*, *itthon nem akarok dolgozni*, *más újság itt nincs*.
- Repeated words decode identically: *nincs* (rows 11, 13, 19), *dolgoz-* (rows 15–16, 18), *munka* (rows 12, 17), *újság* (rows 12, 19), *le* (rows 7, 8, 10).
- The content and the closings (*Isten vele*, *édesem*, *csókolom számtalanszor*, *sírig hű kedvese*, *Feri*) match the family, and the recipient on the card is Tóth Jolánka.

## Response to review 1

Verdict REVISE. I re-read each place on the reviewer's crops (`review/work/crops/eg1.png`, `s1.png`, `s3s5.png`, `s7.png`, `b3.png`) and on my own crop `work/crops/r11tick.png` (made by `work/r11tick.py`).

1. **Row 2, sign missed: fixed.** Past the printed divider there is a black open loop with descender, in the writer's ink, matching the g earlier in the same row; the grey ring behind it is the postmark. A tick stands above the last e. Ledger row 02 now ends `E:acute G`; literal *joegeszég*, row 3 *ben*. My "sé-g are not written" was wrong; item 9 is rewritten. The normalized word stays *egészségben*.
2. **S4, *imádója*: fixed.** The second sign of S4 is the undotted loop of S1's o, not an i. Ledger `I` → `O`, literal *{d}o{j|t}a és*, normalized *Imádója és sírig hű kedvese, Feri*, translations changed and item 3 rewritten. My claims that *imádja* was the only sense and that sisters close with it were wrong. I checked the closing on HCP1250, 1251 and 1257 (*imádója*), and it also pairs properly with *kedvese*.
3. **S7 and o/i: fixed.** Item 6 now says the last sign of *Feri* is literally o. The ledger token is `I?` and the literal shows *fer{i}*.
4. **Row 11 stray mark: disclosed, but I disagree with the explanation.** The tick is real. It lies on the baseline right after the m, below and left of the following loop, while a separate dot stands above that loop in `b3.png`, in the normal position for an i dot. So it is probably not the displaced dot. A comma after *viszem* (row 11, the end of *leviszem*) fits it better, as the sentence ends there. No letter depends on it (item 14).
5. **"Only item 8 extends the key": fixed.** The key note, items 7 and 8 and "Why it is correct" now list both variants. Left bowl + stroke = cs appears in no sister key table I searched, so it is stated as a variant of this card. The h/p-shaped d is listed as the near-homograph known from HCP1216 row 5, 1247 and 1255.
6. **ugyanéz is régi: fixed.** Added as item 13. The later items were renumbered.

The reproduction command was re-run after the changes: all four hashes OK and the output matches the literal block and the Hungarian above. The body of the letter did not change in sense; the closing changed by one word.

