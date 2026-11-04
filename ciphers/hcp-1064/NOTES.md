# Notes hcp-1064

2026-11-03: captured by Claude Opus 5.5 (orchestrator).

## 2026-11-03 — solver attempt (Claude Opus 5.5), stopped as PARTIAL

Read source/metadata.md, SOURCES.md; worked on the hires originals in work/hires/
(crops in work/crops/, made with the codex-runtime python/PIL; 180° and 90° rotations
because the card is written in four directions).

Web check: a short search of Klaus Schmeh's blog (scienceblogs.de, Schrödel cards) found no
post about this card (Weiden / Mitterteich / Kögner). The 1918 "Zwick family" cards there
(Roßhaupten, key 1=a 2=e 3=i 4=o 5=u 6=l 7=n 8=m 9=r 0=s) are a different correspondence;
that key was tested here and fails (see below). No sister card in this repo (grep for
Kögner / Mitterteich / Weiden in ciphers/*: none besides this one).

### What the card is
Bavarian picture postcard (clover wreath with a small envelope, verse "Weile ich auch fern von
hier, / In Treue send' ich dieses Brieflein Dir"), 7½ Pf Bavarian stamp, postmark WEIDEN (OPF.)
2?, to "Fräulein Betty Kögner bei Herrn Zehendner(?) in Mitterteich, Bahnhofstraße".
Envelope on the picture: "Bei Staufer(?) / Weiden Bahnhofstr.(?)" (return address, plain).
Most of the message is PLAIN German (Latin hand), written in four orientations on both sides.

Plain text read so far (provisional; several words uncertain):
- Address side, upright: "Weiden 20/5 18. Liebe Babet! Die zwei schön[en] Pfingstf[eiertage]
  müßte ich hier in Den [= dem] Loch verbringen, keine Stunde frei. Da meine ist schon ..."
  continuing in the left margin: "... ich muß manchmal ausrennen(?) von 6-10 ... habe ich auch
  Deine Karte erbekommen(?) ..."; upside-down lines: "Nun(?) für heute grüße ich Dich recht
  herzlich in der Hoffnung, daß wir uns bald wiedersehen. Dein ..."; and further lines
  ("... Ging(?) ... habe nicht ... zusammen ...", "21/26"?) NOT yet read.
- Picture side: "Soeben erhielt[e] ich Deine l[ie]b[e] Karte, danke Dir bestens dafür."
  "Daß mir sehr(?) hoffentlich wird der Krieg bald aus, dann machen wir miteinander Fahrt
  [written 'fart'] in die [struck-out word] weite Fern[e], gelt Babet."
  "Man hat Dein[..] die Jül[..](?)" (unclear) followed by cipher lines; "Dan lassen wir" +
  cipher line; "Viele" + cipher.

### Ciphertext (sign-by-sign, my reading; V = check-mark/root sign, Q = reversed c "ↄ",
X = x with two strokes above "ẍ", B = "⊢"-like sign)
- C1 (picture, under "Man hat Dein / die Jül..."):  3 + V . + V 4 2? 4   (end on the printed clover)
- C2: B 2 5 5 2 4 2 -
- C3: V 6 V Q(with dot) 5 / 2 . 2?
- C4 (after plain "Viele"):  8 4 X 5 6 2
- C5: 6 - 5 + 2 .
- C6 (bottom line, after plain "Dan lassen wir"): 3 + V V 2 4 V 2 + 8 .   then plain(?) "um e.." and "2 - ." under the HCPortal stamp
- C7 (right edge, written downward; direction not certain): - 2 6 V 2 6 V 8 0 V .   (the "26" pairs may be one ligatured sign)

### Hypotheses tested (work/patterns.py: pattern search against the de_DE hunspell stems and the
German UD corpus forms in batches/scoring-sol61/german/source/)
1. MASC, words as written: C2 fits only "bessere" (B=b 2=e 5=s 4=r). Then C4 = ?r?s?e has
   no good word ("Grüsse" needs 5=6), C5 = ?-s+e gives Liste/Küste/Kiste… but conflicts with C4,
   and C6 (pattern a b c c d e c d b f) has NO German match under any V/√ split
   ("sicherheit"/"zerstörten" only if the two V's differ, and neither fits "Dann lassen wir …").
2. C4 = "Grüße" with ß written as two signs 5+6 (s+z): gives 8=G 4=r X=ü 5=s 6=z 2=e, but then
   C5 = z?s?e, C7 = -ezVezV80V: no German. Not confirmed.
3. Vowel digits a1 e2 i3 o4 u5 (hcp-1180 "mock algebra", Zwick-family key): C2 would be
   ?euueoe — impossible. Rejected.
4. Signs + - √ / . as decoration (as on hcp-1180): leaves digit strings with no consonants. Rejected.
5. Reversed / mirror reading of each group: no matches.
6. Alphabet-number readings (a=1…) and arithmetic evaluation of the groups: nonsense.

### Why it stops
No key reads all seven groups; every candidate breaks on C5/C6/C7. The groups are short,
several signs are uncertain (V vs √, the "26" ligature, signs under the clover and under the
HCPortal stamp, and the reading direction of C7), and the plain text around the cipher is
itself only partly read. Neither the cipher nor the whole card is read, so no DONE marker and
no register entry. Next steps for a future attempt: settle the sign inventory at 5x on each
group, read all plain lines (they may name what C6 is: "Dann lassen wir … um …"), then retry
hypothesis 2 with C5 as a signature and C7 read upward.
