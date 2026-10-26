# Portal1498 / pc_hcp_179 — full encrypted-passage candidate

The rendered portal showed Not solved on2026-10-26. **All18 Pigpen glyphs**
in the address-side passage map to:

```
LATE
TONIGHT
DARLING
```

Surrounding cursive makes the sentence:
“Don't be LATE, TONIGHT, DARLING, if you can help it.”
Commas between encrypted words are visible. Capitalization is editorial.
Slovak: „Ak môžeš, nemeškaj dnes večer, miláčik.“

## Cipher and key
Interleaved Pigpen alphabet. Outline tokens name the strokes present:
BR bottom/right; B bottom/left/right; BL bottom/left;
R top/bottom/right; C all four; L top/bottom/left;
TR top/right; T top/left/right; TL top/left.
0 means undotted,1 dotted. Wedges use their visible form V,>,<,^.
|Tokens|Letters|
|---|---|
|BR0 BR1|A B|
|B0 B1|C D|
|BL0 BL1|E F|
|R0 R1|G H|
|C0 C1|I J|
|L0 L1|K L|
|TR0 TR1|M N|
|T0 T1|O P|
|TL0 TL1|Q R|
|V0 V1|S T|
|>0 >1|U V|
|<0 <1|W X|
|^0 ^1|Y Z|

Only the symbols actually used here establish this passage's key; unused
entries are the conventional completion, not evidence of additional letters.

## Reproduction
Run from repository root:
`python3 ciphers/hcp-1498/work/decode.py`

No attached transcription; work/transcription.txt is an own manual reading
of source/address-large.jpg. Script checks immutable source hashes and
decodes all18 transcribed symbols; inverse-key roundtrip passes. This checks
mapping consistency, not independent pixel validation or OCR.

## Scope and limits
Claim covers the entire three-word Pigpen passage, not all surrounding cursive.
Cursive be/if and the rest of the letter are not encrypted positions.
Repeated T,N,I,G,L,A agree across words under one key. Image context supports
the reading, with no changed dots, per-word keys, or inferred extra glyphs.
No uncertain cipher symbol remains in this transcription; independent reviewer
must still inspect shapes and dots. No historical sender identification claim:
catalogue says sender Ernest, while greeting Dear Ernest and apparent closing
Maud are recorded separately rather than reconciled through speculation.
No published solution used. No accepted final solution, PDF or register entry
claimed before independent review.
Fresh register snapshot contains110 records with no exact source1498 or
name pc_hcp_179 match. This does not establish historical novelty.

## Response to review 1

Review 1 by Claude Opus 5.5 (2026-10-26), verdict ACCEPT. The reviewer read the
18 Pigpen signs independently with an own geometric key; the transcription is
token-identical and decodes to LATE / TONIGHT / DARLING. The reviewer also
checked the rest of the card and found no further cipher signs. No finding
changes the plaintext.

1. Address misread (minor) – accepted. The card reads "Mr E. Mobsby, 9 Carden
   Rd, Peckham, S.E."; the provisional "9 Ewerdon Rd" in source/metadata.md
   and the earlier notes is a misreading. source/ is unchanged; the correction
   is recorded here and in the report.
2. Sender/recipient (minor) – accepted. Ernest is the recipient (Mr E. Mobsby,
   greeted "Dear Ernest"); the writer signs "Yours etc Maud". The portal's
   "sender Ernest" field therefore appears to be wrong. The report says so and
   makes no further identity claim.
3. First sign of LATE (minor) – accepted. The dotted `[` (L) touches the final
   e of the cursive "be"; it is readable at 16x but is listed in the report as
   the one crowded sign.
4. What the command proves (minor) – accepted. The report states that
   decode.py checks the mapping of the manual transcription, not the pixels;
   the pixel check is the reviewer's independent reading.

Closing steps (this response, report, register entry, FINAL) prepared by Claude Opus 5.5 on the solver's behalf at the human's request, 2026-10-26.
