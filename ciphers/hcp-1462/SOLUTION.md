# HCP 1462 / pc_hcp_143 — solution (round 1)

Portal: https://crypto.hcportal.eu/dashboard/cryptograms/1462 — status "Not solved"
when captured (2026-10-26); no transcription or solution attached; no published
solution of this card found. Picture side: "Prittlewell Church" (Southend-on-Sea,
Essex). Address side: R. E. Holmes Esq, 12 Bedford Rd, West Green Rd, Tottenham.
Edward VII ½d stamp (so c. 1902–1910); date not legible.

## Cipher type and key

Line-by-line **route transposition** (no substitution). For every physical line
the writer put the plaintext's odd-position letters first, then the
even-position letters in reverse order (`cipher = p[0::2] + p[1::2][::-1]`). To
decipher, read leftmost, rightmost, second, second-from-right, … inward. The route
restarts on each written line. Same scheme as sister card hcp-1460 ("Dear Sadie").
Word spaces in the cipher are not meaningful; "P.S." is written in clear.

## Transcription (own, from source/address-large.jpg) and plaintext

| # | Cipher (work/transcription.txt) | Decrypted |
|---|---|---|
| 1 | DaRlhpare | Dear Ralph |
| 2 | Tiitehrhcuchssh | This is the church |
| 3 | Imonttishogiga | I am going to this |
| 4 | eeignnv | evening. |
| 5 | Peswieonostreal | Please write soon. |
| 6 | Iiloooorwormtsdlw | I will do so tomorrow. |
| 7 | YsaiedSr | Yrs Sadie |
| 8 | P.S. WntEswodotaote | P.S. Went to Eastwood |
| 9 | timrignnosh | this morning. |

All 9 cipher lines, 110 letters, decrypt with the one rule; nothing left over.

**English (original language):** "Dear Ralph, This is the church I am going to this
evening. Please write soon. I will do so tomorrow. Yrs Sadie. P.S. Went to Eastwood
this morning."

**Slovak:** „Milý Ralph, toto je kostol, do ktorého idem dnes večer. Prosím, napíš
čoskoro. Ja tak urobím zajtra. Tvoja Sadie. P.S. Dnes ráno som bola v Eastwoode.“

## Reproduce (one command, from repo root)

```sh
python3 ciphers/hcp-1462/work/decode-full.py
```

It checks the SHA-256 of every file in source/ against work/source-sha256.json,
decrypts each line of work/transcription.txt, re-encrypts to confirm the
round trip, and prints the 9 plaintext lines (110 letters).

## Uncertainties (all letters read from pixels; points below are disclosed)

1. **L1** `DaRlhpare`: 4th sign `l` is a short loop (could be taken for `e`);
   the last letters `are` are faint, partly under the printed wheel letter W.
2. **L2** `Tiitehrhcuchssh`: (a) first sign is a cursive capital **T** (loop +
   descending stem); it is clearly unlike the signature's `Y`, which earlier work
   had read here. (b) 9th sign read **c** (this hand's c has a curled top, so it
   resembles e; it also sits on the dark printed band). (c) 10th sign is a heavy,
   apparently retraced **u** that earlier work read as `uu`; read as one letter.
3. **L3** 12th sign `i`: its stroke merges with a printed arc; its dot sits
   offset to the right. Earlier work left it as i/l.
4. **L4** 5th sign read `n` (two humps), not m.
5. **L5** last sign is `l`: the "cross-stroke" under it, which earlier work saw as
   a possible f, belongs to the printed symbol row of the wheel.
6. **L6** the 4th `o` of the run `oooo` (7th letter) lies on the large printed
   ring letter **S**; pixels show a darker pencil loop over the S's lower bowl
   (≈170–185 grey vs ≈195–205 for print alone), read as `o`. This is the weakest
   reading on the card; it is the only letter that fits ("tomorrow"). A stray dot
   after the first `o` is ignored. The 10th sign is `o` (could look like a),
   written over a printed wheel symbol.
7. **L8** 4th sign read as cursive capital **E** (large upper loop + small lower
   bowl; could be taken for b). 11th sign read as one `a` whose closing stroke is
   dark; it could be mistaken for `a`+`o`.
