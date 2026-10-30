# HCP 1081 (cpc_1911-07-08_UK_Lee-on-the-solent_UK_Fareham_): a reversed-writing postcard from Jack to Miss M. Jallett, 1911

Human solver: Tomáš Pavuk

**Status: read in full (all six cipher rows, no letter restored or left over). Review 1 verdict was ACCEPT. Only the wording about letter forms changed; the plaintext did not.** Report dated 2026-10-30.

## Origin and context

This is record 1081 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1081), portal name cpc_1911-07-08_UK_Lee-on-the-solent_UK_Fareham_. It belongs to Tobias Schrödel's collection of cryptographic postcards (private collection). When the record was captured on 2026-10-26, the portal listed it as follows:

- status **Not solved**, tags Postcard and T. Schrödel Collection
- main category Transposition, language Unknown
- date 1911-07-08, sender Unknown, recipient Miss. M. Jallett
- no transcription or solution attached

The source reference given by the portal is T. Schrödel, *Cryptographic postcards*, HistoCrypt 2021 (DOI 10.3384/ecp183166). That paper describes the collection in general and does not discuss this card. It does not contain the names Fareham, Solent or Jallett, or the year 1911.

The picture side is a coloured printed scene: a couple in folk costume sitting in a landscape, the man playing a mandolin-like instrument. It has no writing.

The address side is a British "POST CARD" (VELLO brand) with an Edward VII halfpenny stamp. The stamp is cancelled "…ON-THE-SOL[ENT]" (Lee-on-the-Solent, Hampshire), 7.15 PM, JY 8 11, which matches the portal date of 8 July 1911. The address, in plain writing, is to **Miss M. Jallett** in **Fareham**, a town a few miles from Lee-on-the-Solent; the middle address lines are only partly legible.

The message half of the address side is written diagonally in pencil. It begins with four plain lines, followed by six lines that look like gibberish. The gibberish lines are the cipher.

![Picture side (source/picture.jpg)](../source/picture.jpg)

![Address side: plain header and the six reversed rows on the left, address and Lee-on-the-Solent postmark of 8 July 1911 on the right (source/address.jpg)](../source/address.jpg)

![Message area rotated 38° and enlarged 3×, used for the reading (work/body-rot38-x3.png)](../work/body-rot38-x3.png)

## Method

All reading was done by hand on enlarged, contrast-boosted crops of the portal scan. No OCR was used.

1. The earlier OpenAI GPT solver (GPT-6 Astra, 2026-10-26) collected the sources and saw that the lower rows read as English when reversed: *write if had time / your with / all love / Jack*. It left the first two rows unread and handed over no solution.
2. Claude Opus 5.5 (2026-10-29/30) rotated the message area by 38°, enlarged it 3× to 7×, and read the two upper rows. It then wrote a full letter-by-letter transcription (work/transcription.txt) and a script that reverses every row (work/decipher.py).

**The rule is simple. Each body row is its own plaintext written backwards, letter by letter**, so both the letters within each word and the order of the words are reversed. The rows themselves are read in normal order, top to bottom. Most letters are ordinary English cursive, but the writer also mirrors some letter forms:

- every d (in `dluow`, `dna`, `dah`) is written like a b;
- the final b of `ysub` has its ascender on the right, so it looks like a d.

The plain header ("Dear M / Just a card / thanking you / for letter") is not enciphered.

Reproduction, run from the repository root:

```text
python3 -I ciphers/hcp-1081/work/decipher.py
```

The script checks the SHA-256 hashes of the four source files, reads the transcription and prints each row with its reversal.

## Key

Cipher type: **reversed writing**, a simple transposition. The portal category is Transposition. There is no secret key; the only rule is "reverse each row".

## Transcription and plaintext

Cipher rows as written (left to right, top row first) and their reversal:

```text
B1  esaelp ysub yrev ma   -> am very busy please
B2  dluow dna esucxe      -> excuse and would
B3  emit dah fi etirw     -> write if had time
B4  htiw ruoy             -> your with
B5  evol lla              -> all love
B6  kcaJ   x              -> Jack x
```

Whole message (original English; the plain header first, then the deciphered body). The words in brackets are the writer's own omissions, not cipher:

*Dear M, Just a card thanking you for letter. Am very busy, please excuse, and would write if [I] had time. Your[s] with all love, Jack x*

Slovak translation: *Milá M., len pohľadnica s poďakovaním za list. Som veľmi zaneprázdnený, prosím, ospravedlň ma, a písal by som, keby som mal čas. Tvoj so všetkou láskou, Jack x*

## Uncertainties

- **B1 `ysub` / `yrev`.** Both words begin with a loosely written y. Word 2 ends in a mirrored b (the same mirroring the writer uses for d), and word 3 ends in a looped v, so the row reads "am very busy". With the two words swapped, it would read "am busy very": the same meaning but worse English, and the letter forms do not support it.
- **B1 `ma`.** A pencil blot covers the humps of the m. The reading rests on the number of humps and on the closed a.
- **B4 `ruoy`.** The word has four letters, so it reads "your", not the usual closing "yours". No s is visible and none was added.
- **B2 `esucxe`.** The x is written as two opposed arcs, which is normal in this hand.
- **Header initial "M".** This is plain text, not cipher. The looped capital is read as M, which agrees with the addressee.
- **Image quality.** Only the 1024-pixel portal scan exists, so the smaller strokes rest on that resolution.
- **People.** The writer "Jack" and the addressee cannot be identified beyond the address on the card.

## Review summary

An independent reviewer (a separate Claude Opus 5.5 agent) ran the reproduction command and checked every row sign by sign on its own crops. It also typed its own transcription and decoded it with its own script. The two transcriptions are identical, and the plaintext matches. The reviewer confirmed that the header, postmark and addressee fit the reading, and that no published solution was used. **Verdict: ACCEPT**, with three minor findings:

1. SOLUTION.md had said the letters were not mirrored. In fact every d and the final b of `ysub` are mirrored glyphs. *Changed:* the description now says this, and the mirrored b is cited as evidence for the B1 word order.
2. The disclosure that B4 reads "your" (no s) is adequate. *No change.*
3. The cipher type should be called "Reversed writing", not just "Mirror writing". *Adopted* in this report and in the register entry.

The transcription and the plaintext were not changed by the review.

## Credit

- **Earlier OpenAI GPT solver (GPT-6 Astra, 2026-10-26):** source capture, metadata, check of the Schrödel paper, and the reversal reading of rows B3–B6.
- **Claude Opus 5.5 (2026-10-29/30):** reading of rows B1–B2, full transcription, decipherment script, documentation and this report.
- **Review:** an independent Claude Opus 5.5 agent.
