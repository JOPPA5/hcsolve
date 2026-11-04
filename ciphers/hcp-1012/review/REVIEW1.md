REVISE

# Review 1 - hcp-1012 (cpc_-11-12_DE_Hof_DE_Selb_)

Reviewer: Claude Opus 5.5 (claude-opus-5-5), 2026-11-03. Solver: Claude Opus 5.5 (round 1).

## Summary

The decipherment is correct: the number substitution (position in the 25-letter alphabet without J, plus 6; A=7 ... Z=31) is confirmed independently and explains every number on the card. The plaintext is coherent period German. The problems are a word in the transcription that is not on the card ("Sie"), a mistranscribed sign (the ä is the cipher number 7 with an umlaut mark, not a plain Kurrent ä), an unexplained "F" mark, and a translation of the margin postscript that commits to one of two readings. These are concrete but small fixes; the reading stands.

## What I verified and how

1. Ran the solver command from the repo root: `python3 -I ciphers/hcp-1012/work/decode.py`. All four SHA-256 checks print OK. Output matches the claimed plaintext: "brif, erhalten, besten / Dank für aufklärung, / Entschuldigen Sie diese Karte. / brief, folgt, sonntag, / der nicht eher, zeit, / der alle tage / Stunden! H. Gruss. / Freundlichst auch ihr(e)?".
2. Independent decoder `review/work/my_decode.py`, run on my own reading of the card. It builds the key from the J-less alphabet and decodes my reading to BRIF ERHALTEN BESTEN / AUFKLÄRUNG / BRIEF FOLGT SONNTAG / NICHT EHER ZEIT / ALLE TAGE. 16 distinct numbers (7 8 11 12 13 14 15 16 17 19 20 23 24 25 26 31), all in 7..31, none left over.
3. Dropping J is confirmed by the card itself: AUFKLÄRUNG has 16 = K and 17 = L next to each other. With J in the alphabet K would be 17. The rule is overdetermined: 16 letters fit one arithmetic rule, with two independent occurrences of BRIEF/BRIF and of ERHALTEN/EHER.
4. Transcription check against `work/hires/..._pic.jpg`, rotated 90 degrees counter-clockwise (`review/work/pic_rot.jpg`). Every message line was cropped at 1.2x, and the doubtful signs at 3-4x (`review/work/a1-a6.jpg`, `b1-b6.jpg`, `ae3.jpg`, `diese.jpg`, `der1.jpg`, `der2.jpg`, `ps.jpg`). All number groups in lines 1, 2, 4, 5 and 6 match the transcription sign for sign, including "8: 11.24.25.11.19", "24.20.nn.25.7.13" (four minims, read as nn), "19.15.ch.25", "11.h.11.23" and "31.11.15.25".
5. The two "der" words (`der1.jpg`, `der2.jpg`): a looped d followed by about four short strokes that end in an r-like tail. "der" is a fair pixel reading. Kurrent "da" (with a closed a) is not there, and "denn" would need more minims. Translating it as "since" rests on word sense, and the solver says so. Accepted.
6. Address side: "Wohlgeboren / Fräulein Rosa Lang / Selb / Kirchplatz", Bavarian 5 Pf stamp, Hof 12 NOV, Selb 13 NOV. This matches the solver's description and the portal recipient "Fräulein Lang". The pencil "25.194" in the top margin is a collector or dealer number, not part of the message.
7. Steganography: I found no writing around the stamp, at the edges of the address side, or in the picture. The printed verse is struck through, but the strikes do not pick out letters in any way I could read as a message. As the solver says, the area under the stamp cannot be inspected.
8. No published solution was found or claimed. The portal lists none.

## Findings

1. **(major) "Sie" is not on the card.** Line 3 reads "Entschuldigen Diese[n/r] Karte!" (`review/work/a3.jpg`, `diese.jpg`). After "Entschuldigen" comes a single word that starts with a looped capital D, then a dotted i, e, long s, e, and a final n or r stroke. There is no separate "Sie". The transcription, the plaintext and `decode.py` output give "Entschuldigen Sie diese Karte". Transcribe the word as written ("Diese", or "Diesen/Dieser" if the final stroke is counted) and mark "[Sie]" as an editorial supply. The meaning does not change.
2. **(minor) The ä in AUFKLÄRUNG is the cipher number 7 with an umlaut mark, not plain Kurrent ä.** At 3x (`review/work/ae3.jpg`) the sign is the same crossed "7" used elsewhere for A, with a small Kurrent e-shaped umlaut mark written above it. The transcription should read `7(umlaut)` rather than `{ä}`, and uncertainty 4 should be corrected. The decoded result does not change.
3. **(minor) The "F" before the first "der" is a separate mark.** In `der1.jpg` a clear F with two crossbars stands after "7.13" and is detached from the loop of the d. SOLUTION.md calls it an "F-shaped lead-in stroke". It should be recorded as an unexplained separate mark, for example a false start or correction.
4. **(minor) The postscript translation commits to one reading.** The margin line (`review/work/ps.jpg`) reads "Freundlichst auch ihre" (or "Ihre"), possibly with a final comma. If it is the formal "Ihre", it is a closing formula, "Most kindly, also your ...", leading into the monogram. If it is "ihr", it means "[greetings] to her too". The English "Kindest [regards] to her too" and the Slovak "Najsrdečnejšie aj jej" give only the second. Give both readings, or prefer "Ihre", since the writer addresses the recipient with the formal "Sie" form throughout. Also, in the rotated reading orientation this line runs up the left margin. "Upside down at the top edge" is true only for the scan as delivered, so say which orientation is meant.
5. **(minor) Register type.** The cipher is plain number substitution with plain Kurrent words mixed in. If an entry is written later, use `MASC`. No steganographic message was found, so `MASC + Steganography` does not apply on this evidence.

## What I could not verify

- The area under the stamp. The scan cannot show it.
- The year. The postmarks show no legible year. "About 1900-1910", based on the Bavarian arms stamp, is plausible but unproven.
- The signature monogram, which I also cannot read. It is correctly disclosed as unread. It is a single signature item, not an unread clause, so the card still counts as complete.
- Whether the final stroke of "Diese(n/r)" is n or r.
