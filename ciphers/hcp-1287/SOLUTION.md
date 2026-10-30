# HCP1287 — Sender to Jolánka Tóth: a funeral, a strike camp and an evening with the journeymen's families (May 1912)

**Status: complete reading, reviewed (round 1, verdict REVISE; all findings addressed, see the last section).** Claude Opus 5.5, 2026-10-30. Two word-sense residuals remain: row 12 (9 or k, item 1) and row 11 (*nagy bát[r]an* against *nagybátyám*, item 9).

Credit: all reading here is by Claude Opus 5.5; this number had no earlier work. The key is the Jolánka-family key established on finished cards (HCP1216, 1301, 1243 and others, whose earlier passes were by the OpenAI GPT solver with completion by Claude Opus 5.5). No published solution of this card was found or used: the portal says *Not solved*, with no transcription or solution attached, and the orchestrator's AI-register check of 2026-10-30 shows no record.

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented graphic signs (Jolánka postcard family). No new key was invented. Numerals stay in clear in this family (HCP1218, 1298).

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | section mark (S, top often closed like 8) | k | F-like | r |
| six | b | wave | l | right bowl `)` | s |
| joined opposed bowls | cs | three short strokes | m | gamma/corner | t |
| short stroke left + tall stroke right | d | two short strokes | n | plain cross x | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross + | f | tall stroke + short stroke right | h / p | low descender | y |
| open loop with descender | g | dotted crossed curve | i | crossed diagonal (flagged) | z |
| inverted T | j | | | | |

