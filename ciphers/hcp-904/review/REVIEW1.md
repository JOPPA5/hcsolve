ACCEPT

# Review 1 of hcp-904 (Claude Opus 5.5 as reviewer, 2026-11-03)

Card: "Gruss aus Leipzig – Reichsgericht", Leipzig 1902, to Martin Laibelein, Wolferode b/ Eisleben (Pfarre). The claim is German written in Greek letters (a letter-for-letter MASC), six lines on the picture side.

## What I verified and how

1. **Solver command.** I ran `python3 -I ciphers/hcp-904/work/decode.py` from the repo root. All four SHA-256 checks print OK, and the six output lines match the plaintext claimed in SOLUTION.md exactly.
2. **Independent decryption.** `review/work/my_decode.py` holds my own transcription and a key I built separately from a plain Greek→Latin table, plus ʽ=h, Ϝ=W, Ι=J. Its output (`review/work/mine.txt`) matches the solver's output (`review/work/theirs.txt`) exactly according to `diff`. My transcription is also identical to `work/transcription.txt`. I did not read the card blind: I checked the solver's transcription sign by sign against the crops below and found nothing to change. No sign is left unmapped. The signs used are ʽ Α Β Γ Δ Ι Κ Λ Μ α β γ δ ε ζ ι κ λ μ ν ο ρ σ τ υ φ χ Ϝ. The key is a single, consistent alphabet with no homophones. The only phonetic liberties are υ for w ("beantuorten") and φ for v ("fier").
3. **Transcription against the pixels.** I made my own crops at 2–5x from `work/hires/..._pic.jpg`: `review/work/l0_*.png`, `l1_*.png`, `l2_*.png`, `l2r.png`, `l3a-c.png`, `l4a-c.png`, `l5a-b.png`, `l5start.png`, `l6start.png`, `blot1.png` and `sig.png`. I checked every word of all six lines:
   - L1 Κονντε λειδερ Δειν λιεβεν Βριεφ: clear. The final ν of Δειν has an extra stroke but is still ν.
   - L2 νιχτ μεʽρ βεαντυορτεν. φιερ Ϝοχεν σινδ: clear. The ρ of φιερ is partly blotted but visible.
   - L3 αβε[ρ] λανγ, καννστ Δυ μιρ κεινε ανδε[ρ]: two blotted signs, both disclosed (see findings).
   - L4 Αδρ. ανγεβεν? σονστ μυστ Δυ Διχ σχον σο λανγε γε-: clear.
   - L5 δυλδιγεν. ʽαβε μιχ σεʽρ υβερ Δεινεν Βριεφ γεφρευτ.: clear apart from the start (finding 2).
   - L6 ʽερζλιχεν Γρυσσ υ Κυσσ Δεινε τρ. Ιε??ι.: the ʽ is written as the same large hook as in ʽαβε, on the line with a dot above it. The ζ is z-shaped with a cross stroke. The Γ is written T-shaped.
4. **Plaintext quality.** The text is coherent German of about 1900 from a private correspondent: an apology for a late reply, a request for another address, and a closing "herzlichen Gruss u Kuss Deine tr. ...". The small grammatical slips ("Dein lieben", "must", "geduldigen") are plausible for the writer and are transcribed as written, not normalised away. "L. M." fits the recipient's first name, Martin, from the address side.
5. **Other sides.** On the address side the Kurrent address is plain, with no cipher. The picture side shows no other handwriting: the marks in the sky are printing or ink smudges, not letters. The stamp has not been lifted, so nothing can be said about writing under it. The solver states this.
6. **Sources.** Portal status is Not solved and no solution is attached. The solver reports that no published solution was used, and I found no sign that one was. Number 904 is not listed in skip.txt or register-exclusions.json.

## Findings

1. **minor** – The initial of line 1 is under a solid triangular blot (`review/work/blot1.png`). Its outline fits Λ, but a filled Δ cannot be ruled out, which would give "D. M." (for example "Dein M."). The solver discloses this and reads Λ from context. The report should name Δ as the alternative explicitly, not only "4, Δ or Λ" in passing, and should make clear that "Lieber Martin" is an expansion.
2. **minor** – In line 5, the first three signs of "δυλδιγεν" (`review/work/l5start.png`) are smudged and heavily overwritten: δ and υ blurred, λ almost solid. They are still readable as δ υ λ, and the word "geduldigen" confirms them. The transcription gives them without any mark, though. Add a note that these signs are smudged and partly confirmed by word sense.
3. **minor** – In the key table, Γ in "Γρυσσ" is drawn T-shaped and could be mistaken for τ/Τ. "Gruss" settles it, but the table should mention the variant. Likewise, the ʽ at the start of "ʽερζλιχεν" is a free-standing hook with a dot above it, and could be misread as ι or ε.
4. **minor** – The signature reads "Ιε??ι". The 3rd sign is ν/η-like with a cross stroke, and the 4th is a ϑ/δ-like loop (`review/work/sig.png`). Leaving it unresolved is honest. Since it is a single name, the card can still count as complete under this run's rule (one unread word, rest reads). If a reading is offered, it should be marked as a guess.
5. **minor (register)** – The plain label `MASC` is the right type. I found no steganography: the address side is plain and nothing is hidden in the picture. The writing under the stamp was not checked, so `MASC + Steganography` is not justified for this card.

## What I could not verify

- Whether anything is written under the stamp, since it was not lifted and only the scan is available.
- The identity of the sender (Je..i) and the full form of the line-1 initial.
- Whether "ande[r]" was followed by an e at the right edge. The blot and the card edge make this impossible to see, but the meaning is the same either way.
