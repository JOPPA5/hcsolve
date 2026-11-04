# HCP 1090 (cpc_1911-04-01_DE_Oppenau_DE_Goggingen_): a Morse love note from Anna to Ernst, 1911

Human solver: Tomáš Pavuk

**Status: deciphered in full (16 Morse columns, every mark accounted for; one word emended on sense); independent review 1 verdict ACCEPT, four minor findings addressed, reading unchanged.** Report dated 2026-11-03.

## Origin and context

The cryptogram is record 1090 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1090), portal name cpc_1911-04-01_DE_Oppenau_DE_Goggingen_, part of Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-11-03 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, language Unknown, sender Unknown, recipient Ernst Häusler, with no transcription or solution attached. The only reference given is the HistoCrypt article on the collection (https://ecp.ep.liu.se/index.php/histocrypt/article/view/166).

The card is a picture postcard of the Titisee in the Black Forest. It was posted at **Oppenau** (Renchtal, Baden) on **1 April 1911** and addressed to "Herrn Ernst Häusler (Eisenb. Assist.), Göggingen, Amt Meßkirch, Baden", a railway assistant in a village in southern Baden. The stamp is a Germania 5 Pfennig of the Deutsches Reich, cancelled at Oppenau.

The whole left half of the address side is filled with pen dots and dashes in vertical columns. Along the dividing line there is a short plain note, "31. III. 11. ab. 9 U[hr]" (31 March 1911, evening, 9 o'clock; the end is cut by the card edge), one day before the postmark. The address and this note are ordinary handwriting.

![Picture side: Titisee (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side as scanned: Morse columns on the left, address and stamp on the right (source/address-large.jpg)](../source/address-large.jpg)

**Search for hidden writing.** The picture side shows no handwriting and no hidden marks. Nothing is written around or along the edges of the stamp; what may lie under the stamp cannot be examined from the scans. No published solution of this card was found by a short web search, and none was used.

## Method

The Morse half of the high-resolution address scan was turned 90° anticlockwise, so that the writer's columns become horizontal rows. Every row was read mark by mark from enlarged strips (3–5×), and the transcription was typed into work/transcription.txt (one line per column, letters separated by spaces). An automatic ink-mark detector (work/blobs.py, work/verify_marks.py) was used as a cross-check: in eight columns it agrees mark for mark with the hand transcription; the remaining differences were each inspected on enlargements and are detector artefacts (a blotted dash, a large round dot, the grey insertion loops, the printed publisher logo and the "Titisee" imprint, the card edge).

A trial decode of each column with German Morse gave German words at once (LIEBER ERNST in the rightmost column, "AUF DA" followed by "S WIEDERSEHEN" in the next column to the left), which fixed the reading order: **columns from right to left, each top to bottom**. Words run across column ends (JET|ZT, S|O, LANGWEIL|IG, BA|LD, DA|S).

![Morse half turned 90° anticlockwise: the writer's columns as rows, first row = first line of the text; the two grey insertion loops and the small grey handwritten letter are visible (review/work/rot_small.png)](../review/work/rot_small.png)

The reproduction command, run from the repository root, checks the SHA-256 of the scans and prints the literal letter stream and the edited plaintext:

```text
python3 -I ciphers/hcp-1090/work/decode.py
```

## Key

German Morse code of the period, with one personal habit of the writer:

| Sign | Value | Note |
|---|---|---|
| ..... | H | standard Morse for the digit 5; used for H in all six places (GEHT, HIER, VIERZEHN, SEHR, WIEDERSEHEN, HERZLICH); the four-dot H never occurs |
| ---- | CH | German Morse (DOCH, SCHÖN, ICH, MICH, DICH, HERZLICH) |
| .-.- | Ä | German Morse (WÄREST) |
| ---. | Ö | German Morse (SCHÖN) |
| all others | standard | international Morse letters |

Two letter groups were added later in lighter grey ink inside small insertion loops: ---- (the CH of the first ICH) and ..... (the H of VIERZEHN). They supply exactly the letters missing at those points. One letter is written in ordinary Kurrent handwriting instead of Morse (see Uncertainties). No word spaces are visibly wider than letter spaces, so word division is editorial. Register type: MASC/Morse.

## Plaintext

Transcription and literal decoding, column by column in reading order ({...} = Morse inside a grey insertion loop; [u] = a Kurrent letter u written in plain script):

```text
c15 .-.. .. . -... . .-. / . .-. -. ... -               LIEBER ERNST
c14 .-- .. . / --. . ..... - / . ... / -.. .. .-.       WIE GEHT ES DIR
c13 --- / .-- .-.- .-. . ... - / -.. ..-                O WÄREST DU
c12 -.. --- ---- / ..... .. . .-. / .-- .. .            DOCH HIER WIE
c11 ... ---- ---. -. / .-- .- .-. / . ...               SCHÖN WAR ES
c10 ...- --- .-. / ...- .. . .-. --.. . {.....} -.      VOR VIERZEHN
c09 - .- --. . -. / ..- -. -.. / .--- . -               TAGEN UND JET
c08 --.. - / .. ... - / . ... / -- .. .-. / ...         ZT IST ES MIR S
c07 --- / .-.. .- -. --. .-- . .. .-..                  O LANGWEIL
c06 .. --. / -.- --- -- -- . / -... .-                  IG KOMME BA
c05 .-.. -.. / .. {----} / ..-. .-. . ..- . / -- .. ----  LD ICH FREUE MICH
c04 ... --- / ... . ..... .-. / .- ..- ..-. / -.. .-    SO SEHR AUF DA
c03 ... / .-- .. . -.. . .-. ... . ..... . -.           S WIEDERSEHEN
c02 .. ---- / --. .-. [u] ..... ... . / -.. .. ----     ICH GRuHSE DICH
c01 ..... . .-. --.. .-.. .. ---- / -.. . .. -. .       HERZLICH DEINE
c00 .- -. -. .-                                          ANNA
```

Literal letter stream (word division editorial):

```text
LIEBER ERNST WIE GEHT ES DIR O WÄREST DU DOCH HIER WIE SCHÖN WAR ES VOR
VIERZEHN TAGEN UND JETZT IST ES MIR SO LANGWEILIG KOMME BALD ICH FREUE
MICH SO SEHR AUF DAS WIEDERSEHEN ICH GRuHSE DICH HERZLICH DEINE ANNA
```

German, edited (one emendation, GRuHSE to GRÜSSE; punctuation added):

> Lieber Ernst! Wie geht es dir? O wärest du doch hier! Wie schön war es vor vierzehn Tagen, und jetzt ist es mir so langweilig. Komme bald. Ich freue mich so sehr auf das Wiedersehen. Ich grüße dich herzlich, deine Anna. (Plain note: 31. III. 11. ab. 9 U[hr])

**English translation.** Dear Ernst! How are you? Oh, if only you were here! How lovely it was a fortnight ago, and now I am so bored. Come soon. I am looking forward so much to seeing you again. I greet you warmly, your Anna. (Written 31 March 1911, 9 p.m.)

**Slovak translation.** Milý Ernst! Ako sa máš? Ach, keby si tu bol! Aké to bolo krásne pred štrnástimi dňami, a teraz sa tak nudím. Príď čoskoro. Tak veľmi sa teším na naše opätovné stretnutie. Srdečne ťa pozdravujem, tvoja Anna. (Písané 31. 3. 1911 o 21. hodine.)

## Uncertainties

1. **GRÜSSE (column c02).** After G R the writer left a gap and wrote a small letter in grey ink in ordinary handwriting: a Kurrent u with a single curl above it (the u-hook, not two umlaut dots). It is read as ü only from sense; the writer apparently did not know the Morse sign for Ü. The next groups are ..... ... . and, as ..... is the writer's H everywhere else, the literal reading is GRuHSE. "Ich grüße dich herzlich" is certain from sense, so the five-dot group is taken as a slip for S. This word rests on word sense. If the grey mark were an unrelated later annotation, the word would still be GRÜSSE.
2. **G of TAGEN (c09).** The first dash of --. ends in a heavy ink blot with no gap; it is read as one dash. A split into -. -. (TANNEN) would need a gap that is not there, and "vor vierzehn Tagen" requires TAGEN.
3. **R of DIR (c14)** is written beside the foot of the column because the column reached the card edge.
4. **Last CH of MICH (c05):** the fourth dash sits at the card edge, short but visible.
5. **Signature ANNA (c00):** the letters are crowded; .- -. -. .- is the only split that gives a name. The sender's surname is not given.
6. A tiny faint speck (about a fifth of a dot) just before the five-dot H of GEHT was judged a pen touch and not counted; counting it would give six dots, which is no Morse sign.
7. Word division and punctuation are editorial. Under the stamp could not be examined.

## Why the reading is believed correct

Every Morse mark on the address side is used, with no leftover groups, and all sixteen columns decode into continuous, grammatical German of the period with the expected opening (Lieber Ernst), closing (ich grüße dich herzlich, deine Anna) and signature. The key has no free parameters: it is standard German Morse plus one consistent personal habit (five dots for H). The two later insertion loops supply exactly the letters missing at those points, which confirms both the reading order and the five-dot H. The places fit: Oppenau and Titisee are in the Black Forest, the addressee is a railway assistant in Göggingen (Amt Meßkirch), all in Baden, and the plain date note agrees with the postmark.

## Review and what changed

The independent reviewer (a separate Claude Opus 5.5 agent) cropped and rotated the scan itself, read all sixteen rows mark by mark, and decoded them with its own script using only standard Morse (review/work/my_decode.py). Its mark sequence is identical to the solver's in all sixteen columns; the only difference is that its decoder prints the five-dot sign as the digit 5. It also confirmed the reading order, the insertion loops, the TAGEN blot, MICH, DICH (running through the printed publisher logo), the ANNA split and the date note on enlargements. Verdict: **ACCEPT**, with four minor findings, all addressed:

1. The five-dot sign is now described as the standard Morse digit 5, used by the writer in place of H.
2. The grey handwritten letter is now decoded literally as u (Kurrent u-hook), giving the literal stream GRuHSE; ü and the emendation GRÜSSE are marked as resting on sense.
3. The stray speck before the H of GEHT is now disclosed.
4. The report states plainly that nothing is written around the stamp and that under the stamp could not be examined.

The decoded text did not change.

## Credits

Transcription, decipherment and this report: Claude Opus 5.5 (Anthropic), 2026-11-03. Independent review: a separate Claude Opus 5.5 agent. Human solver: Tomáš Pavuk.
