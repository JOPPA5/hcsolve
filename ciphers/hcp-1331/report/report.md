# HCP 1331 (pc_hcp_12): "Dear Old Boy", an English postcard from Ada with dots for letters

Human solver: Tomáš Pavuk

**Status: read in full, with 13 dotted letters and one doubtful sign restored by word sense; independent review 1 verdict ACCEPT, no change to the text.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1331 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1331), portal name pc_hcp_12, part of the HCPortal collection of cryptographic postcards. When captured on 2026-10-30 the portal listed it as **Not solved**, category Unknown, date Unknown, language Unknown, location Europe, sender Ada, recipient F. Stuniger, with no transcription or solution attached.

The picture side is a real-photo portrait captioned **Miss Madge Crichton**, with the printed marks RAPID PHOTO E.C. and 3623, and no handwriting.

The address side is scanned sideways. Turned upright it shows the address on the right half: **Mr F. Stringer, "Easebourne", Midhurst** (the portal reads the surname as Stuniger). The message fills the lower left of the same side. The stamp is an Edward VII halfpenny with the numeral 381 obliteration, beside a HORSHAM datestamp reading 8 PM, AU 4. The year is illegible, so the card can be dated only to the Edward VII stamp period.

The large ring with the alphabet is the HCPortal watermark, not part of the card.

![Address side turned upright. The dotted words are in lines 1, 3 and 4 of the message (work/adr-upright-ccw.png)](../work/adr-upright-ccw.png)

![Picture side as scanned: Miss Madge Crichton (source/picture-large.jpg)](../source/picture-large.jpg)

## Method

No cipher in the usual sense is involved. The solver (Claude Opus 5.5) rotated the hi-res original, enlarged each line and read it by eye. Six of the nine lines proved to be ordinary English. In the other three, some letters are replaced by one written dot each, and the remaining letters keep their own values.

The solver tested two rules for choosing the letters. "Vowels only" fails, because l in Old, s in last, h in night and r in dearie are dotted. No regular position rule fits either. Each masked word was then matched against the system word list (work/candidates.py), and the phrase in context chose among the candidates. The concealed words are the affectionate ones: the salutation and "miss you last night dearie". The train time and the rehearsal news are in clear.

## Key

There is no key. The method is **letter suppression: a dot for each omitted letter**, in English, on selected words only. The reader fills in the letters from sense. A dot carries no information about its letter, so unlike a substitution this cannot be proved by decryption; it can only be shown to be the natural reading.

| Written | Read | Dotted letters |
|---|---|---|
| `D..r O.d B.y` (underlined) | Dear Old Boy | e a, l, o |
| `M.ss y.u` | miss you | i, o |
| `l..t n.g.t` | last night | a s, i h |
| `de...e` | dearie | a r i |

That makes 13 dots in 8 words. The r of `D..r` is a small 2-shaped form, and the d of `O.d` is a looped delta form.

![Enlargement of de...e: the blotted second sign, then three dots and the final e (review/work/l4b.png)](../review/work/l4b.png)

## Plaintext

The card as written, line by line:

```text
D..r O.d B.y
Train arrives at Midhurst
9-54. Did M.ss y.u
l..t n.g.t de...e
I went to the Rehearsal
but we did not have
the Pole last night
rather silly I think
yours with love Ada
```

Restored English:

```text
Dear Old Boy
Train arrives at Midhurst
9-54. Did miss you
last night dearie
I went to the Rehearsal
but we did not have
the Pole last night
rather silly I think
yours with love Ada
```

English sense: **Dear Old Boy, the train arrives at Midhurst at 9.54. [I] did miss you last night, dearie. I went to the rehearsal, but we did not have the Pole last night; rather silly, I think. Yours with love, Ada.**

