# HCP 1390 (pc_hcp_71): an English love card to Mr W. Abbott, 6 May 1907

Human solver: Tomáš Pavuk

**Status: message body deciphered in full (56 of 56 cipher letters); two short closing groups remain unread. Independent review 1 verdict ACCEPT; no decoded letter changed as a result of the review.** Report dated 2026-10-29.

## Origin and context

The cryptogram is record 1390 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1390), portal name pc_hcp_71, part of the HCPortal collection of cryptographic postcards (private collection). When it was captured on 2026-10-26 the portal listed it as **Not solved**, tagged Postcard, HCPortal collection, category Substitution, date 1907-05-06, language Unknown, location Europe, sender Unknown, recipient "W. Abboú" (a machine rendering of Abbott), with no transcription or solution attached.

The picture side is a printed view, **The Exchange, Liverpool**; it carries no handwriting. Everything handwritten is on the address side, which is scanned sideways: the message stands in the left-hand correspondence field and is read after turning the scan 270°. The address, in plain writing, is to **Mr W. Abbott**, a farm (probably Stokelake Farm, as on sister card HCP 1397) at **Chudleigh, S. Devon**. The plain heading reads **C. H. Monday** and the plain date **May 6th 1907**, matching the portal date.

The card belongs to a family of English cipher postcards from one couple in 1907–08 (HCP 1386–1407 in this repository), all to Mr W. Abbott and all written in the same simple letter shift. The key here was found from this card's own words and agrees with the family key.

![Address side as scanned: message on the left, address on the right (source/address.jpg)](../source/address.jpg)

![Message turned upright and enlarged (work/message-large.jpg)](../work/message-large.jpg)

![Picture side: The Exchange, Liverpool (source/picture.jpg)](../source/picture.jpg)

## Method

The transcription is **manual**, made sign by sign from the scan turned upright and enlarged; no OCR was used and the portal supplied no transcription. Several short words were legible at once as shifted English: `Nz Pxo Efbsftu`, `up ebz`, `Gspn zpvs pxo`, `Hjsm`. Each letter is one place further along the alphabet than the plain letter, so subtracting one (A→Z) gives MY OWN DEAREST, TO DAY, FROM YOUR OWN, GIRL. The same shift then reads the two middle lines. A sweep of all 26 shifts confirms that only this one gives English. Word divisions follow the handwriting; dots after many words are ordinary punctuation and are not transcribed.

## Key

Caesar substitution, encryption shift +1 (decryption: each letter one place back).

```text
Cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

The key decodes every one of the 56 letters of the body, with no exception.

## Plaintext

Ciphertext, line by line as on the card:

```text
L1 Nz Pxo Efbsftu
L2 Nboz uibolt Gps
L3 hsboe Mfuufs
L4 up ebz [capital + raised small letter, dot] y y
L5 Gspn zpvs pxo
L6 [capital M + raised small letter, dot] Hjsm
```

Decoded:

```text
L1 My Own Dearest
L2 Many thanks For
L3 grand Letter
L4 to day [unread group] x x
L5 From your own
L6 [unread abbreviation] Girl
```

**English (normalized):** "My own dearest, many thanks for grand letter to-day. [unread] xx (kisses). From your own [unread] girl."

**Slovak:** „Môj najdrahší, veľká vďaka za skvelý list dnes. [nečitateľné] xx (bozky). Od tvojho vlastného [nečitateľná skratka] dievčaťa.“

The plain parts of the card: heading "C. H. Monday", date "May 6th 1907", address "Mr W. Abbott / [Stokelake?] Farm / Chudleigh / S. Devon", and the printed caption "The Exchange Liverpool".

## Reproduction

From the repository root:

```bash
python3 -I ciphers/hcp-1390/work/decode.py
```

The script checks the SHA-256 hashes of the original source files, reads the manual transcription (work/transcription.json), applies the key, verifies that re-enciphering gives back the cipher text, and prints the six decoded lines. It reproduces the **body only**; the two unread closing groups are printed as notes, not decoded.

## Uncertainties

- **The group after "to day".** A large looped capital (M-like; it lies partly under the grey HCPortal watermark band) with a small raised h-like letter and a dot (work/line4-tail-3x.png). It may be an initial or an abbreviation, enciphered or plain; it is not read.
- **The two marks after it.** Each has a small hook at top left and a long descending diagonal. Read as cursive cipher `y y` they decode to `x x`; read as plain crosses they are `× ×`. Either way they are kisses.
- **The abbreviation before "Girl".** An apparently retraced capital M followed by a small raised letter with a tall ascender (h/k/b-like) and a dot (work/signature-3x.png). An earlier reading `Mu` (→ `Lt`, "little"?) was withdrawn in review because no u-shape is visible. Its build resembles the group after "to day"; neither is read.
- The heading initials C. H. and the farm name are plain writing outside the cipher and are not expanded. The sender's identity is not established.
- No published solution of this card was found (portal status Not solved; AI Decipherment Register checked 2026-10-29, no entry).

![Group after "to day", enlarged 3x from the upright image (work/line4-tail-3x.png)](../work/line4-tail-3x.png)

![Abbreviation before "Girl", enlarged 3x from the upright image (work/signature-3x.png)](../work/signature-3x.png)

## Review summary

Reviewer: Claude Opus 5.5 (Anthropic), a separate agent, round 1, verdict **ACCEPT**. The reviewer ran the reproduction command (output identical to the claimed plaintext), made its own transcription from rotated 3×–7× crops of the scan, and decoded it with its own script: all 56 letters give the same body, and only shift 1 of 26 gives English. It checked the date, address and family context against the sister cards HCP 1386–1407. Its four minor findings were all accepted:

- **Stale status text.** SOLUTION.md still opened with the earlier "partial" status; it now carries one current status, and the decoder no longer prints "PARTIAL".
- **"Mu." not supported.** The signature abbreviation is now described as "M + raised h/k/b-like letter, unread"; the conditional "Lt"/"little" reading was withdrawn.
- **×× may be y y.** Both readings (cipher `y y` → `xx`, or plain crosses) are now given; the meaning, kisses, is the same.
- **Command covers the body only.** This is now stated in the script output and in this report.

No decoded letter of the body changed as a result of the review.

## Credits

The source capture, the manual transcription and the decipherment of the body were done on 2026-10-26 by an OpenAI GPT solver, which left the card as a partial reading. Claude Opus 5.5 (Anthropic) completed the closing analysis on 2026-10-29, handed it to review, answered the review and wrote this report.

## Sources

- HC Portal record 1390, General, Description and Attachments tabs, captured 2026-10-26: https://crypto.hcportal.eu/dashboard/cryptograms/1390 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/4230/conversions/pc_hcp_71_pic-large.jpg (source/picture.jpg).
- Address side: https://api.hcportal.eu/media/4231/conversions/pc_hcp_71_adr-large.jpg (source/address.jpg).
- Sister cards of the same couple in this repository: ciphers/hcp-1386 … hcp-1407 (e.g. hcp-1397, same address).
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-29.
