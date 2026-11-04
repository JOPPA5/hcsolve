ACCEPT

# Review 1 – hcp-1047 (reviewer: Claude Opus 5.5, 2026-11-03)

## What I verified and how

1. Solver command: `python3 -I ciphers/hcp-1047/work/decode.py` from the repo root. All three SHA-256 checks print OK and the
   output is exactly the plaintext claimed in SOLUTION.md (9 lines, LIEBES L SATZCHEN … DENE SUSI).
2. Independent transcription and decode: I rotated the hi-res address scan (work/hires/..._adr.jpg, 3469x2298) 90 degrees
   clockwise and read the whole 9-line number block myself from review/work/r0.png … r3.png, then zoomed the doubtful
   signs (review/work/z_l1mid.png, z_l2.png, z_l3end.png, z_l4end.png, z_l6.png, z_l9.png). My own transcription is in
   review/work/my_decode.py, which decodes it with A=2 … I=10, K=11 … Z=26 (no J). Its output is identical to the
   solver's (only a trailing space differs). My reading agrees with work/transcription.txt number for number.
3. Key coverage: 20 distinct numbers occur (2–15, 18–21, 23, 26), all inside 2–26; every number in the block maps to a
   letter of a German word. The key is fully determined by this card alone (a plain shifted alphabet giving coherent German
   over 79 numbers); it also agrees with the sister cards hcp-1113 and hcp-1134 (same signature "Susi", same opening
   "Liebes Schätzchen" on hcp-1134).
4. Specific signs checked on the pixels:
   - Line 2, 13 with an overbar = MM in SCHLIMMER: the bar is clearly visible over 13.
   - Line 5 end: a heavily blotted "26" after WIEDER, rewritten as the first number of line 6. Correctly omitted.
   - Lines 7–8: the double tick over 21 (Ü) in GRÜSZT and KÜSZT is clear.
   - Line 9: 5.6.14.6 = DENE, four numbers only, no 10 – the slip is real, not a misreading.
   - Line 1: 19.2 of SATZCHEN – crossed 1, a looped 9, then a heavy overwritten 2 with its usual light tail; no umlaut
     mark. CH really omitted.
   - Line 4: 9.15.7.7.6 = HOFFE; the first 9 has a tall loop as described.
5. Steganography (stamp, picture, edges), checked because of the human's note that a postcard series had hidden messages
   under the stamp: the Germania 5 Pf stamp is still affixed (review/work/z_stamp.png); its lower-left corner is creased/
   lifted but no ink is visible beneath it or at its edges. The picture side ("Der Herzenschmied", B.N.K. 3278/7) carries
   only print; the dark marks on the man's shoulder and sleeve (review/work/z_shirt.png) are water staining/emulsion damage,
   not writing. The address side holds only the plain Kurrent address. No hidden message found, so "MASC" (not
   "MASC + Steganography") is the right register type.
6. Plaintext quality: idiomatic German of the period ("Sollte es schlimmer geworden sein, was ich nicht hoffe, so gehe
   wieder zum Arzt. Es grüßt und küßt dich deine Susi"); a local love note to Fritz Lehmann, "Hier", Freiburg (Schlesien),
   1909, consistent with the Susi cards of the same series. Translations (EN, SK) are correct.
7. Sources: portal status Not solved, no attached transcription/solution; no published solution was used, and the solver
   says so.

## Findings

1. (minor) Line 3, last number: SOLUTION.md (uncertainty 5) says 12 (WAL) is "excluded on the pixels". On the enlargement
   (z_l3end.png) the second digit has a closed top loop but also a rightward base stroke like this writer's 2; it is a
   hybrid, not a clean 9 (compare the 9s in "19.4.9" on line 2, z_l2.png, which have no base stroke). The reading 19 = S
   (WAS) is right, but it rests on word sense; the wording should say so.
2. (minor) The "cross-like lead-in strokes" (uncertainty 4) follow a pattern the solver did not notice: they sit on the
   first number of exactly the words that are capitalised in German – Liebes (12), Schätzchen (19), Sollte (19), Arzt (2),
   Susi (19) – and on no lowercase word (es, ich, gehe, dich …). They look like the writer's capital-letter mark. This
   strengthens the reading (they are not deletions) and is worth one sentence. It also bears on the lone "12": it carries
   no such mark, which slightly argues against reading it as a capital initial ("Lehmann"); it stays the one unexplained
   sign, which is acceptable for a complete solution.
3. (minor) Register: type should be MASC (number substitution). No steganographic part was found (see 5 above), so the
   "MASC + Steganography" label the human mentioned for another series does not apply here. Use a short role such as
   "transcription, key transfer, decipherment by Claude Opus 5.5; independent AI review". The card is not in
   register-exclusions.json.

## What I could not verify

- What lies under the stamp: it is still affixed, and only the scan is available.
- The meaning of the lone "12" (L) on line 1.
- The street name in the address ("Alte Bahnhofstr."?) – it is not part of the cipher, and I did not check it in detail.
