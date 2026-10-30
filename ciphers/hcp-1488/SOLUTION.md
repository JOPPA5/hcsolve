# Portal1488 / pc_hcp_169 — partial ROT13 reading

**Partial.** Portal Not solved verified2026-10-26. ROT13 is supported by
two short manually transcribed passages in the faint correspondence:

|Location|Cipher excerpt|Reading|
|---|---|---|
|Opening|V gubhtug V|I thought I|
|Closing|Sbaq ybir sebz|Fond love from|

These are separate passages; **the middle is not transcribed or decoded**.
No continuous complete letter or sender identification claimed.

Slovak meaning of excerpts: „Myslel/myslela som, že ja…“ and
„S vrúcnou láskou od…“. An idiomatic complete sentence cannot be supplied
without recovering the omitted material.

## Reproduction
Run from repository root:
`python3 ciphers/hcp-1488/work/decode.py`

Key is Caesar13, A↔N,B↔O,...,M↔Z. Own manual readings in work/excerpts.txt,
no transcription attached. Script verifies immutable source hashes and
roundtrips the21 excerpt letters. This is not OCR or independent pixel
validation and says nothing about full body coverage.

Originals are source/address-large.jpg and source/picture-large.jpg.
Working rotation/enlargements/contrast copies are in work/. contrast.swift
reproduces grayscale stretch170..245 using built-in CoreGraphics; the
enhancement does not reconstruct missing strokes. It operates only on crops,
not immutable source. Some body letters remain indistinct behind watermark.
No published solution used. No DONE1, FINAL, PDF or register entry.

## Update 2026-10-29 (Claude Opus 5.5) — still PARTIAL

Cipher: Caesar shift 13 (ROT13), English, word spacing and punctuation kept.
Credit: ROT13 and the two excerpts above were found by the earlier OpenAI GPT
solver (2026-10-26); the line readings below are new, read by Claude Opus 5.5
from enlarged crops of work/upright.jpg.

Command (repo root): `python3 -I ciphers/hcp-1488/work/decode_partial.py`
(checks source hashes, decodes work/transcription-partial.txt).

| Line | Ciphertext | Plaintext |
|---|---|---|
|1|V gubhtug V jbhyq fraq|I thought I would send|
|2|guvf gb gryy lbh ubj|this to tell you how|
|3|unccl V jnf ynfg avtug.|happy I was last night.|
|4|V [?] lbh [?] [?] zber|I [?] you [?] [?] more|
|5|[?] [?] [?] [f/z]hpu nf|[?] [?] [?] [s/m]uch as|
|6|cbffvoyr. Va fcvgr bs gur|possible. In spite of the|
|7|Pncgnva'f frezba V nz|Captain's sermon I am|
|8|nsenvq V nz na vqbyngre|afraid I am an idolater|
|9|sbe V fvzcyl jbefuvc lbh qrne.|for I simply worship you dear.|
|10-11|Sbaq ybir sebz Crepl|Fond love from Percy|

Slovak: „Myslel som, že ti pošlem toto, aby som ti povedal, aký som bol
včera večer šťastný. … možné. Napriek kapitánovej kázni sa obávam, že som
modloslužobník, lebo ťa jednoducho zbožňujem, drahá. S vrúcnou láskou, Percy."

Uncertain / missing: lines 4-5 (about 6-8 words) are under the printed dark
band and big watermark letters and are not readable on the 1024-px scan; no
guess is entered. 'jbhyq', 'ubj', 't' of 'avtug' and the signature 'Crepl'
are faint but fit the visible strokes. Not complete, so no DONE1.
