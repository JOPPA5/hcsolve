# Physical-source audit of HCP350/351 edges and dates

The scans support a stronger common-edge hypothesis than the working transcriptions: preferred independent readings agree18/20at the opening and10/10at the ending. They also contain physical evidence for a March1944 arrival of351. These findings justify source-supported alternatives, not silent transcription/metadata corrections, a proven20-letter header, shared keys, or recovered plaintext.

All original images were inspected:350cryptogram-1.jpg andcryptogram-2.jpg;351cryptogram.jpg. Metadata and source attribution were read. All originals remain unchanged. Inspection crops are nearest-neighbor enlarged original pixels; blue-channel views suppress some blue overprint contrast without inventing strokes. They are derivative inspection aids, not replacement sources. Source hashes and reproducible counts are in comparison.json; `python3 batches/framing-source-audit-sol61/compare.py` reproduces counts against the unchanged working baselines.

## Independent edge readings

| Source region | Preferred direct reading | Disclosed baseline alternative |
|---|---|---|
|350first20|`SOSOL HUJRZ PMQKK EWRTH`|lastletter ofPMQKK is X in workingbaseline|
|351first20|`SOSOL HUJRZ RWQKK EWRTH`|thirdletter ofHUJRZ is U in workingbaseline|
|350last10|`TGKDH HWUTS`|same as baseline|
|351last10|`TGKDH HWUTS`|thirdletter ofTGKDH is M in workingbaseline|

The source-supported differences from baseline are350position15 X→K,351position8 U→J,351position378 M→K. These are preferred readings, not canonical edits.350opening enlargement shows a left stem and two right strokes in the finalK ofPMQKK. Both HUJRZ groups show a narrow right stem/bottom hook in J, unlike their preceding wider U.351TGKDH has the K-like leftstem/diagonal form visible in enlargement; blue watermark still affects this glyph, so M remains disclosed. Source glyph comparisons were made to other letters on each strip rather than selected to maximize overlap.

Unchanged baselines agree16/20at the opening,9/10at the ending, and2/355inside. Preferred edge alternatives give18/20and10/10. The two remaining opening disagreements are positions11–12 (`PM` versus `RW`); the other18opening positions agree. Interior identity is computed from unchanged baselines, not a newly retranscribed whole middle; its two equal positions are global81 and196 and remain subject to other middle glyph uncertainties. The source-preferred alternative must not be combined selectively with baselines to claim a measured canonical ciphertext.

## Physical length and boundaries

350sheet1 has six group rows8,10,10,11,10,10 (=59groups); continuation sheet2 has11,7 (=18). A handwrittenII on sheet2 supports continuation. Total77five-letter groups=385letters.351rows8,11,10,11,10,11,10,6 also total77groups=385letters. Each original puts clear `385` immediately after the addressee and before SOSOL. This agrees with the physical grouped-body length.

350clear addressee reads `HOLAKOVI 385`;351reads `SOLAKOVI 385` (initialS literal, not silently repaired toH).350ends `...TGKDH HWUTS CIEKER 3001 +`;351ends `...TGKDH HWUTS = CIEKER 3002 ++`. These clear signatures, numbers and transmission punctuation lie outside the77cipher groups.350/351message identifiers3001/3002andsameCIEKER signature are directly supported. The terminal = in351 separates the groupedbody from clear signature; it does not mark the lasttwo groups as a separate indicator.

The firstfour groups are ordinary continuous groups on the firstline, with no special delimiter after the20thletter. The lasttwo groups are ordinary groups on the final strip, with no special delimiter before them. No visible source instruction identifies them as unencrypted headers/trailers, cryptographic settings, or an excluded part of385. All three supplied images are telegram forms; no separate explanatory coverletter is present in these attachments. Portal title `Nerozlúštiteľný telegram` is metadata, not a visible instruction to remove a specified prefix. Both85/84service fields differ from body385, but their administrative interpretation must not be invented from their numbers alone.

## Date evidence and its limits

350routingstrip reads approximately `1478 MADRIND 85/84 28 1445 =`; MADRIND is the visible spelling, while Madrid is the location supplied in metadata.351strip clearly reads `1395 S MADRID 1229 85/84 1 2200 =`. The terminal28/1and1445/2200are consistent with service day/time fields; this interpretation is an inference from the forms, not an independently printed calendar date.350portal records1944-02-28;351portal records1944-11-03, both preserved.

351upper-right round postmark, enlarged in351-date.png, favors `2.III44-23`: three narrow strokes are visible after the day2, with no clearly visible crossed X. It is a Bratislava telegraph-office arrival/time stamp, not necessarily the sender's date. The earlier2.XI-like reading remains a low-resolution uncertainty; this audit favors III rather than silently declaring metadata erroneous. No legible handwritten11.IIIor3.XIdate was found on the supplied images.351top handwritten `816/18429` appears a registration reference, not such a calendar date;350top longnumber and continuationII likewise do not establish an additional message date.

Combining the favored2March1944arrival with351service-day1gives a plausible1March1944sending hypothesis, following350's portal28Februarydate. Consecutive3001/3002identifiers strengthen the possibility of temporally adjacent messages. They do not establish a same-day cryptographic key or that both texts share a plaintext. Because an uncertain stamp reading and different administrative event dates are involved, this is explicitly an alternate chronology; portal dates and originalmetadata remain unchanged.

## Concrete next tests supported by this audit

Treat the three disclosed letter alternatives as a fixed source-derived variant set (at most8combinations), not arbitrary cipher correction. Recheck exact common-edge/constant-displacement constraints on those variants before another ring search. Especially compare source-preferred18/20opening and10/10ending as possible prepared framing while keeping the355middle intact and separately disclosed. If such constraints still contradict a shared schedule/key, do not infer that the edge groups are open text: changing stepping, key reset, different plaintext or transcription uncertainty remain possible.

Primary historical research into the actual sender's Madrid protocol may now reasonably focus on lateFebruary/earlyMarch1944 as an alternative toNovember, while preserving both chronological possibilities. No target solution was looked up, no cipher file/metadata/marker was edited, and no watcher or reviewer was used.
