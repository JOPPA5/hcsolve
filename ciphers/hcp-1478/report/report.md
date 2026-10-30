# HCP 1478 (pc_hcp_159): an English greeting from "Peggy" to Mr Dixon, Hereford, 1907

Human solver: Tomáš Pavuk

**Status: deciphered (every cipher glyph decoded; one word and the abcd part of the key tentative); independent review 1 verdict ACCEPT, no decoded letter changed.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1478 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1478), portal name pc_hcp_159, part of the HCPortal collection of cryptographic postcards (private collection). When it was captured on 2026-10-26 the portal listed it as **Not solved**, tagged Postcard, HCPortal collection, category Substitution, date 1907-06-27, language Unknown, location Europe, sender Unknown, recipient "Discon", with no transcription or solution attached.

The picture side is a Valentine's Series "Souvenir Post Card" showing the **Baptist Church, Abergavenny** (Monmouthshire; Valentine number 45734). The address side is addressed in plain writing to **Mr Dixon, 3 St Nicholas St., Hereford** (the portal's "Discon" is a misreading of Dixon). It carries a green ½d Edward VII stamp and a postmark whose town is only partly legible (consistent with Hereford) and whose date ends "27 / 07", matching the portal date 27 June 1907. The cipher message is written in cursive in seven short lines on the address side, above a signature in plain letters.

![Address side with the seven cipher lines and the signature (source/address-large.jpg)](../source/address-large.jpg)

![Picture side: Baptist Church, Abergavenny (source/picture-large.jpg)](../source/picture-large.jpg)

## Method

Setup (portal capture, download of both scans), a first provisional transcription and a bounded screen of simple keys (all 26 Caesar shifts, Atbash, keyboard shifts and keyboard-alphabet substitutions) were done on 2026-10-26 by an earlier solver, OpenAI GPT (GPT-6 Astra); the screen was negative.

On 2026-10-30 Claude Opus 5.5 re-transcribed the seven lines sign by sign from 4–7× enlarged crops, correcting several provisional readings (for example qkflglgqz → qkpbgtgqr, qmccy → jmxg, rymuot → rymwt). The transcription is manual; no OCR was used. A Slovak n-gram hill-climb was tried and abandoned (the text is clearly English). The decisive step was a crib attack with the expected phrases of an Edwardian greeting ("my own", "with", "love from", "your loving"): all of them obey one systematic rule, swapping every letter with the letter two places away inside its block of four (alphabet index XOR 2). The repeated beginning jmx- of jmxg (love) and jmxkpe (loving) confirms it internally. That rule decodes 9 of the 11 cipher words without any adjustment; the two remaining words need a different arrangement of the block a b c d (see Key).

## Key

Monoalphabetic substitution (MASC). For the letters e–x each letter is replaced by its partner two places away within its block of four; the key is reciprocal there:

| Plain  | e | f | g | h | i | j | k | l | m | n | o | p | q | r | s | t | u | v | w | x |
|--------|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cipher | g | h | e | f | k | l | i | j | o | p | m | n | s | t | q | r | w | x | u | v |

The block a b c d does **not** follow the XOR-2 rule on this card. The three attested values fit a rotation, with the fourth value d → c filled in by assumption:

| Plain  | a | b | c | d | y |
|--------|---|---|---|---|---|
| Cipher | d | a | b | (c) | y |

y stands for itself; z is not attested.

## Plaintext

Ciphertext as transcribed, line by line, and its literal decryption:

```text
Rm oy mup    -> To my own
adrfkpe      -> bathing
ukrf         -> with
qkpbgtgqr    -> sincerest
jmxg htmo    -> love from
rymwt        -> t your
jmxkpe       -> loving
                (signature in clear, written "Depgy"/"Pepgy")
```

Reading (English, the original language):

**To my own [bathing?] with sincerest love from [t] your loving Peggy.**

Slovak translation: **Môjmu vlastnému [kúpajúcemu sa?] s najúprimnejšou láskou od tvojej milujúcej Peggy.**

"With sincerest love from your loving …" is a stock postcard formula of the period, and the message has the usual shape of such a greeting.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1478/work/decode.py
```

The script uses only the Python standard library and writes no files. It checks the SHA-256 hashes of both scans, decodes the manual transcription line by line with the key above, and prints the reading. It does not read the image; the transcription step is manual and was checked independently in review.

## Uncertainties

- **"bathing" and the abcd block (main weak point).** The pixels clearly show a d r f k p e, and r f k p e → "thing" is certain under the key (r and f are the same glyphs as in ukrf = "with", which rules out "darling"). The first two letters depend on the a b c d part of the key, which is attested independently only by one glyph (c → b in "sincerest"; pure XOR 2 would give "sinderest"). Assuming the abcd block is a permutation of a b c d, "bathing" is the only English word that fits, but the values for a and d are derived from this word itself, so the reasoning is circular. "To my own bathing" is not idiomatic; it may be a private joke, a nickname or a writer's slip. The word is shown as [bathing?].
- **"To".** The first glyph of line 1 is a tall stem with a top loop, bowl and leg. It is read as a cursive capital R (→ T); it closely resembles the writer's lowercase k, which would give the non-word "Io". "To" is overwhelmingly likely from context but rests on this interpretation.
- **Leading glyph of line 6.** Before ymwt ("your") stands a separate r-shaped glyph that would decode to t. It may be a false start or lead-in stroke; it is shown as [t] and given no meaning.
- **The signature** is in plain letters, not in cipher, and is written "Depgy" or "Pepgy" (a cursive capital with a bottom-left loop, and a third letter shaped like this writer's p). It does not decode under the key. "Peggy" is an interpretation.
- **Unattested letters.** z is not attested, and plain j, k, p, q, x, z do not occur; their cipher values follow from the systematic rule (for e–x) and are not confirmed by the text. The value d → c is an assumption completing the rotation.
- The postmark town is only partly legible. The identities of Peggy and Mr Dixon are not established.
- No published solution of this card was found; the portal status was Not solved with no attached solution, and the AI Decipherment Register had no entry for it (checked 2026-10-29).

## Review summary

Reviewer: Claude Opus 5.5 (Anthropic), a separate agent, round 1, verdict **ACCEPT**. The reviewer ran the reproduction command (output identical to the claimed plaintext), decoded its own transcription with its own script both under pure XOR 2 and under the solver's key, confirmed every line of the transcription on its own 4–7× crops, and confirmed that the rule is systematic rather than fitted word by word. Its five findings were all minor:

- **"bathing" is circular.** The word is now marked [bathing?] in SOLUTION.md, in the decoder's output and in this report.
- **"To" depends on reading a k-like glyph as capital R.** Kept as a disclosed uncertainty.
- **The signature is written "Depgy"/"Pepgy".** It is now transcribed as written, with "Peggy" given as an interpretation.
- **Leading r in line 6.** Kept disclosed as [t].
- **Cipher type.** MASC confirmed.

No decoded letter changed as a result of the review.

## Sources

- HC Portal record 1478, General, Description and Attachments tabs, captured 2026-10-26: https://crypto.hcportal.eu/dashboard/cryptograms/1478 (source/metadata.md).
- Address side: https://api.hcportal.eu/media/4495/conversions/pc_hcp_159_adr-large.jpg (source/address-large.jpg).
- Picture side: https://api.hcportal.eu/media/4494/conversions/pc_hcp_159_pic-large.jpg (source/picture-large.jpg).
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-29.
