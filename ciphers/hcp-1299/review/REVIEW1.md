REVISE

# Review 1 of HCP1299 (reviewer: Claude Opus 5.5, 2026-10-30)

The key and nearly all of the reading stand. Six letters in the ledger and one omitted interlinear sign are wrong, and they are not cosmetic: fixing them dissolves two of the three "not understood" items (*gyalka*, *oj ha*, and the object-less *Csinálom*) and reverses the sense of the closing clause. Concrete fixes are listed below; no new cipher work is needed.

## What I verified and how

- **Command.** `python3 -I ciphers/hcp-1299/work/decode.py` runs; all four SHA-256 hashes OK. A script compared its output with SOLUTION.md: all 38 literal rows and the normalized text match. It prints **775** signs; SOLUTION.md says 776 (finding 6).
- **Independent decoding.** `review/work/independent_decode.py` decodes the ledger through the key file of HCP1216 (`work/graphic-key.json`), not the solver's dict: every token maps, the key covers the ciphertext, and no value differs from the solver's. It then diffs the ledger against `review/work/my_reading.txt`, my own row-by-row reading.
- **Pixels.** All rows read from 1.2x panels of the un-converted scan (`review/work/p1`–`p8.png`), plus 3–8x crops of every blot, every disclosed doubt, rows 18, 19, 21, 27–29, the stamp block and the right edge (`review/work/*.png`). Result: **6 letters differ**, in 4 places:

```
18 'sitaz' e -> a        18 'tazez' e -> a        21 'hader' a -> e
27 'nekcs' in -> od      29 'aztfe' (nothing) -> l (interlinear)
```

- **Formula counts.** hogy 10, édesem 5, szívem 4, higyje el 2, becses sorait 2: as claimed.
- **Disclosed restorations.** Row 4 *[t][u][d]o* (`k4.png`): three over-inked signs, outlines compatible; acceptable as disclosed. Row 13 *rai[t]* (`k13.png`): the blot looks more like F than gamma, probably overwriting; sense requires t; disclosed. Row 18 *[n]incs* (`k18.png`): acceptable. Row 29 blot: wholly hidden, as disclosed. E1 *v* under the address flourish, and S1 *i*: acceptable. Stamp block S1–S8 and E1 read as in the ledger. Row 3 *ss* is really two right bowls, not cs (`k3.png`). Row 22 *boldognak* has k, not g (`k22.png`).
- **Language and context.** Period Hungarian love-letter prose, with this writer's habits. Sender Feri, Tóth Jolánka, Jászárokszállás and formulas fit the family. The portal shows no solution, and I found no sign of a borrowed one. The solver disclosed that the reading was not blind.

## Findings

