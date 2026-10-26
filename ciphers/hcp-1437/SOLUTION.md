# HCP 1437 / pc_hcp_118 — full candidate, pending review

The handwritten address-side message uses ordinary Latin consonants with nine
digit substitutions. All 114 message/signature positions have a reading under
one table. This is a solver candidate, not an independently accepted solution.

## Cipher and key

| Cipher digit | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
| Plain letter | A | E | I | O | U | T | N | S | R |

Remaining handwritten Latin letters retain their ordinary values. There are
72 digit positions and 42 unchanged Latin-letter positions. Case is normalized
to uppercase in the output, without changing spelling or punctuation.

## Literal reading

```text
HAVE BEEN TO
OAKLAND ONCE.
WAS. IN. SAN FRANCISCO
YESTERDAY WITH
CASPERS WIFE AND
SAW DAVID WAKEFIELD
PLAY THE MUSIC
MASTER. IT WAS FINE.
SKIPP.
```

Suggested word-level interpretation: “Have been to Oakland once. Was in San
Francisco yesterday with Caspers wife and saw David Wakefield play The Music
Master. It was fine. Skipp.” An apostrophe in “Casper's” and title formatting
would be editorial; neither was added to the literal reading. Do not replace
WAKEFIELD with a historically expected performer's name.

Slovak translation of that interpretation: „Bol(a) som raz v Oaklande. Včera
som bol(a) v San Franciscu s Casperovou manželkou a videl(a) som Davida
Wakefielda hrať v The Music Master. Bolo to pekné. Skipp.“ The title-like
construction is a reading of the postcard's syntax, not an external theatre
identification.

## Reproduction

From the repository root:

`python3 ciphers/hcp-1437/work/decode.py`

No supplied transcription exists. `work/transcript.txt` is my own manual
digit/Latin trace from `source/address.jpg`; the decoder checks hashes of both
original scans and metadata, applies the table, and checks inverse encoding.
The command does not perform image recognition. Hash/roundtrip checks verify
the captured files and mapping, not independent agreement with the ink.

`work/message-large.jpg` covers the whole message; `name-line-large.jpg` and
`companions-line-large.jpg` expose the two name readings at greater scale.
Source coordinates below refer to the original 1024×674 address scan.

## Readings that need review

- The first glyph of OAKLAND (about x109,y264) is overwritten. It is traced as
  4, matching the 4 in TO and ONCE; the underlying crossed stroke is not an
  extra plaintext letter. The frozen group is `41kl17d`.
- CASPERS (about x98–258,y390) is `C18p298`. The p has a long descending
  diagonal; compare p in PLAY and the two signature p strokes. An h reading
  would produce CASHERS; that alternative is disclosed, but its missing
  descender would disagree with the traced p. The surname's owner is unknown.
- WAKEFIELD (about x308–424,y443) is `W1k2f32ld`. The tall loop/branch is
  traced as ordinary k, followed by 2 (E), then f. The same k style occurs in
  OAKLAND and SKIPP. This is the postcard's literal name reading; no historical
  actor identification is claimed. The dense final `32ld` joins handwriting
  but gives I-E-L-D under the same table.
- WAS. IN. preserves the two small separator-like dots. Reading them as full
  stops or casual word dividers changes punctuation, not decoded letters.
- SKIPP (`8k3pp`) is a literal signature reading, not a securely identified
  person. No sender identity or recipient relationship is inferred from it.

Printed publisher text, address, stamp/postmark, and the picture-side printed
caption are outside the handwritten cipher scope. The picture side has no
additional handwritten cipher visible. The printed Oakland caption agrees
with the decoded Oakland reference but supplied no letter substitutions.

## Evidence and limits

The nine-value table works across the whole message: common sequences BEEN,
ONCE, YESTERDAY and the longer SAN FRANCISCO independently repeat its values.
No word-specific substitutions or external plaintext were used. Root captured
all three portal tabs; the current saved status is Not solved. No attached or
published solution was encountered. No independent review has occurred; no
FINAL, report or register entry is justified yet. Watchers were not started,
following the user's standing override.

