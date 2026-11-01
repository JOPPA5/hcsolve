# HCP1274 — Feri to Jolánka Tóth: the reunion must wait a week

**Status: complete reading, review 1 ACCEPT, closed.** Claude Opus 5.5, 2026-11-01. No earlier work exists on this number. The key is the Jolánka family key established on finished cards (HCP1216, 1212, 1213, 1217, 1218, 1243, 1301; the earlier solving of that family was by the OpenAI GPT solver and Claude Opus 5.5). The portal shows *Not solved* and attaches no transcription or solution, so the transcription is mine (`work/ledger.txt`). No published solution of this card was found; I looked only at the portal and the repo, and did not read the HistoCrypt article linked on the portal.

## Cipher type and key

Hungarian, monoalphabetic substitution with invented graphic signs (register type MASC), red ink, no word division. Same key as HCP1216:

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | section mark / loop with hook | k | F-like | r |
| six | b | wave | l | right bowl | s |
| left bowl + right bowl | cs | three short strokes | m | gamma | t |
| short stroke + long stroke | d | two short strokes | n | plain cross | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross + | f | long stroke + short stroke | h | dotted crossed curve | i |
| open loop with descender | g | inverted T | j | low descender | y |
| joined loop + descender | gy | crossed diagonal with tail | z | | |

Two marks over o/u give ö/ő/ü; a tick gives an acute. n+y and l+y are run together. c alone, zs and others do not occur on this card. This card separates d (short then long) from h (long then short), and z (tailed) from u (plain) well. Those d and h descriptions are this card's own hand, not the family wording.

