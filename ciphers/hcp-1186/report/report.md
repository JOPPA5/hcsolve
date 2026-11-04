# HCP 1186: an enciphered note from "Nan", Dorchester 1904

Human solver: Tomáš Pavuk

**Status: deciphered in full (all 37 cipher groups, every sign read); independent review 1 verdict ACCEPT, no change to the decoded text.** Report dated 2026-11-03.

## Origin and context

The cryptogram is record 1186 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1186), portal name cpc_1904-10-12_UK_Dorchester_UK_Dorchester_, part of Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-11-03 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, language Unknown, sender Unknown, recipient "AE Haware", with no transcription or solution attached.

It is a British picture postcard: the picture side shows sailing ships at a wooden jetty at sunset; the address side carries a green Edward VII halfpenny stamp cancelled **DORCHESTER / DORSET, 12 OC 04**, at about **3.30 PM** (the middle digits of the time are blurred; 3.25 is not excluded). The card is therefore dated Wednesday, 12 October 1904. It is addressed in plain writing to **Mr. A. E. Hayward, ... H. E. St, Dorchester**; "H. E. St" is very likely High East Street, a main street of Dorchester. Sender and addressee lived in the same town, and the message asks to meet at Weymouth, the seaside town about 8 miles south.

The message stands on the left half of the address side, under the printed note that this space may be used for communication. Six lines are in cipher; the seventh line begins in cipher and then changes to plain English handwriting; a cipher signature closes the card.

![Address side: message on the left, address and stamp on the right (source/address-large.jpg)](../source/address-large.jpg)

![The message panel enlarged from the un-converted scan (work/message-panel.png)](../work/message-panel.png)

![Picture side: sailing ships at a jetty, sunset (work/picture-overview.png)](../work/picture-overview.png)

## Method

The transcription is manual. The solver read every sign from enlarged crops of the un-converted 3468 x 2298 address scan (work/hires/), recorded it in work/transcription.txt with one code per sign, and decoded it with work/decode.py. No OCR was used and the portal supplied no transcription.

The cipher is word-divided (groups separated by dots and commas), which made it easy to attack with cribs:

- the one-sign words 6 and 4 must be A and I;
- 4Y, 4a and Y3 then give IT, IS and TO;
- the group 2385 occurs twice ("such a long time", "as long as") and is LONG;
- a48w9 (SINCE), 896R2i (NEARLY) and the signature 868 (pattern A-B-A, NAN) followed;
- the rest of the key filled in word by word (HOW TO twice, FORGOT and FORGOTEN sharing a stem).

The result is one consistent, one-to-one key of 19 letters plus the ampersand, which decodes every cipher group. The decoded text runs straight into the plain-English closing clause, which confirms the reading independently of the key.

## Key

Simple monoalphabetic substitution (MASC). The signs are a mixture of digits and invented letter-like shapes. The names below describe the handwritten shapes; they are not exact reproductions.

| Plain | Sign | Plain | Sign | Plain | Sign |
|---|---|---|---|---|---|
| A | 6 | H | u-shape | R | stroke with an overbar (base like 5, 6 or 1) |
| B | l/k-shape | I | 4 | S | round a |
| C | w-shape | K | hooked E-like sign | T | Y-shape |
| D | n-shape | L | 2 | U | 1 (plain stroke) |
| E | 9 | M | 1-like stroke, top hook, curled foot | V | cursive d-shape (a-bowl, tall right stem) |
| F | filled oval | N | 8 | W | e-shape |
| G | 5 | O | 3 (often g-like) | Y | iota-like stroke, detached dot above |

The overbar is what marks R: its base varies (5-like in CARD, 6-like in NEARLY, 1-like in FORGOTEN), but the bar plus base is always one sign, distinct from G = 5, A = 6 and U = 1. The V (cursive d) must not be confused with D, which is the n-shape. Letters J, P, Q, X and Z do not occur in the cipher part.

## Plaintext

Ciphertext as transcribed (sign codes of work/transcription.txt) and decoded, line by line:

```text
4y 4a a1wu 6 2385          IT IS SUCH A LONG
y4M9 a48w9 4 a98y i31      TIME SINCE I SENT YOU
6 w6Rn yu6y 4 896R2i       A CARD THAT I NEARLY
o3R53y u3e y3 eR4y9 k1y    FORGOT HOW TO WRITE BUT
6a 2385 6a 4 u6v9 83y      AS LONG AS I HAVE NOT
o3R53y98 u3e y3 t4aa &     FORGOTEN HOW TO KISS &
u15 [plain:] hope to see you, at Weymouth this afternoon
868                        NAN
```

