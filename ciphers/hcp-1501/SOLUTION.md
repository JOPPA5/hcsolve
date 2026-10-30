# HC Portal 1501 (pc_hcp_182) - solution

Status: **complete reading**, handed to review as round 1. Solver for this round: Claude Opus 5.5
(claude-opus-5-5), acting as solver on 2026-10-30. The earlier GPT solver (GPT-6 Astra / GPT-6.1 Sol, 2026-10-26)
captured the source images and metadata, inspected all three portal tabs, and noted the Morse-like
appearance as a hypothesis; it produced no transcription, key or plaintext. Everything below the
source capture (segmentation, code, transcription, decoding) is new work done in this round.

No published solution was found or used: the portal status is "Not solved", it has no attached
transcription or solution, and the orchestrator's check of the AI Decipherment Register (2026-10-29)
found no record for this card.

## Cipher type and key

**International Morse code, hand-drawn with an unusual sign set** (no secret key). On the address side, in
33 lines drawn with a pen, the writer uses four kinds of mark:

| mark on the card | meaning |
|---|---|
| short horizontal dash (typically 5-11 px in the 1024 px scan) | Morse *dot* |
| long horizontal dash (typically 16-27 px) | Morse *dash* |
| small round ink dot (2-4 px) | gap between letters |
| large round blob (6-10 px, clearly heavier) | gap between words |

The code groups are standard International Morse letters (A `.-`, B `-...`, ... as in the
table in `work/decode.py`). No numerals or punctuation occur. Words run on across line ends (e.g. `Y|OU`,
`KN|OW`, `S|UNDAY`). The type for the register would be "Morse code".

How it was found: measuring the marks (`work/components.py`, `work/track.py`) gave three groups:
dots, blobs, and dashes whose widths fall into two clusters (about 6-11 px and 16-25 px, with few between them).
Taking short dash = dot, long dash = dash, small dot = letter break and blob = word break, the first line decodes at once to
`YOU CAN`, and every line of the card then gives English text.

## Transcription

`work/transcription.txt`: a manual transcription of all 33 lines, made from enlarged crops (5-8x) of
`source/address-large.jpg` by Claude Opus 5.5. The automatic mark measurements were used only as an aid.
Every line was checked by eye against annotated crops (`work/annot.py`, `work/zoom.py`; crops in
`work/crops/`). The portal attaches no transcription. The picture side (Barnard Castle) carries no cipher text.
The handwritten date "March 1st 1911", the address and the postmarks are in clear.

## Command (run from the repository root)

```sh
python3 ciphers/hcp-1501/work/decode.py
```

Standard library only. It checks the SHA-256 of `source/address-large.jpg`, `source/picture-large.jpg`,
`source/metadata.md` and `work/transcription.txt`, then decodes the whole transcription. It prints each line
and the two text blocks below.

## Plaintext (English, original language)

Physical layout: lines 9-33 (below the date "March 1st 1911") are the letter. Lines 1-8, at the top of the
card and above the date, start with a handwritten "P.S." and are the postscript.

Literal decoder output, without punctuation:

> DEAR NELL JUST A LINE TO LET YOU KNOW THAT I AM STILL ALIVE AND KICKING HOPE YOU ARE THE SAME I HAD A
> LETTER FROM E JEWIT ON MONDAY I WILL SHOW YOU IT ON SUNDAY IT MIGHT INTEREST YOU WELL SO LONG TILL SUNDAY
> SWETHEART WITH BEST LOVE AND KISSES YOURS ALWAYS DEAREST GEORGE
>
> P.S. YOU CAN SEND ME A LINE BACK IF YOU LIKE ITS A LONG WEEK YOU KNOW

Edited text (punctuation added by me; spelling kept as written: "Swetheart" and "Jewit" are the writer's):

> Dear Nell, just a line to let you know that I am still alive and kicking, hope you are the same. I had a
> letter from E. (or T.) Jewit on Monday; I will show you it on Sunday, it might interest you. Well, so long till
> Sunday, swe(e)th[e?]art.¹ With best love and kisses, yours always, dearest George.
>
> P.S. You can send me a line back if you like, it's a long week you know.

¹ "[e?]": the mark read as E (a Morse dot) after H in L28 is 16 px long, nearer the dashes of that line; read literally
it would be T ("SWETHTART"). E is a context reading (see uncertainty 1). "(e)" marks the letter the writer left out.

## Slovak translation

> Milá Nell, len pár riadkov, aby si vedela, že som stále živý a zdravý (doslova „žijem a kopem“), dúfam, že
> aj ty. V pondelok som dostal list od E. Jewita; v nedeľu ti ho ukážem, mohol by ťa zaujímať. Nuž, tak zatiaľ
> do nedele, zlatko. S najvrúcnejšou láskou a bozkami, navždy tvoj, najdrahší George.
>
> P.S. Ak chceš, môžeš mi napísať pár riadkov naspäť, veď vieš, týždeň je dlhý.

## Uncertainties (all disclosed)

1. **Dash length is graded, not two clean sizes.** Most marks fall clearly into short (5-11 px) or long (16-27 px).
   Some fall between (12-16 px). I classified these by comparing them with the short and long dashes next
   to them on the same line, and in most cases the word also requires that reading:
   - read as *dot* (short): L2 SEND `E` (12 px) and ME `E` (13); L6 LONG `G` 3rd mark (12) and WEEK 2nd `E` (13);
     L9 DEAR `R` last mark (12); L17 ARE `E` and SAME `E` (12 each); L18 `I` (11, 13) and HAD `H`
     (10, 10, 12, 14) - the long dashes on that line are 26-27 px; L29 BEST `E` (13) and LOVE `L` 3rd mark (12); L32 DEAR `E` (13);
     L33 GEORGE `G` 3rd mark (12) and final `E` (14).
   - read as *dash* (long): L3 BACK `K` 1st (13); L7 KNOW `K` (13, 14); L8 KNOW `W` (13); L9 NELL `L` 2nd (14).
   - **Weakest point: L28 "SWETHEART", the `E` after `H` is a 16 px mark** (on that line the dots are 6-10 px and the dashes 17-24 px).
     By length alone it is nearer a dash, which would give `SWETHTART`. I read it as `E` (dot) because only that gives a word.
     Treat this one letter as a context-supported reading, not a clear one from the pixels.
2. **The initial in "FROM E JEWIT" (L19)** is a single 12 px mark between two word blobs. The dots on that line are 6-10 px and the dashes 16-25 px,
   so I read it as a dot, `E`. Because it stands alone, the context cannot confirm it, and `T` (dash) is the
   alternative. The surname is drawn `.--- . .-- .. -` = **JEWIT** with one T, followed by a word blob and `ON`. I give it as written.
   It may be a misspelling of Jewitt.
3. **Writer's own spellings or omissions, kept as written:** "SWETHEART" (one E is missing: after `S W E` comes directly
   `T`); "HOPE YOU ARE THE SAME" has no "I" before HOPE (L16 starts directly with `....`, which I checked on an enlargement).
