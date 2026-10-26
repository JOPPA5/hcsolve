# HCP56 - review-corrected ROT13 correspondence

## Cipher and key

Caesar substitution, shift 13 (ROT13). Same operation encrypts and decrypts.

```text
cipher: ABCDEFGHIJKLMNOPQRSTUVWXYZ
plain:  NOPQRSTUVWXYZABCDEFGHIJKLM
```

The opening v gubhtug v jbhyq suggested the shift, then the entire message
decoded under the same fixed mapping. No per-word exception or rearrangement.

## Plaintext

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

The separate unencrypted signature appears **Cecil**, but this is a
provisional cursive reading, not a verified sender identity. Captains is
normally understood as Captain's; its apostrophe is editorial. IDOLATOR
is preserved. Punctuation is not cryptographic.

## Slovak translation

„Napadlo mi poslať ti toto, aby som ti povedal, aký som bol včera večer
šťastný. Teraz ťa milujem desaťkrát viac než kedykoľvek predtým, ak je
niečo také možné. Napriek kapitánovej kázni sa obávam, že som modloslužobník,
pretože ťa jednoducho zbožňujem, drahá. S vrúcnou láskou od…“

Gendered grammar is a translation choice, not independent identification.
The captain's sermon reference does not establish a captain, institution
or event.

## Reproduction

From repository root:

```sh
python3 ciphers/hcp-56/work/decode.py
```

Checks source hashes and decodes work/ciphertext.txt, the disclosed manual
transcription. No OCR is performed; the portal supplied no transcription.
Source-to-transcription correspondence needs independent visual checking.

All Caesar shifts for comparison:

```sh
python3 ciphers/hcp-56/work/decode.py --all-shifts
```

Common-word ranking is a transparent diagnostic, not a probability or
independent validation of handwritten letter readings.

## Evidence and limits

One key accounts for all transcribed correspondence and closing, with
continuous English across 183 letters after review corrections. Re-encryption
checks implementation consistency, not image-to-letter accuracy. Unencrypted
signature is separate. No published target plaintext used; no historical-priority
or verified identity claim. Review 1 (Claude Opus 5.5) requested the corrections
below and explicitly stated no further review round was needed after them.
The revised literal text preserves lowercase i wherever cipher v is lowercase;
uppercase I in an edited reading is an editorial capitalization choice.


## Response to review 1

Review: review/REVIEW1.md, REVISE, Claude Opus 5.5, 2026-10-26.

1. Closing corrected from the erroneous earlier transcription to `Sbaq ybir sebz`,
   literally **Fond love from**. Compared the scan-derived r-close.png and
   r-all.png with the handwritten line. work/ciphertext.txt, plaintext,
   translation and NOTES now agree. No key change.
2. Added omitted `qrne` at the end of line 9, giving **dear**. The reviewer
   details r-dear.png/r-you.png show the four-letter group after lbh. The
   false earlier claim of complete coverage has been replaced by revised
   coverage: **183 alphabetic positions** including the closing.
3. Restored the source's lowercase `v` pronouns throughout the diplomatic
   ciphertext. Literal decryption therefore gives lowercase i. Va and Pncgnvaf
   retain their capitals. Case-normalized prose is editorial only.
4. Kept the separate ordinary signature **Cecil** provisional. The captain's
   identity, sender identity and any unseen picture side remain unclaimed.

The reproduction command checks unchanged source hashes, decrypts all183
manual letters and re-encrypts them exactly. Roundtrips do not independently
prove palaeographic readings. The reviewer independently checked the whole
card and key; these corrections implement the expressly stated closing
conditions. Final closure follows report generation and visual QA.


## Finalization - 2026-10-26

The coordinating solver verified the item-by-item review response, reran the
corrected decoder with original-source hash checks, and produced the report
PDF. All rendered pages were visually inspected after final typography
corrections. The review explicitly permits closure after the specified local
corrections without another round. Remaining reading uncertainties are
preserved; no new independent ACCEPT verdict is claimed.

The local register-entry.txt is prepared with solver TODO because no solver
name was supplied for the entry. Nothing was submitted externally. Original
source files and review files were left unchanged. FINAL records closure
after these review conditions and report checks.
