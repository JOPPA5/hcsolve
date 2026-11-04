# HCP1250 — Feri to Jolánka Tóth: "you will be my partner", waiting and wishing her a good time tomorrow

**Status: complete reading, small disclosed points only; review 1 verdict ACCEPT, see the response at the end.** Written 2026-11-01 by Claude Opus 5.5 (solver). There is no earlier work on this number. No published solution was found: the portal shows status *Not solved* and attaches no transcription or solution. The key comes from the finished Jolánka family cards; no plaintext of this card was available.

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented graphic signs (MASC): the "Jolánka" postcard family. The key was transferred unchanged from HCP1216; the text is the sender's usual Feri-to-Jolánka letter. All ciphertext is on the address side: 24 rows on the left half (row 24 runs along the bottom edge to the right edge) and 8 rows in the stamp field, where the stamp is gone and the rows stand upright over the printed seal. The picture side has only print (Cigányprímás / Lári-Fári verse).

**Type note (2026-11-03):** the card is now typed **MASC + Steganography**, because part of the message (8 rows, from *Szép kedvesem* to *Feri*) was written in the stamp box, hidden under the stamp, which is now lifted. The key and the reading are unchanged.

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | section mark S or 8 | k | F-like | r |
| six | b | wave | l | right bowl | s |
| opposed bowls | cs | three short strokes | m | gamma/corner | t |
| long stroke + tick | d | two short strokes | n | plain cross x | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross + | f | tall stroke + short tick | h / p | y-sign | y |
| open loop | g | dotted crossed curve | i | tailed cross | z |
| inverted T | j | | | | |

