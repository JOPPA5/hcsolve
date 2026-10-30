# HCP1285 — Tóth Jolánka card, Jászárokszállás, 14 January 1912

**Status: every written sign is read; the main message is complete; the closing fragment (last 4 + 4 signs) is read letter by letter but its expansion is tentative. Review 1 verdict ACCEPT; its minor findings are addressed below.** Written 2026-10-30 by Claude Opus 5.5. There was no earlier work on this number.

Portal status: Not solved, no attached transcription or solution. No published solution was found or used. The key comes from the finished family cards of this repo (HCP1216, 1213, 1217, 1218, 1243, 1301), whose earlier work was done by the OpenAI GPT solver and completed by Claude Opus 5.5.

## Cipher type and key

Hungarian (the portal says Unknown), simple monoalphabetic substitution with invented graphic signs, the Jolánka family key without change:

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | section mark | k | F-like | r |
| six | b | wave | l | right bowl | s |
| left bowl | c | three short strokes | m | gamma | t |
| long + short stroke (short at left) | d | two short strokes; joined variant: tail with two arches after a loop | n | plain cross x | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross + | f | tall + tick at upper right | h | low descender | y |
| open loop | g | tall + tick at lower right | p | crossed diagonal with hook | z |
| dotted crossed curve | i | inverted T | j | joined loop + descender | gy |

