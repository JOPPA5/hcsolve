# HCP 1437 (pc_hcp_118): a digit-for-vowel postcard from Mill Valley

Human solver: Tomáš Pavuk

**Status: deciphered in full; independent review 1 verdict ACCEPT.** Report dated 2026-10-26.

## Origin and context

The cryptogram is record 1437 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1437), portal name pc_hcp_118, part of the HCPortal cryptographic postcards collection (private collection). When it was captured on 2026-10-26 the portal listed it as **Not solved**, main category Substitution, language Unknown, date 1908-09-25, sender Unknown, recipient Briggs, with no transcription or solution attached.

It is an American picture postcard published by the Newman Post Card Co., Los Angeles. The picture side shows the Bell Tower & Chimes, Mills Seminary, Oakland, Cal., and carries no handwriting. On the address side the postmark reads MILL VA[LLEY] SEP 25 5 PM 190[8]; the last digit of the year and the hour are partly under the stamp, so the year 1908 rests on the portal. 25 September 1908 was a Friday. The card is addressed in plain script to Mrs S. J. Briggs, Canaan, Conn., Box 275, which agrees with the portal recipient. The message, nine short lines on the left half of the address side, is written in a mixture of digits and ordinary cursive letters and is signed, inside the same system, SKIPP.

Mill Valley lies in Marin County, across the bay from San Francisco and Oakland, which fits the message ("have been to Oakland once", "was in San Francisco yesterday").

![Address side with the nine-line message on the left (source/address.jpg)](../source/address.jpg)

## Method

No transcription was supplied, so the solver traced the message manually from source/address.jpg into work/transcript.txt, recording every sign either as a digit or as an ordinary Latin letter. The first groups (`H1v2 B227 64`) suggested HAVE BEEN TO if 2 = E and 7 = N; extending this across the card gave a single table of nine digits for the five vowels and the four frequent consonants T, N, S, R, while all other letters are written normally. Common words (BEEN, ONCE, YESTERDAY) and the long SAN FRANCISCO repeat the same values independently, and no word needs a special substitution.

The message has 114 letter positions: 72 digits and 42 Latin letters. Each digit has one value everywhere (counts 1:15, 2:13, 3:10, 4:4, 5:1, 6:6, 7:8, 8:11, 9:4). The 42 plain letters all come from b c d f h k l m p v w y; no plain vowel and no plain t, n, s or r appears anywhere, exactly as the scheme predicts.

In review the whole message was read again from the scan, independently and sign by sign, with enlarged crops of every row and 5–10× details of the doubtful places, and decoded with an independently written script. The two readings agree at all 114 letter positions; the reviewer found one full stop (after YESTERDAY) that the solver's trace omits.

## Key

A partial substitution: nine letters are replaced by digits, every other letter keeps its ordinary form.

| Cipher digit | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
| Plain letter | A | E | I | O | U | T | N | S | R |

The order is the five vowels A E I O U followed by T N S R.

## Plaintext

Transcription of the card (work/transcript.txt, with the full stop after `y28629d1y` added in review; digits as written, Latin letters in lower case except where the writer used a capital):

```text
H1v2 B227 64
41kl17d 47c2.
W18. 37. 817 F917c38c4
y28629d1y. w36h
C18p298 w3f2 17d
81w D1v3d W1k2f32ld
pl1y 6h2 m583c
m18629. 36 w18 f372.
8k3pp.
```

As written, decoded (line breaks and full stops as on the card):

```text
HAVE BEEN TO
OAKLAND ONCE.
WAS. IN. SAN FRANCISCO
YESTERDAY. WITH
CASPERS WIFE AND
SAW DAVID WAKEFIELD
PLAY THE MUSIC
MASTER. IT WAS FINE.
SKIPP.
```

Normalized English (apostrophe, capitals and title editorial; the bracketed name is an interpretation, not a decoded reading): **Have been to Oakland once. Was in San Francisco yesterday with Casper's wife and saw David Wakefield [i.e. David Warfield] play The Music Master. It was fine. Skipp.**

Slovak translation: **Bol(a) som raz v Oaklande. Včera som bol(a) v San Franciscu s Casperovou manželkou a videl(a) som Davida Wakefielda [t. j. Davida Warfielda] hrať v hre The Music Master. Bolo to pekné. Skipp.**

