# Notes — 2026-10-26

User requested another easy unresolved target. Full three-tab inspection,
source downloaded. Arbitrary-symbol monoalphabetic candidate; some writing
overlaps a postal cancellation. Deferred after initial visual triage in
favour of a cleaner simple target. No claimed plaintext, no transcript
yet, no DONE/FINAL/register entry. No source image edited.

# 2026-10-30 — Claude Opus 5.5 (solver) — PARTIAL, no DONE1

Same physical card as HCP 1487 (pc_hcp_168; see ciphers/hcp-1487, where a
partial reading was made the same day by Claude Opus 5.5 using this card's
clean photo). Earlier triage here (metadata, source download) by an OpenAI
GPT solver (GPT-6 Astra / GPT-6.1 Sol), 2026-10-26.

Cipher: ad-hoc geometric signs, **homophonic** substitution (several signs
for some letters). Re-read every sign at 5-12x. New findings vs. hcp-1487:
- The "H" signs differ by inner strokes: H+1 short stroke (H1) = o,
  H+2 strokes (H2) = e, H+3 strokes (H3) = y, H with an inner x (HX) = u.
  (H family seems to carry vowels; plain H at the end is unresolved.)
- Bar with one dot/tick above (row 1, DOTUP) differs from the ÷ with dots
  above and below (row 6, DIV = n).
- Homophones: e = ∩+bar / H2; o = ∪ / H1; n = ∩ / ÷; r = □ / P-box /
  box with middle bar; y = H3 / box with dot; u = HX / ϕ-sign.
- Key and transcription: work/transcription.txt; decoder (checks hashes):
  `python3 -I ciphers/hcp-55/work/decode_partial.py`

Reading (row by row):
```
R0: [EYE] o.                       (unresolved greeting/abbreviation)
R1: most, d? i [~4-5 signs under postmark] o?
R2: int, you,
R3: again, for
R4: I am leaving                   (final g = V-like sign at the divider)
R5: on P.M. train
R6: for Greenport,
R7: will write
R8: you there.  [H]                (H = unencrypted? or cipher initial)
```
Probable sense: "[?]. Must (written 'most') disappoint you again, for I am
leaving on [the] P.M. train for Greenport. Will write you there. H."
Slovak: „Musím ťa znova sklamať, lebo odchádzam popoludňajším vlakom do
Greenportu. Napíšem ti odtiaľ. H."
"Greenport" (G R E E N P O R T, 9 signs) is what fixed H2, DIV, CIRC, H1.

Why it stops (no DONE1):
1. Row 1, word 2: after DOTUP (d?) and ⊣ (i) about 4-5 pencil signs lie under
   the heavy black postmark; only fragments (a vertical, a short bar) show,
   also on the hcp-1487 scan and with colour separation (JPEG chroma too
   coarse). "disappo|int" fits the context but would be a multi-letter
   restoration, which the standards forbid.
2. Row 0 (EYE + o) unresolved: EYE (flat oval with a line through) occurs
   once and matches no established sign.
3. Final "H" (partly behind the printed divider) unresolved: plain cipher
   sign or unencrypted initial.
4. Row 1 word 1 reads literally "most" (H1 = o, confirmed by Greenport);
   the sense wants "must" — writer's slip or a second H1 value, undecided.
No published solution found or used. Register: none (partial).
