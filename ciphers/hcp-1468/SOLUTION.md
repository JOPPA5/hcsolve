# HCP1468 / pc_hcp_149 — partial Morse reading

Fresh Not solved2026-10-26. Standard International Morse, A=.-,B=-...,
etc., directly reads these separately frozen excerpts:

```text
ADDRESS SIDE:
SO GLAD YOU ARE
STUDYI
MORSE

PICTURE SIDE, PREFIX:
WAS THIS ONE
UP WITH THE FLEET
```

Address likely says “So glad you are studying Morse”; STUDYI is followed
by a repaired/overlapping region, with --. (G) inserted above under a curved
stroke. N is not securely isolated, so STUDYING is not represented as a
complete unambiguous token transcript. Bottom address-side groups also
remain unresolved in segmentation, possibly initials or a continuation.

Slovak of the clear parts: „Som rád/rada, že … Morseovu abecedu.“;
„Bola táto [loď] s flotilou …?“ The bracketed ship reference is contextual,
from printed HMS Resolution caption; no identification of a real fleet
event is established. This is partial text, not a finished translation.

## Reproduce excerpts

From repository root:
`python3 ciphers/hcp-1468/work/decode.py`

No supplied transcription. work/address-excerpts.txt and work/picture-prefix.txt
are own manual dot/dash readings from the two original scans. Script checks
source hashes and standard-code inverse roundtrips for the frozen excerpts.
This is not OCR or independent scan validation, and deliberately excludes
unsettled marks rather than manufacturing a complete message.

## Unresolved

Address-side inserted/corrected region, final address-side groups, end of
picture-side second line and picture-side third line need full transcription
and spacing analysis. Do not silently complete a place name from the expected
naval context. Working side-by-side enlarged crops supplied. Original scans
unchanged. Printed captions/address/postmark excluded from cipher count.

All3rendered tabs read; no attached/published solution encountered or used.
No full-message claim, DONE1/FINAL, report or register entry.

## Additional scan-led check, 2026-10-26

A second solver pass froze the first four groups of the picture-side bottom
row as `-. . .-.. -.-.`, literally **NELC**. This extends the directly
transcribed material by four letters, to 51 positions overall, but supplies
no defensible English place name. In particular, the third group has one
dash and three dots (`.-..`, L); replacing it with W (`.--`) merely to form
NEW would change the observed marks. The following C is `-.-.`. The remaining
right-hand marks still need segmentation; no NEWCASTLE completion is claimed.

Reproduce this separate check with
`python3 ciphers/hcp-1468/work/agent-remaining-check.py`.
Approximate original-pixel coordinates are recorded in the script and a
bottom-row enlargement is `work/agent-picture-line3-large.jpg`. This is a
manual reading by another solver subagent, not the independent review required
for acceptance. Address terminal alternatives TRJF/CJF are reproduced without
choosing an expanded signature. No reliable N was isolated in the correction
following STUDYI. The cipher remains partial, without a handover marker.

## Fresh boundary check, 2026-10-26

The next picture-side bottom-row run was inspected again at native resolution
and enlarged. Six dot-like marks have approximately uniform centre spacing;
two thin crossing strokes leave cancellation/boundaries uncertain. The script
`python3 ciphers/hcp-1468/work/ten-boundary-check.py` lists all 29 ways to divide
six preserved dots into the standard E/I/S/H codes. It shows why a fluent
completion cannot be selected from this run alone. In particular, HI is only
one possible division; HIT is not claimed. Approximate manual pixel centres
and fresh crops are in work/. This adds an explicit ambiguity audit, **zero
new frozen plaintext letters**, and leaves the whole message partial.

## Update 2026-10-30 (Claude Opus 5.5) — still PARTIAL

Full literal transcription of every Morse mark now in
`work/claude-literal-transcript.txt`; run from repo root:
`python3 ciphers/hcp-1468/work/claude-literal-decode.py` (checks hashes), output:

```text
ADDRESS:  SO GLAD / YOU ARE / STUDYI[x] (+ inserted G) / MORSE / C JF
PICTURE:  WAS TSIS ONE / UP WITH THE FLET|TE / NELC H|E|E T?
```

Corrections to the excerpts above: the picture side literally has T S I S
(three dots, not four, after T) and F L E T (one E dot, not two); "THIS" and
"FLEET" are intended readings requiring dropped-dot writer errors. The sign
after STUDYI is obscured by a smudge on the divider line (N would be a
restoration). Address signature literally C J F (initials?).

Probable intended text: "So glad you are studying Morse. C.J.F." /
"Was this one up with the fleet ...?" — the end of the question
("T E/N" after a slash, then "NELC HEET?") yields no English and is left
undeciphered; see NOTES.md 2026-10-30 for what was tried. Earlier work by
the OpenAI GPT solver (GPT-6 Astra / GPT-6.1 Sol) is credited.
