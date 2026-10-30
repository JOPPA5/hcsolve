# HCP 1193 — solver notes

## 2026-10-25: easy-target selection and first reading

User authorized selection of relatively easy unresolved HC Portal ciphers,
excluding 494 and 517. Checked README, skip list, local state and the live
register. Filtered the rendered catalogue by Not solved, Monoalphabetic,
and cpc_. The final catalogue page exposed 1188, 1189, 1190 and 1193;
1193 was selected first, descending. None has a local directory predating
this session, and none appears by source URL in the live register export.
Only 1193 has so far received the full three-tab inspection.

The Pigpen tag, small numerals and repeated outlines suggested a 3x3
alphabet repeated in blocks of nine. The observed HELEN, NOT GET THE
LETTER and EXPECTED TONIGHT gave a consistent reflected grid. Applied
the same key through the next lines, obtaining a sustained letter about
missing Helen and arriving almost as soon as the card. A brief switch
to German reads WAS IST LOS DENN MIT DIR?; LOSDENN is written without
an apparent intervening space.

No keyword search or external plaintext was used. All transcription is
manual; the script mechanically maps the entered shapes. It verifies
source hashes, but does not independently establish that the transcription
matches the pixels. This distinction matters: a successful decoder run
is not independent cryptanalytic validation.

Uncertainties: faded initial W, one isolated glyph after MY, several small
numerals, and the closing lines crossed by a collection stamp. Transcribed
lines 1–11 remain provisional, especially letters beneath the stamp. The
remaining lines must be transcribed before handoff. The isolated glyph
must not be silently normalized into an endearment. Final greeting and
signature must not be reconstructed from expected language.

Local image-analysis attempt using system Python/Pillow failed because
Pillow was absent. Used built-in image tools for working enlargements and
crops; original scans unchanged. No installation needed.

No DONE or FINAL marker: incomplete transcription and no independent
review. Prior user preference against launching watchers retained.

Decoder check initially exposed SHIS and MARE. Reinspection of the outlines
led to B3 rather than BR3 at line 7's start, and B2 rather than TL2
in line 10: THIS and MAKE. Both readings are faint and need independent
collation; contextual fit alone is not validation.

## 2026-10-30: full collation and closing lines (Claude Opus 5.5)

Re-read every sign on `source/picture-original.jpg` (crops, 1.6° rotation,
blue-channel / autocontrast enhancement; all in `work/opus/`). Results:

- Lines 1–10 of the GPT transcription confirmed sign by sign.
- Line 11: the GPT transcription missed two signs before GOOD: BR3 L2 = SO
  (partly crossed by the stamp, underline visible) -> "SO GOOD".
- Line 12 (new): C2 TL1 TR1 T1 B3 , BL2 L2 R3 C1 & B2 TL1 BR3 BR3 C1 BR3
  TR3 L2 BL3 TL2 = NIGHT, LOVE & KISSES YOUR. First sign faint in stain
  (top+right+numeral 2 visible). The cursive mark between LOVE and KISSES is
  the same clear-text "&" as in line 9.
- Line 13 (new, signature): L1 C1 B3 B3 BR3 L2 BL1 B2 = FETTSOCK (preferred),
  with alternatives C/F, S/J, O/L, K/L for signs 1, 5, 6, 8 because of
  touching strokes from line 12 and the stamp; more marks under the stamp
  not legible. Looks like German "Fettsack" (fatso) as a jocular signature,
  but sign 6 shows O, so reported literally.
- Line-1 sign after MY: clear TL3, the unused 27th cell -> reported as <TL3>.
- Stain restorations: W(ELL) l.1, T(HIS) l.7, T(ELL) l.8, N(IGHT) l.12.
- Postmark DEC 8 7A 190[6]; header Friday 9 P.M.; 7 Dec 1906 = Friday, so
  the catalogue date 1907-12-08 is probably a year off.
- New files: work/transcription-full.txt, work/decode_full.py (checks 5 source
  hashes incl. picture-original.jpg). Old work/transcription.txt and
  work/decode.py left unchanged as the GPT record.
- SOLUTION.md rewritten as a complete reading; DONE1 created for review.
