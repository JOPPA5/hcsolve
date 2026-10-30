# Solver notes

2026-10-26: Fresh three-tab inspection, originals captured. Three vertical columns of dot/dash rows on picture right. Word boxes and arrows establish top-to-bottom order in each column, then next column right. American Morse suspected from spaced-dot O and long-dash L, not ordinary International Morse. Initial reading I GOT IN A ...; whole reading not yet established. No watcher launched, respecting user instruction from the ongoing session.

Follow-up: froze all 137 main-text letter positions in work/transcript.json.
One fixed American Morse key reads all word boxes. I GOT IN A HOLE AND HAD
TO SELL THAT ORCHESTRA CARTOON FOR A DOLLAR ... BROOKLAND YESTERDAY PM ...
WEARING A SKULL CAP ... WONT HAVE THE NERVE TO WEAR IT AT HOME.
L and T lengths and spaced O/R/C/Y must be distinguished. Early unaudited
visual guesses ORCHESTRA suffix, BROOKLYN, AM HERE were rejected after
separate column/end crops: the frozen readings are ORCHESTRA, BROOKLAND,
AT HOME. No guessed name/location was supplied to the decoder.
The cancelled box is unread. Final two rows of six large dots could be
R S, but function/reading not secure; explicitly excluded, no DONE1.
Source hashes and all 137 transcript-to-key roundtrips pass, not pixel proof.

Additional bounded solver pass: terminal dots compared quantitatively by
approximate manual centre coordinates in work/terminal-scope.json. Top-row
horizontal gaps 22/10 pixels vs bottom 15/13 support American R/S under
one-letter-per-row parsing. This is conditional glyph evidence, not proof of
initials, signature or decoration. Kept 137 frozen main letters unchanged.
Cancelled box enlarged separately: diagonal crossing ink overlaps dark
horizontal and dot-like marks; no uniquely defensible original row/word.
New check-terminal-scope.py verifies source hashes, conditional key mapping
and prints gap evidence. No marker, source change, reviewer or watcher.

2026-10-26, ten-agent helper 04: independently viewed original picture and
large terminal/cancelled crops. Replaced manual spacing-only evidence with
native-pixel connected-component measurements, compared against R in
WEARING, R in WEAR and S in SKULL. Script measure-terminal-pixels.py checks
source hashes and saves all seven threshold outcomes, including failed
component counts at90/100. At110..150 terminal upper gap ratio2.169..2.213,
control R2.062..2.324, terminal lower1.113..1.129, controlS0.808..0.845.
No claim that ratios alone establish intended alphabetic function. The
cancelled box is still mixed underlying/cancellation ink; no cancelled
word recovered. Main137letters unchanged; no DONE, watcher or reviewer.

## 2026-10-29 — Claude Opus 5.5 (solver), completion
Cancelled box = hatched false start; terminal dots ". .." / "..." =
American Morse R S, signature initials. Register re-checked (357, 1453
absent). Watcher + DONE1.
