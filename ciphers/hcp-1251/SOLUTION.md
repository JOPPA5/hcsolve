# HCP1251 — Feri to Jolánka Tóth, Easter Sunday 1914: "only death can part us"

**Status: complete reading, revised after review 1 (verdict REVISE).** Claude Opus 5.5, 2026-11-01. No earlier work existed on this number; the key is the shared Jolánka family key from finished sister cards (mainly HCP1216, reviewed and FINAL). The portal shows status Not solved and attaches no transcription or solution, and no published solution of this card turned up. The transcription was made by me from the scan; it was not blind to the family's vocabulary.

Card: picture postcard, cancelled BUDAPEST 914 APR 12 (Easter Sunday 1914), addressed in clear to "Szép reményű Tóth Jolánka úrleánynak, Jászárokszállás". The picture side has only a printed verse (*Csendes álmok éjjelén…*), no cipher. The cipher is on the address side: 25 rows in the left half, rows 26–28 across the full width along the bottom edge, and seven rows in the stamp box, uncovered when the stamp was soaked off.

## Cipher type and key

**Register type: MASC + Steganography** (2026-11-03: the stamp box carries a hidden closing in the cipher signs, written under the stamp; see "Stamp-box message (2026-11-03)").

Hungarian, simple monoalphabetic substitution with invented graphic signs (Jolánka family). `work/key.json` lists the sign classes; they are those of HCP1216 with these variants on this card:

- **v** is a peak with a long left leg (*válaszolni, levelére, húsvét, vagyon*).
- **d** appears both as a joined stroke and tick and as the crossing "4" shape (*édes, de*).
- **l** is sometimes a plain chevron without its hook (*lapot, levelére*).
- **k** is the section-mark S. **g** is the hooked S; a large S stands for g in *boldo|gok* (row 22) and a large double-looped form for g in *drágám* (row 16).
- **i** is often written without its dot, which then looks like o (*Ilonka, mostani, nem illik, annyira, sietek*). These calls rest on word sense.
- **gy** is written as g + y, not as one joined sign.

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1251/work/decode.py
```

It checks the SHA-256 of both source images and both originals, reads `work/ledger.txt` (770 signs, one character per written sign), checks that every character is a sign class in `work/key.json`, prints the literal rows, and prints `work/normalized.txt`. **It does not apply a key:** the ledger is a manual transcription written directly in plaintext letters (not OCR), so `key.json` is descriptive and the command validates and prints rather than deciphers. The independent check is the reviewer's sign-class transcription of nine rows decoded with HCP1216's `graphic-key.json`.

## Literal decipherment

```
01 szeretetedesjolankambe               15 atervehogyszetvalasszonben
02 csessoraitmegkahtammelyet            16 nünketugyedragamaznemfog
03 köszönömszehenedesem                 17 nekisikerülnimertnincsaza
04 enküldtemmaganakegylahot             18 hatalomamielvaszonegymas
05 multlevelerejaszberenybe             19 tolcsakahalaldeezthagyjuk
06 m[a]jdmegfogjakahniilon              20 utoljaraedesembarmijen
07 katoldemostsietekvala                21 szegenyekleszünkisdeboldo
08 szolnijelensorairaminde              22 gokesnekemnemkelsemmimas
09 ne[k]elotkivanokkellemhusv{o}        23 nemad[o]msemenyivagyon
10 tiünneheketremelemajöhu[s]vet        24 ermagatmertavagyonazel
11 kelemesebesboldogableszmint          25 fogydemagaedesmegmarad
12 amostaniigazavanedesemhogy           26 kösznömmaganakedesemhogyanyiraönfelaldozódere
13 aszülőnekmindentsz[a]badcsak         27 melemhogyerrenemleszszükségemmertmindigfogokanyi[t]
14 nemillikestudomhogyaz                28 keresnihogyszenyenegycsaladoteltartsakcsakez

