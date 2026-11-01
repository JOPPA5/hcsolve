ACCEPT

# Review 1 of HCP1263 (Feri to Jolánka Tóth): reviewer Claude Opus 5.5, 2026-11-01

Verdict: **ACCEPT**. The cipher type, the key and the reading stand. I found no wrong word in the plaintext. Six minor points remain, and the solver should fix them before FINAL. The most useful one is finding 1: *bővebben*, not *bővebbet*.

## What I verified and how

1. **Solver's command.** `python3 -I ciphers/hcp-1263/work/decode.py` runs. All four SHA-256 checks print OK. The printed rows match the literal block in SOLUTION.md, 21 main rows plus 7 stamp-box rows.
2. **Independent transcription and decode.** `review/work/indep_decode.py` holds my own row-by-row reading in shape names, made from my own crops (`review/work/crop.py`, `crop2.py`, `crops/`; 2x bands of every row, 3.5x to 6x zooms of doubtful spots). The key values come from the table in HCP1216. Of 28 rows, 25 are identical to the solver's literal text. The three differences are shape versus word-sense calls:
   - row 8: my shape reading gives *be he önre*, the solver has *be de önre* (disclosed, his item 5);
   - stamp row 6: *lanszot* by shape, the solver has *lanszor* (not disclosed, finding 2);
   - stamp row 7: *ueri* by shape, the solver has *feri* (disclosed, his item 7).
3. **Coverage.** 357 tokens; every sign has a value. Two are flagged restorations (`[a]`, rows 19, 21). There is no stray or unassigned sign class.
4. **Literal versus normalized.** A difflib alignment of the literal text against `work/normalized.txt` shows 12 places where letters differ beyond accents. All are disclosed in items 13 to 15: *szereret*, *sajnaltomat*, *refezem*, *ebölafeny|kepemelelatot*, *mot*, *bovebbe*, *dogom*. Nothing was changed silently.
5. **Every restoration and word-sense call, on the pixels:**
   - Row 19 *holn[a]p*: pale top bar, pale middle stroke, heavy dark mass. Two versus three bars truly cannot be told apart. Disclosed correctly. *Holnap* is the only word.
   - Row 21 *v[a]n*: one clean top bar, then three close strokes. See finding 4. The final n is two thin, ink-starved strokes, still clearly two.
   - Row 17 digit 3: a flat top and an angular turn, pale ink. It stands near the s sign but is more angular than the s of row 21. Solver's call is reasonable and correctly marked as the weakest point. The next sign is h (long stroke, foot, right tick), then e with a clear acute, then gamma.
   - Row 8 *De*: long stroke with the tick on the right, then three bars. The bars are visible, so *ha* is excluded as he says. HCP1216's comparison crop shows d of *de* written in the same way, so the claim about the family holds.
   - Row 7 strikeover: pale bars under the dark x, two dots above: confirmed. See finding 3 on the undertext.
   - Row 4 closed 8-form k: confirmed. Row 16 deformed m: confirmed, three strokes with a K-like middle.
   - Row 6: F, three bars, cross, three bars, chevron-crossed form, three bars: confirmed sign by sign. The literal really is *refezem*, and *fejezem* is an interpretation, as disclosed.
   - Chevron-crossed z: the same form occurs in *bízom*, *számta* and *lanszor*, so the second z form is carried by three independent words.
   - Row 12 *lezö-*: the sign is the z (long arm), with a dot for ö above it.
   - Row 15, the sign after *egy*: three bars, *egyen*. My crop first looked like two; the top bar is just above that crop.
