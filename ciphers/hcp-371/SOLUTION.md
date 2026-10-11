# hcp-371 — unresolved

No plaintext or key has been established. No review handover is claimed.

The portal describes the 1944 message as “Nerozlúštiteľný telegram - opakovať” and marks it Not solved / Unsolvable. This archival description is context, not proof that modern decipherment is impossible.

## Transcription

There is no attached transcription or solution. `work/transcription.txt` is my literal visual transcription of `source/cryptogram.jpg`; the header `4207` is separated from the cipher. The body contains 203 letters in 41 printed groups, with irregular groups `SZEPRR` (6), `JORMCO` (6), `HMLA` (4), and `LI` (2). I have not inserted characters to make a putative 207-letter message. Interpreting the header as a length indicator is unproved.

## Findings

The letter distribution (IoC 0.058528, vowels AEIOUY 42.36%) permits a transposition hypothesis. A single ordinary columnar transposition search is inconclusive: widths 2–24, 12 seeded restarts and 20,000 mutations each, with a Slovak quadgram score. The same search exactly recovers a generated 203-letter Slovak positive control with width 11 and its key. Target results contain isolated wordlike fragments but no coherent message; they are not plaintext.

`sh ciphers/hcp-371/work/reproduce.sh` reproduces the tested searches and control. This is an analysis command, not a decipherment command. Quadgrams were copied from the shared `hcp-393/work/quadgrams.tsv` model; its training corpus is Slovak UD SNK. This limited model/search cannot exclude double transposition, other transposition systems, ciphertext corruption, or a different cipher family.

A full plaintext-producing command, original-language plaintext, translation and key remain unavailable. No register entry or DONE marker is warranted.
