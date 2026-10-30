# HCP 1505 (pc_hcp_186): a numeric-cipher postcard from Fred in Scotland to Ethel in Barnsley, 1917

Human solver: Tomáš Pavuk

**Status: deciphered in full (102 of 102 numbers; one faded number restored, one sender's slip corrected only in the normalised text); independent review 1 verdict ACCEPT, no change to the reading.** Report dated 2026-10-29.

## Origin and context

The cryptogram is record 1505 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1505), portal name pc_hcp_186, part of the HCPortal collection of cryptographic postcards (private collection). When it was captured on 2026-10-26 the portal listed it as **Not solved**, category Substitution / Monoalphabetic, date 1917-03-24, language Unknown, location Europe, sender and recipient Unknown, with no transcription or solution attached.

The picture side is a First World War cartoon from the *Bystander* magazine series (the address side is printed "Bystander's Fragments ... Series"), captioned **A MAXIM MAXIM** – "Fire should be withheld till a favourable target presents itself". It carries no cipher.

The address side is addressed in plain writing to a Mrs ... Baxter (name only partly legible), 21 Shaw Street, Barnsley, Yorks, England, with a green George V halfpenny stamp whose postmark is not legible. To the left of the dividing line, written sideways, is the plain header **Scotland / Sat. noon / Dear Ethel**, followed by seven lines of numbers (written in rows running up the card) and the plain signature **Fred.** The portal date 24 March 1917 was a Saturday, which agrees with "Sat.".

![Address side as scanned: the numeric message in rows along the left half, the address at the right (source/address-large.jpg)](../source/address-large.jpg)

![The message area turned upright (work/message.jpg)](../work/message.jpg)

![Picture side: Bystander cartoon "A Maxim Maxim" (source/picture-large.jpg)](../source/picture-large.jpg)

## Method

The message consists of 102 numbers between 2 and 26, grouped into words by spaces. Numbers above 9 are written with an underline (mostly, not always), which distinguishes e.g. 12 from 1 2. The range 1–26 and the word structure point to a numeric alphabet. The ordinary A=1 … Z=26 gives nonsense; the reversed alphabet **A=26 … Z=1** gives English at once (18 / 26.14 = I AM), and the same fixed table then decodes every other word without any adjustment.

The transcription is manual. An OpenAI GPT solver (GPT-6 Astra) captured the portal record on 2026-10-26, identified the reversed-alphabet key and made a first transcription with seven ambiguous digits (4/7, 9/18, 22/12, 4/24). Claude Opus 5.5 re-read every number on 2026-10-29 from 3–6x enlargements of the scan and resolved them on the shapes, not from the expected words: the writer's 7 has a hooked top and a descender, his 4 sits on the line (so NOT, TO, TIME read 13.12.7, 7.12, 7.18.14.22); the group after GOOD is 23.26. The decoder is a few lines of Python that applies the fixed table.

In review, a separate Claude Opus 5.5 agent made its own crops, typed its own transcription and decoded it with its own script; its 102-number decryption is identical to the solver's.

## Key

Reversed numeric alphabet (each letter is replaced by its position counted from Z):

| A | B | C | D | E | F | G | H | I | J | K | L | M |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 26 | 25 | 24 | 23 | 22 | 21 | 20 | 19 | 18 | 17 | 16 | 15 | 14 |

| N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |

Cipher type: monoalphabetic substitution (MASC) with numbers. The decorative alphabet wheel printed over the scans is the HCPortal watermark, not part of the card.

## Plaintext

Ciphertext as transcribed, one line per handwritten line (words separated by "/", numbers by "."; `15r` = restored number):

```text
18 / 26.14 / 20.12.18.13.20
21.12.9 / 14.2 / 8.6.18.7 / 7.12 / 13.18.20.19.7 / 8.12
4.18.15.15 / 13.12.7 / 19.26.5.22 / 7.18.14.22 / 7.12
4.9.18.7.22 / 25.6.7 / 4.18.15.15 / 8.22.13.23 / 26
15.22.7.7.22.18 / 7.12.14.12.18.18.12.4 / 19.26.5.22
26 / 20.12.12.23 / 23.26 / 15r.12.5.22 / 7.12 / 25.12.7.19
2.12.6.9 / 12.4.13
```

Literal decryption (lower case = restored sign):

```text
I AM GOING
FOR MY SUIT TO NIGHT SO
WILL NOT HAVE TIME TO
WRITE BUT WILL SEND A
LETTEI TOMOIIOW HAVE
A GOOD DA lOVE TO BOTH
YOUR OWN
```

