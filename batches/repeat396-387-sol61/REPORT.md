# Published HCP387 context for HCP396

The original and repeat have eleven groups, 55 letters and the same header 755. Independent scan collation finds 53 agreeing positions and two preferred differences: original 387 group9 CIAAI versus396 CIASI (position44 A/S), and original 387 group11 OORNT versus396 OORMT (position54 N/M). These are source-supported preferred readings with watermark caveats, not changes selected by an inventory or key search. All other groups agree.

|Group|Positions1|387 preferred|396 preferred/old work|
|---:|---|---|---|
|1|1–5|VEPES|VEPES|
|2|6–10|NMONO|NMONO|
|3|11–15|DRTSI|DRTSI|
|4|16–20|UZOIP|UZOIP|
|5|21–25|UJPTA|UJPTA|
|6|26–30|SZTRA|SZTRA|
|7|31–35|CSCNU|CSCNU|
|8|36–40|DWJPM|DWJPM|
|9|41–45|CIAAI|CIASI|
|10|46–50|UJIUI|UJIUI|
|11|51–55|OORNT|OORMT|

Original 387physically bears 80214 and2.VIII.1944, addressed to Sidor at Città del Vaticano. Repeat 396bears 80230 and7.VIII.1944; its note refers to record/telegram 80229/44. Parent obtained public Solved 387 as context after Global Filter 80214. Portal General names 80214/1944, but Description mistakenly says 80124; preserve that discrepancy. This is attributed context, not a new decipherment of an already Solved record.

Preferred reading of the published handwritten draft:

> Podajte šifrou stručnú zprávu
> o situácii a [prečiarknuté: svojej činnosti?]
> možnej činnosti.

The page also has “2) telegram” and addressee Sidor above the message. The uncrossed final word **MOŽNEJ** is preferred at moderate to high confidence: initial m/o, a visible caron over thethird letter, followed by n/e andfinal j. Earlier low-resolution impressions of vašej/mojej were abandoned after enlargement; they are not normalized into the working text. ČINNOSTI is clear. The crossed phrase appears to be “svojej činnosti”, but the multiple deletion strokes and watermark prevent a confident literal transcription; preserve it as tentative and excluded from the preferred final draft. Handwriting.txt records confidence by word. Accents are conventional readings of the forms, not all equally sharp.

PODAJTE and ŠIFROU are legible; the long descending f in šifrou is especially material. The preferred uncrossed plaintext normalizes to50 letters:

`podajtesifroustrucnuzpravuo situacii a moznej cinnosti`

The reproducible file preferred-prepared-plaintext50.txt removes the spaces in this displayed string. No source word was changed to remove F.

No exact pure-transposition inventory follows. Both55-letter ciphertexts contain **zero F**, whereas the readable draft containsone F inŠIFROU. Omitting anygroup and addingXfiller cannot manufacture that missing F. The closest declared preparation uses the preferred final draft with no added X and removes387 group8DWJPM: 50 letters remain, with **one F missing and one P surplus**. DWJPM contains the only W, absent from the draft, but its indicator role remains a hypothesis because the complete inventories still fail.

All 432 inventory cases are preserved: preferred final text, tentative earlier “svojej činnosti” replacement, or both phrases retained (not preferred), each with0–5 terminal X and every group omission or none, on both independent ciphertext readings. There are no exact matches. The closest case is unique and uses387 CIAAI/OORNT;396's preferred readings introduce the additional A/S and N/M differences. This comparison does not justify rewriting396 to an artificial exact duplicate.

Concrete P/F positions, numbered from1, are saved in P-F-locations.json:

- Original and repeat ciphertext P: **3** (VEPES slot 3), **20** (UZOIP slot 5), **23** (UJPTA slot 3), **39** (DWJPM slot 4).
- Preferred plaintextP: **1** in Podajte and **22** in zprávu.
- Preferred plaintextF: **10**, ŠIFROU slot 3.
- If DWJPM is removed, the remaining ciphertext Ps are stillpositions3/20/23inboth whole and 50-letter body; none is selected as a missing F. The P in DWJPM at 39 is removed only under that explicit indicator hypothesis.

All four printed Ps remain P in this batch. The source images support their printed P shapes; there is no physical basis to choose one and change it to F solely for anagram agreement. Word/groupcropcoordinates in P-F-locations.json support further inspection; exact character mapping would require recovered transposition keys. A conditional one-symbol-error known-plaintext experiment could be run separately with the F/P mismatch disclosed, but this batch establishes neither a key nor an exact historical preparation.

Reproduce: `python3 batches/repeat 396-387-sol61/analyze.py`. It verifies manual scan readings/counts, not OCR or blind key recovery. Manifest contains all source/work hashes; originals and cipher files were untouched. Crops use nearest-neighbor enlargement only, no retouch. Mainboxes:387cipher(322,337,836,410),396cipher(343,423,850,493),handwriting(130,230,980,430),3×. Detail boxes: finalword(167,350,394,433),firstline(215,236,963,311),crossed(480,299,918,380),4×;387lastgroups(490,374,740,412),396lastgroups(510,457,764,495),5×. Original images 1024×1365.

Provenance: [public387](https://crypto.hcportal.eu/dashboard/cryptograms/387), [396 repeat](https://crypto.hcportal.eu/dashboard/cryptograms/396), [387 cipher image](https://api.hcportal.eu/media/1076/conversions/51971655400541-large.jpg), [published handwritten plaintext](https://api.hcportal.eu/media/1077/conversions/87251655400543-large.jpg). Actual URLs and rendered three-tab metadata were obtained by root in batches/solved-context-main/387/SOURCES.md. This subagent worked offline; no cipher edits, source edits, markers or register entries.
