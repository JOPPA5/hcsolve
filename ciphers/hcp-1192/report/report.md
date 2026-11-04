# HCP 1192 (cpc_1906-11-06_USA_Cobleskill. NY_USA__): an Election Day note to "Master Warren", Cobleskill N.Y., 1906

Human solver: Tomáš Pavuk

**Status: deciphered in full (86 of 86 cipher signs); independent review 1 verdict ACCEPT, no change to the reading.** Report dated 2026-11-03.

## Origin and context

The cryptogram is record 1192 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1192), portal name cpc_1906-11-06_USA_Cobleskill. NY_USA__, part of Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-11-03 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, with language, sender and recipient Unknown and no transcription or solution attached. The portal links the HistoCrypt article on the collection (https://ecp.ep.liu.se/index.php/histocrypt/article/view/166).

The picture side is a colour print titled **"After the Chase"** (Copyright 1906, American-Journal-Examiner): three huntsmen in red coats resting by a fireplace. The address side carries the line "Compliments of the New York Sunday American and Journal", so this was a give-away card of William Randolph Hearst's newspapers. The address is written in plain: **"Master Warren Becker, City."** The surname is cursive and partly under the portal watermark, so "Becker" is a reading, not a certainty. The postmark reads **COBLESKILL N.Y. NOV 6 5 PM 1906**. The printed stamp box at the top right is empty: no stamp was ever affixed.

6 November 1906 was Election Day in New York. That year Charles Evans Hughes ran for governor against Hearst himself. The message asks the boy, half in jest, whether he is "going to vote today", on a card handed out by Hearst's papers during the campaign.

The whole message is enciphered. It runs in the white margin all round the picture.

![Picture side as scanned: the cipher runs round the picture in the white margin (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side: Master Warren Becker, City; COBLESKILL N.Y. NOV 6 1906 postmark; empty stamp box at the right edge (source/address-large.jpg)](../source/address-large.jpg)

## Method

The transcription is **manual** and was made from the un-converted high-resolution scan the portal also serves (3468 × 2298 pixels). Each margin was cropped and enlarged, and every sign was given a shape name (work/transcription.txt). No OCR was used and the portal supplied no transcription.

The sign classes were then fed to a word-pattern annealer with an English word list. With the line order reversed it produced "hello", "warren" (the addressee) and "how" in the innermost right-hand line. That fixed eight letters. The phrases "are you? going to vote today?" and "give my love to mamma" then fixed the rest. Only after this did it become clear that the reversal comes from how the card is written:

- Every line is written with the **tops of the signs toward the picture**. The top strip is therefore upside-down relative to the card, the side strips are sideways, and only the bottom strip is upright.
- Read that way, every line runs normally left to right. The message spirals counter-clockwise round the picture: three lines in the right margin (innermost first), then the top strip, the left strip and the bottom strip, and finally the outermost right-hand line with the date and signature.

The orientation is confirmed by characters that are not part of the key. The question marks and the date digits are written in clear, and they read as "?" and "6, '06" only in the writer's orientation. Held the other way they look like "¿" and "9 … 9".

![Upper part of the right margin, enlarged (rotated so that the writer's orientation is upside down): "sis." at the top, then the ends of lines 3 and 1 (work/crops/rpanel_a.png)](../work/crops/rpanel_a.png)

The decoding script checks the hi-res originals and the source scans by SHA-256. A web search for a published solution of this card found none.

## Key

Simple monoalphabetic substitution with **18 invented signs**: one sign per letter, no homophones, no nulls. Punctuation (? . , ') and the date digits are written in clear. The signs are described as they look in the writer's orientation.

| Letter | Sign | Letter | Sign |
|---|---|---|---|
| a | single stroke, near vertical | n | I with serifs (I-beam) |
| b | single horizontal dash | o | circle with a horizontal bar through it |
| d | single stroke at about 45° ( / ) | r | two parallel strokes closed by end bars running / |
| e | two near-vertical strokes ( ‖ ) | s | the same sign mirrored, end bars running \ |
| g | two strokes leaning the other way ( \\ ) | t | circle with a single stem |
| h | two strokes at about 45° ( // ) | u | circle with an upright cross through it |
| i | plus sign + | v | circle with a diagonal cross through it |
| l | asterisk | w | circle with 6–8 spokes (wheel) |
| m | T-shape | y | hooked stroke |

The letters c, f, j, k, p, q, x and z do not occur. No other card in this repository uses this alphabet; the key was reconstructed from this card alone.

The most important distinctions were checked on enlargements. r and s are mirror images of each other; the difference is visible and consistent on all 8 occurrences. w (wheel) and u (circle with a 4-arm cross) are clearly different. The stroke signs a, d, e, h and g are separated by slant and by the number of strokes.

## Plaintext and translation

The text is in English. As read, line by line in reading order:

```text
hello warren, how
are you? going to
vote today?
how is anna gertrude?
give my love to mamma.
be a good boy.
nov 6,'06.
sis.
```

Normalised: **"Hello Warren, how are you? Going to vote today? How is Anna Gertrude? Give my love to Mamma. Be a good boy. Nov. 6, '06. Sis."**

English: the text is already English (see above). "Sis" is the writer's signature: an older sister writing to her younger brother.

Slovak: „Ahoj, Warren, ako sa máš? Ideš dnes voliť? Ako sa má Anna Gertrúda? Pozdravuj odo mňa mamičku. Buď dobrý chlapec. 6. nov. 1906. Sestra (Sis)."

The full plaintext is reproduced from the repository root with

```text
python3 -I ciphers/hcp-1192/work/decode.py
```

which checks the hashes of the scans, decodes the manual transcription with the key, and reports that every key entry is used.

## What remains uncertain

1. **Final "a" of "mamma".** The last stroke is faint and leans more (about 25–30°) than the other a-strokes, though clearly less than a d-stroke. It is read as "a" partly by word sense; "mammd" is not a word.
2. **"e" of "give".** The double stroke leans about 15–20°, like the e of "love" next to it, and much less than the h-sign (about 45°). This is a slant judgement supported by word sense.
3. **Middle date digit.** It is an open loop partly under the portal watermark. "0" is the natural reading and agrees with the postmark year 1906.
4. **"Anna Gertrude".** This is read letter by letter. It may be one person with two names, or two people with "and" omitted; the card does not say.
5. **"Becker".** The surname in the address is a reading of cursive under the watermark. It plays no part in the decipherment.

No sign is restored and no sign is left unread.

**Steganography.** On some other postcard series hidden text was found under the stamp. This card has no stamp: the printed stamp box is visible and empty. Nothing else is written in the picture or along the edges apart from the cipher border. The cipher type is therefore plain MASC, without steganography.

## Review and what changed

An independent reviewer (a separate Claude Opus 5.5 agent) cut its own rotated crops from the hi-res scan, read every line sign by sign, and wrote its own key and decoder. Its reading agrees with the solver's in all 86 cipher signs, and all 18 key entries are used. It confirmed the writer's orientation from the question marks and the date, checked the r/s, w/u and stroke-slant distinctions on zooms, and confirmed that the empty stamp box rules out a hidden message under a stamp.

The verdict was **ACCEPT** with four minor findings: the last "a" of "mamma", the slant of the e-strokes, the middle date digit and the surname "Becker". Each repeated an uncertainty the solver had already disclosed, and none changed the reading. Nothing in the key or the plaintext was changed after review.

## Credit

Transcription, key reconstruction and decipherment by Claude Opus 5.5 (2026-11-03); independent review by a separate Claude Opus 5.5 agent. There was no earlier work on this number, and no published solution was used.