**h/p is a word-sense call here.** All 5 h signs (*hogy*, *hét-*, *hasztani*, *halaszta-*, *élvezhettem*) are tall+short, which the family key records as p or as the h/p near-homograph (`tall-short-stroke` in HCP1216's `work/graphic-key.json`; HCP1243 gives h as two separate tall strokes). I read h because *pogy*, *pét*, *pasztani* are no words. So p is not attested on this card, but its absence rests on word sense, not on shape.

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1274/work/decode.py
```

It checks the SHA-256 of all four images, decodes `work/ledger.txt` (one token per written sign, a hand transcription from the pixels, not OCR) and prints the literal rows and the normalized text `work/normalized.txt`.

Rows 18–19 share the bottom left; 20–22 are the bottom right, past the divider (*bol* sits below *tavol*). Row 18 runs beyond row 19.

```
01 kedvesjolankam          12 telenel[x]halaszta
02 sajnala[x]ttalkeltu     13 niaztaboldogsagot
03 datnomhogyaviszont      14 melyetoldalamel
04 latásörömeitkeny        15 leélvezhettemvol
05 telenvagyokegyhet       16 namulassonjolede
06 telodabhasztani         17 semésgoljöramaki
07 edesemmostcsinalunk     18 mégakordogozikmikot
08 aröföskeskereskedö      19 sétalnikelene
09 nekberendezestesma      20 istenveleedesem
10 keletvolnakeszlen       21 üdvözölveatavol
11 niemiatvagyokkeny       22 bol
```

Unenciphered parts. Stamp box: *csokolom szám talan szor sirig hü Feri*. Address: *Szépreményű Tóth Jolanka úrleánynak, Jász-Árokszalás* (Jászárokszállás). Picture side, printed: *Sirassatok engem orgonavirágok…; Megyek, megyek messze földre! Elbujdosok, eltávozok mindörökre:*

## Hungarian (normalized)

Kedves Jolánkám! Sajnálattal kell tudatnom, hogy a viszontlátás örömeit kénytelen vagyok egy héttel odább ha[la]sztani. Édesem, most csinálunk a rőfös [kes] kereskedőnek berendezést, és ma kellett volna kész lenni, emiatt vagyok kénytelen elhalasztani azt a boldogságot, melyet oldala mellé élvezhettem volna. Mulasson jól, édesem, és go[ndo]ljö[n] rám, aki még akkor do[l]gozik, mikor sétálni kellene. Isten vele, édesem! Üdvözölve a távolból.

Stamp box: Csókolom számtalanszor. Sírig hű Feri.

## English

Dear Jolánka of mine! I am sorry to have to tell you that I am forced to put off the joys of our reunion by a week. My darling, we are now making the fittings for the draper, and it should have been finished today; that is why I am forced to postpone the happiness I could have enjoyed at your side. Have a good time, my darling, and think of me, who am still working when one ought to be out for a stroll. Farewell, my darling! Greetings from afar.
Stamp box: I kiss you countless times. Faithful unto the grave, Feri.

## Slovak

Milá moja Jolánka! S ľútosťou Vám musím oznámiť, že radosti zo stretnutia som nútený o týždeň odložiť. Drahá, teraz robíme zariadenie pre obchodníka s látkami a dnes to malo byť hotové, preto som nútený odložiť to šťastie, ktoré som si mohol užiť po Vašom boku. Dobre sa zabávajte, drahá, a myslite na mňa, ktorý ešte pracujem aj vtedy, keď by sa malo ísť na prechádzku. S Bohom, drahá! Pozdrav z diaľky.
V rámčeku na známku: Bozkávam Vás nespočetnekrát. Do hrobu verný Feri.

## Uncertainties

Calls resting on word sense or on the writer's spelling; every sign is transcribed as written.

1. **Row 3, first sign, read d (word sense).** Two tall strokes, the second a little longer: the proportions are closer to h/d than to a short n, but the sign is not a textbook d. *tu|datnom* is the only word; *tunatnom* is none.
2. **Row 3, *a* before *viszont*:** its lower part is a blot; a top bar is clear. *hogy a viszontlátás* gives the reading.
3. **Row 6, *hasztani*:** h a s z t a n i, all clear. Normalized *ha[la]sztani* (the writer dropped *la*); rows 12–13 spell *halasztani* in full, so this is an emendation, not a reading. *egy héttel odább* (*odab* on the card) means a week further on.
4. **Row 8, *kes* before *kereskedö*:** k e s is clearly written, with a three-bar e and no dotted i, so it is not *kis* as written; probably a false start. It is left out of the translation; it does not change the sense. In *rőfös* the two-mark sign is read ő (word sense; ö and ő are not told apart).
5. **Row 17, *goljö rám*:** g o l j ö r a m, all clear. Normalized *go[ndo]ljö[n] rám*, standard *gondoljon rám* ("think of me"), on sense: the writer's missing *ndo* and final *n* are supplied. **This is the word most short of letters (four); *ha[la]sztani* and *do[l]gozik* (items 3, 6) also lack letters. The clause around it reads.**
6. **Row 18, *dogozik*:** normalized *dolgozik*; the l is absent (also a spoken form). ***mikot*:** last sign is the gamma t, no mid-bar; normalized *mikor* (slip or an incomplete r).
7. **Row 10–11, *keszlen|ni*:** read *kész lenni* ("be finished"), written as one with one n carried over the row break; there is no u sign, so *készülni* is not the reading.
8. **Row 14–15, *oldala mel|le élvez-*:** literally *mellé* ("to [your] side") where *mellett* ("at [your] side") is expected; the translation follows the expected sense. Alternative word split *oldalam mellé* ("to my side") is not excluded, since the m is shared.
9. Single-consonant spellings normalized: *kel* → kell, *kelene* → kellene, *keletvolna* → kellett volna, *emiat* → emiatt, *akor* → akkor, *odab* → odább.
10. **Struck signs:** row 2 (a word-sized scribble inside *sajnálattal*) and row 12 (an A-shaped sign with a bar through it) were cancelled by the writer; no reading claimed.
11. Row 1 last sign: three strokes, the third with a small cross-tick; read m. Row 16 first sign: n with its strokes joined at the base, followed by a full stop. The *k* occurs both as a section mark and with a closed loop; both forms fit *kereskedő*, *kény-*.
12. **Row 19, last sign of *kelene*, read e (word sense).** A clear top bar and one lower kinked stroke: either a three-bar e with the lower bars run together, or a two-bar a (*kelena*, a slip). Normalized *kellene* stands either way.
13. **Corrections and stray marks.** Row 4: the second ö of *örömeit* is heavily overwritten; the reading ö is sound. Row 11, after the first i: a separate narrow pale loop between rows 11 and 12, lighter than the surrounding ink, matching no key class; treated as a stray mark, not a sign. A stray dot sits near the row 11 n. Neither changes the text.
14. Accents are transcribed only where clearly visible and otherwise supplied. No date is legible on the card.

## Why it is correct

All ciphertext on the card is decoded: 338 signs read, the 2 the writer struck left unread, and only the stray marks in uncertainty 13 outside the count. The sister key's letter values were applied without change (the shape variants are noted under the key) and yield continuous, situated Hungarian: a concrete excuse (a commissioned fitting-out due today), a coherent sequence of ideas, and the family's phrases (*Isten vele*, *édesem*, *sírig hű*), with the same signature as the plain box text (Feri) and the same addressee. Words forced by no context check themselves independently: *rőfös kereskedő*, *berendezést*, *boldogságot*, *élvezhettem*, *sétálni kellene*.

## Response to review 1

Verdict ACCEPT, four minor findings, no change to any decoded letter. `work/ledger.txt` got a comment line only (the row data are untouched), `work/normalized.txt` is unchanged. Re-run of `python3 -I ciphers/hcp-1274/work/decode.py`: all four hashes OK, same output.

1. **Row 19 last sign. Fixed.** I checked `review/work/z_kelene.png`: top bar plus one kinked lower stroke, as the reviewer says. Marked as a word-sense call in uncertainty 12 and in a ledger comment. *kellene* stands.
2. **h/p not disclosed. Fixed.** Added a paragraph under the key table: all 5 h signs are tall+short, h rests on word sense, the d and h descriptions are this card's hand. The statement that p does not occur is removed.
3. **Two marks not accounted for. Fixed.** Checked `review/work/z_oval.png` and my crops `work/resp/r4.png`, `work/resp/r11.png`: the pale loop, the stray dot and the overwritten ö are there. Now uncertainty 13; the "no sign left over" claim in *Why it is correct* is softened.
4. **Inconsistency in the uncertainties. Fixed.** Item 5 now gives the normalized form *go[ndo]ljö[n]* as in `work/normalized.txt`, with *gondoljon* as the standard form, and no longer calls it the only short word. Item 4's *kis* is dropped: the sign is e.

Also from the review: "applied without change" now refers to letter values only. I agree with the reviewer's list of what stays unverified, including that the HistoCrypt article was not read.
