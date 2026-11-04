# HCP 1082: a French number-cipher postcard from Gare des Aubrais to Nantes, 1942

Human solver: Tomáš Pavuk

**Status: deciphered in full (105 of 105 cipher signs, 26 words); independent review 1 verdict ACCEPT, no change to the decoded text.** Report dated 2026-11-03.

## Origin and context

The cryptogram is record 1082 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1082), portal name "cpc_1942-08-27_FR_Loiret, Gare des Aubres_FR_Nantes_", part of Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-11-03 the portal listed it as **Not solved**, tagged Postcard, T. Schrödel Collection, language Unknown, sender Unknown, recipient Lucien Rabaud, with no transcription or solution attached. The only linked reference is the general HistoCrypt article on the Schrödel collection; no reading of this card was found or used.

The picture side is a printed photo card "258. TOURS — La Poste" (Réal-Photo, C.A.P., Paris), showing the post and telephone office in Tours. It carries no handwriting.

The address side is postmarked **GARE DES AUBRAIS / LOIRET, 27-8-42** (27 August 1942; Les Aubrais is the railway junction of Orléans) on a 1F50 Pétain definitive stamp. The address is in plain writing: **Mr Lucien Rabaud, 6 rue Fellonneau, Nantes, L. Inf.** (Loire-Inférieure). The whole message, ten lines on the left half, is written in pencil as groups of digits with small tick marks, separated by dashes.

![Address side: ten lines of digit cipher on the left, plain address to Lucien Rabaud in Nantes on the right (source/address-large.jpg)](../source/address-large.jpg)

![Picture side: Tours, La Poste; no writing (source/picture-large.jpg)](../source/picture-large.jpg)

Other marks on the card, none of them cipher: the address, the printed caption and publisher line, the stamp and two postmarks, a short black stroke above line 5 in a different medium, and the HCPortal watermark on both sides. The stamp box was inspected on the full-resolution scan: the stamp is intact and there is no writing around it or along the edges. Whatever might lie under the stamp cannot be checked from scans.

![Stamp box on the original scan: intact 1F50 Pétain stamp, no hidden writing visible (work/zoom/stamp.png)](../work/zoom/stamp.png)

## Method

