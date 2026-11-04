# Notes hcp-1056

2026-11-03: captured by Claude Opus 5.5 (orchestrator).

## 2026-11-03 – Claude Opus 5.5 (solver), status PARTIAL, no marker

Card: Ulm, 10.8.1917, from M. Zwick (soldier, Ulm) to his parents ("Liebe Eltern!"), Herrn Georg Zwick, Erbenschwang, Post Ingenried b. Schongau (Bay.). German Kurrent. Picture side (Ulm, Partie an der Blau) and stamp box: no hidden writing seen (no stamp present; only machine cancels).

Cipher: digit substitution for some letters inside plain Kurrent words; other letters stay plain. Key established on this card and checked on sister hcp-910 (same sender):
1=a 2=e 3=i 4=o 5=u 6=l 7=n 8=m 9=r 0=s (vowels 1-5 in order a e i o u).
Evidence: 237g2g2b27 = eingegeben; 59615b = urlaub; d3029 Tage = "diser Tage" (writer spells "diser" also in plain text: "Habe diser Tage"); 15f d28 = auf dem; 837d = mind.; 910: 2372 k61372 b3tte = eine klaine bitte, 37 59615b k4882 = in Urlaub komme, 74ch = noch.
Transcription and decoding: work/decode.py (`python3 -I ciphers/hcp-1056/work/decode.py`).

Reading so far: "Ulm, den 9.(?) 17. Liebe Eltern! Das mir von Euch zugesandte P?????? m[it] [... under postmark ...] Freude(?) erh-alten, wofür ich mich bestens bedanke. Habe diser Tage um [korchus?] Urlaub eingegeben und werde es Euch gleich mitteilen wann ich fahren kann. Noch 1000 Grüße sowie auch nochmals besten Dank für die Gabe. Schließe nun im besten Hoffen auf baldiges frohes Wiedersehen, sendet Euer dankschuldiger Sohn M. Zwick. Ich war diser Tage auf dem Minster, mind. 778 Stufen."

Why it stops (partial):
1. The word before "Urlaub" decodes k-o-r-?-u-s with a tall double Kurrent sign read as "ch" (as in 910 "74ch" = noch): "korchus" is not a German word I can identify; the leave type is the point of the sentence. Alternatives tried: Kursus, Korps, Vorschuss (needs V; the sign matches the k of 910), Wirtschafts (does not fit the digits).
2. Plain line 2 is crossed by the Ulm postmark and the slogan cancel: the noun after "zugesandte" (shape S/P-r-long-long-e-n; Päckchen? Sachen?) and 1-2 words after "m[it]" are not read; "Freude" is a guess from the visible "-reude".
3. Münster written 8-3-3-7-0-t-2-9 = "miinster" (two 3s read on the pixels; ü probably rendered as i/ii, dialect). 778 is underlined as a real number (the Ulm Münster tower has 768 steps; written figure kept as read). Date day digit not certain.
