ACCEPT

# Review 1 – hcp-1197 (reviewer: Claude Opus 5.5, 2026-11-03)

## What I verified and how

1. Ran the command from SOLUTION.md: `python3 -I ciphers/hcp-1197/work/decode.py`. All four SHA-256 checks print OK; output
   `DEINEN GELIEBTEN / BRAUTIGAm`, identical to the claimed plaintext.
2. Independent decoder `review/work/verify.py` (alphabet built from string.ascii_uppercase minus J, no shared code):
   J-less numbering gives `DEINEN GELIEBTEN BRAUTIGAM`; full 26-letter numbering gives `DEIMEM GEKIEBSEM BQATSIGAL`.
   The J-less key is therefore forced, and every one of the 24 groups decodes to a real word.
3. Transcription checked sign by sign on the hi-res picture side (work/hires/..._pic.jpg), crops in review/work/
   (line1.png, line2.png, z1.png, z2.png, stampzone.png – autocontrast, 3x):
   - Line 1 `4,5,9,13,5,13 – 7,5,11,9,5,2,` is clean ink outside the collection stamp.
   - Line 1 `19` under the stamp: a slanted stroke runs through the stamp's "C" and a 9-loop sits over the "P",
     followed by a clear `5,13`. The reading is supported by the pixels, as the solver says.
   - Line 2 `2,17,1,20,19,9,7,1,` is clean. The last group starts with a dark "1" just before the stamp ring.
     Inside the stamp's "C" there is a further dark diagonal ink stroke that is not part of the stamp lettering.
     So a second digit exists, but its shape cannot be identified. The `2` is a restoration from word sense
     (BRÄUTIGA_ → M = 12), and the solver discloses it as such (lower-case `m`, `[2]` in the transcription).
4. Pencil capitals along the lower edge (bottom.png): I read "DEINEN" (large) and "GELIEBTEN BRAUTIG", which
   then runs into the stamp. This independent old decipherment agrees with the reading. The solver records it in
   SOURCES.md and SOLUTION.md and does not present it as its own work.
5. Plain Kurrent text: "Gruß aus Frankfurt a/M / sendet dir / dieser kleine Junge hier. / Ungenannt und nur /
   zu gut bekannt. / Liebe Grüße an: / … / und an – – – – / " " Fräulein Schwester". I agree with this reading.
   "Schwester" is partly under the stamp and its middle letters rest on word sense; this is disclosed.
6. Language and context: "Liebe Grüße an: deinen geliebten Bräutigam" is correct accusative German of 1899 and fits
   a teasing anonymous card to a young woman. Address: Fräulein Käthchen Walther, Hofconfection,
   Sachsenhausen, Dreieichstraße 1. St. This is consistent with the Frankfurt-Sachsenhausen postmark.
7. Stamp box and picture side checked for steganography (stamp.png, skirt.png). There is no writing beside the stamp.
   The faint pencil marks on the girl's skirt are illegible at hi-res, which is disclosed as uncertainty 4.

## Findings

1. (minor) The 5 Pf Reichspost stamp is affixed upside down (the "5" and "REICHSPOST" are inverted in stamp.png).
   This may be a deliberate "Briefmarkensprache" signal on a love-teasing card. SOLUTION.md says only "stamp affixed".
   Please note the inverted stamp as a possible stamp-language message, without claiming a meaning.
2. (minor) Date: the large postmark reads 4.2.99, and the cancel on the stamp shows "…4 2 99" with a possible
   leading "1" at the left edge. The portal file name says 1899-02-14. SOLUTION.md half-states this; give one
   explicit date with its uncertainty (4 or 14 February 1899) in the report.
3. (minor) The "pencil decipherment" agrees only up to "BRAUTIG"; the rest is lost at the stamp. It therefore
   does not confirm the restored M. The wording "It agrees with the decoding" should say it covers the text only
   up to BRAUTIG.
4. (minor) Register type: the cipher is plain number substitution (MASC). I found no steganographic part, so
   `MASC` is correct; `MASC + Steganography` is not warranted for this card.

## Could not verify

- The second digit of the last group (hidden by the HCPortal stamp). M is the only letter that completes a word,
  so the restoration is safe, but it is not visible.
- The faint pencil word on the girl's skirt, and anything under the affixed stamp.
- Sender identity (deliberately anonymous).
