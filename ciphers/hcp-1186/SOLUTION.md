# hcp-1186 — Solution (round 1)

Card: HC Portal cryptogram 1186, `cpc_1904-10-12_UK_Dorchester_UK_Dorchester_`, T. Schrödel collection.
Picture postcard (sailing ships at a jetty, sunset), British halfpenny stamp, postmark DORCHESTER 12 OC 04
(12 October 1904, afternoon). Addressed to Mr A. E. Hayward, Dorchester (portal: "AE Haware").
Portal status Not solved, no transcription or solution attached; no published solution of this card found.
Transcription, key reconstruction and decipherment: Claude Opus 5.5 (2026-11-03). No earlier work on this number.

## Cipher type and key

Simple monoalphabetic substitution (MASC) with digits and letter-like invented signs, word divisions kept
(groups separated by dots/commas), the final clause written in plain English, signature enciphered.

| plain | sign | plain | sign | plain | sign |
|---|---|---|---|---|---|
| A | 6 | H | u-shape | R | stroke with overbar (written like 5̄, 6̄ or 1̄) |
| B | l/k-shape | I | 4 | S | a |
| C | w-shape | K | hooked t/E-like sign | T | Y-shape |
| D | n-shape | L | 2 | U | 1 (plain stroke) |
| E | 9 | M | 2-like sign with long hook | V | cursive d-shape (a-bowl with tall right stem; not D, which is the n-shape) |
| F | filled oval o | N | 8 | W | e-shape |
| G | 5 | O | 3 (often g-like) | Y | dotted iota-like sign |

19 plaintext letters occur (J, P, Q, X, Z not used in the ciphertext; P only in the plain clause).
Sign codes used in `work/transcription.txt` are listed in its header.

## Command (from repo root)

    python3 -I ciphers/hcp-1186/work/decode.py

It verifies the SHA-256 of the four image files, then decodes `work/transcription.txt` with the key.

## Plaintext (English, as written)

It is such a long time since I sent you a card that I nearly forgot how to write, but as long as I have not
forgoten [sic, one T] how to kiss & hug, [plain:] hope to see you at Weymouth this afternoon. Nan

Line by line (ciphertext → plaintext):

    4y 4a a1wu 6 2385          IT IS SUCH A LONG
    y4M9 a48w9 4 a98y i31      TIME SINCE I SENT YOU
    6 w6Rn yu6y 4 896R2i       A CARD THAT I NEARLY
    o3R53y u3e y3 eR4y9 k1y    FORGOT HOW TO WRITE BUT
    6a 2385 6a 4 u6v9 83y      AS LONG AS I HAVE NOT
    o3R53y98 u3e y3 t4aa &     FORGOTEN HOW TO KISS &
    u15 (plain) ...            HUG hope to see you at Weymouth this afternoon
    868                        NAN

English (normalised): It is such a long time since I sent you a card that I nearly forgot how to write, but as
long as I have not forgotten how to kiss and hug. Hope to see you at Weymouth this afternoon. Nan

Slovak: Je to tak dávno, čo som ti poslala pohľadnicu, že som takmer zabudla písať, ale kým som nezabudla bozkávať
a objímať... Dúfam, že sa dnes popoludní uvidíme vo Weymouthe. Nan

## Uncertainties

1. M (sign in y4M9 = TIME) occurs once; its value rests on word sense ("such a long time since"). The sign is
   visibly different from 1 (U) and 2 (L).
2. V (u6v9 = HAVE) occurs once; the sign is an a with a raised right stem, distinct from S = round a, but its value
   rests on word sense.
3. B (k1y = BUT), K (t4aa = KISS), W (e: HOW, WRITE), D (w6Rn = CARD) and F (FORGOT/FORGOTEN) are each fixed by one
   or two words; all fit the context.
4. Line 4, FORGOT: the second sign is a rounded, blotted form, not a clear 3; it is read as O because the same
   word is spelled with a clear 3 on line 6. The R sign varies in base shape (5-, 6- or 1-like) but always has an
   overbar.
5. FORGOTEN has only one T-sign (counted 8 signs on the enlarged crop); reported as written.
6. Signature 868 = NAN (pattern ABA with known N and A); a name or nickname, not otherwise verifiable.
7. Address: "Mr A. E. Hayward, ... H. E. St, Dorchester" (the "Hay" is faint); the second address line (something
   like "Connaught?? 7 Col.. Sup..") is cramped and not read. It is the address, not part of the message.
8. Steganography: the stamp is still on the card, so nothing underneath could be inspected. No hidden writing seen
   along the edges or in the picture side.

## Why I believe it is correct

- Every cipher group on the card (37 groups, including the signature) decodes under one consistent, one-to-one key
  to grammatical English that flows straight into the plain-English closing clause.
- Repeats check out: 2385 = LONG twice, u3e y3 = HOW TO twice, 6a = AS twice, FORGOT/FORGOTEN share their stem.
- Content fits the card: an English halfpenny card posted at Dorchester asking to meet at Weymouth (8 miles away)
  the same afternoon.

## Response to review 1

Review 1 (separate Claude Opus 5.5 agent) gave verdict ACCEPT with four minor findings and no blocker or major
finding. Re-checked on the un-converted address scan (work/hires/..._adr.jpg); new images work/message-panel.png,
work/postmark-rotated.png and work/picture-overview.png. No decoded letter changes. The reproduction command
`python3 -I ciphers/hcp-1186/work/decode.py` was re-run after these edits: "source hashes OK (4 files)" and the
same eight lines as above.

1. Address (minor) - accepted. Re-read at 3x: first line "Mr. A. E. Hayward": the title is an M with one raised
   letter (r) and a dot under it, so "Mr." is the most likely reading; "Mrs" cannot be fully excluded because the
   raised part is small, and it is stated as uncertain. "Hay" in Hayward is faint (portal: "AE Haware"). Third line
   "H. E. St", very likely High East Street, Dorchester (a real central street), which fits the Dorchester postmark.
   The second line, squeezed in above the third (something like "Company?? 7 Col. Sgt?/Sup."), stays unread; it is
   part of the address, not of the message, and is not counted as part of the text.
2. Postmark time (minor) - accepted. Rotated crop work/postmark-rotated.png: DORCHESTER / DORSET, 12 OC 04, time
   read as 3.30 PM; the middle digits are blurred and 3.25 PM is not excluded. A same-day local delivery in
   Dorchester in 1904 would still allow a meeting in Weymouth (about 8 miles, by train) "this afternoon" only if the
   card was posted well before; the writer may also have meant a later train. The content does not depend on it.
3. V sign (minor) - accepted. The V of HAVE (u6v9) looks like a cursive d: a round a-bowl with a tall right stem.
   It must not be confused with D, which in this key is the n-shaped sign (w6Rn = CARD). Key table entry V is
   therefore "cursive d-shape (a-bowl with tall right stem)".
4. Feminine Slovak forms (minor) - accepted. The writer signs NAN (a usual diminutive of Ann/Agnes/Hannah), so the
   Slovak translation uses feminine verb forms (poslala, zabudla); this is an assumption from the signature, not a
   fact on the card.

Steganography (also asked by the human for other card families): the halfpenny stamp is still attached, so
nothing underneath it can be inspected from the scan; no hidden or upside-down writing is visible around the stamp,
along the edges of either side, or inside the picture (sailing ships at a jetty at sunset). Register type stays
MASC, not MASC + Steganography.
