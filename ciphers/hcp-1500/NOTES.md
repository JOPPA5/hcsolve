# Triage
Short mixed cursive letters/digits, working270-degree clockwise rotation.
No reliable cipher transcription yet. Do not treat tempting opening ARE YOU
as established; cursive shape identities and cipher type remain uncertain.
No plaintext/key/marker/register entry claimed. Move to1499 for easier trial.

## 2026-10-30 Claude Opus 5.5 (solver session) – serious attempt, still partial

Earlier triage above was by the GPT solver. I re-read the card from the pixels
(rotation 90 deg CCW of source/address-large.jpg, 3x enlargements in work/).
Working transcription: work/transcription.txt

    abc - ly; - xuder / comde - 13guf.? / h - lz - kncv - / 13g4hs - Pne. /
    pnvvx cn - / Sincely, / mn'yo.

No sister card in the repo (no other Edna Knight / Attica / Wyoming NY card).
The picture side carries no writing (only the portal watermark wheel).

Tests run (scripts in work/tests/, vocabulary = 3,621 English words that occur
>=2 times in this repo's solutions/reports and in /usr/share/dict/words):
- Caesar all 26 shifts and Atbash: nothing (shift +1 gives "i ma", isolated).
- Affine, all 312 keys: best 7/32 letters in words – noise.
- Keyword-mixed alphabets (every /usr/share/dict/words word as keyword, all
  offsets, both directions; kw.py): best 17/32 letters, gibberish.
- Columnar-written alphabets, QWERTY neighbour shifts: nothing.
- Progressive shifts (continuous and per-word reset): nothing.
- Vigenere/Beaufort with dictionary keywords (vig.py) and with every key of
  period 1-4 (vig2.py, digits skipped or consuming key): best 13/32, noise.
- Exhaustive word-pattern search (pat2.py) over the letter-only words
  abc ly xuder comde h lz kncv pne pnvvx cn: NO assignment exists with a
  one-to-one substitution, none with a many-to-one (homophonic) one, none
  with an involutive (pair-swap) one (pat3.py), and none with each word
  reversed. Sub-sets work only trivially (e.g. "a of rest ben betty se").
Conclusion: the card is not a word-preserving simple/homophonic/reciprocal
substitution of standard English with the dashes as word breaks, nor any
Caesar/affine/keyword/periodic variant. Possible reasons: misspelt or
abbreviated plaintext (note "Sincely"), the dashes not marking words, a
personal code (digits 1,3,4 inside words; shared prefix "13g" in 13guf and
13g4hs), or a non-English language. Not enough text (~45 signs) to break a
free system statistically. No plaintext claimed; no SOLUTION.md, no marker.
(scripts expect to be run from the repo root)
