# HCP1224 — Feri to Jolánka Tóth: wages, the coming winter, and a heart "pining in the distance"

**Status: complete reading, review 1 (REVISE) addressed.** Claude Opus 5.5, 2026-11-02. No earlier work exists on this number. The portal shows status Not solved and attaches no transcription or solution; no published solution was found. The key is not new: it is the Jolánka family key established by the OpenAI GPT solver and Claude Opus 5.5 on the finished cards listed below.

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented graphic signs (Jolánka postcard family). Key transferred unchanged from HCP1216 (same table on HCP1212, 1213, 1217, 1218, 1243, 1301). The address side (Szépreményű Tóth Jolánka úrleánynak, Jász-Árokszállás) is in clear. The picture side has no writing.

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | section mark / s-shape | k | F-like | r |
| six | b | wave | l | right bowl | s |
| opposed bowls | cs | three short strokes | m | gamma | t |
| long + short stroke | d | two short strokes | n | plain cross x | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross | f | tall stroke + short | h / p (here also d) | low descender | y |
| open loop with descender | g | dotted crossed curve | i | crossed diagonal with tail | z |
| inverted T | j | joined loop + descender | gy | | |

Marks over o/u give ö/ő, ü/ű. sz = s + z, zs = z + s. In row 11 "43 fil" and the k after it are written in clear.

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1224/work/decode.py
```

It checks the SHA-256 of all four scans, decodes `work/ledger.txt` (572 tokens: 26 main rows, the last running along the bottom edge to the right corner, plus 7 rows under the stamp) and prints the literal letters and `work/normalized.txt`. The ledger is a manual transcription from enlarged crops of the hires address scan; the computer decodes it, it does not read pixels.

## Literal decipherment

```
01 kedvesjolankambecses          14 abajhogyjönateles
02 soraitmegkaptammely           15 ijenkorkevesamunka
03 etnagyonköszönökami           16 demajdcsakkitelelekva
04 amjobanletünkharajtam         17 lahogykedvesemolvassa
05 fügnemvalunkelsohaede         18 csakelharmadiklapomat
06 semanakhogyjobeitmint         19 marabairtamhogyjozsi
07 gyöngyösönaznekemmin          20 ekaltöltötotemavasarnapot
08 degyvolnacsakakazfaj          21 mostvasarnap{#}emvoltam
09 hogyjolankamolytavol          22 seholköszonomaversetha
10 vantölemamiafize              23 szivbölirtaaszivemmarreg
11 testiletiit[43 fil k]e        24 azöneedesemhogygondol
12 resektöbetnapontamint         25 hatojathogylapjatmutoga
13 gyöngyösöndecsakaz            26 tomvalkinekjoeg{o|i?}segetkivanokistenvaleedesemf
stamp: gondolj / nehaata / volban / epedö / szivre / hüima / dodferi
```

## Hungarian (normalized)

Kedves Jolánkám! Becses soráit megkaptam, melyet nagyon köszönök. A mi ám jóban lettünk, ha rajtam függ, nem válunk el soha, édesem. Annak, hogy jobb-e itt, mint Gyöngyösön, az nékem mindegy volna, csak az fáj, hogy Jolánkám oly távol van tőlem. Ami a fizetést illeti, itt 43 fil. keresek többet naponta, mint Gyöngyösön, de csak az a baj, hogy jön a tél, és ilyenkor kevés a munka, de majd csak kitelelek valahogy. Kedvesem, olvassa csak el harmadik lapomat, már abba írtam, hogy Józsiékkal töltöttem a vasárnapot. Most vasárnap nem voltam sehol. Köszönöm a verset, ha szívből írta, a szívem már rég az öné. Édesem, hogy gondolhat olyat, hogy lapját mutogatom valakinek? Jó egészséget kívánok, Isten vele, édesem. [f]

Under the stamp: Gondolj néha a távolban epedő szívre. Hű imádód Feri.

## English

Dear Jolánka! I have received your esteemed lines, for which I thank you very much. We have become close, you know, and if it depends on me we shall never part, my sweet. Whether it is better here than in Gyöngyös would be all the same to me; it only hurts that my Jolánka is so far from me. As for the pay, here I earn 43 fillér more per day than in Gyöngyös, but the only trouble is that winter is coming, and at this time there is little work, but I shall get through the winter somehow. My darling, do read my third card; I already wrote in it that I spent Sunday with Józsi and his family. This Sunday I went nowhere. Thank you for the verse, if you wrote it from the heart; my heart has long been yours. My sweet, how can you think such a thing, that I show your card to anyone? I wish you good health; God be with you, my sweet. [f]

Under the stamp: Think sometimes of the heart pining in the distance. Your faithful adorer, Feri.

## Slovak

Milá Jolánka! Vaše vzácne riadky som dostal, za ktoré veľmi ďakujem. Veď sme sa zblížili, a ak to bude závisieť odo mňa, nikdy sa nerozídeme, moja sladká. Či je tu lepšie ako v Gyöngyösi, to by mi bolo jedno, bolí ma len to, že moja Jolánka je odo mňa taká ďaleko. Čo sa týka platu, tu zarobím denne o 43 fillérov viac ako v Gyöngyösi, ale problém je len v tom, že prichádza zima a v tomto čase je málo práce, ale nejako tú zimu prečkám. Moja drahá, prečítajte si moju tretiu pohľadnicu, už som v nej písal, že som nedeľu strávil s Józsim a jeho rodinou. Túto nedeľu som nebol nikde. Ďakujem za verš, ak ste ho písali zo srdca; moje srdce je už dávno Vaše. Moja sladká, ako si môžete myslieť niečo také, že Vašu pohľadnicu niekomu ukazujem? Prajem Vám dobré zdravie, s Bohom, moja sladká. [f]

Pod známkou: Mysli niekedy na srdce túžiace v diaľke. Tvoj verný ctiteľ Feri.

## Uncertainties

1. **Rows 3–4, "a mi ám jóban lettünk".** All signs are clear but one: the row-3 end (`...köszönök|ami`) and row-4 start (`amjoban`) give *ami am joban*. I divide this as *a mi ám jóban*, "we, you know, on good terms", taking ám as the emphatic particle. The division and the sense are an editorial interpretation; the sentence start *A mi* is awkward. The last sign of row 3 is the crossed curve with no visible dot. Single b also allows *jobban* ("more/better"), which reads worse. The two blotted bar signs (row 2 *megkaptam*, row 4 *jóban*) keep an upper bar and a blot, read a by word sense.
2. **Row 8, "csakakaz".** Literal c-s-a-k-a-k-a-z, with two clear k-shaped signs, normalized *csak az* as a repeated syllable. Row 13 writes *csakaz* without the repeat. Nothing else gives a word here.
3. **Row 20, "töltötotem".** Literal t-ö-l-t-ö-t-o-t-e-m, one syllable too many, normalized *töltöttem*. Row 26 has two more slips of the same kind: *valkinek* (a colloquial contraction, normalized *valakinek*) and *vale* (two bars, normalized *vele*).
4. **Row 21, struck sign.** After *vasárnap* a two-stroke sign is crossed with two bars (`{#}`), then three bars and m, so the literal is {#}-e-m. The word is plainly a corrected *nem*; only the struck n is a sense call. The first pass counted two bars, wrongly.
5. **End of row 26.** After *édesem* a final + sign with a long bar sits at the corner: literally f. It may be an initial for Feri or a flourish; it is left literal as [f]. No clause depends on it.
6. **Stamp row 2.** The last two signs are read t + a (*a tá|volban*). The first is a gamma with the two a bars beside it, so the reading is well supported, and *távolban epedő szívre* reads perfectly.
7. **h/p/d calls resting on word sense.** All tall-plus-short signs (marked H: in the ledger): p in megkaptam, naponta, lapomat, vasárnapot, vasárnap, lapját, epedő; d in de (row 13), harmadik, édesem (rows 24, 26), gondol (row 24), gondolj, epedő, imádód (twice); h elsewhere (hogy, ha, soha, sehol, néha, hű, gondolhat). Only the d of rows 1, 5, 8 and 16 has the joined 4-like form. Row 18 k of *harmadik* is a heavy blot on a section sign, read by word sense. Row 24 h of *hogy* is heavily blotted, but the tick and the following *ogy* fix it. The stamp row 6 i of *imádód* shows no dot. The row 12 n of *naponta* is a blot with two strokes showing. In rows 19, 20 and 25 the bars after t or j are counted as two, a, where dots from the next row or crowding make the count harder (*írtam*, *vasárnapot*, *lapját*).
8. **Row 26, "egészséget".** The card has e-g, one curved sign, s-e-g-e-t, literal *eg{o|i?}seget*: eight signs after the o of *jó*, not nine. The curved sign has a closed lower loop and a hooked right end, like an undotted o or i, and it is not the crossed z of rows 3, 7, 22, 23. No shape settles its class. Normalized *egészséget* as a word-sense call from the set phrase *jó egészséget kívánok* (HCP1216 spells *egesseges*). The word is safe; the spelling is not. Row 15 *ijenkor* and row 25 *ojat* are the writer's spelling of ilyenkor, olyat (HCP1216 has *ojan*). His single consonants (*letünk, füg, abba* as *aba*, *többet* as *töbet*, *kitelelek*) are normalized. In row 15 the j is overwritten by a blot, but the inverted-T base is visible.
9. **Row 3, dots.** The ö marks are visible in row 3 (*köszönök*, three times) but not at the matching place in row 22 (*köszonom*); that literal stands. Stamp row 7 has an acute tick over the o of *dód*, which confirms ó. Other acute accents are mostly too faint to audit and the ledger leaves them out.
10. **"43 fil k".** "fil." is taken as fillér. The clear k belongs to *ke|resek*; why he left it in clear is unknown. The "harmadik lapomat" (third card) and Józsi are not identified. *abba* ("in that one") is my reading of *aba*, and "and family" is the sense of the -ék plural.
11. Address is Ön (formal) in the body, but *gondolj* and *imádód* under the stamp are familiar. This mix is in the signs and is kept. Date 1912-10-12 comes from the portal file name. The large postmark reads BUDAPE… 912 OK…, so "itt" (here) is apparently Budapest, which suits a workman comparing wages with Gyöngyös, though a postmark gives only the posting place. Its day is not legible. The second postmark reads …ROK… (Jászárokszállás) with OKT and what look like 1 and 2, which agrees with the portal date but is not a firm day reading.

## Why it is correct

- The family key was applied unchanged. Of the 572 tokens all have a single value except the one curved sign in row 26, disclosed above; no new sign was invented.
- The whole card reads as coherent Hungarian: a working man writing about pay and winter work, with idiomatic phrases nobody would get by chance (*ha rajtam függ, nem válunk el soha*; *kitelelek valahogy*; *a távolban epedő szívre*; *hű imádód Feri*).
- Repeats decode the same at different places: Gyöngyösön ×2, hogy ×7 (*valahogy* included), csak az, édesem ×3, szív- ×3, köszön- ×2.
- The writer sometimes punctuates, and the marks agree with the division: a clear full stop after *öné* (row 24) and a comma-like mark between the two a of row 23 (*írta, a szívem*).
- Context fits the family: Feri as sender; a workman with a Gyöngyös connection on HCP1303/1310 and a Gyöngyös station on HCP1271; Jászárokszállás address. This is agreement of context, not proof that all Feris are one person.

## Response to review 1

Verdict REVISE. I rechecked each finding on the reviewer's enlargements and the hires scan. All nine are accepted. No word of the normalized text changed; only the punctuation of one sentence did. `work/ledger.txt`, `work/decode.py` and `work/normalized.txt` were corrected and the command re-run: all hashes OK, 572 tokens.

1. **Row 26, egészséget: fixed.** The crop shows loop, three bars, g, one curved sign, right bowl, three bars, g, three bars, gamma. The ledger had one sign too many and the wrong class. Ledger now `J O E G Q S E G E T`, decoded *eg{o|i?}seget*; uncertainty 8 rewritten. The false literal *egezseget* is gone.
2. **Row 26, valakinek: fixed.** Nothing stands between the wave and the k. Ledger now `V A L K I N E K`, literal *valkinek*, listed as a spelling in uncertainty 3.
3. **Row 26, vele: fixed.** The sign after the chevron has two bars. Ledger now `V A L E`, literal *vale*, disclosed in uncertainty 3. Count corrected to 572 tokens.
4. **Row 21: fixed.** Three bars in one column after `#`; ledger now `X E M`. Uncertainty 4 rewritten.
5. **Row 3: fixed.** Both dots of the o after z are visible. Ledger `O: N O:`.
6. **Counts: fixed.** hogy ×7 (with *valahogy*). I also corrected a count the reviewer did not raise: édesem occurs ×3 (rows 5–6, 24, 26), not ×4. Tokens 572.
7. **Row 24 full stop: fixed.** The dot after *öne* is clear. Normalized and all translations now read "... az öné. Édesem, hogy gondolhat olyat ...". The row 23 mark is recorded under "Why it is correct".
8. **Disclosures: fixed.** (a) Row 18 k listed in uncertainty 7. (b) The signs of *gondol*, and of stamp rows 1, 4 and 7, are now `H:d`. The same tall-plus-short form appears in *édesem* in rows 24 and 26, which the reviewer did not list, so these are `H:d` too. (c) The tick on *dód* is recorded in uncertainty 9.
9. **Context: fixed.** Budapest postmark added to uncertainty 11 with the caveat. I also record the second postmark.

The reviewer's open point, the sense of *a mi ám jóban lettünk*, stays disclosed as uncertainty 1: it is one phrase, all its signs are read, and only the division is editorial.

