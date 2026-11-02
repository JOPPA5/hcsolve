REVISE

# Review 1 of hcp-1148 (Claude Opus 5.5, independent reviewer, 2026-11-02)

The cipher, the key family and the message stand: this is a real Hungarian love-letter card, and every sign decodes. Three concrete fixes are needed: one misread sign, one wrong word division, and one sign class merged into another. Two further points are minor. None of them changes the story, and no clause is unread.

## What I verified and how

- Ran `python3 -I ciphers/hcp-1148/work/decode.py`. Hashes OK (4 files). Output is 415 signs, 412 by table, 3 by sense, and it matches the plaintext in SOLUTION.md word for word.
- Wrote my own parser and key from the sister tables in `review/work/indep.py` (`python3 -I ciphers/hcp-1148/review/work/indep.py`). It gives the same letter string, and no sign falls outside the key. This check only tests the transcription's arithmetic. The pixel check is below.
- Read the whole message from my own crops of `work/hires/..._adr.jpg` at 2x (`review/work/crop.py`, output in `review/work/c/`): all 22 rows, sign by sign, every vowel mark and comma, against `work/transcription.txt`. Zoomed to 3.5x to 5x on the disputed signs (`bocs`, `valam`, `rajta`, `ugr`, `olel`, `szer2`, `lath`, `arpad`, `end15`, `mert`) and made a montage of all 12 dot-left signs (`review/work/montage.py`, `c/dotleft.png`).
- Apart from findings 1 and 3, I agree with every sign in the transcription.
- Checked key values against other cards. `6` = j, `6.` = ny, `4.` = gy and `2` = c also stand on hcp-1135, 1136, 1138, 1142 (some still in review). hcp-1174's table agrees on the shared signs.
- Picture side: no writing. Date: the stroke between `1916.` and `V` is the comma of the `7,` in the row above, so V/9 stands, and it agrees with the portal file name (1916-05-09). Postmark: only fragments are legible, as the solver says.
- Disclosed readings checked on pixels:
  - `valamit`: the odd sign has two counters, so it is a blotted 8 with its comma, and `8,` is well supported.
  - `rajta`, `jól`: `6` has no comma; the comma near rajta belongs to the 8.
  - `mert tudom`: both 8s have a comma.
  - `láthatom`: the comma of `8,` runs into the 5, as stated.
  - `ölel-`: the first sign is a plain 9-shape, by sense only, as stated; same habit on hcp-1174.
  - `szerelem` line 2: one low dot, the high position is merged into the 1/8 join, as stated.
  - `voltál`: stray low dot present, high dot clear.
  - The plain 7-shape as 1 (`ugrani`, `irok`, second b of `egyébb`) has no bar, as stated.
- Language: natural colloquial period Hungarian with a rhymed quatrain. Names fit (Margitka, Árpád). No published solution was used, and the unchecked HistoCrypt article is disclosed.

## Findings

1. **major: `bocses` is a misread sign; the card has `bocsás`.** Transcription L12 gives `1, 0 2, 1: 7,`. In `review/work/c/bocs.png` (x 90-520, y 1060-1170 of the hires scan, 4x) the 1 after `2,` has a single high dot and nothing below it. That is `1'` = á, not `1:` = e; every other e on the card shows both dots. The word is `bocsás meg`, a one-s spelling of bocsáss. Fix the transcription (`1,` `0` `2,` `1'` `7,`), the plaintext, and the "spellings kept as written" entry, which explains a form the writer did not write. Counts become `1:` 47, `1'` 15.

2. **major: `ölelés` is a wrong word division; read `ölel és`.** The letters are unchanged, but the card's closing is the family formula `üdvözöl számtalanszor, ölel és csókol hű kedvesed`: greets countless times, embraces and kisses. The same wording stands on hcp-1143 (`üdvözöl számtalanszor, ölel és csókol hű imádód`), 1146, 1151, 1162, and elsewhere. A bare noun "ölelés" between two verbs is forced. Fix the Hungarian, the English ("embraces and kisses you"), the Slovak ("objíma a bozkáva") and uncertainty 2's label. The transcription needs two entries, `ölel` and `és`.

3. **major: two signs are merged as `:1`; the card has one-dot `.1` and two-dot `:1`.** SOLUTION.md says "the one sign `:1` covers u and ü, so the spelling of these vowels is mine". The pixels contradict this (`c/dotleft.png`, all 12 instances):
   - Two dots: hazaértünk, értünk, együtt. All are ü.
   - One dot: indultunk (twice), nadrágunk, ugrani, tudom, bú. All are u/ú, none with two dots.
   - One dot in ü words: keresztül, üdvözöl, hű.

   So no u word carries two dots, and sister cards hcp-1135, 1137, 1138 and 1142 list `.1` = u separately. hcp-1139 even credits `.1` to this card, whose table lacks it. Add `.1` to the key and transcription as u, ú, with the writer's one-dot form also standing for ü in the three listed words (disclose that). Print `indultunk`, which the signs now support; the current `indultünk` is unsupported.

4. **minor: sign count.** "The 30 signs" and "25 of the 30 values" are wrong for the table given: it and decode.py have 29 signs (`indep.py`: 29 used). With `.1` from finding 3 the total becomes 30, so state the new-sign list and the 25-of-N figure accordingly.

5. **minor: brackets.** SOLUTION.md says punctuation is the solver's own and mentions only the `)` after `cselekedtem`. A second clear `)` stands after Árpád (`c/arpad.png`), and a pale slanted stroke before the first `1'` of Árpád may be its opening bracket, so `(Árpád)` is on the card, as on sister cards (hcp-1143, 1146, 1162). Disclose it. The stroke is faint, so call the opening bracket probable.

## Could not verify

- Whether the HistoCrypt article discusses this card (not checked by solver or by me).
- The postmark date: too fragmentary.
- Who "we" were, and whether the quatrain has a printed source.
- The one-dot `.1` in keresztül, üdvözöl and hű could be a lost or omitted second dot rather than a homophone. It does not affect any word.
