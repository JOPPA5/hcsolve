# HCP 1073 (cpc_1910-07-13_DE_Aschersleben_DE_Hier_hugocarl-01): a German love postcard to Hugo Carl, Aschersleben 1910

Human solver: Tomáš Pavuk

**Status: deciphered in full; every sign of the message is read. Independent review 1 verdict ACCEPT (four minor findings, no change to the reading).** Report dated 2026-11-03.

## Origin and context

The cryptogram is record 1073 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1073), portal name cpc_1910-07-13_DE_Aschersleben_DE_Hier_hugocarl-01, part of Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-11-03 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, language Unknown, sender Unknown, recipient Hugo Carl, with no transcription or solution attached. The portal links the HistoCrypt paper on the collection (https://ecp.ep.liu.se/index.php/histocrypt/article/view/166). No published reading of this card was found.

The picture side is a printed photograph of a young woman in profile with a pearl net in her hair, inside a round frame, with a publisher mark and "Ser. 115/2". There is no handwriting on the picture side.

The address side carries a 5-Pfennig Germania stamp of the Deutsches Reich, cancelled **ASCHERSLEBEN 13.7.10** (13 July 1910), and the address in plain German Kurrent: **Herrn / Hugo Carl / Hier / Über den Steinen.** "Hier" ("here") means local delivery inside Aschersleben (Saxony-Anhalt); Über den Steinen is a street in the town. The last word of the street is read from the St ligature and the following minims, but the call "Steinen" also rests on the street name existing there.

The cipher message fills the left half of the address side, written sideways: on the scan it runs top to bottom in columns, the rightmost column first. Turned 90 degrees counter-clockwise it reads as eight ordinary lines.

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side as scanned: cipher message on the left, address and ASCHERSLEBEN 13.7.10 cancel on the right (source/address-large.jpg)](../source/address-large.jpg)

![The message turned 90 degrees counter-clockwise, from the hi-res original (work/message_rotated.jpg)](../work/message_rotated.jpg)

## Method

There was no portal transcription, so the message was transcribed by hand from the un-converted high-resolution scan, sign by sign on enlarged, rotated crops (work/transcription.txt, one token per sign). Two features stood out at once: many signs are digits 2 to 9, and the vowels o, u and ü are written as ordinary Kurrent letters. The opening "1000, 5Rüsse u. 8üsse" suggested "1000 Grüsse u. Küsse" (a thousand greetings and kisses), giving 5 = g and 8 = k. The digits then fall into a simple rule: the alphabet without j, starting with c = 1, gives d = 2, e = 3, f = 4, g = 5, h = 6, i = 7, k = 8, l = 9. Eight different digits obey this one rule, which is strong evidence against a forced reading. The remaining letters (r, s, a, n, ch, t, w, b) are written with invented signs (a small triangle, a short hook, a wide inverted V, a dash, a cross, a crossed A-like sign, a double loop, a tall stroke), each found from the sense of the words it occurs in and then checked against all its other occurrences.

Word ends are marked by a slanted stroke under the line (transcribed as commas). The decoder work/decode.py checks the SHA-256 of the four images, decodes the transcription with the key, prints the result and asserts that the word-divided plaintext uses exactly the decoded letters. Command, from the repository root:

    python3 -I ciphers/hcp-1073/work/decode.py

## Key

Simple monoalphabetic substitution (MASC), German.

| Sign | Plain | Sign | Plain |
|---|---|---|---|
| 2 | d | small triangle | r |
| 3 | e | short hook | s |
| 4 | f | s-like sign with two dots (once) | s |
| 5 | g | wide inverted V | a |
| 6 | h, and b (see uncertainties) | dash | n |
| 7 | i | cross | ch |
| 8 | k | crossed A-like sign | t |
| 9 | l | double loop | w |
| tall l-shaped stroke (once) | B | rho-like loop with descender (once) | st |
| o, u, ü | plain Kurrent o, u, ü | 1000 | the number 1000 |

Sign counts on the card: 3 (e) 18 times, dash (n) 16, 7 (i) 13, 2 (d) 11. Every recurring sign keeps one value in all its occurrences, except sign 6.

## Plaintext

