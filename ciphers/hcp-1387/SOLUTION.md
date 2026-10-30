# HCP 1387 / pc_hcp_68 — Caesar +1 love postcard to W. Abbott (1 Dec 1907)

**Status: complete reading of the enciphered body, with disclosed residual points (one dotted abbreviation group in row 6 is not expanded; one word reading — "Girl" — rests partly on context). Review 1: ACCEPT (four minor findings, addressed below; no cipher letter changed).**

## Source

HC Portal cryptogram 1387 (`pc_hcp_68`), read on 2026-10-26 (General, Description, Attachments): status **Not solved**, no transcription or solution attached, date 1907-12-01, recipient field "W. Abboú", language Unknown. Files and URLs: `SOURCES.md`, `source/metadata.md`. No published solution of this card was found or used (portal status, `skip.txt`, absence of attachments; the AI Decipherment Register had no record for it on 2026-10-29 per the orchestrator).

Picture side: printed "Buxton from the Town Hall" (Valentine's Series); no handwriting. Address side (read after rotating 90° counter-clockwise): plain address **Mr W. Abbott, Stokelake Farm, Chudleigh, S. Devon**; halfpenny Edward VII stamp, postmark **WIMBORNE … DE 1 07**. 1 December 1907 was a Sunday, matching the plain heading **"G. H. Sunday"**. A circled plain aside at lower left reads **"going to D."** (D. not expanded). The circular A–Z disc and building logo over both scans are a scanning overlay, not part of the card.

This card belongs to the run of W. Abbott postcards (HC Portal 1386–1398, 1401–1407) written by a correspondent signing G. H. (or C. H.) with the same Caesar key (e.g. hcp-1397, FINAL: "My dearest, this one is a Scotch view. Love from your own girl.").

## Cipher and key

Caesar substitution: each plaintext letter is written as the **next** letter of the alphabet (encryption +1, decryption −1). Case and the writer's dots are kept.

```
Cipher: ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain:  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

## Transcription and plaintext (68 cipher letters, all with the one key)

| Row | Ciphertext (manual reading) | Literal plaintext |
|---|---|---|
| 1 | Nz. Pxo. E.h Cpz. | My. Own. D.g Boy. |
| 2 | Mfuufs uijt | Letter this |
| 3 | npsjoh, | moring, |
| 4 | Uibolt wfsz. | Thanks very. |
| 5 | Nvdi gps bmm. | Much for all. |
| 6 | Nz. h.v y. Gspn | My. g.u x. From |
| 7 | Zpvs Pxo. E.h Hjsm | Your Own. D.g Girl |

Reading (English, punctuation editorial):

> G. H. Sunday. — My own D.g [guess: darling?] boy. Letter this morning. Thanks very much for all. My [g.u x — unexpanded]. From your own D.g [guess: darling?] girl. (aside: going to D.)

English sense (the expansion "darling" is a guess, see Uncertainty 4): the writer thanks her "own darling boy" for the letter that came this morning and for everything, and signs as his own darling girl.

Slovak translation:

> G. H., nedeľa. — Môj vlastný D.g [odhad: drahý?] chlapče. List [prišiel] dnes ráno. Veľmi pekne ďakujem za všetko. Môj [g.u x — nerozvinuté]. Od tvojho vlastného D.g [odhad: drahého?] dievčaťa. (poznámka: idem do D.)

## Command

From the repository root:

```sh
python3 -I ciphers/hcp-1387/work/solve.py
```

It checks the SHA-256 of `source/address.jpg`, `source/picture.jpg`, `source/metadata.md`, decrypts every row of `work/transcript_full.json` with −1, verifies the round trip, prints the 7 rows (68 letters) and the unshifted plain fields. The transcript is a manual visual reading, not OCR.

## Uncertainties

1. **Row 6 "h.v y."** — a dotted abbreviation group between "My." and "From". Glyphs read provisionally: *h* (same form as the h in E.h and in npsjoh), a looped *v*-shape, and a cursive *y* with descender. Mechanically "g.u x." (x is possibly a kiss). The second glyph could alternatively be this writer's z (→ "g.y x."), although it is larger and ends in an upstroke, unlike the flat-based z of Nz/Cpz. Not expanded; glyph identities not certain. This is the main residual.
2. **Row 7 "Hjsm" → Girl.** The capital H is certain (same form as the plain H in the heading). The following strokes (a stem with a hooked descender, no visible dot, a bowl, a short final m) also resemble the "pn" of Gspn; a literal "Hpn" would give "Gom", not a word. "Girl" is chosen because of the j-hook, the parallel with row 1 "Boy", and the sister cards' "your own girl" closing. Disclosed as a reading that relies partly on context.
3. **Row 3 "npsjoh" → "moring".** No ink for the second *o* (plain n) is visible between s and j; the writer apparently omitted it. Intended word "morning"; nothing inserted into the literal output.
4. **"E.h" → "D.g"** (rows 1 and 7) — abbreviation. If enciphered, D.g might stand for "darling" (first and last letters), but that expansion is only a guess. It is also possible that "E.h" is written in plain (initials or a pet name) and is not enciphered at all (cf. hcp-1388). Not expanded in the literal output.
5. Row 2 "uijt": the final t is this writer's uncrossed c-like t (as in Uibolt); one of the two dots near it may be a period.
6. Plain fields: initials G. H. (C. H. not excluded; cf. hcp-1397 review) and "D." in the aside are not expanded; sender identity not claimed. The postmark reads WIMBORNE 10 PM DE 1 07 (hour legible on the scan, as recorded in `work/transcript_full.json`).

## Why it is correct

- One fixed shift turns every one of the 68 cipher letters into English, with no per-word adjustments; strong long words: Uibolt→Thanks, Mfuufs→Letter, Gspn→From, Nvdi gps bmm→Much for all, wfsz→very.
- The message is a coherent love-card formula (greeting, thanks for a letter, closing) identical in style and key to the accepted sister card hcp-1397 and the other Abbott cards.
- Context agrees: postmark 1 Dec 1907 = Sunday = plain heading; addressee W. Abbott as on the sister cards.

## Credit

Earlier work in this directory (source capture, scans, rotation crops, identification of the −1 key and the 26-letter partial excerpt "My Own … Boy / very / Much for / From / Own") was done by an OpenAI GPT solver (GPT-6 Astra / GPT-6.1 Sol) on 2026-10-26. The full transcription of all seven rows (Letter this moring, Thanks, all, Your, Girl, the row-6 group), `work/transcript_full.json`, `work/solve.py` and this document are by Claude Opus 5.5 on 2026-10-29. The older `work/decode.py` / `work/transcription.json` (partial excerpt) are kept unchanged.

## Response to review 1

Verdict ACCEPT, four minor findings. No cipher letter, transcription row or key changed; `work/transcript_full.json` rows are untouched.

1. **Row 7 "Hjsm" → Girl.** Agreed; caveat kept. Re-checked on `review/work/girl.png`: the stroke after H has a bowl at the top but its descender ends in a left-curling hook (this writer's j, as in uijt), not the straight p descender of Zpvs/Gspn. Uncertainty 2 still states that the reading rests partly on context; the report repeats it.
2. **Row 6 "h.v y."** Fixed: Uncertainty 1 now names the alternative z reading of the second glyph (→ "g.y x.") next to v. The group remains unexpanded.
3. **"E.h" / "darling?"** Fixed: the bracketed expansion in the reading and both translations is now labelled "guess", and Uncertainty 4 names the alternative that "E.h" is written in plain (initials or a pet name), as left open on sister card hcp-1388.
4. **Postmark hour.** Fixed: on `source/address.jpg` the postmark reads "10 PM" above "DE 1 / 07", as in `work/transcript_full.json`; Uncertainty 6 now says so instead of calling the hour unsettled.

The reproduction command `python3 -I ciphers/hcp-1387/work/solve.py` was re-run after these edits (output unchanged: 7 rows, 68 letters, source hashes OK). Report: `report/report.md` / `report/report.pdf`. Closing steps by Claude Opus 5.5 on 2026-10-30.