Dots over o/u give ö/ü. *gy* is written with two signs here (open loop + y-sign), *sz* as s + z, *ly* as j. Long-vowel accents are written only now and then: clear ticks stand over bars in row 12 (*hatnánk*), row 15 (*enyém*), row 22 and stamp row 4 (*né-*). The ledger records only ö/ü; the other accents are supplied in normalization, and the ticks that are there agree with it.

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1250/work/decode.py
```

It checks the SHA-256 of the four scans, decodes the sign ledger `work/ledger.txt` (570 signs, one token per written sign) and prints the literal rows and the normalized text `work/normalized.txt`. The ledger is a manual transcription from enlarged crops of the high-resolution address scan; the script decodes tokens and does not read pixels.

## Literal decipherment (as printed by the command)

```
01 edesegyetlenremenyemki         13 idömindenhetegyeszten
02 vanomhogyalegjobbegesseg       14 döesadigtartm{e/i}gaztnem
03 bentalaljasoraimmisajnos       15 mondhatomhogyenyem
04 ritkanvanmostanabajomu         16 vagyörökreesnemvalaszt
05 latastkivanoholnapdejolmu      17 elegymesto[l]semidesaj
06 latgondoljonraismertnel        18 nosmegsokaleszdebez
07 külöznömkelajomulatast         19 unkazistenbenzttertom
08 maganelkülnemtudokmulat        20 mintazenekmondjahogy
09 sagotszereznicsakazfajmert     21 megerjükmeaztazidöt
10 nincsegykicsitkozelebhozam     22 babamteleszelaparom
11 hogygyakrabbantalkoz           23 amitenaligaligvarom
12 hatnanknekemojhoszuaz          24 istenveleedescsokoljaimadojaferi
stamp field: szepkad vesem gondol jonne h[a]ram viszot latasra feri
```

## Hungarian (normalized)

Édes egyetlen reményem! Kívánom, hogy a legjobb egésségben találja soraim. Mi sajnos ritkán van mostanába[n]. Jó mulatást kívánó[k] holnap; de jól mulat, gondoljon rá[m] is, mert nélkülöznöm kel[l] a jó mulatást maga nélkül. Nem tudok mulatságot szerezni, csak az fáj, mert nincs egy kicsit közelebb hozzám, hogy gyakrabban találkozhatnánk. Nekem oly hosszú az idő, minden hét egy esztendő, és addig tart, míg azt nem mondhatom, hogy enyém vagy örökre, és nem választ el egymástól semmi, de sajnos még soká lesz, de bízunk az Istenben, [a]zt tartom, mint az ének mondja, hogy megérjük mé[g] azt az időt, babám, te leszel a párom, amit én alig, alig várom. Isten vele, édes. Csókolja imádója, Feri.

Stamp field: Szép kedvesem, gondoljon néha rám. Viszo[n]tlátásra. Feri.

## English

My sweet only hope! I wish that my lines find you in the best of health. Which, unfortunately, is rare lately. [Or, as a separate sentence: "What, unfortunately, is rare lately."] I wish you a good time tomorrow; but when you are having a good time, think of me too, because I must do without a good time, without you. I cannot find any amusement; only this hurts, that you are not a little closer to me, so that we could meet more often. For me the time is so long, every week a year, and it will last until I can say that you are mine forever and nothing separates us from each other. But unfortunately that will be long yet; but we trust in God, I hold, as the song says, that we shall yet live to see that time, my darling, when you will be my partner, which I can hardly, hardly wait for. Farewell, sweet one. Your adorer Feri kisses you.

Stamp field: My beautiful darling, think of me sometimes. Until we meet again. Feri.

## Slovak

Moja sladká jediná nádej! Želám si, aby Vás moje riadky našli v najlepšom zdraví. Čo je, žiaľ, teraz zriedkavé. Želám Vám zajtra dobrú zábavu; ale keď sa budete dobre zabávať, myslite aj na mňa, lebo ja sa musím zaobísť bez dobrej zábavy, bez Vás. Neviem si nájsť zábavu, bolí ma len to, že nie ste trochu bližšie ku mne, aby sme sa mohli stretávať častejšie. Mne je čas taký dlhý, každý týždeň je ako rok, a potrvá to dovtedy, kým nebudem môcť povedať, že si navždy moja a že nás od seba nič neoddelí. Ale žiaľ, to bude ešte dlho trvať; no dúfame v Boha, ja si myslím, ako hovorí pieseň, že sa ešte dožijeme toho času, moja milá, keď budeš mojou družkou, čoho sa sotva, sotva dočkám. S Bohom, drahá. Bozkáva Vás Váš ctiteľ Feri.

Pole známky: Moja krásna drahá, myslite na mňa niekedy. Dovidenia. Feri.

## Uncertainties

Restorations of hidden signs (two):

1. **Row 17, the l of *egymástól*.** The sign after *t o* lies under a heavy dark ink blot. It has about three legs joined at the top, so the pixels cannot choose between a wave and three strokes (m) or similar. The l rests on the word alone: only l makes a word (*nem választ el egymástól semmi*). Disclosed restoration, token `[L]`.
2. **Stamp row 5, the a of *ha*.** It falls on the printed seal and shows only as faint pink bars among the orange print. Restored from *néha rám*, token `[A]`.

Calls resting on word sense:

3. **h/p sign**: p in *holnap* (row 5), *párom* (row 22), *szép* (stamp row 1); elsewhere h (*hogy*, *hét*, *hatnánk*, *hosszú*, *hol-*, *ha*). Before the p of *párom* stands a separate wedge-shaped blob touching the tall stroke, then the tall stroke and the short stroke. The blob is unexplained (a blot or a cancelled sign?) and is not a token in the ledger; *a párom* stands without it.
4. **Row 14 `m{e/i}g`.** The vowel is overwritten: three bars with a long crossing stroke, apparently e corrected to i (or the reverse). It is normalized *míg* ("until"), which the sentence *addig tart, míg…* requires. Read as the plain particle *meg*, the sentence would be weak.
5. **d/n**: *mondhatom*, *mondja*, *gondoljon*, *minden* have the d as a two-stroke sign with a short first stroke, close to n. The word settles each one.
6. **Row 18–19 `bez|unk`** has three bars (e) after the b, not the dotted i: literal *bezunk*, normalized *bízunk*. Word sense only; no other word fits *…az Istenben*.
7. **Row 19 `[a]zt`.** After *Istenben* the card has only z t. The a is not on the card (writer's omission) and is supplied.
8. **Row 21 `me azt`**: normalized *mé[g] azt*; the g is not on the card. HCP1216 has the same omission (*me[g] most*).
9. **Row 5 `kivano`**: normalized *kívánó[k]*, reading the final k as omitted. *Kívánom* (m omitted) gives the same sense.
10. **Row 4 `mi sajnos…`** (rows 3–4): *Mi sajnos ritkán van mostanában* can attach to the health wish ("which is rare with us lately") or stand alone. All signs are clear; the sentence division is editorial, and so is the division before *jó mulatást* and after *holnap*. *de jól mulat* is read as "but when you are having a good time"; the conditional force is my interpretation.
11. **Row 2 and row 7, the m after o** (*kívánom*, *nélkülöznöm*) shows three strokes plus one short extra stroke at both places. Treated as m; no word uses the extra stroke.
12. **Row 24 `imádója`**: the i here looks more like a dotted loop than the crossed i; the word decides it.
13. **Row 23 `amit`**: the t has a rounded, hooked form, unlike the usual corner. Word sense.
14. **Writer's spellings normalized**: *kel* → kell, *közeleb* → közelebb, *hozam* → hozzám (the a sign, so not *hozom*), *talkozhatnank* → találkozhatnánk (*ál* omitted across rows 11–12), *ojhoszu* → oly hosszú, *adig* → addig, *mostanaba* → mostanába[n] (no n on the card; colloquial -ba for -ban is also possible), *mest-* → *mást-* (three bars for a in *egymástól*), *semi* → semmi, *tertom* → tartom (three bars for a), *enek* → ének, *szep kadvesem* → szép kedvesem (see item 18), *jonne* → jon né (word break inside the row), *viszot* → viszo[n]t (n not on the card).
15. Row 1 has a stray dot after *ki*; it is treated as a speck. Most accents are not written and are supplied (see the key section for those that are written).
16. *Isten vele* is formal, and the letter mixes formal address (*találja, gondoljon*) with *te leszel a párom* inside the reported song line. I keep that as written. The song itself is not identified.
17. **Row 6 `rais`** is what is written: no sign stands between a and i. It is normalized *rá[m] is* ("of me too"), taking the m as one more dropped letter, because *mert* then keeps its usual sense and the stamp field has *gondoljon néha rám*. The alternative is the literal *rá is* ("of this too, that…"), which stretches *mert* to "that". The signs are the same either way.
18. **Stamp row 1, the vowel after k.** The sign is smudged: one upper bar, then a thick lower mass that may be one bar or two merged. It is tokenized as a (two bars) but cannot be told from e (three bars). So *kadvesem* may be a writer's error or just a smudged *kedvesem*; the word stands either way.
19. **Row 19, the s of *Istenben*** has a hollow, abraded top and reads as a right bowl only with some allowance. Word sense.
20. **Row 4, punctuation.** A short oblique ink stroke stands between the final a of *mostanaba* and the j of *jó* (about x 1245, y 333 in the hi-res scan). It is not a ledger token. It is probably a comma, and it supports the sentence break there. The rest of the punctuation is editorial.

Address side, not enciphered: *Szépremény[ű] Tóth Jolánka úrleánynak, Jász Árokszállás*. The end of the first word runs into a pink smear; HCP1252 and HCP1253 have the full *Szépreményű*. The date 1913-06-16 comes from the portal file name; the cancellation is only partly legible.

## Why it is correct

- The HCP1216 key, unchanged, turns all 570 signs into Hungarian. Only two signs are restored, and no sign is left without a value.
- No plaintext of this card was known beforehand, and whole long stretches came out unforced: *kívánom, hogy a legjobb egésségben találja soraim*; *nincs egy kicsit közelebb hozzám, hogy gyakrabban*; *nem választ el egymástól semmi*; *megérjük még azt az időt*.
- Repeated words decode identically at different places (*hogy* ×4, *mulat-* ×4, *mert* ×2, *alig* ×2, *idő* ×2, *Feri* ×2).
- The content fits the family: same opening health wish and closing formulas (*Isten vele, viszontlátásra, csókolja, imádója, Feri*), same missing-letter spelling habits.

## Response to review 1

Verdict ACCEPT, eight minor findings. I rechecked the reviewer's zooms (`review/work/crops/z4.png`, `z6.png`, `z17.png`, `z19.png`, `z22.png`, `ys.png`) and agree with all eight. No sign value and no ledger token changed; the literal rows are the same.

1. **Row 6 alternative: fixed, adopted.** Normalized text now has *gondoljon rá[m] is, mert…*, in `work/normalized.txt` and here, with English and Slovak changed. The literal *rá is* reading is kept as the disclosed alternative (uncertainty 17).
2. **Row 4 `mostanaba`: fixed.** Normalized now *mostanába[n]*, listed in item 14. The oblique stroke is real ink on z4; disclosed as a probable comma (uncertainty 20).
3. **Row 17 overclaim: fixed.** The blot shows about three joined legs; the wording of restoration 1 no longer says only a wave is compatible and states that the l rests on the word.
4. **Stamp row 1: fixed.** The sign is too smudged to count the bars. Item 14 no longer states a writer's error as fact; see uncertainty 18.
5. **Row 22 p: fixed.** The separate wedge is clear on z22; described in uncertainty 3.
6. **Row 19 s: fixed.** Added as uncertainty 19.
7. **Accents: fixed.** The key section now names the clear ticks.
8. **Translations: fixed.** "with us" and "u nás" removed; Slovak now *čoho sa sotva, sotva dočkám*; the row 6 sentence changed in both.

The reproduction command was re-run after these edits: four hashes OK, 570 signs, and the normalized text prints the two changed words.

## Stamp-box message (2026-11-03)

Stamp-box audit, Claude Opus 5.5, ordered by the human on 2026-11-03. The stamp box at the top right of the address side was cropped again from the original scan (work/hires/..._adr.jpg) at about 2x of the hi-res file (about 7x the source/ image), in colour and as an auto-contrast green channel (work/stamp-2026-11-03/stamp_rgb.png, top_g.png, bot_g.png). The stamp is **lifted** and the box holds **8 upright rows in the cipher signs**, written over the printed seal. There is no plain Hungarian in the box. The sender hid this part under the stamp, so the card is steganographic as well as enciphered.

The message was already read in full on 2026-11-01 (the "stamp field" lines above, tokens in work/ledger.txt). The new crops agree with it sign by sign: row 1 *szepkad*, row 2 *vesem*, rows 3 to 5 *gondol jon ne*, row 6 *h[a]ram*, row 7 *viszot*, row 8 *latasra*, last row *feri*. Nothing new was read and nothing changed.

- Literal: `szepkad vesem gondol jonne h[a]ram viszot latasra feri`
- Hungarian: Szép kedvesem, gondoljon néha rám. Viszo[n]tlátásra. Feri.
- English: My beautiful darling, think of me sometimes. Until we meet again. Feri.
- Slovak: Moja krásna drahá, myslite na mňa niekedy. Dovidenia. Feri.

Still uncertain, as before: the a of *ha* (row 5/6) lies on the seal and is restored (uncertainty 2); the vowel after k in row 1 is smudged, a or e (uncertainty 18); the n of *viszont* is not written. No clause is unread. The reproduction script already covers these rows and was not changed.
