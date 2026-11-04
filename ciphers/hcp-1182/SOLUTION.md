# hcp-1182 (HC Portal 1182, cpc_1909-10-16_DE_Berlin_DE_Lichtenrade_) - solution, round 1 (revised after review 1)

Status: complete reading of both Morse texts on the card (the 17-line letter and the faint vertical
line along the divider, added after review 1), with small disclosed residual points (listed below).
Solver: Claude Opus 5.5 (claude-opus-5-5), 2026-11-03. No earlier solver work exists on this number;
the orchestrator (Claude Opus 5.5) captured the portal tabs and scans on 2026-11-03.
No published solution was found or used: the portal status is "Not solved", it attaches no
transcription or solution, and a short web search (Kosney / Lichtenrade / 1909 / Morse) found nothing.

## The card

Picture postcard (studio portrait of a young woman, printed series number "9/18"), German 5 Pf.
Germania stamp, postmark Berlin. Recipient (address in clear, Kurrent): Fr. Anna Kosney,
Lichtenrade. Header in clear (Kurrent): "Lichtenberg. Den. 16.10.09." The left half of the
address side holds 17 lines of Morse code drawn in pen. A second, much fainter (grey) line of
Morse runs vertically along the printed divider, from the top edge of the card to the bottom,
written with the card turned 90 degrees; it reads SÜSSER SCHLINGEL. The picture side has no writing.

## Cipher type and key

Hand-written International (German) Morse code - no secret key. Signs on the card:

| mark | meaning |
|---|---|
| ink dot / short dash | Morse dot / dash |
| thin slanted stroke `/` | end of letter |
| doubled stroke, second one heavy `//` | end of word |
| Latin `=` at a line end | hyphen (word continues on next line) |
| horizontal bar over a group | letter doubled (Kurrent convention, as m-bar = mm): BESTIMMT, SCHLIESSEN |
| long line under groups | underlining for emphasis ("BRINGE BITTE DEN RING MIT") |

Letters are standard Morse plus German CH `----` and Ü `..--`, with two consistent personal
deviations of the writer:

- W is written `.--.` (standard P) - 3 times: WIRD, EWIG, WILL. Standard P never occurs.
- Z is written `-.--` (standard Y) - 4 times: ZU, ZEIT, SCHATZ, HERZLICH. Standard Y never occurs.

The writer added small Kurrent glosses under the first use of these unusual signs: a "w"-like
squiggle under the first W (line 6), a "z" (3-shaped) under the first Z (line 4), and a similar
mark under the Ü of GRÜST (line 16). They confirm the readings but are not needed for them.

Register type label (from the allowed list): MASC/Morse. The vertical line is not treated as
steganography: it is written openly on the address side, in the same Morse, visible on the plain
scan without processing, and is a tender epithet closing the letter, i.e. a margin postscript, not a
concealed message (not under the stamp, not in the picture).

## Transcription

`work/transcription.txt` (all 17 lines), read by eye from 2-4.5x enlarged crops of
`work/hires/cpc_1909-10-16_DE_Berlin_DE_Lichtenrade__adr.jpg` (crops in `work/crops/`).
The portal attaches no transcription.

## Reproduce (one command, from the repo root)

    python3 -I ciphers/hcp-1182/work/decode.py

It checks the SHA-256 of the source scans and the hi-res original, decodes the transcription with
the key above, and prints line-by-line and running text.

## Plaintext (German, as decoded)

    LIEBE ANNA K=        OMME DOCH            BITTE BESTIMMT
    ICH BLEIBE Z=        U HAUSE DIE ZEIT     WIRD MIR EW=
    IG LANG – B=         RINGE BITTE          DEN RING MIT
    LIEBR SCHAT=         Z ICH HOFFE          STARK AUF DE=
    IN ERSCHEINEN        NUN WILL ICH         SCHLIESSEN
    ES GRÜST DICH HE=    RZLICH D HUGO

    Vertical line along the divider:  SÜSSER SCHLINGEL

Edited (punctuation editorial):

> Liebe Anna, komme doch bitte bestimmt, ich bleibe zu Hause, die Zeit wird mir ewig lang. –
> Bringe bitte den Ring mit, lieb[e]r Schatz. Ich hoffe stark auf dein Erscheinen. Nun will ich
> schließen. Es grü[ß]t dich herzlich D[ein] Hugo.
> Along the divider: Süßer Schlingel.
>
> (Clear text: Lichtenberg, den 16.10.09. Address: Fr. Anna Kosney, Lichtenrade, Holz...str. No 34, bei Schreiber[?].)

English:

> Dear Anna, do please come for certain; I am staying at home, time is passing ever so slowly for me. –
> Please bring the ring with you, dear sweetheart. I very much hope you will come. Now I shall close.
> Warm greetings, your Hugo. (Lichtenberg, 16 October 1909.)
> Along the divider: Sweet rascal.

Slovak:

