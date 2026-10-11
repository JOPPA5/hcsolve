# Published391 context and399 unchanged-repeat collation

The source supports identifying399 as retransmission of telegram80219, whose original is the already Solved portal391. This is contextual attribution to an existing published archival plaintext, not our new decipherment. Full scan collation is complete (49groups/245letters); literal perfect equality is not established because several glyphs remain uncertain under the watermark.

Parent obtained all three rendered portal391 tabs and attachment lightboxes on2026-10-11, preserving provenance in [its SOURCES](../solved-context-main/391/SOURCES.md). The original391 form bears80219 and5.VIII.1944, recipient NADLAC Rumänien. The399 form bears80233 and10.VIII.1944, recipient Timisoara Rumänien. Its prose explicitly says the legation requested80219/44 because indecipherable and that the telegram was repeated “v tom istom znení ako pod č.80219.” Thus the two catalog records represent original and explicit unchanged repeat, despite routing differences.

Published archival draft, read directly from391 plaintext.jpg:

> Intervenuj okamžite,aby Rumuni povolili sem úhradu cez Compte spécial Lei sumy 3.040.810.-RM ,predstavujúcu časť slovenskej kvoty zbrojných dodávok Škodovky,majúcej sa poukázať v smluvnom období,počínajúcom 15.apríla 1944.Telegrafuj.

`plaintext391.txt` preserves the four typed lines and the spelling “kvoty”, “smluvnom”. This paragraph is transcribed from the attached archival clear-text draft. No solved-key recovery or independent inverse has been performed. An English reading is: intervene immediately so Romania permits remittance here through Compte spécial Lei of3,040,810RM, representing part of the Slovak allocation for Škoda arms deliveries during the contractual period beginning15April1944; report by telegram.

`groups.md` and `groups.json` collate every one of49five-letter groups against both images and the old399work transcription. Independently preferred readings agree at239/245positions, with six tentative differences:

| Group |391 preferred|399 preferred|differing position(s) in group|
|---:|---|---|---|
|22|OSAUC|OSEUC|3|
|33|PETTA|PETTE|5|
|38|CEEKM|AEEKM|1|
|43|KJACJ|KJEAJ|3,4|
|46|REHUL|KEHUL|1|

These differences are local source-reading uncertainties, not six established transmission errors. The word “unchanged” does not authorize silently merging the sheets into an artificially exact245letter string. Further shared uncertainties include PJN[L/I]Y, K[A/E]MLO, watermark-obscured secondletter in391 Z[K/L]ETI, and AOUOU/AOHOU. Source glyph alternatives and raw crop boxes are preserved in the table and crop script provenance below. Both sheets favor CRRER over old ORRER and KAMLO over old KEMLO, but both remain separate literal working readings; canonical399 source/work files are untouched.

Header5245 is identical in both. Each has49groups245letters, so the trailing245count agrees physically. There is no printed separator identifying an indicator group. The prefix5 must not be called day or indicator position without additional evidence. Removing one whole group leaves240letters, but this is a hypothetical framing operation; the indicator location is not established by these scans.

Inventory checks (`inventory.json`) explicitly test both preferred readings, every possible one-group omission and no omission, against two declared preparation models only:

- Literal archival alphabetic letters, numbers omitted:184letters. It contains fourZ while either preferred ciphertext contains only threeZ. Therefore this literal normalization cannot be a pure transposition with optional filler, irrespective of which group is removed.
- Spell every decimal digit separately using nula/jedna/dva/tri/styri/pat/sest/sedem/osem/devat:241letters before separator/filler. Closest inventory among tested omissions still misses21requiredletters and has20surplusletters (399,omit33). No exact known-plaintext/ciphertext pair or indicator follows from that near length.

The second check is a disclosed preprocessing hypothesis, not a claim about historical R instructions. Conventional cardinal wording of money/date, use of abbreviations, punctuation, and differences between a draft and text actually submitted remain unresolved. Matching245count alone would not establish the preparation or key. No exact-cover key attack should treat these literals as an established240letter plaintext until preprocessing and inventories are reconciled.

Reproduce full49group/digit inventory collation: `python3 batches/solved-context-sol61/collate.py`. It reads immutable downloaded images only for their hashes and separately typed working text; the image judgments are not automated OCR or a truth oracle. Manifest contains full source hashes and confirms no cipher source modification. Root acquired391 files; this subagent read them offline after native-browser calls hung and were abandoned. No UI/API/download bypass was used by this subagent.

Inspection crops are nearest-neighbor3× enlargements of source pixels, no retouch. Boxes in original1024×1365 coordinates:391ct(170,270,870,565),399ct(295,780,895,1035),391pt(40,140,980,315). Row-detail391 boxes: (245,276,860,310),(245,316,865,353),(245,443,862,478),(245,490,870,558). Row-detail399: (357,785,900,824),(360,825,896,861),(360,932,910,974),(360,971,910,1041).

Provenance links: [portal391](https://crypto.hcportal.eu/dashboard/cryptograms/391), [portal399](https://crypto.hcportal.eu/dashboard/cryptograms/399), [391cipher attachment](https://api.hcportal.eu/media/1088/conversions/78701655400560-large.jpg), [391published archival plaintext attachment](https://api.hcportal.eu/media/1089/conversions/71931655400561-large.jpg). URLs came from parent's rendered attachment lightboxes, never guessed. Portal sender is displayed as “Bukovisnký”; typed signature appears Bukovinský. No marker, register entry, solver novelty claim, or canonical cipher edits were made.
