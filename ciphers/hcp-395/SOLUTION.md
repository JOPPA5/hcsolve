# HC Portal395 — unsolved analysis

No plaintext, key, or decipherment is claimed. No handover marker is warranted.

The immutable image and portal metadata are in source/. A manually made **tentative** transcription is in work/transcription.txt; no transcription was attached on the portal. The cipher type is unknown. R/XQ triple columnar transposition is a contextual hypothesis only, based on the historical paper disclosed in SOURCES.md; it does not provide this telegram's solution.

`python3 ciphers/hcp-395/work/analyze.py` reproduces frequency statistics and initial single-columnar/route attempts from the manual transcription. It does **not** produce a full plaintext from the image. No full decryption command exists yet.

The visible cover note says the Vatican requested repetition of telegrams80213 and80214; their texts were checked, deemed correct, and resent, with a postal error suspected. This note is not evidence that those exact words are encrypted in the body. An English summary is included here for context only; there is no deciphered original-language plaintext or translation to report.

Main unresolved issues: faint characters under watermark; exact header reading; identity of the cipher; key permutations and indicator position/table if R/XQ; all285 ciphertext letters. Initial tests yielded no coherent text. Full details and limits are in NOTES.md and work/analysis.txt. No published solution was encountered, no register entry written, and no DONE or FINAL marker created.

## Continued structural analysis — GPT-6.1 Sol

The scan shows one continuous285letterblock without a physicalsegmentdelimiter. A two-blockRmodel has36possiblegroupboundaries under documentedminimum/maximumlengths; no specificsplit is established. New segmentedsingle-columnar tests (25,114,176evaluations, widths2–7) pass exact200+75lettertwo-blockcontrols but recover no coherenttargettext. Standardtriplecolumnarmathematics also roundtrips280/285letters, so the historic250payloadlimit is contextual rather than mathematical proof of segmentation.

Under the additional hypothesis that395and396share a dailyRindicatorposition/table, jointletter-to-digitconstraints eliminatepositions2/7/9/10/11 and sharplylimit some alignmentpairs:position1only(1,22)/(12,22),position6only(7,19)/(8,20)/(11,20)/(16,7)/(20,11). This remains conditional on tentative395transcription and the shared-keyhypothesis. `work/segment_constraints.py`, `work/split_columnar.cpp` and `work/joint_indicator_constraints.py` reproduce the newchecks. No plaintext/key is claimed.
