REVISE

# Review 1 of HCP1307 — Claude Opus 5.5, 2026-10-30

The reading stands: Jolánka-family key, Hungarian, Feri to Jolánka Tóth, whole card. One sign in the ledger is not on the card (finding 1), and that needs a concrete fix before FINAL. Nothing else changes the text.

## What I verified and how

- **Solver's command.** `python3 -I ciphers/hcp-1307/work/decode.py` ran from the repo root. All 4 hashes OK. Its output equals the literal block and the normalized text in SOLUTION.md. It reports 592 signs.
- **Independent decode.** `review/work/mine.txt` is my own row-by-row transcription in my own sign-class names, read from my crops of the un-converted original (`review/work/crop.py`, `review/work/crops/`, 1.3x to 6x). `review/work/my_read.py` decodes it with the key from the hcp-1216 table and diffs it against the ledger through a separate token map. Result: 591 signs against 592. 31 of 32 rows are identical; only row 26 differs (finding 1). I had seen the solver's text before transcribing, so this is not a blind reading. The disagreement in row 26 shows it was not a copy.
- **Key.** It is the hcp-1216 key unchanged. Every sign has a value; no nulls or leftovers. The key covers all 26 main rows and 6 stamp rows, including the two rows along the bottom edge. No rows are missed, and rows 25 and 26 do run on under the address.
- **Contested items on the pixels:**
  - Row 2, *várt*: a dark F over an earlier sign, with the chevron's long leg running into it from the left and one short low bar beneath. Solver's account holds. The acute above the a of *vá-* is real.
  - Row 7, *jajt*: both signs are the inverted T, and neither is the upright cross of row 26 *fogja* or stamp *Feri*. The literal reading is right and *fájt* is an emendation, as disclosed. I have no better reading.
  - Row 19, *mihez*: the sign after h shows two bars and a smudge, as disclosed.
  - Row 21: the sign after *magá-* is a gamma inside a brown stain. Its top bar slopes down to the right. The two-bar a with its tick before it is clear.
  - Row 25, *itjon*: a clear gamma, not an F. The slip is real and is disclosed.
  - Row 25, *lapot*: the h/p sign has a blot at the foot of the long stroke and a separate tick. The reading holds.
  - Stamp row 1: after the last o one stroke runs into the torn edge of the stamp paper. m is a restoration, correctly marked; only the family formula and sense say m rather than n.
  - The other stamp rows end before the stamp fragment, so nothing else is hidden there.
- **Ordinary rows.** I read every row sign by sign (rows 3 to 24 at 1.9x to 3x). Stroke counts for m and n agree throughout, including the doubled groups *nem mentem*, *édesem mér*, *szeretem ma*, and row 8 *sem*.
- **d/n.** No d/n call on this card depends on word sense. The d's long stroke with its detached upper tick is distinct from the two-stroke n wherever I checked.
- **Language.** Period love-letter Hungarian with the family's formal address. The grammar works (*elveszteném*, *teljesíteni fogja*). The English and Slovak follow the Hungarian without inventing anything. Sister hcp-1216 has the same signature formula, the same *ojan*, *mer* and the Rákospalota/Jászárokszállás setting.
- **Claimed counts.** *édesem* ×6, *hogy* ×5, *sorait* ×4, *magát* ×3, *mint* ×2 are all correct.
- **Picture side.** The printed verse and title are as stated. There is no cipher on it.
- **Sources.** No solution is attached in the capture. Nothing suggests a published solution was used. Key provenance is credited.

## Findings

1. **major — Row 26 ledger contains a sign that is not on the card.** The ledger has `T E ~ J E ) @ T E 2`, giving *teljesiteni*. On the card the inverted T is followed directly by the right bowl, with clean paper between them and no three-bar sign (`review/work/crops/t.png` at 6x, also `r26m.png`). The literal text is *teljsiteni*, a dropped letter of the kind this writer makes. The e was supplied from the word but sits in a ledger described as "one token per written sign" and in the literal block, with no `^` and no entry under Uncertainties. Normalized *teljesíteni* is still right; it just needs to be shown as [e]. Fix:
   - delete the token from row 26 of `work/ledger.txt`;
   - correct the literal block in SOLUTION.md;
   - change 592 to 591 in both places in SOLUTION.md (decode.py recounts by itself);
   - add the item to Uncertainties, and show the normalized text as *telj[e]síteni* or list it among the writer's spellings.

2. **minor — Row 26 acute missing from the ledger.** A short stroke above the two-bar a of *vá-rom* sits low among the descenders of row 25, near hires (212, 1990); see `review/work/crops/r25l.png` and `r26a.png`. By the ledger's own rule (accents marked where seen) the token should be `='`, and the literal should read *várom*.

3. **minor — "one restored sign" understates what is supplied.** The header and Uncertainties speak of one restored sign, but the normalized text also supplies [t] in *mer[t]* and the word [ha]; finding 1 adds [e]. [ha] is disclosed in item 6. *mer[t]* appears only in the spelling list. The literal has a clear tick on the e, *mér*, so it is not identical with the *mer* of hcp-1216, and colloquial *mér* "why" should at least be ruled out in a line; the causal sense is the better one. Separate "hidden sign" (one) from "letters and words supplied by the editor" (the list).

4. **minor — two soft spots not mentioned.**
   - Row 1: the fifth sign, the e of the repeated *-re-*, is much fainter than its neighbours. Item 2 of Uncertainties treats *szereretet* as firm. Mention the faintness, since it may be a wiped slip.
   - Row 5: the h/p sign of *nehezen* has its long stroke under a dark blot, with only the tick clean. Word sense decides it. Add it to item 8.

## What I could not verify

- The date (cancel blank) and the identity of Feri beyond the formula and place parallels.
- The clear word above the cancel. I read *Szépme…* and no further, and no sister card helps. The solver's caution is fair.
- ö against ő: the card does not distinguish them, as stated.
- The sign hidden under the stamp fragment.
- The portal page and the register check, which I did not repeat; I relied on the capture in `source/metadata.md` and the orchestrator's check.
