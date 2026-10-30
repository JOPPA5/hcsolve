# HCP 1393 / pc_hcp_74 — Caesar shift, complete reading

Status: **complete reading of the encrypted message; two shorthand fields kept literal.**
Handed to review as DONE1 (Claude Opus 5.5 as solver, 2026-10-29). Review 1 (2026-10-30): verdict ACCEPT, four minor
findings, all accepted; the shorthand wording below was corrected (see Response to review 1). No decoded letter changed.

## Source and context

Portal record https://crypto.hcportal.eu/dashboard/cryptograms/1393 (name `pc_hcp_74`), status
**Not solved**, no attached transcription or solution (General, Description and Attachments read by the
earlier solver on 2026-10-26; see SOURCES.md). Portal date 1907-04-29; recipient field "W. Abboú";
language "Unknown".

- Picture side (source/picture.jpg): printed colour view **"Church Parade. Southsea."**; no handwriting.
- Address side (source/address.jpg, rotated in work/address-rotated.jpg): halfpenny Edward VII stamp
  cancelled **WIMBORNE / 10 PM / AP 29 / 07** (agrees with the portal date; 29 April 1907 was a Monday,
  agreeing with the written heading "Monday"). Address: Mr W. Abbott, [farm name, probably Stokelake
  Farm as on sister hcp-1397], Chudleigh, S. Devon. The portal's "W. Abboú" is a misreading of "Abbott";
  source/metadata.md is left unchanged.
- Plain (unenciphered) heading: **G. H. Monday.**
- The circular A–Z disc visible on both scans is an overlay on the scans, not part of the card.

This card belongs to the run of cards to Mr W. Abbott, Chudleigh, 1907–08 (HC Portal 1386–1407), all
in the same Caesar shift; closed sister: hcp-1397 (FINAL).

## Cipher and key

Caesar substitution: each plaintext letter is written as the **next** letter of the alphabet
(encryption +1, decryption −1).

