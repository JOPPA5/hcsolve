# HCP1316 — Feri to Jolánka Tóth: safe arrival, the dancing school, slanderous talk

**Status: complete reading of the live text, with disclosed residual points. One clause (rows 15–17) has doubtful signs (rows 15, 16, 17) and its sense stays tentative; a short struck-out passage in row 16 is not decoded. Review 1: REVISE, findings addressed below.** 2026-10-30, Claude Opus 5.5.

Credit: all reading here is by Claude Opus 5.5 (2026-10-30). There is no earlier work on this number. The key comes from the finished Jolánka family (HCP1212, 1213, 1216, 1217, 1218, 1243, 1301), which was established by the OpenAI GPT solver and completed by Claude Opus 5.5. No external plaintext was used. The portal shows status *Not solved* and attaches no transcription or solution, and no published solution of this card turned up. The orchestrator's AI-register check of 2026-10-30 found no record.

Portal language is "Unknown"; the language is **Hungarian**.

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented graphic signs, same key as the family. All cipher text is in red ink: 19 rows on the left, 5 rows in the stamp box. The address is in clear (Szépreményű Tóth Jolanka úrleánynak, Jász Árokszállás), and is not ciphered.

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | section mark, open S | k | F-like | r |
| six | b | wave | l | right bowl | s |
| left bowl | c | three short strokes | m | gamma/corner | t |
| short + long stroke | d | two short strokes | n | arched x | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross + | f | tall + short stroke | h / p | low descender | y |
| open loop with descender | g | dotted crossed curve | i | arched x with long rising tail | z |
| inverted T | j | | | | |

