# HCP 947 – solution (round 1, revised after review 1)

Card: cpc_1909-06-03_DE_Doberan_DE_Reddelich_ernagarbe-03, T. Schrödel collection, postmarked 3 June 1909 (1909-06-03 from the collection file name; on the scan only the year "09" of the postmark is securely legible), to Frl. Erna Garbe, Reddelich (Mecklenburg). Portal status Not solved, no attached transcription or solution. Solved by Claude Opus 5.5 on 2026-11-03; there was no earlier work on this number. No published solution was found or used (portal links only the generic collection paper).

## What is on the card

- Picture side: printed studio portrait of the actress Gudrun Hildebrandt (printed caption, publisher mark "GCo 1936/3"). No handwriting, no hidden text found in the picture or along the edges; the violet smear on the top edge is an ink stain, not writing.
- Address side: German Kurrent pencil greetings from several people (plain text, transcribed below), the address, a small drawn airship (Zeppelin) doodle bottom left, and a three-line block of invented-looking signs at the left margin. That block is the only ciphertext.
- Stamp: 5 Pf Germania, intact on the scan. Nothing written is visible around its perforations; what may be under it cannot be inspected from a scan (not lifted). This is a limit, not a finding.

## Cipher type and key

Simple monoalphabetic substitution in which each letter is replaced by an altered (mostly turned upside-down) Latin capital: register type **MASC**. Punctuation is written normally; each word is closed by ",-" and the last one by "!-".

| Sign (as drawn, card held with cursive upright) | Letter | Basis |
|---|---|---|
| ∀ (inverted A, crossbar), lines 1 and 2 | A | shape |
| hooked bracket / C open to the right | C | shape + word sense |
| H-like sign with extra strokes | H | word sense (ACH) |
| Λ with a faint central stem (inverted W) | W | shape + word sense |
| zigzag Σ-like sign (twice) | R | word sense, consistent in both places |
| 8 (closed S) | S | word sense |
| ⊥ | T | shape (inverted T) |
| ᗡ | D | shape (D turned 180°) |
| Π | U | shape (inverted U) |
| 工 (I-beam) | H | H turned 90°; word sense |
| stroke above, dot below | I | shape (i turned 180°) |
| 3 | E | shape (cursive Ɛ turned 180°) |

## Transcription and plaintext

Literal sign rows (see `work/decode.py` for the sign names):

```
∀  [C]  [H]  ,-
Λ| ∀'  Σ  8  ⊥  ,-
ᗡ  Π  ,-  工  'ı.  3  Σ  !-
```

Plaintext (German): **ACH, WÄRST DU HIER!** – "Ach, wärst du hier!"

- English: "Oh, if only you were here!"
- Slovak: "Ach, keby si tu bola!"

## Plain (unenciphered) text on the card – read from the Kurrent

- Writer 1 (revised after review 1): "Fröhliche Pfingsten und Grüße sendet. – Eine neue Karte folgt bald. H.(?) Weber."
  Line by line: "Fröhliche Pfingſten und" / "Grüße" / "sendet." (left column) and "Eine neue / Karte folgt / bald." (small column to the right).
  EN: "Happy Whitsun and greetings sends … A new card follows soon. H. Weber." SK: "Veselé Turíce a pozdravy posiela … Čoskoro príde nová pohľadnica. H. Weber."
  (In plain English: "H. Weber sends a happy Whitsun and greetings. A new card follows soon.")
- Writer 2: "Auch ich sende schönen Gruß. Kollegin Warchow"
  EN: "I too send kind regards. Colleague Warchow" SK: "Aj ja posielam pekný pozdrav. Kolegyňa Warchow"
- Writer 3: "Meinen Gruß sendet unbekannterweise A. Schmidt(?)"
  EN: "My greetings, though we have not met, A. Schmidt(?)" SK: "Môj pozdrav posiela neznámy/-a A. Schmidt(?)"
- Address: "Frl. Erna Garbe, Reddelich".

## Reproduce

From the repository root:

```
python3 -I ciphers/hcp-947/work/decode.py
```

It checks the SHA-256 of all four source/hires images and decodes the manual sign transcription through the key, printing `words    : ACH / WARST / DU / HIER!` and `plaintext: ACH WARST DU HIER!` (the ",-" signs are word separators, not commas). The transcription is manual (from enlarged crops in `work/`), not OCR.

## Uncertainties

