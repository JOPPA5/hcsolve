# HCP 1392 / pc_hcp_73 — Caesar −1 (letter after), English love postcard, 9 May 1907

**Status: complete reading of the enciphered body (57 letters); review 1 verdict REVISE, findings addressed (see Response to review 1).**
Two closing initial groups ("N & L!" and "N^b") are reported literally, as on the sister cards;
some readings are flagged as less secure (see Uncertainties).

## Source and context

https://crypto.hcportal.eu/dashboard/cryptograms/1392 — portal status *Not solved*, no
transcription or solution attached (read 2026-10-26, see SOURCES.md). Picture side:
printed view "Connaught Park and Dover Castle", no handwriting. Address side
(source/address.jpg): halfpenny Edward VII stamp, postmark `[WI]MBORNE 10 PM MY 9 07`;
address in plain writing **Mr W. Abbott, Stokelake Farm, Chudleigh, Devon** (the earlier
note "…, Dover" was wrong — Dover is only the picture); plain heading **"G. H. Thursday."**;
plain date in the left margin **"May 9th 07"** (9 May 1907 was a Thursday; agrees with
portal date 1907-05-09 and postmark). The card belongs to the Abbott correspondence
hcp-1386…1407 (same addressee, same Caesar key, same formulas "My own dearest … from your
own … girl", cf. hcp-1390, hcp-1397). No published solution of this card was found or used.

## Cipher and key

Monoalphabetic Caesar shift: each plaintext letter is written as the **next** letter of
the alphabet (encrypt +1, decrypt −1). Dots and the dash are written in clear.

```
Cipher: ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain:  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

## Transcription and plaintext (address side, rotated 90° CCW)

| Ciphertext (manual reading) | Plaintext |
|---|---|
| *(plain)* G. H. Thursday. | G. H. Thursday. |
| Nz Pxo. Efbsftu | My Own. Dearest |
| Tfoejoh. b. dbse | Sending. a. card |
| up. Z— jotufbe | to. Y— instead |
| pg. mfuufs. N & L! | of. letter. [N & L!, initial group, literal] |
| Gspn. zpvs pxo N^b: | From. your own [N^b: abbreviation, literal] |
| Hjsm | Girl |
| *(plain, margin)* May 9th 07 | May 9th 07 |

57 alphabetic cipher letters in the enciphered body; one key covers all of them, round trip verified.
The two initial groups are kept literal and not shifted.

**English:** "G. H. Thursday. My own dearest, sending a card to Y— instead of a letter.
[N & L!] From your own [N^b, undecoded abbreviation] girl. May 9th '07."

**Slovak:** „G. H. Štvrtok. Môj najdrahší, posielam Y— pohľadnicu namiesto listu.
[N & L!] Od tvojho vlastného [N^b, undecoded abbreviation] dievčaťa. 9. mája 1907.“

## Single command (from the repository root)

```
python3 -I ciphers/hcp-1392/work/decode_full.py
```

Verifies SHA-256 of both source images, decrypts `work/transcript_full.json` line by
line, checks the inverse key re-encrypts every line exactly, prints 57 letters decoded,
the two literal groups and the plain fields. The transcript is a manual visual reading
(not OCR); enlarged crops supporting it are in `work/crops/`.

## Uncertainties

1. **Closing abbreviation** after "pxo": a capital N (cursive, arched lead-in) followed by
   a small raised b/h-like letter with two dots beneath — the same abbreviation the
   reviewer of hcp-1390 described there ("M + raised h/k/b-like letter"). Whether it is
   enciphered (N^b → M^a) or a plain initial is undecidable; it is reported literally and
   not expanded (`work/crops/l6-abbrev-10x.png`). A raised letter with a mark beneath is the
   usual form of a superscript abbreviation such as "Nᵒ" ("your own No. … girl"?); sister
   card hcp-1407 has "N.-1" in this same slot and hcp-1393 "Mᵘ.". Listed as alternatives only.
2. **"N & L!"** (end of line 4, paler ink). Read after review 1 as the writer's capital N
   (long rising lead-in, down-stroke, arched second hump, as the N of "Nz" and of the closing
   "N^b"), a short dash, a small reversed-c ampersand, a tall pale capital L with a dark foot,
   and "!". The same closing group stands in the same slot on sister cards hcp-1393, 1395
   ("M. & L."), 1403 ("N. & L.") and 1407 ("M. & L.'"). N vs M is not fully excluded. Kept
   literal; if enciphered it would give "M & K" (perhaps "[many kisses] & love"-type shorthand),
   not claimed. The earlier reading "Ib-Ib!" = "Ha-Ha!" is withdrawn
   (`review/work/compare_N.png`, `review/work/R4t.png`).
3. **"Efbsftu"** (line 1): E, f, b, s are dark; the final "ftu" is pale and crossed by the
   portal watermark ring, but an f-descender with t-crossbar and a u are visible
   (`work/crops/l2-efbsftu-red8x.png`). Same salutation as hcp-1386/1390.
4. **"Z—"**: a single cipher letter Z (= Y) followed by a long dash, i.e. an abbreviation
   "Y—" (perhaps "you", perhaps a name); not expanded.
5. Large initials: the capital T of "Tfoejoh" is joined to the following f (its stem is
   the f descender); the capital G of "Gspn" has the Y-like form with a tail turning back
   at the baseline, as this writer's G on hcp-1397. In both cases only that letter gives a
   word (SENDING, FROM). A small dot above "pxo" in line 5 is taken as a stray mark.
6. Heading initials "G. H." (possibly C. H. as read on sister cards) and the date are plain
   and not shifted; no sender identity is claimed. Postmark office is partly covered.

## Why it is correct

Every word of the enciphered body (57 letters) decodes with one fixed shift to grammatical
1907 English that fits the card; two short initial groups ("N & L!", "N^b") are kept literal,
as on the sister cards of the same writer:
a lover sends a picture card instead of a letter, with the family's standard salutation and
closing. Date in cipher context (Thursday, May 9th 07) agrees with postmark and portal.

## Credit

Earlier work (2026-10-26) by the OpenAI GPT solver: key identification and a partial
reading (My Own Dear / ?ending a card / to Y— instead / of letter / ?rom your own M…),
work/decode.py and work/transcript.json (kept unchanged). Completed by Claude Opus 5.5 on
2026-10-29: full re-reading from the pixels, "Dearest", "Girl", the initials T
and G, corrected address (Chudleigh, Devon), new transcript and decoder.

## Response to review 1

Verdict REVISE (reviewer: Claude Opus 5.5, 2026-10-30). All three findings accepted and fixed.

1. **(major) "Ib-Ib!" = "Ha-Ha!" is a misreading — accepted, fixed.** I re-examined the reviewer's
   `review/work/compare_N.png` and `review/work/R4t.png` and the sister crop
   `ciphers/hcp-1393/work/crops/l4c.png`. The first sign of the tail has exactly the construction
   of this writer's capital N (long rising lead-in, down-stroke, arched hump), as in "Nz" and the
   closing N^b; it is followed by a short dash, a reversed-c ampersand, and a tall pale L, then
   "!". The "Ib-Ib" reading needed two unlike shapes both to be I and is withdrawn, together with
   the "teasing" interpretation. Changes: `work/transcript_full.json` (line 4 now `pg. mfuufs.`,
   new field `literal_groups` with `N & L!`), `work/decode_full.py` (prints both literal groups),
   the transcription table, translations, Uncertainty 2, letter count 61 → 57. Re-ran
   `python3 -I ciphers/hcp-1392/work/decode_full.py`: source hashes OK, 6 lines, 57 letters,
   round trip asserts pass, output as in the table above.
2. **(minor) "No." possibility and sister parallels for N^b — added** to Uncertainty 1 (and to the
   `before_Hjsm` note in the transcript) as alternatives, not expanded.
3. **(minor) "Why it is correct" overstated — fixed:** now says that the enciphered body decodes
   completely and two initial groups are kept literal.

The reading of the enciphered body is unchanged apart from the removal of the misread group.
