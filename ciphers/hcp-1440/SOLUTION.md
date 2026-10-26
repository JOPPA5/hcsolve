# HCP1440 / pc_hcp_121 — full cipher-passage candidate

Awaiting independent review, not an accepted solution.

## Source and scope

Fresh Not solved status2026-10-26; all three portal tabs inspected.
No attached transcription or solution. The encrypted passage consists of
two short lines above the ordinary cursive letter on the address side.
All19 Pigpen letters are covered. The rest of the letter, date4-17-08,
ordinary Ha Ha, address/signature and printed Easter picture are outside
the cipher count. Both original scans were inspected; no further Pigpen
passage was observed on the picture side.

Portal date1908-04-17, recipient Ray Bartley, sender unknown. Ordinary
address gives Laurens, Iowa. English is the decoded language; portal
language is Unknown. The sender's visible ordinary initials are not
expanded to an identified person.

## Key

Three-count Pigpen grid. Tokens name strokes PRESENT, then dot count:
BR bottom/right; B bottom/left/right; BL bottom/left;
R top/bottom/right; C all four; L top/bottom/left;
TR top/right; T top/left/right; TL top/left.

| Outline | 1 dot | 2 dots | 3 dots |
|---|---|---|---|
|BR|A|J|S|
|B|B|K|T|
|BL|C|L|U|
|R|D|M|V|
|C|E|N|W|
|L|F|O|X|
|TR|G|P|Y|
|T|H|Q|Z|
|TL|I|R|unused|

Unused entries are conventional key completion, not additional evidence.

## Literal plaintext and translation

```text
DONT YOU WISH
YOU COULD
```

With editorial punctuation: “Don't you wish you could?” The adjacent
ordinary cursive says “Ha Ha.” The cipher does not state the object of
“could”; no missing word is supplied.

Slovak: „Neprial by si si, aby si to tiež mohol?“ This is a contextual
translation of the taunting question, not extra decoded text.

## Reproduce

From repository root:

```sh
python3 ciphers/hcp-1440/work/decode.py
```

It checks source hashes, decodes all19 explicitly manual tokens, and tests
inverse-key roundtrips. It does not read image pixels automatically. The
transcript was made from source/address.jpg and work/header-large.jpg;
it is an own reading, not a supplied transcript or ground truth.

## Evidence and limitations

One fixed key reads both lines. YOU appears twice with the same three
signs. D and O repeat consistently in DONT and COULD; U repeats with three
dots. The adjacent Ha Ha fits the sense, but is supporting context only.
Some small dots touch the outlines, especially three-dot W and U; review
should check the enlarged header against the original. No unresolved
alphabetic sign remains in the proposed reading, and no per-word key
exceptions are used.

Other Ray Bartley postcards were encountered nearby in the portal, but
their content was not used as a supplied plaintext. Same addressee does
not prove an identical key or sender. No published solution consulted.
Fresh public register snapshot110records has no exact source URL or
pc_hcp_121 match; this does not prove historical novelty.

No formal reviewer has accepted this candidate. No FINAL, PDF report or
register entry is claimed before that review.

## Response to review 1

Reviewer: Claude Opus 5.5, verdict ACCEPT (review/REVIEW1.md, 2026-10-26). The reviewer transcribed the two header rows from source/address.jpg independently and decoded them with its own script; its 19 tokens agree with work/transcription.txt at every position. The plaintext is unchanged.

1. The N of DONT (minor). Accepted and added to the uncertainties. The closed box has one clear dot inside at the left; the second "dot" is a dark mark merged into the right-hand side of the box. Read strictly as one dot, the sign would be E (DOET). The two-dot reading N is adopted because only it gives a word; this is a context-based reading of an imperfect sign.
2. Two specks above the D of COULD (minor). Accepted and added to the uncertainties. The final sign (`]`, one dot inside = D) has two small specks just above its top stroke, outside the outline. Counted as dots they would make it three-dot `]` = V (COULV). They are not counted: every other dot in both rows sits inside its outline, and these specks are smaller than the real dots. Whether they are ink or paper defects is not established.
3. The I of WISH (minor). Accepted and added to the uncertainties. The left stroke of the `┌` (I) runs down into the printed caption "This Space for Writing Messages". No bottom stroke is visible, so the sign is not `[` (F, which would give WFSH).
4. Context left out (minor). Accepted. 1908-04-17 was Good Friday (Easter Sunday was 19 April 1908), which matches the "Easter Greetings" picture side. The cipher is followed directly by a plain "Ha Ha."; the plain letter below tells of going to Lodge and dancing although someone "didn't want us to dance but we did it anyway", of sitting up all night, and of wanting to go to a play in Humboldt. It is signed with the plain initials R.E.B. The postmark reads RUT[LAND] APR 1? … PM 1908 IOWA (the day digit and hour are covered by the printed "POST CARD" ornament). The address is Mr Ray Bartley, Laurens, Iowa. A teasing "Don't you wish you could? Ha Ha." fits this letter; no object for "could" is supplied. These additions are made here and in the report; the initials are not expanded to an identified person, and source/metadata.md is unchanged.

Remaining uncertainties carried into the report: findings 1–3 above; the postmark day digit; a wider search for an earlier published decipherment was not made (the portal showed Not solved and the same-day register snapshot work/register-snapshot.json has no entry for 1440 / pc_hcp_121).

Closing steps (this response, report, register entry, FINAL) prepared by Claude Opus 5.5 on the solver's behalf at the human's request, 2026-10-26.
