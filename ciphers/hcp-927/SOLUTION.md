# hcp-927 (HC Portal 927, cpc_1910-06-19_DE_Graudenz (Grudziadz)_DE_Rendsburg_) - PARTIAL solution

Status: **partial**. No DONE marker. The main Morse message (19 vertical lines) is read in full. The
upside-down Morse postscript along the top edge is read except for its last row tail: about five sign
groups after "84 TAGE" that I could not make into words.

Solver: Claude Opus 5.5 (claude-opus-5-5), 2026-11-03. No earlier solver work exists on this number.
The orchestrator (also Claude Opus 5.5) captured the portal tabs and scans on 2026-11-03. No published
solution was found or used. The portal status is "Not solved" and the portal attaches no transcription
or solution.

## The card

German "Soldatenkarte" (photo postcard sent free of postage, so there is no stamp box), postmark
GRAUDENZ 19.6.10. The address, in clear Kurrent, reads "Soldatenkarte / Eigene Angelegenheit d.
Empfängers / Gefr. Tamb. Pries(?) / 4te Comp. Inft. Regt. No 85 / Rendsburg". It is followed by two
lower lines that I cannot read reliably: "Schwg(?)" and a struck-through word. The surname is partly
covered by the postmark. The picture side is a group photo of soldiers (the drummers and fifers of
II/129, Truppenübungsplatz Gruppe 1910) with painted slogans that are part of the photograph. The
photo carries no handwriting. The left half of the address side holds all the Morse.

## Cipher type and key

Hand-written International (German) Morse code. There is no secret key. German extras: CH `----`,
Ü `..--`, Ö `---.`. ß is written as S + Z (`... --..`), the old "sz" spelling. Other marks:

- slanted stroke after GRAUDENZ = comma
- `//` at the end of line 18 = hyphen (GR= / ÜSZT)
- a dash crossed by a stroke (an "x") at the foot of line 7 = a struck-out element. It is not read.
- line 2's final D (`-..`) is squeezed in beside the foot of line 2 / line 3.

Layout: the main text runs in 19 vertical lines. Each line reads top to bottom, and the lines are taken
from the right edge of the message field towards the left edge. The date 19.6.10 is written in figures
at the foot of line 1. The postscript is 4 horizontal rows along the top edge. They are written upside
down, so you turn the card 180°, read the bottom row first, and read each row right to left (in card
coordinates). Allowed register label: MASC/Morse (not submitted, since this is partial).

## Reproduce (one command, from the repo root)

    python3 -I ciphers/hcp-927/work/decode.py

The command checks the SHA-256 of the 2 source scans and the 2 hi-res originals. It then decodes
`work/transcription.txt` (my own transcription, one Morse letter per token) and prints the result line by
line and as running text. The portal attaches no transcription.

## Plaintext

Main message (complete):

    GRAUDENZ, DEN 19.6.10 / LIEBER FREUND / BEDANCKE MICH HERZLICH FÜR DEINEN SCHÖNEN BRIEF UND
    DEN SCHÖNEN ANSCHNAUZER. DU HATTEST JA RECHT, ABER ICH HAB TROTZDEM EIN PAR TAGE GEWARTET MIT
    DER ANTWORT BIS DIESE KARTEN FERTIG WAREN. ES GRÜSZT FRANZ

Normalised: "Graudenz, den 19.6.10. Lieber Freund! Bedanke mich herzlich für deinen schönen Brief und
den schönen Anschnauzer. Du hattest ja recht, aber ich hab' trotzdem ein paar Tage gewartet mit der
Antwort, bis diese Karten fertig waren. Es grüßt Franz."

English: "Graudenz, 19 June 1910. Dear friend, many thanks for your nice letter and the nice telling-off.
You were right, of course, but I still waited a few days with the answer until these cards were ready.
Greetings, Franz."

Slovak: "Graudenz, 19. 6. 1910. Milý priateľ, srdečne ďakujem za tvoj pekný list a za pekné
vynadanie. Mal si pravdu, ale aj tak som s odpoveďou pár dní počkal, kým neboli hotové tieto
pohľadnice. Pozdravuje Franz."

Postscript (upside-down rows, partial):

    RESEREVE HAT NOCH 84 TAGE  [?...----] [?-...] [?-...] [?.--]

Normalised: "Reserve hat noch 84 Tage ..." ("Reserve" is written with an extra E). This is the soldiers'
countdown to discharge, and it matches the photo's own slogans: "Reserve hat nur noch einige Wochen!"
and "die letzten 100". English: "The reserve has 84 more days ...". Slovak: "Záloha má ešte 84 dní ...".

## Uncertainties (all disclosed)

1. Unread postscript tail (why this is partial). After "TAGE", row 1 holds, in reading order:
   a smeared blot of three dots, then four short dashes, a gap, `-...`, `-...`, a gap, and `.` `--` (or
   `.--`), plus a small comma-like tick. Read as letters, that gives S CH / B B / W (or E M), which is
   not German. I also tried left-to-right reading, element reversal, number forms (full and cut
   numerals), and dot/dash swap. None of them makes words. The blot may be a smeared error.
2. Line 2: a tiny dot (about 9 px, against 20 px for normal dots) touches the E of FREUND. I treat it as
   a pen speck. Counting it would give "FRIUND". A small off-line dot beside the squeezed final D is
   ignored for the same reason.
3. BEDANCKE: it is spelled with `-.-.` C before K. The signs are clear (letter gaps of 50-60 px on
   both sides), so this is the writer's spelling of "bedanke". PAR = "paar", also the writer's spelling.
4. ANSCHNAUZER: line 7 ends `.-` and then has a struck-through element. I read A+NSCHNAUZER across the
   line break. The word sense supports this.
5. FRANZ: its last letter Z (`--..`) is written on a short side line next to the foot of line 19 because
   the writer ran out of space. The long dash of GRÜSZT (about 108 px) is read as T.
6. RESEREVE: row 4 has an extra dot (E) between R and V. It is clearly ink in the row, so I report it
   literally.
7. Several column tops lie on the printed text "Angabe der Nummer auf der Bildseite" and several lower
   elements of the left four lines lie on the printed photographer's imprint. In those places ink and
   print were separated by darkness and shape on 2-3x crops. The postscript's row 3 dashes also overlap
   the printed "Nachbestellung dieser Karte jederzeit unter".
8. Address: the surname "Pries" (portal reading) is partly under the postmark. "Schwg(?)" and the
   struck-through bottom word are unread. They are address details, not message text.

## Why the readings are believed

- The main text is grammatical colloquial German from start to finish. It covers every element in the
  19 lines and has a heading with place and date that matches the postmark (GRAUDENZ 19.6.10). It has
  a salutation (LIEBER FREUND) and a signature (FRANZ).
- "Bis diese Karten fertig waren" refers to the photo postcard itself. The postscript's "Reserve hat
  noch 84 Tage" echoes the slogans painted in the photo.
- Letter and word gaps measured on the scan (letter gap about 40-100 px, word gap about 140-220 px)
  agree with the segmentation used. Blob measurements are in `work/blobs.json` (`work/blobs.py`).

## Files

- `work/transcription.txt` - the transcription; `work/decode.py` - the decoder and hash check.
- `work/blobs.py`, `work/cols2.py` - ink blob detection and column grouping (aid only; every sign was
  checked by eye). `work/strips2.py`, `work/strips3.py`, `work/zoom.py` - rotated column strips used for
  reading. The crops are in `work/crops/`.