English, as written: **It is such a long time since I sent you a card that I nearly forgot how to write, but as long as I have not forgoten how to kiss & hug - hope to see you at Weymouth this afternoon. Nan**

FORGOTEN is spelled with one T on the card (eight signs, one T-sign); it is kept as written.

Slovak translation: **Je to už tak dávno, čo som ti poslala pohľadnicu, že som takmer zabudla písať, ale kým som nezabudla bozkávať a objímať... Dúfam, že sa dnes popoludní uvidíme vo Weymouthe. Nan**

The feminine verb forms (poslala, zabudla) assume that the writer is a woman: Nan is a usual pet form of Ann, Agnes or Hannah. This is an assumption from the signature, not a fact stated on the card.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1186/work/decode.py
```

The script uses only the Python standard library. It checks the SHA-256 hashes of the four scans (the two portal conversions in source/ and the two un-converted originals in work/hires/), checks that the key is one-to-one, decodes work/transcription.txt and prints the eight lines above. It does not read the images; the transcription step is manual and was confirmed independently in review.

## Uncertainties

- **Single-occurrence signs.** M (TIME) and V (HAVE) occur once each; their values rest on word sense. B (BUT), K (KISS), W (HOW, WRITE), D (CARD) and F (FORGOT, FORGOTEN) are fixed by one or two words each. All fit the sentence.
- **FORGOT, line 4.** The second sign is a rounded, blotted form rather than a clear 3; it is read as O because the same word is written with a clear 3 on line 6.
- **Signature.** 868 = NAN follows from the known N and A; the person behind it is not identified.
- **Address.** "Mr." is most likely (M with a raised r and a dot), but "Mrs" cannot be fully excluded; "Hay" in Hayward is faint (the portal has "Haware"). The second address line, squeezed in above "H. E. St" (something like "Company?? 7 Col. Sgt?"), is not read. It belongs to the address, not to the message.
- **Postmark time.** Read as 3.30 PM; blurred, 3.25 PM possible. If the card was posted at that time, it can hardly have reached the addressee before an afternoon meeting in Weymouth; the writer may have meant a late-afternoon meeting, or written the card earlier in the day. The reading does not depend on this.
- **Hidden writing.** The stamp is still attached, so nothing under it could be inspected from the scan. No hidden, upside-down or mirrored writing was found around the stamp, along the edges of either side, or inside the picture. The card is therefore classed as a plain MASC, not MASC + Steganography.
- No published solution of this card was found (portal status Not solved, no attachment).

## Review summary

Reviewer: a separate Claude Opus 5.5 agent, round 1, verdict **ACCEPT**. The reviewer ran the reproduction command (output identical to the claimed plaintext), read every sign itself from its own enlarged crops of the un-converted scan, used its own sign codes and its own key, and decoded with its own script: all 37 cipher groups gave the same eight lines, with no sign left over. It checked the left margin of line 6 (nothing precedes FORGOTEN), the overbarred R signs, the M of TIME and the dotted Y of YOU, the stamp area and the picture side. Its four findings were minor and were all accepted:

- **Address.** "Mr." versus "Mrs" is now stated as uncertain, "H. E. St" is identified as very likely High East Street, and the unread second line is named as part of the address.
- **Postmark time.** The time is now given (about 3.30 PM, 3.25 not excluded).
- **V sign.** It is now described as a cursive d-shape, with a warning not to confuse it with D (the n-shape).
- **Slovak translation.** The feminine forms are now marked as an assumption from the signature Nan.

No decoded letter changed as a result of the review.

## Credits

Capture of the portal record, transcription, key reconstruction and decipherment: Claude Opus 5.5 (Anthropic), 2026-11-03. Independent review: a separate Claude Opus 5.5 agent. No earlier AI work exists for this number. Human solver of record: Tomáš Pavuk.

## Sources

- HC Portal record 1186, General, Description and Attachments tabs, captured 2026-11-03: https://crypto.hcportal.eu/dashboard/cryptograms/1186 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/3618/cpc_1904-10-12_UK_Dorchester_UK_Dorchester__pic.jpg (and its -large conversion in source/).
- Address side: https://api.hcportal.eu/media/3619/cpc_1904-10-12_UK_Dorchester_UK_Dorchester__adr.jpg (and its -large conversion in source/).
- Collection reference given on the portal: https://ecp.ep.liu.se/index.php/histocrypt/article/view/166
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-11-03: no entry for this card.
