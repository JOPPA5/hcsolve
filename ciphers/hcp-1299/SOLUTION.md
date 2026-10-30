# HCP1299 — Feri to Jolánka Tóth: why my reply seemed late, and how my heart aches

**Status: complete reading, corrected after review 1 (verdict REVISE; see the last section).** One word stays unexplained (*ojot*, row 10); see Uncertainties. By Claude Opus 5.5, 2026-10-30. There is no earlier work on this number. No external plaintext was used: the portal shows *Not solved* and attaches no transcription or solution, and the orchestrator's register check (2026-10-30) found no record of this card.

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented graphic signs: the "Jolánka" postcard family, same key as HCP1216, 1212, 1213, 1217, 1218, 1243, 1301. The key was taken over from those cards and fitted without change; as on the sister cards, *gy* is written as two signs.

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | section mark | k | F-like | r |
| six | b | wave | l | right bowl | s |
| left bowl (only inside cs) | c | three short strokes | m | gamma/corner | t |
| long + short joined | d | two short strokes | n | plain cross | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross | f | tall stroke + separate short (h/p near-homograph) | h / p | low descender | y |
| open loop with descender | g | crossed curve (dot often displaced) | i | crossed diagonal with tail | z |
| inverted T | j | opposed bowls | cs | | |