Transcription as tokens (rotated card, line by line; R triangle, S hook, Sd dotted s, a inverted V, N dash, + cross, T crossed A, W double loop, B tall stroke, P rho-loop):

```text
{1000} , 5 R ü S S 3 , u . 8 ü S S 3 ,
S 3 N 2 3 T , 2 7 R ,
2 3 7 N ,
2 7 S S 3 9 .
6 o 4 4 3 N T 9 7 + , 6 7 P , 2 u , 5 3 S u N 2 !
W 3 N N , N 7 + T , 2 a N N , 9 a N 5 W 3 7 9 3 , 2 7 + ,
B 7 T T 3 , N 7 + T , S o , u . 2 3 N 8 , 3 7 N
6 7 Sd + 3 N , a N , 2 3 7 N 3 T R u 2 3 .
```

German, as decoded:

> 1000 Grüsse u. Küsse sendet Dir Dein Dissel. Hoffentlich bist du gesund! Wenn nicht, dann langweile dich bitte nicht so u. denk ein bischen an deine Trude.

English:

> A thousand greetings and kisses are sent to you by your Dissel. I hope you are well! If not, then please don't be so bored, and think a little of your Trude.

Slovak:

> Tisíc pozdravov a bozkov ti posiela tvoj(a) Dissel. Dúfam, že si zdravý! Ak nie, tak sa, prosím, tak nenuď a mysli trochu na svoju Trude.

"Dein Dissel" has masculine/neuter "Dein", so the gender of the person behind the name Dissel is not fixed by the text; the Slovak "tvoj(a)" leaves it open. "deine Trude" is feminine. Whether Dissel and Trude are the same person (a pet name and a first name) is unknown.

The text is fluent, idiomatic German of the period, a typical lover's card sent within one town. Spelling as written: "bischen" for "bisschen", a common period form.

## Uncertainties

1. Sign 6 is a homograph. By the digit rule it is h, and it is h in "Hoffentlich" (a large capital form); in "bist" and "bischen" it must be b, since the Kurrent b looks much like a 6. These two b values are word-sense resolutions, coded in decode.py as a small position table, not output of the key rule.
2. The short hook (s) and the inverted V (a) are similar. The a in "an" is clearly a wide inverted V; in "dann" and "langweile" the reviewer found the distinction clear on the scan as well.
3. The rho-like loop occurs only once, in "bist", and is read as one sign for "st"; the dotted s-like sign occurs only once, in "bischen"; the tall stroke occurs only once, as the capital B of "Bitte".
4. "Dissel" is read letter by letter (d, i, s, s, e, l); it is a name or pet name and cannot be checked.
5. The street name "Steinen" in the plain address rests partly on the street existing in Aschersleben.
6. Nothing is written on the picture side or along the edges. The stamp is still on the card, so any writing under it cannot be checked from the scans; no hidden (steganographic) part was found anywhere on the visible card.

## Review and what changed

An independent Claude Opus 5.5 reviewer ran the decoder, made its own rotated crops of the hi-res scan, re-read all eight lines sign by sign and decoded them with its own script, which derives the digits from the rule "alphabet without j, c = 1" instead of the solver's table. Its output is identical to the solver's except that the rule alone gives h where the text needs b (the disclosed sign-6 homograph). It confirmed the transcription against the scan, checked that line 6 ends at the card edge with nothing cut off, and confirmed the sign counts, the street name and the absence of writing on the picture side. Verdict **ACCEPT** with four minor findings:

1. A comment in the transcription file described the writing direction wrongly. Fixed.
2. The Slovak translation gave Dissel a feminine "tvoja", which the German does not establish. Changed to "tvoj(a)" with a note.
3. The decoder resolves sign 6 by a hard-coded position table; this is now stated plainly in the solution and here.
4. The cipher type for the register is MASC; no steganographic part was found, so it is not labelled "MASC + Steganography".

None of these changed a single decoded letter.

## Credits

Transcription, key reconstruction and decipherment by Claude Opus 5.5 (Anthropic) on 2026-11-03, with an independent review by a separate Claude Opus 5.5 agent; no earlier AI work on this card. Card scans from the HC Portal, T. Schrödel collection.
