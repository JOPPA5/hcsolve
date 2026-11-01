# HCP1271: to Jolánka Tóth, new workshop and new address at Gyöngyöspüspök (March 1912)

**Status: whole message read, every cipher row decoded; small disclosed points below.** Claude Opus 5.5, 2026-11-01.

Credit: reading, ledger and interpretation by Claude Opus 5.5. No earlier work exists on this number. The key comes from the finished Jolánka cards, chiefly HCP1216 (key first transferred by the OpenAI GPT solver, completed by Claude Opus 5.5). The portal shows status Not solved and attaches no transcription or solution; no published solution was seen or used. The orchestrator's AI-register check of 2026-11-01 found no record of this card.

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented graphic signs (Jolánka family key, unchanged). Word spaces are partly kept. Portal language "Unknown" is resolved: Hungarian.

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | section mark (S, 8 forms) | k | F-like | r |
| six | b | wave | l | right bowl | s |
| left bowl (€-like) | c | three short strokes | m | gamma | t |
| opposed bowls | cs | two short strokes | n | plain cross x | u |
| short stroke left + tall right | d | cursive loop with hooked arm | o | chevron (1-shaped) | v |
| three bars | e | tall stroke + short right | h / p | low descender | y |
| open loop with descender | g | loop with straight crossbar, dotted | i | crossed flagged diagonal | z |
| loop + descender joined | gy | inverted T | j | | |

