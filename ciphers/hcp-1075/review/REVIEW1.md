ACCEPT

# Review 1 — hcp-1075 (American Morse postcard, Akron, Ohio, to Ezra W. Sipple, Meyersdale, Pa.)

Reviewer: Claude Opus 5.5, 2026-11-03. Round 1 (DONE1).

## What I verified and how

1. Solver command. `python3 -I ciphers/hcp-1075/work/decode.py` from the repo root runs,
   checks hashes and prints
   `RECD YOUR CARD THIS AM I WILL WRITE SOON MY ADDRESS IS 457 CARROLL ST AKRON OHIO`
   (17 words, 64 signs), identical to the plaintext claimed in SOLUTION.md.

2. Independent transcription and decode. I read every row of the Morse block again from my
   own crops of `work/hires/cpc_--_USA__USA___adr.jpg` (review/work/r1_*.png … r8z.png,
   s2.png, s4.png, s6.png, s8.png; scripts crops.py, crop2.py, stack.py) and decoded my own
   reading with an independently written American-Morse table (review/work/my_decode.py).
   Output, with literal values for the disputed signs:
   `RECD YOUR CARD THIS AM OWILL WRITE SOON MY ADDRESS IS 457 CARROLL ST AKRONOHIO`
   The only differences from the solver are exactly the points the solver disclosed: the
   first sign of row 4 is two dots with a gap (~18 display units) between this writer's I
   (~11) and O (~26), and no comma stands between it and WILL, nor between AKRON and OHIO.
   "I WILL" is the only sensible reading. Every other sign agrees with the solver's
   transcript, row by row:
   - row 1 `. .. | . | .. . | -.. ,  .. .. | . .` RECD YO — confirmed;
   - row 2 U R , C A R D , — confirmed (C spaced `.. .`, R `. ..`);
   - row 3 T H I S , A M , — confirmed;
   - row 4 I W I L L , W R — confirmed; the L dashes are of middle length, as disclosed;
   - row 5 I T E , S O O N , M — confirmed; the second O is drawn tight (I-like), as disclosed;
   - row 6 Y , A D D R E S S , I S , — confirmed, including the caret-inserted second D
     (`-..` written above the line) and the wide first pair of Y;
   - row 7 `....- | --- | --..` = 4 5 7 in American numerals, then C A R R O L L with two
     clearly long L dashes — confirmed;
   - row 8 S T , A K R O N O H I O — confirmed.

3. OHIO under the collector stamp. I located the dark blobs in the stamp area with my own
   connected-component script (review/work/blobs.py). Ten ink blobs: x = 2694, 2788 | 2862,
   2893, 2931, 2973 | 3091, 3118 | 3216, 3283 (hi-res px), minimum grey 60–127, against
   151–154 for the stamp letters. The faintest one (x 2694, min 127, small) is the only one in
   doubt; it lies on the sloping row line (y 2032, extrapolated row ~2030), has the
   green-black ink colour in a 2.2x crop (r8y.png), and sits inside the stamp word, not at a
   separator position. Grouping by gaps gives O (94) H (31/38/42) I (27) O (67) = OHIO;
   without that dot the row would read E H I O, which is nonsense. Ink reading accepted.

4. Key and coverage. American landline Morse reads all 64 signs; no sign is unused or
   unmapped. Spaced-dot letters (C, O, R, Y), the long L, and numerals 5 = `---`,
   7 = `--..` exclude International Morse. Key agrees with FINAL sister hcp-1453.

5. Plain parts. Picture side (my crops n1–n5.png): "No 547 Carroll St / akron ohio",
   "I have not forgot the code but do Not / remember the Noo on the Bx card", corner
   "547 Carroll" and initials "J. N S." (N or W). All as reported. Stamp box on the address
   side: only the printed Tuck trademark; nothing written. No hidden or upside-down writing
   seen on either side (the picture-side note is open writing, not steganography).

6. Language and context. Ordinary period American English postcard ("Rec'd your card this
   a.m."). Tuck Raphotype card of Akron City Hospital (completed 1902), Akron address, a
   recipient in Meyersdale, Pa. — coherent. Register type MASC/Morse is an allowed label.

## Findings

1. (minor) Notation mismatch: the transcription table in SOLUTION.md writes the WILL dashes
   as `-*  -*`, while work/transcript.json and decode.py use `=` (long L). The decode is
   right only because the JSON says `=`; the table should say `=*` (or explain that the
   dashes are read as L by word sense) so the two do not contradict.

2. (minor) House number. The Morse clearly says 457; the plain note twice writes 547
   (first digit a looped 5, possibly 8 — I see the same form in both places). The solver
   discloses this. The report and normalised plaintext should keep "457" as the decipherment
   but state the conflict next to it, not only in the uncertainty list.

3. (minor) Published-solution check. The portal links Schrödel, "Cryptographic postcards",
   HistoCrypt 2021 (ecp.ep.liu.se/…/166). NOTES says nothing was looked up beyond the
   portal. I fetched only the abstract, which does not mention this card. A quick look at
   the PDF for this card (Akron / Sipple / Morse) should be recorded in SOURCES.md.

4. (minor) Literal vs read forms. For full transparency the solver could print, beside the
   normalised text, the literal letter string "O WILL … SOIN … AKRONOHIO" (as my script
   does), so a reader sees which three letters rest on word sense. Already described in
   prose; not a blocker.

No blocker or major finding. The reading is correct and the four word-sense points are all
disclosed honestly.

## What I could not verify

- The full HistoCrypt 2021 paper (only the abstract was read).
- Whether 457 or 547 Carroll St was the real address, and the identity of "J. N. S."
  (or "J. W. S.") — the card gives no date or postmark.
- The meaning of "Bx" in "the Bx card".