With the plain header and signature, normalised English:

**Scotland, Sat. noon. Dear Ethel, I am going for my suit to-night, so will not have time to write, but will send a letter tomorrow. Have a good DA[y?]. Love to both. Your own Fred.**

Slovak translation: **Škótsko, sobota napoludnie. Milá Ethel, dnes večer idem po svoj oblek, takže nebudem mať čas písať, ale zajtra pošlem list. Maj sa dobre (prajem pekný de[ň?]). S láskou pozdravujem oboch. Tvoj Fred.**

Notes on the reading:

- **LETTEI, TOMOIIOW.** Three times the writer put 18 for R. In this key 18 is I, but 18 is R's position in the ordinary forward alphabet – a natural slip when encoding by hand. Elsewhere R is correctly 9 (FOR, WRITE, YOUR). The 18s are clearly written; only the normalised text corrects them.
- **"Going for my suit"** probably means collecting a suit from a tailor; "love to both" suggests Ethel lived with another person, perhaps the Mrs Baxter of the address. The identities of Fred and Ethel are not established.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1505/work/decode2.py
```

The script uses only the Python standard library. It checks the SHA-256 hashes of the two scans, decodes all 102 numbers of work/transcription-v2.txt with the fixed key (1=Z … 26=A), prints the literal decryption above and a normalised line with only the R-slip corrected, and ends with `signs: 102, restored: 1`. The transcription step itself is manual.

## Uncertainties

1. **R written as 18** (sender's slip) in LETTER and TOMORROW, see above. Disclosed; corrected only in the normalised text.
2. **"DA" after "HAVE A GOOD".** Read 23.26 (D A), followed by a full stop; 22 (E) is a less likely reading of the first number. "Day" is the probable intent, but no Y survives on the card. Between "23 26." and the next word lies a gap with room for two or three numbers, in an abraded, lighter patch of the paper (the same patch that took the 1 of 15 in LOVE). A lost sign there (e.g. 2 = Y, giving DAY) cannot be excluded, although the full stop directly after 26 argues against it. DA is kept as the literal reading.
3. **First sign of LOVE (restored).** Only a 5 and an underline survive in the abraded patch; the underline marks a two-digit number, and 15 (L) is the only value that gives a word (otherwise VOVE). Restored as 15 and marked.
4. Underlining of two-digit numbers is not fully systematic (the 14 of TOMORROW is not underlined); no reading depends on it.
5. The postmark is illegible; the date 24 March 1917 rests on the portal metadata and agrees with "Sat." on the card. The addressee's name and the header were not needed for the decryption and are read only approximately.
6. No prior publication of this card was found: portal status Not solved with no attached solution (2026-10-26), and no entry for it in the AI Decipherment Register (checked 2026-10-29).

## Review summary

Reviewer: Claude Opus 5.5 (Anthropic), a separate agent, round 1, verdict **ACCEPT**. The reviewer ran the reproduction command (output identical to the claimed plaintext), re-read every number from its own 2–6x crops, and decoded its own transcription with its own script, obtaining the same 102-number decryption. It confirmed the 7/4 distinction, the clearly written 18s in LETTER and TOMORROW, the reading 23.26 after GOOD, the restored 15 of LOVE, and that 24 March 1917 was a Saturday. Its three minor findings were all accepted:

- **Abraded gap before LOVE.** The uncertainties now state that a sign may have been lost there (possibly Y, giving DAY); DA stays the literal reading.
- **I / AM.** The first line had been transcribed as one group IAM; the scan shows I and AM as separate groups. The transcription was corrected to `18 / 26.14`; the decoded letters are unchanged.
- **Underlining.** The statement that two-digit numbers are underlined was softened to "mostly".

No decoded letter changed as a result of the review.

## Credits

Source capture, key identification and first partial transcription: OpenAI GPT (GPT-6 Astra), 2026-10-26. Full re-reading, resolution of the ambiguous digits, decipherment, response to review and this report: Claude Opus 5.5, 2026-10-29. Independent review: a separate Claude Opus 5.5 agent.

## Sources

- HC Portal record 1505, General, Description and Attachments tabs, captured 2026-10-26: https://crypto.hcportal.eu/dashboard/cryptograms/1505 (source/metadata.md).
- Address side: https://api.hcportal.eu/media/4576/conversions/pc_hcp_186_adr-large.jpg (source/address-large.jpg).
- Picture side: https://api.hcportal.eu/media/4575/conversions/pc_hcp_186_pic-large.jpg (source/picture-large.jpg).
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-29.
