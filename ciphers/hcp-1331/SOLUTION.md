# hcp-1331 (pc_hcp_12) — solution

Solver: Claude Opus 5.5, 2026-10-30. No earlier work on this number, no solution attached on the portal, and none found.

## Cipher type and key

**Letter suppression by dots ("dotted" concealment), English, with the rest of the card in clear.** It is not a substitution. Selected letters are replaced by one dot each, and the written letters keep their own values. There is no key: the dots follow no rule I could find (they hit vowels and consonants alike: l in Old, s in last, h in night, r in dearie), so the reader fills them in from sense. Only 2 of 9 lines are concealed in part, plus the salutation: the private, affectionate words. The train time and the rehearsal news are in clear.

Portal category is Unknown. Suggested label: letter omission / dots for letters (not a MASC).

## Transcription of the concealed words

Message is written across the left of the address side, rotated 90 degrees. `.` = one written dot.

| Written | Read | Dotted letters |
|---|---|---|
| `D..r O.d B.y` (underlined) | Dear Old Boy | e a, l, o |
| `M.ss y.u` | miss you | i, o |
| `l..t n.g.t` | last night | a s, i h |
| `de...e` | dearie | a r i |

13 dots in all. The `r` of Dear is the small 2-shaped form; the `d` of Old is a looped delta form.

## Plaintext (English)

    Dear Old Boy
    Train arrives at Midhurst
    9-54. Did miss you
    last night dearie
    I went to the Rehearsal
    but we did not have
    the Pole last night
    rather silly I think
    yours with love Ada

Address: Mr F. Stringer, "Easebourne", Midhurst. Printed on the picture side: Miss Madge Crichton, Rapid Photo E.C., no. 3623.

## Translations

**English sense:** Dear Old Boy, the train arrives at Midhurst at 9.54. [I] did miss you last night, dearie. I went to the rehearsal, but we did not have the Pole last night; rather silly, I think. Yours with love, Ada.

**Slovensky:** Drahý starý chlapče, vlak prichádza do Midhurstu o 9.54. Včera večer si mi naozaj chýbal, miláčik. Išla som na skúšku, ale včera večer sme nemali „Pole"; dosť hlúpe, myslím. S láskou tvoja Ada.

## Single command (from the repo root)

    python3 -I ciphers/hcp-1331/work/decode.py

It checks the SHA-256 of both source images and both hi-res originals, checks that the hard-coded transcription and the hard-coded expansion agree with each other letter by letter (an internal consistency test, not a check against the image), and prints the full plaintext. Pattern evidence: `python3 -I ciphers/hcp-1331/work/candidates.py` (output in `work/candidates.txt`; needs `/usr/share/dict/words`).

## Uncertainties

1. **All 13 dotted letters rest on word sense**, since a dot carries no information. Each word was checked against the system word list: `y.u` has one candidate; `D..r`, `O.d`, `B.y` and `M.ss` are fixed by the set phrases Dear Old Boy and miss you.
2. **`l..t`** has 19 list candidates (lost, left, lust…). "last" is chosen for the phrase with night, which the writer also has in clear three lines lower. The first sign itself could be taken for t, because a stroke runs across its stem, which would allow `t..t` = "that night" (31 list hits for t..t). I keep l: the upper stem is thick and doubled, as in a closed loop, and the cross stroke does not continue to the right of the stem as the bar of the final t does, so it is an entry stroke.
3. **`n.g.t`: the third sign is not a clean g.** It is a very small flat hook, clearly more than a dot, and at the pixel level it looks more like a tiny c or r. `n.c.t` and `n.r.t` give no list word, while `n.g.t` gives night. So the g rests on word sense. Below the hook, inside the grey watermark ring, is a thin broken mark running down-left, the direction of this writer's g and y descenders. It may be an ink-starved tail, which would make the hook a real g, or only a speck; it is not settled. If the hook were instead a misshapen dot, the word would still be night and the dot count 14.
4. **`de...e` = dearie rests on word sense.** The second sign is a blotted small letter with a tail: e is my reading, a is not excluded. The list gives 51 words for de...e (decide, desire, degree…) and 31 for da...e, but only dearie completes "did miss you last night …". This is the weakest word. There are clearly three dots between the blot and the final e.
5. **"the Pole"** is clear on the pixels (capital P, then o-l-e), but its meaning is unknown: perhaps a prop, a person or a nickname. Not explained, and the Slovak keeps it in quotation marks.
6. **"rather" and "silly"** lie at the card's edge, overlapped by the printer's imprint and by the descenders of the line above. The opening `r` is a little open and could look like `o`; the `s` of silly looks like `p`. "rather silly" is the only sensible reading.
7. **Addressee:** the surname looks like *Strunger* or *Stringer*; the portal gives *Stuniger*. A small tick above and to the right of the middle of the name fits this writer's displaced i-dots and favours "Stringer" (my first statement that the i is undotted was wrong). This does not affect the message.
8. **Date:** postmark HORSHAM, 8 PM, AU 4, numeral 381 on an Edward VII halfpenny stamp. The year is not legible (only a fragment under the date line), so the card is dated only to the Edward VII stamp period. The portal gives date Unknown.
9. The ring-shaped portal watermark overlies the concealed lines but is translucent. Dots were checked through it on enlarged crops, though a dot wholly hidden by it cannot be ruled out in theory.

## Why I believe it is correct

- All 13 concealing dots fall into the 8 restored words, and the letter counts match exactly (checked by script against the hard-coded transcription, not against the image). The only other dots near the message are the writer's displaced i-dots over silly, think and night, and the full stop after 9-54.
- The restored words make a natural, coherent line in the same voice as the clear text: an affectionate salutation and "did miss you last night, dearie", and the concealed words are exactly the ones a writer on an open postcard would hide.
- Context fits: the address and the message both name Midhurst, the card is posted at Horsham, also in Sussex, and it is signed Ada as the portal says. "Easebourne" stands in quotation marks in the address, which suggests a house name rather than the village, so it is left unresolved and gives no support.

## Credit

Transcription and reading by Claude Opus 5.5. No earlier work used.

## Response to review 1

Verdict ACCEPT. No letter of the plaintext changed. The reproduction command was re-run after the edits: hashes OK, 13 dotted letters, the same 9 lines.

1. **First sign of l..t could be t: accepted, disclosed.** I viewed `review/work/first_l.png` and agree with the reviewer's description and its conclusion. Uncertainty 2 now states the t..t alternative and why l is kept.
2. **Tail under the n.g.t hook: accepted, disclosed.** The mark is visible in `review/work/hook_tail2.png`, thin and broken. Uncertainty 3 now mentions it as unsettled, and the 14-dot case.
3. **"The i is undotted": accepted, corrected.** The tick is visible in `review/work/name.png`. Uncertainty 7 is corrected; Stringer is now better supported.
4. **hcp-1463 and the name Ada: accepted, corrected.** Its metadata gives Sender Unknown and an ordinary address to Miss Ada Nicholls. NOTES.md is corrected; the card was never used.
5. **Wording of what the checks prove: accepted, corrected.** The command description and the first "why correct" point now say the check is internal, and the other dots on the card are named as i-dots and one full stop. The final message of `work/decode.py` was reworded to match; its logic did not change.
6. **Easebourne: accepted, corrected.** The adjacency argument is dropped and the word is treated as unresolved.
