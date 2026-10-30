# HCP 1436 / pc_hcp_117: International Morse love note (Singapore, 27 May 1912)

Status: full reading; review 1 verdict ACCEPT (minor findings addressed below). Earlier work: an OpenAI GPT
solver (GPT-6 Astra / GPT-6.1 Sol) found the orientation, the cipher and a
98-letter excerpt reading (`work/transcript.json`, `work/decode.py`).
Claude Opus 5.5 re-read every group on enlarged crops on 2026-10-29/30 and
completed the transcription (`work/full-transcript.json`). The portal attaches
no transcription or solution, and no published solution was found. The
portal status is "Not solved".

## Cipher and key

Plain **International (Continental) Morse code**, written in pen as dots and
dashes. It is not a substitution layered on top of Morse. Short upright
strokes separate letters and double strokes separate words. To read it, rotate
`source/address.jpg` by 270 degrees (see `work/upright.jpg` and
`work/code-reversed-large.jpg`). The text runs left to right, top to bottom,
in 10 rows. The key is the standard A–Z Morse table in `work/decode_full.py`.
The two loop rows along the card edge are an ornamental border, not Morse.

## Plaintext (English, original)

> MY OWN DARLING GIRLIE, WOULD YOU LIKE A NICE LONG WALK ROUND THIS — PART?
> HOW I SHOULD LOVE TO TAKE YOU, DARLING. EVER [blot] EVER YOUR OWN, OMAR

Punctuation is editorial. "— " stands for the long stroke described below.

Translation (Slovak): „Moje vlastné drahé dievčatko, chcela by si sa pekne
dlho prejsť po tomto kúte? Ako rád by som ťa vzal, drahá. Navždy [a] navždy
tvoj vlastný, Omar.“

(English is the original language. A modern paraphrase: "My own darling
girl, would you like a nice long walk round this part? How I should love to
take you, darling. Ever [and] ever your own, Omar.")

The address side reads: M. C. Hutton, 94 Gunterstone Rd, West Kensington,
London W., England. It is postmarked Singapore, 27 May 1912. The picture side
shows "Botanical Garden, Singapore", which fits the invitation to a walk.

## Reproduce (one command, from the repo root)

```
python3 -I ciphers/hcp-1436/work/decode_full.py
```

The command checks the SHA-256 of both scans and of `metadata.md`
(`work/source-sha256.json`). It then decodes the full dot/dash transcription
and prints:

```
MY OWN DARLING GIRLIE WoULD YOu LIKE A NICE LOng WALK ROUND THIS [LONGSTROKE] PART HOW I sHOULD LOVE TO TAKE YOU DARLING EVER [BLOT] EVER YOUR OWN OMAR
105 letters decoded (5 disclosed restorations/judgments shown in lower case); source hashes OK.
```

## Uncertainties (all disclosed; the lower-case letters in the output)

1. **wOuld (restoration).** An ink blot covers the first two marks of the
   group between W and ULD. Its last dash is visible, and the blot is about
   two dash-lengths wide. Only O (`---`) gives a word.
2. **yoU (line 3).** The first mark of the U group is 24 px wide with a
   notch, which I read as two touching dots (`..-`). The other two U's on
   the card (line 7 YOU, line 9 YOUR) are clean `..-`.
3. **loNG.** After `---` the row shows a clean dash, then a grey smudge
   about 1.5 dashes wide crossed by a letter divider, then a clean dash and
   a dot. The reading `-. | --.` places **two** marks inside the smudge: the
   dot of N and the first dash of G. Both N and G are therefore judgments
   (lower case in the output). LONG is the only word that fits.
4. **Should vs RHOULD.** The first group is dot / 24 px mark / dot. In this
   word the dots measure 11–17 px and the dashes 27–36 px, so the central mark
   falls between the two sizes. Read as a dot it gives S (SHOULD). Read as a
   short dash it gives R, and the earlier GPT pass froze the literal RHOULD.
   I read S. A reviewer may prefer to report it as "RHOULD [sic, = SHOULD]".
   The meaning does not change.
5. **Long stroke before PART** (start of line 6). It is a heavy horizontal
   stroke about 4 dash-lengths long, set between word dividers. No Morse
   letter has that form. I take it as punctuation or a cancellation and do
   not decode it. Read literally as a single dash it would be a stray T.
6. **Blot between EVER and EVER.** It is a looped ink blot set between word
   dividers. It may be a hand-drawn "&" or a cancelled AND, but it is not
   restored: "ever [and] ever" is only interpretation.
7. **PART is literal.** The final group is a single dash = T. PARK
   (`-.-`) would fit the garden picture better, but it is not on the card,
   and "round this part" is acceptable English.
8. **OWN.** A full-height divider stroke crosses between the two dashes of
   W. Taken literally it would give O-A-T-N, so I treat it as a stray stroke.
9. **Signature OMAR** (`--- / -- / .- / .-.`), read literally from clear
   groups. The first dash is long but shows no gap. The signature is
   tightly spaced: the dot of A sits on (touches) the divider to its right.
   "Omar" may be a pet name or nickname rather than the writer's given
   name; who the sender was is not established.

## Why I believe it is correct

- One standard alphabet, applied without any word-specific substitutions,
  turns all ten rows into fluent Edwardian English with a coherent
  salutation, body and sign-off. 105 letters are read, and 100 of them
  directly from clean marks.
- The content (an invitation to a walk, "ever ever your own") fits a
  1912 postcard sent from Singapore to a young woman in London, with the
  Botanical Garden picture on the other side.
- Every row of Morse on the card is covered. The residual points above are
  local, and none of them affects the sense.

## Files

- `work/full-transcript.json`: the full dot/dash transcription, with notes.
- `work/decode_full.py`: the one-command decoder and hash check.
- `work/c2/`: enlarged crops used for this pass (rows `r*.png`, zooms `z_*.png`).
- `work/transcript.json`, `work/decode.py`, `work/scan-audit.md`: earlier
  GPT excerpt pass, kept for the record.

## Response to review 1

Review 1 (Claude Opus 5.5) verdict **ACCEPT**, three minor findings. The
reviewer's independent transcription and decoder matched this reading letter
for letter (105 letters, same word division, same two non-Morse marks).

1. **LONG: two marks in the smudge (minor) - fixed.** Agreed. On
   `review/work/z_long.png` (and `work/c2/z_long.png`) the row-4 group after
   `---` is dash, smudge crossed by a divider, dash, dot; the smudge has to
   hold both the dot of N and the first dash of G. The G token in
   `work/full-transcript.json` is now flagged `!` like the N, the note
   `line4_N` describes both inferred marks, and uncertainty item 3 says so.
   Re-running `python3 -I ciphers/hcp-1436/work/decode_full.py` now prints
   `... A NICE LOng WALK ...` and `105 letters decoded (5 disclosed
   restorations/judgments shown in lower case); source hashes OK.` The count
   of letters read directly from clean marks is corrected from 101 to 100.
   The reading itself is unchanged.
2. **OMAR spacing and pet name (minor) - fixed.** Uncertainty item 9 now
   states that the dot of A touches the divider on its right and that
   "Omar" may be a pet name rather than a given name. Reading unchanged.
3. **Presentation of the long stroke (minor) - addressed.** The report
   states explicitly that the long stroke has no letter value and is not a
   T; in the plaintext it is shown as a dash of punctuation only. The
   run-together words in the first NOTES.md entries (2026-10-26, earlier
   GPT pass) are left as written, since NOTES.md is a historical log; their
   content is summarised correctly in the later entries.

No letter of the reading changed; only the disclosure of one letter (G in
LONG) was tightened. The solution is closed with FINAL.