Slovak translation: **Drahý starý chlapče, vlak prichádza do Midhurstu o 9.54. Včera večer si mi naozaj chýbal, miláčik. Išla som na skúšku, ale včera večer sme nemali „Pole"; dosť hlúpe, myslím. S láskou tvoja Ada.**

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1331/work/decode.py
```

The script uses only the standard library. It checks the SHA-256 hashes of both scans and both hi-res originals, checks that the hard-coded transcription and expansion agree letter by letter, and prints the nine lines with a count of 13 dotted letters. It does not read the image: the check is internal, and the transcription rests on reading the scan. `python3 -I ciphers/hcp-1331/work/candidates.py` gives the word-list evidence (it needs /usr/share/dict/words).

## Uncertainties

- **All 13 dotted letters rest on word sense.** `y.u` has one list candidate. `D..r`, `O.d`, `B.y` and `M.ss` are fixed by the set phrases.
- **`l..t`** has 19 list candidates. "last" is chosen because the writer has "last night" in clear three lines lower. The first sign has a stroke across its stem and could be taken for t, which would allow "that night". It is kept as l: the upper stem is doubled, as in a closed loop, and the stroke does not continue right of the stem as a t bar does.
- **`n.g.t`:** the third sign is not a clean g but a very small flat hook, looking more like a tiny c or r. Neither of those gives a word, so g rests on word sense. A thin broken mark below it may be an ink-starved tail or a speck. If the hook were a misshapen dot, the word would still be night, with 14 dots.
- **`de...e` = dearie is the weakest word.** The second sign is blotted; e is the reading, and a is not excluded. The word list gives 51 words for de...e and 31 for da...e, but only dearie completes the phrase. There are exactly three dots.
- **"the Pole"** is clear on the pixels, but its meaning is unknown: a prop, a person or a nickname. The capital was tested against R, which this writer shapes differently in Rehearsal.
- **"rather" and "silly"** lie at the card's edge, overlapped by the printer's imprint and the descenders of the line above. They are the only sensible reading.
- **Addressee.** Stringer is preferred to Strunger, since a small tick above the name fits this writer's displaced i-dots. The portal's Stuniger looks like a misreading. This does not affect the message.
- **Easebourne** stands in quotation marks, so it may be a house name rather than the village; this is unresolved.
- **Date.** Only the Edward VII stamp dates the card; the year in the postmark is illegible. The link between numeral 381 and Horsham rests on the two strikes appearing together, not on an outside reference.
- **Why these letters were chosen** is unknown. The writer's motive, keeping the tender words from the eyes of the postman, is an inference.
- **Hidden dots.** The watermark is translucent and ink of this weight shows through it, but a dot wholly hidden cannot be excluded in theory.
- **Prior publication.** None was found on the portal, and the AI Decipherment Register had no record on 2026-10-30. No wider web search was made.

## Review summary

Reviewer: a separate Claude Opus 5.5 agent, round 1, verdict **ACCEPT**. Solver and reviewer are the same model, so this is not the two-provider check the workflow prefers. The reviewer ran the command, wrote its own transcription and expansion (review/work/verify.py, identical result, though this shows agreement only, since both are expansions by sense), and checked all lines on its own crops of the hi-res original. It confirmed the 13 dots, the clear lines, "Pole" against "Role", and the word-list counts, and it identified the dots near lines 6 to 8 as i-dots. Its six findings were all minor, and all were accepted:

- **First sign of l..t:** the possible t is now disclosed.
- **Tail under the hook of n.g.t:** now disclosed, with the 14-dot case.
- **Stringer:** the claim that the i is undotted was wrong and is corrected.
- **hcp-1463:** a note wrongly said it shares the sender Ada, whereas Ada is its addressee. Corrected; that card was never used.
- **What the script proves:** the wording now says the check is internal, and the other dots on the card are explained.
- **Easebourne:** the argument that it is adjacent to Midhurst was dropped, and the word is left unresolved.

No letter of the text changed. All work on this card, from transcription to closing, was done by Claude Opus 5.5, with no earlier GPT work.

## Sources

- HC Portal record 1331, all three tabs, captured 2026-10-30: https://crypto.hcportal.eu/dashboard/cryptograms/1331 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/4053/conversions/pc_hcp_12_pic-large.jpg (source/picture-large.jpg); original https://api.hcportal.eu/media/4053/pc_hcp_12_pic.JPG (work/hires/).
- Address side: https://api.hcportal.eu/media/4054/conversions/pc_hcp_12_adr-large.jpg (source/address-large.jpg); original https://api.hcportal.eu/media/4054/pc_hcp_12_adr.JPG (work/hires/).
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked by the orchestrator on 2026-10-30.
