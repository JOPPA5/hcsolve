# hcp-1047 – solution (round 1)

Card: HC Portal cryptogram 1047, `cpc_1909-07-24_DE_Freiburg-(Schlesien)_DE_Hier_fritzlehmann-05`, T. Schrödel collection.
Postmark FREIBURG (SCHLESIEN) 24.7.09, Germania 5 Pf. Address side in plain Kurrent: "An Herrn Fritz Lehmann, Hier,
Alte Bahnhofstr. No 29" (street name read loosely, "Bahnhof" partly on word sense; not part of the cipher).
Picture side: printed photo card "Der Herzenschmied" (B.N.K. 3278/7) with a printed four-line verse; no handwriting found.

Portal status: Not solved; no transcription or solution attached. Transcription and decipherment are my own
(Claude Opus 5.5, 2026-11-03), read from work/hires/. No earlier work existed in this directory. The key is the one
already established on the Lehmann sister cards hcp-1113 and hcp-1134 (same recipient, same signature "Susi", same hand
and number style), which I tested on this card rather than assumed. No published solution of this card was found or used.

## Cipher type and key

Number substitution (MASC), German. 25-letter alphabet without J: A=2, B=3, C=4, D=5, E=6, F=7, G=8, H=9, I=10, K=11,
L=12, M=13, N=14, O=15, P=16, Q=17, R=18, S=19, T=20, U=21, V=22, W=23, X=24, Y=25, Z=26 (1 unused).
Dots separate numbers, dashes separate words, a double tick over a number marks an umlaut (21" = Ü), a bar over a number
doubles it (13 with bar = MM), and "+" is used as a clause separator (comma).

Every number on the card maps to a letter of a German word; no number is left over.

## Command

    python3 -I ciphers/hcp-1047/work/decode.py

(from the repo root) – checks the SHA-256 of both source scans and the hi-res address scan, then decodes
work/transcription.txt. Output:

    LIEBES L SATZCHEN
    SOLLTE ES SCHLIMMER
    GEWORDEN SEIN, WAS
    ICH NICHT HOFFE
    SO GEHE WIEDER
    ZUM ARZT,
    ES GRÜSZT UND
    KÜSZT DICH
    DENE SUSI

## Plaintext

As written: LIEBES L SATZCHEN – SOLLTE ES SCHLIMMER GEWORDEN SEIN, WAS ICH NICHT HOFFE, SO GEHE WIEDER ZUM ARZT,
ES GRÜSZT UND KÜSZT DICH DENE SUSI

Normalised German: "Liebes [L.] Schätzchen! Sollte es schlimmer geworden sein, was ich nicht hoffe, so gehe wieder zum Arzt.
Es grüßt und küßt dich deine Susi."

English: "Dear [L.] sweetheart! Should it have got worse, which I do not hope, then go to the doctor again.
Greetings and kisses, your Susi."

Slovak: "Milý [L.] poklad/miláčik! Ak by sa to zhoršilo, v čo nedúfam, tak choď znova k lekárovi.
Pozdravuje a bozkáva ťa tvoja Susi."

## Uncertainties and writer slips (all from the pixels)

1. Line 1, "12" standing alone between two dashes = L. Its purpose is unclear (an initial, perhaps for "Lehmann", or an
   abandoned start); reported literally. It is the only unexplained item.
2. Line 1, 19.2.20.26.4.9.6.14 = SATZCHEN: the writer omitted the CH of "Schätzchen" and wrote no umlaut on the 2. The 2 is
   overwritten in darker ink; its light tail is the writer's normal 2-tail, not an umlaut. "Schätzchen" is word sense
   (the sister card hcp-1134 by the same writer has the full 19.4.9.2".20.26.4.9.6.14).
3. Line 9, 5.6.14.6 = DENE: the I (10) of "deine" is missing; clearly four numbers on the scan. Normalised by word sense.
4. Several initial 1s (lines 1, 2, 9, and the 19 in line 1) and the 2 of ARZT (line 6) carry a dark lead-in or overwrite
   stroke that looks like a cross. Read as the digit itself because each gives the only fitting letter (L, S, S, A);
   none is a deletion. The only real deletion is a blotted "26" at the end of line 5, rewritten as the first number of line 6.
5. Line 3, last number: read 19, giving WAS. The second digit has a closed top loop like this writer's 9 but also a
   rightward base stroke like his 2, so it is a hybrid shape; the choice of 19 (WAS) over 12 (WAL) rests on word sense
   (corrected after review 1, finding 1).
6. Line 4, HOFFE: the first sign is a 9 with a tall loop that reaches above the line (looks like a 9 written over a 1).
7. The small tick after many 5s (15, 5) is this writer's 5 flourish, not an umlaut (it also appears in DICH and DENE).
8. GRÜSZT / KÜSZT: Z stands for ß, as on the sister cards.
9. Steganography check: the stamp is still affixed and shows no ink traces at its edges on the scan, so anything
   underneath cannot be inspected. The picture side carries only print. Edges: nothing found.

## Why I believe it is correct

- The whole number block (9 lines, 79 numbers) decodes to a coherent German message with the key already established on
  two sister cards to the same recipient; no number outside 2–26 occurs.
- The message fits the context: a short love note to Fritz Lehmann in the same town (local "Hier" address), signed
  "Susi" as on hcp-1113 and hcp-1134, and the mention of a doctor matches hcp-1060.
- The three irregularities (lone L, SATZCHEN, DENE) are single-letter-level writer slips, each disclosed above; no letter
  was restored.

## Response to review 1

Verdict ACCEPT, three minor findings; no number or letter of the reading changed.

1. Line 3, last number (19 vs 12). Agreed. I re-examined review/work/z_l3end.png and work/crops/rot.png: the second digit
   has a closed top loop but also a rightward base stroke like this writer's 2, unlike the clean 9s of 19.4.9 on line 2.
   Uncertainty 5 above now says the reading 19 = S (WAS) rests on word sense, not on the pixels alone. Transcription
   unchanged.
2. Cross-like lead-in strokes. Agreed and adopted. On work/crops/rot.png the crossed or overwritten first numbers are
   exactly those of Liebes (12), Schätzchen (19), Sollte (19), Arzt (2) and Susi (19), the words that are capitalised in
   German; no lowercase word (es, ich, gehe, dich, und …) carries one. They are the writer's capital mark, not deletions.
   The lone "12" between dashes on line 1 carries no such mark, which argues slightly against an initial such as "L(ehmann)";
   it stays the one unexplained sign.
3. Register type. Agreed: MASC (number substitution). Because the human flagged hidden messages under the stamp on another
   postcard series, I rechecked this card myself: the Germania 5 Pf stamp is still affixed and shows no ink at its edges
   or at the creased lower-left corner; the address side has only the plain address; on the hi-res picture side the marks
   on the man's shoulder and sleeve (crop of work/hires/..._pic.jpg) are spots, splashes and emulsion damage, not letters.
   No steganographic part found, so not "MASC + Steganography". Short role used in register-entry.txt.

Re-ran `python3 -I ciphers/hcp-1047/work/decode.py` after these edits: three hash checks OK, output identical to the
plaintext above.
