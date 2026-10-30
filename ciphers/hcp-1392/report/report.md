# HCP 1392 (pc_hcp_73): an English love card to Mr W. Abbott, 9 May 1907

Human solver: Tomáš Pavuk

**Status: enciphered message body deciphered in full (57 of 57 cipher letters); two short closing initial groups are kept literal. Independent review 1 verdict REVISE; one misread group at the end of line 4 was withdrawn, no decoded letter of the body changed.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1392 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1392), portal name pc_hcp_73, part of the HCPortal collection of cryptographic postcards (private collection). When it was captured on 2026-10-26 the portal listed it as **Not solved**, tagged Postcard, HCPortal collection, category Substitution, date 1907-05-09, language Unknown, location Europe, sender Unknown, recipient "W. Abboú" (a machine rendering of Abbott), with no transcription or solution attached.

The picture side is a printed view, **Connaught Park and Dover Castle**, with no handwriting. Everything handwritten is on the address side, which is scanned sideways; the message is read after turning the scan 90° counter-clockwise. The address, in plain writing, is to **Mr W. Abbott, Stokelake Farm, Chudleigh, Devon**. The card bears a halfpenny Edward VII stamp and the postmark **[WI]MBORNE 10 PM MY 9 07**. The plain heading reads **G. H. Thursday.** and the plain date in the margin **May 9th 07**; 9 May 1907 was indeed a Thursday, and the date agrees with the postmark and the portal.

The card belongs to a family of English cipher postcards from one couple in 1907–08 (HCP 1386–1407 in this repository), all to Mr W. Abbott, all in the same simple letter shift and with the same formulas ("My own dearest … from your own … girl"). No published solution of this card was found or used.

![Address side as scanned (source/address.jpg)](../source/address.jpg)

![Message turned upright and enlarged (work/crops/message-rot-3x.png)](../work/crops/message-rot-3x.png)

![Picture side: Connaught Park and Dover Castle (source/picture.jpg)](../source/picture.jpg)

## Method

The transcription is **manual**, made sign by sign from the scan turned upright and enlarged 3–10×; no OCR was used and the portal supplied no transcription. Short words such as `Nz Pxo`, `Gspn zpvs pxo` and `Hjsm` are visibly English shifted one letter forward; subtracting one (A→Z) gives MY OWN, FROM YOUR OWN, GIRL, and the same shift reads every other enciphered word. A sweep of all 26 shifts (also done independently by the reviewer) shows that only this shift gives English. The key is the same as on the sister cards HCP 1390, 1393, 1395, 1397 and 1407. Dots after many words are the writer's punctuation and are kept.

A script (`work/decode_full.py`) checks the SHA-256 of both source images, decrypts the transcript `work/transcript_full.json` line by line, re-encrypts every line to confirm the round trip, and prints the literal groups and the plain fields. From the repository root:

```text
python3 -I ciphers/hcp-1392/work/decode_full.py
```

## Key

Caesar substitution, encryption shift +1 (each plain letter is written as the next letter of the alphabet; decryption one place back).

```text
Cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

## Transcription and plaintext

| Ciphertext | Plaintext |
|---|---|
| *(plain)* G. H. Thursday. | G. H. Thursday. |
| Nz Pxo. Efbsftu | My Own. Dearest |
| Tfoejoh. b. dbse | Sending. a. card |
| up. Z— jotufbe | to. Y— instead |
| pg. mfuufs. N & L! | of. letter. [N & L!] |
| Gspn. zpvs pxo N^b: | From. your own [N^b] |
| Hjsm | Girl |
| *(plain, margin)* May 9th 07 | May 9th 07 |

Square brackets mark the two initial groups that are kept literal and not shifted.

**English:** "G. H. Thursday. My own dearest, sending a card to Y— instead of a letter. [N & L!] From your own [N^b] girl. May 9th '07."

**Slovak:** „G. H. Štvrtok. Môj najdrahší, posielam Y— pohľadnicu namiesto listu. [N & L!] Od tvojho vlastného [N^b] dievčaťa. 9. mája 1907.“

## Uncertainties

1. **"N & L!"** (end of line 4, paler ink): the writer's capital N, a short dash, a small reversed-c ampersand, a tall pale capital L, and "!". The same group stands in the same place on sister cards HCP 1393, 1395 ("M. & L."), 1403 ("N. & L.") and 1407 ("M. & L.'"). N or M is not fully decided. Whether it is enciphered (it would give "M & K") or plain initials, and what it abbreviates (perhaps a "[many kisses] & love"-type formula), is not claimed.
2. **"N^b"** before "Hjsm": a capital N followed by a small raised b/h-like letter with two dots beneath. A raised letter with a mark under it is the usual form of a superscript abbreviation such as "Nᵒ" ("your own No. … girl"?); HCP 1407 has "N.-1" and HCP 1393 "Mᵘ." in the same slot. Kept literal.
3. **"Efbsftu"** (DEAREST): E, f, b, s are dark; the final "ftu" is pale and crossed by the portal watermark ring. The reading is supported by the visible letters and by the identical salutation on HCP 1390 and 1407.
4. **"Z—"** = "Y—": a single cipher letter with a long dash, an abbreviation (perhaps "you", perhaps a name); not expanded.
5. The capital T of "Tfoejoh" is joined to the following f, and the capital G of "Gspn" has this writer's Y-like G form; in both places only that letter gives a word (SENDING, FROM).
6. The heading initials "G. H." (read "C. H." on a sister card) and the date are plain. The identity of the sender and the full postmark office name are not established.

## Why the reading is believed correct

All 57 letters of the enciphered body decode with one fixed shift into grammatical English of the period that fits the card: a lover sends a picture postcard instead of a letter, with the family's standard salutation and closing. The day and date in the heading agree with the postmark and the portal, and the key is the one used throughout the Abbott correspondence. Only the two short initial groups, which are also unresolved on the sister cards, are left undecoded.

## Review and what changed

An independent reviewer (a separate Claude Opus 5.5 agent) ran the reproduction command, decoded its own independent transcription with its own script (shift sweep: only −1 gives English), checked every line against enlarged crops of the scan, and checked the sources. Verdict **REVISE** with three findings:

1. **(major)** The end of line 4 had been read "Ib-Ib!" = "Ha-Ha!". The reviewer showed that its first sign has exactly the construction of this writer's capital N, and that the group is the "N & L" closing group of the sister cards. The solver re-examined the crops, agreed, withdrew "Ha-Ha!" and now keeps the group literal as "N & L!"; the count of enciphered letters went from 61 to 57.
2. **(minor)** The "No." possibility and the sister parallels for the "N^b" group were added as alternatives.
3. **(minor)** The statement of why the reading is correct was corrected so that it no longer claims that every word decodes.

The decoded letters of the message body did not change.

## Credit

Initial capture, key identification and a partial reading (My Own Dear / ?ending a card / to Y— instead / of letter / ?rom your own M…) were done on 2026-10-26 by an OpenAI GPT solver. The full re-reading from the scan, the corrected address, the final transcript and decoder, the response to review and this report were done by Claude Opus 5.5 on 2026-10-29/30; the independent review was done by a separate Claude Opus 5.5 agent.
