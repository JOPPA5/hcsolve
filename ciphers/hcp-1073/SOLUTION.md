# hcp-1073 — solution (round 1)

Card: HC Portal cryptogram 1073, cpc_1910-07-13_DE_Aschersleben_DE_Hier_hugocarl-01 (T. Schrödel collection).
Picture postcard (woman in profile, "Ser. 115/2"), 5-Pfennig Germania stamp, cancelled ASCHERSLEBEN 13.7.10.
Portal status Not solved; no transcription or solution attached; none found elsewhere. The portal has no
transcription, so the transcription in work/transcription.txt is my own, read from the hi-res scan.
Solved by Claude Opus 5.5 (2026-11-03); there was no earlier work on this number.

## Plain (unenciphered) parts

Address, in Kurrent: "Herrn Hugo Carl / Hier / Über den Steinen." ("Hier" = local delivery in
Aschersleben). "Über den Steinen" is a street in Aschersleben; the Kurrent "St" ligature and "einen" are
read from the strokes, but the call Steinen (not e.g. "Brunnen") also rests on word sense and the street name.

## Cipher

Simple monoalphabetic substitution (MASC), German, written sideways in the left half of the address side.
The scan must be turned 90 degrees counter-clockwise to read it. Separate words are followed by a slanted
stroke under the line (written as commas in the transcription).

Key (sign -> letter), token names as in work/transcription.txt:

| sign | letter | sign | letter |
|---|---|---|---|
| 2 | d | R (small triangle) | r |
| 3 | e | S (short hook) | s |
| 4 | f | Sd (s-like sign with two dots, once) | s |
| 5 | g / G | a (wide inverted V) | a |
| 6 | h (H) and b | N (dash) | n |
| 7 | i | + (cross) | ch |
| 8 | k / K | T (crossed A-like sign) | t |
| 9 | l / L | W (double loop) | w / W |
| B (tall l-shaped stroke) | B | P (rho-like loop, once) | st |
| o, u, ü | plain (o, u, ü) | 1000 | the number 1000 |

The digit part is systematic: the alphabet without j, starting c=1, gives d=2, e=3, f=4, g=5, h=6, i=7,
k=8, l=9. Only 2–9 occur. The vowels o, u, ü are written in plain Kurrent (u with its breve, ü with two
dots).

## Plaintext (German)

1000 Grüsse u. Küsse sendet Dir Dein Dissel. Hoffentlich bist du gesund! Wenn nicht, dann langweile
dich bitte nicht so u. denk ein bischen an deine Trude.

English: A thousand greetings and kisses are sent to you by your Dissel. I hope you are well! If not,
then please don't be so bored, and think a little of your Trude.

Slovak: Tisíc pozdravov a bozkov ti posiela tvoj(a) Dissel. Dúfam, že si zdravý! Ak nie, tak sa, prosím,
tak nenuď a mysli trochu na svoju Trude.

## Command (run from repo root)

    python3 -I ciphers/hcp-1073/work/decode.py

It checks the SHA-256 of the four images, decodes work/transcription.txt letter by letter with the
key, prints the result, and asserts that the word-divided plaintext uses exactly the decoded letters.

## Uncertainties

1. Sign 6 is a homograph: it is H in "Hoffentlich" (a large capital form) and b in "bist" and "bischen".
   By the digit scheme 6 = h; the b readings follow from word sense (the Kurrent b looks much like a 6).
   In work/decode.py this is done by a hard-coded position table SIX = {(5,0):'h', (5,11):'b', (8,0):'b'}
   (line, token index); these two b values are word-sense resolutions, not output of the key rule.
2. The short hook S (s) and the inverted V a (a) are similar. The a in "an" is clearly a wide inverted V;
   in "dann" and "langweile" the sign is narrower and the s/a split there rests partly on word sense.
3. P (rho-like sign) occurs only once, in "bist"; reading it as one sign for "st" (rather than s with t
   left out) rests on sense. Sd (s with two dots) occurs only once, in "bischen".
4. "B" (tall stroke) occurs only once, as the capital in "Bitte".
5. "Dissel" (line 4, 2 7 S S 3 9) is read letter by letter; it is a name or pet name and cannot be checked.
   "Dein Dissel" and "deine Trude" both look like signatures; whether they are the same person is unknown.
6. Spelling as written: "langweile" (for langweile dich = be bored), "bischen" (for bisschen).
7. Nothing is visible on the picture side apart from the print. The stamp is still on the card; any
   writing under it cannot be checked from the scans.

## Why I believe it is correct

Every sign on the card is decoded; the result is fluent, idiomatic German of the period (a typical
lover's postcard). The digit values follow a simple rule (c=1 ... l=9, j omitted) checked by 8 different
digits, and every recurring sign keeps its value across all occurrences (e = 3 in 18 places, n = dash in
16, i = 7 in 13, d = 2 in 11).

Note on the Slovak: the German has "Dein Dissel" (masculine/neuter Dein, not Deine), so the writer's gender
under the name Dissel is not established; "tvoj(a)" leaves it open. "deine Trude" is feminine.

## Response to review 1

Verdict ACCEPT, four minor findings; the reading is unchanged.

1. Transcription header direction. Fixed: work/transcription.txt line 1 now says the text runs
   top-to-bottom in columns on the scan, rightmost column first ("1000" at the top of the rightmost
   column), and that the card is turned 90 degrees counter-clockwise to read it. Re-ran
   `python3 -I ciphers/hcp-1073/work/decode.py`: four hash checks OK, assert OK, same plaintext.
2. Slovak "tvoja Dissel". Agreed and fixed: now "tvoj(a) Dissel", with a note above that "Dein Dissel"
   does not fix the writer's gender.
3. Hard-coded resolution of sign 6. Agreed: uncertainty 1 now names the position table SIX in decode.py
   and says the two b values are word-sense resolutions. The printed word-divided plaintext is tied to the
   decoded stream by the assert, so it cannot drift from the transcription.
4. Register type. Agreed: type MASC. I re-inspected the hi-res picture side and the address side for
   hidden writing (picture area, margins, edges, along the printed "Ser. 115/2" mark): only the printed
   photograph and publisher mark, the address and the cipher text. The stamp is still on the card, so
   writing under it cannot be checked; no steganographic part was found, so "MASC + Steganography" is not
   used.
