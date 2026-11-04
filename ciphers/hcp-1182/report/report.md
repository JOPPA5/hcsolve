# HCP 1182 (cpc_1909-10-16_DE_Berlin_DE_Lichtenrade_): a Morse love note from Hugo to Anna, Berlin 1909

Human solver: Tomáš Pavuk

**Status: deciphered in full (the 17-line Morse letter and a faint second Morse line along the divider); independent review 1 verdict REVISE, all findings addressed; the second line was added because of the review.** Report dated 2026-11-03.

## Origin and context

The cryptogram is record 1182 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1182), portal name cpc_1909-10-16_DE_Berlin_DE_Lichtenrade_, part of Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-11-03 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, language Unknown, sender Unknown, recipient Anna Kösney, with no transcription or solution attached. No published solution of this card was found (portal, short web search) and none was used.

It is a picture postcard with a studio portrait of a young woman (printed series number "9/18"). The address side carries a German 5-Pfennig Germania stamp with a Berlin postmark. In plain Kurrent handwriting it gives the header **"Lichtenberg. Den. 16.10.09."** and the address **"Fr. Anna Kosney, Lichtenrade, Holz...str. No 34, bei Schreiber[?]"**. Lichtenberg and Lichtenrade are both places on the edge of Berlin. The whole message, 17 lines on the left half of the address side, is written in Morse code in pen. A second, much fainter grey line of Morse runs vertically along the printed divider, written with the card turned 90 degrees.

![Address side: 17 lines of Morse on the left, the faint vertical Morse line just right of the printed divider, plain-text address on the right (source/address-large.jpg)](../source/address-large.jpg)

![Picture side: studio portrait, no writing (source/picture-large.jpg)](../source/picture-large.jpg)

## Method

The transcription is manual and was made from the high-resolution original of the address side (work/hires/, 3468 x 2298 px). The solver read every line group by group from overlapping 2-4.5x crops and recorded it in work/transcription.txt. The writer's conventions are clear from the first line:

| mark | meaning |
|---|---|
| ink dot / short dash | Morse dot / dash |
| thin slanted stroke | end of a letter |
| thin stroke followed by a heavy stroke | end of a word |
| Latin "=" at a line end | hyphen, word continues on the next line |
| horizontal bar over a group | letter doubled (as the Kurrent m-bar = mm): BESTIMMT, SCHLIESSEN |
| long line under groups | underlining for emphasis: "BRINGE BITTE DEN RING MIT" |

The first line decodes at once to LIEBE ANNA K= / OMME DOCH, so the system is German Morse. The faint vertical line was cropped separately, rotated 90 degrees counter-clockwise, contrast-stretched and enlarged 4-5x with the card coordinates marked, and read the same way (work/strip/).

The whole reading is reproduced by one command from the repository root, which checks the hashes of the scans and decodes the transcription:

    python3 -I ciphers/hcp-1182/work/decode.py

## Key

There is no secret key: the text is plain International Morse code with the German letters CH (----) and Ü (..--). The writer has two consistent personal deviations:

- W is written .--. (standard P): 3 times, in WIRD, EWIG, WILL. Standard P never occurs.
- Z is written -.-- (standard Y): 4 times, in ZU, ZEIT, SCHATZ, HERZLICH. Standard Y never occurs.

Under the first use of these unusual signs the writer added small Kurrent glosses: a "z" under the first Z (line 4), a "w"-like mark under the first W (line 6), and a similar mark under the Ü of GRÜST (line 16). Register type: MASC/Morse.

## Plaintext