cs and sz are spelt c+s, s+z; gy is g+y. Diacritics: dots or double marks over the sign (ü, ű); acutes are mostly not written or too faint and are supplied in normalization.

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1316/work/decode.py
```

It checks the SHA-256 of both source images and both hires originals, decodes `work/ledger.txt` (one token per written sign, a manual transcription from enlarged crops, not OCR) and prints the normalized text `work/normalized.txt`. Crops are in `work/crops/`.

## Literal decipherment (as printed by the command)

```
01 edesszerelmemdraga          11 adsemitmegragal
02 jolankamtudatomhogy         12 mazobeszedekrecsak
03 szerencsesenmeg             13 legyenkitartoszerel
04 erkeztemmegatancz           14 memugymintszeretem
05 iskolaisvoltam              15 m?a?gatmitbarmar
06 kedvesemaboldogsag          16 tetem?is  + struck-out passage
07 kertjebenegyfokal           17 {b|d}ebizonyithatnak
08 m?egintbeljeb               18 ezelbez{e|a}tomsoraim
09 kerültemboldogit            19 istenveatavolbol
10 azatudathogynem
stamp: cso[k][o]lom / szamta / lanszor / hű kedves / se feri
```

## Hungarian (normalized)

Édes szerelmem, drága Jolánkám! Tudatom, hogy szerencsésen megérkeztem, meg a tánciskola is volt ám. Kedvesem, a boldogság kertjében egy fokkal megint beljebb kerültem. Boldogít az a tudat, hogy nem ad semmit [a] megrágalmazó beszédekre. Csak legyen kitartó, szerelmem, úgy, mint szeretem magát, mit bár már tettem is bebizonyíthatnák. Ezzel be[zár]om soraim. Isten ve[le] a távolból.

Under the stamp: Csókolom számtalanszor. Hű kedvese, Feri.

## English

My sweet love, dear Jolánka! I let you know that I arrived safely, and the dancing school took place too. My darling, in the garden of happiness I have once again got one step further in. I am made happy by the knowledge that you give nothing for slanderous talk. Only stay steadfast, my love, just as I love you, which I wish my deeds too could already prove (sense tentative). With this I close my lines. God be with you, from afar.

Under the stamp: I kiss you countless times. Your faithful sweetheart, Feri.

## Slovak

Moja sladká láska, drahá Jolánka! Oznamujem Vám, že som šťastne docestoval a bola aj tanečná škola. Drahá, v záhrade šťastia som sa zasa o stupeň dostal hlbšie. Teší ma vedomie, že nedáte nič na ohováračské reči. Len zostaňte vytrvalá, moja láska, tak ako ja ľúbim Vás, čo by, kiež, už mohli dokázať aj moje skutky (zmysel neistý). Týmto končím svoje riadky. S Bohom z diaľky.

Pod známkou: Bozkávam Vás nespočetnekrát. Váš verný milý, Feri.

## Uncertainties

Calls that rest on word sense, not on a clean sign match, are marked **context**.

1. **Rows 15–17, sense.** The letters give *m?a?gat mit bar mar tetem is {b|d}e bizonyithatnak*. The main reading is *mit bár már tettem is bebizonyíthatnák*, with *bár* + conditional as the optative "if only" and *tettem* "my deed" (the writer's usual single consonant, as in *fokal, ezel, beljeb, semit*): "which I wish my deeds too could already prove". This is the only version found in which the *bár* clause is grammatical, but it is not clean: the plural ending *-nák* does not agree with a singular *tettem* (strict grammar wants *bebizonyíthatná*, or *tetteim* with the plural). The other reading is in item 8. The translation stays tentative. The h of *-hat-* rests on the h/p/n stroke-pair family (**context**).
2. **Row 16, m of *tetem* (context).** The sign is a retouched, thick three-stroke zigzag, unlike the separate strokes of normal m. It has a closing top line, and a z-sign retouched into it cannot be excluded; the reviewer could not confirm m from the pixels and left it unknown. Read as joined m because *tettem is* is the only word found; *tetéz is* is the alternative.
3. **Row 16, struck-out passage.** After *tetem is* the writer crossed out a stretch with several heavy horizontal lines; the lines run past the printed column rule to the right. It is layered: a raised second 6 and a dotted sign stand above the struck line, and a large loop stands below the blot, so the place was overwritten more than once. Under the lines one can see b, an x-like sign, o, a blot, then F, strokes, e/a bars, F. As a hypothesis only, raised b + dotted i + x-like sign + o could be a false start of *bizo-*, which row 17 then writes out. The passage is cancelled text and is **not decoded or used**. A signs-level reading is not possible.
4. **Row 4, m of *meg*.** The first sign is a heavily overwritten stroke with two crossbars (an a or e corrected), followed by two plain strokes. Read as three strokes = m.
5. **Row 8, first sign (context).** A dark stroke plus a Latin-looking "a" form, apparently a retouched m. Only *megint* fits *…egint*.
6. **Row 11, *semit*.** Between i and t stands a thoroughly blacked-out hatched sign, taken as a cancelled sign with no value. The row reads *semit* = *semmit* (**context**). There is no written *a* before *megrágalmazó*.
7. **Row 15, first two signs of *magát* (context).** The first sign is thick, with three strokes and a branched extra ink stroke, so it looks like four strokes; it is read as a retouched m (ledger M?). The second is blotted; bars cannot be counted, so a versus e is not settled from the pixels. *magát* fits *szeretem*.
8. **Row 17, first sign (context).** Corrected in review. Under an ink halo there is a tall curved stem and a closed bowl, whose thin lower arc reaches the foot of a stroke rising on the right. The bowl fits the six (b) and is unexplained under d; the rising stroke fits d (short + long stroke) and is unexplained under b. The pixels lean to b but do not settle it (ledger `{b|d}`). The e after it is clear. Read b, the word is *bebizonyíthatnák* (main reading, from the standard verb *bebizonyít* "to prove"). Read d, it is *de bizonyíthatnak/-nák*, "but they can/could prove it" (or "…which I have indeed already done, but they can prove it"). Bare *bizonyít* and *de* both occur in the family (HCP1212, 1216), so the choice rests on the *bár* clause. **Ending:** acutes are mostly unwritten, so *-nak* (indicative) and *-nák* (conditional) are both possible; two bars are certain, so *-nék* is excluded.
9. **Row 18, *bez{e|a}tom*.** The sign before t has two full bars and only a tiny speck under the left of the top bar, where e needs a middle bar. This writer's e can have a reduced middle bar (row 7, sign 2), so e stays possible, but a or á is also possible, and it is the reading that fits. The next sign is plain gamma (t) with no crossbar; the r in *soraim* in the same row has one. Normalized *be[zár]om* ("I close") is an editorial correction, since *ezzel bezárom soraim* is a formula. If the sign is a, the slip is one sign, t for r, and the shapes differ by one missing crossbar; if it is e, it is two signs. The bracket marks that this is not what is written.
10. **Row 19, *ve a*.** After v the card has e then a; *vele* lacks *l e*, a writer's omission supplied in brackets (compare *Isten vele* on HCP1216).
11. **Stamp, *csókolom*.** k and o lie in the stain left by the removed stamp: only an arc of k and a damaged arch-and-crossing of o remain. These are **restorations of physically damaged signs**; the a of *számta* is also stained but its bars are visible.
12. **Stamp, *kedves|se*.** The word *kedvese* is written with s at the end of row 4 and again at the start of row 5, a dittography across the line.
13. **u versus z.** Both are arched crosses; z has a long rising tail. Every u/z decision here gives a word (*tudatom, úgy, érkeztem, szerel-*), which helps but means they rest partly on context.
14. Editorial spelling: *fokal → fokkal, beljeb → beljebb, ezel → ezzel*, row 4 *tancz* (period spelling) → *tánc*. Word division and punctuation are editorial. *hogy* in row 2 and 10 uses the tall-stroke pair.
15. **Row 5 word division.** The letters are *…iskola is voltam*. The text divides *volt ám* ("took place, you know"). *voltam* "I was" is the alternative, which would need a missing case ending (*tánciskolá[ban] is voltam*, "I was at the dancing school too") and suits the first-person run *megérkeztem, kerültem*. Both are possible; the division is editorial.
16. Address side: the first address word in clear is not transcribed in the ledger because it is not cipher. Portal date 1912-06-30; the postmark shows a day 30, the rest was not fully read. The picture side has only the printed verse and is not ciphered.

## Why it is correct

- The family key, unchanged, turns all 24 rows into continuous Hungarian, with no key adjustment except the explicit u/z tail observation that already exists in the family.
- The phrases are specific and idiomatic: *a boldogság kertjében*, *megrágalmazó beszédekre*, *legyen kitartó*, *tudatom hogy szerencsésen megérkeztem*, and closing formulas shared with the family (*számtalanszor*, *hű kedvese*, *Feri*).
- Repeats decode identically (*szerel-* rows 1, 13/14; *hogy* rows 2, 10; *boldog-* rows 6, 9).
- The sender Feri and addressee match HCP1212, 1213, 1216.

## Response to review 1

Verdict REVISE, seven findings. All are accepted and checked on the reviewer's crops (`review/work/crops/`). `python3 -I ciphers/hcp-1316/work/decode.py` was re-run after the fixes: all four hashes OK, 337 signs, and the output matches the blocks above.

1. **Row 17, first sign (major): fixed.** On `r17_blob.png` the bowl and stem are clear, and the rising right-hand stroke is also real, as the reviewer says. Ledger token D? changed to `{b|d}`, item 8 rewritten with both readings. The main reading is now *bebizonyíthatnák*, not *de bizonyíthatnak*, because b is the pixel lean and *bár* + conditional gives the clause a structure ("if only"), which *de* did not. Item 1 states the remaining number disagreement. English, Slovak and the Hungarian are updated. One sign value changes (d to b as the main reading) and the clause stays tentative, as it was at handover; the rest of the reading is untouched.
2. **Row 18, sign 8 (minor): fixed.** Marked `{e|a}` in the ledger, item 9 restated. Added: the gamma after it differs from the F of *soraim* by one missing crossbar.
3. **Row 5 division (minor): fixed.** New item 15 gives *voltam*. I keep *volt ám* in the text: it needs no supplied ending.
4. **-nak / -nák (minor): fixed.** In item 8, and -nák is used in the main reading.
5. **Row 15, first sign (minor): fixed.** Ledger M?, item 7 extended. Confirmed on `r15_start.png`.
6. **Row 16 (minor): fixed.** Item 3 corrected on `r16_strike.png`: the lines pass the rule, and the raised 6, dotted sign and lower loop are described. Item 2 records that the reviewer could not confirm m. The false-start idea *bizo-* is new, marked as a hypothesis and not used.
7. **Status line (minor): fixed.** The header no longer says "read letter by letter".
