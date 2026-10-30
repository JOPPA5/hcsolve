# HCP 1464 (pc_hcp_145): a mirror-written note from Joe to Miss L. Wood, 1905

Human solver: Tomáš Pavuk

**Status: read in full by horizontal reflection; the last letter of one word is restored from context. Independent review 1 verdict ACCEPT, no change to the reading.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1464 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1464), portal name pc_hcp_145, part of the HCPortal collection of cryptographic postcards (private collection). When it was captured on 2026-10-26 the portal listed it as **Not solved**, tagged Postcard, HCPortal collection, category Transposition, date 1905-12-12, language Unknown, location Europe, sender Unknown, recipient L. Wood, with no transcription or solution attached.

The picture side is a printed view captioned **FELISKIRK. NEAR THIRSK** (Felixkirk, a village in the North Riding of Yorkshire). It carries no handwriting.

The address side is in plain writing: **Miss L. Wood / Kepwick / Northallerton / York's.** Kepwick is a small village a few miles north of Felixkirk, near Northallerton, so picture and address belong to the same neighbourhood. The postmark on the original scan reads **DE 12 05**, i.e. 12 December 1905, which matches the portal date. To the left of the address, in the message half of the card, stand four short lines of handwriting that look like nonsense as scanned: they are written in mirror image.

![Picture side: Feliskirk near Thirsk (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side as scanned; the mirror-written message is on the left (source/address-large.jpg)](../source/address-large.jpg)

The large lettered wheel and the padlocked building drawn faintly over both scans are the HCPortal watermark, not part of the card.

## Method

The "cipher" is **mirror writing**: the message was written right to left with every letter reversed, so that it reads normally in a mirror. Mirror writing was a common postcard game in the Edwardian period; it hides a message from a casual glance but uses no key.

The address side was reflected left to right as a pure pixel operation, with no text added:

```sh
sips -f horizontal ciphers/hcp-1464/source/address-large.jpg --out /tmp/hcp-1464-decoded.jpg
```

The output is byte-identical to work/decoded.jpg in the cipher directory. In the reflected image the four lines read directly as cursive English. Rotation by 180 degrees and a vertical flip were tried first and do not produce legible text (work/rotated.jpg, work/vertical-flip.jpg).

![The message after left-right reflection, enlarged 3x (work/message-reflected-3x.png)](../work/message-reflected-3x.png)

The address and postmark are written normally and are read on the original scan; only the message is mirrored.

The earliest work (capture of the portal record, download of the scans, discovery that a horizontal reflection makes the message legible, and a first reading with the last word of line 2 left open) was done by an OpenAI GPT solver. Claude Opus 5.5 completed the reading, handed it to review, and prepared this report.

## Key

There is no key. The only transformation is a horizontal (left-right) reflection of the whole message. Cipher type: **mirror writing**.

## Plaintext

Reflected text, line by line as on the card (square brackets mark a restored letter):

```text
I hope you
will like thi[s]
from Joe.
Amen
```

English (original): **I hope you will like this, from Joe. Amen**

Slovak translation: **Dúfam, že sa ti toto bude páčiť. Od Joea. Amen.**

"This" presumably refers to the picture postcard itself; "Amen" reads as a playful closing.

## Uncertainties

- **The last letter of "this".** In the original orientation the second line runs up to the left edge of the card. At 5x the word ends with a clear *t*, *h* and dotted *i*, followed by a heavy ink blot that runs into the card edge. The blot fills the position of a final letter but is **not a recognisable letter form**. The *s* is restored from context ("will like thi-" admits essentially only "this"), not seen.

![The end of line 2 in the original orientation, 5x: "this" mirrored, with the blotted final position at the card edge on the left (work/edge-original-5x.png)](../work/edge-original-5x.png)

- **Persons.** "Joe" and Miss L. Wood of Kepwick are not identified further; this is not needed for the reading.
- **Decorative strokes.** Short dashes below "Amen" and below "York's" are taken as flourishes or underlining; they show no alphabet and no second code.
- **Physical card.** Whether the final letter was lost to trimming or to blotting can be judged only from the 1024-pixel scan.
- No search for a prior publication of this card was made beyond the portal status (Not solved, no attached solution) and the AI Decipherment Register (no entry for cryptograms/1464 or pc_hcp_145, checked 2026-10-29).

![Address in the original orientation, 2x: Miss L. Wood, Kepwick, Northallerton, York's (work/address-2x.png)](../work/address-2x.png)

## Review summary

Reviewer: Claude Opus 5.5 (Anthropic), a separate agent, round 1, verdict **ACCEPT**. The reviewer ran the reflection command (output identical to work/decoded.jpg), reflected the scan independently with its own script, read the message letter by letter from its own enlargements and obtained exactly the same four lines. It accepted "this" as a disclosed restoration, confirmed that the whole message area is accounted for and that the picture side carries no handwriting, and found the text natural Edwardian English, consistent with the Felixkirk picture, the Kepwick address and the December 1905 postmark. Its four findings were minor and are reflected here:

- **Address.** The second address line, earlier given as "Hayrick(?)", is clearly **Kepwick**; corrected.
- **Postmark.** "DE 12 05" is read on the original scan, not on the reflected one; corrected.
- **Stale wording.** Pre-handover wording in SOLUTION.md is superseded by its response to review; one Slovak rendering is used.
- **Edge letter.** The final *s* of "this" is now described as restored from context and from an ink blot at the edge, not as a visible cursive *s*.

No word of the message changed as a result of the review.

## Sources

- HC Portal record 1464, General, Description and Attachments tabs, captured 2026-10-26: https://crypto.hcportal.eu/dashboard/cryptograms/1464 (source/metadata.md).
- Address side: https://api.hcportal.eu/media/4453/conversions/pc_hcp_145_adr-large.jpg (source/address-large.jpg).
- Picture side: https://api.hcportal.eu/media/4452/conversions/pc_hcp_145_pic-large.jpg (source/picture-large.jpg).
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-29.