## Response to review 1

Reviewer: Claude Opus 5.5, verdict ACCEPT (review/REVIEW1.md, 2026-10-26). The reviewer read the whole message from source/address.jpg independently, sign by sign, and decoded its reading with its own script. All 114 letter positions agree with work/transcript.txt; the only difference is one full stop. No letter of the plaintext changes.

1. One full stop omitted (minor). Accepted. Row 4 has a clear dot after `y28629d1y`, of the same kind as the dots in `W18.` and `37.`, so the literal reading is `YESTERDAY. WITH`. The correction is made here and in the report; work/transcript.txt and the output of work/decode.py are left unchanged and therefore still lack this dot. A possible faint dot between `pl1y` and `6h2` (PLAY / THE) is too faint to be called ink; it is disclosed as an uncertainty and not added to the literal text. Neither dot changes a letter.
2. The strongest context was hidden (minor). Accepted. *The Music Master* (Charles Klein, produced by David Belasco in 1904) was the vehicle of the actor David Warfield, who played Anton von Barwig in it from 1904 to 1908, and a 1908 issue of the *San Francisco Dramatic Review* reports a run of "David Warfield in The Music Master" in San Francisco (reviewer's sources, cited as context: https://en.wikipedia.org/wiki/David_Warfield , https://en.wikipedia.org/wiki/The_Music_Master_(play) , https://lantern.mediahist.org/catalog/sanfrandram1908sanf_0702 ; the exact week of the run was not established). The ink reads `W1k2f32ld` = WAKEFIELD, not `W19f32ld` (WARFIELD): the k matches the k of OAKLAND and SKIPP, and the digit 9 in this hand descends below the line. The literal plaintext therefore keeps WAKEFIELD, and the report states openly that the writer most probably misspelled or misremembered the name Warfield. That the decoded text names the right first name and the right play in San Francisco in 1908 is independent confirmation of the decipherment and is now part of the evidence. The earlier sentence "not an external theatre identification" is superseded by this paragraph.
3. Near-homographs not disclosed (minor). Accepted and added to the uncertainties: (a) the first c of FRANCISCO and the c of MUSIC are written as a looped, e-like cursive c; since E is always the digit 2 in this system, they must be c; (b) the capital F of FRANCISCO is a 7-like capital, distinguished from the digit 7 (= N) by its flat top bar, its size and the context.
4. Plain-text context not recorded (minor). Accepted. The postmark reads MILL VA[LLEY] SEP 25 5 PM 190[8] (the last year digit and the hour are partly under the stamp; the year 1908 rests on the portal). 1908-09-25 was a Friday, so "yesterday" was Thursday 24 September. Mill Valley (Marin County) lies across the bay from San Francisco and Oakland. The card is addressed in plain script to Mrs S. J. Briggs, Canaan, Conn., Box 275, which agrees with the portal recipient Briggs. The publisher imprint is Newman Post Card Co., Los Angeles; the picture side shows the Bell Tower & Chimes, Mills Seminary, Oakland, Cal. The portal language "Unknown" is, on the evidence of the plaintext, English. These corrections are recorded here and in the report; source/metadata.md is unchanged.

Remaining uncertainties carried into the report: the underlying stroke beneath the overwritten 4 of OAKLAND; the p/h choice in CASPERS (p, with the descender, is read by both solver and reviewer); the identity of Skipp (sender) and Casper; the exact dates of Warfield's 1908 San Francisco engagement; a wider search for an earlier published decipherment was not made (the portal showed Not solved and the same-day register snapshot has no entry for 1437 / pc_hcp_118).

Closing steps (this response, report, register entry, FINAL) prepared by Claude Opus 5.5 on the solver's behalf at the human's request, 2026-10-26.
