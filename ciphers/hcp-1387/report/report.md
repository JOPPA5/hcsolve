# HCP 1387 (pc_hcp_68): an English Caesar love postcard to W. Abbott, 1 December 1907

Human solver: Tomáš Pavuk

**Status: enciphered body read in full (68 of 68 cipher letters, one key); one short dotted abbreviation group is left unexpanded and one word ("Girl") rests partly on context. Independent review 1 verdict ACCEPT, no change to the decoded letters.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1387 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1387), portal name pc_hcp_68, part of the HCPortal collection of cryptographic postcards (private collection). When it was captured on 2026-10-26 the portal listed it as **Not solved**, tagged Postcard, HCPortal collection, category Substitution, date 1907-12-01, language Unknown, location Europe, sender Unknown, recipient "W. Abboú" (a misreading of Abbott), with no transcription or solution attached.

The picture side is a printed view, "Buxton from the Town Hall" (Valentine's Series), with no handwriting. All the writing is on the address side. The address is in plain: **Mr W. Abbott, Stokelake Farm, Chudleigh, S. Devon.** The card carries a green halfpenny Edward VII stamp cancelled **WIMBORNE 10 PM DE 1 07**. The message, written on the left half of the card and read after turning it 90° counter-clockwise, opens with the plain heading **"G. H. Sunday"**; 1 December 1907 was indeed a Sunday. A circled plain aside at the lower left reads **"going to D."**. Below the heading, seven lines are enciphered.

The large circular A–Z disc and the building logo printed over both scans are the HCPortal watermark, not part of the card.

The card belongs to a run of postcards to W. Abbott at Stokelake Farm (HC Portal 1386–1398 and 1401–1407, 1907–08) written by a correspondent who signs as G. H. (possibly C. H.) and uses the same simple cipher. Several of them are deciphered in this repository, for example HCP 1397 ("Love from your own girl") and HCP 1388.

![Address side as scanned (source/address.jpg)](../source/address.jpg)

![Message area turned upright: plain heading "G. H. Sunday", seven cipher rows, and the circled aside "going to D." (work/message.jpg)](../work/message.jpg)

## Method

The transcription is **manual**: the address side was turned 90° counter-clockwise and the seven message rows were read letter by letter from 2–5× enlargements. No OCR was used and the portal supplied no transcription. The rows and the plain fields are recorded in `work/transcript_full.json`.

Short words make the key obvious. **Nz** becomes "My" and **Gspn** becomes "From" if each letter is moved one place back in the alphabet. Once applied to the whole text, the same shift turns every one of the 68 cipher letters into English, with no per-word adjustment: **Mfuufs** → Letter, **Uibolt wfsz** → Thanks very, **Nvdi gps bmm** → Much for all, **Zpvs Pxo** → Your Own. The same key is used on the sister cards to W. Abbott.

The difficult places were checked against other occurrences of the same letter shapes in this hand. They are the j of npsjoh and Hjsm (a long upstroke whose descender loops or hooks to the left, as in uijt), the c-like s (as in wfsz), the uncrossed t (as in Uibolt) and the flat-based z (as in Nz, Cpz).

In review the reviewer made its own upright 3× crop of the scan and further enlargements (row 3, rows 6–7, the last word, the row-6 middle group, a comparison of z forms). It checked every row against the ink and decrypted the transcript with its own independent script; the result was identical.

## Key

Caesar substitution with shift +1: each plaintext letter is written as the **next** letter of the alphabet. To decipher, move each letter one place back. Case and the writer's dots are kept.

```text
Cipher: ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain:  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

## Plaintext

Ciphertext as transcribed, and the literal plaintext, row by row:

| Row | Ciphertext | Literal plaintext |
|---|---|---|
| 1 | Nz. Pxo. E.h Cpz. | My. Own. D.g Boy. |
| 2 | Mfuufs uijt | Letter this |
| 3 | npsjoh, | moring, |
| 4 | Uibolt wfsz. | Thanks very. |
| 5 | Nvdi gps bmm. | Much for all. |
| 6 | Nz. h.v y. Gspn | My. g.u x. From |
| 7 | Zpvs Pxo. E.h Hjsm | Your Own. D.g Girl |

The writer puts dots after many words; they are separators, not sentence ends.

Normalized English (punctuation editorial; plain parts in italics; bracketed expansions are guesses):

**_G. H. Sunday._ — My own D.g [darling?] boy. Letter this morning. Thanks very much for all. My g.u x [unexpanded]. From your own D.g [darling?] girl. _(Aside: going to D.)_**

Sense: the writer thanks "her own boy" for the letter that arrived that morning and for everything, and signs as "your own girl".

Slovak translation: **G. H., nedeľa. — Môj vlastný D.g [drahý?] chlapče. List [prišiel] dnes ráno. Veľmi pekne ďakujem za všetko. Môj g.u x [nerozvinuté]. Od tvojho vlastného D.g [drahého?] dievčaťa. (Poznámka: idem do D.)**

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1387/work/solve.py
```

The script uses only the Python standard library. It checks the SHA-256 hashes of both scans and the metadata. It then decrypts every row of the manual transcript in `work/transcript_full.json` with the shift −1 and verifies the round trip. Finally it prints the seven rows above, the count "68 cipher letters decrypted with one key", and the plain fields. It does not read the image; the transcription step is manual and was confirmed independently in review.

## Uncertainties

- **Row 6 "h.v y." (main residual).** A dotted abbreviation group between "My." and "From". The first glyph has the same form as the h of E.h. The second is a looped v-like sign; it could alternatively be this writer's z (giving "g.y" instead of "g.u"), although it is larger and ends in an upstroke, unlike the flat-based z of Nz and Cpz. The third is a cursive y with a descender. Mechanically the group reads "g.u x." (the x is possibly a kiss). It is left unexpanded.
- **Row 7 "Hjsm" → Girl.** The capital H is certain. The next stroke has a bowl at the top of its stem, a little like this writer's p, but its descender ends in a left-curling hook (j), not the straight p descender of Zpvs and Gspn. A literal "Hp…" reading gives no word. "Girl" is chosen on the j-hook, the parallel with "Boy" in row 1, and the "your own girl" closing of the sister cards: the reading relies partly on context.
- **"E.h" (rows 1 and 7).** If enciphered it gives "D.g", which might abbreviate "darling", but this expansion is a guess. It is also possible that "E.h" is written in plain (initials or a pet name) and not enciphered at all, as was left open on sister card HCP 1388.
- **Row 3 "moring".** No ink for a second o is visible between s and j; the writer apparently left out a letter of "morning". Nothing was inserted into the literal output.
- **Row 2 "uijt".** The final t is this writer's uncrossed, c-like t; one of the two dots near it may be a period.
- **Plain fields.** The initials may be G. H. or C. H.; "D." in the aside is not expanded; the identities of the writer and of W. Abbott are not established beyond the address.
- No search for a prior publication of this card was made beyond the portal status (Not solved, no attachment) and the AI Decipherment Register (no record for this card, checked 2026-10-29).

## Review summary

Reviewer: a separate Claude Opus 5.5 agent, round 1, verdict **ACCEPT**. The reviewer ran the reproduction command (output identical to the claimed plaintext) and decrypted the transcript with its own script. It found that one fixed key covers all 68 letters, made its own crops and enlargements, and confirmed rows 1–7 letter by letter against the ink. That includes the literal "moring". It also checked that the text is idiomatic Edwardian English and that it agrees with the sister cards. Finally, it confirmed that the postmark date (Sunday, 1 December 1907) matches the heading and that no published solution was used. Its four findings were minor and are reflected here:

- **"Girl".** The caveat that the reading partly depends on context is kept (above).
- **Row 6 group.** The alternative z reading of its second glyph is now named next to v.
- **"E.h" / darling.** The expansion "darling" is now marked as a guess, and the plain "E.h." alternative is named.
- **Postmark hour.** Now consistently given as 10 PM (legible on the scan).

No decoded letter changed as a result of the review.

## Credit

The first stage of the work in this directory was done by an OpenAI GPT solver (GPT-6 Astra / GPT-6.1 Sol) on 2026-10-26. It captured the sources, rotated and cropped the scans, identified the −1 key and read a partial excerpt of 26 letters. Claude Opus 5.5 completed the work on 2026-10-29–30: the full transcription of all seven rows, the reproduction script, the solution, the response to review and this report. The independent review was made by a separate Claude Opus 5.5 agent.

## Sources

- HC Portal record 1387, General, Description and Attachments tabs, captured 2026-10-26: https://crypto.hcportal.eu/dashboard/cryptograms/1387 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/4221/conversions/pc_hcp_68_pic-large.jpg (source/picture.jpg).
- Address side: https://api.hcportal.eu/media/4222/conversions/pc_hcp_68_adr-large.jpg (source/address.jpg).
- Sister cards to W. Abbott in this repository, e.g. ciphers/hcp-1397 and ciphers/hcp-1388.
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-29.
