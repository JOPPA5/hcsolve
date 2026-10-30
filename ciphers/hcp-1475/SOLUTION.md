# hcp-1475 (pc_hcp_156) - solution

Status: complete reading of the only ciphertext on the card; the expansion is an
interpretation of an initialism (see "Uncertainties").

## Card
Picture postcard (windmill, Photochromie series 80 nr. 1956), address side:
"Mrs P. H. Ellis, 50 Eversley Road, Charlton S.E." (London), purple date hand
stamp "11 JUL 1910" (not a postmark; the card has no postage stamp or
cancellation, so it may not have gone through the post). Pencil "£4 50" top right is a later dealer price, not cipher.
The only coded text is one line of nine capitals written up the left margin
(read after turning the card 90 degrees counter-clockwise), ending in a full stop.

## Cipher type and key
Initialism (acronym code): each capital is the first letter of one English word.
No substitution: the letters are the plaintext initials themselves.

| initial | word |
|---|---|
| I | I |
| L | love / loves |
| M | my / me |
| W | wife |
| A | and |

## Ciphertext (transcription, own, from source/address-large.jpg enlarged 4-8x)
`ILMWAMWLM.`  (file: work/transcription.txt)

## Plaintext
English (original): **I love my wife and my wife loves me.**

Slovak: *Ľúbim svoju ženu a moja žena ľúbi mňa.*

## Command (run from repo root; checks source hashes)
```
python3 -I ciphers/hcp-1475/work/decode.py
```
Output ends with: `plaintext : I love my wife and my wife loves me.`

The script checks the source hashes and that each word of the proposed expansion
starts with the transcribed letter; it does not (and for an initialism cannot)
derive the words, which are hard-coded as the proposed expansion.

## Uncertainties
- Transcription: all nine letters are clear on the pixels. Letter 6 has a short
  right leg but has the same M form as letter 3 and the last letter; letter 4 and
  letter 7 are W (four strokes, \/\/). No sign is restored.
- Expansion: an initialism has no key that proves the words. "I love my wife and
  my wife loves me" fits every letter, reuses the same word for every repeated
  letter with the same word or a form of the same pronoun (L = love/loves,
  M = my/me, W = wife), gives the chiastic, grammatical sentence typical of
  Edwardian sweetheart initial-messages, and suits a card addressed to a
  married woman (Mrs P. H. Ellis), perhaps written by her husband. Another
  expansion cannot be excluded in principle, but none as coherent was found.
- Sender is unsigned; "husband" is an inference from the text. Whether the card
  was posted, and by whom, cannot be shown.

## Why I believe it is correct
Only five distinct letters in nine positions, and the repetitions follow the exact
pattern X-L-M-W-A-M-W-L-M of a mirrored "I love my wife / my wife loves me"
sentence; Caesar shifts of the string give nothing readable, so a substitution is
not indicated. The whole ciphertext (9/9 letters) is covered.

## Credits
Source capture (metadata, scans, SOURCES.md) and first provisional reading
"ILYMAMWLM" by the earlier OpenAI GPT solver (GPT-6 Astra / GPT-6.1 Sol), which
also suggested an "I love you"-type initialism but did not expand it.
Re-transcription from the pixels (correcting letters 3-4 to "MW"), expansion,
script and this solution: Claude Opus 5.5, 2026-10-30. No published solution of
this card was found; portal status at capture: Not solved.

## Response to review 1

Verdict ACCEPT; three minor findings, all addressed. The transcription and the
expansion are unchanged.

1. **Command verifies, does not derive** - agreed. work/decode.py now says in its
   docstring and comment that KEY is the proposed expansion, hard-coded; the
   misleading "stem" printout (which stripped "s" for L only) was replaced by a
   plain list of the words used per initial and an explicit "initials check".
   The Command section of this file states the same. Re-run on 2026-10-30:
   hashes ok, `ciphertext: ILMWAMWLM`, `initials check: all 9 initials match`,
   `plaintext : I love my wife and my wife loves me.`
2. **"same word for every repeated letter" overstated** - agreed; now reads "the
   same word or a form of the same pronoun" (M = my twice, me once).
3. **Postmark / husband** - agreed. Re-checked source/address-large.jpg
   (work/reading.jpg): there is no postage stamp and no cancellation; the purple
   "11 JUL 1910" is a plain date hand stamp. The Card section now says so, and the
   writer is described as "perhaps her husband"; who wrote or sent the card
   cannot be shown.
