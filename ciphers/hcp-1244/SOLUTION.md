# HCP1244 — Feri (Holes Ferenc) to Jolánka Tóth: safe arrival at Gyöngyös, Easter sprinkling

**Status: the whole enciphered text is read (17 rows plus one word below the address), with the small residual points listed below. One word of the separate plain note in the stamp box stays unread. Handed over as DONE1; revised after review 1 (see the end).** 2026-11-01, Claude Opus 5.5.

Credit: all reading on this number is by Claude Opus 5.5. There is no earlier work on this card. The key comes from the finished Jolánka cards (HCP1216 and others, partly solved earlier by the OpenAI GPT solver). The portal shows *Not solved* with no transcription or solution, and no published solution of this card turned up.

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented graphic signs (Jolánka family), the key of HCP1216 unchanged. Word division is not marked. Tokens are those of `work/ledger-opus.txt`.

| sign (token) | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars `=` | a | section mark `S` | k | F-like `F` | r |
| six `6` | b | wave `~` | l | right bowl `)` | s |
| opposed bowls `()` | cs | three short strokes `3` | m | gamma `7` | t |
| short + long stroke `4` | d | two short strokes `2` | n | plain cross `x` | u |
| three bars `#` | e | cursive loop `Q` | o | chevron `^` | v |
| open loop with descender `9` | g | tall + short stroke `H` | h / p | low descender `y` | y |
| dotted crossed curve `J` | i | joined loop + descender `GY` | gy | long crossed diagonal `Z` | z |
| inverted T `T` | j | | | | |

The last sign of row 14 carries both a gamma top and an inverted-T base bar. The ledger token is `7T` and the command prints it `{j|t}` (item 10). The tokens `<ap>`, `<,>` and `<.>` are marks in rows 14–15, not letters (item 17).