- The umlaut in WÄRST rests on word sense alone: above the second sign of line 2 (the ∀) there is only a single small upright tick, not two dots and not drawn turned like the letter; the literal decode gives WARST ("Ach, warst du hier!" would also be German but less idiomatic).
- R (zigzag sign), S (8), C (bracket) and both H forms rest on word sense; R is at least consistent in its two occurrences. The two H signs differ in form (H-like in line 1, I-beam in line 3).
- Plain text, writer 1: "und" at the end of line 1 rests partly on word sense. After "Pfingſt" the strokes are e-n (two pairs of minims), then u-n (minims, the first with a small loop) and a tall looped final letter that I take as Kurrent d; read literally without context it could also be taken as e-n-o-r-k (reviewer) or ...woch (Pfingstwoche). "Grüße" (line 2) is read from the letter shapes (G with descender, r, ü with a dot-like mark, ß as ſ plus a z-loop, e); a "Wünsche" reading would give the same sense. The tall strokes that cross line 2 (including the "!"-like one) are the descenders of P and f in "Pf" from line 1 (crop work/r1_l12.png).
- Signatures: the initial before Weber is a large looped capital, H or J; "A. Schmidt" is likely but not certain. "Warchow" is now read securely (W-a-r-c-h-o-w, work/r1_warchow.png).
- The area under the stamp could not be inspected.

## Why I believe it is correct

All 12 cipher signs are used, and they give the idiomatic postcard phrase "Ach, wärst du hier!" with word lengths 3/5/2/4 matching the separators ",-". Six signs (∀, ⊥, Π, ᗡ, inverted i with dot below, 3) are visibly Latin letters turned upside down, which fixes the system; the rest follow from one coherent sentence. The message suits a card full of greetings to Erna Garbe.

## Response to review 1

Reviewer verdict REVISE (Claude Opus 5.5, 2026-11-03). The ciphertext reading was confirmed; the findings concern the plain Kurrent text, the script output and wording. New crops of the hires scan: work/r1_full.png, r1_line1.png, r1_pfingst.png, r1_end.png, r1_mid.png, r1_line2.png, r1_line2b.png, r1_l2a.png, r1_l2b.png, r1_l12.png, r1_l3.png, r1_col2.png, r1_warchow.png.

1. **"Grüße" vs "gewünscht" (major) – disagree, with evidence; reading kept, uncertainty added.** The crop work/r1_l12.png shows lines 1 and 2 together. The tall stroke that looked like "!" after the word, and the tall stroke over the apparent "h", are the long descenders of P and f in "Pfingſt" on line 1. They run straight down from that word. Once these are removed, line 2 has only five letter groups: a capital with a descender (G), r, ü (a dot-like mark at hires x≈480), ß (a long ſ plus a z-loop at the baseline) and a final e. This is too short for g-e-w-ü-n-ſ-c-h-t, which would need about ten minim strokes between the first letter and the ſ; I count about five. Also, no t is present, since the supposed t is the f-descender. "Grüße" also gives "sendet" (line 3, clearly ſ-e-n-d-e-t, work/r1_l3.png) the object it needs. A "gewünscht" reading would leave "sendet" without one. "Wünsche" is noted as an alternative with the same meaning.
2. **"Pfingst…" ending (major) – addressed.** The ending is re-read as "Pfingſten und": e-n, then u-n, then a tall looped final letter read as Kurrent d. SOLUTION.md now states that "und" rests partly on word sense and gives the literal alternatives (the reviewer's e-n-o-r-k shape; "Pfingstwoche", which would also fit the posting date of Thursday 3 June 1909, four days after Whit Sunday on 30 May). Whichever reading is right, the clause is read: "Fröhliche Pfingsten und Grüße sendet" with one uncertain word. The opening clause is therefore not an unread clause. The column "Eine neue Karte folgt bald." reads cleanly (work/r1_col2.png).
3. **decode.py comma (minor) – fixed.** ",-" is now treated as a word separator. Re-run from the repo root: `python3 -I ciphers/hcp-947/work/decode.py` prints `source hashes OK`, `words    : ACH / WARST / DU / HIER!`, `plaintext: ACH WARST DU HIER!`. The reading "Ach, wärst du hier!" adds the comma and umlaut as normal orthography.
4. **Umlaut mark (minor) – fixed.** The Uncertainties section now says that the mark is a single upright tick, not two dots and not drawn turned, so Ä rests on word sense alone.
5. **Signatures (minor) – fixed.** "Warkow" is corrected to "Warchow". The letters W-a-r-c-h-o-w are clear in work/r1_warchow.png, and Warchow is a Mecklenburg surname. The Weber initial is given as H or J.

The cipher reading, the key and the type (MASC) are unchanged. As the reviewer also found, nothing hidden is visible under or around the stamp or in the picture, so the label "MASC + Steganography" is not used.
