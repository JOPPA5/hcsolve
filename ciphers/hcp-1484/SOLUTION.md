# HCP 1484 / pc_hcp_165 — solution (round 1)

Portal status when captured (2026-10-26): Not solved; no transcription or
solution attached; no published decipherment of this card found or used.
Postcard "Pictorial Comedy" (James Henderson & Sons, London), picture "The
turning of the Tide"; portal date 1908-01-30. Address (ordinary script, my
reading of the scan): Miss G. Williams, "Baron Hill", York Road, Colwyn Bay,
N. Wales. (`source/metadata.md` has "Bowntree"/"Oak Road" as provisional
readings; the scan shows "Baron Hill" and "York Road" more plausibly. Not used
as a crib.) The picture side carries no cipher writing, only the portal's
watermark.

## Credits

The 2026-10-26 setup (portal capture, SOURCES.md, triage note in NOTES.md) was
done by an OpenAI GPT solver (GPT-6 Astra / GPT-6.1 Sol); it made no
transcription or decipherment. Transcription, identification of the system,
key and plaintext: Claude Opus 5.5, 2026-10-29.

## Cipher type and key

Monoalphabetic substitution with a self-made, systematically built sign
alphabet; word spaces not written; ordinary punctuation kept. The whole
message is written **upside down** relative to the printed card (the "?" marks
and commas only make sense after turning the card 180 degrees); read it rotated.

Construction (every consonant is a vertical stem with 1-3 short horizontal
bars; vowels are geometric shapes):

| Bars on | hang from top: 1 / 2 / 3 bars | stand at bottom: 1 / 2 / 3 bars |
|---|---|---|
| left of stem | B / C / D | F / G / H |
| right of stem | (J) / K / L | M / N / P |
| both sides | (Q) / R / S | T / V / W |

(i.e. left-top = B C D, left-bottom = F G H, right-top = J K L, right-bottom
= M N P, both-top = Q R S, both-bottom = T V W.)