6. **Tested alternative that failed.** I tried to read an s joined to the o in row 14 (*most* in full) and an l joined in row 21 (*dolgom*). The arch on the o in row 14 also occurs on *írom* (row 13) and *szor* (stamp row 6), where no s can stand, so it belongs to the o. The open o in row 21 matches the one in row 5. The solver's *mot* and *dogom* stand.
7. **d/p/h claim.** Tick on the left for *kaptam, képem, lap, holnap* and *édes, majd, kedve, dolgot*; tick on the right for *hogy, hét, holnap*: confirmed. Only row 8 is the exception.
8. **Word checks.** The repetition counts claimed (*hogy* ×2, *megy-* ×3, *édesem* ×2, *majd* ×2) are right. The text runs across row breaks and is natural period Hungarian. Formal address, *Isten vele*, *csókolom számtalanszor*, the signature and *egyetlen reményem* all agree with HCP1216. Sound and spelling slips are the same kind as on sister cards.
9. **Picture side and address.** The printed poem *Sokszor úgy szeretnék sírni...* and the red mark on the woman's hair are as stated. The address *Szépremény… Tóth Jolánka úrleánynak Jász Árokszállás* is as stated. The postmark shows "913".
10. **Provenance.** `source/metadata.md` records Not solved and no attached solution. HCP1263 is not in `skip.txt` or `register-exclusions.json`. I saw no sign of an outside solution.

## Findings

1. **minor. *bővebbet* should be *bővebben*.** The literal is *boveb|be irok*. Either form needs one added letter, and SOLUTION item 15 picks t. But *bővebben* is the phrase this writer uses: HCP1252 and HCP1266 *majd legközelebb bővebben*, HCP1255 *majd vasárnap bővebben*, HCP1294 *majd szóval bővebben*. A search of the Jolánka family SOLUTION files found no *bővebbet*. "Majd holnap bővebben írok" is also the normal idiom ("I will write in more detail tomorrow"). Fix `work/normalized.txt`, the Hungarian text, item 15 and, lightly, the translations. The second bar group in row 20 is three bars with the lower two joined by a pen drag, so there is no sign for n; it is a dropped letter, as with the other omissions on this card.

2. **minor. Final sign of stamp row 6 has no crossbar.** At 4x (`crops/z_s57.png`) the last sign of *lanszor* is a stroke with a curved top and no middle bar: a gamma by shape, so literally *lanszot*. The ledger gives R without a note. Item 7 discusses the reverse case in stamp row 5 but not this one. *Számtalanszor* settles it. Add it to item 7 as a word-sense call.

3. **minor. Undertext in row 7 is more readable than stated.** Item 11 calls the pale sign under the first stroke of n "b or e-shaped, not readable". At 4x (`crops/z_r7.png`) it has an upper and a lower bowl and looks closest to the closed 8-form of k used in row 4. With the pale e below the ü, this suggests the writer first wrote *megyek* ("I am going") and changed it to *megyünk* ("we are going"). This is a suggestion, not a certainty. Mention it as possible.

4. **minor. Row 21 is not "the same kind of blot" as row 19.** Item 2 says so, but row 21 has no pink halo. It has a clean top bar and then three close strokes, so it looks retraced or overwritten (`crops/z_r21b.png`). The restoration stands. Correct the description.

5. **minor. The photograph argument is overread.** "Why it is correct", last bullet, offers the man on the picture side as support for *fényképemmel*. The picture side is a printed commercial series (number 3747/48 and a publisher's mark at the card edge), with a poem. A stock model is the likely subject. The words *fényképemmel ellátott* stand on the signs, not on this picture. Drop the argument or state that it is uncertain whether the card shows Feri.

6. **minor. Slovak grammar.** "jeden z týchto pohľadníc" should be "jednu z týchto pohľadníc", since *pohľadnica* is feminine.

## Could not verify

- The live portal state; I relied on `source/metadata.md` and the orchestrator's register check.
- The HistoCrypt paper linked on the portal; I did not read it for a published solution of this card.
- The day and month of the postmarks. The left postmark is unread and SOLUTION does not mention it.
- The digit in row 17 beyond doubt. 3 is the best reading; another small number is not fully excluded.
- Identity of Ilonka, and whether Berény is Jászberény; the subject of *nem megy le* stays open, as the solver says.
- That the f of *Feri* is a separate tilted-cross form. On this card the sign looks like the plain x; I did not compare the HCP1216 row 21 pixels. The signature rests on the family, as disclosed.
