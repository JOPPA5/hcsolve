# HCP 1486 (pc_hcp_167): an English postcard in reversed writing, Will to Miss A. Russell, c. 1905

Human solver: Tomáš Pavuk

**Status: deciphered in full (all seven cipher lines, every letter); independent review 1 verdict ACCEPT, no change to the reading.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1486 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1486), portal name pc_hcp_167, part of the HCPortal collection of cryptographic postcards (private collection). When it was captured on 2026-10-26 the portal listed it as **Not solved**, category Substitution, used around 1905, language Unknown, location Europe, sender Will, recipient A. Russell, with no transcription or solution attached.

The address side is printed "POST CARD", "Trichromatic P.C. by J. Welch & Sons, Portsmouth, Printed at our Works in Belgium". It carries a green halfpenny King Edward VII stamp (the Edward VII issue began in 1902) with an illegible cancellation, and the address in plain writing: **Miss A. Russell / Mill House / Bugsell / Etchingham / Sussex.** Bugsell is probably the hamlet of that name near Hurst Green and Salehurst, a few kilometres from the post town Etchingham in East Sussex (not checked against a map). The earlier portal capture (source/metadata.md) read the place as "Buxted [reading provisional]"; the scan clearly shows "Bugsell".

The message stands on the left half of the address side: seven lines of dotted, strange-looking writing, followed by the plain sign-off **S.W.A.K. Will** ("Sealed With A Kiss"). The picture side is a hand-coloured photograph of a young couple embracing in a wood, titled "Language of Flowers" with an inset of forget-me-nots and the caption "Forget-me-not – True Love". It carries no cipher text.

![Address side: the seven dotted lines and the plain sign-off at the left, the address at the right (source/address-large.jpg)](../source/address-large.jpg)

![Picture side: "Language of Flowers", "Forget-me-not – True Love" (source/picture-large.jpg)](../source/picture-large.jpg)

## Method

Earlier work: an OpenAI GPT solver (GPT-6 Astra) captured the portal page, the two scans and the metadata on 2026-10-26 and triaged the card as "custom dotted letterlike correspondence", without a reading. Claude Opus 5.5 then made the transcription and decipherment.

The body was enlarged 3–7× line by line. At first sight it looks like an invented alphabet, but several groups are ordinary cursive letters in reverse order: **k.n.i.h.t** is "think", **y.a.d.s.e.u.T** is "Tuesday", **n.w.o.d** is "down", **t.h.g.i.N** is "night". The letters themselves are not mirrored (a mirrored copy of the scan was checked); only the order of letters and words in each line runs **right to left**. The many dots, above, below and between the letters, have no positional regularity and are **nulls**, added to make the writing look like a cipher.

Because each word was written starting at its right end, its first letter (written first) often has a flourished or capital-like shape. These initial forms account for all the "strange" signs; everything else is ordinary handwriting. The transcription (work/transcription.txt) records each line in visual left-to-right order, with word gaps and a label for each flourished initial; the script reverses each line, drops the dots and prints the plaintext.

![The cipher body enlarged (work/body.png, crop made in review)](../work/body.png)

## Key

Not a substitution: **reversed writing with null dots**. Read each line from its right end to its left end, top line first, and ignore the dots. The flourished word-initial forms have these values:

| Sign (initial form) | Where it occurs | Value |
|---|---|---|
| crossbar with two short legs (pi-like capital T) | think, this, Tuesday | t / T |
| crossbar with one 3-/z-shaped stem descending below the line | bit, be / hope | b / h (from context) |
| looped sign with long tail | you (twice) / quite | y / q |
| crossed loop standing alone | twice | the word "a" |
| loop with descender | are | a |
| w-forms | well, with | w |
| 3-shaped sign | night | n |
| horizontal loop | love | l |
| open loop | Sha(ll) | S |
| tall looped stroke without crossbar | fright | f |
| capital D | Dont | D |
| M-like sign at the end of "you" | twice | u |

![The two crossbar forms: think, this, Tuesday (two legs, = t) and bit, hope, be (single descending stem, = b/h) (work/sign-forms.png, panel made in review)](../work/sign-forms.png)

## Plaintext

Transcription in visual order (as on the card; "." = null dot, "|" = word gap, [..] = flourished initial):

