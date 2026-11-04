# Notes hcp-1184

2026-11-03: captured by Claude Opus 5.5 (orchestrator).

## 2026-11-03 Claude Opus 5.5 (solver) - partial reading, no marker

Card: picture side "Gruss aus Salonichi", dated in plain "8. mai 1897", printed "Verlag des Deutschen Kegelclub in Salonichi";
address side to "Frau Willi Windisch, k.u.k. Marine-Beamtens-Gattin, Triest, Via Capuano", Triest postmark 12.5.97.
Signed in plain Latin cursive "Fritze". No sister card in the repo (grep for Windisch/Triest/Salonichi: none).
Read from work/hires/ pic (3468x2298); crops were made in the scratchpad (and a few in work/crops/).

Cipher: German, monoalphabetic substitution with invented signs, words separated by commas,
an underline under a sign doubles it (ll, ss, mm). Text in 13 main lines + top line + two lines in the
round vignette + one vertical line along the left edge. No stamp on picture side; modern HCPortal
watermark overlaps lines 5-12 at right.

Key established (sign -> plain), each confirmed in several words:
  - (dash) e | + ei | | (stroke) i | S n | ~ l | ~ underlined ll | c (open r-shape) r | : h | x t | = z |
  O (plain circle) a | @ (circle with dot) o | omega-shape au | 7 (hook) b | 7 with dot m | crossed tt st |
  w-shape (rounded) s | w-shape underlined ss | W (double cup) w | e-shape (plain) u | e-shape crossed eu/u |
  cup with dot ch | same underlined sch | dot g | n-shape (round) d | inverted v f | small cup v |
  K-like ck | 2-shaped k | V j | e with two dots ue | o with dots ae | Z-like tz.

Plaintext read (German):
  Mein liebstes Will[?]e[?]l!  (pet name, signs U-shape and 6-shape unexplained)
  Dein liebstes Schreiben heute glücklich erhalten, danke dir herzlichst dafür. Bin hocherfreut,
  dich, mein alles, gesund zu wissen; mir geht es auch schon besser.
  Meine Civilkleider (first sign = second U-shape, see below) schicke nicht, ich [?? ??? - under watermark]
  jetzt noch nicht am Lande. Um einen Teppich zu kaufen brauche ich dessen Länge und Breite,
  schicke mir diese Masse ehestens. Die Sachen habe ich noch nicht erhalten, die
  Wahre Liebe verzeiht alles, [d]rumm bin auch ich dir wieder gut. Sei herzlichst geküsst von deinem Fritze.
  Vignette: und dem kleinen Schatzerl noch viele heisse Busserln dir.  Top: Grüsse mir alle.
  Edge: verbleibe mir recht gesund.

Why it stops (partial):
  1. Line 6 tail: after "ich" the ink under the HCPortal watermark shows roughly "cup-a-r , dot box d s":
     "war bis" fits the sense but the last group (box, d-shape, s) does not match the b and i signs
     seen elsewhere; a whole clause cannot be read from the pixels.
  2. Line 1 pet name W-i-ll-U-e-6-l: the U-shape also appears twice in "?i?il-kleider", so it cannot be
     a single letter for both Civil (c and v); the 6-shape occurs nowhere else. Unread.
  3. Line 10 tail "die" runs into "Wahre Liebe..." - the sentence break is unclear (maybe "die" closes a
     clause continued under the watermark).
  4. Line 11 first sign of "[d]rumm" is under the watermark face; "d" is a restoration by sense.
  The whole-card rule (an unread clause is partial) applies, so no DONE marker.
Steganography check: picture side, edges and vignettes inspected; the edge and vignette texts are the
same cipher, included above. Address side has no cipher.
