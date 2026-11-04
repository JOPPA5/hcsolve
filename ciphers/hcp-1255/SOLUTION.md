# HCP1255 — Feri to Jolánka Tóth: "your letter came, I am coming on Sunday"

**Status: complete reading, corrected after review 1 (one small unexplained run of three syllables, item 1; one unread ink blot, item 2).** Written 2026-11-01 by Claude Opus 5.5. No earlier work on this number exists. The portal shows status *Not solved*, with no transcription or solution attached; no published solution of this card was found. The transcription was made by me from the scan, sign by sign.

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented graphic signs: the "Jolánka" postcard family, key transferred unchanged from the finished cards HCP1216, 1213, 1217, 1218, 1243, 1301 (table in `ciphers/hcp-1216/SOLUTION.md`). No new sign value was needed.

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | section mark | k | F-like | r |
| six | b | wave | l | right bowl | s |
| opposed bowls | cs | three short strokes | m | gamma/corner | t |
| tall stroke + short (see below) | d / h / p | two short strokes | n | plain cross x | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross + | f | low descender | y | crossed diagonal | z |
| open loop with descender | g | dotted crossed curve | i | inverted T | j |
| joined loop + descender | gy | | | | |

**Type note (2026-11-03):** register type is now **MASC + Steganography**: besides the cipher, the card carries a hidden plain-Hungarian message in the stamp box, written where the stamp was stuck over it (the stamp has since been lifted). See "Stamp-box message (2026-11-03)".