```text
L1: . [U] . o . [Y:y] | . t . n . o . [D]
L2: [X] . | s . i . h . [T:t] | . k . n . i . h . [T:t]
L3: . t . h . g . i . r . [F] . | [X] | . f . o . | t . i . [B:b]
L4: l l . | e . r . [A] . | [U] . o . [Y:y] . | e . p . o . [B:h]
L5: a . h . [S] . | l . l . e . [W] . | e . t . i . u . [Y:q]
L6: y . a . d . s . e . u . [T:T] . | n . w . o . d . | e . [B:b]
L7: e . v . o . [L] | h . t . i . [W] . | t . h . g . i . [N]
```

Literal English, each line read right to left:

```text
L1  Dont you
L2  think this a
L3  bit of a fright
L4  hope you are ll
L5  quite well Sha
L6  be down Tuesday
L7  night with love
    S.W.A.K.  Will
```

Normalized English (punctuation editorial; bracketed letters are not on the card):

**Don't you think this a bit of a fright? Hope you are [a]ll quite well. Sha[ll] be down Tuesday night. With love, S.W.A.K., Will**

"This" presumably refers to the picture on the other side, the couple in the wood.

Slovak translation: **Nezdá sa ti toto trochu strašné? Dúfam, že ste všetci celkom zdraví. Prídem v utorok večer. S láskou, S.W.A.K. (zapečatené bozkom), Will**

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1486/work/decode.py
```

The script uses only the Python standard library. It checks the SHA-256 hashes of the two scans and the metadata in source/, reads the manual transcription in work/transcription.txt, reverses each line, drops the null dots and prints the seven plaintext lines and the running text. It does not read the image; the transcription step is manual and was confirmed independently in review.

## Uncertainties

- **b/h from context.** The descending-stem crossbar sign stands for b in "bit" and "be" and for h in "hope". These two values come from context, not from distinct shapes; other values give no words ("tit of", "tope"). It may simply be the writer's flourished capital B/H.
- **"ll" for "all".** Line 4 has only "ll" after "are"; the writer omitted the a. Not restored in the literal text.
- **"Sha" + "be".** Line 5 ends "Sha" and line 6 begins "be": "Shall be", with "ll" omitted. The second sign of line 6 is a small loop a little taller than x-height, read e (the same form as the e of "quite"). If it were "ll" the text would be "Shall down Tuesday night", with the same meaning.
- **Open-loop S** of "Sha" is an unusual form; only "Sha(ll)" fits the following line.
- **"Dont"** has no apostrophe on the card.
- **Dots** are treated as nulls; they were not recorded individually.
- The identities of "Will" and of Miss A. Russell of Mill House were not researched; the location of Bugsell was not checked against an external source; the postmark date is illegible, so the date rests on the stamp (Edward VII, from 1902) and the portal's "around 1905".

## Review summary

Reviewer: a separate Claude Opus 5.5 agent (Anthropic), round 1, verdict **ACCEPT**. Because the solver of round 1 was also Claude Opus 5.5, the review was not cross-provider. The reviewer ran the reproduction command (output identical to SOLUTION.md), made its own 2–5× crops of every line, wrote its own visual transcription with its own sign labels and its own decoder (review/work/indep_decode.py), and obtained identical plaintext. It confirmed the reversed order on the pixels, that the letters are not mirrored, that the dots are irregular nulls, the omissions "ll" and "Sha", the e in "be", the f in "fright" and the stand-alone "a" signs, and that no published solution was used. Its four minor findings and what changed:

- **Two crossbar forms.** The solver had described a single polyvalent T-shaped sign for t, b and h. The reviewer showed two forms: two short legs (always t) and one descending stem (b/h). The key table, the transcription labels ([T] and [B]) and the uncertainties now separate them; the reading is unchanged.
- **Bugsell.** The "[Buxted?]" alternative was dropped; Bugsell near Etchingham is given as probable.
- **Dates.** Dates are now given in UTC consistently.
- **Restorations.** "[a]ll" and "Sha[ll]" stay bracketed and are not silently normalized.

No letter of the reading changed as a result of the review.

## Sources

- HC Portal record 1486, General, Description and Attachments tabs, captured 2026-10-26: https://crypto.hcportal.eu/dashboard/cryptograms/1486 (source/metadata.md).
- Address side: https://api.hcportal.eu/media/4519/conversions/pc_hcp_167_adr-large.jpg (source/address-large.jpg).
- Picture side: https://api.hcportal.eu/media/4518/conversions/pc_hcp_167_pic-large.jpg (source/picture-large.jpg).
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-29: no entry for this card.
