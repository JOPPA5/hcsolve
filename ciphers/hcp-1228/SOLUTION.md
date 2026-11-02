# HCP1228 — Feri to Jolánka Tóth: six kilometres away in a railway uniform

**Status: complete reading, review 1 (REVISE) addressed.** Claude Opus 5.5, 2026-11-02. There is no earlier work on this number. No external plaintext was used: the portal shows Not solved and attaches no transcription or solution, and no published solution of this card was met (no separate web search was made; the orchestrator's register check of 2026-11-02 found no record). The scan file name dates the card 1913-09-07 and calls it jolanka-42.

## Cipher type and key

Hungarian, monoalphabetic substitution with invented graphic signs (register label MASC): the Jolánka family key, transferred unchanged from finished cards HCP1216, 1212, 1213, 1217, 1218, 1243, 1301. Word spaces are mostly kept. Digits are left in clear (6, 1/2, 11).

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | section mark | k | F-like | r |
| six | b | wave | l | right bowl | s |
| opposed bowls | cs | three short strokes | m | gamma/corner | t |
| short + long stroke joined/close | d | two short strokes | n | plain thick cross | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross + | f | tall stroke + short tick | h / p | descender with hook | y |
| open loop with descender | g | dotted crossed curve | i | curled crossed diagonal | z |
| inverted T | j | | | | |

Marks over a sign: two dots give ö/ü, a tick or dot gives á/é and the like. gy and ny are written as g + y and n + y on this card. On this card the signs for c alone, q, w, x do not occur.

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1228/work/decode.py
```

It checks the SHA-256 of all four image files, decodes `work/ledger.txt` (one token per written sign: 27 rows plus 6 rows round the stamp) and prints the literal text and `work/normalized.txt`. The ledger is a manual transcription from enlarged crops of the un-converted scan in `work/hires/`, made with the family key in mind, so it is not blind.

## Literal decipherment (as printed by the command)

```
01 szeretet edes egyetlen remenyem
02 kivanom hogy a legjobb egesség
03 ben talalja soraim. az éjel voltam
04 magához közel csak 6 kilométer ta      ("gá" interlinear)
05 volságra de sajnos épen anyit ert
06 mint ha ot se lettem volna mert
07 nem láthattam de jobban van ez
08 igy mert ha elmetem volna csak
09 kellemetlen let volna maganak
10 [cancelled] eben a vasuti ruhaban va
11 lo l.átas majd lehet hogy meg
12 virad meg enneke is valaha
13 azt tartom hogy türöké. es
14 szenvedöké a menyeknek országa
15 hát én is var[o]k varok még a viszont
16 látásörömeit élvezhetem
17 hana ha lme[n][t]em volna ara akar
18 hogy haragudot volna is rám
19 bementem volna mert nem
20 tudtam volna ellentalni
21 vagyaimnak. mar 1/2 11kor pesten
22 voltam anyi volt az egész
23 othonlétem hogy megnéz
24 te szüleimet egessegesek ézel
25 bezrom soraim maradok
26 sirig hü kedvesse és imado
27 ja feri
stamp: csokol / ja szam / talan / sz[o][r] / ima[d]o / ja feri
```

## Hungarian (normalized)

Szeretett édes egyetlen reményem! Kívánom, hogy a legjobb egészségben találja soraim. Az éjjel voltam magához közel, csak 6 kilométer távolságra, de sajnos éppen annyit ért, mintha ott se lettem volna, mert nem láthattam. De jobban van ez így, mert ha elmentem volna, csak kellemetlen lett volna magának [törölt szó] ebben a vasúti ruhában való látás. Majd lehet, hogy megvirrad még énnek[em] is valaha. Azt tartom, hogy tűrőké és szenvedőké a mennyeknek országa. Hát én is várok, várok, míg a viszontlátás örömeit élvezhetem. Hanem ha [e]lmentem volna arra, akárhogy haragudott volna is rám, bementem volna, mert nem tudtam volna ellentállni vágyaimnak. Már 1/2 11-kor Pesten voltam, annyi volt az egész otthonlétem, hogy megnéztem szüleimet, egészségesek. Ezzel bezárom soraim. Maradok sírig hű kedvese és imádója, Feri.

Under the stamp: Csókolja számtalanszor imádója, Feri.

Unenciphered: the address (Őnagysága Tóth Jolánka úrleánynak, Jász Árokszállás) and the printed picture side (Szerelmi üzenet. Halló! Ki beszél? Kedvesed!).

## English

My beloved sweet only hope! I wish that these lines find you in the best of health. Last night I was close to you, only 6 kilometres away, but sadly it was worth just as much as if I had not been there at all, because I could not see you. But it is better this way, because if I had gone, it would only have been unpleasant for you [cancelled word] to see me in this railway uniform. Perhaps one day the dawn will come for me too. I hold that the kingdom of heaven belongs to those who endure and suffer. Well, I too wait, I wait, until I can enjoy the joys of seeing you again. But if I had gone that way, however angry you might have been with me, I would have gone in, because I could not have resisted my longing. By half past ten I was already in Pest; that was all there was to my stay at home, that I looked in on my parents, they are well. With this I close my lines. I remain, faithful unto the grave, your sweetheart and adorer, Feri.

Under the stamp: Your adorer Feri kisses you countless times.

## Slovak

Moja milovaná sladká jediná nádej! Želám si, aby Vás tieto riadky našli v najlepšom zdraví. Minulú noc som bol blízko Vás, len 6 kilometrov ďaleko, ale žiaľ, malo to takú cenu, akoby som tam vôbec nebol, lebo som Vás nemohol vidieť. Ale je to takto lepšie, lebo keby som bol išiel, bolo by Vám len nepríjemné [prečiarknuté slovo] vidieť ma v tejto železničiarskej rovnošate. Možno raz svitne aj mne. Tvrdím, že trpezlivým a trpiacim patrí nebeské kráľovstvo. Veď aj ja čakám, čakám, kým si budem môcť vychutnať radosti opätovného stretnutia. Ale keby som bol išiel tam, nech by ste sa na mňa hnevali akokoľvek, bol by som vošiel, lebo by som nebol vedel odolať svojim túžbam. Už o pol jedenástej som bol v Pešti; to bol celý môj pobyt doma, že som pozrel rodičov, sú zdraví. Týmto končím svoje riadky. Zostávam Vám do hrobu verný milý a ctiteľ, Feri.

Pod známkou: Bozkáva Vás nespočetnekrát Váš ctiteľ Feri.

## Uncertainties (all disclosed)

Readings that rest on word sense, not on sign shape alone:

1. **Row 4 `ta`**: the last sign but one looks like F (r) with a heavy second arm, and the printed divider crosses near it. It is read t because *kilométer tá|volságra* is the only sense. r would give nothing.
2. **Row 7 `de`**: the first sign is the tall + tick h/p shape, not the usual d. Read d from sense, as on HCP1216 row 5. The alternative *hej* (with one j shared) does not change the meaning.
3. **Row 5 `épen`, row 21 `pesten`**: p against h from sense, as usual in this family. In row 5 the sign is heavily inked.
4. **Row 12 `enneke`**: the signs are clear (e n n e k e). Normalized *énnek[em]* ("for me too"), which assumes a dropped m; *ennek is* with a stray e would give nearly the same sense. *virad* is taken as *megvirrad* (figurative: "the day will dawn").
5. **Row 13–14 `türöké. es szenvedöké a menyeknek országa`**: the signs are clear. The normalization to *mennyeknek országa* only doubles the n, as with `anyit` and `anyi`. The ending -ké could be mistaken for a question particle, but the phrase reads naturally as "belongs to those who endure and suffer".
6. **Row 15 `hát én is`**: the sign shapes decide it: h, two bars (a), gamma (t), three bars (é), n. The accent on the a is faint, but the bar count does not depend on it. **`még`** in the same row is normalized as dialect *míg* ("until"). Sense without it is less good.
7. **Row 17 `hana ha lme[n][t]em`**: the signs of *hana* are firm and the spacing is as read (for the blot see item 8). Normalized *hanem ha [e]lmentem*. This is the weakest normalization on the card: *hana* for *hanem* is assumed, and an e is supplied. The following clause fixes the meaning.

Restorations (physically hidden signs):

8. **Row 15, first `var[o]k`**: the fourth sign lies under a pale blot; only a stub on the left, a hook on the right and a tail below survive. They fit the loop o, and the same word follows at once in clear. **Row 17 `lme[n][t]em`**: the n and t lie under a wet blot. The first stroke of n is firm and the second ghostly; of t only the top arm is firm. Both fit, and the same verb form stands in row 19 and, with `elmetem`, in row 8.
9. **Stamp row 4 `sz[o][r]`** and **row 5 `ima[d]o`**: the F arms and a pale stem of the r are visible outside the right side of the printed triangle; the o lies on the printed monogram and only a loop-like bowl can be made out; the d is damaged. The two bars in the stamp disc are read as the writer's a of row 5, though they could be part of the print. The words are fixed by *szám-talan-szor*, and *imádója Feri* in rows 26–27.

Other points:

10. **Row 10**: the opening word is struck out heavily with two lines, about 5 or 6 signs. It is not read and has no effect on the sentence. It ends in a v-like shape that may be a sign under the strike. The comma-like mark just below that shape is not punctuation: it is the accent of the á of row 11 below.
11. Writer spellings normalized: *szeretet, éjel, ot, let, ara, epen, othon, haragudot, ézel* (single for double consonant); *elmetem* (n omitted); *bezrom* (á omitted); *megnézte* (the m of *megnéztem* omitted); *egesség* and *egessegesek* (for *egészség*); *anyit*, *anyi*, *menyeknek* (single n, for *annyit*, *annyi*, *mennyeknek*); *ellentalni* (*ellentállni*, for *ellenállni*); *kedvesse* (doubled s); *eben* (*ebben*). Accents are shown only where a mark is visible; the rest are supplied.
12. Two small written dots have no text value and are kept as `.` in the ledger: after the first letter of *l.átas* in row 11, and after *türöké* in row 13.
13. The postmark is mostly illegible; the scan name, not the postmark, gives the date 1913-09-07. Interpreting Feri as a railway employee rests on *ebben a vasúti ruhában*. No identification beyond the first name is claimed.

## Why it is correct

- The family key, unchanged, turns all signs of 27 rows and the stamp rows into Hungarian. The only unread item is the writer's own cancelled word.
- The text is continuous and coherent, with formal third-person address (*találja, magának, haragudott volna*) and the family's closing formula (*sírig hű kedvese*). Long words decode without forcing: *egészségben, távolságra, kellemetlen, viszontlátás örömeit, ellentállni vágyaimnak, szüleimet*.
- The digits in clear agree with the words around them (*6 kilométer*, *1/2 11-kor*).
- Repeated words decode the same: *volna* ×7, *mert* ×3, *hogy* ×5, *soraim* ×2, *imádója Feri* ×2.

## Response to review 1

Verdict REVISE, seven findings. All are accepted and fixed. I rechecked findings 1 to 5 on the reviewer's crops and my own (`work/crops/rv_r11_13.png`, `rv_dots.png`). After the fixes `python3 -I ciphers/hcp-1228/work/decode.py` passes all four hash checks and prints the literal block above.

1. **Row 15 `hát én is` (major): fixed.** On `review/work/z15a.png` the second sign has two bars and a pale tick above, and the fourth has three bars and a clear accent. Ledger now `H A' T / E' N`. Normalized text, English, Slovak and uncertainty 6 are changed. The new reading also follows the saying before it better, and needs no free rendering.
2. **`anyit`, `anyi` (major): fixed.** Both crops show one pair of strokes between a and y. I had supplied the second n from the expected word. The ledger now follows the card, and both spellings are in uncertainty 11. The normalized text keeps *annyit*, *annyi*.
3. **Row 14 `menyeknek` (minor): fixed.** The disputed sign ends in the left hook of k, as `review/work/gk.png` shows against eight g signs. Ledger and uncertainty 5 are corrected.
4. **Undisclosed restorations (minor): fixed.** Row 17 n and t and stamp row 4 o are now marked `?` in the ledger and print in brackets. Items 7, 8 and 9 are reworded, and item 9 also records the open question about the two bars in the stamp disc.
5. **Written dots (minor): fixed.** Both dots are recorded in the ledger and described in item 12. The row 11 dot stands at the base of the line after the wave, inside the word, so it is stray. The review's dot "after the third sign" is this one. The tick that looks like a comma under the struck word of row 10 is the accent of the same á, noted in item 10.
6. **Counts (minor): fixed.** *mert* ×3, *hogy* ×5, confirmed against the rows printed above (mert 6, 8, 19; hogy 2, 11, 13, 18, 23).
7. **Slovak wording (minor): fixed**, with the reviewer's sentence.

The cipher type, the key and the sense of the card are unchanged. One clause changes ("all week" becomes "well, I too"), and the other changes are spelling and disclosure. The reading is not substantially changed, so this goes to FINAL, not DONE2. Two points stay open, as the review says: the postmark date, and whether *hana* means *hanem*.