Two marks over o/u give ö/ő, ü/ű. The text over the stamp box and the address are in plain writing, and the verse on the picture side is printed: none of these is ciphertext.

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1255/work/decode_opus.py
```

It checks the SHA-256 of all four image files, decodes the sign ledger `work/ledger-opus.txt` (20 rows, one token per written sign), and prints the literal rows and `work/normalized-opus.txt`.

## Literal decipherment (as printed by the command)

```
01 kevesjolankambecses        11 lenlanlemegyekazthi
02 soraitköszönattel          12 szeedesapamislemegy
03 megkaptammelyetepe         13 ezelbezaromsoraim
04 dőszivelvartamiga          14 istenveleaviszont
05 zan[?]sajnalomhogynem      15 latásrüdvözlomata
06 vigyazotmagarade           16 volbolsirighütisz
07 azmegnyugtathogymar        17 telőjeferiedesjolan
08 mulobavanitninsemi         18 markesorejarazidi
09 utságedesjolankam          19 töbetnemirokmajd
10 vasarnapokvetlenlen        20 vasarnapbovaban
```

Plain writing over the stamp box: csokolom / szamta / lan / szor / szerető / sziv.
Address: Szépreményű(?) Tóth Jolánka úrleánynak, Jász-Árokszállás.

## Hungarian (normalized)

Kedves Jolánkám! Becses sorait köszönettel megkaptam, melyet epedő szívvel vártam. Igazán [blot] sajnálom, hogy nem vigyázott magára, de az megnyugtat, hogy már múlóba van. Itt nincs semmi újság. Édes Jolánkám, vasárnap okvetlen {len len lan} lemegyek. Azt hiszem, édesapám is lemegy. Ezzel bezárom soraimat. Isten vele, a viszontlátásra. Üdvözlöm a távolból. Sírig hű tisztelője, Feri. Édes Jolán, már későre jár az idő, többet nem írok. Majd vasárnap bővebben.

Over the stamp box (plain): Csókolom számtalanszor. Szerető szív.

## English

Dear Jolánka! I received your esteemed lines with thanks; I had awaited them with a yearning heart. I am truly sorry that you did not take care of yourself, but it reassures me that it is already passing. There is no news here. Sweet Jolánka, on Sunday I will definitely {len len lan} come down. I think my father is coming down too. With this I close my lines. God be with you, until we meet again. I greet you from afar. Your admirer, faithful unto the grave, Feri. Sweet Jolán, it is getting late, I will write no more. More on Sunday.

Over the stamp box: I kiss you countless times. Loving heart.

## Slovak

Milá Jolánka! Vaše vzácne riadky som s vďakou dostal, očakával som ich s túžiacim srdcom. Naozaj ľutujem, že ste si nedávali pozor, ale upokojuje ma, že to už prechádza. Tu nie je nič nové. Sladká Jolánka, v nedeľu určite {len len lan} prídem dolu. Myslím, že aj môj otec príde dolu. Týmto končím svoje riadky. S Bohom, dovidenia. Pozdravujem Vás z diaľky. Váš až do hrobu verný ctiteľ, Feri. Sladká Jolán, už je neskoro, viac nepíšem. Viac v nedeľu.

Cez políčko na známku: Bozkávam Vás nespočetnekrát. Milujúce srdce.

## Stamp-box message (2026-11-03)

Audit by Claude Opus 5.5 on the un-converted original `work/hires/cpc_1912-03-11_HU__HU_Jasz-Arokszalas_jolanka-08_adr.jpg`; crops at 2-4x in `work/stamp-2026-11-03/` (`stampbox_2x.png`, `band0-2_3x.png`, `corner_4x.png`).

- **State:** the stamp has been lifted. The dashed stamp box is empty except for the printed publisher wreath (P. R. A.); just below its lower right corner a torn green stamp fragment remains on the card, with a paper scar around it, and the right postmark runs onto that spot. So the writing in the box lay under (or at) the stamp: a hidden message, steganography.
- **Script:** plain Hungarian in the same red ink, not cipher signs.
- **Literal reading (6 lines):** `csokolom / szamta / lan / szor / szerető / sziv`. Every letter is read from the pixels; *szamta* and *lan* run over the printed wreath but stay legible; *szerető* has the two marks of ő. Nothing restored.
- **Normalized Hungarian:** Csókolom számtalanszor. Szerető szív.
- **English:** I kiss you countless times. Loving heart.
- **Slovak:** Bozkávam Vás nespočetnekrát. Milujúce srdce.
- **Unread:** nothing. This is the same text already given above; the audit only confirms it and records that it sat under the stamp. The ledger script does not cover it; it is read by eye.

## Uncertainties

Every sign is transcribed as written; the normalization is editorial.

1. **Rows 10–11, the run `len len lan` (unexplained).** After *okvetlen* come three wave + bars + two-stroke groups, then *lemegyek*: `okvet-len len|len lan|lemegyek`. The signs are clear, except that the first wave of row 11 lies partly under the printed word "Bromüra" and that the wave of the `lan` has an ink spot. I read that spotted sign as a wave, not a chevron, because it dips and has a rising tail beyond the spot; if it were a chevron the group would be *van*, which still gives no sentence. An isolated slanted mark stands above the l of the final *-len* of *okvetlen* in row 10; I cannot say what it is. I have no meaning for this run. It may be a false start or stutter on *le-*, but that is a guess. Removing it gives a sound sentence, so it is left marked in braces, not translated.
2. **Row 5, *Igazán* and the blot.** Row 4 ends `iga`. Row 5 opens with z, a, then two nearly equal strokes (50 and 43 px, ratio 0.86), which is this writer's n (his n pairs measure about 0.83–1.10, tall + short pairs 0.47–0.62, and measured d pairs have the second stroke longer). A large ink blot follows, then *sajnálom*. The blot has two tips at bar-like heights on the right, so it may hide a sign, or be a correction or a spill; nothing in it can be read. I lead with *Igazán sajnálom* ("I am truly sorry"), one simple sentence that needs nothing from the blot. The former reading *Igaza, d[e] sajnálom* ("You are right, but I am sorry") needs the pair to be d, against the stroke proportions, and a restored e, and gives two adversative *de* in a row; it remains a weaker alternative. The n rests on stroke shape plus sense, from a small sample of measured pairs, not on proof.
3. **Tall + short sign (d / h / p), chosen by word sense.** d: *epedő* (r4), *de* (r6), *édes* (r9, 12, 17), *üdvözlöm* (r15), *majd* (r19). h: *hogy* (r5, 7), *hi-* (r11), *hű* (r16). p: *megkaptam*, *epedő* (r3), *vasárnap* (r10, 20), *édesapám* (r12). The d of *édes* tends to a shorter first stroke, and the d of *idő* (r18) is two long strokes, but none of this is a clean rule.
4. **Two-bar e.** Tokens record the bars seen, and the writer separates a and e well. Only two words have e normalized over a two-bar sign: *köszönettel* (r2, literal *köszönattel*) and *bővebben* (r20, literal *bovaban*, also one b and no marks on o).
5. **Row 20 *bővebben*** is therefore an interpretation of `bovaban`: all signs are clear, the word is reconstructed. It fits *Majd vasárnap …* ("more on Sunday"). The same applies to row 8 *múlóba van* (literal, colloquial for *múlóban*).
6. **Row 9 *újság*:** the second sign is plainly a gamma (t), literal `utság`, not an inverted T (j). Read as a writer's slip, on sense (*semmi újság*).
7. **Row 11–12 *hiszem*:** literal `hi|sze`, m omitted by the writer. The first sign of row 12 is a right bowl seen under the printed "Br" of "Bromüra" (separated with a red-minus-green map, `work/rows/print_red.png`). The i of row 11 stands past the printed rule.
8. **Row 16 *sírig*:** the first sign is a slanted stroke with a bowl, an unusual form of s, read by word sense in the family formula *sírig hű*. *hű* has two marks read as ű.
9. **Row 18 *idő*:** the last sign has the i form (literal *idi*, no marks); o is supplied on sense. The second-last sign is read d, as two long strokes.
10. **Row 3:** the t of *megkaptam* is smudged and looks F-like; t by sense.
11. **Row 14–15:** *viszontlátásra üdvözlöm* is literally `viszontlatásr|üdvözlom`; the final a is missing. The fourth sign of row 15 is two full bars with a short slanted mark high on the right, taken as a with an acute mark as in *újság* (r9 pos 4); if the mark were a short third bar the sign would be e (*latesr*), and the word would not change. Row 1 is literally `keves`: the third sign has the v form, not the d of row 9, so *Kedves* assumes an omitted d. Other spellings normalized: *sziv el* → szívvel, *vigyazot* → vigyázott, *ninsemi* → nincs semmi, *it* → itt, *ezel* → ezzel, *soraim* → soraimat, *tobet* → többet; most accents are supplied.
12. **Paratext.** The first address word (reading *Szépreményű*) is an uncertain reading of plain script; it is not part of the cipher. The plain stamp text ends *sziv*; I give it as is. The date 1912-03-11 comes from the portal file name. The postmarks partly support it: the left one shows day 11 clearly and the right one shows 912; the month is not verified. Sender "Feri" is from the signature (row 17); I do not claim he is the Feri of HCP1216, although the formula *sírig hű* recurs.

## Why it is correct

- A key transferred unchanged from finished cards turns all 20 rows into Hungarian; nothing is fitted to this card.
- The text is coherent and specific: a reply to a letter, concern about an illness that is passing, a Sunday visit, closing formulas of the family (*Isten vele, a viszontlátásra*; *sírig hű*), a postscript that it is late.
- Repeats agree: *hogy* ×2, *édes* ×3, *Jolán(kám)* ×3, *vasárnap* ×2, *lemegy-* ×2, *sorai-* ×2.
- Word-sense choices are limited to the points listed above.

## Response to review 1

Verdict REVISE. All seven findings are accepted; I rechecked each on the reviewer's crops and on `work/review1/r05_left.png` (3x, row 5). `python3 -I ciphers/hcp-1255/work/decode_opus.py` passes all four hashes and prints the corrected text above.

1. **Row 5 (major): fixed.** On the crop the pair after z, a is two nearly equal strokes, not tall + short. Ledger token `D [E]` is now `N [?]`. *Igazán sajnálom* leads in all three languages, the blot is stated as unread and the old reading is kept as a weaker alternative (item 2). The sentence meaning changes only in this clause: "You are right" goes, "truly" comes in.
2. **Rows 10–11 (major): fixed.** The last group of row 10 has three bars on the crop. r10 pos 18 is now E, so the run is {len len lan} everywhere. The mark above the *-len* of *okvetlen* is recorded in item 1 and the ledger header. The run stays unexplained.
3. **Row 12 (major): fixed.** Both signs have three clean bars. r12 pos 15 and 17 are now E, literal *lemegy*; removed from item 4.
4. **Rows 7 and 15 (minor): fixed.** r07 pos 11 is two clean bars, now A, literal *megnyugtat*. r15 pos 4 is now A:acute, with the e alternative stated in item 11.
5. **Two-bar e (minor): fixed.** Item 4 and the ledger header are rewritten; only r02 and r20 remain. The sentence "each a here may be e" is gone from item 1.
6. **Key table (minor): fixed.** gy row added.
7. **Date (minor): fixed.** Item 12 now states day 11 on the left postmark and 912 on the right one, both seen on the address scan. The month remains unverified.

No key value changed. The corrections change one clause of the translation (row 5), the spelling of the unexplained run, and four literal letters of words already read; the rest of the reading stands.
