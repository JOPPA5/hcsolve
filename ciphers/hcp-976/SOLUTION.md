# hcp-976 – solution (Claude Opus 5.5, 2026-11-03)

Card: Bad Brückenau (Kurpark) to Frau Emma Krumbholz, Heidelberg, Mittelstr. 18; postmark BRÜCKEN[AU] ... 10 (portal file name dates it 1910-03-21). Marked "1)" on both sides: card 1 of a numbered series. Sister card hcp-974 ("3)", same sender, same addressee) uses the same key (its first line `7238 Z50t18d 30t` = "Mein Zustand ist").

No published solution was found; the portal lists the card as Not solved with no attached transcription or solution. The transcription is my own (work/transcription.txt), read from work/hires/..._adr.jpg rotated 90 degrees clockwise.

## Cipher type and key

Number substitution (monoalphabetic, register label `MASC`) applied only to ten letters; all other letters are written in plain German Kurrent.

| digit | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 |
|---|---|---|---|---|---|---|---|---|---|---|
| letter | a | e | i | o | u | l | m | n | r | s |

The vowels a e i o u take 1–5, then l m n r s take 6 7 8 9 0. ü is 5 with a stroke above. Plain Kurrent letters on the card: H, d, c, h, t, D, V, B, k, N, r (in "Nr").

No steganography: the stamp has been removed and the area underneath is blank. The picture side has only the printed captions and the handwritten "1)".

## Command (run from repo root)

    python3 -I ciphers/hcp-976/work/decode.py

This checks the SHA-256 of the four source images and decodes work/transcription.txt with the key above.

## Plaintext (German)

    Meinen Lieben!            (plain Kurrent)
    Heute sende
    euch die Ansich-
    ten von Brück-
    enau. Diese ist
    die – Mitte, Nr. 2
    die linke Seite,
    + Nr. 3 die rech-
    te Seite. Onsre [= unsre]
    Vila steht

Running text: Meinen Lieben! Heute sende euch die Ansichten von Brückenau. Diese ist die Mitte, Nr. 2 die linke Seite, und [+] Nr. 3 die rechte Seite. Onsre (unsre) Vila steht … (the sentence continues on card 2, which is not in this collection entry).

English: My dear ones! Today I am sending you the views of Brückenau. This one is the middle, No. 2 the left side, and No. 3 the right side. Our villa stands …

Slovak: Moji milí! Dnes vám posielam pohľady z Brückenau. Toto je stred, č. 2 ľavá strana a č. 3 pravá strana. Naša vila stojí …

## Uncertainties

1. "Nr 2" / "Nr 3": read as a Kurrent capital N plus Kurrent r, followed by the plain numerals 2 and 3. Taken alone, the digits could be read as cipher e/i ("Nre", "Nri"), which would make no sense. The numeral reading rests on context: the card is marked "1)" and its sister is marked "3)". This is the only place where digits are not cipher.
2. "onsre": the signs are clearly 4 8 0 9 2 = o n s r e. 4 = o is fixed by "von" (V48). The word is read as a dialect or slip form of "unsre" (our). It is reported literally and not corrected.
3. "Vila" is written V-3-6-1 = Vila, with one l (sic). The thin stroke between 1 and the heavily retraced 0 of "steht" is treated as a connecting or retracing stroke, not a letter.
4. Line 8 "te [+H] Seite": before "Seite" there is a long dark stroke crossed by three vertical strokes. It looks like a cancelled H (Hälfte?) or a cross mark. It is left out of the plaintext. The dark "+" in the margin before "Nr 3" is read as the common handwritten abbreviation for "und" (and); it is rendered "und" in the running text and translations. Both marks, the heavily retraced 3 in "Seite" and the 0 of "steht" are in darker ink than the rest and may come from a later retracing pass by the writer or another hand; this cannot be decided from the scan. No matching cross could be found on the picture side.
5. Several letters were not decided by shape alone; for these the reading is fixed by the word: Kurrent c+h in "euch", "Ansichten", "rechte"; ck in "Brückenau"; k in "linke"; tt in "Mitte" (a doubled t ligature); d in "sende". The digits themselves are unambiguous.
6. The message breaks off ("steht …") because it continues on card 2 of the series.

## Why it is correct

- The key has a simple structure (vowels 1–5, then l m n r s) and is confirmed independently on sister card hcp-974.
- Every digit on the card decodes to fluent German that fits the card: the views of Brückenau, a numbered three-card series (1 = middle), and "Brückenau" matches the place on the picture and the postmark.
- No digit is left undecoded, and no sign gets two values (apart from the numerals in "Nr 2/3", which are disclosed).

## Credit

Transcription, key reconstruction and decipherment by Claude Opus 5.5 (2026-11-03). No earlier work on this number.

## Response to review 1

Verdict ACCEPT. All three findings are minor; none changes a decoded letter.

1. "+" before "Nr 3" = "und": agreed and fixed. Looking again at work/crops/msg_rot.png, the "+" stands at the line start exactly where the conjunction belongs ("Nr. 2 die linke Seite, + Nr. 3 die rechte Seite"). The running German text now reads "und [+]", the English "and", the Slovak "a"; uncertainty 4 states the reading. The line-by-line transcription keeps the literal "+".
2. Darker ink of the cross-mark, the "+", the retraced 3 in "Seite" and the 0 in "steht": agreed; added to uncertainty 4 as a possible later retracing pass whose author cannot be determined. The cross-mark stays out of the plaintext.
3. "Die"/"Von" capitals in decoder output: the transcription uses D and V for the writer's looped capital-like forms; this is a transcription convention only. The report and the running text use normal German case (die, von, Mitte, Seite). No change to decode.py, so the reproduction output is unchanged.

Reproduction re-run after the edits (2026-11-03): `python3 -I ciphers/hcp-976/work/decode.py` prints "source hashes OK" and the same ten lines as before.

Stamp and picture side re-checked for hidden writing (prompted by the note that the Jolánka series hides messages under the stamp): the stamp box (review/work/stamp_enh.png) holds only paper residue and the postmark, and the picture side only printed captions and the "1)". Type stays `MASC`, not `MASC + Steganography`.