Dots over o/u give ö/ü. Acute marks and the ő/ű double marks are mostly not distinguishable and are supplied in normalization. q, w, x are unused.

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1299/work/decode.py
```

It checks the SHA-256 of the two source scans and the two un-converted originals, decodes `work/ledger.txt` (776 signs, one token per written sign, one of them an interlinear insertion), prints the literal letters row by row, then the normalized text `work/normalized.txt`. The ledger is a manual transcription from enlarged crops of the original `work/hires/..._adr.jpg` (`work/crop.py` regenerates any crop; a few key crops are in `work/crops/`). It is not OCR, and the reading was not blind: word sense guided segmentation, and the points where it decided a sign are listed below.

## Literal decipherment (as printed by the command)

```
01 szeretetedesjolankamedesegyet     16 vemmikorbecsessoraitel
02 lenremenyemkivanomhogy            17 olvastamcsakeztsajnaltam
03 alegjobbegessegbentalaljaso       18 hogymiert[n]incsitazazan
04 raimsajnalattalveszem[t][u][d]o   19 gyalkaamelikesoroket
05 masulhogyutobbisoraojke           20 irjahogyszivemhezölel
06 sönvalaszoltamvolna               21 hetnemhogyhaderezhetne
07 barenmikormegkaptamrög            22 teljesenboldognakma
08 tönvalaszoltammert                23 gathigyjeeledesemugyfaj
09 azthiszemedesemhogyma             24 aszïvemhogynemletha
10 gaisojotnehezenvarja              25 tomcsakaztszeretnemtud
11 soraimintamijennehe               26 nimedigkelmegazegyütle
12 zenvaromamagabecsesso             27 tünkigazenarvaszivemnekcsodalomedesemhogyojha
13 rai[t]higyjeeledesemszo           28 marbelenyugszikhogyhaegyicsitesetlegkesikalapom
14 valkisemlehetfejezniazt           29 abolkelazt[f]e{l}teteleznihogykönyenefelejtenehaasor
15 azerzesemielfogtaszi              E1 sszetvalasztanabenünket   (up the right edge)
Under the stamp: istenvele | edesem | csokolja | szamta | lanszor | sirig | hukedves | seferi
```

## Hungarian (normalized)

Szeretet[t] édes Jolánkám, édes egyetlen reményem! Kívánom, hogy a legjobb egésségben találja soraim. Sajnálattal veszem tudomásul, hogy utóbbi sora[ira] oly későn válaszoltam volna, bár én, mikor megkaptam, rögtön válaszoltam, mert azt hiszem, édesem, hogy maga is ojot[?] nehezen várja soraim, [m]int a[hogy] milyen nehezen várom a maga becses sorait. Higyje el, édesem, szóval ki sem lehet fejezni azt az érzésem, mi elfogta szívem, mikor becses sorait elolvastam. Csak ezt sajnáltam, hogy miért nincs it[t] az az angyalka, a melyik e sorokat írja, hogy szívemhez ölelhetném, hogy had[d] érezhetné teljesen boldognak magát. Higyje el, édesem, úgy fáj a szívem, hogy nem láthatom. Csak azt szeretném tudni, med[d]ig kel[l] még az együt[t]létünkig az én árva szívemnek. Csodálom, édesem, hogy oj[=oly] hamar belenyugszik, hogy ha egy [k]icsit esetleg késik a lapom, ab[b]ól kel[l] azt [f]eltételezni, hogy kön[n]yen e[l]felejtene, ha a sors szétválasztana ben[n]ünket.

Under the stamp: Isten vele, édesem! Csókolja számtalanszor sírig hű kedvese, Feri.

## English

My beloved sweet Jolánka, my sweet only hope! I wish that my lines may find you in the best of health. I learn with regret that I am supposed to have answered your last lines so late, although when I received them I answered at once, because I believe, darling, that you too wait for my lines as impatiently as I wait for your precious lines. Believe me, darling, words cannot even express the feeling that seized my heart when I had read your precious lines. I regretted only this: why is that little angel who writes these lines not here, so that I could press her to my heart, so that she might feel herself completely happy. Believe me, darling, my heart aches so that I cannot see you. I should only like to know how long my orphaned heart must still wait until we are together. I am surprised, darling, that you so quickly accept that if my card is perhaps a little late, one must conclude from it that [I] would easily forget [you] if fate parted us.

Under the stamp: God be with you, darling! Kisses you countless times your sweetheart, faithful unto the grave, Feri.

## Slovak

Moja milovaná, sladká Jolánka, moja sladká jediná nádej! Želám si, aby Vás moje riadky našli v najlepšom zdraví. S ľútosťou beriem na vedomie, že som vraj na Vaše posledné riadky odpovedal tak neskoro, hoci keď som ich dostal, odpovedal som hneď, lebo si myslím, drahá, že aj Vy tak ťažko čakáte moje riadky, ako ja ťažko čakám Vaše vzácne riadky. Verte mi, drahá, slovami sa ani nedá vyjadriť ten pocit, ktorý mi zovrel srdce, keď som dočítal Vaše vzácne riadky. Ľutoval som len to, prečo tu nie je ten anjelik, ktorý píše tieto riadky, aby som ho mohol pritisnúť k srdcu, aby sa mohol cítiť úplne šťastný. Verte mi, drahá, tak ma bolí srdce, že Vás nemôžem vidieť. Chcel by som len vedieť, ako dlho ešte musí moje osirelé srdce čakať, kým budeme spolu. Čudujem sa, drahá, že sa tak rýchlo zmierujete s tým, že keď môj lístok možno trochu mešká, treba z toho usudzovať, že by som [Vás] ľahko zabudol, keby nás osud rozdelil.

Pod známkou: S Bohom, drahá! Bozkáva Vás nespočetnekrát Váš do hrobu verný milý, Feri.

## Uncertainties

Unresolved or decided by sense:

1. **Row 29 *könyene felejtene*.** The signs are n y e n e f, with no n before the last e, so the written text has no negation. Normalized *könnyen e[l]felejtene*, "would easily forget"; plain *könnyen felejtene* with a stray e is also possible. A negated *könnyen ne* would need a shared n (as in *soraim|int*, row 11) and gives the opposite of the reproach the writer rejects, so it is set aside on sense. The verb is 3rd person, so grammatically it is formal "you" or a slip for 1st-person *felejteném*. The sense favours "I" (he is the late correspondent), and the translations put [I] in brackets, but the card does not settle it.
2. **Rows 27 *oj hamar*.** *oj* is this writer's spelling of *oly* (rows 5 and HCP1216 *ojan*); the word runs over the line end, *oj ha|mar*. The h/p sign is read h. The y of *hogy* before it is a blot whose outline fits y.
3. **Row 10 *ojot*.** Clear signs, odd form: perhaps *oly*/*olyan* ("so"), perhaps *jó* ("quite") with a false start. Left literal; the sense "(so) hard" does not depend on the choice.
4. **Row 5 *sora*.** Literal; normalized *sora[ira]* ("to your lines") is my supply for the verb *válaszoltam*.

Blot restorations, each disclosed in the ledger as `[x]`:

5. **Row 4 *[t][u][d]o*:** three heavily over-inked signs; their outlines (gamma, cross, joined strokes) fit, and only *tudomásul* makes the phrase. **Row 13 *rai[t]*:** a blot with a gamma/F outline. **Row 18 *[n]incs*:** two strokes visible in a blot. **Row 29 *[f]e{l}tételezni*:** the blot hides a single sign completely; the f is supplied by sense only. The l is on the card, a small wave written above the line between e and t as the writer's own insertion; it is marked `{~}` in the ledger.

Shape calls that rest on word sense:

6. **h/p sign:** read p in *kaptam* (row 7) and *lapom* (row 28), h elsewhere. *lapom* ("my card") rests on sense. Also d (joined) vs h (separate) is close in *boldognak* (row 22) and *had* (row 21). **d/n:** *csodálom* (row 27) has the long lower stroke of d; the reading is also what the sentence needs. **o/i:** the o of *csodálom* has its loop filled with ink and no dot of its own (the dot below it belongs to row 28).
7. **a/e (two vs three bars):** several faint signs are hard to count; I read them by sense, for example the last signs of *válaszoltam* (rows 6, 8) and *mert* (row 8). The literal text shows two mismatches I kept: *sorokét* row 19 (normalized sorokat) and *letha-* row 24, a heavily inked sign (láthatom), perhaps a corrected or clogged a. Row 28 *esetleg*: the t's stroke slightly overshoots its bar, close to the f shape; only t makes a word. Row 29 *aból*: two small marks stand over the o, read as the accent (ó).
8. **Row 18 *it*:** the sign before t is the crossed-curve i with an accent tick, not fully distinct from o; *ott* ("there") is possible, and the meaning changes only slightly. **Row 24 *szïvem*:** two dots over the i. **Stamp S1:** the first sign merges with the stamp's frame shadow and is read i from *Isten*.
9. **E1 v of *szétválasztana*:** the chevron is crossed by the flourish of the address handwriting; the s and z before it are clear.

Writer's spellings normalized, none affecting sense: *szeretet* (t single), *sora*, *mijen*, *melik* (ly written j or l), *higyje*, *kel*, *medig*, *együtle*, *aból*, *benünket*, *had*. Shared letter at a word joint: *soraimint* = soraim + mint (row 11). The missing k of *[k]icsit* (row 28) is the writer's omission. Stamp S7–S8 *kedves | se* writes s twice across the line, normalized *kedvese*. Row 21 *érezhetné* is kept 3rd person as written; its subject is the little angel (Jolánka herself), with *magát*. *az az an|gyalka* and *oj ha|mar* are words split over a line end.

The picture side is printed Hungarian and not ciphertext: the caption *Szeretni édes...* and the verse *Óh milyen boldogság / Szeretni, szeretni! / Nem tudnálak soha / Tégedet feledni.* ("Oh what happiness / To love, to love! / I could never / Forget you."). The postmark date is not legible; the cancellation is Rákospalota, and the address is the same as on the sister cards. Plain handwriting beside the postmark is not cipher; it reads tentatively *Szép reményi…*, with the end struck through. Its purpose is unknown. No date is claimed.

## Why it is correct

- The family key, unchanged, turns all 776 signs into Hungarian, with no sign left without a value; outside the items listed above they fall in ordinary Hungarian words. Only *ojot* (row 10) stays unexplained.
- Long unbroken phrases come out without any adjustment: *kívánom hogy a legjobb egésségben találja soraim*, *sajnálattal veszem tudomásul*, *szóval ki sem lehet fejezni*, *úgy fáj a szívem*, *az én árva szívemnek*, *ha a sors szétválasztana bennünket*.
- Repeated items decode identically in different places: *hogy* ×10 or more, *higyje el édesem* ×2, *becses sorait* ×2, *édesem* ×5, *szívem* ×4.
- The opening, closing and sender formulas match HCP1216 and the family: *édes egyetlen reményem*, *Isten vele*, *sírig hű kedvese*, *Feri*; the writer's habits match too (*ojan*-type ly → j, *higyje el* as in HCP1216 *higgyje el*).

## Response to review 1

Verdict REVISE. I checked every finding on the un-converted scan (`work/crops/resp/`, enlarged 2 to 5x) and accept all eight. The key is unchanged; four rows of the ledger changed: five signs replaced and one interlinear sign added. Decoded after the fixes: 776 signs. The command still runs and all four hashes pass.

1. **Accepted, fixed.** Row 27 is *csodálom*: the sign before a has a short upper stroke over a clearly longer lower one, the d form (`z27.png`, also the reviewer's `cmp_x.png`), not the equal strokes of n. The preceding sign has no dot: the two dots below that row sit at x about 1835 and 2000 on the original scan and are the dots of the two i signs of *icsit* in row 28. Ledger `CS Q 4 = ~ Q 3`. Word sense supports the d and the o; the d stroke is also visible in the pixels.
2. **Accepted, fixed.** *oj ha|mar* = *oly hamar*. Only the division changed.
3. **Accepted, fixed.** Row 18 has two bars in both places (`review/work/z_azaz.png`); the vertical at the second is the card's printed divider. *az az an|gyalka*. Ledger `= Z = Z = 2`. "Her" replaces "it" in the English, and the subject of *érezhetné* becomes the angel, not "you".
4. **Accepted, fixed.** Row 29 has n y e n e f (`work/crops/resp/B3.png`, `z28.png`). My "shared n" was an inference that the text does not show, and my claim that it did not affect sense was wrong. Normalized *kön[n]yen e[l]felejtene*; Hungarian, English and Slovak changed. The open question of the verb's person is uncertainty 1.
5. **Accepted, fixed.** The small wave above the line in row 29 is an interlinear l (`review/work/t1.png`). New ledger token `{~}`, and `work/decode.py` prints it as `{l}`.
6. **Accepted, fixed.** Row 21 has three bars after r (`review/work/k21b.png`), the third faint. Literal *derezhetne*. The earlier "776" was one too many against the 775 then printed; the count now printed is 776, with the l added.
7. **Done.** Title line, uncertainties, the *Why it is correct* section, and `work/normalized.txt` updated. I kept the historic dead ends in `NOTES.md` and added a dated correction. *ojot* stays unresolved. Row 24 *letha-* stays as disclosed.
8. **Done.** The plain handwriting (tentative) and the full picture-side verse are recorded above.

The reviewer also asked for a full a/e pass. I went through rows 1 to 29 on enlarged panels (`work/crops/resp/L*.png`, `R*.png`, `B*.png`). It changed no further sign. It added two disclosures in uncertainty 7: the t of *esetleg* (row 28, close to the f shape, read by sense) and the marks over the o of *aból*.
