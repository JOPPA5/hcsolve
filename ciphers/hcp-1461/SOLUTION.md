# HCP1461 / pc_hcp_142 — partial reverse-alphabet reading

Portal freshly Not solved2026-10-26. Numeric passages use reversed alphabet:
1=Z,2=Y,...,26=A; equivalently plaintext character code91 minus source number.
This gives eight separately labeled excerpts:

```text
SWEETHEART HENRY
WULF
HUSB AND HENRY
SWEETHEART
SWEETHEART SADIE
BAD
WIFE
ORNING [tail only]
```

HUSB AND is split by a physical line boundary; joining it as HUSBAND is an
editorial interpretation, not an additional substitution. The literal words
are retained. Repeated SWEETHEART has identical codes. Henry Wulf matches
the ordinary address and catalogue recipient, supporting the reading without
substituting context for scan validation. No further historical identity claimed.

Ordinary cursive provides context: “Dear Loving” before the first excerpt,
“R.D.” before WULF, “or” before HUSB AND HENRY, “How is my” before another
SWEETHEART, and “cold” after BAD. This is not a full diplomatic prose transcript.
Slovak meanings: „miláčik Henry“, „manžel Henry“, „miláčik Sadie“, „zlý/zlá“.
These are isolated readings, not a complete translated letter.

## Reproduce

From repository root:
`python3 ciphers/hcp-1461/work/decode.py`

No supplied transcript. work/excerpts.json is own manual reading of selected
numeric passages from source/address-large.jpg, labeled by source context.
Script verifies original image/metadata hashes, decodes every stored number
and checks reverse-key roundtrip. These checks do not establish OCR, independent
pixel validation or coverage of all numbers/prose on the card. Original
images unchanged; enlarged crops supplied.

## Unresolved scope

The left-margin addition after ordinary “or” now securely reads WIFE from
4-18-21-22, followed by ordinary cursive Sadie D. Bottom numeric tail
12-9-13-18-13-20 reads ORNING; its first number is obscured (4/14), so the
fullword remains [W/M]ORNING rather than a silently restored MORNING.
These additions bring stored clear numeric coverage to69positions.

Small header and other left-margin/bottom additions remain uncertain, as does
a numerical group after the “my SWEETHEART” passage. No guessed HEALTH or
header quotation is provided as plaintext. Remaining handwritten prose is
not fully transcribed. Whole-message decipherment unproven. Picture has no
observed cipher. All3rendered tabs inspected, no attached/published solution
used. No DONE1/FINAL, report or register entry.

## Second visual pass trace
work/followup-trace.json records accepted added numbers separately from
uncertain header/bottom code alternatives. `python3 ciphers/hcp-1461/work/followup-trace.py`
prints those alternatives without choosing a familiar quotation. Header
first code14/16 gives [M/K]ISS; a current visual candidate for the nextgroup
is REMBE[T/R], not a securely read REMEMBER. No HEALTH reading added.

## Third visual pass: additional positional evidence

The numeric word immediately before cursive “getting” has clear outer codes
`19-22-?-9-2`, giving **HE?RY**. Four additional positions are frozen separately
in `work/ten05-position-audit.json`, bringing clear stored numeric positions
to **73** (69 in the original excerpts plus4 here). The middle code visually
suggests26, which would produce literal **HEARY**, but its second digit crosses
other marks. It remains provisional. Reading HENRY would require13 at that
position; context alone does not justify that change. This is not HEALTH.

Run `python3 ciphers/hcp-1461/work/ten05-position-audit.py` for this separate
positional audit. Its hash checks and deterministic decoding validate the
stored choices, not image recognition. A newly isolated lower-right numeric
addition also remains unsegmented; no familiar phrase is supplied. Header
and bottom prefix alternatives remain unchanged. The whole card is partial.

## Fourth pass (Claude Opus 5.5, 2026-10-30) — still PARTIAL

Earlier passes by the OpenAI GPT solver; this pass re-read all groups on the
pixels. Run `python3 -I ciphers/hcp-1461/work/pass4_decode.py` (reads
work/pass4-readings.json; key n -> chr(91-n)). Established reading of the
numeric words in context (cursive in lower case, decoded in capitals):

> A KISS to REMBET [XXXX]. Dear Lovling SWEETHEART HENRY D. WULF or HUSBAND
> HENRY. How is my SWEETHEART HEARY getting along now. Your SWEETHEART SADIE
> is getting along fine, only I got a BAD cold just now. I can hardly talk
> t… [M]ORNING, that is all for this time. I write more later on. Good bye
> for … Dearie. — How did [H]ONEY dear get HOME last night XX. — (margin)
> … SWEE[…] … or WIFE, Sadie D.

English: the same (a sweetheart's note to her husband Henry Wulf: she has a bad
cold, asks how he got home last night). Slovak: „Bozk na pamiatku(?). Drahý
milujúci miláčik Henry D. Wulf alebo manžel Henry. Ako sa má môj miláčik
Henry? Tvoja milá Sadie sa má dobre, len mám zlú nádchu… ráno… Ako sa
miláčik dostal včera večer domov? Bozky. … alebo manželka, Sadie D.“

Residual / open points: REMBET literal (interpretation "remember" not proven);
HEARY literal (writer slip for HENRY); [M]ORNING restoration under the printed
logo; first code of HONEY blurred; SWEETHEART after "Your" partly overwritten;
inner left-margin numeric line unread after SWEE…; top-left "4-2…" fragment
and diagonal corner note unread; cursive prose transcription is approximate.
Because the inner margin line cannot be read, the card remains partial: no
DONE1, report or register entry.