Dots over x give ü. `cz` is old spelling for c (*czím*). No f occurs.

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1271/work/decode.py
```

It checks the SHA-256 of both `source/` scans and both `work/hires/` originals, decodes `work/ledger.txt` (263 signs, one token per written sign, read by eye on enlarged crops, not OCR and not blind) and prints the literal rows and `work/normalized.txt`. Crops: `work/crops/`, made by `work/crop.py`.

## Literal decipherment

`[x]` = blotted sign restored by word sense; `h` = the h/p sign.

```
01 dragacsilagomki        10 ideczimezesorait
02 vanomhogyalegjobb      11 kedvesjolankam
03 kedvebentalaljaso      12 [j][o]mulatastkiva
04 raimedesemtudatom      13 [n]okholnahragon
05 hogyenmarmamunka       14 [d]oljonn[e]haram
06 bademostmasmühely      15 kiszintengon[d]ol
07 betehataczimem         16 onristenveaviszont
08 ismegvaltozik          17 latasracsokolomezersze
09 [c]zimemiseshedig
```

## Hungarian (normalized)

Drága csil[l]agom! Kívánom, hogy a legjobb kedvében találja soraim. Édesem, tudatom, hogy én már ma munkába [megyek?], de most más műhelybe, tehát a czímem is megváltozik. Czímem is, és pedig: Gyöngyös Püspöki. Ide czímez[z]e sorait. Kedves Jolánkám, jó mulatást kívánok holnapra. Gondoljon néha rám, ki szintén gondol önr[e]. Isten ve[le], a viszontlátásra. Csókolom ezersze[r].

Stamp box, plain: Üdvözlöm a távolból, hű kedvese.

## English

Dear star of mine! I hope my lines find you in the best of spirits. My darling, I let you know that I am already [going] to work today, but now to another workshop, so my address changes too. My address too, namely: Gyöngyöspüspöki. Address your lines here. Dear Jolánka, I wish you a good time tomorrow. Think of me sometimes, who also thinks of you. Farewell, until we meet again. I kiss you a thousand times.

Stamp box: I greet you from afar. Your faithful sweetheart.

## Slovak

Drahá moja hviezda! Želám si, aby Vás moje riadky našli v najlepšej nálade. Drahá, oznamujem Vám, že už dnes [idem] do práce, ale teraz do inej dielne, takže sa mení aj moja adresa. Aj moja adresa, a to: Gyöngyöspüspöki. Sem adresujte svoje riadky. Milá Jolánka, želám Vám na zajtra dobrú zábavu. Myslite niekedy na mňa, ktorý tiež myslí na Vás. S Bohom, dovidenia. Bozkávam Vás tisíckrát.

Pole na známku: Pozdravujem Vás z diaľky. Váš verný milý.

## Not enciphered

- Between rows 9 and 10, plain cursive: *Gyöngyös Püspöki*. It is written large as the address itself and is part of the sentence.
- Stamp box, plain cursive: *üdvöz / löm a / távol / ból hű / kedvese*.
- Address: *Szépreményű Tóth Jolánka úrleánynak, Jász Árokszállás*. The last word runs under the collector's stamp and the card edge; it is read from the family's other addresses as well as the pixels.
- Picture side: printed verse and title (*Akiknek a szívük fáj...*) and series number 1376/5; no handwriting.

## Uncertainties

1. **Blots, restored by word sense.** Row 1 k of *kívánom*: pink-smudged, but the section-mark outline is legible, so it is not bracketed in the literal. Row 9 first sign (c of *czimem*): a solid blot, restored from the following z and the same word in rows 7 and 10. Row 13 first sign (n of *kívánok*): a blot of about two strokes. Row 14 first sign (d of *gondoljon*) and row 15 d of *gondol*: heavily inked, but the short-left-plus-tall shape remains. Row 14 e of *néha*: blotted bars with an accent above.
2. **Row 12 *jó*.** The first sign is a blotted inverted T. The next is wiped in a pink smear: a loop survives, plus a mark above taken as the acute, and part of a right arm. That arm is damaged, so it could be i; *ji* gives no word, and *jó mulatást kívánok* also occurs on HCP1310. The ó rests on word sense.
3. **Row 9 *-miseshedig* word division.** All signs after the blot are clean. Read *czímem is, és pedig* ("my address too, namely"), which repeats *czímem is* from rows 7–8. This repetition is awkward. The alternative *czíme Mises, pedig Gyöngyös Püspöki* (a person or firm called Mises) is not excluded, but gives no known name. An accent stroke stands above the e of `ese`, which favours *és* over *Mises*; the uncertainty stays because the sentence remains awkward. Either way the sign is p, and *pedig* rests on word sense.
4. **h/p calls by word sense:** p in *holnapra* (row 13) and *pedig* (row 9); h elsewhere (*hogy*, *műhely*, *tehát*, *néha*).
5. **Row 5–6 *munkába*.** No verb is written. I read it elliptically, *munkába [megyek]* ("going to work"); the verb is my supply. The sense of the clause does not depend on it, but "am going" against "am at" is not settled, and *műhelybe* may stand for *műhelybe[n]*. The English and Slovak bracket the supplied verb for this reason.
6. **Row 16 *önr[e]*.** The loop shows no clear ö dots, but the descender of row 15's i crosses its top, so dots may be hidden. The e is not on the card; the row goes straight on to *isten*. Reading *on r-* otherwise gives no sense after *szintén gondol*.
7. **Row 17 opening.** The second and fourth letters of *látásra* are blurred bars; a is taken from the word. After the cs of *csókolom* is an o overwritten into a dense 8-like mass, with a large hooked arm. The arm joins the loop and is taken as part of the o (one sign), not as a separate s. No accent is visible on o.
8. **Writer's omissions, normalized:** *csilagom* (one l), *czímeze* (one z), *ve* for *vele* (compare HCP1310 *isten ve[l]ed*), *ezersze* (no final r; nothing follows on the card).
9. **Sender and date.** The card is unsigned beyond *hű kedvese*. Hand, closing formulas and his being a workman with a Gyöngyös connection fit "Feri" of HCP1303/1310, but no identification is claimed. The date 16 March 1912 comes from the file name, and the left cancel shows a compatible fragment (*12*, *MA*, *16*). That day was a Saturday, which fits *holnapra* for a Sunday outing, but this is only suggestive.

## Why it is correct

- The family key, unchanged, turns all 17 rows into Hungarian with no unexplained sign.
- The stream gives long unforced phrases with typical family formulas: *kívánom, hogy a legjobb kedvében találja soraim* (also HCP1303), *édesem, tudatom*, *Isten ve[le], a viszontlátásra*.
- The enciphered *ide czímezze sorait* ("address your lines here") directly follows the plain place name, and *a czímem is megváltozik* announces it. The cipher thus makes sense with text that was not enciphered.
- Repeats decode identically: *czím-* ×3, *édes-/kedves-*, *gon-* ×2.

## Response to review 1

Verdict ACCEPT. All five findings are minor; I rechecked each on the reviewer's crops and accepted all of them. Only the ledger tokens below changed; the normalized Hungarian did not. `python3 -I ciphers/hcp-1271/work/decode.py` was re-run after the fixes: all four hashes OK, 263 signs, output matches the literal block above.

1. **Row 3 sign 7: fixed.** `review/work/t2.png` shows three bars before the n, the third lying low near row 4. It is e, not a. Ledger token and literal now give *kedveben-*, as the normalized text already did.
2. **Row 17 stray sign: fixed.** In `review/work/z17b.png` the stroke leaves the overwritten loop without a break and hooks down, as the arm of an o does. `{s}` is removed from the ledger and decoder, the count goes from 264 to 263 signs, and Uncertainty 7 and "Why it is correct" are updated. *Csókolom* is unaffected.
3. **Row 1 k: fixed.** `review/work/a2.png` shows the section-mark outline under the pink smudge. The brackets are dropped and the sign is listed in Uncertainty 1.
4. **Row 9 accent: fixed.** `review/work/c2.png` shows a short stroke above the e of `ese`. It is noted in Uncertainty 3 as favouring *és*; the uncertainty stays.
5. **Supplied verb in the translations: fixed.** English and Slovak now bracket it, and Uncertainty 5 says so.