8. **L9** 8th sign read **n** (two humps, same as the 7th); earlier work read it
   as `m` and got the literal "morming". With n the line is "this morning".
9. **Not ciphertext, not fully read:** (a) a faint plain-English pencil note in the
   picture-side bottom margin, legible only as "I hope you will …" with a closing
   word that may be "Sadie"; the middle is too faint in this scan. (b) A pencil
   mark "Bssn"/"Bran"(?) top left of the address side, above POST CARD — likely
   not part of the message (possibly a later annotation); uninterpreted.
10. People: "Sadie" and "Ralph" (= R. E. Holmes) are not identified further.

## Why this is correct

- One fixed, simple rule turns all 110 cipher letters on the card into fluent,
  period-appropriate English with no leftover or rearranged letters.
- Context fits closely: the picture is Prittlewell Church ("This is the church I
  am going to this evening"), and **Eastwood** is the neighbouring parish of
  Prittlewell in Southend-on-Sea, Essex.
- The scheme and the writer's name match sister card hcp-1460 ("Dear Sadie …"),
  apparently the other side of the same correspondence.

## Credit

Earlier work (OpenAI GPT solver, 2026-10-26): portal capture, source download,
route identification, and readings of lines 1, 4, 5 (with l/f open), 3 (with i/l
open), 7 (provisional) and 9 (as "morming"). Completed by Claude Opus 5.5 on
2026-10-30: re-read every line on enlarged crops, newly read lines 2, 6 and 8
(PS "Went to Eastwood"), resolved L3 i, L5 l and L9 n, wrote work/transcription.txt
and work/decode-full.py. The old partial scripts (decode.py, decode-follow.py)
are superseded but kept.

## Response to review 1

Review 1 (Claude Opus 5.5, verdict ACCEPT) had four minor findings. None of them
changes a decrypted letter. The reproduction command was re-run after this
response (`python3 -I ciphers/hcp-1462/work/decode-full.py`): source hashes OK,
9 lines, 110 letters, output unchanged.

1. **L9 8th sign n vs m — agreed, wording corrected.** I re-checked
   review/work/l9n.png at 8x. The 8th sign is narrower and more cramped than the
   7th and has a small extra stroke; a literal `m` (the earlier "morming")
   cannot be excluded from the pixels. Uncertainty 8 above overstated it ("same
   as the 7th"). Corrected reading: **n is preferred on sense; m is possible as a
   slip of the pen.** The line reads "this morning" either way; the transcription
   keeps `n`.
2. **"Printed wheel" is the HCPortal watermark — agreed.** The same large
   alphabet ring (…W X Y Z A B C D E…) with the building-and-padlock emblem lies
   across source/picture-large.jpg as well, over the photograph of the church.
   It is the portal's overlay on both scans, not something printed on or used
   with the card. Wherever uncertainties 1, 2, 3, 5 and 6 above say "printed
   wheel", "printed band", "printed arc", "printed symbol row" or "printed ring
   letter S", read "HCPortal watermark". The point of each uncertainty (a pencil
   letter partly overlaid by grey watermark ink) is unchanged, and the writer did
   not use a cipher wheel; the route rule needs none.
3. **Picture-side note — tentative fuller reading added.** On a 2x/4x
   autocontrast crop (work/pic-note-2x.png) the bottom-margin pencil line reads
   tentatively "I hope you will u[nderstand?] … message. Sadie": "I hope you
   will" is clear, the next word starts with u/w and runs under the watermark
   ring, a short word follows, then "messag[e]" and a closing "Sadie". It is plain
   English, not ciphertext, and plausibly refers to the ciphered message on the
   address side.
4. **Link to hcp-1460 — wording softened.** hcp-1460 (to Miss Ovington, South
   Tottenham, 1905, opening "Dear Sadie", signed by another writer) uses the same
   route transposition and also goes to a Tottenham address. That the two cards
   come from one circle of correspondents, possibly Sadie and Ralph, is an
   **inference**, not established; "apparently the other side of the same
   correspondence" above should be read with that qualification.

Not changed: the transcription, the key and the plaintext. Status: complete
(all 110 cipher letters read), with the disclosed weak points L6 (pencil o over
the watermark S) and L9 (n/m).