4. **Marks partly crossed by other ink,** all still visible on enlargement, so none of them is a restoration:
   L10 the dash of `N` in LINE and L12 the dot of `A` in THAT (crossed by the red vertical rule); L11 the final dash of `U` in
   YOU (touches the postmark circle); L15 the first dash of `G`, L17 the dash of `A` in SAME, L18 one `T`, L20/L22/L23/L27/L29 single dashes (red rule or blots). The automatic
   measurement drops some of these marks; the transcription includes them from the visual check.
5. **Separators:** in L3 the break between `C` and `K` of BACK is a pale, slightly larger grey dot. I treated it as a letter break.
   In L29 the mark at x≈475 (5×3 px) after `O` of LOVE is read as a letter-break dot. The other choice would turn
   `...-` (V) into `....-` (the digit 4), which gives no word. Missing small dots before some blobs do not affect the reading.
6. "Nell" (salutation) versus "Miss O. Davy" (address): "Nell" may be a pet name. The code gives `-. . .-.. .-..`
   unambiguously; I make no claim about the identity.

## Why I believe it is correct

- One standard code (International Morse) with a simple mapping of the card's marks decodes **all 33 lines,
  every code group**, into valid letters. No group is invalid, and nothing is left undeciphered.
- The result is natural, idiomatic English of the period. It is a short, coherent love letter ("alive and kicking", "so long till Sunday",
  "yours always"). The P.S. at the top, already marked "P.S." in clear, decodes to a matching postscript.
- The context agrees: an English picture postcard (Barnard Castle) posted on 2 March 1911 from Brough (E. Yorks) to Gilberdyke, E. Yorks,
  and dated "March 1st 1911" in clear. The Sunday-to-Sunday rhythm ("a long week") suits a weekly courtship.
- The letter-length statistics come from independent measurements (`work/components.py`) and are not tuned to the plaintext.
  Apart from the points listed above, every mark was classified as clearly short or clearly long.

## Files

- `work/transcription.txt` - the transcription (the input of the command)
- `work/decode.py` - hash-checked decoder (the single command)
- `work/components.py`, `work/track.py`, `work/classify.py` - the mark measurements (need PIL; run with the runtime python and `-I`).
  These were an aid, and their automatic output has known errors, which the visual check corrected.
- `work/annot.py`, `work/zoom.py`, `work/crops/` - the enlarged and annotated crops used for the visual check

## Response to review 1

Review 1 (Claude Opus 5.5, separate agent) gave the verdict **ACCEPT** with five minor findings and no blocker or major.
Its independent decoder gave the same 265 groups, 0 invalid, and the same text. No letter of the reading changes.

1. **L28 SWETHEART, flag the context-read E (minor) - fixed.** `work/transcription.txt` now has comment lines at the
   end flagging this mark (16 px, literal `-` = T would give SWETHTART), and the edited text above reads "swe(e)th[e?]art"
   with a footnote. The decoder reads only the `L` lines, so its output is unchanged; the transcription hash in
   `work/decode.py` was updated, and `python3 -I ciphers/hcp-1501/work/decode.py` was re-run from the repository root:
   hash checks pass, output identical to the plaintext above. The report marks the same letter.
2. **L19 initial E/T (minor) - agreed, kept as disclosed.** The edited text now says "E. (or T.) Jewit"; a comment
   in the transcription flags the mark; the report does the same.
3. **L29 separator after O of LOVE (minor) - agreed, no change.** Flagged by a comment in the transcription and kept
   in the uncertainties (point 5).
4. **Intermediate-length marks (minor) - addressed in the report.** The report states that dash length varies from
   line to line (dots about 5-14 px, dashes about 13-27 px in the 1024 px scan) and that marks were read relative to
   the other marks on their own line, with the list of the boundary cases.
5. **Type label and sign set (minor) - agreed.** The register type is "Morse code"; the report explains in a
   sentence that the visible round dots are *separators*, not Morse dots, and that Morse dots are the short dashes.

Things the reviewer could not verify (identities of Nell / Miss O. Davy, George and E. Jewit; the physical card) remain
open and are listed in the report.
