ACCEPT

# Review 1 – hcp-1449 (pc_hcp_130)

Reviewer: Claude Opus 5.5 (claude-opus-5-5), 2026-10-30. Solver's claim: English written in Greek letters, reading "Have just seen ⟨μγ⟩ off / look out for him / tomorrow kind regards".

## What I verified and how

1. **Solver's command.** `python3 -I ciphers/hcp-1449/work/decode.py` (from repo root): all three source hashes `OK`; output
   `have just seen mg off / look out for him / tomorrow kind regards` – identical to SOLUTION.md.
2. **Independent transcription and decoder.** I rotated `source/address.jpg` myself (90° CCW, crop of the message area → `review/work/msg.png`, script `review/work/crops.py`) and made 4–8x autocontrast and thresholded crops (`review/work/crops2.py`, `crops3.py`; outputs `r*_*.png`, `w4b.png`, `just.png`, `L2a/L2b/L3a/L3b.png`, `him.png`, `off.png`, `out_thr2.png`, `regards_g.png`, `sig.png`). I transcribed the three lines sign by sign under my own glyph labels and decoded with my own key in `review/work/my_decode.py`:
   ```
   have just seen mg off
   look out for him
   tomorrow kind regards
   22 distinct glyph labels; 49 glyphs; all mapped: True
   ```
   Same result as the solver. Every glyph of the passage is covered; no sign is left over.
3. **Sign-by-sign checks on the pixels** (all confirmed):
   - *have*: Η (U-shape with bar, like the H of "him"), α (q-shaped), υ (v), η with an over-bar.
   - *just*: dotted Latin j with descender, ο, σ (o with a horizontal bar to the right, clearly different from the preceding ο), τ (`just.png`).
   - *seen*: σ, η̄, η̄, ν.
   - *word 4*: first glyph is the same w-like μ as the last glyph of "him" and the μ of "tomorrow"; second is the 3/y-shaped glyph with descender, the same form as γ in "regards" (`w4b.png`, `regards_g.png`). The watermark ring right of it contains no ink (thresholded crop `w4_thr.png`): nothing is hidden there.
   - *off*: ω + a ligatured pair of barred, descending φ (`off.png`).
   - *look*: λ, ω, ω (first one heavily inked), κ.
   - *out*: ω, a blotted/overwritten middle sign, τ (`L2b.png`, `out_thr2.png`). The core is round; ο is the natural reading but not proven by the pixels alone – disclosed by the solver (uncertainty 2).
   - *for*: tall looped f, ω, ρ. *him*: Η, ι, μ (`him.png`).
   - *tomorrow*: τ ω μ ω ρ ρ ω + final larger w with a flourish. *kind*: κ ι ν δ. *regards*: ρ η γ α ρ δ σ.
4. **Language and context.** All words are ordinary English; the message ("have just seen … off, look out for him tomorrow, kind regards") is coherent and fits a holiday card written at "Menai Bridge, Sat evening" (plain heading, visible on the scan) to Miss L. Thompson, Birmingham. Greek-letter English is a common Edwardian postcard practice. Key is internally consistent across repeats (o, s, r, h, e, d, m).
5. **Sources/honesty.** Portal status "Not solved", no attached transcription/solution (source/metadata.md, SOURCES.md). The earlier GPT triage is credited truthfully in NOTES.md and SOLUTION.md. No published solution is claimed or used.

## Findings

1. **minor – presentation of word 4.** The card has exactly two signs ⟨μγ⟩ followed directly by "off"; I confirmed there is no further ink. SOLUTION.md's normalised plaintext "Have just seen my(?) [ … ] off" inserts a gap that is not on the card, and the English translation line uses "[him / ⟨μγ⟩]", which is a third, different rendering. Please give one consistent rendering, e.g. literal "Have just seen ⟨mg⟩ off", with the alternatives "my [sic, noun omitted]" or initials "M.G." stated in the uncertainty, and keep "him" out of the bracket (it is not a reading of the signs). Note that the sender's monogram (`sig.png`) also looks like two capitals (H/J + M?); do not equate it with ⟨μγ⟩ without evidence.
2. **minor – γ doing double duty.** If "my" is preferred, the key must say γ = g and γ = y (one homophone-like glyph for two letters), since the decoder prints "mg". State this explicitly in the key table rather than only in prose.
3. **minor – allographs not recorded.** (a) e is written as η with an over-bar (η̄) in "have" and "seen"; the transcription silently drops the bar. (b) f appears in two forms: a tall looped ℓ-like f in "for" and barred, descending φ in the ligature of "off"; both are transcribed as φ. Neither affects the reading, but the transcription should note them since it claims to be glyph-faithful.
4. **minor – ν/υ.** Same v-shape read as v in "have" and n in "seen", "kind"; this is a context-only distinction (disclosed, uncertainty 3). Fine as it stands; just make the key table show it as one glyph with two values.

No blocker or major issues.

## What I could not verify

- The postmark and date (illegible; only "Sat evening" in the plain heading).
- The sender's identity / monogram and the meaning of ⟨μγ⟩ (initials vs. "my").
- The blotted middle sign of "out" beyond its round shape.
- Resolution is limited (1024 px card width, heavy portal watermark over the message); all judgments above were made on 4–8x enlargements.
