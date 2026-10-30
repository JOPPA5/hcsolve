# Notes hcp-1338

2026-10-30: captured by Claude Opus 5.5 (orchestrator).

2026-10-30 (Claude Opus 5.5, solver): PARTIAL. No SOLUTION.md and no marker: the words cannot be established.

Transcription (read from work/hires/pc_hcp_19_adr.JPG, 3x crops; saved in work/transcription.txt), 35 letters, 5 lines:
  M O D A A H Q / S D H A M R / D H Y A G O A D / W E L T A F K / F Y E A A D C
Letters are separated by dots (a short dash before O in line 1). Sign calls are secure; the least certain are L in line 4 (could be read as a looped Z) and G in line 3. Line 4 E has three separate bars, so it is E here even though sister cards seem to have F at this place (see below). Address (Miss Wooster, The Grange, Shenley, Herts) is plain; Barnet postmark; picture side has only the printed title STILL WATERS. The wheel behind the scan is the portal watermark, not part of the card.

Conclusion: this is very probably an initial-letter abbreviation (each letter = first letter of one word), not a cipher with a recoverable key. Evidence:
- All six Wooster cards (1322, 1334-1337, 1339; contact-sheet reading only, provisional, not transcribed) open with the same run M O D A A H (Q) S D and close with near-identical runs ending D C (this card: W E L T A F K F Y E A A D C). Only the middle changes.
- hcp-1322 line 3 has "15 to 11" and line 2 ends in "(mms)", both in clear (checked on an enlarged crop). A time written in clear inside the letters fits abbreviated words.
- Dots after every letter, as for initials.
- work/tests.py: all 26 Caesar shifts, the same reversed, and Atbash give nothing. The statistics do not decide it (35 letters is too short: chi2 57.8 against word-initial frequencies, 64.0 against all-letter frequencies), so this test adds little.
A simple substitution of these short texts cannot be strictly excluded by statistics, but the 1322 clear time argues against it.

Why it stops: an initial has many possible expansions and there is no key, so no unique plaintext exists. Candidate expansions below are GUESSES, not a decipherment; none may be used as a reading:
- M O D = "My Own Darling" (salutation); the rest of it, A A H Q S D, unknown.
- H Y A G O A D: perhaps "Hope You Are Getting On All (right?) D..." - unverified, and D does not fit "right".
- closing F Y E A A D C: perhaps "From Your Ever A... And Devoted C."; C would be the sender's initial. W E L T A F K perhaps ends "...Love To A..., Fond Kisses". Unverified.
What could settle it: a private key from the correspondents, or a Wooster card with enough clear text to fix expansions. Comparing the full set of cards may narrow recurring groups but cannot prove words.
