# HCP 1451 (pc_hcp_132) — Atbash: "True and always loving"

Postcard posted at St Albans, 8 Feb 1906 (½d Edward VII stamp), to Miss L. Schuller, "The Queens Arms", High Street, Berkhamsted, Herts. Picture side: printed song card "My Little Octoroon" (print only, no handwriting). The cipher is the four-line handwritten note on the left of the address side. Portal status when captured: Not solved; no transcription or solution attached; no published solution of this card found.

## Cipher type and key

Atbash (reversed Latin alphabet), letter for letter, word divisions and capitals kept:

```
plain : A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
cipher: Z Y X W V U T S R Q P O N M L K J I H G F E D C B A
```

## Transcription (from source/address.jpg, 5x enlarged crops) and plaintext

| Line | As written (diplomatic) | Normalised cipher | Plain |
|---|---|---|---|
| 1 | Gifv | Gifv | True |
| 2 | Jmw | Zmw | And |
| 3 | Jodjbh | Zodzbh | Always |
| 4 | Olermt | Olermt | Loving |

Below the text: "— " —" (dash, double tick, dash), decorative/closing marks without letters.

**Plaintext (English, original):** True and always loving
**Slovak:** Verný a vždy milujúci (verná a vždy milujúca)
(A standard Edwardian closing line; no name follows.)

## Command (from repo root)

```sh
python3 -I ciphers/hcp-1451/work/decode.py
```

Verifies the SHA-256 of all files in source/ (work/source-sha256.json), then Atbash-decodes work/transcription.json and prints `True And Always Loving` (19 letters).

## Uncertainties

1. **Z written as J (all three positions).** Every cipher Z on the card is written in a J/j form: the two capitals (lines 2 and 3) are J-shaped, and the fourth letter of line 3 is a clearly dotted lowercase j. The transcription is normalised J/j-glyph = Z (work/transcription.json keeps both `diplomatic` and normalised `cipher`). Literal J under Atbash gives Q ("True Qnd Qlwqys Loving"), so Z is the only reading that yields words. Because it happens at 3 of 3 positions it is systematic, not a single slip; whether the writer deliberately substituted J for Z or used a J-like z form (dotting it once) cannot be decided from one card. The plaintext is unaffected.
2. **Lines 2 and 4 completed in 2026-10-29.** Line 2 has three letters (the "n" of the earlier four-letter G?NV readings is the second arch of m); line 4's fourth glyph is a cursive r, not v.
3. No sender name or signature; the ditto-like tick under the text carries no letters. The sender is unknown.

## Why it is correct

All 19 cipher letters on the card decode under one fixed, keyless rule to four English words forming a common period closing phrase ("true and always loving"), consistent with an English postcard of 1906 to a young woman. Line 1 (Gifv → True) was found by the earlier work; lines 2–4 now read without alternatives.

## Corrections to earlier work and credit

Earlier work (OpenAI GPT solver, 2026-10-26; see NOTES.md, work/decode-atbash.py, work/transcription-atbash.json, work/stroke-audit.md) identified Atbash and read lines 1 and 3 (TRUE, ALWAYS), but left line 2 unresolved (four-letter G?NV hypotheses) and read line 4 as OLEVMT → "LOVENG". The completing reading by Claude Opus 5.5 on 2026-10-29: line 2 has three letters, Zmw → And; line 4's fourth glyph is a cursive r (no top-right hook, unlike the v of line 1), Olermt → Loving. The old decoder and transcription are kept for the record; the current ones are work/decode.py and work/transcription.json.

## Response to review 1

Review 1 (Claude Opus 5.5, verdict ACCEPT) had three minor findings; all accepted, reading unchanged.

1. **Transcription normalised, not diplomatic** – fixed. work/transcription.json now gives a `diplomatic` field per line (`Gifv / Jmw / Jodjbh / Olermt`) next to the normalised `cipher` field, plus a `diplomatic_note` stating J/j-glyph = Z as an interpretation. The line-3 note now calls the 4th glyph a dotted j (rechecked on review/work/all.png: the dot is a distinct ink point). work/decode.py now also asserts that diplomatic with J→Z equals the normalised text. Re-run: `python3 -I ciphers/hcp-1451/work/decode.py` → `True And Always Loving`, source hashes OK, 19 letters.
2. **"Writer's slip" understated** – agreed and fixed. Uncertainty 1 now says all 3 of 3 Z positions use a J/j form, i.e. a systematic habit, not a slip; the intent (J for Z vs. J-like z allograph) is left open.
3. **Line-2 letter count** – addressed in uncertainty 2 here and explained in the report: the earlier four-letter G?NV reading took the second arch of m for a separate n, and the J-shaped capital for G.
