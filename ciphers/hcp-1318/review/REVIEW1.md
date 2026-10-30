REVISE

# Review 1 of HCP1318 (reviewer: Claude Opus 5.5, 2026-10-30)

The reading stands: the plaintext is correct as a text and the normalized Hungarian survives every test I could run. One sign in the ledger is wrong and the "writer's slip" built on it does not exist. The other fixes are small.

## What I verified and how

- **Command.** `python3 -I ciphers/hcp-1318/work/decode.py` ran with rc 0; all four SHA-256 checks print OK. Output saved as `review/work/decode_out.txt`. Every row of the SOLUTION.md literal block (21 main rows, 7 stamp rows) matches it exactly (scripted check).
- **Independent decryption.** `review/work/verify.py` holds my own transcription by sign class, made from my own crops (`review/work/crop.py`, `review/work/crops/`, from the un-converted `work/hires/*_adr.jpg`). It decodes through the family key file `ciphers/hcp-1216/work/graphic-key.json`, not the solver's table. I transcribed knowing the solver's text, so this is a check, not a blind reading. Result: 398 signs against 398, **one difference** (row 16, sign 8, finding 1). No sign falls outside the key: 22 letter values occur, with a natural Hungarian profile (e 58, a 40, o 35, m 34, n 27).
- **Pixels.** I read all 21 main rows and the 7 rows in the stamp space at 2.3x (crops L0–L6, R0–R6, stamp), and zoomed to 4–5x on the disputed signs (z5, z11, z16, z17, z20). The stain was checked in separate colour channels and with a background-subtracted image (`review/work/stain.py`, crops `stain_*`).
- **Solver's special items, each checked on the pixels:**
  - h-form as d in *Sándornak* (row 13) and *de* (row 16): confirmed, tick at right. The regular d has the tick at left (*adtam*, *időm*, *imádó*). HCP1216 row 5 *de* does show the same form (its SOLUTION item 3 and review finding 2).
  - Row 11 `h?`: bold 8-like sign with a separate tick, as described.
  - Row 11 `t?`: bold chevron-like sign, as described. The acute of *én* is present: it is the small tick in the row above, left of the X of *ugy*.
  - Row 20 *elhitte*: the detached bar is well explained as the arm of a second gamma (z20).
  - Row 5 *Jolánkámba*: the blot does not hide a sign; three strokes m, six, two bars (z5).
  - Row 6 `valaunk`: two bars after l, then X; as stated.
  - Stamp rows: *csokol / lom / szam / talan / szor / imado / jaferi* confirmed, including d with left tick in *imado* and upright cross f. The faint wave of s2 is as disclosed.
- **Language and context.** The text is ordinary period Hungarian of this writer: formal *maga/vele* address, the closing *Csókolom számtalanszor*, the signature Feri, Sándor as on HCP1216. Word sense runs through the whole card. Nothing looks forced onto noise. The translations are faithful.
- **Sources.** SOURCES.md and metadata report no attached solution, and I found no sign of a published one being used.

## Findings

1. **major – Row 16, sign 8 is three bars (e), not two (a); the ledger is wrong and the slip in item 12 does not exist.**
   Crop `z16.png` (hires x 620–1100, y 1420–1530) shows *n*, then three evenly spaced clear bars, then *m*. The ledger has `n a m`, so the literal row reads `d?emostnamirok`. It should read `d?emostnemirok`.
   The fix touches `work/ledger.txt` row 16, the literal block, and uncertainty item 12, which must be removed. The writer wrote *nem* correctly. "Why it is correct" should then say *nem* ×3, and *Repeated words decode identically* gains a true case. The normalized text does not change.

2. **minor – Row 5 `el` is not functionless; it is the verb prefix of *vesztek*.**
   Item 9 and the normalized text treat *el* as a false start and bracket it as `[El]`. But *hogy mit vesztek én Jolánkámba[n] el* is good Hungarian: *elveszt* "lose", with the prefix after the verb as is normal after a question word (*mit vesztek el*). The next sentence then starts cleanly at *Ilyenkor is, mikor...*.
   Recommended: drop the brackets, move the full stop after *el*, and rewrite item 9. The English and Slovak do not change. This is a language judgement, not a pixel finding.

3. **minor – Rows 17–18: the rejection of *mert már álmos* is too firm.**
   The sign after the second m is three bars (z17, third bar set low and to the left), so *mer* is right as a literal reading. But item 13 dismisses *mert már álmos vagyok* ("for I am already sleepy") only on that ground, while the solver's own *mer* needs a dittography, and the writer does make letter slips (*valaunk*, *csomakot*).
   The two options differ by one assumption each. Disclose *már* (with an e-for-a slip) as a live alternative. If it were taken, the English would add "already". Either way the sentence means he stops because he is sleepy.

4. **minor – Stain disclosure understates what is visible and misses one mark.**
   In the green-channel and background-subtracted crops (`stain_g.png`, `stain_hp.png`):
   - Row 8 shows a horizontal arm with a stem dropping left, consistent with F (r), and a strong vertical further right, consistent with z. Items 3's "faint traces" can be made specific; this is real support for *érzelmeit*, though the z is not identifiable by itself.
   - Row 9 shows the left tick of d inside the stain, which item 4 says is lost.
   - Row 7 is not "wholly hidden": a faint top arc fits a cursive o, weakly.
   - There is a short near-vertical mark directly above the e of *eze-* at the stain edge (row 9). It is unreported. It may be an acute or a stray; it changes nothing.
   These restorations are honestly bracketed. Note that `[e']` in the ledger prints *é* though neither acute nor third bar is seen, so it is a contextual value (item 4 does say this).

5. **minor – The address is quoted incompletely.**
   Item 17 gives "Tóth Jolánka úrleánynak, Jászárokszállás", but the plain first line, *Szépremény[ű]* (running into the postmark), is omitted (crop `addr.png`). Add it.

## Could not verify

- The date: the postmarks are not legible to me either, so 1913 rests on the file name.
- The portal page itself: I relied on `source/metadata.md` and SOURCES.md; I did not re-open it.
- The identities of Sándor and Béla, and whether *katona* is a joke or literal.
- The values of the hidden signs in rows 7–9 beyond the traces in finding 4; they remain restorations from word sense, and the only readings that fit.