| Shape | Letter |
|---|---|
| circle with central dot | A |
| triangle | E |
| triangle with an inner vertical stroke | I |
| empty square | O |
| square with a `\` diagonal (top left to bottom right) | U |
| square with a `/` diagonal (bottom left to top right), often with an extra short stroke from the top-left corner | Y |

A superscript "2" after a sign doubles the letter (7 cases: LITTLE, BETTER,
LLANGOLLEN ×2, SHALL, HAPPY, ALL — always where English has a double letter).
J (right-top, 1 bar) and Q (both-top, 1 bar) do not occur on this card; they are
filled in from the pattern only. Signs for X and Z are not attested.

Files: `work/transcription.txt` (own sign-by-sign transcription in a
descriptive notation, lines in the writer's order), `work/key.json`,
`work/decode.py`.

## Plaintext (English)

```
MY OWN LITTLE DARLING,
THANK YOU EVER SO MUCH
FOR THE POSTCARD. I HOPE
TO HEAR EVEN BETTER NEWS
IN THE MORNING. WHY A
CARD OF LLANGOLLEN? SHALL
WE GO THERE TOGETHER, SOME
HAPPY DAY, [d] DARLING? I LOVE
YOU, "DEAREST-OF-ALL-THE-WORLD,"
YOUR BOY.
```

Normalised: "My own little darling, thank you ever so much for the postcard. I
hope to hear even better news in the morning. Why a card of Llangollen? Shall we
go there together, some happy day, darling? I love you, 'dearest-of-all-the-
world'. Your boy." ("together" is underlined on the card.)

Slovak: „Môj vlastný malý miláčik, veľmi pekne ďakujem za pohľadnicu. Dúfam,
že ráno sa dozviem ešte lepšie správy. Prečo pohľadnica z Llangollenu? Pôjdeme
tam spolu niekedy v šťastný deň, miláčik? Ľúbim ťa, „najdrahšia na celom
svete“. Tvoj chlapec.“

(Llangollen is a town in Denbighshire, N. Wales, about 50 km from Colwyn Bay.
The sender signs only "your boy"; no identity is claimed.)

## Reproduce (from repo root)

```
python3 -I ciphers/hcp-1484/work/decode.py
```

Checks the SHA-256 of the three files in `source/`, maps every sign through
`work/key.json` (fails on any unmapped sign), prints the plaintext above and
"177 signs, all mapped".

## Uncertainties

1. **Faint sign before "DARLING" (line 8).** After "SOME HAPPY DAY," there is a
   sign in much lighter ink, lower than the line, with a curl below: pixel
   profile shows a stem with three left bars from the top, i.e. the D-sign,
   followed by the normal dark "DARLING". I read it as an abandoned start of
   "DARLING" (pen ran dry, re-inked, rewritten) and print it as `[d]`. It
   does not affect the sense; another reading of this one faint sign is not
   excluded (it is too faint to rule out bars on both sides), and it is not
   counted as part of the message text.
2. **Signs touched by the printed card text** (vertical "Pictorial Comedy …
   James Henderson & Sons, London"): the M of "SOME" (line 7), the final E of
   "LOVE" (line 8) and the final D of "WORLD" (line 9) are partly overlapped by
   printed letters; each is still identifiable from its visible strokes and is
   the only letter that makes the word. No sign was restored from context alone.
3. Word division is mine (the writer left almost no spaces); punctuation is as on
   the card. The hyphens in "DEAREST-OF-ALL-THE-WORLD" and the quotation marks
   around it are on the card.
4. The key letters J, Q are inferred from the pattern; X and Z unknown (none
   needed for this text).

## Why I believe it is correct

- All 177 signs on the card are transcribed and decoded; no sign is left over
  and none is unmapped.
- The key was first found statistically (hill-climbing on a provisional
  transcription gave "THAN… YOU EVER", "IN THE MORNING", "TO HEAR EVEN BETTER");
  then the bar-count/side/anchor structure became visible and every stem was
  re-checked on 10–16× enlargements against it (e.g. L = three bars right/top in
  both L's of LITTLE, D = three bars left/top in DARLING, P = three bars
  right/bottom in POSTCARD and HOPE vs N = two bars in OWN, THANK).
- The resulting key is a clean, regular design (6 × 3 consonant grid plus six
  vowel shapes), not a table fitted sign by sign.
- The text is fluent period English with fitting content: a love letter to a
  young woman in Colwyn Bay that mentions Llangollen, a nearby Welsh beauty
  spot; the picture shows a kissing couple ("The turning of the Tide").
- Repeated words decode identically (DARLING ×2, YOU ×2 plus YOUR, THE ×3, TO/TOGETHER,
  the doubled-letter mark always on a real English double letter).

Sister cards hcp-1483 and hcp-1485 (same addressee and address, early 1908)
use the same kind of signs; they were not used to derive anything here. (See
the response to review 1: hcp-1485 has since been read with the same key.)

## Response to review 1

Review 1 (Claude Opus 5.5, 2026-10-30): verdict **ACCEPT**, three minor findings.
The reviewer's own transcription and independent rule-based decoder agree with
mine in all 177 signs. No letter of the reading changes.

1. **Y glyph description (minor) – fixed.** I re-checked the Y and U squares on
   the reviewer's enlargements (`review/work/y_yourboy.png`, `y_my.png`,
   `y_why.png`, `y_you2.png`): in YOUR BOY the Y squares carry a `/` diagonal
   (with an extra short stroke from the top-left corner, giving a Y-like fork),
   the U square a `\` diagonal. My earlier wording "V from the two top corners"
   was a loose description of the forked variant. The vowel table above and the
   notation comment in `work/transcription.txt` now say U = square with `\`,
   Y = square with `/`, often with an extra stroke from the top-left corner,
   matching hcp-1485. The sign classes (BOXU/BOXY) and the key were already
   right; `python3 -I ciphers/hcp-1484/work/decode.py` re-run after the edit
   gives the same plaintext and "177 signs, all mapped".
2. **Faint sign (minor) – accepted.** Uncertainty 1 is sharpened: the faint
   lighter-ink sign before the second DARLING is too faint to rule out bars on
   both sides of the stem; it is printed as `[d]` only as the most likely
   reading (an abandoned start of DARLING), and it is not counted as part of the
   message text. The report states this.
3. **Sister-card corroboration (minor) – accepted.** hcp-1485 (same addressee,
   "Miss G. Williams", same address) was read separately with the identical
   stroke alphabet and greets "Gwennie darling", which fits the initial G; its
   review 1 verdict is ACCEPT (not yet closed when this was written). This is
   independent support for the key and the addressee reading, and the report
   cites it with that status. Nothing on this card was derived from hcp-1485.
