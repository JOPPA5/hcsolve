# Portal1491 / pc_hcp_172 — mirror-writing candidate

Rendered status Not solved on2026-10-26. The entire correspondence is
mirror-written English, with a short French closing. Independent review pending.

## Transform and reproduction
Key: rotate the original address image270degrees clockwise, then reflect
horizontally. The address is normal writing and does not need this transform;
the transformed correspondence appears in the lower half of corrected image.

Run from repository root:
`python3 ciphers/hcp-1491/work/decode.py`

This verifies immutable source hashes and produces /tmp/hcp-1491-decoded.png
directly from source/address-large.jpg. It also prints the separately saved
manual reading in work/plaintext.txt. **It does not OCR the image.**
An already generated lossless corrected image is in work/decoded.png.
The transform is reproducible evidence; the manual reading still needs an
independent comparison against that image.

## Plaintext
```
I got back quite safely and
delivered your little parcel and
messages. I did not meet Lawrence
or see him at the station but I
met an old "B" and he kept me talking
til I had to run for my train in
the end. I hope you will keep "well
and warm" as you said in your
message. Au revoir
Ever your own Browning.
```

Punctuation/quotation placement reflects a manual reading, with conventional
capitalization. No additional words supplied. B is not expanded.
The visible spelling til is preserved rather than normalized to till.

Slovak: „Vrátil som sa celkom bezpečne a doručil som tvoj balíček aj odkazy.
Lawrencea som nestretol ani nevidel na stanici, ale stretol som starého B
a ten ma zdržal rozhovorom, až som napokon musel utekať na vlak.
Dúfam, že zostaneš zdravá a v teple, ako si napísala vo svojom odkaze.
Dovidenia. Navždy tvoj Browning.“
Writer gender in this translation is conventional, not an independently
established biographical fact.

## Evidence and limits
One fixed geometric transform reveals the complete coherent correspondence,
including parcel, station/train narrative and closing. No cipher key fitting,
per-word correction, hidden omitted passage, or corpus plaintext used.
Lawrence, quoted B and apparent Browning should be independently checked
against handwriting. No identification of a famous Browning or another
historical person claimed. Plain address and printed picture text excluded.
No supplied/published solution used. No accepted FINAL, PDF or register entry
claimed before independent review.
Manual correspondence transcription contains234 alphabetic characters.
Fresh register110 records has no exact URL1491/name pc_hcp_172 match;
this does not establish historical priority.

## Response to review 1

Review 1 by Claude Opus 5.5 (2026-10-26), verdict ACCEPT. The reviewer read the
transformed scan independently and agreed with the plaintext word for word and
line for line. No finding changes the plaintext.

1. Addressee surname (minor) – accepted. The card reads "Miss Frances Mantz"
   (crossed t followed by a long-tailed z; no d or y). The earlier image note
   "Miss Frances Mandy" in source/metadata.md is a misreading; the portal's
   recipient field "Frances Mandy" is recorded as the catalogue value. source/
   is left unchanged; the correction is recorded here and in the report.
2. Cipher type (minor) – accepted. The report and register entry use
   "Mirror writing" (mirror-written cursive turned 90 degrees on the card) and
   note that the portal tag "Transposition" differs.
3. `til` (minor) – accepted. The literal reading `til` is kept and listed in
   the report as a reading judgement: a second l could be lost in a cramped
   loop at this resolution.
4. Default output path (minor) – accepted. The report names work/decoded.png
   as the evidence image and gives the command with an explicit output path;
   decode.py itself is not changed.

The reviewer also noted that no full stop is visible after "Browning"; the
report shows the closing without it. Postmark: VICTORIA DOCKS (London E.),
3.15 PM, ·A 18, 09 – day and year agree with the portal date 1909-01-18; the
month is only partly legible.

Closing steps (this response, report, register entry, FINAL) prepared by Claude Opus 5.5 on the solver's behalf at the human's request, 2026-10-26.
