# HCP345 / published HCP486 repeat collation

All 65 ciphertext letters agree between the original HCP486 scan, the HCP345 repeat scan, and the old HCP345 working transcription. Both printed headers are 165. This is complete literal collation, not just a matching opening. HCP486 is telegram 80102; HCP345 is its repeat 80103. The repeat explicitly says 80102/44 was resent after a request from Bucharest and that the earlier message was correctly encrypted. The public HCP486 description independently links 80103 to 80102.

The following plaintext is **published archival context**, not our independent decipherment or a new register entry. Literal quoted telegram:

> dňa 25.januára ide odtiaľ kurier,ktorým
> Vám pošleme effektívne Lei.

The archival draft spells “kurier” without an acute accent and “effektívne” with two F. Date 25 and month januára are clear. It is an “Úradný záznam” instructing that this telegram be sent to the Slovak legation in Bucharest, signed Holák. The ciphertext record says received 19.I.1944 at 1530. Portal date 1943-01-19 conflicts with its name 80102/1944 and these physical 1944 references; metadata was not changed.

Full independent glyph collation, positions numbered from 1:

|Group|Positions|486scan|345scan|345oldwork|
|---:|---|---|---|---|
|1|1–5|HFEBM|HFEBM|HFEBM|
|2|6–10|NIEPE|NIEPE|NIEPE|
|3|11–15|MSDKK|MSDKK|MSDKK|
|4|16–20|EOVMU|EOVMU|EOVMU|
|5|21–25|IEDEE|IEDEE|IEDEE|
|6|26–30|APDLM|APDLM|APDLM|
|7|31–35|EAKVE|EAKVE|EAKVE|
|8|36–40|IFATY|IFATY|IFATY|
|9|41–45|IAOIR|IAOIR|IAOIR|
|10|46–50|NFDNL|NFDNL|NFDNL|
|11|51–55|TVAER|TVAER|TVAER|
|12|56–60|TRRTA|TRRTA|TRRTA|
|13|61–65|ULOAJ|ULOAJ|ULOAJ|


The watermarks cross some letters, but the two independently typed copies support the full sequence without adding or forcing any glyph. No material residual reading ambiguity was found.

An exact **conditional** known-plaintext anagram is available. Normalize the printed words by removing accents, spaces and punctuation, retain double F, and spell 25 digit by digit as **DVE PAT**. Removing first cipher group **HFEBM** then leaves 60 ciphertext letters, exactly the inventory of the 60-letter prepared plaintext, with no missing letters or filler:

`dnadvepatjanuaraideodtialkurierktorymvamposlemeeffektivnelei`

DVE is the Slovak feminine form of two. Its use here is an explicit preparation hypothesis, not an established historical numeric rule. This exact match is unique among all 13 group omissions and the declared numeric variants. H/B occur only in the first group and are absent from this plaintext, providing another indicator constraint for this record. Do not generalize prefix 1 into an indicator-position rule.

`inventory.json` preserves every group omission and no omission under six models, 84 checks total: digits omitted (54 letters), DVA PAT (60), DVE PAT (60), nonstandard DVADSATPAT (64), standard cardinal DVADSIATPAT (65), and ordinal DVADSIATEHOPIATEHO (72). DVA PAT with first group removed misses one A and has one E extra; cardinal alternatives do not match. No source A/E correction was used to obtain the match.

`conditional-pair.json` and the two 60-letter text files preserve the candidate pair for key recovery. Inventory agreement is necessary for pure transposition but does not establish a historical key or prove that DVE was the actual numeric code. The published draft and exact inventory make this stronger than a guessed crib; recovered keys still require full independent inverse and re-encryption. Until then describe it as published plaintext with conditional DVE PAT preparation and first-group indicator hypothesis.

Reproduce: `python3 batches/repeat345-486-sol61/analyze.py`. This checks the manual transcriptions and inventories; it is not OCR or blind key recovery. `manifest.json` contains source/work hashes and crop boxes. Crops use only nearest-neighbor 3× enlargement, no retouch. Original sizes: 486 ciphertext 1024×776, plaintext 1024×593, 345 source 1024×1365. No sources, cipher notes, metadata, markers or register entries were changed.

Root collected all three rendered public HCP486 tabs and actual attachment URLs; this subagent worked offline. Provenance is in `batches/solved-context-main/486/SOURCES.md`: [HCP486](https://crypto.hcportal.eu/dashboard/cryptograms/486), [HCP345](https://crypto.hcportal.eu/dashboard/cryptograms/345), [cipher image](https://api.hcportal.eu/media/1357/conversions/78101655407590-large.jpg), [published archival plaintext](https://api.hcportal.eu/media/1358/conversions/76561655407590-large.jpg).
