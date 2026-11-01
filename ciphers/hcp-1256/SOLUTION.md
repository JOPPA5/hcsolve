# HCP1256 — Feri to Jolánka Tóth: lonely in Pest, a photograph promised, home for St Stephen's Day

**Status: complete reading of the message; one short stretch of the sign-off before "imádója" (one word or a short phrase, about ten signs) is read literally but not understood. Review 1 (REVISE) addressed; see the last section.** Claude Opus 5.5, 2026-11-01.

Credit: solved by Claude Opus 5.5 with the Jolánka-family key taken from the finished cards (hcp-1216 and siblings). No earlier work exists on this number. The portal shows *Not solved*, with no transcription or solution attached; I met no published solution of this card.

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented graphic signs (Jolánka family), the key and sign classes of HCP1216 unchanged; this card's text confirms them. Sign classes: two bars a; six b; left bowl c; long + short tick d; three bars e; upright cross f; open loop with descender g; tall stroke + short tick h/p; dotted crossed curve i; inverted T j; section mark k; wave l; three short strokes m; two short strokes n; cursive loop o; F-shape r; right bowl s; corner t; plain cross u; chevron v; low descender y; crossed diagonal z. The digraphs have no sign of their own on this card: gy is written as two separate signs, g + y, and cs as left bowl + right bowl, i.e. c + s. Dots over o/u give ö/ü; acute marks are supplied in normalization.

Observations on this hand: a corner t may be written in two pen lifts (row 21 *tudom*); the k appears both as a large section mark and as a small "5"; the d is often short tick + long stroke.