1. **major. Row 27 *Csinálom* is misread; it is *csodálom* ("I am surprised").** The ledger has `CS i 2 = ~ Q 3`. In `cmp_x.png` the sign read n is a short upper-left stroke with a clearly longer stroke running below it: the d form, matching the d of *édesem* in the same row (`cmp_d.png`) and row 1 (`cmp_d2.png`), and unlike the two equal parallel strokes of n in *szívemnek* (`cmp_n.png`). The sign read i has no dot, which SOLUTION.md itself admits; it is the o loop (the same inked form as the o of *-lom*). Fix: `CS Q 4 = ~ Q 3`. The solver's "*csonálom* is no word" tested only n. The brief's warning about d/n stroke length applies exactly here.
2. **major. Rows 27–28 *oj ha / már* is a wrong word division: *oj hamar* = *oly hamar*, "so quickly".** All signs are as the ledger has them; only the split across the line end is wrong. With finding 1 the sentence parses at once: *Csodálom, édesem, hogy oly hamar belenyugszik, hogy ha egy [k]icsit esetleg késik a lapom, abból kell azt feltételezni, hogy…* Uncertainty 2 disappears.
3. **major. Rows 18–19: *az ezen gyalka* is *az az an|gyalka*, "that little angel".** Both signs ledgered three-bar are clearly **two** bars (`z_azaz.png`; compare the three bars in `cmp_d.png`). The vertical at the second one is the card's printed divider, not a stroke. Fix: `= Z = Z = 2` = *a z a z a n*, then row 19 *gyalka*, a word broken over the line. *az az angyalka, a melyik e sorokat írja, hogy szívemhez ölelhetném*: "that little angel who writes these lines, so that I could press her to my heart". The solver's guess of "a hand" and the untranslated word both go, and "it" in the translations becomes "her". The family supports it: HCP1302 has *kis angyalka*, also split over rows, and HCP1307 has *angyalom*.
4. **major. Row 29: the translation inserts a negation that is not on the card and reverses the sense.** The signs are `… S Q: 2 Y # 2 # + # ~ # T L # 2 #`, *könyene felejtene* (`z_kony.png`, `z_r29b.png`): no n before *e*. The solver normalizes *kön[n]ye[n] [n]e felejtene* and translates "would not forget easily", listing this among "writer's spellings… none affecting sense", where it plainly does affect sense. The natural reading is *könnyen e[l]felejtene*, "would easily forget", or *könnyen felejtene* with a stray e; the writer also skipped this l in *fe-tételezni*. It is the very reproach he is rejecting, and it answers the printed verse on the picture side, *Nem tudnálak soha Tégedet feledni*. The verb is 3rd person, so it is either formal "you" or a slip for 1st-person *-ném*. The sense of the reproach favours "I", the late correspondent, but the card does not settle it; say so. The Hungarian, English and Slovak must all change.
5. **major. Row 29: the l of *feltételezni* is on the card, and the ledger omits it.** A small wave sign stands above the line between the *e* and the *t* (`t1.png`), an interlinear correction. SOLUTION.md says the l is "absent on the card, or under the same blot". It lies below row 28's *i*, is not that sign's dot, and has the wave form. Add it to the ledger marked as interlinear, and revise uncertainty 5. *fetételezni* with `[f]` stays a sense restoration for the blot only.
6. **minor. Row 21: the sign after r is three bars, not two.** The third bar is faint but present (`k21b.png`), so the literal is *d e r e z h e t n e*, *hadd érezhetne*, and the "*derázhetne*" mismatch in uncertainty 7 goes. Also correct the count: 776 in SOLUTION.md against 775 printed. With the l added it will be 776, but state the count the command prints.
7. **minor. Consequences to clean up.** Uncertainty 1 and 2 entries, the *Csinálom* remark, the title line "Two words are read sign by sign but not understood", the notes' dead-end list, the *Why it is correct* claim, and the *az ezen* in normalized text. Only *ojot* (row 10) remains truly unresolved; I confirm its signs and have no better reading. Row 24 *letha-*: the over-inked sign shows three lobes (`k24.png`) and may well be a corrected or clogged a; keep as disclosed.
8. **minor. The plain handwriting by the postmark should be transcribed, not skipped.** It reads about *Szép reményi…* with the end struck through (`plain.png`). It is not cipher, but it is written text on the card and belongs in the record, as a tentative reading. The picture-side verse should be quoted in full: *Óh milyen boldogság / Szeretni, szeretni! / Nem tudnálak soha / Tégedet feledni.*

## Suggested reading of the affected passages (for the solver to verify)

- *Csak ezt sajnáltam, hogy miért nincs it[t] az az an|gyalka, a melyik e sorokat írja, hogy szívemhez ölelhetném, hogy had[d] érezhetné teljesen boldognak magát.*
- *Csodálom, édesem, hogy oj[=oly] hamar belenyugszik, hogy ha egy [k]icsit esetleg késik a lapom, ab[b]ól kel[l] azt [f]eltételezni, hogy kön[n]yen e[l]felejtene, ha a sors szétválasztana ben[n]ünket.*
- English: "I am surprised, darling, that you so quickly accept that if my card is perhaps a little late, one must conclude from it that [you/I] would easily forget if fate parted us."

## What I could not verify

- No native Hungarian check; the idiom of *belenyugszik, hogy* and the subject of *felejtene* are my judgement.
- I did not count bars at high zoom on every a/e of the card. Those I sampled at high zoom were right except for the three in the diff above, so a full a/e pass by the solver is worthwhile; two of the three errors sat in words the solver could not understand.
- h/p calls rest on word sense, as disclosed. Row 18 *it/ott* stays open.
- The postmark date is illegible to me as well, so the card stays undated. Portal state and the register check were taken from `source/metadata.md` and the orchestrator's note.
