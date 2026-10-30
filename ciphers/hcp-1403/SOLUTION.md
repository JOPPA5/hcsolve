# HCP 1403 / pc_hcp_84 — body deciphered, closing partial

**The alphabetic body is read; the complete card remains partial because closing shortforms/strokes are unresolved. No DONE1.**

Root freshly read General, Description and Attachments on the portal: Not solved; no attached transcription or solution. Both immutable originals were inspected by this solver. The printed picture is The Ladies Tower, Elie, N.B.; no handwritten continuation was observed. The ordinary heading on the address side reads C. H. Friday. Portal date is 1908-02-07; recipient metadata remains preserved as W. Abboú. The handwritten address apparently reads Mr W. Abbott, Stokelake Farms, Chudleigh, S. Devon, but those visual context readings do not alter the original metadata.

## Cipher and key

Caesar substitution, with the written alphabet shifted forward by one. Decrypt by subtracting one, wrapping A to Z:

```
Cipher: ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain:  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

The coordinator supplied this key as a hypothesis from the related HCP1406/1407 cards. This card independently supports it across bn→AM, tp→SO, Tpssz→SORRY, dbo'u→CAN'T, xsjuf→WRITE and ojhiu→NIGHT. No external published solution, corpus match or supplied portal transcript was used.

## Body: frozen manual transcript and plaintext

| Ciphertext | Plaintext |
|---|---|
| Nz. Pxo. Efbs. | MY. OWN. DEAR. |
| J. bn. tp. Tpssz. | I. AM. SO. SORRY. |
| J. dbo'u. xsjuf. | I. CAN'T. WRITE. |
| npsf. | MORE. |
| “up-ojhiu.” | “TO-NIGHT.” |

Readable English with editorial word punctuation:

> My own dear, I am so sorry I can't write more to-night.

This is the complete main alphabetic body: 40 letters. The editorial rendering removes the writer's frequent dots; the literal table and decoder retain them. The apostrophe in dbo'u shifts to CAN'T without adding a missing letter.

Slovak translation of the body:

> Môj drahý / moja drahá, veľmi ma mrzí, že dnes večer nemôžem napísať viac.

Gender and identity are not established by the translation.

## Closing: what is and is not read

An additional Zpvs→YOUR and final Hjsm→GIRL are frozen, bringing the total to 48 alphabetic positions. They are separated by unresolved closing material:

```
[initial-like shorthand, M/N-like signs ... & L]
YOUR [faint strokes]
[short curved/tall-stroke field] GIRL
```

The initial-like field contains dots and an ampersand. It is classified as shorthand/initials, not silently discarded. Whether its letters are ordinary abbreviations or themselves shifted is undecided; possible expansions such as “many kisses and love” are not inserted. Under the body shift, a written M would give L, N would give M, and L would give K; under an ordinary-plaintext abbreviation those initials would remain unchanged.

Faint strokes after YOUR may be writing or a flourish; OWN is a contextual possibility, not frozen. Before GIRL there is a short curved sign and tall stroke whose exact alphabetic reading and expansion remain unresolved. The final word GIRL is read directly from H-j-s-m; the preceding short field is not expanded to DEAR, DARLING or a name to make the closing fluent.

## Reproduction

From the repository root:

```
python3 ciphers/hcp-1403/work/decode.py
```

The script checks immutable source hashes and decodes `work/transcription.json` using Caesar −1. It checks closing-token encipherment round trips. This is a frozen **manual** transcription of the scan, not OCR or pixel-based independent validation. It produces the full supported body and literal closing fragments, with explicit unresolved fields; it does not produce an established full-card plaintext.

No review, PDF, register entry or FINAL exists. The watcher was not launched, following the persistent user override.

## Completion and handover — Claude Opus 5.5 as solver, 2026-10-29

Status: **message complete; closing abbreviations reported literally. Handed
to review (DONE1).**

Closing (work/closing.jpg), read line by line:

```text
…hr. N. & L.  Zpvs. Px[o]      ->  … N. & L.  YOUR  OWN
El.  Hjsm                      ->  El.  GIRL
```

- `Zpvs` = YOUR and `Hjsm` = GIRL are certain. After YOUR, `Px` and a faint
  third stroke are the start of `Pxo` = **OWN**, the same word as in the
  body and in the sister cards. It is read, though faint.
- **`El.`** before GIRL is a fixed abbreviation that this couple also uses on
  HCP1386, where it appears in both the salutation (“My own El. Boy”) and the
  closing (“Your own El. Girl”). It is kept literal. Under Caesar −1 it
  would be *Dk.*, and no expansion is claimed.
- `N. & L.` (with a preceding `…hr.`) is a shorthand line, perhaps
  “[many kisses] & love” (`N` → M, `L` → K under the shift). It is kept literal.

Reading: “My own dear, I am so sorry I can't write more to-night. … N. & L.
Your own El. Girl.”

## Response to review 1 — Claude Opus 5.5 as solver, 2026-10-30

All six findings accepted after re-checking the scan (`work/message.jpg`,
reviewer crops `review/work/l1b.png`, `l4c.png`, `cl1a.png`, `cl1b.png`).
Because the salutation and one body word change, this goes back as **DONE2**.
**This section supersedes the body table, plaintext, translation, gender
statement and letter counts given above.**

1. **Salutation (major) — fixed.** At 6× the group after `Pxo.` is a cursive
   capital E with a dot, a separate tall `l` with a dot, then `Cpz` (looped C,
   p with descender, z of the same form as in `Tpssz`). There is no f/b/s; the
   earlier `Efbs` was a misreading. Line 1 is now `Nz. Pxo. {E.} {l.} Cpz.` →
   MY OWN [E. L.] BOY. The E. L. pair is kept literal, as on hcp-1386 (which
   now also reads `Nz. Pxo. E. L. Cpz.` → "My own E. L. boy").
2. **Line 4 (major) — fixed.** The word is `mfuufs` (lead-in m, long f, minims
   uu, second long f, small final s) = LETTER, not `npsf` = MORE; the same
   word appears in hcp-1386 ("thanks very much for letter").
3. **Faint word after YOUR (minor) — fixed.** Now given as **[OWN]**, a
   contextual restoration (only a faint P-like diagonal is visible), in both
   transcript and decoder output. The earlier "read, though faint" is withdrawn.
4. **HCP1386 claim (minor) — fixed.** hcp-1386 has since been completed and
   reads `E. L.` literally in salutation and closing; it is cited here as a
   parallel of the same couple, not as an expansion of E. L. No meaning of
   E. L. is claimed.
5. **First token of closing (minor) — fixed.** Transcribed as `Nz` → MY,
   marked *probable*: the sign has the same N + small z form as the first word
   of line 1, but the second stroke could be read r. It parallels "To-day. My.
   N. & L. from your…" on hcp-1386.
6. **Transcription and decoder (minor) — fixed.** `work/transcription.json`
   now holds the corrected lines; `{…}` marks literal abbreviations;
   `work/decode.py` prints them unshifted and reports counts: 41 shifted
   letters in the body, 10 in the closing (MY, YOUR, GIRL; [OWN] not counted).

### Corrected reading (round 2)

| Ciphertext | Plaintext |
|---|---|
| Nz. Pxo. E. l. Cpz. | MY. OWN. [E. L.] BOY. |
| J. bn. tp. Tpssz. | I. AM. SO. SORRY. |
| J. dbo'u. xsjuf. | I. CAN'T. WRITE. |
| mfuufs. | LETTER. |
| "up-ojhiu." | "TO-NIGHT." |
| Nz. N. & L. Zpvs. [Pxo] | MY [N. & L.] YOUR [OWN] |
| E. l. Hjsm | [E. L.] GIRL |

English: *"My own E. L. Boy, I am so sorry I can't write letter 'to-night'.
My N. & L. Your [own] E. L. Girl."*

Slovak: *„Môj vlastný E. L. chlapec, veľmi ma mrzí, že dnes večer nemôžem
napísať list. Moje N. & L. Tvoje [vlastné] E. L. dievča."*

The writer signs as the girl and addresses the recipient (Mr W. Abbott,
Chudleigh) as boy; heading "C. H. Friday" fits the portal date 1908-02-07
(a Friday; postmark WIMBORNE FE 7 08).

Remaining uncertainty: meaning of `E. L.` and `N. & L.` (literal; whether
they are plain or shifted is undecided); `Nz` at the start of the closing is
probable, not certain; [OWN] is restored, not read.

Reproduction (unchanged command, from repo root):

```
python3 -I ciphers/hcp-1403/work/decode.py
```

## Response to review 2 — Claude Opus 5.5 as solver, 2026-10-30

Verdict ACCEPT; the three minor findings are addressed as follows. No
deciphered letter changed.

1. **Superseded text at the top of this file (minor) — acknowledged.** The
   early sections (`Efbs`/DEAR, `npsf`/MORE, "40 letters", the gender
   statement, unbracketed YOUR OWN) are kept as the history of the work, as
   the README asks for a running record. They remain superseded by the
   round-2 table above. The report (`report/report.md`) and the register
   entry use only the round-2 reading.
2. **Hard-coded "Reading:" line in decode.py (minor) — fixed.** `work/decode.py`
   now assembles the final reading from `work/transcription.json` (decoded
   body lines, the closing fields with literal groups unshifted and the
   restored [OWN] marked as such) and asserts it against the expected text.
   Re-run of `python3 -I ciphers/hcp-1403/work/decode.py` prints:
   `Reading (computed): MY OWN [E. L.] BOY I AM SO SORRY I CAN'T WRITE LETTER "TO-NIGHT" / MY [N. & L.] YOUR [OWN] [E. L.] GIRL`
   followed by `Source hashes pass.` (41 + 10 shifted letters, unchanged).
3. **Notation of E. L. (minor) — fixed.** The body line in the transcript is now
   `Nz. Pxo. {E. l.} Cpz.`, i.e. one literal group, matching the closing. The
   decoder prints `[E. L.]` in both places, and the report uses only "E. L.".
   In the closing the dots after E and l are not clearly visible. That group is
   read as E. L. by its letter shapes and by analogy with line 1 and with
   hcp-1386, and the report says so.
