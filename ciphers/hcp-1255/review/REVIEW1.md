REVISE

# Review 1 of HCP1255 (Claude Opus 5.5, reviewer, 2026-11-01)

The decipherment stands: family key, cipher type, sender, addressee and nearly all of the text are confirmed. Concrete fixes are needed in one clause (row 5) and in five ledger tokens. Two uncertainty items describe the pixels wrongly. The card should not go to FINAL until they are fixed.

## What I verified and how

- **Command.** `python3 -I ciphers/hcp-1255/work/decode_opus.py` passes all four hashes. Its output is identical to the literal rows and normalized text in SOLUTION.md.
- **Independent decode.** `review/work/my_decode_rv.py` holds my own sign-class transcription of all 20 rows, made from `review/work/b*.png` and `z_*.png` (2.5x to 6x crops of the hires scan), plus the hcp-1216 key. It diffs against the solver ledger position by position. Sign counts agree in all 20 rows. There are 6 differences at 5 places, listed in findings 1 to 4. Everything else matches.
- **Machine check of bars and strokes.** `review/work/measure_rv.py` labels the ink components, counts the stacked bars and gives the height ratio of adjacent stroke pairs. Bar counts agree with the ledger, except at r07 pos 11, r10 pos 18 and r12 pos 15 and 17, which show the ledger wrong. At r15 pos 4 the script counts 2 and the ledger has E.
- **Key coverage.** Every sign on the card maps into the family key. No new sign value is needed. The hcp-1216 table was checked directly.
- **Language.** Period Hungarian with the family formulas: *Isten vele, a viszontlátásra*, *sírig hű*, *Csókolom számtalanszor*. It is coherent and not forced onto noise.
- **Sign checks of disclosed items.** I confirmed these on the crops:
  - r12 first sign (red bowl under the printed "Br")
  - r03 smudged t
  - r09 t in *újság*
  - r16 unusual s of *sírig*
  - r16 two marks over x (ű)
  - r18 *idi*, with two long strokes
  - r01 *keves*, chevron with no d
  - r20 *bovaban*, all clear
  - r11 final i past the rule
  - r05 final m past the rule
- **Paratext.** The plain stamp-box text and the address agree with the scan. The picture-side verse is printed, not cipher.
- **Honesty.** I saw no sign of a published solution being used. The portal attaches none (SOURCES.md).

## Findings

1. **major: row 5, *Igaza, d[e] sajnálom* is not the best reading, and the alternative is undisclosed.**
   - The pair before the blot (x≈240–290, y≈468 on the hires scan, `review/work/z_r5.png`) is two nearly equal strokes, 50 and 43 px, ratio 0.86.
   - That matches this writer's n pairs, whose ratio is about 0.83–1.10. It does not match his tall+short pairs, which measure 0.47–0.62.
   - It also does not match the d pairs I could measure, where the second stroke is longer: 1.25 (r18), 1.54 (r12, r19), 1.96 (r06).
   - As n, the row gives **igazan + blot + sajnalom**, i.e. *Igazán sajnálom, hogy nem vigyázott magára, de az megnyugtat…* ("I am truly sorry that you did not take care of yourself, but it reassures me…").
   - That is one simple sentence. The solver's reading gives an unmotivated "You are right" and then two adversative *de* in a row.
   - The solver's item 3 lists r5 *d* among the d cases without saying it is an equal-stroke pair. Item 2 says e is "the only letter that makes a word". That holds only if the preceding sign is d.
   - The blot has two tips on the right at bar-like heights, so a sign may lie under it. Nothing there can be read. It could be a filled or corrected sign, or a spill. I cannot prove which.
   - **Fix:** adopt *Igazán sajnálom* as the leading reading, or at the least give both readings, in all three languages. State that the blot is unread. Change the ledger token (`N` plus an unread sign, not `D [E]`).

2. **major: rows 10–11, the unexplained run is mistranscribed.** The sign group ending row 10 has three bars (`review/work/z_r10.png`: three pale bars, also counted 3 by the script), so it is **len**, not *lan*.
   - The literal text is `okvet-len len | len lan lemegyek`, i.e. the run is {len len lan}, not {lan len lan}.
   - The first *len* of row 10 also has an isolated mark above it. It is not recorded in the ledger or the notes.
   - **Fix:** ledger r10 pos 18 → E. Update SOLUTION item 1, the normalized text and all translations. Record the mark.
   - The run remains unexplained, which I accept as disclosed. The sentence reads without it, and I found no better reading. The second wave of row 11 does show the tail of a wave beyond the spot.

3. **major: row 12, *lamagy* is false; the pixels are plain *lemegy*.** Both signs have three clean bars (`review/work/z_r12.png`, script count 3 and 3). The ledger has A at pos 15 and 17. Item 4 lists this word as evidence for "two-bar e" with "literal *lamagy*", which is a misdescription, and the header claim "tokens record the bars SEEN" is untrue here.
   - **Fix:** ledger r12 pos 15 and 17 → E. Delete it from item 4.

4. **minor: rows 7 and 15, more wrong bar tokens.**
   - r07 pos 11, in *megnyugt?t*, is two clean bars (`z_r7.png`), so literal *megnyugtat*. Item 4 says "literally *megnyugtet* (three bars)", which is wrong, and the correct word needs no normalizing.
   - r15 pos 4 has two full bars plus a short slanted mark high on the right (`z_r15.png`). This looks like two bars with an acute mark, as at r09 pos 4, giving *látásr*. If the mark is taken as a short third bar, the sign is e. Either way, item 11's "literally latesr" should be disclosed as a choice.
   - **Fix:** ledger r07 pos 11 → A, and r15 pos 4 → A:acute or a stated alternative.

5. **minor: item 4's claim about two-bar e needs rewriting after findings 3 and 4.** Of its cases, only *köszönattel* (r02, confirmed two bars) and *bovaban* (r20) survive. The writer separates a and e much more reliably than item 4 implies. The same applies to the sentence in item 1 that "each a here may be e".

6. **minor: the key table omits gy.** The ledger uses GY (joined loop + descender), and hcp-1216 has it, but the table in SOLUTION.md lists only y. Add the row.

7. **minor: date.** Item 12 says the postmarks were not verified. In fact they partly support the date: day "11" is clear on the left postmark, and "912" on the right one (`z_stampd.png`). State this. The month stays unverified.

## What I could not verify

- What lies under the row 5 blot.
- The meaning of the run {len len lan}.
- The month on the postmarks.
- The first address word *Szépreményű* beyond a plausible reading of the script.
- Whether Feri is the same person as on HCP1216.
- The stroke-pair measurements are a small sample, and d in r18 is close to equal. Finding 1 is strong evidence, not proof. It rests on stroke shape plus sense, and the review treats it that way.

## Register entry

After the fixes the card qualifies as complete: one short run is unexplained and the rest reads.
