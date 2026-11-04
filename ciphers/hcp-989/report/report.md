# HCP 989 (cpc_1901-10-19_AT_Wien_AT_Wien_): a rune-cipher rendezvous in a Vienna cider tavern

Human solver: Tomáš Pavuk

**Status: deciphered; the two enciphered words of the meeting place read APFELWEIN. STUBE. One enciphered word in parentheses (8 of the 22 cipher signs on the card) is not read. Independent review 1 verdict ACCEPT, no change to the reading.** Report dated 2026-11-03.

## Origin and context

The cryptogram is record 989 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/989), portal name cpc_1901-10-19_AT_Wien_AT_Wien_, part of Tobias Schrödel's collection of cryptographic postcards (private collection; see also https://ecp.ep.liu.se/index.php/histocrypt/article/view/166). When captured on 2026-11-03 the portal listed it as **Not solved**, language Unknown, sender Unknown, recipient Hugo P., with no transcription or solution attached. A short web search found no published reading of this card.

It is an embossed picture postcard (a sailing ship in a storm inside a wooden frame with flowers). The message is written in ink along the left margin of the picture side, so the card has to be turned 90° to read it. The address side reads, in plain Kurrent script, "Hochwohlgeboren Herrn Hugo P?ell, Beamten, Wien Hernals XVII, Weidmanngasse(?) 3", with a sender's note at the lower left "Absender J.(?) Kraus, Wien XVIII. Schulgasse(?) 9" (both names uncertain readings of handwriting). The Austrian 5-heller stamp is glued diagonally over the printed header, not in the stamp box; it is cancelled WIEN 19 10 01, and an arrival cancel of the same day sits to the right.

![Picture side as scanned; the message runs along the left margin (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side: Hugo P?ell, Wien XVII; stamp glued diagonally over the header (source/address-large.jpg)](../source/address-large.jpg)

![The message strip, turned upright (work/crops/strip.png)](../work/crops/strip.png)

Most of the message is plain German Kurrent. Only the place of the meeting (two words) and one word in parentheses are enciphered.

## Method

The solver (Claude Opus 5.5) worked from the un-converted high-resolution scan, cropped and rotated the message strip and enlarged each cipher word 3 to 5 times (work/crops/). Each sign was given a shape code and recorded in work/transcription.txt. The signs are rune-like (fehu, lambda, a lightning bolt, an up-arrow, a square u-rune) and belong to the same home-made alphabet as two other Vienna-area cards in this repository, HCP 1194 and 1195 (to Anton Schönfelder, 1900). That key was transferred unchanged: no sign value was invented for this card. The decoder work/decode.py checks the SHA-256 of the scans, applies the key and prints the message:

```text
python3 -I ciphers/hcp-989/work/decode.py
cipher signs -> AP/BF/WELF/WEIN. STUP/BE.
decoded      -> APFELWEIN. STUBE.
```

![The enciphered words on line 3 (work/crops/line3.png)](../work/crops/line3.png)

The reviewer cropped the strip independently, read every sign at 4 to 8 times enlargement and decoded with its own script (review/work/mydecode.py). Applied literally, the sister key gives ABFELFEIN. STUBE.; solver and reviewer agree on all 14 signs.

## Key

Monoalphabetic substitution with rune-like signs (values from HCP 1194/1195):

| Sign (code) | Letter |
|---|---|
| stem with short slant on the left, ᛅ-like (diag) | A |
| B-shape with long tail, ᛒ (b) | B, also P (no dot on this card) |
| fehu with two twigs, ᚠ (f2) | F, also W (no distinction on this card) |
| cross, slanted as X (x) | E |
| stem with hook at top, ᛚ (hook_l) | L |
| plain stem ᛁ (stem) | I |
| lambda Λ (lam) | N |
| lightning ϟ (bolt) | S |
| up-arrow ᛏ (arrow_up) | T |
| square u-rune Π (u_pi) | U |

On the sister cards P is a dotted B and W a marked fehu; this writer used the plain sign for both, so P and W are chosen by word sense.

## Plaintext

German (enciphered part in capitals; line breaks as on the card):

```text
Lieber Hugo                                    3/4 7 - 7 Uhr
Ich erwarte Dich zwischen [blacked out] Uhr
in der APFELWEIN. STUBE.
[struck-out word] ([one enciphered word, not read]) am Samstag 19/10      Toni
```

Normalised: "Lieber Hugo! Ich erwarte Dich zwischen ¾7 und 7 Uhr in der Apfelweinstube (...) am Samstag 19/10. Toni."

English: "Dear Hugo! I'll be waiting for you between a quarter to seven and seven o'clock in the cider tavern (Apfelweinstube) (...) on Saturday 19/10. Toni."

Slovak: "Milý Hugo! Budem ťa čakať medzi trištvrte na sedem a siedmou v jablčnej vinárni (Apfelweinstube) (...) v sobotu 19. 10. Toni."

19 October 1901 was a Saturday and the card was posted and delivered in Vienna that same day, so it arranges a meeting for the same evening (Vienna had several deliveries a day).

## Uncertainties

1. **The parenthetical word on line 4 is not read.** It has 8 cipher signs, about a third of the 22 cipher signs on the card. Signs 3 to 5 are heavily overwritten by the writer; sign 1 looks like ϟ (S) with a top bar, sign 2 like the Y-form of E, signs 6 and 7 like K and I, and sign 8 is a 大-like shape not in the sister keys. No defensible word fits, so none is offered. It is a single word (probably the name or place of the tavern) and the rest of the message reads without it.

![The unread parenthetical word (work/crops/p1.png)](../work/crops/p1.png)

2. Word-sense letters in APFELWEIN: P (same sign as B), W (same sign as F) and I (written mainly as a short dash with only a ghost of a stem, the pen running dry). The literal key output is ABFELFEIN; APFELWEIN STUBE is the only German reading the pattern allows and fits "in der ___". The L/N split rests on leg length (L short, N reaching the baseline).
3. The time after "zwischen" is blacked out by the writer, and the corrected time is written at the top right ("3/4 7 - 7 Uhr"). The word before the parenthesis is inked over by the writer. Both are deletions, not ciphertext.
4. Plain-script names: "Toni" (initial T or J), the surname P?ell/Pöll, Weidmanngasse/Weidmannsgasse, and the sender's note "J. Kraus, XVIII., Schulgasse 9" are uncertain readings.
5. Steganography: the printed stamp box is empty and no hidden writing was found on the picture or the edges. The stamp is glued diagonally off the box, so a note under it cannot be ruled out from the scan.
6. Whether this writer is the same person as on HCP 1194/1195 (1900) is not known; the alphabet is the same, but the recipient differs.

## Review and changes

An independent Claude Opus 5.5 reviewer re-ran the command, re-read every sign, checked the date (a Saturday) and the postmarks, and returned **ACCEPT** with five minor findings:

1. The W is not a heavier fehu, as first claimed, but the same sign as F. The key file, transcription and decoder now use one sign F/W and resolve it explicitly by word sense.
2. The solution now says plainly that P and W come from word sense (literal output ABFELFEIN).
3. The I is now stated to rest on word sense, since it is mainly a dash.
4. The share of unread cipher signs (8 of 22) is now stated, and the register type is plain MASC, since no steganography was found.
5. The street name stays marked uncertain.

None of these changed the reading.

## Credit

Transcription, key transfer and decipherment by Claude Opus 5.5 (2026-11-03); key values from the sister cards HCP 1194 and 1195; independent review by a separate Claude Opus 5.5 agent. No published solution was used.
