# Notes hcp-1175

2026-11-01: captured by Claude Opus 5.5 (orchestrator).

2026-11-01 (Claude Opus 5.5, solver): PARTIAL. No marker. No SOLUTION.md claim of completeness.

Card: plain struck-through Hungarian verse, signed Sz. A., with a boxed digit block above it. Greeting "Kedves Ángyika!" to Szegedi Jánosné; violet "(Margitkám!)" sits under the block, so the digits look meant for Margit Sziber. The later brown strokes are overstrike; the verse is still readable. Plain text (not cipher):
A szellő is csak azt súgja, / Amely tőlem hozzád téved, / A gerle is csak azt búgja: / Mikor látlak újra téged? / Távolban a [vágyam? one word, hyphenated, reading unsure] nekem; / Ha te is itt volnál velem. [boxed:] Légy szíves írjál / mert ....m..... (the dots are on the card, a word withheld) / Sz. A.

Cipher, established by comparing sisters (read only, nothing written there): hcp-1178 note says roughly "ha tudod olvasd el a szám betűt is" (read the number-letters too; words partly under overstrike). Digit plus mark is one sign, so about 30 signs. Punctuation is NOT decoration and NOT word division.
Footholds:
- CSÓKOLLAK: "2,0705,5.1.7" on 1178, repeated on 1174. Gives 2,=cs 0=o 7=k 5,/5.=l 1.=a. Strong: two cards, pattern with the doubled l and repeated o and k.
- ÖLELHET-LEK IS: 1174 "Ha 0,5,1:5,51:8,51:7 2.6, téged". Gives 0,=ö 1:=e 8,=t 2.=i 6,=s, bare 5=h. Weak spot: the "l" of -lek is written bare 5, so writer's slip or my error.
- KEDVESEM: 1174 "7 1:8 3. 1:7, 1:3". Gives 8=d 3.=v 7,=s 3=m.
- SZERET-: 1174 "hogy 7. 1: 3, 1: 8, 1: 8". Gives 7.=sz 3,=r. The sequence reads szeretet with bare 8 at the end, i.e. d/t not fully separated.
- HADIFELSZERELÉS opens 1175: 5 1. 8 2. 4, 1: 4. 7. 1: 3, 1: 5, 1 6, = h a d i f e l sz e r e l é s, 15 signs, and adds 4,=f 4.=l 1=é. Strongest single check on the key: it was not used to derive h a d i e sz r, and the word fits the war date (1915).

Output for 1175 under this key:
hadifelszerelés mal/vél okis omas edir hetekakor a[9]étos[4]ö[1,]lövöddafad
Stops because: "(...) írhetek akkor" ("then I can write") is a tempting read of the middle but needs an unexplained "ed" before it; "okisomas" has no reading; the tail "a[9]étos[4]ö[1,]lövöddafad" reads as nothing, and "lövöd" there would be forced. Signs 9, bare 4 and 1, are unknown, and no n, g, b, j, p, u/ü has been found, though n must occur, so some signs I treat as known likely carry those letters. Homophones (l = 4. 5, 5.; s = 6, 7,) are unexplained, so the mark distinctions may be misunderstood. Only about a third of the card is secure; forcing the rest would be noise-fitting.

Next: a joint attack on all digit passages (1174 top/mid/bottom, 1178, 1179 bottom lines and the top-right group) with a Hungarian word list; none was available locally. 1176 and 1177 show no digits at this resolution. Marks on 1179 are purple-stained and need re-reading. The sister transcriptions above were made for this analysis in scratch and are not filed in those directories.
Files: work/transcription.txt, work/decode_partial.py. Register: no entry (partial).

2026-11-02 (Claude Opus 5.5, solver, second attempt): the old key above was wrong in many values (it forced hadifelszerelés). With the plain hcp-1174 table line 1 gives ha még e?szer el, so 4. = gy and the sentence runs on: Ha még egyszer elindulok és oda nem érhetek akor az uton főblövöm magam. Pixels corrected: L2 sign 4 and L4 sign 1 are .1 (dot left of the 1) = u, by analogy with :1 = ü; L3 last is 9, = z (high comma). Crops in work/rev. Dotted line after "mert": ink isolated, 8 marks, m, 5 marks, no other letters; count fits "főbelövöm magam", recorded as conjecture only. All other open text clear. Files: work/transcription2.txt, work/decode.py. Old transcription.txt and decode_partial.py are superseded. See SOLUTION.md, Revision 2026-11-02.

2026-11-02 (Claude Opus 5.5, solver, after review 1): verdict ACCEPT, five minor findings, all addressed; no sign or word changed. See SOLUTION.md, Response to review 1. Report written. Register entry written on the reviewer's judgement call that the dotted line is one withheld item, not a partial card; drop the entry if the human reads the rule more strictly.
