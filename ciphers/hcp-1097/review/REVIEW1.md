REVISE

# Review 1 of hcp-1097 (reviewer: Claude Opus 5.5, 2026-11-03)

## What I verified and how

1. Ran the command from SOLUTION.md: `python3 -I ciphers/hcp-1097/work/decode.py`. Hash check passes ("source hashes OK"); output matches the claimed transcription, literal decoding and plaintext line by line.
2. Wrote my own decoder, `review/work/my_decode.py` (vowel key 1=a 2=e 3=i 4=o 5=u, consonants clear), over my own reading of the 11 lines plus the foot note. It gives the same 11 message lines as the solver.
3. Transcription against the pixels: cropped every line of the hires address side (`review/work/line01.png` … `line12.png`) and enlarged the doubtful places 2-3x (`z_this.png`, `z_busy.png`, `z_l11.png`, `z_am.png`, `z_answered.png`, `z_foot.png`). All 11 message lines read as the solver transcribed them. Specific checks:
   - line 6 "th1s": the third sign is a plain vertical stroke (the a-sign), as disclosed; "this" rests on word sense.
   - line 7 "b3sy": a heavy, overwritten 3-shape; it may have been written over another figure (possibly 5). "busy" on word sense, disclosed.
   - line 11 "1g41ng": the fourth sign is a stroke; "agoing" on word sense, disclosed. The final sign of this line is a heavy blot of 3/?-shape; "?" is a reasonable reading.
   - line 10 "w4lsl2b2n": w-4-l-s-l-2-b-2-n is clear.
4. Picture side (`review/work/pic_overview.png`): printed view "A Quiet Spot", only the HCPortal collection stamp; no hidden writing seen. Under the stamp cannot be inspected from scans (disclosed). The user's remark about writing under the stamp concerns the Jolánka series; this US card is not part of it, and nothing here suggests a hidden layer, so MASC (not "MASC + Steganography") is the right type.
5. Plaintext: coherent rural American English of 1909 with the writer's own spellings ("to late", "spose", "your" = you're); corn husking fits a 1 November postmark. Key covers every sign of the 11 lines.
6. No portal solution or transcription is attached; I found no claim of a published solution.

## Findings

1. **major — the foot note is very probably the enciphered signature "Maud", not a collector number.** The bracketed item under the last line is in the same pencil and hand as the message, centred where a signature goes. Enlarged (`review/work/z_foot.png`): the first sign has the same looped lead-in plus humps as this writer's m in "1m" (line 9, `z_am.png`); the second is a "1"; the third a "5"; the last has a bowl with an ascender rising above it, the same form as the writer's d in "1nsw2r2d" (`z_answered.png`) and "c1rd", rather than a 9. Read as "(m15d)" it decodes with the card's own key to "(maud)", a common female first name of the period; "n…" gives no word. SOLUTION.md says "Sender unsigned" and "It contains no message text", which is then wrong. Fix: transcribe the foot note as (m15d) = Maud (sender's signature), mark the m/n and d/9 calls as resting on letter form plus word sense, include it in the plaintext and translation, and drop the collector-number claim (or argue it with evidence).
2. **minor — Slovak translation of the sender's gender.** With the signature Maud, the sender is a woman; "dostal(a)", "odpovedal(a)" can become "dostala", "odpovedala".
3. **minor — no English/Slovak note on "Wolsleben".** The reading is clear; whether it is a family (at the Wolslebens') or a place is undetermined and is disclosed. Fine as is; just keep it disclosed in the report.
4. **minor — line 11 final sign.** The heavy terminal mark after "st1y" is read as "?"; it could be a blotted 3-shape. Worth one sentence among the uncertainties (it does not change the reading).

## What I could not verify

- The area under the stamp (scans only).
- Whether "Wolsleben" is a Nebraska family or place, and the identity of Ben Russell / Maud; no records checked.
- The blurred year digit of the postmark (portal file name gives 1909-11-01).
