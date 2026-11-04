# hcp-989 — Solution (round 1, Claude Opus 5.5, 2026-11-03)

Card: embossed picture postcard (sailing ship in a storm, wooden frame with flowers), Wien, postmark 19 X 1901,
to "Hochwohlgeboren Herrn Hugo P(?)ell, Beamten, Wien Hernals XVII, Weidmanngasse(?) 3". Sender's note at the lower
left of the address side (plain Kurrent): "Absender J.(?) Kraus, Wien XVIII. Schulgasse(?) 9" (names read with
uncertainty, reported literally). T. Schrödel collection; portal status Not solved, no transcription or solution
attached. Short web search for this card: nothing found. No earlier work on this number; transcription, key and
decipherment are by Claude Opus 5.5.

The message is written in ink along the left margin of the picture side (card turned 90°), mostly in plain German
Kurrent; only the place of the meeting is enciphered (two words) plus one parenthetical word.

## Cipher type and key

Simple monoalphabetic substitution (MASC) with a home-made rune-like alphabet, German plaintext. It is the same
alphabet family as the Vienna/Tepl cards hcp-1194 and hcp-1195 (to Anton Schönfelder, Wien IV, 1900), and every
sign on this card that was read takes the value it has there; nothing was invented for this card:

| sign (code in work/key.json) | letter | same value on |
|---|---|---|
| stem with short slant stroke on the left, ᛅ-like (diag) | A | 1194, 1195 |
| B-shape with long tail, ᛒ (b) | P in APFEL, B in STUBE | B on 1194/1195 (P there = dotted B; no dot here) |
| fehu, two twigs ᚠ (f2) | F in APFEL, W in WEIN | F on 1194/1195 (W there = heavy/dotted ᚠ; on this card both are the same plain sign) |
| cross, here slanted as X (x) | E | 1194, 1195 (+ = E) |
| stem with hook at top, ᛚ (hook_l) | L | 1194, 1195 |
| plain stem ᛁ (stem); here mainly a short dash with a ghost stem | I | 1194, 1195 |
| lambda Λ (lam) | N | 1194, 1195 |
| lightning ϟ (bolt) | S | 1194, 1195 |
| up-arrow ᛏ (arrow_up) | T | 1194, 1195 |
| square u-rune Π (u_pi) | U | 1194, 1195 |

## Command (from repo root)

    python3 -I ciphers/hcp-989/work/decode.py

It checks the SHA-256 of the two source images and the two hi-res originals, applies work/key.json to
work/transcription.txt and prints the decoded words and the full message. Output (decoded part):

    cipher signs -> AP/BF/WELF/WEIN. STUP/BE.
    decoded      -> APFELWEIN. STUBE.

## Plaintext (German; enciphered part in capitals)

    Lieber Hugo                                    3/4 7 - 7 Uhr
    Ich erwarte Dich zwischen [blacked out] Uhr
    in der APFELWEIN. STUBE.
    [struck-out word] ([one enciphered word, not read]) am Samstag 19/10      Toni

Normalised: "Lieber Hugo! Ich erwarte Dich zwischen ¾7 und 7 Uhr in der Apfelweinstube (...) am Samstag 19/10. Toni."

English: "Dear Hugo! I'll be waiting for you between a quarter to seven and seven o'clock in the cider tavern
(Apfelweinstube) (...) on Saturday 19/10. Toni."

Slovak: "Milý Hugo! Budem ťa čakať medzi trištvrte na sedem a siedmou v jabĺčnej vinárni (Apfelweinstube) (...)
v sobotu 19. 10. Toni."

19 October 1901 was a Saturday, and the address side is postmarked Wien 19 X 01: the card arranges a meeting the
same evening (Vienna had several delivery rounds a day).

## Uncertainties (all disclosed)

1. The parenthetical word on line 4 ("(" + 8 signs + ")") is NOT read. Signs 3–5 are thickly overwritten by the
   writer (corrections); sign 1 looks like ϟ (S) with a top bar, sign 2 like the Y-form of E, signs 6–7 like K
   (ᚴ with a leg) and I (ᛁ), sign 8 is a 大-shape not in the sister keys. No word fits that I can defend, so it is
   left open (crops work/crops/p1.png, pa.png, pb.png). It is a single word in parentheses — probably a name or
   location of the tavern — and the rest of the message reads without it.
