# HCP1270 — Feri to Jolánka Tóth: the army medical review, a possible farewell, and no suit to visit in

**Status: PARTIAL. All signs are transcribed and rows 1 to 29 plus row 30 up to *ruhám* read as connected Hungarian, but the last clause of row 30 is not understood (item 1 under Uncertainties). No register entry.** Claude Opus 5.5, 2026-11-01.

Credit: no earlier work on this number. The key comes from the finished Jolánka family cards (HCP1216, 1212, 1213, 1217, 1218, 1243, 1301; capture and key transfer there by the OpenAI GPT solver, completed by Claude Opus 5.5). All reading on this card is by Claude Opus 5.5. The portal shows status *Not solved* and attaches no transcription or solution. No published solution of this card was found; no outside plaintext was used. The transcription is my own, from `work/hires/*_adr.jpg`.

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented graphic signs, the Jolánka family key unchanged (table in `ciphers/hcp-1216/SOLUTION.md`). Ledger tokens: letters as themselves, `F`=r, `)`=s, `X`=u, `6`=b, `+`=f, `H`=h/p sign, `CS`=cs. This writer spells *gy* and *ny* as two signs (g+y, n+y) on this card. *cs* appears as opposed bowls `()` and as a closed ring (rows 12, 25). Plain address text: *Szépreményű Tóth Jolánka úrleánynak, Jász Árokszállás*; rectangular Újpest postmark.

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1270/work/decode.py
```

It checks the SHA-256 of all four image files, decodes `work/ledger.txt` (848 tokens, 30 main rows plus 8 rows under the stamp), and prints the literal rows and `work/normalized.txt`. The ledger is a manual reading of enlarged crops, not OCR. Rows 1–24 fill the left panel; rows 25–30 run across the whole card; the stamp rows S1–S8 sit in the stamp square.

## Literal decipherment

```
01 szeretetedesjolankamkecsesso           16 vahanemsikerülafelül
02 raitmegkahtammelyetköszö               17 viszgalatakorlegjobb
03 nökszehenamisorailetoen                18 ba[n]leszhaelbucsuzunkegy
04 rögtönvalaszoltamigaz                  19 mastolesenmajdbucsut
05 hogynahigutazotezalah                  20 mondokmindennekesugy
06 azsebembeedesemsajnalato               21 eltünö[k]hogyhiremsem
07 matkelkifejeznemhogyo                  22 haljasenkimertakormar
08 janrosszulvegzödötamulat               23 latomazthogyüldözaba[l]
09 sagedesemhakesikavalaszom              24 sorseshaenekemnincssze
10 aztcsakelfoglaltsagomnak               25 rencsemnemteszemszerencsetlennemagatisbiztatoszavam
11 tuladonitsahalaisten                   26 melmegmagaboldoglehetmasferfimeletismertanöiszivkö
12 nakezidöszerintnincs                   27 nyenfe[l]ejtdeazthagyjukutoljaratalanerrenemkerüla
13 semmibajomamiazorvo                    28 sorkedvesemamia[m]enetelemetiletiugyaladolognagyonsze
14 sivizitetiletimegnem                   29 retnekmennihogylathassamdeaztartviszahogynincsked
15 voltamöszintenmegval                   30 vemrevaloruhamsohamostvazazoltonyamitmabistud
stamp: [cs]okol [j]as[z][a]m talan szor s[z]ere [t]oked vesse feri
```

## Hungarian (normalized)

Szeretett édes Jolánkám! Kecses sorait megkaptam, melyet köszönök szépen. Ami sorai[t] [i]lletően, rögtön válaszoltam, igaz, hogy napig utazott ez a lap a zsebembe. Édesem, sajnálatomat kell kifejeznem, hogy olyan rosszul végződött a mulatság. Édesem, ha késik a válaszom, azt csak elfoglaltságomnak tulajdonítsa. Hála Istennek, ez idő szerint nincs semmi bajom. Ami az orvosi vizitet illeti, még nem voltam. Őszintén megvallva, ha nem sikerül a felülvizsgálatakor, legjobban lesz, ha elbúcsúzunk egymástól, és én majd búcsút mondok mindennek, és úgy eltűnök, hogy hírem sem hallja senki, mert akkor már látom azt, hogy üldöz a balsors, és ha énnekem nincs szerencsém, nem teszem szerencsétlenné magát is. Biztató szavam mel[?] még maga boldog lehet más férfi mellett is, mert a női szív könnyen felejt. De azt hagyjuk utoljára, talán erre nem kerül a sor. Kedvesem, ami a menetelemet illeti, úgy áll a dolog, nagyon szeretnék menni, hogy láthassam, de az tart vissza, hogy nincs kedvemre való ruhám, ⟨clause unread: `sohamostvazazoltonyamitmabistud`⟩.

Under the stamp: [Cs]ókol[j]a s[zá]mtalanszor s[z]ere[t]ő kedvese Feri.

## English

My beloved sweet Jolánka! I received your graceful lines, for which I thank you kindly. As for your lines, I answered at once, though it is true this card travelled in my pocket for some days (literally *napig*, "for a day" or "up to the day"; a number may be understood). My darling, I must express my regret that the party ended so badly. My darling, if my answer is late, put it down only to my being busy. Thank God, at present nothing is wrong with me. As for the medical inspection, I have not been yet. To be frank, if it does not go well at the review board, it will be best if we say goodbye to each other, and I will then say farewell to everything and vanish so that no one hears of me, for then I will see that ill fortune pursues me; and if I have no luck, I will not make you unhappy too. My word of comfort [`mel`, unresolved]: you can still be happy with another man as well, for a woman's heart forgets easily. But let us leave that for last; perhaps it will not come to that. My dear, as for my going there, things stand like this: I would very much like to go so that I can see you, but what holds me back is that I have no clothes to my liking, ... [last clause unread; only the fragments *most* "now", *az öltöny* "the suit", *amit* "which" are firm].
Under the stamp (partly restored): Kisses you countless times, your loving sweetheart, Feri.

## Slovak

Moja milovaná, sladká Jolánka! Vaše pôvabné riadky som dostal, za čo pekne ďakujem. Čo sa týka Vašich riadkov, odpovedal som hneď, pravda, že tento lístok cestoval niekoľko dní v mojom vrecku (doslova *napig*, „jeden deň“ alebo „do dňa“; možno sa rozumie počet). Drahá, musím vyjadriť ľútosť, že sa zábava skončila tak zle. Drahá, ak moja odpoveď mešká, pripíšte to iba mojej zaneprázdnenosti. Vďaka Bohu, toho času mi nič nie je. Čo sa týka lekárskej prehliadky, ešte som tam nebol. Úprimne povedané, ak sa to na superrevízii nepodarí, najlepšie bude, ak sa rozlúčime, a ja potom dám zbohom všetkému a zmiznem tak, že o mne nikto nebude počuť, lebo vtedy už uvidím, že ma prenasleduje nešťastie; a ak nemám šťastie, neurobím nešťastnou aj Vás. Moje povzbudivé slovo [`mel`, nevyriešené]: Vy ešte môžete byť šťastná aj s iným mužom, lebo ženské srdce ľahko zabúda. Ale to nechajme nakoniec, azda k tomu nedôjde. Drahá, čo sa týka môjho odchodu, je to tak: veľmi by som chcel ísť, aby som Vás videl, ale to ma zdržiava, že nemám šaty podľa svojej chuti, ... [posledná veta neprečítaná; isté sú len zlomky *most* „teraz“, *az öltöny* „ten oblek“, *amit* „ktorý“].
Pod známkou (čiastočne doplnené): Bozkáva Vás nespočetnekrát Váš milujúci milý, Feri.

## Uncertainties

1. **Row 30, last clause: unread, the card is partial.** Literal `sohamostvazazoltonyamitmabistud`. Every sign is legible; the sense is not. Only *most* ("now"), *az öltöny* ("the suit") and *amit* ("which") are firm. The former conjecture *soha most va[n] az öltöny, amit ma[ga] is tud[ja]* needed three changes against the signs (`z` to n, `6` to *ga*, added *-ja*) and still has no syntax, so it is withdrawn as a reading; `ma bíz tud` is no better (the sign is s, not z). Also tried after the review, all without a sentence: `v azaz` (*azaz* "that is"), `sopa` (h/p read p), `-tun` (d/n read n), *bő* for `bi` (the sign has a single dot, i), and three bars for the first a of `vaz` (that sign has a small extra tick between its bars, so *vez* is possible as a sign, but gives no word). The clause runs to the corner of the card and may stop short for want of room. No Hungarian speaker has checked it.
2. **Row 5 `ez a # lap`**: before the wave of *lap* stands a z-like sign joined to the wave. I take it as a false start. *lap* itself rests on word sense (h/p sign read p, small a).
3. **Row 7, last sign** is a blotted cross after *o*, treated as a cancelled start of *j*: row 8 opens with a clear *j*, giving *ojan* = olyan.
4. **Row 18 `ba[n]`**: the two strokes are overinked. *legjobb|ban* is literal with one b too many; normalized *legjobban lesz*. The n is a restoration from a blotted sign.
5. **Row 21 `eltünö[k]`**: the sign after n is a blot with two dots and a hook at upper right. The hook could belong to a k or be a separate s; *eltűnök* is the only word, so k is word sense. The isolated stroke at the end of row 21 has no letter value.
6. **Row 23 `ba[l]`, row 27 `fe[l]ejt`, row 28 `a[m]enetelemet`**: each sign is overinked; the values are restorations that give *balsors*, *felejt*, *menetelemet*.
7. **Row 26 `mel`, unresolved.** Three strokes, three bars, a clear wave, literally *mel*. *Mert* would need two letters not on the card, and the writer spells *mert* correctly in rows 22 and 26, so this is left as `mel[?]`. Two ways to take it: *Biztató szavam: még maga boldog lehet ...* with `mel` as a stray word, or *mel[y]* ("which") with y dropped, as in `ojan` for *olyan*; the older punctuation *..., biztató szavam! Mer[t] még ...* is the third and weakest. The sense of the sentence is the same in all three. The h/p and d/n calls in *kaptam, szépen, napig, lap* (p) and *hogy, ha, hála, lehet, hírem* (h), and in *idő, mondok, üldöz, végződött, dolog* (d) rest on word sense. So do the k/g calls: closed k and open g with descender run close together on this card, for example in row 24 *enekem* and row 16 *sikerül*. No word changes.
8. **Row 29 `aztart`**: the sign after *de* has a closing curve, so it looks between a and s. Read *de az tart vissza* by sense; literal `s` would give *de sztart*.
9. **Row 9**: the a after *val* is overwritten with a vertical stroke; value a by word.
10. **Stamp rows.** The stamp was torn off and took ink with it. S1 opens with faint remnants read *cs*; S2 opens with a worn sign read *j*, then *a*, then the faded *sz*, a lost *á* and three strokes *m*; a green-stained crescent there (`#`) is paper damage. S5 *s[z]ere* and S6 *[t]ő* are also damaged. *Csókolja számtalanszor szerető kedvese Feri* is the family closing formula and fits all surviving signs, but S2 is largely a restoration, so the normalized line brackets the restored letters. The first sign of S2 is only a broken angle (the family also has *Csókolom*; *Csókolja* fits better), and S1 has more faint residue at its right end that the ledger does not account for.
11. Row 3 literal `amisorailetoen` has one i and no t between *sora* and *let*: the normalized *sorai[t] [i]lletően* adds both, and *ami ... illetően* itself mixes two constructions. Row 5 *napig* is "for a day / up to the day", not *napokig*; the translations' "some days" is an interpretation.
12. Writer's spellings normalized: double consonants dropped (*szeretet, kel, mulat, ilet-, mellet, ojan, akor, hala, visza*), *tuladonitsa* (j omitted), *ennekem/enekem*, *vizsgalat* with *sz*, *ál a dolog*. Accents and many dots are invisible and are supplied.
13. Date and sender identity are not on the card apart from the signature Feri. The felülvizsgálat suggests the First World War, but that is my inference.