All work on this card was done by Claude Opus 5.5; there was no earlier solver. The transcription is manual: the ten lines were read sign by sign from the un-converted original scan (work/hires/), enlarged 2–4 times (work/lines/, work/zoom/). Each sign is one digit, optionally followed by one tick (') or two ticks ("). The result, 27 written groups and 105 signs, is in work/transcription.txt.

The key followed from two short groups. Line 3 opens with an isolated "1", which in a French text is most naturally the word À; line 6 then reads "1 - 2 5' 4' - 6' 5' 8' 0'", which fits "À BON PORT". That gives A = 1, B = 2, O = 5', N = 4', P = 6', R = 8', T = 0', which is exactly the alphabet written in rows of ten under the digits 1 2 3 4 5 6 7 8 9 0, the first row unmarked, the second with one tick and the third with two. With that table every other group reads as French.

The reviewer, working separately, wrote its own decoder (key built independently as three rows of ten), checked every sign of the transcription against its own crops of the original scan, and obtained an identical plaintext with no undefined sign.

The reproduction command, run from the repository root, checks the SHA-256 of the scans and prints both the literal decryption and the corrected one:

```text
python3 -I ciphers/hcp-1082/work/decode.py
```

## Key

Monoalphabetic number substitution (MASC). Digit order 1 to 9, then 0.

| digit | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 |
|---|---|---|---|---|---|---|---|---|---|---|
| no mark | A | B | C | D | E | F | G | H | I | J |
| ' | K | L | M | N | O | P | Q | R | S | T |
| " | U | V | W | X | Y | Z | | | | |

The places 7", 8", 9" and 0" are empty, and none of them occurs on the card. French accents and apostrophes are not written.

## Ciphertext and plaintext

Ciphertext as transcribed, line by line (" | " marks the writer's dashes), with the literal decryption (marks exactly as written) and the decryption after the seven writer's slips listed below are corrected:

```text
   ciphertext                              literal              corrected
1  3' 5' 4' | 3 8 5 8' | 2' 1" 3 9 6 4'    MON CHER LUCIFN      MON CHER LUCIEN
2  0 5 | 6' 5 4' 9' 5 | 2 9 5 4'           JE PENSE BIEN        JE PENSE BIEN
3  1 | 0' 5' 9 | 0 1 9 | 6 1 9 0'          A TOI JAI FAIT       A TOI JAI FAIT
4  2 5' 4' | 2" 5' 5" 1 7 5 | 5 0'         BON VOYAGE ET        BON VOYAGE ET
5  9' 1" 9 9' | 1 8' 8' 9 2" 5 5           SUIS ARRIVEE         SUIS ARRIVEE
6  1 | 2 5' 4' | 6' 5' 8' 0'               A BON PORT           A BON PORT
7  0 5 | 0' 5 4 2 5 9 5                   JE TEDBEIE           JE TENVOIE
8  2 9 5 4 | 4 5 9 | 3 8 5' 9' 5 9'       BIED DEI CHOSES      BIEN DES CHOSES
9  2 5' 4' 9' | 9' 5' 1" 2" 5              BONS SOUVE           BONS SOUVE-
10 4 9 8' 9' | 1 4' 4 8' 5                 DIRS ANDRE           NIRS ANDRE
```

French text, with accents and apostrophes restored:

> Mon cher Lucien, je pense bien à toi. J'ai fait bon voyage et suis arrivée à bon port. Je t'envoie bien des choses. Bons souvenirs. André

English: My dear Lucien, I am thinking of you a lot. I had a good journey and arrived safely. I send you all the best. Fond regards. André

Slovak: Môj drahý Lucien, veľmi na teba myslím. Mala som dobrú cestu a šťastne som docestovala. Posielam ti veľa pozdravov. Pekné spomienky. André

Note on the translations: the feminine forms in the Slovak (mala som, docestovala) follow the feminine "arrivée" written on the card. The signature reads ANDRE, so whether the writer was André or Andrée is not resolved (see below).

## Uncertainties and writer's slips

Seven signs depart from the key; in each case the intended letter is fixed by an unambiguous French word, and the same words are written correctly elsewhere on the card. These are corrections of the writer's enciphering, not of the reading:

1. LUCIEN (line 1): the fifth sign is clearly a closed-loop 6 (= F) instead of 5 (= E). The name is confirmed by the plain address.
2. T'ENVOIE (line 7): written 0' 5 4 2 5 9 5; the 4, 2 and 5 lack their marks (4' = N, 2" = V, 5' = O). The digit sequence equals T-E-N-V-O-I-E exactly.
3. BIEN (line 8): the final 4 lacks its tick (D instead of N); BIEN in line 2 has it.
4. DES (line 8): the final 9 lacks its tick (I instead of S).
5. NIRS (line 10, the end of SOUVENIRS): the first 4 lacks its tick.

Readings that rest partly on the key and on word sense:

- Line 5, fourth sign (S of SUIS): the 9 is followed by a curved pencil tick and a faint second stroke, partly covered by the black stroke, so a double mark cannot be excluded from the scan. 9" has no value in the key, and 9' (S) is the only reading that gives a letter and the word SUIS.
- Line 5, second 8 of ARRIVEE: its tick is written low, comma-like, next to a small blot; read 8' (R).
- Line 1, the 4 of MON: retraced in darker pencil with a small round tick; read 4' (N).

Other open points:

- Signature 1 4' 4 8' 5 = ANDRE. The feminine "arrivée" does not agree with André; either the writer is Andrée with one E left out, or the agreement is a slip. The text is given literally as ANDRE.
- Street name in the plain address: read "Fellonneau" (looped cursive F); it is not ciphertext.
- Nothing can be said about anything hidden under the stamp.

## Why the solution is correct

All 105 signs decode with one fixed, systematic key (the alphabet in three rows of ten), and the text is grammatical, idiomatic French of a travel card: "j'ai fait bon voyage et suis arrivée à bon port", "je t'envoie bien des choses", "bons souvenirs". The decrypted salutation names the addressee of the plain address, and a journey reported from the Orléans rail junction to someone in Nantes fits the postmark. The key is too regular to be overfitted, and the only departures are one wrong digit and six missing marks, each on a sign whose digit is right.

## Review and what changed

An independent reviewer (a separate Claude Opus 5.5 agent) re-ran the command, decoded the transcription with its own script, checked every sign against its own crops of the original scan, inspected the stamp box and the picture side, and judged the French. Verdict: **ACCEPT**, with four minor findings and no blockers:

1. The street name had been given as "Cellanneau (?)"; the reviewer read a looped F and "Fellonneau". Checked on a new enlargement and corrected.
2. The S of SUIS may carry a double mark; the report now says that this call rests partly on the key and word sense.
3. The gender of the Slovak translation follows "arrivée"; a note on this has been added.
4. The report shows the literal and corrected decryptions side by side and lists every emendation.

The reviewer also confirmed the cipher type as MASC (number substitution) with no steganographic part. The decoded text was not changed by the review.
