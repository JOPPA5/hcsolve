# HCP 1504 (pc_hcp_185): Christmas card from "your brother John" in false word division

Human solver: Tomáš Pavuk

**Status: accepted in independent review 1 (ACCEPT); final edition, 2026-10-26.**

## Origin and context

The card is record 1504 of the HCPortal cryptographic postcards collection (https://crypto.hcportal.eu/dashboard/cryptograms/1504), portal name pc_hcp_185, held in a private collection. The portal lists the main category as Transposition and gives date, language, location, sender and recipient as Unknown. When the solver acquired it on 2026-10-26 the record was marked **Not solved**, with no attached transcription or solution.

The card is a Raphael Tuck & Sons "Oilette" (plate marked) No. C2031, printed in England. The picture side is a printed Christmas card ("A Happy Christmas. Radiant may the gladness be that Christmas-time shall bring to thee") with no hidden text. The address side carries six short handwritten lines and no address, stamp or postmark, so the card was probably sent in an envelope or handed over. It cannot be dated more closely than the Tuck "Oilette" period. The signature JOHN is plain; who John was is unknown. The large lettered disk over both scans is the portal's watermark, not part of the card.

![Address side with the handwritten message (portal scan)](../source/address-large.jpg)

## Method

There is no attached transcription. The solver transcribed the six lines by hand from the scan (`work/transcription.txt`):

```
hop eyo uar
ewel lhop et
ose eyo usoo
nfro myou
rloven gbrother
john
```

The groups look like nonsense, but joined together the 55 letters read straight through as English. The writer only moved the word breaks, so that they fall inside English words (hop/eyo/uar = hope you ar[e], ewel/lhop/et = [e] well hope t[o]). No letter is substituted, dropped, added or moved. The portal category "Transposition" is therefore broad: in this card it is the spacing that is disguised, not the letter order.

## Key

There is no key in the usual sense. The only "key" is the new word division, and it is the plaintext itself. The decoder reads the solver's word list (`work/words.txt`) and checks that joining those words gives exactly the transcribed letter string, in order. Because the word list is the answer, this check cannot fail on content. What it does prove is that nothing was added, dropped or rearranged. The real evidence for the solution is that the unchanged letters read as continuous, natural English.

## Plaintext

Literal, as on the card (respaced only):

```
hope you are well hope to see you soon from your loveng brother john
```

Normalized reading: "Hope you are well. Hope to see you soon. From your loving brother John."

Slovak translation: „Dúfam, že sa máš dobre. Dúfam, že sa čoskoro uvidíme. Od tvojho milujúceho brata Johna."

The literal text keeps LOVENG, the spelling on the card. LOVING is the obvious intended word, but it is an editorial correction, not decoded output.

## Reproduction

From the repository root:

```
python3 ciphers/hcp-1504/work/decode.py
```

It checks the SHA-256 hashes of the source files, joins the transcription, respaces it with `work/words.txt`, and prints the plaintext, the letter count (55) and the line lengths. It does not read the image; the transcription is manual.

## Uncertainties

- `u` vs `w`: the first letter of `uar` and `usoo` has a lead-in stroke that makes it look like `w`. Both solver and reviewer read `u`; this hand's `w` (in `ewel`) is drawn differently.
- LOVENG: the fifth letter of `rloven` is a looped `e` with no i-dot. It is kept literally; "loving" is an interpretation.
- Date and people: no postmark, address or date. John's identity and the recipient are unknown.
- The decoder cannot fail on content (see Key); correctness rests on the transcription, which the reviewer confirmed independently.

## Review summary

The reviewer was Claude Opus 5.5 (Anthropic) and the verdict was **ACCEPT**. The reviewer transcribed the card letter by letter from enlarged crops before looking at the solver's file and got the identical 55 letters. A dictionary segmentation that did not use the solver's word list gave the same message. The documented command reproduced the claimed output byte for byte. Four minor findings:

- u/w: agreed with `u`; the note is kept (no change).
- LOVENG: agreed with keeping the literal spelling (no change).
- The "key" is the answer: this report now says plainly that there is no key in the usual sense and that the decoder cannot fail on content.
- Type label: the register type is "False word division (respacing)", not a transposition of letters.

The plaintext and transcription did not change as a result of the review. The closing steps (response to review, this report, register entry) were prepared by Claude Opus 5.5 on behalf of the solver (OpenAI GPT-6 Astra) at the human's request.

## Sources

- Portal record: https://crypto.hcportal.eu/dashboard/cryptograms/1504 (General, Description and Attachments tabs, read 2026-10-26).
- Address side: https://api.hcportal.eu/media/4573/conversions/pc_hcp_185_adr-large.jpg
- Picture side: https://api.hcportal.eu/media/4572/conversions/pc_hcp_185_pic-large.jpg
- AI Decipherment Register snapshot (https://ai.hcportal.eu/register/?format=json, 110 records): no entry for this card. This is not proof that no solution was ever published.
- No published solution was used.
