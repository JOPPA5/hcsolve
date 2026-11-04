# hcp-983 — solution (Claude Opus 5.5, 2026-11-03)

All work on this card is by Claude Opus 5.5; there was no earlier solver work. No published solution was found or used (portal status Not solved, no attached transcription or solution).

## Card
Feldpost Easter postcard ("Beste Ostergrüsse", soldier with Pickelhaube and girl, publisher mark R 5204/3), addressed in Latin cursive (lateinische Schreibschrift, with German long ſ and u-bow habits) to "Fräulein Lina Botsch [portal: Botch] bei Herrn Geisendörfer in Endsee, Post Steinach a/E" (a/E most likely "an der Ens": Steinach an der Ens is the postal place for Endsee near Rothenburg ob der Tauber) (Endsee, Middle Franconia, Bavaria). Black military postmark "K.B. ..." (Königlich Bayerisch, WWI field post; the unit name and number in the ring are not legible enough to read). Message written sideways along the left half of the address side.

## Cipher type and key
Plain German verse followed by a two-line number substitution (MASC with numbers): the alphabet is numbered A=1 ... H=8, I/J=9, K=10, L=11, ..., R=17, S=18, T=19 (alphabet with I/J merged, so R/S/T fall one below the 26-letter count). Every number on the card fits this key; no letter after T occurs. Dots separate the numbers; wider gaps separate words.

Someone later pencilled block capitals above the numbers (J O H / H E R B S T and S C H T E J B E B T L D). The first line of pencil agrees with the key; the second is partly wrong (T for 17, B T L for 2.1.11). The pencil is a later reader's attempt, not part of the cipher, and the reading below ignores it.

## Ciphertext (from the pixels, card rotated 90° CCW, enlarged 2x)
```
9.14.8.  8.5.17.2.18.19.
18.3.8.17.5.9.2.5.  2.1.11.4.
```

## Plaintext (German)
Plain part (Latin cursive, not enciphered):
> Zum Zeichen daß ich dein gedenke, / Ich dir dieses Kärtchen sende, / Gruß und Kuß sendet Dir

Enciphered part:
> Joh. Herbst / Schreibe bald.

Full message: "Zum Zeichen daß ich dein gedenke, ich dir dieses Kärtchen sende. Gruß und Kuß sendet Dir Joh. Herbst. Schreibe bald."

English: "As a sign that I think of you, I send you this little card. Greetings and a kiss are sent to you by Joh[ann] Herbst. Write soon."

Slovak: "Na znak, že na teba myslím, posielam ti túto kartičku. Pozdrav a bozk ti posiela Joh[ann] Herbst. Napíš čoskoro."

## Command (run from the repo root)
```
python3 -I ciphers/hcp-983/work/decode.py
```
Checks the SHA-256 of all four scans, then decodes `work/transcription.txt` with the key. Output:
```
I/JOH HERBST
SCHREI/JBE BALD
```

## Uncertainties
- "9" is the merged I/J sign; "Joh." (J) and "Schreibe" (I) are chosen by word sense.
- "Joh." is an abbreviation (most likely Johann); the full name is not written.
- The digits 17 (handwritten 7 with a hook, looks like "1y") and the 2 in 2.1.11.4 (written like a "v") were compared with the other 7s and 2s on the card and are consistent; the decode BALD and SCHREIBE confirm them.
- "Gruß" and "Kuß" are written with the German u-bow (breve) over the u, which can look like "gräß"/"Käß" in the scan; word sense and the stock verse fix them. The final "ke" of "gedenke" is written below the line.
- Spelling of the surname in the address: the portal gives "Botch"; the pixels show "Botsch" with an overwritten letter. Not part of the cipher.
- The stamp box holds only a printed red triangle, the postmark and a few faint green offset specks (no letters). No hidden writing was seen on the picture side or along the edges at the available resolution. No stamp is present (field post), so nothing could be hidden under one.

## Why it is correct
Every number on the card decodes under one simple key into two coherent German phrases — a signature (Joh. Herbst) and the stock closing "Schreibe bald" — which fit the plain verse that precedes them ("Gruß und Kuß sendet Dir ..."). A soldier's Feldpost card with a ciphered name and request is typical of the period. The pencil annotation on line 1 independently agrees.

## Response to review 1

Verdict ACCEPT; all five minor findings addressed, no change to the reading.

1. Script misnamed (minor) – agreed. On review/work/verse12.png the letters e, h, r, n, d and the descending Z are Latin-cursive forms; only the long ſ in daß/Gruß/Kuß and the u-bow are German habits. "Kurrent" replaced by "Latin cursive" throughout SOLUTION.md; the report uses the corrected description.
2. "Post Steinach a/E" (minor) – agreed. The crop review/work/post.png shows "Steinach" (the a is overwritten) followed by "a/E"; Steinach an der Ens is the post office for Endsee, so the address now gives "an der Ens" as the likely expansion.
3. Unattested key tail in decode.py (minor) – fixed: ALPH in work/decode.py now stops at T (values 1–19), with a comment that 20 and above are unattested. Re-ran `python3 -I ciphers/hcp-983/work/decode.py`: hashes OK, output unchanged (I/JOH HERBST / SCHREI/JBE BALD).
4. Surname Botsch/Botach (minor) – agreed, remains disclosed as uncertain (pixels: "Bot" + overwritten letter(s) + "ch"; portal "Botch"). Not part of the cipher.
5. J/I by word sense, Joh. = Johann(es) (minor) – already disclosed; kept as is.

Stamp/steganography check (prompted also by the human's note that the Jolánka series often hides a message under the stamp): this card never carried a stamp (field post); the box holds the printed red triangle, the K.B. postmark and green specks without letter shapes, and the picture side has no handwriting. Type stays MASC, not MASC + Steganography.
