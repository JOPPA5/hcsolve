# HCP1301 — deciphered Hungarian message; reviewed; corrections incorporated

Solver: OpenAI GPT-6. Independent reviewer: Claude Opus 5.5, review 1 dated 2026-10-12.

## Claim and scope
The complete main cryptogram and the four-line cryptogram under the removed stamp can be read with a monoalphabetic graphic substitution. It is the same alphabet as HCP1243. This replaces the previous unsuccessful scout: that scout merged short/long strokes and misread ligatures and accents. The present result comes from visual reading across both cards, not from the old statistical score.

Source: the archived address-side scan of the 4 June 1912 postcard to Tóth Jolánka. No exact earlier decipherment was found in the previous bounded publication audit; this is not a claim of exhaustive historical priority. Printed picture-side verse is ordinary Hungarian, not ciphertext.

## Key

The h/p shapes are near-homographs at this resolution and sometimes require context; d/n can differ mainly in stroke length. The named classes describe tendencies, not a deterministic image classifier.
`work/graphic-key.json` gives the reproducible named graphic classes. Shapes are mnemonic descriptions, not a claim that modern Unicode exactly reproduces the handwriting:

| Plain | Graphic class | Plain | Graphic class |
|---|---|---|---|
| a | two horizontal bars | b | 6-like |
| c | left bowl | d | two joined long strokes |
| e | three horizontal bars | f | cross |
| g | open loop with descending stroke | h | two separate tall strokes |
| i | crossed curved stroke, normally dotted | j | inverted T |
| k | section-sign-like curve | l | wave |
| m | three short strokes | n | two short strokes |
| o | cursive loop | p | tall stroke with short companion |
| r | F-like | s | right bowl |
| t | gamma-like corner | u | x-like cross |
| v | chevron | y | low descending curve |
| z | crossed diagonal | | |

Vowel accents are written above the substitution signs. They are sometimes faint or omitted. Joined `gy` and `cs` can look like one sign; the small circle in `csak` and the stamp greeting is the joined left/right bowls, `cs`. Numerals in the schedule are literal. The f class is most clearly supported by the companion card. This is a shared graphic alphabet, not an invented key for each word.

## Plaintext, normalized Hungarian
Punctuation, word boundaries, consistent accents and doubled consonants below are editorial. The manual row edition distinguishes proposed visible text from explicit editorial repairs; it is not a blind shape transcription.

> Kedves Jolánkám! Hogy telt el a vasárnapja? Remélem, jól. Ami engem illet, elég jól telt, mert nem volt egy percz szabad időm. Délután 3-tól ötig választmányi ülés, öttől hétig tűzoltógyakorlat, és este ½9-től 12-ig a mozgószínházban voltam őrségen. Abból is láthatja, Jolánkám, édesem, nem mehettem le. Majd jövő vasárnap okvetlen lemegyek, de ha csak teheti, jöjjön fel, édesem, csütörtökön. Epedő szívvel várva maradok őszinte imádója. Tisztelem kedves mamáját.

Under the removed stamp, after rotating its text 90° counterclockwise:

> Csókolja a távolból imádója.

## English translation
My dear Jolánka! How was your Sunday? I hope it was pleasant. As for me, it went quite well, because I did not have a minute to spare. From three to five in the afternoon there was a committee meeting, from five to seven a fire brigade drill, and in the evening from half past eight until midnight I was on guard duty at the cinema. From this you can see, my dear Jolánka, my sweetheart, that I could not come down. Next Sunday I shall certainly come down, but if you possibly can, come up on Thursday, my sweetheart. Waiting for you with a yearning heart, I remain your sincere admirer. My respects to your dear mother.

Under the stamp: Your admirer kisses you from afar.

## Reproduction and evidence limits
There is currently **no source-image-to-plaintext command**. The prior token ledger was generated from a hard-coded manual reading, not independently transcribed sign by sign. It has been renamed `work/manual-edition.json`; its output is an editorial aid, not verification.

```sh
python3 batches/postcards-five-2026-10-12/verification/decode.py 1301
```

This checks the archived image hash and displays the saved manual row edition. It does not OCR or decipher pixels. The actual correctness evidence is the reviewer's independent sign-by-sign rereading of the original scan, recorded in `review/REVIEW1.md`. The source-comparison page assists inspection; row rectangles are approximate inspection windows, not segmented glyph coordinates. For HCP1301 the stamp rows share one inspection rectangle; this does not locate individual rows.

## Uncertainties and editorial repairs
- Main row 4 appears `ilet`, row 5 `nem vol`, row 11 `aból`, row 13 `mehetem`; doubled letters or the final t in `volt` were restored in the normalized paragraph, not asserted as extra cipher signs.
- Rows 7–8 contain written numerals 5 and 7 (the first is overwritten); `5tig` / `5tól 7ig` are normalized to Hungarian words.
- Final main-row signature is abbreviated `imádoj.`; `imádója` is an expansion, corroborated by the stamp message.
- Accent placement and one overwritten sign in `vasárnapja` are less secure than the lexical reading. `csak` uses a joined cs shape, not the numeral zero.
- The reviewer independently confirmed the complete message. The REVISE findings below have been addressed using the explicitly permitted documentary correction route; no second review round is claimed. No external register submission has been made.

## Why this is more than a plausible opening
One graphic alphabet explains the salutation, the full 20-row narrative, the distinctive words `választmányi`, `tűzoltógyakorlat`, `mozgószínházban`, the final greeting to the mother, and the separately oriented stamp message. The same alphabet also reads HCP1243's unrelated arrival/posting narrative and love verse. The full endings were visually checked, not inferred from a successful synthetic control.

## Response to review 1
1. **Reproduction limitation:** accepted. The ledger is now called `manual-edition.json`, not “verified”. No source-to-plaintext command exists; this is stated explicitly above, taking the alternative the reviewer expressly allowed under “Required for closing”. The successful round trip is not evidence.
2. **Row 9:** corrected to `kolatéseste½9től12ig`. The normalized word `gyako(r)lat` restores an absent r, and the visible `és` is retained in Hungarian and as “and” in English.
3. **Row 17:** corrected to `tö{rt?}ökön`, preserving the unresolved single hooked sign. The normalized `csütörtökön` expands a possible rt ligature or supplies a missing letter; it does not claim eight separate signs.
4. **Key:** h/p near-homography and d/n stroke-length ambiguity are now explicit.
5. **Row 6:** the uncertain a/e bar count is shown as `b{a|e}d`; `szabad` remains the lexical interpretation.
6. **Protocol and method:** the English translation change after DONE1 was explicitly requested by the user. No watcher is launched under the user's standing instruction. The batch summary now says English. The visual break-in used the repeated Jolánkám salutation and shared greetings across 1301/1243, then checked the alphabet against long unrelated words and the rotated stamp message; no contemporaneous glyph-by-glyph discovery log exists, so this is a retrospective method summary, not a reconstructed trial history.

The reviewer's verdict remains **REVISE** as written; the reviewer explicitly stated that these documentary corrections need no further review. Closure follows that instruction and README step 5. The companion card has a possible cursive signature `De…`; its exact name is unresolved and is not used to identify this sender.
