# HC Portal 1097 — vowel-to-digit substitution (Somerford, Nebraska, 1909)

Solver: Claude Opus 5.5, 2026-11-03. No earlier work exists on this number; no published solution of this card was found or used (portal status Not solved, no attached transcription or solution).

## Card

Picture postcard "A Quiet Spot" (park bridge). Addressed in plain pencil to "Mr. Ben Russell, Somerford, Nebr."; postmark SOMERFORD NOV 1 190(9) NEBR (year digit partly blurred; portal file name gives 1909-11-01); 1-cent Franklin stamp. Signed at the foot in cipher "(m15d)" = Maud (corrected after review 1). Language English. The whole message (left half of the address side, 11 lines) is enciphered; nothing on the picture side. The space under the stamp could not be inspected (only scans exist).

## Cipher type and key

Simple monoalphabetic substitution of the vowels only (register type: MASC). Consonants are written in clear.

| a | e | i | o | u |
|---|---|---|---|---|
| 1 | 2 | 3 | 4 | 5 |

The i-sign is written as a "3" that in places looks like a 9 or a small g; context separates it from the cursive g (g4t = got).

## Command (from repo root)

```sh
python3 -I ciphers/hcp-1097/work/decode.py
```

It checks the SHA-256 of both source scans, reads work/transcription.txt (my line-by-line reading of the hires scan work/hires/...__adr.jpg) and prints each line with its literal decoding plus the full literal plaintext.

## Transcription and literal decoding

```
y45 g4t b1ck h2r2            -> you got back here
3n th3s c45ntry 1g13n        -> in this country again
3 g4t y45r p4st c1rd         -> i got your post card
t4 l1t2 t4 1nsw2r2d          -> to late to answered
3t s4 3 w3ll s2nd y45        -> it so i will send you
th1s 4n2. 3 sp4s2            -> thas one. i spose
y45r v2ry b3sy!              -> your very bisy!
h5sk3ng c4rn n4w             -> husking corn now
3 1m 1t w4lsl2b2n            -> i am at wolsleben
n4w h4w l4ng 1r2             -> now how long are
y45 1g41ng t4 st1y?          -> you agoang to stay?
(m15d)                       -> (maud)   signature
```

## Plaintext (English, with editorial punctuation)

You got back here in this country again. I got your post card to[o] late to answered it, so I will send you this one. I spose you're very busy husking corn now. I am at Wolsleben now. How long are you a-going to stay?
(Maud)

(Spelling "to late", "to answered", "spose", "your" for "you're" is the writer's own and kept.)

## Slovak translation

Si zase späť tu v tomto kraji. Tvoju pohľadnicu som dostala príliš neskoro, aby som na ňu odpovedala, tak ti posielam túto. Asi máš veľa práce s lúpaním kukurice. Teraz som u Wolslebenovcov (vo Wolslebene). Ako dlho tam zostaneš?
(Maud)

## Uncertainties (all disclosed)

1. Line 6 "th1s": the third sign is a single vertical stroke, graphically the a-sign "1", so the literal decode is "thas". Read as "this" (writer used a plain undotted i, or slipped) — rests on word sense; line 2 spells the same word th3s correctly.
2. Line 11 "1g41ng": the fourth sign is again a vertical stroke (a pencil dot sits above the 4/stroke area). Literal "agoang"; read "agoing" (colloquial "a-going") on word sense.
3. Line 7 "b3sy": the sign after b is a heavy, overwritten 3 (perhaps over another figure). Literal "bisy"; read "busy" on word sense (either a writer's misspelling or a corrected sign).
4. "w4lsl2b2n" = Wolsleben, read letter by letter (w-o-l-s-l-e-b-e-n); taken as a family or place name (a German surname). Not verified against Nebraska records.
5. Signature "(m15d)" at the foot (revised after review 1; first read as a collector number "(n159)"): same pencil and hand as the message, centred under it. The first sign has the looped lead-in and humps of this writer's m in "1m" (line 9), not n; the last sign has a bowl with a slanting ascender like the d of "1nsw2r2d" and "c1rd", not a 9. The m and d calls rest on letter form plus word sense ("Maud"; "n..." or "...9" give no word).
8. Line 11 final sign: a heavy blotted mark read as "?"; it could be a blotted 3-shape (i). It changes nothing in the reading.
6. Line 4 "1nsw2r2d": the r between w2 and 2d is small but present.
7. Under-stamp area not inspectable; no hidden writing seen on the picture side or edges.

## Why I believe it is correct

Every sign in the 11 message lines and the signature decodes with one five-entry key; the result is coherent rural Nebraska English of 1909 (corn husking season fits a 1 November postmark), the addressee Ben Russell is in Somerford, and the only deviations are three single vowel signs that are explained above. The key is the most common amateur postcard trick of the period (vowels replaced by 1–5).

## Response to review 1

Review 1 (REVISE) had four findings; all are accepted. The 11 message lines are unchanged.

1. major, foot note = signature "Maud": fixed. I enlarged the foot note (review/work/z_foot.png) and compared it with z_am.png and z_answered.png: the first sign is the same looped-humped m as in "1m", the last a d with a slanting ascender as in "1nsw2r2d". Transcription changed to "#SIG (m15d)" in work/transcription.txt; work/decode.py now decodes it and prints "(m15d) -> (maud) (signature)". Re-ran `python3 -I ciphers/hcp-1097/work/decode.py`: source hashes OK, all 11 lines unchanged, literal plaintext now ends "(MAUD)". The collector-number claim is dropped; "Sender unsigned" is corrected; the m/d calls are marked as resting on letter form plus word sense (uncertainty 5).
2. minor, Slovak gender: fixed, "dostala", "odpovedala".
3. minor, Wolsleben: kept disclosed (uncertainty 4) and in the report.
4. minor, line 11 final sign: added as uncertainty 8.

On the human note about steganographic messages under the stamp (Jolánka series): this card is a US card outside that series; neither side shows hidden or reversed writing in the picture, stamp box or edges, and the stamp itself cannot be lifted from scans. The type stays MASC, with the under-stamp area listed as not inspectable.
