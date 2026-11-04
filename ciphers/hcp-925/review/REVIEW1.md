ACCEPT

# Review 1 - hcp-925 (reviewer: Claude Opus 5.5, claude-opus-5-5, 2026-11-03)

## What I verified and how

1. Ran the solver's command from the repo root: `python3 -I ciphers/hcp-925/work/decode.py`.
   All four SHA-256 hashes print OK; the decoded lines are identical to the ones claimed in SOLUTION.md
   (ZUMGEBUTSTAGE / ALSICHHEUTEFRUHERUHERWAC + circled HTE / UNDANMEINENLIEBLINGDACHTE / FIELMIRDERGEDANKEEIN /
   HEUTMUSSEINGEBUTSTAGSEIN / SENDET / DEIN / LIEBLING / KATCHENHOTTUM).
2. Read the picture side myself from `work/hires/..._pic.jpg` with my own crops at 1-4x
   (`review/work/r1a.png` ... `r5a.png`, `dachte.png`, `circ.png`, `gebt1.png`, `gebt2.png`, `sig.png`,
   `sig_end.png`, `sig_o.png`; crop helper `review/work/crop.py`), every row, and wrote my reading into
   `review/work/indep_decode.py` with its own key (A-Z without J = 1-25). Run: `python3 -I review/work/indep_decode.py`.
   My row-by-row reading is digit-for-digit identical to `work/transcription.txt` (checked with diff: IDENTICAL).
   140 groups, distinct values 1-14, 17-20, 22, 25; every group decodes, none needs a second value.
3. Key: the natural alphabet-position key without J is consistent on the whole card (e.g. K = 10 in GEDANKE and
   KATCHEN, Z = 25 in ZUM, W = 22 in ERWACHTE, so J really is skipped). Not a fitted key; nothing is left over.
4. Critical signs checked on the pixels:
   - GEBUTSTAG (twice): the sign after U is "1" + looped 9 in both places (`gebt1.png`/`r1b.png`, `gebt2.png`),
     clearly different from the writer's 17, which is "1" + a curled, epsilon-like 7 (see 17 in FRUHER, MIR, DER).
     The missing R is a writer slip, correctly disclosed (uncertainty 1).
   - In the second GEBURTSTAG the "1.7" (A, G) has a short dash-like dot between 1 and 7; it is not a 17.
     Reading agrees with the solver.
   - Line-1 end "22.13": the dot after 22 is visible, the "13" is written joined. 1.3 = A C is required by
     ERWACHTE together with the circled 8.19.5 (HTE); disclosed as resting on word sense (uncertainty 3).
   - Circled group (`circ.png`): ".8.19.5" clear, the 9 has the writer's open-top form. Accept HTE.
   - DACHTE (`dachte.png`): "3.8.19"; the 8 is heavily retraced/overwritten but is an 8. The 19 matches the
     writer's 19 elsewhere. Agree.
   - Signature (`sig.png`, `sig_o.png`, `sig_end.png`): 10.1.19.3.8.5.13.8.14.19.19.20.12. The 14 has the writer's
     crossed 4 (as in 7.4.1.3) and is distinct from 19; the final sign is "1" + 2 with a long tail, i.e. 12 (M),
     not 17. KATCHEN HOTTUM confirmed as read.
   - FRUHERUHERWAC: digits 6.17.20.8.5.17.20.8.5.17.22 are clear; the doubled UHER is real on the card.
5. Language: fluent German of c. 1900 (birthday wishes from a sweetheart, "Liebling", "fiel mir der Gedanke ein",
   "heut muss ein Geburtstag sein"), matching the forget-me-not "Der Ferne ein Gruss" card and its printed love verse.
   English and Slovak translations are correct (Slovak uses feminine forms, consistent with a female sender Kätchen).
6. Address side (`review/work/adr_overview.jpg`, `adr_low.png`, `stamp.png`): Heinrich Lechtahler, Wohlgeboren,
   Volxheim, in Rh., plus one further word in a cursive I also cannot read securely. 5 Pf Germania "Deutsches Reich"
   stamp (issued from 1902, consistent with 1903). Postmark: "W..." at the left and "...ESS" at the bottom of the ring,
   which supports the solver's inference "Wöllstein (Rheinhessen)" rather than Wollstein in Posen.
7. Steganography / hidden writing: picture-side edges, the verse block, the margins and the stamp box inspected; no
   reversed, tiny or hidden text visible. The stamp is still on the card, so nothing under it can be checked from
   the scans - the solver says so honestly.
8. Sources: SOURCES.md and metadata record status Not solved and no attached transcription/solution; SOLUTION.md
   states the transcription is the solver's own and a web search found nothing. I found no sign of a borrowed solution.

## Findings

1. (minor) Unread address word. The line under "in Rh." on the address side is not read (I cannot read it securely
   either). It is a single word of plain address writing, disclosed in uncertainty 7, and does not affect the
   message; under the run rule a single un-understood word does not make the card partial. The solver could add a
   tentative reading or a crop of it to SOLUTION.md, but this is not required.
2. (minor) Postmark evidence can be stated more strongly. The bottom of the postmark ring shows "...ESS"
   (Rheinhessen), which supports the Wöllstein (Rheinhessen) identification; SOLUTION.md calls it inference only.
   Suggest citing the visible "...ESS" in the report.
3. (minor) The address opens with an abbreviation before "Heinrich" (looks like "S. H." / "Sr. H."), rendered by the
   solver simply as "Herrn". Harmless, but the report could give it as written.
4. (minor) For the register: cipher type MASC (number substitution, no stegano part found) is the right label; the
   card does not qualify for "MASC + Steganography" because no hidden message was found and the area under the
   stamp cannot be inspected. The report should say the under-stamp area remains unverified.

## What I could not verify

- Anything hidden under the stamp (stamp still attached; only scans available).
- The identity of Kätchen Hottum and Heinrich Lechtahler (surnames reported literally; not checked in records).
- The single lower address word.