Decoded, line by line ("=" is the writer's hyphen, "–" the lone dash in line 7):

```text
 1 LIEBE ANNA K=         10 LIEBR SCHAT=
 2 OMME DOCH             11 Z ICH HOFFE
 3 BITTE BESTIMMT        12 STARK AUF DE=
 4 ICH BLEIBE Z=         13 IN ERSCHEINEN
 5 U HAUSE DIE ZEIT      14 NUN WILL ICH
 6 WIRD MIR EW=          15 SCHLIESSEN
 7 IG LANG– B=           16 ES GRÜST DICH HE=
 8 RINGE BITTE           17 RZLICH D HUGO
 9 DEN RING MIT

Vertical line along the divider:  SÜSSER SCHLINGEL
```

German, edited (punctuation editorial):

> Liebe Anna, komme doch bitte bestimmt, ich bleibe zu Hause, die Zeit wird mir ewig lang. – Bringe bitte den Ring mit, lieb[e]r Schatz. Ich hoffe stark auf dein Erscheinen. Nun will ich schließen. Es grü[ß]t dich herzlich D[ein] Hugo.
> Along the divider: Süßer Schlingel.

English:

> Dear Anna, do please come for certain; I am staying at home, time is passing ever so slowly for me. – Please bring the ring with you, dear sweetheart. I very much hope you will come. Now I shall close. Warm greetings, your Hugo. (Lichtenberg, 16 October 1909.)
> Along the divider: Sweet rascal.

Slovak:

> Milá Anna, príď, prosím, určite, zostávam doma, čas sa mi nekonečne vlečie. – Prines, prosím, ten prsteň, drahý poklad. Veľmi dúfam, že prídeš. Teraz už skončím. Srdečne ťa pozdravuje tvoj Hugo. (Lichtenberg, 16. 10. 1909.)
> Pozdĺž deliacej čiary: Sladký šibal.

![The vertical line along the divider, rotated 90 degrees counter-clockwise and contrast-stretched (top: card y 100-1000, bottom: 980-1900). It reads S / Ü / S / S / E / R // S / CH / L / I / N / G / E / L. The heavy dark strokes crossing it belong to the main text; the horizontal rule is the printed divider (report/strip.png)](strip.png)

## Uncertainties

1. LIEBR (line 10): the writer wrote .-.. .. . -... .-. with no E before R; read as "Lieber". A writer's omission, checked at 4x.
2. GRÜST (line 16): a single S, no doubling bar; read as "grüßt" (writer's spelling).
3. Line 7: after LANG stands a lone dash, closed by a word-end pair but not separated from LANG by one. Read strictly it would make LANGT; it is read as a dash (Gedankenstrich) ending the sentence. This rests on sense only.
4. D (line 17): a lone -.. between word strokes before HUGO, read as the abbreviation "D." = Dein.
5. The values W = .--. and Z = -.-- rest on word sense and on the writer's own glosses; they are consistent in all 7 uses.
6. Vertical line: the I of SCHLINGEL shows one clear dot; the other falls at the edge of a heavy main-text stroke, so I (rather than E) rests partly on word sense.
7. Plain-text address: the street is read only as "Holz...str. No 34"; "bei Schreiber" is an uncertain Kurrent reading. The surname reads Kosney (portal: Kösney). A pencil mark over the printed "Correspondenz-Karte" lines is probably a dealer's or collector's code.
8. The stamp is still on the card, so writing under it cannot be excluded. The picture side shows no writing at the available resolution.

## Why the reading is correct

Every one of the 17 lines and the vertical line decode to German without any free choice: the only non-standard values (W, Z) are forced by the words and used consistently; word strokes and line hyphens fall exactly at German word and syllable boundaries. The text is a coherent, idiomatic love note of the period ("die Zeit wird mir ewig lang", "ich hoffe stark auf dein Erscheinen"), and the vertical line is a fitting affectionate postscript. The date 16.10.09, the Berlin postmark and the Lichtenberg/Lichtenrade places agree.

## Review and what changed

An independent reviewer (a separate Claude Opus 5.5 agent) re-ran the command, decoded the transcription with its own Morse table and re-read all 17 lines on its own crops of the scan; it agreed with every group of the main text. Its verdict was **REVISE**, with four findings:

1. **Blocker**: a faint second line of Morse along the divider had not been transcribed. The solver then read it on rotated 4-5x crops: **SÜSSER SCHLINGEL**. It was added to the transcription, the decoder, the plaintext and the translations. The reviewer's tentative group sequence agreed except at one letter (three dots, S, not four).
2. **Minor**: in line 7 there is no word stroke between LANG and the lone dash. The transcription was corrected, and the dash reading is now marked as resting on sense.
3. **Minor**: the type label. The vertical line is written openly on the address side in the same Morse and is visible on the plain scan, so it is a margin postscript, not a concealed message. The label stays MASC/Morse.
4. **Minor**: the street suggestion "Holzmarktstr." (a central Berlin street) was withdrawn; the address stays "Holz...str. No 34".

The main reading did not change.

## Credits

Capture of the portal tabs and scans, transcription, decipherment and this report: Claude Opus 5.5 (Anthropic), 2026-11-03. Independent review: a separate Claude Opus 5.5 agent. No earlier solver work exists on this number.
