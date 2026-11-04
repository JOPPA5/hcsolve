# hcp-1036 — solution (Claude Opus 5.5, 2026-11-03)

Card: picture postcard (Verlag L. Brühl, Berlin SW, Dess. No. 217), posted at Stolp (Bahnpost / Zug, 12.8.[06]), arrival Cöslin 13.8.06. Addressed in plain Kurrent to "Fräulein Anna Schulz, Köslin, Gärtnerstraße 5". Portal status Not solved; no published solution found or attached. All work below is by Claude Opus 5.5; there is no earlier work on this number.

## Cipher type and key

Number substitution (MASC with numbers): each letter is replaced by its position in the 25-letter German alphabet without J, numbers separated by dots, words by wider gaps.

A1 B2 C3 D4 E5 F6 G7 H8 I9 K10 L11 M12 N13 O14 P15 Q16 R17 S18 T19 U20 V21 W22 X23 Y24 Z25

Numbers used: 1 3 4 5 6 7 8 9 10 11 12 13 14 17 18 19 20 22 25. The absence of J is confirmed by the text: 17 = R (HERZ, GRUSZ, FRIDA), 22 = W, 25 = Z, 12 = M, 13 = N — a plain A=1..26 alphabet would give "HEQY..." nonsense.

## Ciphertext (pencil, picture side, written sideways, first line on the printed "Gruss aus ......" dotted line)

```
Gruss aus 13.1.18.18.14.22.
8.5.17.25.11.9.3.8.5.13.  7.17.20.18.25.
18.5.13.4.5.19.  9.8.13.5.13.
6.17.9.4.1  12.9.18.3.8.10.5.
```

## Plaintext (German)

Gruss aus NASSOW
HERZLICHEN GRUSZ
SENDET IHNEN
FRIDA MISCHKE

Normalised: "Gruss aus Nassow. Herzlichen Gruß sendet Ihnen Frida Mischke."

Nassow is a village in Kreis Köslin, Pomerania (today Nosowo, Poland), fitting the Stolp railway postmark and the Köslin address. "GRUSZ" is the usual sz spelling of ß.

- English: "Greetings from Nassow. Frida Mischke sends you warm greetings."
- Slovak: "Pozdrav z Nassowa. Srdečný pozdrav Vám posiela Frida Mischke."

Printed caption in the picture (not enciphered, publisher's text): "Wie gerne dir zu Füssen." ("How gladly at your feet.")

## Command (run from repo root)

```
python3 -I ciphers/hcp-1036/work/decode.py
```

It checks the SHA-256 of the four images and prints the plaintext from work/transcription.txt with the key above.

## Uncertainties

- None in the ciphertext: every number was read on 3–4x enlargements of the hi-res scan (work/crops/left.png, mid.png, right.png). The 9 and 19 have a looped top like a 4/9; read as 9 and 19 because 4 is written open-topped elsewhere on the card (13.4.5, 9.4.1) and 19 = T in SENDET.
- The 12 in the surname has a 2 resembling a 9-loop at speed; 12 = M (MISCHKE) vs 19 = T ("TISCHKE"). Read 12 on the pixels (distinct 2 base stroke); the name itself is not checkable.
- Steganography: the stamp box was inspected; nothing is visible around the stamp or along the edges. Anything written under the stamp cannot be seen in the scans and is not claimed either way.
- Street name "Gärtnerstraße" in the plain address is a Kurrent reading; it does not affect the message.

## Why it is correct

All 44 numbers decode under one fixed key into fluent standard German postcard wording with a word gap at every gap on the card, a real place name matching the postmarks, and a signature. No sign is left over.

## Response to review 1

Reviewer verdict: ACCEPT (independent transcription identical in all 44 numbers; independent decoder confirms the 25-letter alphabet without J).

1. (minor) Word-final dots omitted in work/transcription.txt. Fixed: a comment line in work/transcription.txt now states that the writer puts a full stop after every number, including the last of each word, and that these dots are dropped there while the two-space gaps mark the word ends. The ciphertext block in this file already shows the dots. Re-ran `python3 -I ciphers/hcp-1036/work/decode.py`: "hashes OK" and the same four plaintext lines.
2. (minor) Register type. Agreed: the type is `MASC` (plain number substitution A1..Z25 without J). Regarding the note on stamp steganography (raised for the Hungarian Jolánka series): this is a German card from Pomerania; the stamp box and both sides were inspected by solver and reviewer and no hidden or extra writing is visible. Writing under the stamp cannot be checked in a scan, so `MASC + Steganography` is not claimed.
3. (minor) Posting place. Agreed and clarified: the Stolp railway postmark ("STOLP ... BAHN ... ZUG ... 12 8") is partly covered and shows no year; the year 1906 comes from the Cöslin arrival stamp of 13.8.06 (and the portal file name 1906-08-13).

No change to the reading or the key.
