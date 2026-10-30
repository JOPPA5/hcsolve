# HCP 1352 (pc_hcp_33): an English love note in Caesar cipher, signed "Loo", 1 February 1907

Human solver: Tomáš Pavuk

**Status: deciphered in full (97 of 97 enciphered letters, one key); independent review 1 verdict ACCEPT, plaintext unchanged.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1352 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1352), portal name pc_hcp_33, part of the HCPortal collection of cryptographic postcards. When it was captured on 2026-10-30 the portal listed it as **Not solved**, tagged Postcard, HCPortal collection, category Substitution, date 1907-02-01, language Unknown, location Europe, sender Unknown, recipient "W. Abboú" (a catalogue spelling of Abbott), with no transcription or solution attached.

The picture side is a printed view, "Ludlow Castle" (Valentine's Series), with no handwriting. Everything written is on the address side. It carries a halfpenny Edward VII stamp and the postmark WIMBORNE 10 PM FE 1 07, and is addressed to **Mr W. Abbott, Stokelake Farm, Chudleigh, Devon**. Turned 90° counter-clockwise, the left half of that side holds a plain heading, "G. H. Friday", and six rows of cipher. 1 February 1907 was a Friday, so the heading agrees with the postmark. The grey wheel over the card is the portal's watermark, not part of the card.

The recipient and the cipher match a group of Caesar cards to W. Abbott deciphered in this repository (HCP 1386–1407, dated 1907–08, and others with the same address). No published solution of this card was found.

![Address side as delivered (source/address-large.jpg)](../source/address-large.jpg)

![Message turned 90° counter-clockwise, from the high-resolution original (work/crops/whole-rot.jpg)](../work/crops/whole-rot.jpg)

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

## Method

The transcription is **manual**, read sign by sign from enlarged crops of the un-converted original scan (no OCR). The shift was not recovered on this card: it was taken from the sister cards and tested. It worked at once, since groups such as `Ibwf nbef`, `njtublft`, `xjui pvs` and `Nz mpwf` are English words moved one letter forward. All transcription and decipherment on this card are by Claude Opus 5.5; there is no earlier work on this number.

The script `work/decode.py` checks the image hashes, reads the transcription, decrypts every word, verifies the round trip and lists every place where the sign as seen differs from the form the key is applied to. In review a separate Claude Opus 5.5 agent re-read all six rows on its own enlargements, decrypted with its own script and got the same 97 letters.

## Key

Caesar shift: each plaintext letter is written as the **next** letter of the alphabet. To decrypt, subtract one.

```text
Cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

The heading is ordinary writing and is not shifted. Nothing else on the card is left in clear.

## Plaintext and translation

"As seen" gives the sign shapes; an arrow gives the form the key is applied to, wherever the two differ.

| Row | As seen | Plaintext |
|---|---|---|
| 1 | Ualf. (→ Ublf) dasf. (→ dbsf) J. Ibwf. nbef. | TAKE. CARE. I. HAVE. MADE. |
| 2 | op. njtublft. J. bn. wfsz | NO. MISTAKES. I. AM. VERY |
| 3 | nvdg. (→ nvdi) bnvtfe. xjui pvs | MUCH. AMUSED. WITH OUR |
| 4 | ofx? (→ ofx; see 3 below) qmbo. Nz. mpwf. | NEW. PLAN. MY. LOVE. |
| 5 | po. a. (→ b) Qptu. dase. (→ dbse) Ipx. | ON. A. POST. CARD. HOW. |
| 6 | ojdf. uift. (→ uijt) gt. (→ jt) Tfdsfu. M.p.p. | NICE. THIS. IS. SECRET. L.O.O. |

**English** (the original language; punctuation editorial): "G. H. Friday. Take care. I have made no mistakes. I am very much amused with our new plan. My love on a post card. How nice this is. Secret. Loo."

**Slovak:** „G. H. Piatok. Dávaj pozor. Neurobila som žiadne chyby. Veľmi ma baví náš nový plán. Moja láska na pohľadnici. Aké je to milé. Tajné. Loo."

The feminine forms in Slovak follow the sister cards, which are signed by a girl; this card does not state the writer's sex.

To reproduce, from the repository root: `python3 -I ciphers/hcp-1352/work/decode.py`

## Uncertainties

The writer's cipher is not perfectly clean on this card. 89 of the 97 letters decode from the sign as labelled, and 8 signs in 8 words are normalised. Even the 89 include signs labelled by sense where the shape allowed a choice (points 4 and 5).

1. **a-shaped sign for b (4 places: `Ualf`, `dasf`, `a`, `dase`).** Elsewhere b has a tall stem; here the sign is a bowl with no ascender of its own. Either it is a short b or the writer left plain A unshifted. Both give the same plaintext.
2. **`nvdg` = MUCH and `gt` = IS.** These two signs have one shape, a closed bowl with a long looped descender. As g they would give MUCF and FS. It is probably this writer's looped j, used once where i was meant. Both are corrections by sense.
3. **`ofx` = NEW and `uift` = THIS.** The last sign of `ofx` is a long flat bar over a stem, closer to a t, which would give NES; "our new plan" is the only reading found. The third sign of `uift` is an f shape, literally THES, read as a long j.
4. **Medial j.** It is undotted and y-shaped in `njtublft`, `xjui` and `ojdf`. Taken as y it would give X and no words.
5. **Capitals and `bn`.** `Qptu` has a 2-like Q, `Tfdsfu` a detached heavy bar over a curve, and the n of `bn` could be taken for u, but no other word results.
6. **Signature.** The capital has three downstrokes, so it is M, and `Mpp` = LOO also stands on HCP 1398 and 1353. That Loo is a pet name is conjecture, and the dots between the letters are unusual for this signature.
7. **Meaning.** "G. H." is unexplained. "Secret" stands alone between periods, so what it qualifies is not determined. That "our new plan" means the cipher itself would suit "I have made no mistakes" and "on a post card", but this is an interpretation.

## Review

A separate Claude Opus 5.5 agent reviewed the solution (review/REVIEW1.md) with verdict **ACCEPT**. It ran the command, decrypted independently, compared all rows with the pixels, checked that no other shift gives English, and confirmed the Friday date. It raised four minor findings, none affecting the plaintext, and all were addressed:

1. The final capital was described as a two-humped N corrected to M. It has three downstrokes and is M as written, so that correction was dropped.
2. The looped sign of `nvdg` also begins `jt`, which had been given as a plain j. It is now disclosed in both places, which keeps the count at 8 normalised words.
3. A statement was added that the meaning of "G. H." is unknown.
4. The "as written" figure now carries the qualification given under Uncertainties.

The reviewer could not establish who Loo is or what the plan was, and could not decide whether the a-shaped signs are a short b or an unshifted A. Its statements about sister cards rest on their written solutions, not on their images.
