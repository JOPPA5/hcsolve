# Notes

2026-10-26: root capturedall3tabs+bothoriginals. Two shortlines ofcapitalLatinletters onpicturemargin, ordinaryaddress. Workingrotation270. No stabletranscriptor key yet. Possibletransposition/oddletterforms untested. No watcher.

## Offline bounded screen2026-10-26
Manual picture-margin transcript has33 candidateLatin positions, with explicit H/M, detachedbarT/I, andY/I alternatives (8variants). Current visualgroups:
P[H/M]S[T/I]NAA / HSEHH / GGTOG
AAA / AFN[Y/I]NJA / SFCEAN
Ordinaryaddress has no observedcipher. Underline/flourish preserved inpicture butnotassignedletter.

Saved transcription.json and a sourcehash-checking simple-screen.py. For eachvariant enumerated26uniformCaesarshifts, Atbash, total/rowreversal, odd/evenunpacking, rowinterleaving, andrailfencedecryption2–6rails. Outputsimple-screen.txt. No coherentcompleteEnglishreadingfoundbyvisualinspectionofthesecandidates. Isolatedshortwordshapesnotcountedasplaintext. This doesnotexcludeothertranspositions, nonLatininterpretation, missingstrokes, polyalphabeticorcustomsymbolmapping.

StraightmonoalphabeticsubstitutionwouldpreservefourconsecutiveA-likelabelsacrossbottomvisualgroupboundary; oddforEnglish butnotproofagainstcipherortranscript. RepeatedA-likeshapesmaynotbeordinaryletterA; key/transcriptionrequirefurtherwork. No verifiedplaintext, noSOLUTIONS/DONE1/FINAL/registerentry. No watcher/reviewer. Originalsourcehashespassed.

Workingcipher.jpg is crop ofwork/reading.jpg width610height130atx25y830; cipher-large.jpg scales4×. Enlargementsaddnodetail.

## 2026-10-30 Claude Opus 5.5 (solver) - re-check, still partial

Pixel check (source/picture.jpg margin x90-190, rotated 90 deg, 3-5x LANCZOS): confirms the earlier GPT reading
`PHSTNAA HSEHH GGTOG / AAA AFNYNJA SFCEAN` (33 signs). Notes on glyphs: every "A" is an open arch without crossbar
(only the A in SFCEAN may carry one); the T in PHST has a long detached overbar (T or I-with-bar); Y in AFNYNJA is clear;
the wavy line under the text and the "B"-like mark at bottom left are a flourish/signature, not ciphertext.
No sister card in the repo (grep for Deane / Wanstead / Leytonstone / Tuck "Fair Women" found nothing).

Structural observations:
- With the word division as written, "AAA" is a 3-letter word of one repeated letter, and the continuous string has
  AAAA; so no one-to-one letter substitution of English can produce this. A is either a null/marker, a many-to-one
  sign, or the text is not letter-level cipher (e.g. initial letters of words, which cannot be decoded uniquely).
- Removing the 8 A's leaves exactly 25 letters in five groups of five: PHSTN HSEHH GGTOG FNYNJ SFCEN. Striking, but
  only E,E,O,Y are vowels, and HSEHH (abcaa) / GGTOG (aabca) are not English word patterns, so it is not plain
  transposition either.

New screens (scripts in work/, all negative by inspection):
- Caesar 0-25 on the A-stripped 25 letters, forward and reversed.
- 5x5 grid of the A-stripped letters: rows/columns, both directions, all Caesar shifts vs /usr/share/dict/words
  (only hit: column "THONE", meaningless).
- Per-group Caesar (and reversed) dictionary test of every group: no word.
- Progressive (Trithemius-style) shifts +-1..3 and adjacent-pair swap: noise.
- work/keyword-screen.py: keyword-mixed alphabets from every dictionary word, enc/dec: noise.
- work/vig-screen.py: Vigenere / Beaufort / variant with every dictionary word of 3-8 letters (plus DEANE,
  MISSDEANE, LOVE, KISS): best outputs are random fragments (e.g. "...TRIBES...GONN..."), no coherent text.

Why it stops: 33 (or 25) signs are too few for statistical attack on a homophonic/keyed system, and the visible
structure (A runs) rules out the simple systems that this collection usually uses. No plaintext can be honestly
claimed. No SOLUTION.md, no marker, no register entry.