Dots over o/u give ö/ü. Left and right bowl side by side give cs. The text runs left to right after turning the address side 90 degrees clockwise (11 rows, the last short, squeezed in the corner). Three more rows stand in the stamp box, in the upright position of the card. On this card the tick position separates h from p: it is high in *hogy*, *látható* and the final h, low in *kaptam* and *képen*; d (*édes*, *boldog*) has its short stroke on the left.

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1285/work/decode.py
```

It checks the SHA-256 of both source scans and both hires originals, decodes the manual sign ledger `work/ledger.txt`, and prints the literal rows and `work/normalized.txt`. The ledger is a manual reading from enlarged crops (`work/crops/`), not OCR, and not blind: the key was known and word sense helped.

## Literal decipherment

```
01 kedvesédesjola^nkamb.sora      07 szontlatasrviszo^ntkiva
02 itmegkaptamme{blot}lynekna     08 nokilyenboldogsagot
03 gyonörülök.éskeremazis         09 kivanokminteképenlatha
04 renrhogyezrozsasokaig          10 toistenveleédesemhon
05 ny{blot}iljonszamomra.amien    11 esf
06 gemilletaligvaromavi           box: cso / kol / iahf
```

## Hungarian (normalized)

Kedves édes Jolánkám! B[ecses] sorait megkaptam, melynek nagyon örülök, és kérem az Istent, hogy ez rózsa sokáig nyíljon számomra. Ami engem illet, alig várom a viszontlátást. Viszont kívánok ilyen boldogságot [kívánok], mint e képen látható. Isten vele, édesem. Hőn(?) és f[orrón](?) [stamp box:] csókolja, h f(?) or 14(?)

## English

Dear sweet Jolánka! I have received your esteemed lines, which make me very glad, and I pray to God that this rose may bloom for me for a long time. As for me, I can hardly wait to see you again. In return I wish you such happiness as can be seen on this picture. God be with you, my darling. Ardently(?) and [hotly](?) [stamp box:] kisses you, h f(?) or 14(?)

## Slovak

Milá sladká Jolánka! Vaše vážené riadky som dostal a veľmi sa z nich teším a prosím Boha, aby táto ruža dlho kvitla pre mňa. Čo sa mňa týka, sotva sa môžem dočkať nášho stretnutia. Na oplátku Vám želám také šťastie, aké vidno na tomto obrázku. S Bohom, drahá moja. Vrúcne(?) a [horúco](?) [rámček pre známku:] bozkáva Vás, h f(?) alebo 14(?)

## Other text on the card (plain, not enciphered)

Address side: *Szépremény* (over the postmark; a pink smear follows it, so the end may have been wiped: sister cards HCP1294 and others have *Szépreményű*, "of fair promise"), *Tóth Jolánka kisasszonynak szeretettel* ("to Miss Jolánka Tóth, with love"), *Jász-Árokszállás*, then a heavily struck-out start (*Fe…*?) and *al szög* (probably the town quarter Alszög; not certain). Postmark JÁSZÁROKSZÁLLÁS 912 JAN 14, which agrees with the portal date. A second postmark is only partly legible. The picture side is a printed couple with a printed four-line verse about falling leaves, ending *Szerelemről boldogságról* ("of love, of happiness"), which echoes *ilyen boldogságot*; this is the *kép* of row 9.

## Uncertainties

1. **Closing fragment (rows 10–11 and box row 3): the main open point.** The letters are `hon esf` and `ia h f`. The sign after h is a loop with extra overlapping strokes, including a blob and marks above it (a correction, or possibly a double accent ő, which would help *hőn*; not provable), so o is a best reading. Its joined tail has two arches, like n in *nyíljon*; the box tail after o has a single wave, like l. The pixels therefore separate row 10 `hon` from box `kol`, and `hol` in row 10 is unlikely. *Hőn és f[orrón] csókolja* ("ardently and hotly kisses you"), running on from row 11 into the box, is a **conjecture** that supplies the verb rows 10–11 lack. It is not a reading. **The last two box signs may not be letters at all:** read as h and f they also look like the digits **14** (a tall stroke; then a short free tick whose base may run through a faint extension of the crossbar into an upright; the stamp ring and bleed prevent a decision), and the card is postmarked the 14th. So "hű Feri" (h. = faithful, F. = Feri, the family's sender) is only one option, and a signature may not exist. No abbreviation dots stand in the box after h or f. `ia` for *-ja* uses i where j would be correct.
2. **Row 4, `renr` = *Istent*, and row 7, `viszontlátásr` = *viszontlátást*.** Three signs have a clear crossbar and are literally r, but word sense needs t (*az is|tent*, *a viszontlátást*). I take these as writer's slips, not as a key change: gamma stands for t elsewhere on the card, including *Isten* in row 10. All three are ordinary F in form with no sign of a bar added later, so a slip of the pen is my hypothesis about the writer, not something visible. The word *Istent* is not in doubt. Row 7 has a second explanation with no slip: `viszontlátásr` = the formula *viszontlátásr[a]* with a dropped a. *Várom a viszontlátást* is better grammar and stays primary.
3. **Inserted n.** Two small double strokes stand above the rows: in row 1 at the head of the k of *Jolánkám* (after the a, the second stroke touching the k), and between rows 6 and 7 just above the heavy t of the second *viszont*. Both are read as a missed n written in afterwards. The second could also be taken as *várnom* in row 6 (below the r of *várom*), which makes worse sense.
4. **Blots.** Row 2 (*me█lynek*) and row 5 (*ny█íljon*): solid blots, value not claimed. The words are complete without them; each may hide a false start or a doubled letter. Row 1: the a of *Jolánkám* has two clear bars with a square blot directly under them, which could be a blotted third bar (e); a rests on word sense. Row 10: the first sign, read t, is a heavily bled gamma with a spur on its stem at crossbar height; gamma is read by *látható*, and the spur may be bleed or the same t/r slip as in item 2. Blots on row 3 (ö of *örülök*, dots visible), row 7 (the a of *látást*, the last a of *kíva*, the t of *viszont*) and the start of row 8 (joined n, thick) are overwritten letters whose shape is still seen, read with help of word sense.
5. **Repeated *kívánok*** (rows 7–8 and row 9): both are written; the normalization brackets the second. The first sign of row 9 is a looser form of k. *Viszont* may equally mean "however" here.
6. **`b.` in row 1** is written with a dot and is expanded as *b[ecses]* ("esteemed"), the usual letter formula; the expansion is mine, supported by *Becses sorait* written out on HCP1212 and HCP1294.
7. **z / i are close shapes**, and z is called by sense in *az*, *ez*, *rózsa*. Row 10 *Isten* has no dot on its i. *Rózsa* is taken at face value: *ez rózsa* (no article) may be a figure for the love or for Jolánka; the card does not say.
8. Normalized accents are supplied, except those marked in the ledger. *Hőn* for written `hon` is part of the conjecture in item 1, and the box part may also be a date (item 1).
9. No sender name stands on the card. Feri comes only from the family and is not asserted here.

## Why it is correct

- The family key, unchanged, gives Hungarian across all rows with word sense over row breaks (*sora|it*, *na|gyon*, *is|tent*, *en|gem*, *vi|szont*, *kíva|nok*, *látha|tó*), which are not set by the writer.
- The text is idiomatic period letter prose and matches the family formulas (*Kedves … Jolánkám*, *Ami engem illet*, *Isten vele*, *csókolja*), and uses formal *Ön* address as the other cards do.
- *Mint e képen látható* refers to the embracing couple on the picture side, a check independent of the cipher.
- Addressee, town and date agree with the card's plain writing and postmark.
- The verse printed on the picture side ends *Szerelemről boldogságról*, in line with *ilyen boldogságot … mint e képen látható*.

## Response to review 1

Verdict ACCEPT, all findings minor. I looked at the reviewer's enlargements (`review/work/z_*.png`) and agree with each finding. No sign value in the ledger changed. Only `work/normalized.txt` changed, and `python3 -I ciphers/hcp-1285/work/decode.py` was re-run afterwards: all four hashes OK, literal rows unchanged.

1. **Row 1 blot and insertion: fixed.** The square blot under the a is plain in `z_r1_a.png`. It is added to uncertainty 4. Uncertainty 3 now puts the two strokes at the head of the k.
2. **Row 10 first sign: fixed.** Added to uncertainty 4, with the reading by *látható* stated (`z_r10st.png`).
3. **Joined n: fixed.** The variant is in the key table. Uncertainty 1 now says the row 10 tail has two arches and the box tail one wave (`z_end.png`, `z_box.png`), which corrects my "same tail" claim.
4. **Closing fragment: fixed.** (a) The digits 14 are named in uncertainty 1 as a rival to h f; in `z_box.png` the group does look like 14, and I cannot exclude either. Dots are removed from the normalization. (b) The possible double accent is noted, and the normalization and translations now run rows 10–11 into the box as one conjectural clause.
5. **Row 7 alternative: fixed.** *Viszontlátásr[a]* is listed in uncertainty 2. The "added bar" wording is withdrawn, since `z_Fs.png` shows ordinary F. *-t* stays primary on grammar.
6. **Wording: fixed.** The row break is now *látha|tó*. HCP1212 and 1294 are cited for *b[ecses]*. The possibly wiped end of *Szépremény* is noted (`z_szeprem.png`). I checked these citations in the two sister SOLUTION.md files. I also added the picture verse as a further check, as the reviewer suggested.
