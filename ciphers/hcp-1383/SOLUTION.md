# HCP 1383 / pc_hcp_64 — Caesar −1 English love note, Bournemouth, 23 September 1907

**Status: complete reading of the message: 73 of 73 enciphered letters. Two short abbreviation groups (`E. L.`, `M-L.`) are kept literal, as on the sister cards.**
All work on this number by Claude Opus 5.5 as solver, 2026-10-30. No earlier work, and no published solution was found or used. The portal status is Not solved, with no attached transcription or solution.

## Origin

The card is a Max Ettlinger "Royal Series" postcard (Bournemouth Series 1089) with a printed woodland picture and no handwriting on the picture side. It is addressed to Mr W. Abbott, Stokelake Farm, Chudleigh, S. Devon. The postmark reads BOURNEMOUTH 8 PM SP 23 07, which agrees with the plain date on the card and the portal date; 23 September 1907 was a Monday. The message runs sideways on the left of the address side (rotate 90° counter-clockwise).

Plain, not enciphered: the heading `1 Cleveland Rd` and the date `Monday Sep 23rd 07`.

## Cipher and key

Caesar shift: each cipher letter is one place after its plaintext letter (decrypt = shift −1). This is the key of the W. Abbott family (hcp-1386…1407). It was taken as a hypothesis from those cards and holds for every enciphered word here.

```text
cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

## Ciphertext (manual transcription, work/transcription.json) and plaintext

Square brackets mark groups kept literal. Dots and dashes are the writer's.

| Ciphertext | Plaintext |
|---|---|
| Nz. Pxo. [E. L.] Cpz. | MY. OWN. [E. L.] BOY. |
| kvtu dpnf. cbdl. | JUST COME. BACK. |
| J. gpvoe. mfuufst | I. FOUND. LETTERS |
| Xbjujoh. ifsf. gps | WAITING. HERE. FOR |
| pof. xffl. pomz. | ONE. WEEK. ONLY. |
| [M-L.] gspn zpvs Pxo [E-L.] | [M-L.] FROM YOUR OWN [E-L.] |
| Hjsm (written after the plain date) | GIRL |

English: "My own E. L. boy, just come back. I found letters waiting. Here for one week only. M-L. from your own E. L. girl." (The sentence division is editorial; see uncertainty 6.)

Slovak: „Môj vlastný E. L. chlapec, práve som sa vrátila. Našla som čakajúce listy. Tu som iba na jeden týždeň. M-L. od tvojho vlastného E. L. dievčaťa.“

## Command

Run from the repo root. It checks the source hashes and prints the full plaintext from the transcription and key:

```bash
python3 -I ciphers/hcp-1383/work/decode.py
```

## Uncertainties

1. **`E. L.` (twice) and `M-L.` are unexpanded abbreviations.** They are kept literal as on hcp-1386, 1403 and 1407. Shifted, they would give D. K. and L-K. The second is the group hcp-1395 reads as `L. & K.`, so `M-L.` may be enciphered; this card cannot decide that and no meaning is claimed.
2. **First letter of `M-L.`** Read as M because it has three downstrokes, against two in the N of `Nz` on the same card (work/crops/N_vs_closing.png). Sister cards have the same N/M doubt. The joining sign is a plain dash, not the `&` of the sisters.
3. **`Hjsm` could be mistaken for a plain time.** After the date it resembles "4/5 m". It is read as cipher GIRL because the j is a long slash with a hook, which hcp-1386 also records for this word (its uncertainty 1), and the family closing is "your own … girl", and because the formula otherwise lacks its last word. The written position after the date is unusual.
4. **Final `t` of `mfuufst`.** It is shaped like a c with a top stroke. A cipher c would give LETTERB, which is not a word, so it is read as t. The S before it is clear, so LETTERS is plural on the pixels.
5. **`Pxo` (twice).** The P is drawn as a small stem plus a large separate arc, with a dry thin connecting stroke. The second-line `E-L.` also has a dry thin ascender. Read as P and L, matching `Pxo` and `E. L.` on sister cards.
6. **Sentence division of "… waiting here for one week only".** The letters are certain, but the writer puts a dot after nearly every word, so the dots do not divide sentences. The translation takes "Here for one week only" as the writer's own stay, a usual telegraphic phrase on a holiday card. Alternatives are "I found letters waiting here. For one week only" (same sense) and the literal run-on "I found letters waiting here for one week only" (the letters had waited a week). The dates give some support to the stay: Bournemouth postmarks on 23, 24 and 26 Sep (this card, hcp-1382, hcp-1381), then WIMBORNE day 30 on hcp-1370. That support is weak, because the month of the hcp-1370 postmark is illegible, and its heading G. H. also occurs on hcp-1382 with a Bournemouth postmark. None of these three sisters has passed FINAL.

## Why this is correct

One fixed shift turns all 19 enciphered words into plain English without any exception or forced letter. The words run into a coherent sentence and end in the couple's known formula: salutation "My own E. L. boy" (hcp-1386, 1403) and closing "from your own E. L. girl" (hcp-1386). The recipient, year and hand match the family, and the plain date agrees with the postmark. No restoration was used: every letter is read from the card.

Crops used are in work/crops/; `work/crop*.py` regenerate most of them. Line crops: la…lg. Word and sign zooms: wa, wb, z*.

## Response to review 1

Verdict ACCEPT. All three minor findings are addressed. No letter changed, and `work/decode.py` and `work/transcription.json` are unchanged. I re-ran `python3 -I ciphers/hcp-1383/work/decode.py`: hashes OK, 73 shifted and 6 literal letters, the same output as in the table above.

1. **Parsing of "for one week only": fixed, with one correction to the argument.** The English and Slovak now read "I found letters waiting. Here for one week only", and uncertainty 6 gives the alternatives. I checked the supporting dates and they are weaker than the review states: the month of the hcp-1370 postmark is illegible (its SOLUTION.md, uncertainty 5), so "exactly one week" is not established, and "G. H." is also the heading of hcp-1382 (24 Sep, Bournemouth postmark), so that heading does not mark a move away from Bournemouth. I adopted the parsing for its natural sense, and I present the dates only as weak support.
2. **Word count: fixed.** "16" is now 19. Counted from `work/transcription.json`, excluding the literal groups.
3. **Citation: fixed.** Uncertainty 3 now cites hcp-1386 (uncertainty 1). A search of hcp-1398/SOLUTION.md for "slash" or "hook" finds nothing, which confirms the finding.
