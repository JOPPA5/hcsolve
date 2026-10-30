# Triage notes — 2026-10-26

All three rendered tabs read; fresh status Not solved. Neither skip.txt nor markers excluded this item. No watcher or reviewer was started, following the user override.

Picture side shows a racing car and the printed caption “Circuit de la Sarthe. Sortie de St Mars la Brière”. A faint handwritten enciphered message occupies the sky and continues over the lower image, with ordinary French date/time heading. Address side has very faint additional writing in its left half. Several cipher signs resemble numbers or Greek/Latin letters, so an assumed A1Z26 segmentation would be unsafe.

The source was visually inspected in full. This is not a quick clean numeric substitution: faint ink, printed image and watermark complicate distinguishing similar symbols. No manual transcript, verified plaintext or consistent key was obtained. Do not count this as a partial decipherment. No SOLUTION.md or DONE1. Further work should improve contrast in work/ and map glyph positions on both sides before key search.

# Solver pass — 2026-10-30 (Claude Opus 5.5) — PARTIAL, no marker

Earlier triage (2026-10-26, OpenAI GPT solver) captured the sources and left no transcript or key. This pass broke the key and read most of the text. The lower-left lines and the bottom line are too faint at the 1024 px scan to read in full, so the card stays partial.

## Cipher and key (established)
The text is French. Vowels and l, m, n, s are replaced by digits; every other letter is written plain (c, d, p, q, r, t, v, b, f, j, y, x, ç, apostrophes, hyphens and punctuation are kept):
1=a 2=e 3=i 4=o 5=u 6=l 7=m 8=n 9=s (no 0 confirmed).
Anchor words read on the pixels: c47728c2 = commence, 74728t = moment, 629 = les, c45r25r9 = coureurs, 62ttr2 = lettre (three times), 65tt2 = lutte, v459 = vous, 743 = moi, c4t2 = côté, 9p2ct1c62 = spectacle, pr29q52 = presque, d2r4562 = déroule, 9459 729 y25x = sous mes yeux, 28c4r2 = encore.
Context: the card is postmarked 26 June 1906, written at 6 h 30 in the morning. That was the first day of the first ACF Grand Prix on the Circuit de la Sarthe, which is the subject of the picture. The plain heading is probably "Ecorpain(?) – 6H1/2 matin – 26 juin 06" (Écorpain lies on the circuit). The address is Mlle A. Calvet (portal "Galvet"), Institutrice, ...(Mayenne).

## Reading (work/transcript_partial.txt, `python3 -I ciphers/hcp-1448/work/decode_partial.py`)
Je suis en ce moment [bien] intéressé par la lutte qui commence entre les coureurs. Que n'êtes-vous là, à côté de moi, pour jouir du spectacle presque terrifiant qui se déroule sous mes yeux. [... lower-left lines unread ...] reçu votre lettre – Merci! / Encore un [baiser?] de votre [...]

## Why it stops (do not mark DONE)
- Lower-left lines (y≈400–530 px, over the road and the watermark arc) are only partly visible. They show "J'18[...]", "61 58 [..]d48", "[..]1929 p459 v4tr2 62ttr2 q5[..]", and the right end of that line runs into the dark hedge. I could not read them sign by sign, so I did not force words onto them.
- Bottom line under the caption: "28c4r2 58 b13?r29 d? v4tr2 [...]". "baiser(s)" is only a guess, and the end of the line is lost.
- Shape caveats: at this resolution the cipher 9 (s), plain q and plain r are all looped signs with a tail, and I separated them by context. 6 (l) and cursive b look alike. The cipher 2 (e) sometimes looks like 9, which matters for "intéressé" (weak). The opening J looks like the crossed 7 (m). "bien" has one unread middle sign, and "jouir" sits under the watermark.
- Next step: get a higher-resolution scan of the picture side (the portal served only the 1024 px "-large" conversion), then read the lower lines again.
Crops (local background-subtracted: work/local.py; others: crop2/crop4.py) are in work/crops/.
