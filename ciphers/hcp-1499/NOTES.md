# Triage
Address side custom symbol alphabet, fine/faint; no reliable transcript or key.
Picture side ordinary English letter; not treated as deciphered ciphertext.
No solved/partial plaintext claim for the cipher, no marker/register entry.
Switch to other postcards seeking clearer standard-system example.

## 2026-10-30 – Claude Opus 5.5 (solver): serious attempt, still PARTIAL (no marker)
Earlier triage (2026-10-26) was done by the OpenAI GPT solver; this session's work is new.

Material
- Downloaded the full-resolution address scan (see SOURCES.md) -> work/originals/. ~1.7x the "large" conversion.
- Reading orientation: rotate the address side 90 deg counter-clockwise (PIL rotate(90)); 10 lines,
  read top-to-bottom, the first line lies next to the printed divider, the last next to the left edge
  ("... 754"). Digits/# slant naturally in this orientation. Picture side is plain English
  ("Does this look familiar to you? ... the dance (ahem) ... I can tell you."), no cipher there.
- work/components.py: ink-component helper (binarised, rotated); thresholds <115 break faint strokes, so
  readings were made by eye on 4-5x gray crops instead.

Sign inventory (rot90 view): # (most frequent, ~18), short / and tall // pairs, 9, o, o with a high
dash/tick, 6/sigma with tick, 8, 2, 2 with a low dot, 3, 4, 5 (always with a high tick), 7, =, *, d, C, D,
mid dash -, dash with low dot -., ';'-shape (dot above a slash/hook), three-dot cluster, ':'-like end marks,
'"' at the end of line 10. Many marks are dots/ticks placed above-right or below-left of a sign, so it is
unclear whether they are diacritics of one letter or separate letters. This segmentation question is the
main blocker.

Tentative token transcription: work/tentative-tokens-v0.txt (my notation; NOT verified, word breaks by gaps).
Repeated units that look solid on the pixels:
- three-dot cluster + ';' + '#'  occurs 4x (lines 3,5,7,9);
- '= 9 //' (tall //) occurs 2x: '9 = 9//' (l.8) and '[3dots;#] = 9//' (l.9); '9' stands alone 4x;
- '6 # //' + dots (l.6), '3 / //' (l.5), '2 # #' (l.7), '# D' (l.5 end, l.10 start), '-. ; ...' 3x.
Hypotheses tried (none closes the text):
- [3dots;#]=THE, 9=A, '='=B, //=LL -> 'A BALL' / 'THE BALL' (fits the dance theme on the picture side);
- [3dots;#]=SHE, 9=I, '='=W -> 'I WILL' / 'SHE WILL', 6#//+dots = TELLS/SELLS;
- [3dots;#]=WHO, #=O (makes '#;'=OH, '#D'=OF/ON, '2##'=TOO).
  With any of these fixed, simulated annealing (work/anneal_substitution.py, 1:1 substitution, small
  English corpus from repo plaintexts + web2 dictionary) gives no English for the long words
  (e.g. '-. ; o o ; -. 5'', '* .2 d .2 9 -. o 4'). Also rejected: letter-number (A=1..), keyboard-shift,
  plain Morse for the dot/dash marks, Pigpen dot-count. Sister cards in the repo show no matching
  system (searched Wisconsin/Marion/Appleton and symbol keys).
Why it stops: the diacritic-vs-letter status of the dots/ticks and several sign identities (2 vs z vs 9,
o vs 6, short vs tall /) are not settled, so no single key reads the whole card. No plaintext is claimed.
Next steps for whoever continues: decide segmentation by testing the 'the ball'/'she will' cribs against
a larger English model; check whether marks systematically pair with base signs (o/o', 9/9., 2/.2, -/-.,
//;) as a 2-letters-per-base scheme; compare with other North-American 1908 HCP postcards.
No SOLUTION.md, no DONE marker, no register entry.