Stamp box: S1 [is]tenve  S2 {e}ledese[m]  S3 aboldog  S4 viszont  S5 latasra  S6 imado[ja]  S7 fer[i]
```

`h` stands for the h/p sign, `[ ]` for a restored sign, `{ }` for a doubtful one.

## Hungarian (normalized)

Szeretett édes Jolánkám! Becses sorait megkaptam, melyet köszönöm szépen, édesem. Én küldtem magának egy lapot múlt levelére Jászberénybe, majd meg fogja kapni Ilonkától. De most sietek válaszolni jelen soraira. Mindenek előt[t] kívánok kellem[es] húsvéti ünnepeket. Remélem, a jö[vő] húsvét kellemesebb és boldogabb lesz, mint a mostani. Igaza van, édesem, hogy a szülőnek mindent szabad, csak nem illik, és tudom, hogy az a terve, hogy szétválasszon bennünket. Ugye, drágám, az nem fog neki sikerülni, mert nincs az a hatalom, ami elválasszon egymástól, csak a halál. De ezt hagyjuk utoljára. Édesem, bármilyen szegények leszünk is, de boldogok, és nekem nem kell semmi más. Nem adom semennyi vagyonér[t] magát, mert a vagyon az elfogy, de maga, édes[em], megmarad. Köszönöm magának, édesem, hogy annyira önfeláldozó, de remélem, hogy erre nem lesz szükségem, mert mindig fogok annyit keresni, hogy sze[ré]nyen egy családot eltartsak. Csak ez.

Isten vele, édesem, a boldog viszontlátásra! Imádó[ja] Feri.

## English

My beloved sweet Jolánka! I have received your esteemed lines, for which I thank you very much, my sweet. I sent you a card to Jászberény in reply to your last letter; you will get it from Ilonka. But now I hasten to answer your present lines. First of all I wish you a pleasant Easter. I hope next Easter will be more pleasant and happier than this one. You are right, my sweet, that a parent may do anything, it is just not proper, and I know that the plan is to part us. Surely, my darling, that will not succeed, because there is no power that could part us from each other, except death. But let us leave this for last. My sweet, however poor we may be, we shall still be happy, and I need nothing else. I would not give you up for any amount of wealth, because wealth runs out, but you, my sweet, remain. I thank you, my sweet, for being so self-sacrificing, but I hope I shall not need that, because I shall always earn enough to keep a family modestly. That is all.

God be with you, my sweet, until our happy reunion! Your adorer, Feri.

## Slovak

Moja milovaná, sladká Jolánka! Vaše vážené riadky som dostal, za čo veľmi pekne ďakujem, zlatko. Poslal som Vám do Jászberénya lístok ako odpoveď na Váš minulý list; dostanete ho od Ilonky. Ale teraz sa ponáhľam odpovedať na Vaše terajšie riadky. Predovšetkým Vám želám príjemnú Veľkú noc. Dúfam, že budúca Veľká noc bude príjemnejšia a šťastnejšia ako táto. Máte pravdu, zlatko, že rodič môže všetko, len sa to nepatrí, a viem, že plánom je rozdeliť nás. Však, drahá, to sa nepodarí, lebo niet takej moci, ktorá by nás od seba rozdelila, len smrť. Ale to nechajme nakoniec. Zlatko, nech budeme akokoľvek chudobní, predsa budeme šťastní a ja nepotrebujem nič iné. Nedám Vás za žiadne bohatstvo, lebo bohatstvo sa minie, ale Vy, zlatko, zostanete. Ďakujem Vám, zlatko, že ste taká obetavá, ale dúfam, že to nebude potrebné, lebo vždy zarobím toľko, aby som skromne uživil rodinu. Len toľko.

S Bohom, zlatko, do šťastného zhľadania! Váš ctiteľ, Feri.

## Uncertainties

**Readings that rest on context, not on a clean sign**

1. **Two bars against three (a/e).** The third bar is often missing or lost, so the ledger's a/e is the chosen value. Word sense decides at least *de* (row 7), *sietek* (two faint bars), *igaza*, *a vagyon* (row 24, two bars crossed by a water run that continues through neighbouring rows; it is not an r), *de maga* and *magának* (row 26). Row 15 *szét*: the first vowel is two bars on the card, kept as e from sense. Row 20 *bármijen*: two bars and a small dot below, read a; at most an e with a stunted third bar.
2. **Rows 2 and 7, F against gamma.** In *kaptam* the t is a heavy, over-inked sign with a tick, close to r; *sietek* has a gamma touched by cancel specks. Row 15 *terve*: the first sign is an F-like form with a small foot, read t. All three are read from sense.
3. **h/p near-homograph.** Every `h` in the ledger was resolved by the word: *kaptam, szépen, lapot, kapni, ünnepeket* are p; *húsvét, hogy, hatalom, halál, hagyjuk* are h.
4. **Dropped dot on i**: see the key section. Row 10 *ünnepeket*: the fourth of the four strokes carries a horizontal top bar, so it looks like a stroke plus gamma; *nn* rests on word sense. Row 10 *jö*: the accent is a dot plus a longer tick and may be ő; *a jő húsvét* would need no omitted *-vő*.
5. **Row 28, *sze[ré]nyen*.** The signs are clearly s z e n y e n, literal *szenyen*. I normalize to *szerényen* ("modestly"), assuming *ré* was omitted; *szegényen* ("poorly") would also fit the signs equally well and differ little in sense.

**Restorations (signs hidden or only traces seen)**

6. Row 6 *m[a]jd*: the a lies under the cancel ring; only green traces show there.
7. Row 9 *ne[k]e-*: the k of *mindenek* lies under the ring at the left edge; only traces show.
8. Row 9 end, *húsv{o}*: the sign in the cancellation where é is expected is loop-like with a long arm, not bars. Normalized *húsvéti* from sense; possibly a mis-stroke.
9. Row 10 *hu[s]vet*: the sign between ú and v is overlapped by the postmark; a right bowl shows under it, so s is a weak reading supported by sense.
10. Row 13 *sz[a]bad*: this is a correction with two overwritten blocks: the z with bars struck over its right side, then a box of several strokes closed by top and bottom bars. Which strokes are the intended a cannot be determined. The word is safe from sense and the following six = b, and the ledger records one `[a]` for the whole box.
11. Row 23 *nemad[o]m*: the o is a smeared blot; the first n is also a heavy blurred sign. *nem adom* is the only sense found; it fits the following clause exactly.
12. Row 27 *anyi[t]*: the t is cut by the card's right edge; its stem and the start of its top bar show.
13. **Stamp box.** The ink is washed out. S1 left of *ten* is under a stamp fragment, so *[is]* is restored from the family's formula *Isten vele* (HCP1216, 1217). S2 has a faint bar sign at the start, kept as `{e}`, and the l is blurred; a final m would lie at the torn edge. The normalized *vele, édesem* is compressed: S1 ends `ve` and S2 reads `{e} l e d e s e [m]`, so the {e} is dropped as a stray and the one e after l serves both the end of *vele* and the start of *édesem*. This is an editorial judgement on a faded line. S3 *boldog* after the b and S5 *ra* are faint. S6 shows *imádó*; *-ja* is not visible and is supplied in normalization. S7 *fer*: the i lies under the printed "…ER" of the stamp remnant.
14. An ink spill near *önfeláldozó* (row 26) and one in *remélem* (row 27) are treated as no sign.

**Writer's spellings kept as written and normalized editorially** (these are on the card, not reading gaps): *szeretet* for szeretett, *előt* for előtt, *kellem* for kellemes, *jö* for jövő (the writer skipped *-vő*; only the h-sign then the ú follow), *kelemeseb*, *boldogab*, *elvászon* for elválasszon, *kel* for kell, *bármijen* for bármilyen, *semenyi*, *vagyonér* for vagyonért, *édes* for édesem (row 25; the literal *édes* could also stand as written, so that restoration is optional), *kösznöm* for köszönöm, *anyira*, *anyit*. Long accents are mostly unmarked and are supplied.

## Why it is correct

- The family key, unchanged apart from the variants above, turns all 28 main rows into continuous Hungarian with no unexplained word. The stamp box gives the family's usual closing.
- The text argues coherently from start to end: thanks, Easter wishes, the parent's plan to part them, the promise to support a family.
- The context fits. The cancellation is Easter Sunday 1914 and the card wishes a happy Easter. Sister cards name the same Feri, the addressee Tóth Jolánka, her cousin Ilonka (HCP1263, 1272; both FINAL) and Berény, read as Jászberény (*Jászberény* here). The signature formula *imádója Feri* is on HCP1301.
- Repeated words decode identically in separate places: *hogy* ×6, *édesem* ×5, *mert* ×3, *vagyon* ×2, *boldog* ×3, *magát/magának* ×3.

## Response to review 1

Verdict REVISE. All nine findings are accepted after I checked the reviewer's crops of the un-converted scan myself. `python3 -I ciphers/hcp-1251/work/decode.py` re-run after the fixes: all 4 hashes OK, 770 signs, output equals the literal table and the normalized text. The sense of the letter is unchanged.

1. **Row 4 `lapot`: fixed.** The colour separation (`review/work/c/l4m.png`) shows the gamma after the o, unbroken, running under the black D of the postmark; nothing follows it. My `b e` were not on the card and my "no t" remark was wrong. Ledger row 4 now ends `egylahot`; normalized *egy lapot múlt levelére Jászberénybe*; the *lapo* spelling note is deleted.
2. **Row 26 phantom k: fixed.** `review/work/c/r26.png` shows one section-mark S between the two-bar and three-bar signs. Ledger `maganakedesem` = *magának, édesem*; *ked[v]esem* and its spelling note are gone; English "my sweet", Slovak "zlatko".
3. **Row 15 and row 20 a/e: fixed.** Both crops show two bars (row 20 with a small dot below). Ledger now `szetvalasszon`, `barmijen`; both false spelling notes removed; both listed under uncertainty 1.
4. **"g sign for k": withdrawn.** On the crops, the finals of *kívánok, fogok, eltartsak* are the ordinary section mark. Removed from this file and `key.json`. The large S for g (row 22) stays; the large g of *drágám* (row 16) is added.
5. **Row 13: fixed** in uncertainty 10 (two overwritten blocks; the ledger's `[a]` stands for the box, and the intended strokes cannot be determined).
6. **Stamp *vele, édesem*: fixed** in uncertainty 13 (the compression is stated).
7. **Counts: corrected** to *hogy* ×6, *édesem* ×5 (recounted on `normalized.txt` after fix 2).
8. **Disclosure points: fixed.** *ünnepeket* nn and *jö/jő* are in uncertainty 4, *hu[s]vet* in 9, *édes[em]* in the spellings note. HCP1263 and HCP1272 had no FINAL when reviewed; both have FINAL now, so the sentence naming them stands and says so.
9. **Reproduction: fixed** by stating plainly that the command validates and prints a ledger already in plaintext letters and applies no key; the `decode.py` docstring says the same. I did not retranscribe by sign class, since the reviewer's independent class-level decode with HCP1216's key already covers nine rows.

One further change of my own, not from the review: the English and Slovak now attach *Jászberénybe* to *küldtem* ("I sent a card to Jászberény in reply to your last letter"). That fits *majd meg fogja kapni Ilonkától* better; the Hungarian word order allows both, and no letter changes.

The changes are limited to the points above (row 4 `b e` to `t`, one k removed in row 26, two vowels), so no second review round is needed; the review itself says so.

## Stamp-box message (2026-11-03)

Stamp-box audit by Claude Opus 5.5 on the un-converted original (`work/hires/…_adr.jpg`), crops in `work/stamp-2026-11-03/` (`box_red2x.png`, `band0-2_red3x.png`, `faint_color3x.png`). The stamp has been soaked off; only torn fragments of its frame remain (top left, right edge, bottom right with the printed "…ER"). Under it are seven rows of writing, **all in the cipher signs; no plain Hungarian**. The faint brownish strokes right of rows S3–S5 look like Latin cursive at first sight, but in colour they are the washed-out continuation of the same sign rows (the *-oldog*, *-ont*, *-sra* ends), not a second plain-text layer.

The message was already read in full in the main sections above (rows S1–S7); this audit re-checked it on new crops and found no change:

- Literal: `[is]tenve | {e}ledese[m] | aboldog | viszont | latasra | imado[ja] | fer[i]`
- Hungarian: *Isten vele, édesem, a boldog viszontlátásra! Imádó[ja] Feri.*
- English: God be with you, my sweet, until our happy reunion! Your adorer, Feri.
- Slovak: S Bohom, zlatko, do šťastného zhľadania! Váš ctiteľ, Feri.

Unread / restored (unchanged from uncertainty 13): *[is]* of S1 under a stamp fragment (restored from the family formula), final *m* of S2 at the torn edge, *-ja* of S6 not visible (supplied in normalization), *i* of S7 under the printed "…ER" of the stamp remnant. No whole clause is unread. The reproduction script was not changed; the stamp rows are in the existing ledger.

Type: hidden writing exists under the stamp, so the card is typed **MASC + Steganography** (register entry type field and report updated today; nothing else in the register line changed).
