# Notes hcp-1286

2026-10-30: captured by Claude Opus 5.5 (orchestrator).

2026-10-30, Claude Opus 5.5 (solver): PARTIAL reading, no marker created. No earlier work on this number; no published solution found.

Cipher: Hungarian monoalphabetic graphic substitution, the Jolánka family key (hcp-1216 legend) with no change. Card: Budapest 62, 10 Jan 1914, to Tóth Jolánka, Jászárokszállás. Signed Feri. Language of the portal record ("Unknown") is Hungarian. The torn stamp is part of the text area: rows run under it.

Method: crop scripts work/crop*.py on the work/hires address scan; crops/w*.png suppress black postmark ink; crops/s*.png are rectified row strips. Letters below are as read; ? marks a doubtful sign; [] is a word-sense supply.

Working literal rows (main block, then bottom rows, then under stamp):
 1 szeretetedesjolankam
 2 kivanomhogyalegjobb
 3 egessegbentalaljasoraim.ami
 4 engemiletcsakmegvagyok
 5 ehetenvoltamaS[a]ndornal   (S[a]ndor: a and first signs lie under postmark letters; "Sándor" rests on word sense + sisters 1216/1217)
 6 esezt hal?ot?am rolahogy   (hal/ot/t under the dome; "és ezt hallottam" is a word-sense reading of faint strokes)
 7 b?ajo?a/?=szebb olvasC=   NOT UNDERSTOOD, see below
 8 mi?hogymegykedesemfel      (first word doubtful; kedesem = kedvesem, v omitted)
 9 jonekpest[re?] h?at? igy? kezdtem   (x 330-560 display under date line and "62" frame: weakest part after row 7)
10 orulnikozeljovobengyak     (zel/jö partly under postmark)
11 rabbanlathatjukegymast     (hat/j partly hidden by "62")
12 deamintlatszik nemlesz
13 belole egyhamar irjo? edes   (the n of irjon is not seen: after o comes e-bars)
14 emlapa? emeg remenyem      (s + em from edes-em; "lapa e még" unclear)
15 hogyfeljonnekpest edesjo
16 lalankam kilvasban? ketker   (Jo-la-lánkám dittography; first word k+dotted sign+lvasban not understood)
17 destdemondakettorefelele
18 tet. 7 de magamba vagyok    (the 7-shaped sign is unexplained; punctuation or false start)
19 fölidezem kepedmertis? ... see below: rows 18-26 are clean pencil
   fölidézem képed / mert is szeretlek en / ojan nagyon teged / [2] mikor hoz mar? veled ossze? / egy boldog szep ora? / mikor forr az ajkunk? ossze / üdvösseges csokba? / jo mulatast kivanok vasar / napsoraitvarom maradok szerato? kedvese feri
Under stamp: [Iste]n vele / [éd]esem ma / dok sze / tö ked / es?e fe / ri csoko / lom szam / talaszor / X
   = Isten vele édesem, ma[ra]dok sze[re]tő ked[v]ese Feri, csókolom számtalanszor. "Iste" and "éd" are not on the visible card (torn stamp); only their row ends are. Row 5 of stamp has an unexplained 9-shaped sign before the final e. The final X under the last stamp row is unexplained.

Sense of what is secure (not a final translation): "Dear sweet Jolánka, I wish these lines find you in best health. As for me, I am just getting by. This week I was at Sándor's and heard from him that ... [row 7] ... you are coming up to Pest, so I began to be glad that in the near future we can see each other more often. But it seems nothing will come of it soon. Write, my sweet ... my hope that you come up to Pest ... two questions, but say the answer to both. I am alone, I recall your image, because I love you so much. When will that one happy lovely hour bring me together with you? When will our lips melt together in a blissful kiss? I wish you a good time, I await your lines on Sunday. Your loving sweetheart Feri. Farewell ... I kiss you countless times."

Why it stops: row 7 (about 20 signs, display x 60-830, y 285-325) has all signs seen but no accepted Hungarian: sign 1 is a 6 or a tall stroke; then a, j, o, ς-or-s, a, tall stroke, arch-with-tail whose loop is hidden by the 9 of the postmark date, then (a)szebb, then o-l-v-a, a left bowl, bars. Candidates "ha jó az idő és szebb", "bajosan", "szebb olvasni" were tried and none fits every sign, so none is adopted. Row 9 x 330-560 is under the date frame; "Pestre", "hát" and "így" are candidates only. Row 16 first word and row 14 "lapa" are also open. By the brief's standard this is more than a small residual, so DONE1 is not created. A next attempt should start at row 7 and row 9, ideally with a higher-resolution or raking-light scan.

2026-11-02, Claude Opus 5.5 (solver), second attempt: everything re-read from work/hires; see SOLUTION.md "Revision 2026-11-02". Crops: work/rev2/, made with /Users/tomaspavuk/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 -I work/rev2e.py NAME x0 y0 x1 y1 SCALE, run from work/ (hires pixel coordinates). Saturation boost plus contrast separates violet pencil from the black postmark far better than the channel subtractions. Chain of reasoning for row 7: ended row 7 on `Λ = (hidden-top wave) =` + row 8 `III ð` gives vala|mi; the C-shaped trace is the lower half of a wave cut by the cancel line. Dead ends: bajosabb (no bowl at the stroke); az eszébe (second b is a clear b); ilyesmi (sign count); olvasam, olvasni; gy for the sign after szebb (no ς form). Row 8: hook + o + S gives ...g o k; alternatives megyok édesem (does not suit "feljönek") and megy ő kedesem. külvesben: küldésben, külön levélben, levélben tested against signs, none fits. New ledger work/ledger-rev2.txt, normalized work/normalized-rev2.txt, command work/decode_rev2.py.

2026-11-02, Claude Opus 5.5 (solver), after review 1 (REVISE): applied all nine findings, see SOLUTION.md "Response to review 1". Ledger and normalized text corrected in place (rows 7, 8, 17, 18, S3, S4). Row 7 re-read at 5x (work/rev3.py, run from work/ with the runtime above; first sign bowl unclear, then a j o s a, stroke, z e s z e b b, loop, l, v, a, hidden, a). Tried again without success: ha jó az idő, az eszébe (the b is clear), olvasni. Status lowered to partial; no register entry.
