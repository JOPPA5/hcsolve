# HCP 56 - An encrypted postcard from Market Drayton

Human solver: Tomáš Pavuk

## Origin and scope

The postcard was sent to Miss D. Conway, Tunstall, Market Drayton, Salop.
The visible postmark reads Market Drayton, 8.30 PM, 13 September 1906,
consistent with the portal date. The sender's ordinary cursive signature
appears to read Cecil, but that name is provisional and no historical
identity is asserted. The portal provided one address/correspondence scan;
an unseen picture side is not claimed inspected.

Source: https://crypto.hcportal.eu/dashboard/cryptograms/56 . All three
rendered tabs were inspected on 25 October 2026: Not solved, no attached
transcription or solution. Original scan:
https://api.hcportal.eu/media/154/conversions/26731655377829-large.jpg .
The original and captured metadata remain unchanged in source/.

## Method and key

The handwritten Latin-letter message uses ROT13, a Caesar substitution
with a fixed shift of 13. The same operation encrypts and decrypts.

```text
Cipher: ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain:  NOPQRSTUVWXYZABCDEFGHIJKLM
```

The mapping applies uniformly to all 183 alphabetic positions. Ordinary
punctuation and spaces are retained; the signature is not enciphered.
No external target plaintext was used. A register check found no exact
source match, which is not proof that no earlier decipherment exists.

## Literal plaintext

```text
i thought i would send
this to tell you how
happy i was last night.
i love you ten times more
than ever now if such is
possible. In spite of the
Captains sermon i am
afraid i am an idolator
for i simply worship you dear.
Fond love from
```

Lowercase i follows the writer's lowercase cipher v. Capitalizing it in
ordinary English prose is editorial. Captains lacks an apostrophe in the
recorded ciphertext; Captain's is an editorial interpretation. Idolator
is retained without a spelling correction. The separate signature appears
to read Cecil and is not included in the 183 cipher letters.

## Slovak translation

Napadlo mi poslať ti toto, aby som ti povedal, aký som bol včera večer
šťastný. Teraz ťa milujem desaťkrát viac než kedykoľvek predtým, ak je
niečo také možné. Napriek kapitánovej kázni sa obávam, že som
modloslužobník, pretože ťa jednoducho zbožňujem, drahá.
S vrúcnou láskou od…

Gendered grammar is a translation choice. The captain's identity and any
institution or event behind the sermon are not established by the card.

## Review and corrections

Claude Opus 5.5 independently reviewed the complete scan and ROT13 key
on 26 October 2026 (review/REVIEW1.md). The verdict was REVISE for two
reading errors and minor transcription issues. The reviewer stated that
no further review round was required after the specified corrections.

- Corrected the last cipher line to Sbaq ybir sebz, giving Fond love from.
- Restored the omitted qrne, giving dear at the end of the previous line.
- Preserved the writer's lowercase v pronouns in the diplomatic ciphertext.
- Kept the signature reading Cecil provisional and the signature outside
  the enciphered message.

The corrected transcript now covers 183 letters. The original erroneous
closing and omitted word are no longer part of the solution claim.
Source and review files were not changed. The full item-by-item response
is recorded in SOLUTION.md under Response to review 1.

## Reproduction and remaining limits

From the repository root:

```text
python3 ciphers/hcp-56/work/decode.py
```

This checks original-file hashes and decodes work/ciphertext.txt, a
manual transcription collated with the scan and review details. It also
checks inverse encryption. These software checks do not independently
read the image or prove every pencil stroke. The independent review
supplies the separate visual check; the signature remains uncertain.

Solver work: OpenAI GPT, GPT-6 (Codex). Independent review: Claude Opus 5.5.
Report prepared after implementing the review's stated closing conditions.
