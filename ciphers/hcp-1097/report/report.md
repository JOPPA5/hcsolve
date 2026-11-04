# HCP 1097: a vowel-cipher postcard from Maud to Ben Russell, Somerford, Nebraska (1909)

Human solver: Tomáš Pavuk

**Status: deciphered in full (11 message lines and the signature); independent review 1 verdict REVISE, all findings addressed; the message reading did not change, the foot note was reread as the signature "Maud".** Report dated 2026-11-03.

## Origin and context

The cryptogram is record 1097 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1097), portal name "cpc_1909-11-01_USA_Somersford, Nebraska_USA_Somerford, Nebraska_", part of Tobias Schrödel's collection of cryptographic postcards (private collection). When captured on 2026-11-03 the portal listed it as **Not solved**, language Unknown, sender Unknown, recipient Ben Russel, with no transcription or solution attached. No published solution of this card was found or used.

The picture side is a printed view titled "A Quiet Spot" (a bridge in a park); it carries no handwriting. The address side is addressed in plain pencil to **Mr. Ben Russell, Somerford, Nebr.** and bears a green 1-cent Franklin stamp and the postmark SOMERFORD NOV 1 190(9) NEBR (the last year digit is blurred; the portal file name gives 1909-11-01). The message space at the left holds eleven pencil lines and a bracketed signature, all in cipher.

![Address side with the eleven cipher lines and the signature (source/address-large.jpg)](../source/address-large.jpg)

![Picture side, "A Quiet Spot" (source/picture-large.jpg)](../source/picture-large.jpg)

## Method

The solver read every line sign by sign from the un-converted high-resolution scan (work/hires/) and recorded the reading in work/transcription.txt. The text is ordinary cursive English in which only the digits 1 to 5 are foreign: they stand where vowels belong (y45 = you, g4t = got, h2r2 = here). Mapping 1 to 5 onto a, e, i, o, u in order decodes every line into connected English. This is the commonest amateur postcard trick of the period. The script work/decode.py checks the SHA-256 of both source scans and prints each line with its decoding.

Reproduction, from the repository root:

```sh
python3 -I ciphers/hcp-1097/work/decode.py
```

## Key

Monoalphabetic substitution of the vowels only; consonants are written in clear (register type MASC).

| a | e | i | o | u |
|---|---|---|---|---|
| 1 | 2 | 3 | 4 | 5 |

In this hand the i-sign "3" sometimes looks like a 9 or a small g; context separates it from the cursive g.

## Transcription and decoding

```text
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

## Plaintext

You got back here in this country again. I got your post card to[o] late to answered it, so I will send you this one. I spose you're very busy husking corn now. I am at Wolsleben now. How long are you a-going to stay? (Maud)

The spellings "to late", "to answered", "spose" and "your" for "you're" are the writer's own.

## Translations

**English (normalised):** You are back here in this part of the country again. I got your postcard too late to answer it, so I am sending you this one. I suppose you are very busy husking corn now. I am at Wolsleben's now. How long are you going to stay? Maud

**Slovak:** Si zase späť tu v tomto kraji. Tvoju pohľadnicu som dostala príliš neskoro, aby som na ňu odpovedala, tak ti posielam túto. Asi máš veľa práce s lúpaním kukurice. Teraz som u Wolslebenovcov (vo Wolslebene). Ako dlho tam zostaneš? Maud

Corn husking fits the date of the postmark, 1 November.

## Uncertainties

1. Line 6 "th1s": the third sign is a plain vertical stroke, graphically the a-sign, so the literal decoding is "thas"; read "this" on word sense (line 2 writes th3s correctly).
2. Line 11 "1g41ng": the fourth sign is again a stroke; literal "agoang", read "a-going" on word sense.
3. Line 7 "b3sy": the sign after b is a heavy, overwritten 3, possibly over another figure; literal "bisy", read "busy" on word sense.
4. "w4lsl2b2n" = Wolsleben is read clearly letter by letter, but whether it is a family ("at the Wolslebens'") or a place is not established; no Nebraska records were checked.
5. Signature "(m15d)" = Maud: the m and the d are read from letter form (the same m as in "1m", the same d as in "1nsw2r2d") together with word sense. Before review it was wrongly taken as a collector number "(n159)".
6. The heavy final mark of line 11 is read as "?"; it might be a blotted i-sign. It does not affect the reading.
7. The area under the stamp cannot be inspected from scans. No hidden, reversed or upside-down writing was seen in the picture, the stamp box or along the edges, so the card is classed as plain MASC, not MASC + Steganography.

## Review summary

An independent reviewer (a separate Claude Opus 5.5 agent) ran the reproduction command, decoded the card with its own script and its own reading of all lines, and checked every doubtful sign on enlarged crops. It agreed with all eleven message lines and gave verdict REVISE with four findings:

1. (major) The bracketed foot note is the enciphered signature "Maud", not a collector number. Accepted: transcription and decoder changed, "sender unsigned" corrected.
2. (minor) With a female signature, the Slovak translation should use feminine verb forms. Accepted.
3. (minor) Keep the Wolsleben question disclosed. Done (uncertainty 4).
4. (minor) Mention the possible reading of the last mark of line 11. Done (uncertainty 6).

The decoding of the message itself did not change.

## Sources

- HC Portal record 1097: https://crypto.hcportal.eu/dashboard/cryptograms/1097 (metadata, scans).
- Scans: source/address-large.jpg, source/picture-large.jpg; high-resolution originals in work/hires/ (see SOURCES.md).