Dots and ticks over a sign are accents. They appear only here and there and are supplied in normalization. f does not occur.

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1244/work/decode_opus.py
```

It checks the SHA-256 of the two source scans and the two hi-res originals, decodes `work/ledger-opus.txt`, and prints the literal rows and the normalized text `work/normalized-opus.txt`. The ledger is a manual transcription from the pixels, not OCR.

## Literal decipherment (as printed by the command)

```
01 kedvesjolánkam          10 zethogybörigeláz
02 tudatomhogysze          11 tamistenvelaviszont
03 rencsésenmegerkez       12 latásradesokáleszaz
04 tünkagyöngyösialo       13 elegleszkibirni
05 masonvártrankahaés      14 adossoh’semmarad{j|t},
06 anymédesjolankam        15 acsok[s]ohasemart.
07 kiöntözteemárma         16 hacsókotkahbabám
08 gáténamesterurla        17 csakaddvisszamindjart
09 nyaitolannyivi          A1 szeretettel  (below the address)
```

## Hungarian (normalized)

Kedves Jolánkám! Tudatom, hogy szerencsésen megérkeztünk. A gyöngyösi állomáson várt ránk apa és any[á]m. Édes Jolánkám, kiöntözte-e már magát? Én a mester úr lányaitól annyi vizet, hogy bőrig eláztam. Isten vel[e] a viszontlátásra. De soká lesz az, elég lesz kibírni. Adós soh'sem maradj, a csók soha sem árt. Ha csókot kap, babám, csak add vissza mindjárt.

Below the address, enciphered: Szeretettel.

Plain hand, in the stamp box (not enciphered): Csókolom a távolból az e… …tel Fe[?]ri. Holes Ferencz.

Address, plain: Szépreményű Tóth Jolánka kisasszonynak, Jászárokszállás. Picture side: printed verse *Szerenád. Ábránd.*, not cipher.

## English

Dear Jolánka of mine! I let you know that we arrived safely. At Gyöngyös station father and my mother were waiting for us. Sweet Jolánka of mine, has anyone sprinkled you yet? As for me, from the master's daughters [I got] so much water that I was soaked to the skin. God be with you, until we meet again. But that will be a long time; it will be hard enough to bear. Never stay in debt, a kiss never does harm. If you get a kiss, my baby, just give it back at once.
Below the address: With love.
Stamp box: I kiss you from afar … [one word unread] … Feri. Holes Ferencz.

## Slovak

Milá moja Jolánka! Oznamujem Vám, že sme šťastne docestovali. Na stanici v Gyöngyösi nás čakal otec a moja mama. Sladká moja Jolánka, už Vás niekto polial? Ja [som dostal] od dcér pána majstra toľko vody, že som zmokol do nitky. S Bohom, dovidenia. Ale to bude dlho, bude ťažké to vydržať. Nikdy nezostávaj dlžný, bozk nikdy neuškodí. Ak dostanete bozk, zlatko, hneď ho vráť.
Pod adresou: S láskou.
V rámčeku známky: Bozkávam Vás z diaľky … [jedno slovo neprečítané] … Feri. Holes Ferencz.

## Uncertainties

1. **Rows 4–5 *alo|mason*** is normalized *állomáson*: the writer wrote one l and no accents. The sign before o in row 4 is a deep, sharp wave, closer to the wave l than to the chevron v, which on this card always peaks upward. *Állomáson* and the adjacent *gyöngyösi* settle it.
2. **Row 5 *ahaés*.** The sign is h/p, read p: *apa és*, by word sense (the h/p near-homograph). *ránk a pa…* is excluded by the following *és*. The first a belongs to *apa*, not to an article. The sentence has no possessive on *apa*.
3. **Row 6 *anym*.** The signs are a, n+y (joined), then three strokes, the third reduced to a dot-like tick. Normalized *any[á]m*. The á is not on the card.
4. **Row 6 end, *-kam*.** The third stroke of m is curved like an s bowl and stands on the printed divider. Read as m, as in row 1. n + s gives no word.
5. **Rows 7–8.** *kiöntözteemár-magát* is divided *kiöntözte-e már magát*. Word sense decides the division, and the card's date fits (item 12). The third bar of the second e of *-tee* is a firm wedge, set low (`review/work/crops/r7e.png`); the sign is e. *kiöntözte* is singular: literally "has he sprinkled you", an unnamed sprinkler. The translations give "anyone". The row-final *ma|gát* crosses a row break.
6. **Rows 9–10, no verb.** *Én … annyi vizet, hogy bőrig eláztam*: the card has no verb such as *kaptam* before *hogy*. I have not supplied it in the Hungarian. In row 9 the t of *-tól* is largely under a pink blot, but the top bar of the gamma shows to the right of the blot.
7. **Row 10.** *h* of *hogy* is blotted (thick stroke + tick), and the word is certain. The dots over *bör-* are pale. Normalized *bőrig*.
8. **Row 11 *vela*.** The sign after l is a: the green channel (`review/work/crops/r11vela_g.png`) shows two firm bars and no third. So I keep the letter on the card as the article and treat the final e as dropped: *Isten vel[e] a viszontlátásra*. The family's usual close is *Isten vele, a viszontlátásra*. The alternative is that this a stands for the e of *vele* and the article is missing.
9. **Row 13.** A pale, overwritten group stands at *lesz*: a pale crossed diagonal over the z, which I take as a pen correction with no value. It may show the writer re-inked the word.
10. **Row 14, last sign: *maradj* chosen, *maradt* not excluded.** The sign has features of two letters (`review/work/crops/r14end.png`, `work/crops2/r14end_gb.png`). After the short and long strokes of d there is a stem with a gamma top. That top bar runs right into a wet pink smear, and in the green and blue channels its firm core has the thickness and about the length of a normal gamma top. So it is pen work, not the edge of the smear. A base bar also runs from the long stroke through the foot of the stem and past it, which is the construction of the d+j ligature in row 17 (`review/work/crops/r17end.png`). No other t on the card has a base bar. The ledger token is `7T`, printed `{j|t}`, and the normalization uses j, for these reasons:
    - A base bar is a deliberate second stroke and has no place in a t. A slip does not explain it, whereas a t corrected to j does, and the blot lying right on the top bar may be the attempt to wipe it. That last point is a guess: this card has other blots. I cannot show the stroke order from the scan.
    - *Adós sohsem maradj* gives the clause a subject (you), and it fits the imperative *add vissza*. *Adós sohsem maradt* has no stated subject.
    - Rows 14–17 are laid out as a four-line verse, one line per row. Its rhyme is *árt / mindjárt*, on lines 2 and 4. Line 1 does not need to rhyme, so the rhyme with *maradt* is no argument for t. I do not know this verse from any printed source.
    - The tick after the sign (item 17) works as a comma before *a csók…*, which ends at the dot of row 15.
    - Against j: the gamma top is really there, and *soh(a)sem* with an imperative is colloquial (*sohase* is the usual form). If the sign is t, the reading is *Adós sohsem maradt* ("a debtor he never stayed", or a slip for *maradtam*). The division *Adós sohsem maradt a csók*, with the kiss as subject, leaves *soha sem árt* without one. It reads worse. The sense of the verse (jesting advice) stays the same in both readings.
11. **Row 15 [s].** The first sign of *soha* is filled by a blot. Its outline still has the top-left hook and bottom-left foot of the right bowl, with a thin slit inside. No letter other than s gives a word (*csoha* does not exist). Treat it as a disclosed restoration. Row 16 *kap* has the h/p sign, read p by sense, likewise *ha* as h. In row 15 the h of *soha* is heavily inked and blobbed; its tall and short strokes are still separate (`review/work/crops/r15h.png`). **Rows 16–17, person:** *kap* is third person or formal, *add* is informal second person. I take *babám* as a vocative and *kap* as the formal "you" Feri uses earlier on the card (*magát*), with a slide to *te* in the verse. *Ha csókot kap babám* can also mean "if my baby gets a kiss". The English cannot show the switch; the Slovak keeps it (*dostanete … vráť*).
12. **Date.** The date 1912-04-10 comes from the portal's file name. Turned 180° (`review/work/crops/pm180.png`), the postmark shows `91…`, then `APR`, then `10` or `16`. The month is April and the year's last digit is not legible. The ring text is not read. Easter 1912 fell on 7 April by calculation, so sprinkling (Easter Monday, 8 April) fits *kiöntözte-e*, and the writer had just travelled. Calling *kiöntözte* an Easter custom is my interpretation of the context.
13. **Stamp box (plain, not cipher), one unread word.** The stamp has gone, the paper is torn at line 2, and the text lies over the printed stamp-box emblem. Lines read: *csokolom* | *a t…vol* | *ból az e-* | ?*n/r-e-l/d-e-t* | *te/tel + F/Sz-e? + ri*. *a távolból* rests on the same formula on HCP1278 *csókolom a távolból*; the t and á are in the tear and only the top of a stroke shows, so those two letters are a restoration. The first letter of *ból* looks like h or b; b by sense. The word begun with *e-* and running over two lines to *-tel* is not read. I do not offer a guess. The line-end *ri* is in purple over red, so the name's first letters may be of a different ink stage; *Feri* is likely, not certain.
14. **Signature, purple.** *Holes Fe…* is clear; the rest fades under the postmark and I read *Ferencz* only with the help of sister cards (HCP1268 *Holes Ferenc*, HCP1303, HCP1309 *holes feri*). The capital reads H. The F has its top bar visibly detached.
15. Pencil marks at the top right corner (about "17") look like a later dealer or collector mark. They are not read as text. A dot at the left of row 2 is taken as a stray.
16. Accents in the literal text show what is visible; they are not reliable as phonetic evidence. In rows 3, 5 and 13 ticks near a sign could belong to the row above or below.
17. **Marks that are not letters.** Row 14 has a short high arc between h and s (`review/work/crops/r14h.png`), possibly an apostrophe for the dropped a (*soh'sem*), and a slanted tick after the last sign, which I read as a comma. Row 15 has a round dot after the final t, which I read as a full stop. All three are in the ledger (`<ap>`, `<,>`, `<.>`). They are not evidence for the punctuation elsewhere, which is editorial.

## Why it is correct

- All 18 rows decode with the HCP1216 key, unchanged, with no new sign. Two signs are outside the plain table: the d+j ligature in row 17 and the t/j sign at the end of row 14 (item 10).
- The opening formula *Kedves Jolánkám! Tudatom, hogy szerencsésen megérkez-* matches HCP1278 almost word for word, yet it rests on signs read here.
- Sister cards independently connect this writer with Gyöngyös (HCP1271), with work under a master, and with the name Holes Ferenc.
- The closing lines, *A csók soha sem árt. Ha csókot kap, babám, csak add vissza mindjárt*, come from signs mostly clean and of the same hand, and could hardly fall out of noise.
- The word below the address decodes to *szeretettel*, a word with no other support, using the same key.

## Response to review 1

Verdict REVISE. All findings are addressed. One letter of the normalized text changes (*maradt* to *maradj*) and no key value changes. `python3 -I ciphers/hcp-1244/work/decode_opus.py` was re-run: hashes OK, 18 rows, output as in the block above.

1. **major, row 14 last sign: fixed.** I agree. I re-examined the sign in colour and in the green and blue channels (`work/crop_r14.py`, `work/crops2/r14end_gb.png`). The base bar is real, and so is the gamma top: the reviewer could not tell whether the top was pen or smear edge, and the channels show a firm pen core inside the smear. The ledger now has token `7T`, the literal text prints `{j|t}`, and item 10 gives both readings with the evidence. I chose *maradj* and revised the normalization, English and Slovak. "Why it is correct" is corrected. One thing I add to the reviewer's analysis: the rhyme does not favour t, because rows 14–17 form a stanza rhyming on lines 2 and 4.
2. **minor, marks in rows 14–15: fixed.** All three are in the ledger and in item 17. The full stop after *maradt* is gone; the normalization has the comma.
3. **minor, *vela*: fixed.** I confirmed two bars on the green channel. The normalization is now *Isten vel[e] a viszontlátásra*, and item 8 gives the alternative.
4. **minor, *úr lányaitól*: fixed.**
5. **minor, translation details: fixed.** *kiöntözte* is noted as singular in item 5, and the translations now say "anyone" / *niekto*. The switch from *kap* to *add* and the third-person alternative are in item 11. The Slovak keeps the switch.
6. **minor, item descriptions: fixed.** The wedge is described in item 5, the blobbed h of row 15 in item 11, and the postmark month APR in item 12.
7. **Stamp box: no change.** The reviewer had no objection. The one word stays unread and I add no guess. It is alone, in a plain note, and the card is complete with it unread.