The name is written WAKEFIELD and is kept so in the literal text: the ink has `W1k2f32ld`, and the k matches the k of OAKLAND and SKIPP, while the digit 9 (R) in this hand descends below the line. But the context makes clear whom the writer meant. *The Music Master* by Charles Klein, produced by David Belasco in 1904, was the vehicle of the actor **David Warfield**, who played Anton von Barwig in it from 1904 to 1908, and a 1908 issue of the *San Francisco Dramatic Review* reports a run of "David Warfield in The Music Master" in San Francisco (context supplied by the reviewer; sources below; the exact week of the run was not established). The writer most probably misspelled or misremembered Warfield as Wakefield. That the decoded text names the right first name and the right play, in San Francisco, in 1908, is strong independent confirmation of the decipherment.

## Reproduction

From the repository root:

```sh
python3 ciphers/hcp-1437/work/decode.py
```

The script checks the SHA-256 hashes of both scans and of source/metadata.md, decodes the manual trace in work/transcript.txt with the key above and checks the inverse encoding. It does not read the image; the transcription step is manual (and was confirmed independently in review). Its output lacks the full stop after YESTERDAY, which review 1 found on the card and which is added in the literal text above.

## Uncertainties

- The first sign of OAKLAND is a heavy 4 written over an earlier stroke; what lies underneath is not known, and the earlier stroke is not counted as a letter.
- CASPERS is read with p (long descender, as in PLAY and SKIPP); an h would give CASHERS. Solver and reviewer both see p.
- The first c of FRANCISCO and the c of MUSIC are written as a looped, e-like cursive c. Since E is always the digit 2 in this system, they are read as c.
- The capital F of FRANCISCO is a 7-like capital, distinguished from the digit 7 (N) only by its flat top bar, its size and the context.
- WAKEFIELD is the literal reading; the identification with David Warfield is contextual (see above), and the dense final `32ld` is cramped but legible.
- The two small dots in WAS. IN. are kept as written; a possible faint dot between PLAY and THE is too faint to be called ink and is not added.
- The year 1908 and the hour of the postmark rest partly on the portal; the stamp covers the last digits.
- Skipp (the sender) and Casper are not identified.
- No published decipherment was found: the portal showed Not solved with no attachment, and a same-day snapshot of the AI Decipherment Register has no entry for this card. No wider search was made.

## Review summary

Reviewer: Claude Opus 5.5 (Anthropic), round 1, verdict **ACCEPT**. The reviewer ran the reproduction command (output byte-identical to the solver's saved check), read the whole message from the scan in its own transcription before comparing, decoded it with an independent script, checked key consistency and coverage, the doubtful signs at high zoom (OAKLAND, WAKEFIELD, CASPERS, HAVE), the rest of the card for missed ciphertext, and the context. Its four findings were minor and are reflected here:

- A full stop after YESTERDAY was omitted from the trace: it is added to the literal text in this report.
- The strongest context, David Warfield in *The Music Master*, was hidden: it is now stated, with WAKEFIELD kept as the literal reading.
- Near-homographs (the e-like c, the 7-like F) were not disclosed: they are listed under Uncertainties.
- The postmark, address and language were not recorded: they are given under Origin and context.

No letter of the plaintext changed because of the review. The closing steps (response to review, this report, the register entry) were prepared by Claude Opus 5.5 on the solver's behalf at the human's request; the decipherment itself was made by the solver, OpenAI GPT (GPT-6 Astra).

## Sources

- HC Portal record 1437, General, Description and Attachments tabs, captured 2026-10-26: https://crypto.hcportal.eu/dashboard/cryptograms/1437 (source/metadata.md).
- Address side: https://api.hcportal.eu/media/4372/conversions/pc_hcp_118_adr-large.jpg (source/address.jpg).
- Picture side: https://api.hcportal.eu/media/4371/conversions/pc_hcp_118_pic-large.jpg (source/picture.jpg).
- Context (cited by the reviewer, not used in the decipherment): https://en.wikipedia.org/wiki/David_Warfield ; https://en.wikipedia.org/wiki/The_Music_Master_(play) ; *San Francisco Dramatic Review*, 1908, https://lantern.mediahist.org/catalog/sanfrandram1908sanf_0702 .
- AI Decipherment Register snapshot, 2026-10-26: https://ai.hcportal.eu/register/?format=json (saved in ciphers/hcp-1440/work/register-snapshot.json).
