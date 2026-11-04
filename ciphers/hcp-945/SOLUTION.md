# hcp-945 — solution (round 1)

Card: HC Portal cryptogram 945, `cpc_1898-04-30_DE_Hagen in Westfalen_DE_Malchow in Mecklenburg_` (T. Schrödel collection). Lithographed "Gruss aus Hagen i.W." card (Bahnhof, Kriegerdenkmal, Waldlust; Carl Schemmann, Bahnhofswirth). Posted HAGEN (WESTF.) 30.4.98, arrival MALCHOW (MECKL.) 1.5.98, addressed in plain Kurrent to "Fräulein Frieda Necker in Malchow in Mecklenburg". The cipher is four ink lines on the picture side, lower right.

Work: transcription, key reconstruction and decipherment by Claude Opus 5.5 (2026-11-03). No earlier work on this number; the portal shows Not solved with no transcription or solution attached. I did not run a web search for a published solution, and I did not use one.

## Cipher type and key

Monoalphabetic substitution (MASC) with Arabic digits and barred Roman numerals (over- and under-strokes added as decoration). Two plaintext letters have two signs each: e = II or IV, a = I or X. Letter i is written as its dot alone.

| sign (code in work/transcription.txt) | plain |
|---|---|
| `I` barred Roman I | a |
| `X` barred Roman X | a |
| `6` | b |
| `c` small c-shaped hook | c |
| `V` barred Roman V | d |
| `II` barred Roman II (once with a curled first stroke, in "Frieda") | e |
| `IV` barred IV, often written as one ligature that looks like a barred A or 4 | e |
| `F` large 7 with long descender | f |
| `8` | h |
| `.` dot on the baseline | i |
| `L` hooked sign like ʃ / ξ | l |
| `3` | m |
| `2` (also written with a filled loop, ℓ-like) | n |
| `4` | r |
| `S` small hooked sign like 7 or ʔ | s |
| `1` | t |
| `IIII` four strokes under one bar | u |
| `IIII:` the same with diaeresis | ü |

The key is in `work/key.json`. The signs for c, f, l and s occur only once or twice, so their values rest on the words they make.

## Command

From the repo root:

    python3 -I ciphers/hcp-945/work/decode.py

This checks the SHA-256 of both source images and both hi-res originals, then decodes `work/transcription.txt` with `work/key.json` and asserts the result.

## Transcription and plaintext

    3 IV . 2 IV / L . II 6 II / F 4 . II V I        meine liebe frieda
    4 IV . S II / 8 IV IIII 1 II / 2 X c 8          reise heute nach
    2 IV 8 IV . 3 / 8 IIII: S 1 II 2b               neheim hüsten
    V IV . 2 / II V IIII X 4 V                      dein eduard

German (capitals and punctuation added): **Meine liebe Frieda! Reise heute nach Neheim Hüsten. Dein Eduard.** (The card writes the two town names as two words; the hyphenated town Neheim-Hüsten only existed from 1941.)

English: My dear Frieda! (I am) travelling today to Neheim and Hüsten. Your Eduard.

Slovak: Moja milá Frieda! Cestujem dnes do Neheimu a Hüstenu. Tvoj Eduard.

Neheim and Hüsten are neighbouring towns on the Ruhr in the Sauerland (Arnsberg district), about 50 km east of Hagen. They merged as Neheim-Hüsten only in 1941, so in 1898 the writer named two neighbouring places. He may also have meant just the pair as a destination.

## Uncertainties

1. The final `n` of "Hüsten" (the sign 2 at the end of line 3) is written in a lighter brown ink. It looks like an addition or correction, possibly made later. It completes the word and is read as n.
2. Homophones: e has two signs (II and IV) and a has two signs (I and X). I treat the A-shaped ligature and the IV with a separate first stroke (end of "Meine", second sign of "Neheim") as one sign class. If they are separate signs, both still mean e, and the reading does not change.
3. The sign for d in "Frieda" is a heavier, curled V. I read it as the same V as in "Dein" and "Eduard".
4. Single-occurrence signs (c, f, l, b; m occurs twice, in "Meine" and "Neheim") rest on the words they make. The split between s (hook in "Reise" and "Hüsten") and t (flagged 1 in "heute" and "Hüsten") also rests partly on word sense: the two s-hooks are not identical, and the one in "Hüsten" is close in shape to the following 1. The words are ordinary and the place names fit the geography, so I see no competing reading.
5. Nothing is written in the stamp box on the address side that I can see. The stamp is still on the card, so I could not check beneath it. The pencil "22" and "100" are collector or dealer marks, not cipher.
6. The sender's surname and the relationship to Frieda Necker are not on the card.

## Why I believe it is correct

- Every sign on the card is used. The decipherment is 52 letters in 10 words, all ordinary German, with no residue.
- The first line, "Meine liebe Frieda", matches the addressee Frieda Necker on the address side.
- The place names Neheim and Hüsten are real neighbouring towns near Hagen, where the card was posted.
- Signs recur consistently: 8 = h in "heute", "nach", "Neheim" and "Hüsten". 2 = n in "Meine", "nach", "Neheim" and "Dein". The dot = i in six words. 4 = r in "Frieda", "Reise" and "Eduard". IIII = u in "heute" and "Eduard", with an umlaut for ü in "Hüsten". The two different hook signs in "Hüsten" (S, then 1) match s in "Reise" and t in "heute".

## Response to review 1

Verdict ACCEPT; four minor findings. I re-checked the picture side (the reviewer's enlarged crop review/work/l3mid.jpg and a crop of the cipher block from the hi-res original, work/cipher-block.jpg) and the full address side.

1. Second sign of "Neheim" (barred VI / IV variant). Agreed; it is already covered by Uncertainty 2. Both shapes are e-signs, so no change to the transcription or plaintext.
2. s / t resting on context. Fixed: Uncertainty 4 now names s and t explicitly. In "Hüsten" the first hook after the umlauted u is a heavier slanted stroke with a hook to the left, while the 1 next to it is short with a flag at the top; I keep s then t, which also gives the only German word.
3. Hyphenated "Neheim-Hüsten". Fixed: the German reading, the English and Slovak translations and the summary line printed by work/decode.py now give "Neheim Hüsten" as two names, as the card writes them, with the 1941 merger noted. Re-ran `python3 -I ciphers/hcp-945/work/decode.py`: hashes OK, assertion passes, same 52 letters.
4. Stamp box / steganography. Agreed. I looked again at the address side: the 5-Pfennig stamp is still affixed and cancelled HAGEN (WESTF.) 30.4.98; no writing shows around its edges, along the card edges or in the vignettes on the picture side. Nothing under the stamp can be checked from the scans, so the register type stays MASC, and the report says so.
