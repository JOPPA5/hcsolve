ACCEPT

# Review 1 of HCP1285 (Tóth Jolánka card, 14 January 1912)

Reviewer: Claude Opus 5.5, 2026-10-30. The main message stands. All findings are minor. The closing fragment stays a conjecture, and SOLUTION.md already labels it so. Finding 4 should be added before this is called a complete reading.

## What I verified and how

- **Solver command.** `python3 -I ciphers/hcp-1285/work/decode.py` ran from the repo root. All four hashes printed OK, and `shasum -a 256` gave the same values as SOURCES.md. The output matches the literal rows and the normalized text in SOLUTION.md.
- **Independent decoding.** `review/work/own_decode.py` holds my own sign-class transcription, my own key dictionary (taken from the family legend, and checked against `hcp-1216/work/graphic-key.json`) and a row comparison with the ledger. Result: 0 of 14 rows differ, 219 letters. **This was not blind**: I had read the ledger before reading the pixels. The check shows that each ledger token agrees with what I see, not that two readers reached it separately.
- **Pixels.** I rotated the hires address scan (`review/work/crop.py`), made contact sheets of all ten full rows at about 1.85x (`sheets.py`, `sheet1–4.png`), and enlarged the contested places at 3–6x (`zoom*.py`, `z_*.png`): box, rows 10–11, row 1 Jolánkám, row 4 rózsa and *-tent*, row 5 *-jon*, row 7 F and heavy t, row 10 start, and the end of Szépremény. Every sign in rows 1–11 and the box was read this way; I found no sign the ledger misvalues in the main message.
- **Key coverage.** Every sign falls in the family key. No new values are needed, apart from the variant in finding 3.
- **Language and context.** The text is idiomatic Hungarian. *Ami engem illet* appears on HCP1301, and *Becses sorait* on HCP1212 and 1294. The rózsa clause, the viszontlátás sentence and the row breaks all carry over without forcing. *Mint e képen látható* fits the embracing couple on the picture side, and the printed verse there has *Szerelemről boldogságról*, which also echoes *ilyen boldogságot* (SOLUTION.md does not cite this; it is a further check). The postmark reads 912 JAN 14. The address is in plain hand, and the addressee and town agree.
- **Rózsa, row 4.** The sign after z is a slanted, wide right bowl, ending in the same small curl as the clean bowl two signs later, so s is sound.
- **Sources.** Portal status and absence of a solution are as stated in SOURCES.md. I did not re-render the portal.

## Findings

1. **Minor: row 1, *Jolánkám*, undisclosed blot and misdescribed insertion.** `z_r1_a.png`. The sign read a has two clear bars with a square ink blot directly under them. That could be a blotted third bar (e), and a rests on word sense. It is missing from uncertainty 4. The two small strokes stand at the head of the following k, the second touching it, not "above the a". An insertion of n is still the best reading. Fix: add the blot to uncertainty 4 and correct the position in uncertainty 3.

2. **Minor: row 10, first sign t, feathered and undisclosed.** `z_r10st.png`. It is a heavily bled gamma with a spur on its stem at crossbar height. Since three F-for-t slips are claimed elsewhere, say that gamma is read here by *látható*, and that the spur may be either bleed or the same slip.

3. **Minor: joined n is missing from the key table, and uncertainty 1 overstates "the same tail".** `z_r5_on.png`, `z_end.png`, `z_box.png`. In *nyíljon* and row 10, the sign after the loop is a joined tail with two arches; this is a cursive n outside the "two short strokes" class. The box tail after o has a single wave, like l. So the two tails are not the same shape, the pixels themselves separate *hon* from *kol*, and `hol` in row 10 is weaker than uncertainty 1 suggests. Fix: list the variant and correct the sentence.

4. **Minor: closing fragment, two points that should be added.**
   a. The last two box signs, read h and f, also look like the digits **14**. `z_box14.png`: a tall stroke; then a short tick, whose base appears to run on through a faint left extension of the crossbar into an upright. Together those can form a 4. The box is printed over with the stamp ring there and the ink has bled, so this cannot be settled, and the card is postmarked the 14th. I do not claim it is a date, but *h. F.* now has a named rival, and the "signature" may not exist. No abbreviation dots are visible in the box after h or f, which the normalization should not imply.
   b. The extra strokes on the row 10 loop include a blob and marks above it. These could be a double accent (ő), which would help *hőn*; it is not provable. Row 10–11 *hon es f* has no verb, and the box starts with *csókolja*. The natural conjecture is that the closing runs on across the two places: *Hőn és f[orrón] csókolja …* ("ardently and hotly kisses you"). The solver's normalization splits them into two pieces, leaving a fragment. It should at least mention this link, still as a conjecture.

5. **Minor: row 7 has a second explanation that needs no slip.** Literal `viszontlátásr` may be the formula *viszontlátásr[a]* with a dropped a. The writer uses that formula constantly, while the clean F there (`z_Fs.png`) shows no sign of an added bar. Grammatically *várom a viszontlátást* is still better, so *-t* can stay as the primary reading, but uncertainty 2 should list this. The two F in row 4 are likewise ordinary F in form; "gamma with an added bar" is a hypothesis about the writer, and the pixels show no later addition. The word *Istent* itself is not in doubt.

6. **Minor: small wording points.** "Why it is correct" lists `lát|ha|tó`; the card has one row break there, `látha|tó`. Uncertainty 6 could cite HCP1212 and 1294, where *Becses sorait* is written out, as support for *b[ecses]*. The address word stops at *Szépremény* followed by a pink smear (`z_szeprem.png`); sister cards have *Szépreményű*, so the end may have been wiped. Note this as possible.

## Could not verify

- The expansion of `hon esf` and `iahf`: these are conjectures, and the pixels cannot settle them.
- The values of the blots in rows 2 and 5.
- The struck-out start and *al szög* on the address side, beyond a general look; these are plain hand and not part of the cipher.
- Sender identity: no name stands on the card, and the *Feri* of normalization is family inference (disclosed).
- The second postmark was not read.
