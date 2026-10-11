# Published 365 / repeat 369 physical collation

The records are linked by telegram 80155, but **they are not literal 115-letter duplicates**. Original 365 physically contains 22 groups/110 letters despite header 7115. Repeat 369 contains 23 groups/115 letters. It adds UCNIO as group 3 and prints ONDEX WITPK where original 365 has WITPK ONDEX. All 22 original groups otherwise match the corresponding repeat groups. Full group map is in groups.json; no lost group was invented in the original scan.

Published archival plaintext, directly transcribed:

> Tvojim 72 nepovažujem Tvoju tamojšiu funkciu za dotknutú.
> Podaj ihneď konkretnejšiu zprávu o uzadí a podrobnostiach.

Literal source spelling is Tvojim (no accent visible over I), tamojšiu, konkretnejšiu, zprávu, uzadí. Neither grammar nor modern orthography was used to silently rewrite those words. The second line clearly includes “a” before podrobnostiach. Root downloaded the public Solved 365 draft as context; this paragraph is published archival text, not our new decipherment.

The 369 note says Bucharest requests repetition of 80155; the new form bears 80163 and 3.V.1944. Original 365 bears 80155 and 19.IV.1944. Original 365's header 7115 doesnotmatch its physical 110 letters. These discrepancies matter for any asserted known plaintext/ciphertext pair.

Full source-supported group map, numbered from 1:

|365 group|369 group|literal group|
|---:|---:|---|
|1|1|TTPDZ|
|2|2|IJEUJ|
|3|5|WITPK|
|4|4|ONDEX|
|5|6|VASSK|
|6|7|JATAX|
|7|8|EPONK|
|8|9|EONXO|
|9|10|TOKOZ|
|10|11|MPAAE|
|11|12|XDEAB|
|12|13|UTOMA|
|13|14|UODUZ|
|14|15|DUIHO|
|15|16|UIOSN|
|16|17|SUIXU|
|17|18|ARUVJ|
|18|19|CPUNV|
|19|20|ZRFKI|
|20|21|ADHVJ|
|21|22|TIEMD|
|22|23|TMJVR|

Repeat 369 group 3UCNIOhas no physical counterpart in 365. MPAAE and CPUNV are preferred in both images; old 369 work instead has MPAEE and QPUNV. This batch preserves corrected working alternatives separately without editing old source/work files. The U/N candidate issue was examined at higher magnification: SUIXU final U is supported by the bottom bowl in both sheets, not N. UCNIO begins with preferred U (onlyrepeat copy available). OtherU-containinggroups remain source-supported U. No N was substituted to force the inventory.

No tested preparation gives an exact anagram. `analyze.py` checks 6580 explicit cases: seven numeric models, zero/oneXafter each of two sentences plus 0–4 extra finalXs, original 365 andrepeat 369, and every possible group omission or no omission. Numerical alternatives are digitsomitted, SEDEMDVA, SEDEMDVE, SEDEMDESIATDVA, SEDEMDESIATDVE, nonstandardSEDEMDESATDVA andSEDEMDESATDVE. NFD normalization retains every printed word.

Closest conditional model is repeat 369 withWITPK(group 5)removed, 72 preparedasSEDEMDVA, plusfive X total. It leaves 110 ciphertextletters and 110 plaintextletters but still misses one N and has one U extra. All three ways to placefive Xwithin the declared sentence/filler scheme have the same inventory; inventory cannot choose their positions. These are retained in closest-inventory.json, not presented as exact known pairs. W occurs only in WITPK and not in any declared plaintext, making it an indicator candidate under these hypotheses. Because no exact match exists, **indicator location is not established**. In original 365WITPKisgroup 3; headerprefix 7 mustnotbeinterpretedasindicatorposition.

Original 365 withoutWITPK has 105 letters, whereas this prepared plaintext withfive Xhas 110. Its missing UCNIO and group-order difference cannot be repaired by changing the plaintext. Repeat 369 is a more complete conditional key-recovery input, but the N/U inventory discrepancy and exact X positions remain unresolved. A solver with an explicit one-symbol error model could test these hypotheses; any witness would require independent full encryption, source error disclosure and no claim that the archived draft alone supplies a perfect pair.

Reproduce: `python 3 batches/repeat369-365-sol61/analyze.py`. It does manual-transcription comparison and inventories, not key recovery or automated source recognition. manifest.json records source/work hashes and declared models; inventory.json preserves all cases. Crops use nearest-neighbor enlargement only, no retouch. Maincropboxes (original 1024×1365):365 cipher(367,374,957,530),369 cipher(390,400,878,557),365 plaintext(165,275,986,359),3×. AdditionalUinspection:369 UCNIO(554,408,630,446),365 U groups(370,424,957,491),369 U groups(393,480,875,521),4×;365 SUIXU(450,462,527,493),369 SUIXU(719,482,802,518),8×.

Provenance: [public 365](https://crypto.hcportal.eu/dashboard/cryptograms/365), [369 repeat](https://crypto.hcportal.eu/dashboard/cryptograms/369), [365 cipherimage](https://api.hcportal.eu/media/1017/conversions/42831655400443-large.jpg), [published archival plaintext](https://api.hcportal.eu/media/1018/conversions/89341655400445-large.jpg). Root read all three rendered tabs and observed actual attachment URLs; its SOURCES.md is in batches/solved-context-main/365. This agent worked offline. No cipher files, source pixels, markers or register entries were modified.
