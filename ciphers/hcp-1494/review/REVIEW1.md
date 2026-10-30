ACCEPT

# Review 1 — hcp-1494 (pc_hcp_175), reviewer Claude Opus 5.5, 2026-10-30

## What I verified and how

1. **The solver's command.** `python3 -I ciphers/hcp-1494/work/decode_v2.py` (run from the repo root):
   the source hashes match, and it prints 115 cipher signs, 2 with alternative readings and 4 marked as slips/extra signs.
   The printed literal and normalised text match the plaintext in SOLUTION.md word for word.
2. **My own transcription and decode.** I rotated source/address-large.jpg 90° and enlarged it 2–10x
   (review/work/crop.py, sub.py → full.png, l12.png, l34.png, tog.png, l78.png, last.png, qm.png, greet.png).
   I read every cipher sign again under my own glyph names and decoded with a key I rebuilt myself
   (review/work/my_decode.py). Output:
   `DEARD / ITISALONGTIM[8]AGO / IHEARDFROM / YOUHAVEYOUFORGGOTT / ENMEALLTOG[dark]GTHER /
   WORKINGEVERYDAY / LETMEHEARFROMYOU / IFYOUWANTTO / CLARENCE`.
   That is 115 signs and 22 sign types: 20 letter signs, plus the closed 8 in TIMH and the dark stroke, which
   are both disclosed slips. It agrees sign for sign with work/transcription-v2.txt.
3. **Key consistency.** Every sign maps to exactly one letter, and the key covers all of the ciphertext.
   No sign stands for two letters: 8=H in HEARD/HAVE/HEAR/THER, ε=E throughout, −=Y in all 6 places,
   =F in FROM ×2 and IF, and the cursive-D sign = W in WORKING and WANT.
4. **Transcription against the scan, row by row.** All 9 cipher rows and the signature are checked. The specific points:
   - Greeting: `2 ε 1 T 2 :`. The second 2 has no loop but is clearly a 2, followed by a colon, so DEAR D: is right.
   - TIME: the fourth sign is a closed 8, not ε (l12.png). It is disclosed as a writer slip.
   - FORGGOTTEN: two clear + signs (l34.png), as the solver states.
   - ALLTOGETHER: `% 0 + [heavy re-inked stroke with a flag, like 1/7] + % 8 ε T`. The pixels match the description
     (tog.png). Reading this as a garbled ALLTOGETHER is forced only in the sense that the word is certain from
     context, and the solver says so.
   - Final word: `% 0.` The 0 is an open circle, and a fainter, thinner tail has been added. Two 9-shaped marks sit
     under the % and the 0 (last.png). "TO" is the most natural reading of the body of the signs. The marks are
     disclosed and not decoded, which is correct.
   - Signature `C 5 1 T ε 6 c ε` = CLARENCE, which is clear.
5. **Language and context.** The text is idiomatic early-20th-century American English, and the cipher words interlock
   with the plain-hand words ("since I heard from you", "I am still at my old Place and working every day").
   A personal note between Crookston and Fertile, Minn. in 1915 is plausible. No names or dates in the ciphertext need checking.
6. **Honesty.** The portal shows no solution or transcription (according to SOURCES.md). The earlier GPT partial work is credited. All slips and
   uncertain points are listed.

## Findings

1. **minor:** SOLUTION.md says "One fixed 21-letter key". The key (key.json and the table) has 20 letters
   (A C D E F G H I K L M N O R S T U V W Y), and the list of unseen letters (B J P Q X Z) also implies 20. Please correct the count.
2. **minor:** A sentence in "Why I believe it is correct" is garbled: "8 = H in …; = F in FROM ×2 and IF; − Y in …".
   It should read "= stands for F …; − stands for Y …".
3. **minor:** The "?" after ALLTOGETHER has no dot and looks like the writer's 2 (D) (qm.png). It is a
   hook with a flat foot, and a question fits the sentence, so "?" is the right reading. The transcription should
   still say that it is a 2-like hook read as a question mark, not as cipher D.
4. **minor:** In the plain-hand address I read the surname as nearer "Fugleseth/Ingleseth" than "Jungleseth".
   Fugleseth is a Norwegian surname and fits Fertile, Minn. The solver already marks the surname as uncertain.
   Mentioning the alternative would be enough.
5. **minor:** The greeting "DEAR D" does not match the addressee Elvira. This is disclosed and cannot be resolved from the card.
   Leave it as an open point in the report.

## What I could not verify

- Whether the two 9-like marks under the last word were written by the same hand, or are a later correction (for example toward "WANT ME").
  Ink and stroke weight differ slightly (they are thinner and fainter). This is left open, as the solver did.
- The plain closing word above the signature. "Yours" is plausible but not securely legible.
- No identification of Clarence or of 715 Hunter St. (the street is presumably in Crookston). I made no external search.
- I did not re-open the portal page. I took its status and attachments from SOURCES.md and source/metadata.md.