c, in *szerencsésen*, is a left bowl re-inked into a €-like shape. gy is here two separate signs g + y, not the joined form of HCP1216. Dots over o/u give ö/ü; two ticks give ő. Acutes are mostly faint and are supplied in normalization.

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1287/work/decode_opus.py
```

It checks the SHA-256 of all four image files, decodes `work/ledger-opus.txt` (423 written signs, a manual transcription from enlarged crops of the original address-side scan, not OCR), and prints the literal rows and `work/normalized-opus.txt`.

## Literal decipherment (as printed by the command)

```
01 kedvesjolankamtudatom        12 takenisotmaradtam{9|k}o
02 hogyszerencsesenmegerkez     13 raiasegedeklanyai
03 tünkeppenakortemetekezt      14 esfelesegeikelmulat
04 lanytijenszeptemetesmeg      15 tunkedesjolankammes
05 nemlatamdemegjolankam        16 ujsagotnemirhatok
06 seazudvarlojaötször          17 minthogynemtudom
07 ajultelutoljarais            18 medigtarastrajkdeami
08 bevitekatemtőkapol           19 eztiletinembajakarmedig
09 najabaatemetesutan           20 tartbecsessoraitvarva
10 elmentemasrrajktanya         21 istenveleaviszontlatas[i]g
11 raaholnagybatanszol          22 edese[m]
```

Plain hand, not enciphered: stamp corner `csokolom / es csokol / tatom / aval akit / leg jo?on / szeret si / rig hü / kedvese`. In line 5 the letters after `leg jo` are a tall looped letter, a small letter and `on` or `om`, closer to *jobon* than *jobban*; line 4 has one v (`aval`). Address: *Szépreményű* (under the postmarks) *Tóth Jolánka úrleánynak*, a small struck-through or cramped word after it, probably *szeretettel* (not certain), *Jász-Árokszállás*. Picture side: printed verse *Fecském hova szállsz?…*.

## Hungarian (normalized)

Kedves Jolánkám! Tudatom, hogy szerencsésen megérkeztünk. Éppen akkor temették ezt [a] lányt. Ilyen szép temetés[t] még nem láttam, de még Jolánkám se. Az udvarlója ötször ájult el, utoljára is bevitték a temető kápolnájába. A temetés után elmentem a sztrájktanyára, ahol nagy bát[r]an szóltak, én is ott maradtam 9 óráig(?). A segédek lányai[val] és feleségeikkel mulattunk. Édes Jolánkám, más újságot nem írhatok, mint hogy nem tudom, meddig tar[t] a sztrájk. De ami ezt illeti, nem baj, akármeddig tart. Becses sorait várva, Isten vele, a viszontlátásig, édesem.

Stamp corner (plain): Csókolom és csókoltatom avval, akit legjobban(?) szeret. Sírig hű kedvese.

## English

Dear Jolánka! I inform you that we arrived safely. They were burying that girl just then. I have never seen such a beautiful funeral, and neither has my Jolánka. Her suitor fainted five times; the last time they even carried him into the cemetery chapel. After the funeral I went to the strike camp, where they spoke very boldly, and I too stayed there until 9 o'clock(?). We made merry with the journeymen's daughters and wives. Sweet Jolánka, I can write no other news than that I do not know how long the strike will last. But as far as that goes, it does not matter how long it lasts. Awaiting your esteemed lines, farewell, until we meet again, my darling.

Stamp corner: I kiss you and send kisses through the one you love best. Your sweetheart, faithful unto the grave.

## Slovak

Milá Jolánka! Oznamujem Vám, že sme šťastne dorazili. Práve vtedy pochovávali to dievča. Taký krásny pohreb som ešte nevidel a ani moja Jolánka nie. Jej nápadník päťkrát omdlel, naposledy ho dokonca odniesli do cintorínskej kaplnky. Po pohrebe som išiel do štrajkového tábora, kde hovorili veľmi odvážne, a aj ja som tam zostal do 9 hodín(?). Zabávali sme sa s dcérami a manželkami tovarišov. Sladká Jolánka, inú novinu Vám nemôžem napísať, len že neviem, dokedy potrvá štrajk. Ale čo sa toho týka, to nevadí, nech trvá akokoľvek dlho. V očakávaní Vašich vzácnych riadkov, s Bohom, do videnia, drahá moja.

V rohu pri známke: Bozkávam Vás a dávam Vás bozkávať po tom, koho máte najradšej. Váš do hrobu verný milý.

## Uncertainties

The writer drops and doubles letters; every sign is transcribed as written and the normalization is editorial.

1. **Rows 12/13, `{9|k} orai` — the real residual.** Row 12 ends `… t a m`, a heavily inked sign, then `o`; row 13 starts `r a i` at the left margin. The inked sign has a closed top and a left-hooked foot. It is either the digit **9** in clear or the k-sign, whose top is often closed and which has that foot on this card (row 8). Digit reading: *9 órái[g]* "until 9 o'clock", with g omitted by the writer; this is the normalization I chose, from sense and because numerals stay in clear in this family. A dot-like mark up and to the right of the `o` would fit an acute (*ó*, as in *óra*); it may equally be a stray mark, so it is suggestive only. The spacing around the sign is normal and is no evidence either way. Letter reading: *korai* "early", which fits no clear construction here. It is therefore a word-sense call and only a detail of the sentence.
2. **Row 10 `srrajk`.** The second sign is a heavily re-inked F; the same word in row 18 is plainly *strajk*, so the dark sign is probably a t or a false start under correction. Normalized *sztrájktanyára*. *Sztrájk* also appears in HCP1304 (Feri to Jolánka), as an independent parallel.
3. **Row 22 `edese[m]` — restoration.** The final sign lies under a brown blot; strokes emerge on both sides. *m* is the only letter that gives a word (*édesem*). **Row 21 `[i]`**: the i of *viszontlátásig* lies in the blot, but its dot and tail remain visible.
4. **Row 21 first sign.** No dot is visible, but the crossed curve with long right tail is the i-shape, not o: *isten*.
5. **h/p by word sense; d by form.** The sign tall stroke + short stroke right (8 cases) is valued by the word: p in *éppen, szép, kápol-*; h in *hogy, ahol, írhatok, mint hogy*. d is a different form, short stroke left + tall stroke right (12 cases: *kedves, tudatom, udvarlója, édes, de* and others), and n is two short strokes; no d or n on this card needs word sense. *Szép* (row 4) and the first p of *éppen* are re-inked. u/z (plain cross against flagged cross) were also checked against the word.
6. **Row 15 end, `mes`.** The last sign is a re-inked `)`, the three bars carry a tick. *mes* is normalized *más* ("other") from *más újságot nem írhatok*; the e for a is the writer's or a dialect form, not corrected on the card.
7. **Row 3–5 grammar.** *ezt lányt* lacks *a*; *temetés* lacks the accusative -t (*temetést*), or may be a slip; *lányai* (row 13) lacks *-val*. Bracketed in the normalization. *tar* (row 18) lacks t (row 20 has *tart*).
8. **Row 6 `de még Jolánkám se`.** Sense-based punctuation: *…nem láttam, de még Jolánkám se(m)*. Whether it means she has not seen one, or teases her, is not determinable. Final m of Jolánkám in row 5 is a third stroke inside the postmark edge, faint but present.
9. **Row 11 `nagybatan`, `szol|tak` — word-sense residual.** The signs are certain: n a g y b a t a n s z o l t a k. Preferred: *nagy bát[r]an szóltak*, "they spoke very boldly". It needs one dropped r, the kind of omission this writer makes (*tar* for *tart*), takes the written plural verb at face value and suits speeches at a strike camp. Alternative, my first reading: *nagybátyám szóltak*, "my uncle called [me]", which needs y restored, final n changed to m, a polite plural for one's own uncle and an unwritten object. Neither can be proved. Who the girl is, is not stated.
10. **Other spellings normalized:** *akor, latam, ijen, bevitek, temtő, najaba* (for *kápolnájába*, row 8–9), *ot, kel* (for *-kkel*), *medig, ileti*.
11. **Sender.** The card is unsigned in cipher and in the plain stamp text (*kedvese* with no name). The handwriting is not compared in detail; no identification with Feri of HCP1216/1304 is claimed, though the closing formula and the Gyöngyös postmark are in line with those cards. The second postmark shows *YÖN* only, which I read as Gyöngyös, unverified. The first postmark is JÁSZÁROKSZÁLLÁS 912 MA 15, agreeing with the portal date.

## Why I believe it is correct

- The family key, unchanged, turns all 423 signs into Hungarian; the signs not read straight are items 1, 2, 3 and 6.
- The text is coherent and specific: arrival, funeral, a fainting suitor, the strike camp, the journeymen's families, the unknown length of the strike, and the usual closing *Becses sorait várva … Isten vele*.
- Words recur identically across the card: *Jolánkám* ×3, *strajk* ×2 (with item 2), *temet-* ×2, *meddig* ×2 and *nem* ×4.
- The plain stamp text (*sírig hű kedvese*) and the address form (*Szépreményű Tóth Jolánka úrleánynak*) match the family.

## Response to review 1

Verdict REVISE. All five findings are accepted and addressed; I re-checked findings 1 to 4 on the reviewer's crops of the hires scan. No sign value changed, and the 423 signs decode to the same letter sequence. Only row division and normalization changed.

1. **Row 11 (major): fixed.** The reviewer's reading is better. It needs one dropped r, where mine needed three repairs. *Nagy bát[r]an szóltak* is now the preferred normalization in `work/normalized-opus.txt`, and in the Hungarian, English and Slovak above. *Nagybátyám szóltak* stays as the alternative in item 9. It is a word-sense judgment and is labelled so.
2. **Row 12/13 break (major): fixed.** `review/work/crops/r12end.png` shows the `o` on row 12, after the inked sign; `review/work/crops/r06a.png` shows row 13 starting `r a i` at the margin. I moved the `o` in `work/ledger-opus.txt`, and corrected the literal block and item 1. My "wide gap" argument was wrong and is withdrawn. The dot near the `o` is recorded as suggestive only. The 9/k doubt stays disclosed.
3. **d/h (minor): fixed.** The crops bear it out: d (rows 12 and 13) is short then tall, h (row 11 *ahol*) is tall then short. The key table, ledger header and item 5 now say so; only the h/p choice rests on word sense.
4. **Stamp corner (minor): fixed.** The literal form is now `leg jo?on`, with `aval` noted, and *legjobban(?)* in the normalization. Line 5 is hard to read, and only its sense is secure.
5. **Small inaccuracies (minor): fixed.** *Jolánkám* ×3, and the "not read straight" list now names items 1, 2, 3 and 6.

After the fixes, `python3 -I ciphers/hcp-1287/work/decode_opus.py` passes all 4 hash checks and prints 423 signs, with the new rows 12 and 13 and the new normalization.