2. The word before that parenthesis is struck through / inked over by the writer (crop st.png) and cannot be read;
   it is a deleted word, not cipher.
3. The time after "zwischen" is blacked out with ink by the writer (crop c4.png); the corrected time is written as a
   header to the right of the greeting: "3/4 7 - 7 Uhr" (crop t1.png).
4. P in APFEL: the writer uses the same B-shaped sign in APFEL and STUBE (compare line3.png, w1a.png, c2.png). On
   1195 P is a dotted B; no dot is visible here. P rests on word sense (Viennese b/p are both lenis).
5. W vs F (corrected after review 1): sign 6 of the first word is the same two-twig ᚠ as sign 3, with the same
   stroke weight and no dot. This card writes F and W with one sign, so W rests wholly on word sense (APFELWEIN).
6. Signs 8 and 9 of the first word (I, N) are written with a drying pen: the I is mainly a short dark horizontal dash with only a ghost of a
   stem, so I rests on word sense (a hyphen inside the word makes no sense);
   the Λ has a faint right leg (crop w1b.png). The full stop after APFELWEIN is written; "Apfelwein. Stube." is
   taken as the compound Apfelweinstube.
7. Plain-script names: the signature reads "Toni" (initial T/J ambiguous in Kurrent, crop sig.png); recipient's
   surname P?ell/Pöll and sender's note "J. Kraus, XVIII., Schulgasse 9" are uncertain readings of plain script.
8. Steganography check: the stamp is glued diagonally over the printed header of the address side, not in the stamp
   box (which is empty); nothing is visible under or around it in the scan, but the area beneath the stamp cannot be
   inspected from the scan. No other hidden writing seen on the picture or edges.

## Why I believe it is correct

- The key was not fitted to this card: all 11 distinct read signs take exactly the values of the independently
  solved sister alphabet (hcp-1194/1195). Applied literally the key gives ABFELFEIN. STUBE.; two of the nine letters
  of APFELWEIN (P and W) come from word sense, because this card writes P/B and F/W with one sign each, and the I is
  a weak dash. E is consistent in three positions. APFELWEIN STUBE is the only German reading the sign pattern allows,
  and Apfelweinstube is a real Viennese tavern type.
- The decoded words fit the sentence "Ich erwarte Dich ... in der ___" (a place, feminine noun: die Stube) and the
  setting (a Saturday evening rendezvous in Vienna, 1901). The date and weekday agree with the postmark.

## Credit

All work on this card: Claude Opus 5.5 (2026-11-03). Key values taken from the sister cards hcp-1194 and hcp-1195
(also Claude Opus 5.5, same day); no published solution used.

## Response to review 1

Verdict ACCEPT; all five minor findings addressed, the reading is unchanged.

1. W not a heavy ᚠ — agreed. On the 4x crop (review/work/s4to9.png, work/crops/line3.png) signs 3 and 6 have the same
   form and weight. Fixed: work/key.json now has one code f2 = F/W (f2heavy removed), work/transcription.txt writes
   f2 for both, work/decode.py resolves F/W explicitly by word sense; key table and uncertainty 5 rewritten.
   Re-ran `python3 -I ciphers/hcp-989/work/decode.py`: hashes OK, `AP/BF/WELF/WEIN. STUP/BE.` -> `APFELWEIN. STUBE.`
2. P and W from word sense — agreed; "Why I believe it is correct" now states that the literal output is ABFELFEIN
   and that P and W are word-sense calls.
3. I is mainly a dash — agreed; uncertainty 6 and the key table now say I rests on word sense.
4. Proportion unread — agreed: 8 of the 22 cipher signs (about a third) are in the unread parenthetical word; this is
   stated in the report. It is one word and the rest of the card reads, so the card counts as complete. Register type
   is plain MASC: the stamp box is empty and no hidden writing was found (the area under the diagonally glued stamp
   cannot be inspected from the scan; disclosed, uncertainty 8). The human's note that cards of the Jolánka /
   Arokszállás series carry steganographic messages under the stamp concerns that series, not this Vienna card.
5. Weidmanngasse(?) — left marked uncertain, as the reviewer suggests.