> Milá Anna, príď, prosím, určite, zostávam doma, čas sa mi nekonečne vlečie. – Prines, prosím,
> ten prsteň, drahý poklad. Veľmi dúfam, že prídeš. Teraz už skončím. Srdečne ťa pozdravuje tvoj Hugo.
> (Lichtenberg, 16. 10. 1909.)
> Pozdĺž deliacej čiary: Sladký šibal.

## Uncertainties and residual points

1. LIEBR (line 10): the writer wrote `.-.. .. . -... .-.` with no E before R; read as "Lieber".
   Clearly a writer's omission, not a reading problem (checked at 4x, `work/crops/z6.png`).
2. GRÜST (line 16): only one S `...`, no doubling bar; read as "grüßt" (writer's spelling).
3. Line 7: after LANG (G closed by a thin letter stroke only) stands a lone dash, followed by a
   thin + heavy word-end pair. Read strictly the group belongs to the word (LANGT); it is read as a
   dash (Gedankenstrich) ending the sentence, which rests on sense only. One sign.
4. D (line 17): a lone `-..` between word strokes before HUGO, read as the abbreviation "D." = Dein.
5. The W = `.--.` and Z = `-.--` values rest on word sense (WIRD, EWIG, WILL; ZU, ZEIT, SCHATZ,
   HERZLICH) and on the writer's own Kurrent glosses; they are consistent across all 7 uses.
6. Clear-text address: the street is read as "Holz...str." (probably Holzmarktstr.; middle letters of
   the Kurrent uncertain; the earlier suggestion "Holzmarktstr." is withdrawn, as that street is in
central Berlin, not in Lichtenrade), the last line as "bei Schreiber" (uncertain Kurrent name). The surname
   reads Kosney (portal: Kösney). A pencil mark over the printed "Correspondenz-Karte" lines
   (letter-like "A A 4" shapes) is probably a dealer's or collector's code, not part of the message.
7. Vertical line: SÜSSER SCHLINGEL reads sign by sign; the I of SCHLINGEL shows one clear dot, the
   other dot falls under a heavy word stroke of the main text, so I (not E) rests partly on word
   sense. Ü is `..--`, as in GRÜST. The line is faint grey (pencil or diluted ink).
8. No hidden writing was seen on the picture side; the stamp could not be lifted, so writing under
   it cannot be excluded.

## Why it is correct

Every one of the 17 lines decodes to German without any free choice: the only non-standard values
(W, Z) are forced by the words and appear consistently; word strokes and line hyphens fall exactly
at German word and syllable boundaries; the text is a coherent 1909 love note (Hugo to Anna) whose
underlined request about the ring fits the context; the header date 16.10.09 agrees with the Berlin
postmark era and the Lichtenberg - Lichtenrade (both Berlin suburbs) addresses.

## Response to review 1

Verdict REVISE; all four findings addressed. Reproduction re-run after the changes
(`python3 -I ciphers/hcp-1182/work/decode.py`): hashes OK, 17 lines unchanged except the line 7
token, and a new block "Vertical line along the divider (second text): SÜSSER SCHLINGEL".

1. Blocker, untranscribed vertical Morse line - fixed. I cropped the strip (hi-res x 1500-1660,
   y 0-2000), rotated it 90 degrees counter-clockwise, stretched contrast and enlarged it 4-5x with
   the card y marked in red (work/strip/w0000.png ... w1800.png, z0.png, z1.png, zR.png, zS.png,
   zA.png ... zE.png; tool work/strip/win.py, zw.py, rot.py). Nothing precedes the first group
   (z0.png: blank paper from the card edge at y ~55 to y ~130). Reading, groups with card y:
   S `...` (135-150) / Ü `..--` (175-315) / S `...` (400-445) / S `...` (520-570) / E `.` (637) /
   R `.-.` (700, 740, 781) // (thin + darker stroke, word end, ~800-815) S `...` (880-922) /
   CH `----` (960-1135) / L `.-..` (1195, 1230, 1258, 1290) / I `..` (dot ~1395 at the edge of a
   heavy main-text stroke, dot 1420) / N `-.` (1480, 1512) / G `--.` (1570, 1610, 1645) /
   E `.` (1708) / L `.-..` (1757, 1787, 1815, 1835) / final stroke ~1860; after that only the main
   text and the card edge. Result SÜSSER SCHLINGEL ("sweet rascal"), added to
   work/transcription.txt as block V01, decoded by work/decode.py, and added to the plaintext and
   both translations. The reviewer's tentative group sequence agrees except at letter 4, which is
   three dots (S), not four (H); the word SÜSSER confirms it. The card is complete.
2. Minor, line 7 word stroke - accepted. Transcription token changed (no `|` between LANG and the
   dash; the decoder now prints "LANG–"), and uncertainty point 3 now says the dash-as-punctuation
   reading rests on sense.
3. Minor, type label - decided on the evidence: the vertical line is an openly written margin
   postscript in the same Morse (see the type section), so the label stays MASC/Morse, not
   MASC + Steganography. The stamp could not be lifted, so writing under it remains unverifiable.
4. Minor, address suggestion - accepted; "Holzmarktstr." withdrawn, the street stays "Holz...str. No 34".
