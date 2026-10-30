# HCP 1458 (pc_hcp_139): a Morse-stroke postcard to Miss Peggie Lewis, Machen

Human solver: Tomáš Pavuk

**Status: deciphered in full (every stroke group on the card read: 31 letters and one closing sign); independent review 1 verdict ACCEPT, no change to the reading.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1458 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1458), portal name pc_hcp_139, part of the HCPortal collection of cryptographic postcards (private collection). When it was captured on 2026-10-26 the portal listed it as **Not solved**, tagged Postcard, HCPortal collection, category Substitution; Monoalphabetic, date 1904-09-11, language Unknown, location Europe, sender "Sollir", recipient "Peggir Sewis", with no transcription or solution attached.

The picture side is a printed photograph of the actor-manager **Mr. George Alexander** (caption printed on the card). It carries an open greeting in ordinary handwriting, "Kind Regards / Sallie" (the catalogue's "Sollir").

The address side is a British postcard ("This space may be used for communication in the British Isles only"; publisher's line "Series No 1002 Photo Langfier") with an Edward VII halfpenny stamp. The address, in plain writing, reads **Miss Peggie Lewis / Post Office / Machen / (Nr Newpt: Mon.)**, i.e. Machen, a village in Monmouthshire between Newport and Cardiff, South Wales. The communication half of the card holds six lines of black pen strokes, tall and short, grouped and separated by full stops, plus one more group at the foot; a further line of the same kind in faint purple ink runs along the top margin.

The postmark on the stamp is not legible enough to read a day; the date 1904-09-11 is the portal's catalogue date, not a reading by the solver or reviewer. The stamp (issued 1902, in use to 1911) is consistent with it.

![Address side: purple stroke line at the top, six black stroke lines and one closing group in the left half, address to Miss Peggie Lewis, Machen (source/address-large.jpg)](../source/address-large.jpg)

![Picture side: Mr. George Alexander, with the open greeting "Kind Regards / Sallie" (source/picture-large.jpg)](../source/picture-large.jpg)

The large circular alphabet and the "hcportal" logo across both scans are the portal's watermark, not part of the card.

## Method

An earlier triage (2026-10-26, OpenAI GPT solver, GPT-6 Astra / GPT-6.1 Sol) captured the portal metadata and both scans and noted the long/short stroke groups, but established no key or reading. The identification, transcription and decipherment were done on 2026-10-29 by Claude Opus 5.5.

The transcription is **manual**: every stroke group was read on 4–8× enlargements of the address side, the purple line also with its colour isolated from the grey watermark. Each stroke was classed as **tall** or **short** by its height relative to its neighbours; short strokes are typically under half the height of tall ones and sit on the baseline, so the distinction is clear almost everywhere.

The first word gave the key away: a check-mark sign (short then tall), then short-tall-short, then a single short, then a full stop. Read as Morse with tall = dash and short = dot this is A R E, and the next word (tall-short-tall-tall, tall-tall-tall, short-short-tall) is Y O U. The same rule, with no change, turns every following group into English. No letter was supplied from expected wording.

The reproduction script (work/decode.py) checks the SHA-256 of both scans and decodes the transcription file (work/transcription.txt) with the standard Morse table.

In review, a separate Claude Opus 5.5 agent read every stroke group itself from its own 4–7× crops, wrote its reading in its own tall/short notation and decoded it with its own table; its output agreed with the solver's on every line.

## Key

**Morse code written as pen strokes**; there is no secret key:

- tall stroke = dash (–), short stroke = dot (·)
- a visible gap separates letters
- a written full stop ends each word
- letters are the standard International Morse alphabet

| Letter | Morse | Letter | Morse | Letter | Morse |
|---|---|---|---|---|---|
| A | ·– | H | ···· | R | ·–· |
| C | –·–· | I | ·· | S | ··· |
| D | –·· | L | ·–·· | T | – |
| E | · | M | –– | U | ··– |
| F | ··–· | N | –· | V | ···– |
| G | ––· | O | ––– | X | –··– |
|  |  |  |  | Y | –·–– |

Only the letters in the table occur on the card.

## Plaintext

Transcription (dot/dash notation; "/" is a written full stop):

```text
P:  .-.. --- ...- . / -- --- .-.. .-.. .. . /      (purple, top margin)
B1: .- .-. . / -.-- --- ..- /
B2: --. --- .. -. --. / - --- /
B3: -.-. .- .-. -.. .. ..-. /
B4: -. . -..- - / -- --- -. - [blot] .... /
B5: - --- / .... . .- .-. / - .... .. ... /
B6: --. . -. - /
B7: --..-- /
```

Decoded, line for line:

```text
P   LOVE MOLLIE
B1  ARE YOU
B2  GOING TO
B3  CARDIF
B4  NEXT MONTH
B5  TO HEAR THIS
B6  GENT
B7  (closing sign --..--)
```

Editorial reading (punctuation and the second F of Cardiff are editorial):

> Are you going to Cardif[f] next month to hear this gent? — Love, Mollie.

**English:** the text is English already. "This gent" refers to the man pictured on the front, the actor-manager George Alexander, who toured the provincial theatres; Cardiff is the nearest large town to Machen.

**Slovak:** „Pôjdeš budúci mesiac do Cardiffu počuť tohto pána? S láskou, Mollie."

The picture side's plain greeting, "Kind Regards / Sallie", is not enciphered.

## Uncertainties

1. **Line B7.** The group itself (two tall, two short, two tall strokes, then a stop) is clearly written; its *value* is uncertain. In later International Morse `--..--` is the comma, but older tables gave the comma as `.-.-.-`, and since the sentence is a question the writer may have meant the question mark `..--..` (its exact inverse) or simply a closing flourish. The "?" in the editorial reading is an interpretation. Split as letters it would be M I M, which makes no sense here.
2. **Ink blot in MONTH (B4).** A blot sits between the T and the H. No stroke can be seen in it and none is needed: MONTH is complete without it. Nothing was restored.
3. **CARDIF** is written with a single F (`..-.` once, followed by the stop). Reported literally; Cardiff is meant.
4. **The purple line (LOVE MOLLIE)** is faint and partly crosses the grey watermark letters; at high enlargement with colour boost the purple strokes are distinct from the print. This is the weakest part of the card, but solver and reviewer read it the same way.
5. **Who wrote it.** The Morse sign-off says "Mollie", the open greeting on the front says "Sallie" (catalogue "Sollir"). These may be two people (for example Sallie writing with or for Mollie), or "Love Mollie" may mean "love [to] Mollie". The card does not decide it, and the catalogue sender is left as the portal gives it.
6. **Date.** Taken from the portal catalogue (1904-09-11); the postmark day could not be read on the scan.

## Review and what changed

Review 1 (a separate Claude Opus 5.5 agent, 2026-10-30) ran the reproduction command, made its own independent transcription of all eight lines from enlarged crops and decoded it with its own script: identical output. It confirmed that one rule covers every stroke group with nothing left over, that the English is natural for the period and fits the picture and the address, and that no published solution was used. Verdict: **ACCEPT**.

It raised four minor points, all accepted, none changing the reading:

1. B7 should be described as a closing sign of uncertain value, not as a definite comma — done (uncertainty 1).
2. The names Sallie and Mollie should be kept apart and the catalogue sender not "corrected" — done (uncertainty 5).
3. Machen should be described as lying between Newport and Cardiff rather than by a distance from Cardiff — done.
4. The source of the date should be stated, since the postmark is not legible — done (origin section, uncertainty 6).