The red word **Szépremény** at the top of the address side is unenciphered ("fair hope"), as are the address (*Tóth Jolánka úrleánynak szeretettel, Jász-Árokszállás*; *szeretettel*, "with love", is partly under the collection stamp) and the printed verse on the picture side (*Aranyeső*, "Huzok az ujjadra aranyos karikagyűrűt"). No cipher on the picture side.

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1256/work/decode_opus.py
```

It checks the SHA-256 of the four image files, decodes `work/ledger-opus.txt` (one token per written sign, 25 main rows plus 8 rows on the stamp area, revised after review 1) with the key, prints the literal rows, then prints the normalized text `work/normalized-opus.txt`. The ledger is a manual transcription from the un-converted scan in `work/hires/`, not OCR. Crops used are in `work/crops/` and `work/crops2/`; scripts `work/crop*.py`.

## Literal decipherment (as printed by the command)

```
01 szeretetedesjolankam                 14 ojanbaratranincsszük
02 kivanomhogyalegjobb                  15 segemvoltamsandor
03 kedvebentalaljasoraim                16 nalfeloraigbeszegett
04 hogymulatotvasarnah                  17 veleaztlehetmondani
05 jobbanmintenmertenmar                18 hogyminderölbeszelunk
06 egeszelarvulokebeahast               19 aztismontahogymiertnem
07 bemertegyetlenszora                  20 megyekgyakrabbanhozza
08 koztatomtolismegvagyok               21 herszeenaztmondtamugyistudomhogynemerrabeszel
09 fosztvaamenyibefagerjoska            22 getniedesemakerfenykehetjövöhetenmekküldömva
10 hazamentesmostnincssenkim            23 sarnahfogomlevetetnimagamszombatonvettemruhatiscsak
11 barjobaratotkönyensze                24 kolgozhassakakormajdcsakrendbejövökistvankirajra
12 rezhetekcsakhogyhezbe                25 szandekozokhazamennihavalamiközbenemjön
13 kerülesnekemmostmar
stamp area: [i][s][t]enve / leedesem / aboldog / viszot / lat{a/e}sig / {?}arsoka / {-}eszimado / jaferi
```

(h stands for the h/p sign. Rows 21–25 run the full width of the card under the address.)

## Hungarian (normalized)

Szeretett édes Jolánkám! Kívánom, hogy a legjobb kedvében találja soraim. Hogy mulatott vasárnap? Jobban, mint én, mert én már egész elárvulok ebbe a Pestbe, mert egyetlen szórakoztatómtól is meg vagyok fosztva, amennyiben Fáger Jóska hazament, és most nincs senkim. Bár jó barátot könnyen szerezhetek, csakhogy pé[n]zbe kerül, és nekem most már olyan barátra nincs szükségem. Voltam Sándornál, fél óráig beszé[l]gett[ünk]. Vele azt lehet mondani, hogy minde[n]ről beszélünk. Azt is mon[d]ta, hogy miért nem megyek gyakrabban hozzá. Persze én azt mondtam, úgyis tudom, hogy nem ér rá beszélgetni. Édesem, a kér[t] fényképet jövő héten megküldöm; vasárnap fogom levetetni magam. Szombaton vettem ruhát is. Csak dolgozhassak, akkor majd csak rendbe jövök. István királyra szándékozok hazamenni, ha valami közbe nem jön.

Under the stamp: [Ist]en vele, édesem, a boldog viszo[n]tlátásig. {?arsoka[?]ész} imádója Feri.

## English

My beloved sweet Jolánka! I wish that my lines may find you in the best of moods. How did you enjoy yourself on Sunday? Better than I did, for I am growing quite orphaned in this Pest, since I have been deprived even of my only entertainer: Jóska Fáger has gone home, and now I have nobody. True, I could easily get a good friend, only that costs money, and I have no need of that sort of friend any more. I was at Sándor's; we talked for half an hour. With him one can say that we talk about everything. He also asked why I do not go to see him more often. Of course I said that I know anyway that he has no time for chatting. Darling, the photograph you asked for I will send next week; on Sunday I am going to have my picture taken. On Saturday I also bought clothes. If only I can work, then I shall get back on my feet in the end. For King Stephen's Day [20 August] I intend to go home, if nothing comes up.

Under the stamp: God be with you, darling, until the happy reunion. [? unread word or phrase] your admirer, Feri.

## Slovak

Moja milovaná sladká Jolánka! Želám si, aby Vás moje riadky zastihli v najlepšej nálade. Ako ste sa zabavili v nedeľu? Lepšie než ja, lebo ja už celkom osirievam v tejto Pešti, keďže som prišiel aj o svojho jediného zabávača: Jóska Fáger odišiel domov a teraz nemám nikoho. Dobrého priateľa si síce ľahko zaobstarám, lenže to stojí peniaze a takého priateľa už teraz nepotrebujem. Bol som u Šándora, pol hodiny sme sa rozprávali. S ním sa dá povedať, že sa rozprávame o všetkom. Spýtal sa aj, prečo k nemu nechodím častejšie. Pravdaže, ja som povedal, že aj tak viem, že nemá čas na rozprávanie. Drahá, fotografiu, o ktorú ste žiadali, Vám budúci týždeň pošlem; v nedeľu sa dám odfotografovať. V sobotu som si kúpil aj šaty. Len nech môžem pracovať, potom sa nakoniec dám do poriadku. Na Štefana kráľa [20. augusta] mám v úmysle ísť domov, ak do toho niečo nepríde.

Pod známkou: S Bohom, drahá, do šťastného zvidenia. [? neprečítané slovo alebo slovné spojenie] Váš ctiteľ Feri.

## Uncertainties

1. **Sign-off, one unresolved word or short phrase (rows S6–S7).** Literal: `{?}arsoka`, then a bar of a hidden sign, then `esz` before *imádója*. The stretch spans about ten signs across a stamp fragment, so it may be one word or two. The first sign of S6 (stroke + low bowl, touching the stamp remnant, possibly a damaged b) and the sign whose bar shows at the start of S7 are not settled; that second sign lies under the green stamp fragment. *imádója Feri* (S7–S8) reads. I do not offer a guess as a reading.
2. **Row 24 first sign.** *dolgozhassak* begins with a small "5", the writer's small k, not a d; literal `kolgozhassak`. *dolgoz-* is chosen on word sense (a slip of the pen, or a poorly formed d).
3. **Restoration, row S1.** *Ist-* is under a flap of the stamp remnant: only red fragments show. *Isten vele* is restored from the visible `en ve | le` and the family's formula (HCP1216).
4. **Letters the writer omitted, supplied in brackets:** row 12 *pé[n]zbe*; row 19 *mon[d]ta* (written `monta`: only two equal strokes stand between o and t, whereas row 21 *mondtam* has n and d); row 22 *a kér[t] fényképet* (written `aker`, with an accent tick over the e); row S4 *viszo[n]tlátásig* (written `viszot`: no strokes between o and t); row 16, see item 9. The sense does not depend on any of them except row 22: there the t is supplied because *a kért* ("the requested") fits the sentence and the written é excludes *akár*.
5. **Row S5 a or e.** *látásig* has `lat{a/e}sig`: only two bars show attached after the arm of the t, and a third could be merged with the arm's end (`work/crops2/s5.png`). The sign is left open in the ledger; the word is not in doubt.
6. **Row 22 *héten*:** the second stroke of n is covered by a red blot; the first stroke and the word fix it. Same row: the p of *fényképet* is written with short tick + long stroke (the d shape).
7. **h/p and d/n by word sense.** The h/p sign is read p in *vasárnap* (rows 4, 22–23), *Pest*, *pé[n]zbe*, *persze*, *fényképet*, and h elsewhere. Row 2 *kívánom* has n written as two spaced strokes, close to the h/p sign; *szerezhetek* h; *dolgozhassak* h.
8. **Row 6 *Pestbe*:** literal `hast|be`, with two crisp, widely separated bars, i.e. a clear a. *Pest* is therefore an emendation of the vowel (the writer would have meant e), resting on sense: *ebbe a* (literal `ebe a`) requires a place and the city fits a Budapest-area writer (HCP1216 has a Rákospalota cancellation). Other a/e calls with crowded bars (row 15 *ség*, row 13 *kerül*) rest on word sense as well.
9. **Row 16 `beszegett`:** no l written, and a period follows it. *-ünk* is supplied in the normalization on the evidence of row 18 *beszélünk*; the pink overpainting under the g might hide an l.
10. **Row 18 *beszélünk*:** the sign after *beszél* is an F overwritten by a heavy cross, then n k. I read the writer's correction to u(ü); no dots are visible. Row 19 *miért*: the i is also an overwritten sign with its dot. Row 8: the v of *vagyok* is overwritten by a cross stroke but the chevron is plain. Row 17 *azt*: the t sits in a stain but is visible.
11. **Row 18 `minderöl`.** Preferred: *minde[n]ről* ("about everything"), with n omitted as in `pézbe` and `viszot`. Alternative: *mind erről* ("all about this"), which needs no supplied letter, but *erről* has no antecedent in the letter. This is a word-sense call.
12. **Name *Fáger Jóska*** is read from the signs (f a g e r); I could not verify the family name, and the e carries a tick, so *Fágér* is possible. Row 22 `mek` for *meg-* is the small k sign (assimilation, or the g/k similarity).
13. Other writer spellings normalized: *szeretet* → szeretett, *mulatot* → mulatott, *amenyibe* → amennyiben, *könyen* → könnyen, *ojan* → olyan, *kirájra* → királyra, *akor* → akkor.
14. The date is not established. The inverted cancellation is partly visible beside the stamp but I could not read it reliably. "Szépremény" is left as a plain-text motto; it may be a name or place.

## Why it is correct

- The HCP1216 key, unchanged, turns every sign of all 25 main rows into running Hungarian. It was applied to the card, not fitted to it; the unusual multi-word sequences (*szórakoztatómtól is meg vagyok fosztva*, *fényképet … levetetni magam*, *István királyra szándékozok hazamenni*) cannot arise by chance.
- Repeated words decode identically (*hogy* ×6, *csak*, *most*, *mondta/mondtam*, *barát-*, *vasárnap* ×2, *jövő/jövök*).
- The closing formula, the signature Feri, the mention of Sándor (also on HCP1216 and HCP1217) and the formal *Ön* address (*mulatott, találja*) all fit the family.

## Response to review 1

Verdict REVISE. I rechecked every finding on the reviewer's crops and on my own (`work/crop7.py`, `work/crops2/`). All eleven are accepted, finding 7 with the sign left open. After the changes the reviewer's `review/work/my_decode.py`, run against the new literal output (in a scratch copy, nothing written to `review/`), differs in one row only: S5, the sign finding 7 asks to leave open.

1. **Row 22 *a kér[t] fényképet*: fixed.** The accent tick stands over the e (`review/work/T2.png`), so *akár* is excluded. Normalization, English, Slovak and the spelling list changed; the supplied t is disclosed (uncertainty 4).
2. **Row 24 `akor`: fixed.** The second sign is the S-shaped k, identical to the last sign of *hassak* just before it (`review/work/z24.png`). Ledger changed from `)` to `K`; the old uncertainty and the `{a sor / akkor?}` hedge are gone.
3. **Rows 19 and S4: fixed.** `z19.png` shows two equal strokes between o and t, so `monta`. `zs4.png` shows nothing between o and t, so `viszot`. The tokens D and N are removed from the ledger; *mon[d]ta* and *viszo[n]tlátásig* are bracketed in the normalization (uncertainty 4).
4. **Row 21 `herszeen`: fixed.** Two separate three-bar signs stand after z (`z21.png`). The clause is *Persze én azt mondtam*. Ledger, normalization and both translations changed.
5. **S1 last sign e: fixed.** Three widely spaced bars (`zs1.png`). The literal is `…enve | le`; the claim of a writer's spelling *va* is withdrawn.
6. **Row 18: fixed.** *minde[n]ről* is now preferred and *mind erről* is disclosed as the alternative (uncertainty 11). English and Slovak changed.
7. **S5: fixed by leaving it open.** On `work/crops2/s5.png` two bars are visible, and the end of the t's arm could hide a third, so neither a nor e can be asserted. The ledger has the token `A/E`; the writer's-spelling claim is withdrawn (uncertainty 5).
8. **Row 6: fixed.** Bars confirmed crisp on `z6.png`. Uncertainty 8 now says plainly that *Pest* emends a clear a on sense.
9. **Address: fixed.** *szeretettel* is visible on `addr.png` and is now given.
10. **gy and cs: fixed.** gy is two signs and cs is left bowl + right bowl (`work/crops2/cs.png`). The ledger now has tokens `G Y` and `C )`, and the key description is corrected; the decoder no longer has digraph entries. The literal output of these words is unchanged.
11. **Sign-off: fixed.** The status line and uncertainty 1 now say "one word or short phrase". I could not read it either.

Also corrected, not raised in the review: the bracket in row 16 now follows the written `-gett` (*beszé[l]gett[ünk]*). The command `python3 -I ciphers/hcp-1256/work/decode_opus.py` was re-run after all changes: four hashes OK, output as printed above.