```
cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

The key is established on this card itself: Efbsftu→DEAREST, uifsf→THERE, mfuufs→LETTER,
gspn zpvs pxo→FROM YOUR OWN, Ivssbi→HURRAH. One shift covers every enciphered letter (73).

## Transcription and plaintext

| # | Ciphertext (manual, from the scan) | Plaintext |
|---|---|---|
| — | G. H. Monday. *(plain)* | G. H. Monday. |
| 1 | Nz. Pxo. Efbsftu. J. bn | MY. OWN. DEAREST. I. AM |
| 2 | hmbe. uifsf. jt. pof. | GLAD. THERE. IS. ONE. |
| 3 | npsf. mfuufs. gps. | MORE. LETTER. FOR. |
| 4 | nf. uijt xffl! x  M ? L *(shorthand)* | ME. THIS WEEK! x  M ? L |
| 5 | gspn. zpvs. pxo. | FROM. YOUR. OWN. |
| 6 | M[h] *(shorthand: M + raised h-like letter, unread)* "Hjsm" | M[h] "GIRL" |
| 7 | "Ivssbi" *(in a drawn cloud/oval)* | "HURRAH" |

**English (punctuation editorial):**

> G. H. Monday. My own dearest, I am glad there is one more letter for me this week! x M ? L.
> From your own M[h] "Girl". "Hurrah"

**Slovak:**

> G. H., pondelok. Môj najdrahší, som rada, že je tento týždeň pre mňa ešte jeden list! x M ? L.
> Od tvojho vlastného M[h] „dievčaťa“. „Hurá!“

(The gender of "rada"/"vlastného dievčaťa" follows GIRL.)

## Single command (from the repository root)

```bash
python3 -I ciphers/hcp-1393/work/decode2.py
```

It checks the SHA-256 of every file in source/ (work/source-sha256.json), reads the complete manual
transcription work/transcription2.json, decrypts it with Caesar −1, verifies the round trip and prints the
seven lines above (73 enciphered letters). It replays a manual transcription; it does not read pixels.
Enlarged crops used for the reading are in work/crops/ (z0…z6b, z_letter, z4right, oval).

## Uncertainties (all disclosed)

1. **Shorthand at the end of line 4, `M ? L`.** Cursive capital M (or N), a small middle sign that looks like r, & or +,
   capital L with a raised mark and an underline (work/crops/z4right.png). Kept literal and not shifted.
   The same kind of field occurs on sisters hcp-1390 ("M ××") and hcp-1403 ("N. & L."). An expansion
   such as "much love" / "[many kisses] & love" is possible but not claimed. If it were enciphered it would
   give L & K / M & K, which makes no better sense.
2. **The `x` after "week!"** is a cross written slightly below the line — read as a kiss, not a letter.
3. **Signature abbreviation `M[h]`** before "Girl": capital M with a raised tall h-like letter (h, b or k;
   it is not a u) and dots/dash below (work/crops/z6.png, review/work/m_r6b.png). Unread, kept literal,
   unexpanded; the sender is not identified. Sister hcp-1390 has a comparable closing, which after its own
   review is also recorded as "M + raised h/k/b-like letter, unread".
4. **Single letters read with some effort:** the third letter of Efbsftu is a closed loop read as b
   (o would give "DENREST"); the first letter of `jt` (line 2) has the shape of a g (closed upper loop, descender, no dot) and is
   read j **by context only** (g would give "FS", no word; IS is required by "glad there is one more letter"),
   so a writer's j/g slip is assumed; the u and i of `uifsf` (line 2) are faint, partly overlaid strokes
   (f-s-f firm; THERE is the only sensible reading and fits the length); `hmbe` (GLAD) is faint-ish but
   each letter is visible. No letter was
   restored or invented; every letter is read from the ink.
5. **Quotation marks** around "Hjsm" and "Ivssbi" are read as written (opening marks are clear; the closing
   mark of "Girl" may be the opening mark of the cloud). Their purpose is not interpreted.
6. The farm name in the address is outside the cipher and not securely read.

## Why I believe it is correct

- All 73 enciphered letters on the card decode under one fixed shift to correct, grammatical English of
  the period, with no unread enciphered group left.
- The text matches the formulae of the sister cards from the same correspondence ("My own dearest",
  "from your own … girl", the M/N & L-type and M + raised letter shorthand).
- The written "Monday" agrees with the postmark date 29 April 1907 (a Monday) and the portal date.

## Credit and provenance

Source capture, the Caesar −1 identification and a partial reading (salutation, "there is", "more …
for", "me … week", "from your own", and the tentative "Ivssbi → Hurrah") were made on 2026-10-26 by the
earlier OpenAI GPT solver (work/decode.py, work/transcription.json, kept as history). Claude Opus 5.5
re-read the whole card from the pixels on 2026-10-29, resolved line 2 (`hmbe. uifsf. jt. pof.` →
GLAD THERE IS ONE), corrected `mfuufst` → `mfuufs` (LETTER; there is no t), read the end of line 4,
line 6 and the oval, and wrote work/transcription2.json and work/decode2.py. No published solution of
this card was found or used (portal status Not solved, no attached solution).

## Response to review 1

Review 1 (Claude Opus 5.5, 2026-10-30) gave verdict **ACCEPT** with four minor findings. I re-checked each
on the review's crops (review/work/m_r6b.png, m_r4r.png, m_r2mid.png) and accept all four. None changes a
decoded letter; the reproduction command was re-run after the changes and still prints the same seven lines
and 73 decoded letters (the shorthand fields now print as `M ? L` and `M[h]`).

1. **Signature abbreviation — fixed.** On m_r6b.png the raised sign after M has a tall ascender and a
   short arch: an h (or b/k), not a u. The field is now "M + raised h-like letter, unread", written `M[h]`
   in the table, translations, work/transcription2.json and the report. The stale citation of a "Mu. Hjsm"
   closing on hcp-1390 and the "Lᵗ (little)" aside are removed; hcp-1390 itself now records its comparable
   field as unread.
2. **`jt` — disclosed more plainly.** Agreed: the sign is g-shaped (closed loop, descender, no dot).
   Uncertainty 4 and the report now say the letter is read as j by context only.
3. **`uifsf` — disclosed.** Agreed: the u and i are faint and partly overlaid; f-s-f is firm. Added to
   uncertainty 4 and to the transcription notes.
4. **`M ? L` — fixed.** On m_r4r.png the middle sign looks like a small r (could be & or +). The field is now
   written `M ? L` with that description instead of asserting "&".
