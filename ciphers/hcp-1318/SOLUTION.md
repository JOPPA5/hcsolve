# HCP1318 — Feri to Jolánka Tóth: arrived safely, the parcel, "everyone believed I am a soldier"

**Status: complete reading; review 1 verdict REVISE, findings addressed (see the last section).** Solver: Claude Opus 5.5, 2026-10-30. No earlier work exists on this number. The portal shows *Not solved* with no attached transcription or solution; no published solution was found or used. The ledger was made by hand from the pixels, with word expectations in mind (not blind).

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented signs: the Jolánka postcard family, key taken unchanged from finished card HCP1216 (also 1212, 1213, 1217, 1218, 1243, 1301).

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | section mark (S / 8 forms) | k | F-like | r |
| six | b | wave | l | right bowl | s |
| opposed bowls | cs | three short strokes | m | gamma (arm sometimes detached) | t |
| tick + long stroke | d | two short strokes | n | plain X | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross + | f | long stroke + tick at right | h / p (here also d, see 1) | low looped sign | y |
| ς-shaped descender | g | dotted crossed curve | i | X with long arm or tail | z |
| inverted T | j | | | | |

*gy* is written here as two signs (g + y), *sz* as s + z. Accents are marks over the base sign; only the acutes on e, and the two dots of *többet*, were clearly seen.

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1318/work/decode.py
```

It checks the SHA-256 of all four image files, renders `work/ledger.txt` (398 signs, one token per written sign: 21 main rows and 7 rows in the space left under the removed stamp) and prints the normalized text `work/normalized.txt`.

## Literal decipherment

`[x]` = seen only through the stain or hidden; `x?` = value rests on word sense.

```
01 kedvesjolankamtudatom          12 magahozacsomakotat
02 hogyszerencsésenmegér          13 adtamsand?ornakabéla
03 keztem.ijenkorérzém            14 valnembeszelhetem
04 csakhogymitvesztek             15 mertnemvoltidom
05 enjolankambaelijenkor          16 d?emostnemirok
06 ismikorelkelvalaunk            17 többetmertmeral
07 egymast?[o]lszeretném          18 mosvagyokisten
08 szivemé[r][z]elmeitbeol        19 velédesem
09 tanieze[n][é]desjolankamszi    20 mindenkielhitte
10 vebéakorjolankamisugy          21 hogykatonavagyok
11 vonzodnah?ozammint?én          under stamp: csokol / lom / szam / talan / szor / imado / jaferi
```

## Hungarian (normalized)

Kedves Jolánkám! Tudatom, hogy szerencsésen megérkeztem. Ilyenkor érzem csak, hogy mit vesztek én Jolánkámba[n] el. Ilyenkor is, mikor el kell válnunk egymástól, szeretném szívem érzelmeit beoltani ezen édes Jolánkám szívébe, akkor Jolánkám is úgy vonzódna hozzám, mint én magához. A csomagot átadtam Sándornak, a Bélával nem beszélhettem, mert nem volt időm. De most nem írok többet, mert álmos vagyok. Isten vele, édesem. Mindenki elhitte, hogy katona vagyok.

Under the stamp: Csókolom számtalanszor. Imádója Feri.

## English

My dear Jolánka! I let you know that I have arrived safely. Only at such times do I feel what I am losing in my Jolánka. Even at times like this, when we must part from each other, I would like to implant the feelings of my heart into this sweet Jolánka's heart; then my Jolánka too would be as drawn to me as I am to you. I handed the parcel over to Sándor; I could not speak with Béla, because I had no time. But I will not write more now, because I am sleepy. God be with you, my sweet. Everyone believed that I am a soldier.
Under the stamp: I kiss you countless times. Your adorer, Feri.

## Slovak

Moja milá Jolánka! Oznamujem Vám, že som šťastne docestoval. Až v takých chvíľach cítim, čo v mojej Jolánke strácam. Aj v takejto chvíli, keď sa musíme rozlúčiť, by som chcel vštepiť city svojho srdca do srdca tejto sladkej Jolánky; potom by aj moja Jolánka ku mne tak inklinovala, ako ja k Vám. Balík som odovzdal Šándorovi, s Bélom som sa nemohol porozprávať, lebo som nemal čas. Ale teraz už viac nepíšem, lebo som ospalý. S Bohom, moja sladká. Všetci uverili, že som vojak.
Pod známkou: Bozkávam Vás nespočetnekrát. Váš ctiteľ Feri.

## Uncertainties

Signs are transcribed as written; the normalization is editorial.

Signs that rest on word sense or are hidden:

1. **h/d form.** The tall stroke with a tick at right is h (*hogy*, *beszélhetem*, *elhitte*), but must be d in *Sándornak* (row 13) and *de* (row 16); the regular d has the tick at left (*tudatom*, *vonzódna*, *adtam*, *időm*, *imádó*). HCP1216 row 5 has the same *de*. Literal *sanhornak*, *hemost* would not be words.
2. **Stain, row 7:** one sign between *t* and *l* is covered; restored as o (*egymástól*). In the background-subtracted green channel a faint top arc fits a cursive o, weakly. The t is a gamma with a tiny stub under its arm. If the stub were a real bar it would be F, giving *egymásról* ("about each other"), which does not fit *el kell válnunk*.
3. **Stain, row 8:** after the first bars of *é* (visible at the stain edge) two signs are covered; restored as r, z (*érzelmeit*), the only fitting word before *-elmeit*. This is two letters, not one, and is disclosed as such. In the background-subtracted green channel a horizontal arm with a stem dropping left is visible, consistent with F (r), and further right a strong vertical consistent with z, though the z could not be identified from that stroke alone.
4. **Stain, row 9:** two faint strokes (n of *ezen*) and two faint bars (a three-bar e, third bar not seen, read é of *édes*) show through the stain; the d after them shows its long stroke, and its left tick is visible inside the stain in the enhanced crop. `[e']` prints é, a contextual value: neither the acute nor a third bar is seen. A short near-vertical mark stands directly above the e of *eze-* at the stain edge; it may be an acute or a stray and changes nothing.
5. **Row 11 `h?`:** a heavily overwritten bold 8-like sign with a separate tick at left. As it stands it looks like k; *hozzám* ("to me") requires h, so it is read as a correction. The sense is secure but the sign is not clean.
6. **Row 11 `t?`:** in *mint én* the t is cramped against the following e and looks like a bold chevron; a short dash after *i* is treated as a stray mark. *mint én* is required by the comparison with *úgy* ... *magához*.
7. **Last signs:** rows 9 and s7 end in a crossed i whose dot is not visible (row 9 is crossed by the postmark); read i in *szívébe* and *Feri*. Row s4 first signs (t, a) are tangled with row s5. The o of *vagyok* (row 21) is written over and has a bold arm; the final k is clear.

Writer's spellings normalized, all signs clear:

8. *ijen* → ilyen; *Jolánkámba* → -ban (kept with [n]); *kel* → kell; *akor* → akkor; *hozám* → hozzám; *beszélhetem* → beszélhettem (the sense is past, one t omitted); *időm* written without visible ő marks.
9. **`el` in row 5** (*...Jolánkámba el ijenkor is*): both signs clear. *El* is the verb prefix of *vesztek* (*elveszt* "lose"), placed after the verb as is normal after a question word: *mit vesztek én Jolánkámba[n] el*. The next sentence starts at *Ilyenkor is*. Corrected in review; it was first taken as a false start.
10. **Row 6 `valaunk`** → *válnunk*: clearly v a l a u n k; the sign after l is two bars (a) where n is expected.
11. **Row 12–13 `csomakotat adtam`** → *a csomagot átadtam*: k where g is expected (the sign is the clear section mark). The word division *át-adtam* is editorial.
12. Withdrawn in review. Row 16 reads `nemirok`: the e of *nem* has three bars, so there is no slip here.
13. **Rows 17–18 `mertmeral|mos`** → *mert [mer] álmos*: *mert* is begun a second time as *mer* and *álmos* is split across the row break. The sign after the second m is three bars (third bar set low and to the left), so *mer* is the literal reading, and this normalization assumes one dittography. A live alternative is *mert már álmos vagyok* ("for I am already sleepy"), which instead assumes e written for á in *már*; it cannot be excluded, and it would add only "already" to the translation. Either way he stops because he is sleepy.
14. **Row 19 `velédesem`** → *vele, édesem*: one e serves both words. The form *vele* is the formal address that fits *magához*.
15. **Row s2 `lom`:** the wave at the left of this row is faint and on the torn edge of the stamp area; if it is a stain, the word is still *csókolom* (s1 ends in l). Either way the text is the same.
16. **Row 11** *mint én magához*: *magához* is read as formal "to you" (maga), giving "as I am to you". A reader could take it as "to herself/to oneself", but the formal address runs through the family's cards.
17. The date is not legible; the file name gives 1913. The postmark was not read. The address side's plain text (*Szépremény[ű]* running into the postmark, then *Tóth Jolánka úrleánynak, Jászárokszállás*) is unenciphered. "Katona" could be a joke or a real circumstance; the card does not say. Nothing identifies Sándor or Béla beyond their names; Sándor also occurs on HCP1216.

## Why it is correct

- The family key, used unchanged, turns all 398 written signs into Hungarian with no unassigned sign; only the hidden signs of item 2–4 need restoration.
- The text is a coherent, plain message with the family's formal address and the family's closing (*Isten vele*, *Csókolom számtalanszor*, signature Feri as on HCP1216), and its words were not chosen by me: *szerencsésen megérkeztem*, *beszélhetem*, *hogy katona vagyok* came out of clean signs.
- Repeated words decode identically: *Jolánkám* ×4, *hogy* ×3, *ilyenkor* ×2, *nem* ×3, *vagyok* ×2.

## Response to review 1

Verdict REVISE. I re-opened the reviewer's crops for findings 1, 3, 4 and 5 and agree with all five findings. `python3 -I ciphers/hcp-1318/work/decode.py` was re-run after the changes: all four hash checks OK, 398 signs, and the output matches the literal block and the normalized text above.

1. **Row 16, sign 8: fixed.** Crop `review/work/crops/z16.png` shows n, three evenly spaced bars, then m. My ledger was wrong. `work/ledger.txt` row 16 and the literal block now read `d?emostnemirok`. Uncertainty item 12 is withdrawn, and "Why it is correct" now says *nem* ×3. The normalized text does not change.
2. **Row 5 `el`: fixed.** *Mit vesztek ... el* is good Hungarian with the prefix of *elveszt*. The brackets are gone, the full stop moved after *el* in the normalized text (here and in `work/normalized.txt`), and item 9 rewritten. The English and Slovak do not change.
3. **Rows 17–18: fixed.** Crop `z17.png` confirms three bars after the second m, but that alone does not rule out *már*. Item 13 now gives *mert már álmos vagyok* as a live alternative. I keep *mert [mer] álmos* in the normalized text, as neither option is stronger on the evidence. Withdrawing item 12 removes the only e/a confusion I had claimed, but *már* is still possible.
4. **Stain disclosure: fixed.** Crop `stain_hp.png` shows what the reviewer describes. Items 2–4 now state the traces in rows 7–9, the left tick of d in row 9, the contextual value of `[e']`, and the unreported mark above the e of *eze-*.
5. **Address: fixed.** Item 17 now includes the first line *Szépremény[ű]*, visible in crop `addr.png`.

The reading of the card is not substantially changed: one ledger sign, no change to any word of the normalized text, and only the sentence boundary in row 5 moved.
