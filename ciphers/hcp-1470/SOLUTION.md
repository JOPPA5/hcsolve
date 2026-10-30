# HCP 1470 / pc_hcp_151 — numeric signature line (A1Z26)

Status: complete decoding of all 14 numbers on the card; the result is a
personal name-like string that cannot be checked against any outside record.
Solver this round: Claude Opus 5.5 (DONE1 created 2026-10-29T23:17Z UTC). Earlier work (2026-10-26,
OpenAI GPT solver): portal capture, source hashes, provisional 14-number
reading, A1Z26 and shift screen — credited; its reading is confirmed below
except that its 13/12 doubt at position 5 is resolved to 13.

## Card and context

Birthday postcard ("Anniversaire", picture no. 1158: man with a bouquet),
French 10 c Semeuse stamp, railway postmark TOURS A VIERZON 30-3-09
(portal date 1909-03-30). Address in plain French: *Mademoiselle Valentine
P[o/a]udechat aux Caves, Commune de Lacroix (Indre et Loire)* (surname read
loosely, not part of the cipher). The only other handwriting is one curved
line of dash-separated numbers on the correspondence half. Portal status
"Not solved"; no transcription or solution attached; no published solution
of this card found. The grey A–Z disc and logo over both scans are the
HCPortal watermark, not part of the card.

## Cipher type and key

Simple numeric substitution, A1Z26: 1=A, 2=B, ... 26=Z (no offset). The
values used: 1=A 4=D 5=E 9=I 13=M 14=N 15=O 18=R 20=T.

## Transcription (work/transcription.txt)

    13-1-18-9-13-1-18-18-1-14-4-5-15-20

Read on rotated (30 deg) and 3–10x enlarged crops: work/crop-line-start-rot30.png,
work/crop-line-tail-rot30.png, work/crop-14-4-zoom.png.
- Position 5 is "13" (a 1 followed by the same cursive, flat-topped 3 as in
  position 1); the earlier alternative 12 is rejected.
- Positions 10–11 "14-4": both 4s have the same construction (stem with a
  crossbar and a lead-in stroke from the upper left). The second 4 sits on the
  printed double divider line, which obscures part of it; no top bar is seen,
  so a crossed French 7 (giving G) is judged unlikely but not impossible.

## Plaintext

Literal: `MARIMARRANDEOT`
Editorial segmentation: **MARI MARRANDEOT**

Interpretation (not proven): a signature — a first name *Mari* (or *Marie*
written without final e, or French *mari* "husband") and a surname
*Marrandeot*. On an otherwise blank correspondence half of a birthday card the
sender signing in code is the natural reading, and the portal sender field is
"Unknown". The language is French by context (French card, French address);
a name is not language-specific.

- English: "Mari(e) Marrandeot" [signature of the sender].
- Slovak: „Mari(e) Marrandeot" [podpis odosielateľa].

## Single command (from repo root)

    python3 -I ciphers/hcp-1470/work/decode.py

It verifies the SHA-256 of all files in source/ (work/source-sha256.json),
reads work/transcription.txt and prints the literal and segmented plaintext.
The transcription is manual; the script does not read pixels.

## Uncertainties

1. The name is not attested anywhere I could check; *Marrandeot* is not a
   surname I can confirm (similar French names: Marandeau, Marandet). No
   correction is applied — the output is reported literally.
2. Segmentation MARI | MARRANDEOT is editorial (no word separator on the card).
3. Position 11 (4 = D) partly under the printed divider; alternative 7 = G
   would give MARRANGEOT. Judged less likely (see above).
4. Recipient surname in the plain address is a loose reading and irrelevant
   to the decoding.

## Why I believe it is correct

- The whole cipher is 14 numbers, all in 1..26, every one decoded with the
  plain A1Z26 key used on many sister postcards of this collection
  (hcp-1098, 1463, 1492, 1496).
- No shift or reverse alphabet gives anything pronounceable (earlier screen,
  work/numeric-attempts.txt); A1Z26 gives a pronounceable French-looking
  first name + surname, with the repeated pattern 13-1-18 = MAR in both parts.
- Fits the card: a signature is the only text expected on an otherwise blank
  greeting-card message area.
- What it does not establish: the identity of the sender.

## Response to review 1

Review 1 (Claude Opus 5.5, separate agent) verdict: **ACCEPT**. The reviewer's
independent reading of all 14 numbers is identical to work/transcription.txt
and its own decoder gives the same MARIMARRANDEOT. No decoded letter changes.
Reproduction command re-run after this response
(`python3 -I ciphers/hcp-1470/work/decode.py`): `source hashes OK`, 14 numbers,
literal `MARIMARRANDEOT`, segmented `MARI MARRANDEOT` — unchanged.

1. (minor) Name unverified. Agreed; no change to the reading. The report
   presents "Mari(e) Marrandeot" only as the literal decode / probable coded
   signature, not as an identified person, and mentions that it could be a
   variant or slip for an attested central-French surname such as Marandeau
   or Marandet without adopting that.
2. (minor) Position 11, 4 vs 7. Agreed and kept. Re-checked on
   work/crop-14-4-zoom.png: the sign is a long diagonal stem with a crossbar,
   lying under the printed double divider; no top bar is visible, unlike a
   crossed French 7. Reading 4 = D kept; MARRANGEOT (7 = G) stays listed as
   the alternative in the uncertainties and in the report.
3. (minor) Date inconsistency. Fixed: the header now gives the UTC time of
   DONE1 (2026-10-29T23:17Z) instead of the local date 2026-10-30; NOTES.md
   records the same. The report uses UTC dates.
4. (minor) Segmentation/language and the *mari* "husband" gloss. Agreed; the
   segmentation MARI | MARRANDEOT and the French-language attribution stay
   labelled editorial, and the *mari* gloss is marked speculative in the
   report.

Outcome: verdict ACCEPT with all four minor findings addressed and the reading
unchanged, so the cipher is closed (report, register entry, FINAL).