## Why it is correct

The family key, unchanged, gives Hungarian for rows 1 to 29 and row 30 up to *ruhám* with no new sign, and row 30's last clause decodes to letters without yielding a sentence. Long words that nothing could force come out whole: *elfoglaltságomnak, felülvizsgálatakor, szerencsétlenné, elbúcsúzunk, menetelemet*. The content is coherent from the start up to, but not including, the last clause: the recruit awaiting a medical review tells his girl what he will do if it fails. Repeated words decode alike (*hogy* ×6, *édesem* ×2, `ilet-` ×3: *illetően* once, *illeti* twice). Signature Feri, the closing style and the addressee match the family, including HCP1216.

## Response to review 1

Verdict REVISE. No sign, key value or ledger entry changed; `work/ledger.txt` and `work/decode.py` are untouched. `work/normalized.txt`, the translations and the uncertainties were edited, and `python3 -I ciphers/hcp-1270/work/decode.py` was re-run: all four hashes OK, 848 signs.

1. Row 30 clause (major): accepted, and not solved. I re-examined the signs on the reviewer's 3x to 4x crops and tried the segmentations it proposed plus a few of my own (Uncertainty 1); none gives a sentence. The header now says partial, the clause stands as literal text, the continuous translation was removed in English and Slovak, the earlier conjecture is withdrawn, and there is no `register-entry.txt`.
2. `Mer[t]` (minor): fixed. `mel[?]` stays unresolved in the normalized text, *biztató szavam* now opens the next sentence, and alternatives are listed (Uncertainty 7), including *mel[y]*, which the review did not raise.
3. Row 3 (minor): fixed. Restorations bracketed and disclosed (Uncertainty 11).
4. `napig` (minor): fixed. "Some days" is flagged as an interpretation in both translations and in Uncertainty 11.
5. k/g (minor): fixed. One line added to Uncertainty 7.
6. Stamp rows (minor): fixed. Normalized closing bracketed; broken first sign of S2 and S1 residue disclosed (Uncertainty 10).
7. Counts (minor): fixed, confirmed by counting the literal rows: *hogy* 6, *édesem* 2, `ilet-` 3. The claim now stops before the last clause.
