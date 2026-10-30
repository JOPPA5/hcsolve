# HCP 1081 — reversed-writing postcard, Lee-on-the-Solent to Fareham, 8 July 1911

**Status: complete reading (round 1), small disclosed residual points.** Solved on 2026-10-29/30 by Claude Opus 5.5 (as solver), building on a partial reading by the earlier OpenAI GPT solver (2026-10-26), which had established the reversal principle and rows B3-B6 but left rows B1-B2 unread.

Portal: https://crypto.hcportal.eu/dashboard/cryptograms/1081, name `cpc_1911-07-08_UK_Lee-on-the-solent_UK_Fareham_`, status **Not solved** when captured (2026-10-26), category Transposition, T. Schrödel collection. Recipient per metadata and address: Miss M. Jallett, Fareham. No published solution of this card was found (portal attachments show none; the linked Schrödel 2021 paper does not mention this card – see SOURCES.md).

## Cipher type and key

**Reversed writing (line-wise reversal; a simple transposition).** The writer wrote an ordinary plaintext header, then six body rows diagonally across the message half of the card. Each body row is the plaintext of that row written backwards letter by letter (so both the letter order inside words and the word order in the row are reversed). Most letters are normal English cursive, but some are written as mirrored glyphs: every `d` (in `dluow`, `dna`, `dah`) looks like a b, and the final `b` of `ysub` has its ascender on the right, so it looks like a d (corrected after review 1). Rows are read top to bottom. There is no key beyond "reverse each row".

## Transcription (as written, left to right, top row first)

File `work/transcription.txt`; read on `work/body-rot38-x3.png` and further 5-7x crops.

```
B1  esaelp ysub yrev ma
B2  dluow dna esucxe
B3  emit dah fi etirw
B4  htiw ruoy
B5  evol lla
B6  kcaJ          (followed by a separate cross "x")
```

## Plaintext (English, original)

Plain header (not enciphered): **Dear M / Just a card / thanking you / for letter**

Deciphered body: **am very busy please / excuse and would / write if had time / your with / all love / Jack x**

Read as a message: *Dear M., Just a card thanking you for letter. Am very busy, please excuse, and would write if [I] had time. Your[s] with all love, Jack x*

Slovak: *Milá M., len pohľadnica s poďakovaním za list. Som veľmi zaneprázdnený, prosím ospravedlň ma, a písal by som, keby som mal čas. Tvoj s všetkou láskou, Jack x*

(English gloss above is the original language; the bracketed words are the writer's elisions, not ciphertext.)

## Single command (from the repository root)

```sh
python3 -I ciphers/hcp-1081/work/decipher.py
```

It checks SHA-256 of the four files in `source/`, reads `work/transcription.txt`, reverses every row and prints the plaintext. Output (2026-10-29):

```
B1: esaelp ysub yrev ma    -> am very busy please
B2: dluow dna esucxe       -> excuse and would
B3: emit dah fi etirw      -> write if had time
B4: htiw ruoy              -> your with
B5: evol lla               -> all love
B6: kcaJ                   -> Jack
```

## Uncertainties

1. **B1 `ysub` / `yrev` (busy / very)** – the handwriting of these two y-initial words is loose. Word 2 ends with a rising stroke that starts a b-loop and contains an open u; word 3 ends in a v with a closing top loop and has an r-hump and e. I read word 2 = `ysub`, word 3 = `yrev`, giving "am very busy". The closing bowl of word 2 has its tall stroke on the right. That is a mirrored b, the same mirroring the writer uses for every d on the card, so the letter forms themselves support `ysub` (added after review 1). If the two were swapped the row would read "am busy very please" – same content, worse English; the letters favour the reading given.
2. **B1 `ma`** – the m carries a heavy pencil blot over its humps; the reading `ma` (am) rests on the hump count plus the closed a with tail.
3. **B4 `ruoy`** – I read four letters (r, u, o, y), i.e. "your", not "yours"; the expected closing is "Yours with all love". No `s` is visible and none is supplied.
4. **B2 `esucxe`** – the x is written as two opposed arcs (ɔc), normal in this hand.
5. **Header initial "M"** – the greeting initial is a looped capital that I read as M; it agrees with the addressee "Miss M. Jallett" but is not ciphertext and remains slightly uncertain.
6. Header and address/postmark are plaintext and were not part of the decipherment; the postmark place ("...ON-THE-SOL[ENT]", JY 8 11) agrees with the metadata.

No letter is restored; every ciphertext letter above was read from the scan.

## Why I believe it is correct

- One rule (reverse each row) turns every one of the six rows into English words; no row needs a different rule, and no letter is left over.
- The result is a fluent, typical 1911 postcard: thanks for a letter, apology for being busy, "would write if had time", a loving close and a signature with a kiss cross. It continues the plain header naturally ("Just a card thanking you for letter. Am very busy, please excuse…").
- Rows B3-B6 were independently obtained by the earlier GPT solver; the new rows B1-B2 complete the sentence grammatically (`please excuse and would write`).

## Credit

Source capture, metadata, source-paper check and the reversal reading of B3-B6: earlier OpenAI GPT solver (2026-10-26, see NOTES.md). Reading of B1-B2, corrected full transcription, `work/decipher.py`, this document: Claude Opus 5.5, 2026-10-29/30. The older partial script `work/decode.py` is kept for history and is superseded.

## Response to review 1

Verdict: **ACCEPT**, three minor findings. The reading did not change.

1. **Mirrored glyphs (minor): fixed.** I checked `work/body-rot38-x3.png` again. In B2 `dluow` and `dna` and in B3 `dah`, the d is clearly written as a b-shape (bowl on the left of the ascender as seen, i.e. mirrored), and the last letter of `ysub` is the opposite case. I corrected the sentence under "Cipher type and key", which had said the glyphs were not mirrored. The type is now "reversed writing with partly mirrored letter forms". I also cited the mirrored b as evidence under Uncertainty 1.
2. **B4 `ruoy` (minor): agreed, nothing to change.** The disclosure that the text reads "your", not "yours", stays as it is.
3. **Type label (minor): adopted.** The report and the register entry use "Reversed writing" (portal category: Transposition), not "Mirror writing".

Re-ran `python3 -I ciphers/hcp-1081/work/decipher.py` on 2026-10-30. Source SHA-256 4/4 OK, and the output is identical to the output above. The transcription file and the script were not changed.
