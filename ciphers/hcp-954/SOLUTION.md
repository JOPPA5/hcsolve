# hcp-954 – Solution (Claude Opus 5.5, 2026-11-03)

HC Portal cryptogram 954, `cpc_1902-07-06_DE_Heide_DE_Jever_martha-03` (T. Schrödel collection).
Postcard posted at Heide (Holstein) on 6 July 1902 (arrival stamp 7.7.02), addressed in plain
German Kurrent to "Fräulein Martha Ihnken, bei Frau Wwe. Ihnken, Jever (Oldenburg)". The
message on the picture side (yellow rose / river landscape, publisher number 2832) is written in
pencil as numbers. No published solution of this card was found (portal status Not solved, no
attachment; a short web search found nothing for this card). All work here is by Claude Opus 5.5;
there was no earlier work on this number.

## Cipher type and key

Simple monoalphabetic number substitution (register label MASC): each letter is its position
in a 25-letter alphabet without J.

    A1 B2 C3 D4 E5 F6 G7 H8 I9 K10 L11 M12 N13 O14 P15 Q16 R17 S18 T19 U20 V21 W22 X23 Y24 Z25

Evidence for the J-less alphabet: K=10 (Karten, Dank), N=13, O=14, R=17, S=18, T=19, U=20, W=22,
Z=25 (zu) all sit one below the A=1..26 values. Letters used on the card: A B C D E F G H I K L M N
O R S T U W Z. Umlaut ü is written as 20 with two dots above (für, Grüße). ß is written as SZ
(18 25). Slashes drawn on the card divide words; the dots between numbers are separators with no
letter value. The sign shaped like "x" (in "1x 3 8" = DOCH and "13 x 11" in FREUNDLICHE) is this
writer's figure 4.

## Transcription

`work/transcription.txt` (read by Claude Opus 5.5 from the un-converted original
`work/hires/..._pic.jpg`, enlarged crops in `work/crops/`). 12 lines, 140 numbers.

## Command (from the repo root)

    python3 -I ciphers/hcp-954/work/decode.py

It checks the SHA-256 of the four images, decodes the transcription line by line, prints the
letter stream and checks that the word division below reproduces it exactly.

## Plaintext (German)

    Besten Dank für deine lieben Karten. Wie sehne ich mich zu dir, meine gute M.!
    Ich liebe dich doch so sehr. Meinen Brief hast du doch erhalten?
    Freundliche Grüße [written GRÜSZE], ewig dein Carl.

Letter stream: BESTENDANKFÜRDEINELIEBENKARTENWIESEHNEICHMICHZUDIRMEINEGUTEM ICHLIEBEDICHDOCHSOSEHR
MEINENBRIEFHASTDUDOCHERHALTENFREUNDLICHEGRÜSZEEWIGDEINCARL

## English

Many thanks for your dear cards. How I long for you, my good M.! I love you so very much. You
did get my letter, didn't you? Kind regards, forever your Carl.

## Slovak

Srdečná vďaka za tvoje milé pohľadnice. Ako veľmi po tebe túžim, moja dobrá M.! Veď ťa tak
veľmi ľúbim. Môj list si predsa dostala? Priateľské pozdravy, navždy tvoj Carl.

## Uncertainties

1. "M." (12 followed by a dot, end of line 4) is read as the initial of Martha; it could be any
   M-name or abbreviation. The cipher value itself is clear.
2. GRÜSZE, line 10: "7 17 20̈ 18 2" are clear; the 5 of 25 is faint and stands on the edge of
   a printed leaf, followed by a darker 5 whose top stroke runs on into a slash. 18 25 5 = SZE
   (sz for ß) is the only reading that gives a word; "18 2 5" would give SBE. The second figure of
   25 is therefore partly a word-sense call.
3. HAST, line 7: the first figure is an angular, tall 8 (it looks a little like ß); 8 = H gives
   "hast". This rests partly on word sense; 11 (L, "last") would not fit the visible shape or the
   sentence.
4. DOCH, line 8: "1x" read as 14 (x = this writer's 4, also in FREUNDLICHE) and the 3 is
   corrected over another stroke. The word is clear from context and the other DOCH (line 5).
5. "DEIN CARL": no slash between the two words; division by sense. "Carl" is the signature,
   read literally.
6. The address side is plain writing, not cipher. Its last line (the street, apparently
   "...Elisabeth..." under the HCPortal watermark) is not fully legible and is not part of the
   message. Nothing could be inspected under the 5-Pfennig stamp (scan only); no hidden writing is
   visible at the edges or in the picture.

## Why I believe it is correct

Every one of the 140 numbers decodes under one fixed key with no unused or conflicting values;
the result is fluent, period-appropriate German (sz for ß, ü marked by dots on the number) with
word divisions matching the slashes drawn on the card, and it fits a love-card to Fräulein Martha
Ihnken. No letter needed restoration beyond the disclosed partial figures in points 2–4.

## Response to review 1

Review 1 verdict ACCEPT, four minor findings. All addressed; the decoded letters are unchanged.

1. Number count – fixed. The transcription holds 140 number tokens (recounted by script);
   "147" was a slip and is corrected to 140 in both places above.
2. Position of the "?" – fixed. On the hi-res scan (review/work/c_mid.png) the question mark
   stands at the right end of line 8, after "...19 5 13" (ERHALTEN?), next to the rose. It is
   moved there in work/transcription.txt. `python3 -I ciphers/hcp-954/work/decode.py` re-run
   from the repo root: four SHA-256 checks OK, same letter stream, segmentation assert passes,
   line 8 now prints "DOCH / ERHALTEN?".
3. Steganography / stamp – agreed. In view of the human's remark (2026-11-03) that cards of the
   Jolánka series in this collection nearly always have a hidden message under the stamp, I
   re-inspected the address side of this card (work/hires/..._adr.jpg): the 5-Pfennig
   Germania stamp is still attached and cancelled HEIDE 6.7.02; no pencil or ink marks emerge
   from under its edges, and no writing is visible along the card edges or in the picture
   other than the number message. Whether something is written under the stamp cannot be
   determined from the scan. The type therefore stays MASC (not MASC + Steganography), and the
   report states the limitation.
4. GRÜSZE ending – kept. The report states that the faint second figure of 25 in GRÜSZE is the
   one sign call that rests on word sense (uncertainty 2).
