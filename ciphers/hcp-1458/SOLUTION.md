# hcp-1458 (pc_hcp_139) – solution

Solver: Claude Opus 5.5 (claude-opus-5-5), 2026-10-29. Earlier triage (2026-10-26, OpenAI GPT solver, GPT-6 Astra / GPT-6.1 Sol)
captured the portal metadata and both scans, noted "long/short stroke groups" and the Machen/Peggie address, but established
no key or reading. The key identification, transcription and decipherment below are new work by Claude Opus 5.5.
No published solution of this card was found or used; the portal status was "Not solved" when captured.

## Cipher type and key

**Morse code written with pen strokes** (a written, not encrypted-by-key, Morse rendering):

- tall stroke = dash `-`, short stroke = dot `.`
- a visible gap separates letters; a written full stop `.` ends each word
- standard International Morse letters; no further key

Category for the register: Morse code (stroke notation).

## Transcription (work/transcription.txt)

```
P:  .-.. --- ...- . / -- --- .-.. .-.. .. . /          (purple ink, top margin)
B1: .- .-. . / -.-- --- ..- /
B2: --. --- .. -. --. / - --- /
B3: -.-. .- .-. -.. .. ..-. /
B4: -. . -..- - / -- --- -. - [BLOT] .... /
B5: - --- / .... . .- .-. / - .... .. ... /
B6: --. . -. - /
B7: --..-- /
```

## Plaintext (English)

Black message (left half of address side):

> ARE YOU GOING TO CARDIF NEXT MONTH TO HEAR THIS GENT ,

Purple line at the top: **LOVE MOLLIE**

Editorial reading: "Are you going to Cardif[f] next month to hear this gent?  Love, Mollie."
"This gent" refers to the actor-manager pictured on the front (printed caption "Mr. George Alexander"). The open-text
greeting on the picture side reads "Kind Regards / Sallie" (or Sollie; catalogue: "Sollir") and is not enciphered.

Slovak: „Pôjdeš budúci mesiac do Cardiffu počuť tohto pána? S láskou, Mollie."

## Command

From the repo root:

```
python3 -I ciphers/hcp-1458/work/decode.py
```

It verifies the SHA-256 of both source scans and decodes `work/transcription.txt` with the standard Morse table.
Output:

```
source hashes OK
P   LOVE MOLLIE
B1  ARE YOU
B2  GOING TO
B3  CARDIF
B4  NEXT MONTH
B5  TO HEAR THIS
B6  GENT
B7  ,
```

## Uncertainties

1. **Line B7** (`--..--`, a lone group of two tall, two short, two tall strokes followed by a stop). In standard Morse this is
   the comma. Because the sentence is a question, the writer may have meant the question mark (`..--..`, its exact inverse);
   this is an interpretation, not a reading. Split as letters it would be M I M, which makes no sense here.
2. **Ink blot in B4** between `-` (T) and `....` (H) of MONTH. No stroke is visible through it; MONTH is complete without it,
   so nothing is restored. A stroke could physically be hidden there, but no letter is needed.
3. **CARDIF** is written with one F (`..-.` once; the next group is the N of NEXT). Reported literally; Cardiff is meant.
4. **MOLLIE**: the two groups after `--` (M) and `---` (O) are each short-tall-short-short (L), then two shorts (I) and one
   short (E). The purple ink is faint and overlaps the grey watermark; the E is a single short slanted stroke followed by a stop.
   Whether "Love Mollie" is a sign-off of a second writer or "love [to] Mollie" cannot be decided from the card.
5. Short vs. tall was judged by stroke length relative to neighbours on 4–8x crops; short strokes are typically under half the
   height of tall ones and sit at the baseline, so the distinction is clear everywhere except where stated above.

## Why I believe it is correct

- One fixed, standard rule (tall = dash, short = dot) turns every stroke group on the card (8 lines, 31 letters + 1 sign) into
  real English with no unused or undecodable group.
- The message is grammatical and fits the context exactly: the card is addressed to Miss Peggie Lewis, Post Office, Machen
  (Monmouthshire), about 13 km from Cardiff; the picture shows the actor George Alexander, whom "this gent" refers to; the
  postmark and portal date are September 1904.
- Every group was read on enlarged crops of `source/address-large.jpg`; no letter was supplied from expected wording.

## Response to review 1

Review 1 (separate Claude Opus 5.5 agent, 2026-10-30): verdict **ACCEPT**; the reviewer's independent transcription and
decode agree with mine on every line. Four minor findings, all about wording; the reading is unchanged.
`python3 -I ciphers/hcp-1458/work/decode.py` re-run on 2026-10-30: `source hashes OK` and the same eight output lines.

1. **B7 is interpreted, not read** – agreed. The group `--..--` is read with certainty; its *value* is not. In later
   International Morse it is the comma, but older tables gave the comma as `.-.-.-`, and the writer may have meant a question
   mark (`..--..`) or just a closing flourish. The report now calls B7 "a punctuation-like closing sign of uncertain value
   (comma / question mark / flourish)" and the editorial "?" is marked as mine. Uncertainty 1 above stands with this wording.
2. **Sender attribution** – agreed. The open greeting on the picture side is signed "Sallie" (catalogue: "Sollir"); the Morse
   sign-off says "Mollie". The report keeps them as two names that may or may not be the same person (or Sallie writing with or
   for Mollie), does not correct the catalogue sender, and the register entry uses only the portal name `pc_hcp_139`.
3. **Geography wording** – agreed. "about 13 km from Cardiff" is replaced in the report by "Machen, a village in Monmouthshire
   between Newport and Cardiff" (the address itself says "Nr Newpt: Mon.").
4. **Postmark date not independently read** – agreed. On `source/address-large.jpg` the cancellation over the halfpenny stamp is
   not legible enough for a day to be read. The report states that 1904-09-11 is the portal's catalogue date, not my reading;
   the stamp (Edward VII halfpenny, in use 1902–1911) is consistent with it.
