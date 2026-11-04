ACCEPT

# Review 1 – hcp-993 (Erich to Margarethe Kellermann, München 1903)

Reviewer: Claude Opus 5.5, 2026-11-03. Role: reviewer, round 1 (highest marker DONE1).

## What I verified and how

1. **Solver command.** `python3 -I ciphers/hcp-993/work/decode.py` from the repo root: "source hashes OK", and the
   output is the same as the line-by-line plaintext in SOLUTION.md (L1–L14), word for word.
2. **Independent decoder.** `review/work/verify.py` has its own key table and its own parser for
   `work/transcription.txt`. Run it with
   `python3 -I ciphers/hcp-993/review/work/verify.py ciphers/hcp-993/work/transcription.txt`.
   It gives the same plaintext. It also counts the signs: 337 signs read directly from the card, 6 restored (smear or
   card edge), 1 supplied (the omitted d of "ungeduldiger") and 1 emended (dahin). Every sign falls within the
   23-sign key, and no sign has two values. Each listed restoration matches a disclosed item in SOLUTION.md
   "Uncertainties".
3. **Transcription against the pixels.** I rotated the hi-res picture side by 90 degrees (`review/work/rot.png`) and
   read enlarged crops (2–6x) of every cipher line (`review/work/r0_*…r5_*.png`, `grid.png`, `s_L*.png`, `z_*.png`).
   I checked these lines sign by sign against the transcription and found them correct: L1 (mein herzinniggeliebtes
   herzens....!), L3 (werde von tag zu tag ungedul–), L4, L5 (with the boxed 18), L6, L7 (strich durch die rechnung),
   L8 (lieb! dein e wird dich ganz und), L9 right half, L10, L11, and the upside-down L12–L13 (und küssen / dein
   erich) with the two rows of four dots.
   - "ungedul-iger": the card has U 2 9 4 V U 1 and then a hyphen. The second d really is missing, and this is
     disclosed.
   - Smear band (left third of lines L6–L11). Below the smear I can see the faint shapes for ≠φ22 (kann),
     ꝛ0-0-?-1 (wohl, with the h unreadable) and Feldwebel (the e's and the final 1 are visible; the b is not). In
     "aufessen" the gap between + and 5 measures about 2.8 sign-advances (the advance taken from "542" next to it).
     That fits two hidden signs, so the restoration "es" agrees with the spacing, but the letters themselves cannot
     be seen. All of these are disclosed as restorations.
4. **Plain Kurrent sentence.** "…einen lieben brief habe ich erhalten. Bin kern=/gesund." is legible. The word
   "kern" is dense, and the solver's word-sense disclosure is fair. The text joins the cipher on both sides.
5. **Language and context.** The text is idiomatic German of c. 1900 and fits a love letter from a soldier: the
   Feldwebel who might spoil his leave, 18 days until the visit, "aufessen" as a lover's joke. The ciphertext gives
   no internal contradictions.
6. **Address side.** It reads "Fräulein Margarethe Kellermann / p. Adr. Herrn A. Weyhe / Hochwohlgeboren /
   Eschersheim b/Frankfurt a/Main / Frankfurterstr. 49". The Eschersheim arrival postmark reads "-4.2.03 6-7 V."
   The stamp is still affixed, so nothing under it can be checked; this is disclosed. I saw no other writing in the
   margins or on the picture apart from the message. Below the dots there are a few ink specks, but no letters.
7. **Published solution.** None is attached on the portal, and SOURCES.md records the HistoCrypt abstract check.
   I found nothing that suggests the solver used an outside decipherment.

## Findings

1. **minor – the final "Grüßen" does carry umlaut dots.** In the crop `review/work/z_grussen.png`, two dots sit
   above the U of the last word of L11 (9 hook U 5 5 4 2). SOLUTION.md Uncertainty 2 says that the final "Grussen"
   "shows no umlaut dots". That statement is wrong: the transcription should use `Uuml`, and the explanation about
   ink running dry should go. The plaintext does not change.
2. **minor – the postmark statement is inaccurate.** SOLUTION.md says "postmarks München and Eschersheim 4.2.03".
   Only the Eschersheim mark legibly reads "-4.2.03 6-7 V.", which is an arrival in the morning. The München mark
   under the stamp is only partly legible. Its inner lines show a day "3" and month letters that look like "DEZ" or
   are unclear, plus a time slot (`review/work/stamp.png`, `stamp2.png`). It does not legibly read 4.2.03. An
   arrival in Frankfurt between 6 and 7 a.m. on 4 Feb implies the card was posted in München on 3 Feb, although
   the writer dated it "d. 4.". The solver should report the München mark as partly illegible and should not claim
   it confirms the date. The address transcription should also include "p. Adr." and "Hochwohlgeboren". None of
   this affects the decipherment.
3. **minor – "dahin": the 6-for-8 slip is not certain.** At 6x (`review/work/z_dahin.png`) the third sign has a
   closed lower loop and a heavy, ink-filled upper part. It could be an 8 with its top loop filled in, not a 6. The
   emendation to h is disclosed and the reading is the same either way. The wording "written as 6" should become
   "6-like; possibly 8 with a blotted upper loop".
4. **minor – punctuation.** A full stop stands after "wohl" (L10, before "und"), and it is not in the
   transcription. This is cosmetic.

## What I could not verify

- The letters hidden by the smear: the b of Feldwebel, the "es" of aufessen and the h of wohl. They are supported by
  spacing and word sense only, and are correctly disclosed. "auffressen" cannot be excluded completely, but the
  meaning is the same.
- Whatever may be under the affixed stamp (no hidden-writing check is possible from the scans).
- The München postmark date (see finding 2).
- The full HistoCrypt 2021 PDF (not checked by me either).

## Assessment

The key is a consistent single-value MASC that covers every cipher sign on the card. The plaintext is coherent
period German, and every restoration is disclosed and limited to single words inside a fully readable text. The
findings are all minor wording corrections. The register type MASC is appropriate, since no steganographic part was
found.
