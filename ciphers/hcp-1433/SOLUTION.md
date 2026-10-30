# HCP 1433 / pc_hcp_114 — Morse code postcard, 2 Aug 1907

Complete reading of all Morse on the card (39 letters), with the residual
points listed below. Handed to review as DONE1.

**Credit.** The portal capture (all three tabs, both scans, hashes), the
180-degree orientation, and the reading of the first four main rows
(SHALL / ISEEYOU / TOMORRO / WEVE) and the bottom passage (FONDEST / LOVE)
were done by the earlier OpenAI GPT solver on 2026-10-26. That solver left
the fifth main row unresolved (provisional LOMEE / AIOMEE, then withdrawn).
On 2026-10-29 Claude Opus 5.5 re-checked every row on enlarged crops and a
colour screen of `source/address.jpg`, read the fifth row as LOUIE, and
wrote the full transcript and decoder.

Context: portal status Not solved, tag "Morse code", no attached
transcription or solution; dated 1907-08-02, addressed to G. Groves,
Banbury. The picture side (Northborough Church) carries no cipher. No
published solution of this card was found.

## Cipher and key

- **Type:** International Morse code written in pen dots and dashes, each
  letter closed by a long slanted stroke (`/`). No word spaces are marked.
- **Key:** the standard International Morse alphabet A–Z (only letters
  occur). No numerals or punctuation.
- **Orientation:** the message half is upside down relative to the address;
  rotate `source/address.jpg` 180 degrees. The Morse sits in five rows on
  the right half amid ordinary cursive, plus two rows at the bottom.

## Transcript (`work/transcription-full.txt`)

```
... / .... / .- / .-.. / .-..             SHALL
.. / ... / . / . / -.-- / --- / ..-       ISEEYOU
- / --- / -- / --- / .-. / .-. / ---      TOMORRO
.-- / . / ...- / .                        WEVE
.-.. / --- / ..- / .. / .                 LOUIE
..-. / --- / -. / -.. / . / ... / -       FONDEST
.-.. / --- / ...- / .                     LOVE
```

## Plaintext (English)

> SHALL I SEE YOU TOMORROW EVE[NING?] LOUIE
>
> FONDEST LOVE

Word division and punctuation are editorial: "Shall I see you tomorrow
eve, Louie? … Fondest love." "Eve" is the usual period abbreviation of
"evening". LOUIE reads as a name: the addressee's pet name or the writer's
signature for the Morse part. Which of the two is not decided by the text.

- **English:** Shall I see you tomorrow evening, Louie? … Fondest love.
- **Slovak:** Uvidím ťa zajtra večer, Louie? … S najvrúcnejšou láskou.

## Command (run from the repo root)

```sh
python3 -I ciphers/hcp-1433/work/decode_full.py
```

It checks the SHA-256 hashes of `source/` (`work/source-sha256.json`),
decodes `work/transcription-full.txt` with the A–Z Morse table, and
prints the seven rows, the count (39) and the joined main and bottom
passages. The dots and dashes were transcribed by eye from the scan; the
script does not recognise ink.

## Uncertainties

1. **Row 5, first group (L).** A separator stroke from row 4 (after W,
   about x=600 in the rotated scan) ends between `.-` and `..` of row 5.
   It starts at row-4 height (y≈373) and has the slope of the other row-4
   separators, but it is longer (about 67 px against about 46 px for the
   E|V separator) and reaches down into row 5. This writer sometimes lets
   one long stroke serve as separator for two rows (row 1 L|L also closes
   `---` in row 2; the F|O stroke of FONDEST continues as the L|O stroke
   of LOVE), so stroke geometry alone does not exclude a row-5 split.
   L (`.-..`) is chosen on language: the split reading A I O U I E is not
   English. (Revised after review 1, finding 1.)
2. **Row 5, O.** The third dash of `---` (about x=692–703, y≈445) sits just
   above the upside-down red printed text "(Post Office Regulation.)". On a
   colour screen it is dark grey pen ink like the other marks, not red
   print. So O is read, not M. This corrects the earlier provisional "M".
3. **Row 5, U / I / E.** Next come dot, dot, dash (U), then a separator. On
   that separator there is a small ink thickening about 12 px above the row
   line (x≈790, y≈444). It is read as a pen hook on the stroke, and similar
   hooks occur on other separators. If it were a dot, the next letter would
   be S instead of I (LOUSE), or, if it belonged before the stroke, U
   would become F (`..-.`, LOFIE). Both fit the context worse; LOFIE is not
   a word. (LOFIE added after review 1, finding 2.) The second dot
   of I (x≈825) is small and touches the lighter next separator, but it
   stands left of it. The final E is a clear single dot before the last
   stroke, which is followed directly by cursive.
4. **Row 1, H.** One dot of H is lengthened where a cursive descender from
   the line above crosses it. It is read as a dot (4 dots = H).
5. **Row 3.** One dash of an O is short. The group still has three dashes.
6. The cursive text (a note thanking "A. G." for a letter and a picture
   postcard, and talking about someone being back safely) is context only.
   It is not transcribed in full and was not used to choose any Morse
   letter.

## Why I believe it is correct

- Every pen mark in the Morse area belongs to one of the 39 groups, and
  every group is a valid International Morse letter. No sign is left over.
- The decoded text is plain, natural Edwardian English. It fits a
  1907 personal postcard: an evening meeting arranged for the next day,
  ending in a name and "fondest love".
- The two passages were read independently, and both make sense without
  forcing.

## Response to review 1

Review 1 (Claude Opus 5.5, 2026-10-30) gave the verdict ACCEPT, with the
same 39 letters read independently. The reproduction command was re-run
after the changes below and still prints SHALL / ISEEYOU / TOMORRO / WEVE /
LOUIE / FONDEST / LOVE, 39 letters, source hashes OK. No letter changed.

1. **Row-5 L argument (minor) – fixed.** Agreed: the stroke ending between
   `.-` and `..` is longer (about 67 px) than the E|V separator of row 4
   (about 46 px), and the writer does share long separators between rows
   elsewhere (row 1 / row 2; FONDEST / LOVE). Uncertainty 1 now says that
   the geometry alone allows A / I and that L is chosen because AIOUIE is
   not language.
2. **Blob at x≈790 (minor) – fixed.** LOFIE (dot before the stroke, U → F)
   is now listed in uncertainty 3 beside LOUSE as a rejected alternative.
   The blob is still read as a pen hook.
3. **LOUIE as addressee or signature (minor) – agreed, no change needed.**
   SOLUTION.md already leaves this open; the report does the same.
4. **Rough coordinates in `work/final-row-observations.json` (minor) –
   agreed.** That file is the earlier provisional GPT map and is not used by
   the decoder. The current transcript (`work/transcription-full.txt`,
   with U = `..-`) is authoritative, and the report relies only on it.
