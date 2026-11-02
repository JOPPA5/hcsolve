REVISE

# Review 1 of hcp-1157 (Claude Opus 5.5, independent reviewer session)

The cipher reading and the open letter stand. One concrete fix is needed: the last enciphered word should be `ángyikám`, not `angyikám`, with the matching key sign, translations and uncertainty note. Everything else is minor.

## What I verified and how

- Ran `python3 -I ciphers/hcp-1157/work/decode.py`: hashes OK for all 4 files, 24 signs decoded, output equals SOLUTION.md.
- Own decoder from my own sign reading: `review/work/indep.py`. Same text with the solver's transcription; `és ángyikám` with the reading in finding 1.
- Key coverage: 24 signs, 15 distinct, counts correct. 14 values are on the hcp-1174 table; `4.` is not.
- Pixels: every cipher sign at 3x from work/hires (`review/work/l1a, l1b, l2a, l2b, z_ang`, end marks `z_end1, z_end2`). Every open row at 2x (`r1` to `r9`). Weak words at 3x (`z_hany, z_mar, z_mar2, z_ki, z_oln`). Postmark `pm.png`. Picture side `ov_pic.jpg`: no writing.
- Dot heights measured on the hires scan (ink threshold, pixel rows). See finding 1.
- Weekdays computed: 3 Dec 1915 Friday, 12 Sunday, 13 Monday. As stated.
- Sister cards read: hcp-1174, 1178, 1179, 1165, 1144, grep across the family SOLUTION.md files.

Open text: I read it through independently and agree with it word for word, apart from word division (finding 3). Specifically confirmed: `kvártélyon`, `egyik inas sem`, `hált` (printed mark overlaps), `rendez-gettem`, `kályhába`, `lyukas`, `felébredtem`, `hányinger` (h stem and bowl visible beside the printed 2963), `fogot`, `elő` (crossing the printed mark), `már` and `nagy` (both legible through the FOTOTAGLIO box, `z_mar2.png`), `ki` (blotted, but the i dot and the k stem show), `szén gáz` with both accents, `ölni` under `meg-`, closing parenthesis, `Sz. A.`, `mindnyájatokat csókollak`, address. The narrative is coherent period Hungarian. No forced reading. The carbon monoxide story has no match on sister cards that I found, so it is not contradicted or supported from there.

No published solution is attached and none used; SOLUTION.md says the HistoCrypt article was not checked for this card, which is honest.

## Findings

1. **major: line 2 reads `ángyikám`; the first sign is `1'`, not `1.`.** Measured dot positions (pixel rows; the stems of both line 2 signs run to about 245, tops about 174 to 186):

   | sign | dot rows |
   |---|---|
   | line 1 `1.` (Margitkám a) | 120 to 137, near the foot of the stem |
   | line 1 `1'` (kám á) | 77 to 98, at the top of the stem |
   | line 2 first sign (claimed a) | 184 to 203 |
   | line 2 last sign (á, certain) | 187 to 205 |

   The two line 2 dots stand at the same height, within 3 pixels, so the writer made the same sign twice, and the second is á by the agreed reading. The solver saw that the dots match but took the a-reading on word sense. The word sense goes the other way: `kedves ángyikával` stands on hcp-1144 in the correspondence as `ángyika` (sister-in-law or aunt by marriage), glossed there; hcp-1165 renders `angyikát` as ángyika; the hcp-1178 note records that hcp-1175 opens `Kedves Ángyika!`. Together with `mindnyájatokat`, the salutation is to Margitka and to her ángyika, a second woman in the house. SOLUTION.md says the change would be "only the accent", but it decides the word: drop the "little angel" option as main reading, translate as sister-in-law or aunt, and fix the sign table, decode.py transcription, English and Slovak. hcp-1144 is not cited at all in SOLUTION.md. Line 2 `1.` then does not occur. State that the identity of the ángyika on this card is not given, and that the relation is not exact. Residual doubt stays: the dot is lower than the line 1 á, so report it as a reading from the match plus context.

2. **minor: `4.` = gy has independent support the solver missed.** SOLUTION.md says the value "rests on this one occurrence" and is new here. hcp-1165 (key table) has `4.` = gy from `5 0 4.` hogy and `6 1. 4. 0 6,` nagyon. That card is itself still under revision, so cite it as such; but "only new value" should read "not on hcp-1174, also on hcp-1165".

3. **minor: "spelling as written" is not kept.** The card has `egyóra`, `demajd`, `inassem`, `meg raktam` (spaced), `szén gáz`; the text prints `egy óra`, `de majd`, `inas sem`, `megraktam`, while keeping `aligbírtam` and `felvoltam` joined. Either keep all or say that word division is normalized. No effect on sense. `Én` has no visible accent on the card.

4. **minor: the `!` at both line ends is a single slanted stroke, with no dot** (`z_end1.png`, `z_end2.png`). The line 1 stroke has a small hook at the top. It is not a `1` (no flag, and `margitkámi` is nothing), so punctuation is right, but the transcription should say stroke rather than print `!` as seen.

5. **minor: looped `7` in Margitkám is counted as table-decoded.** The script says "all decoded by the table" and the "why correct" section says 23 on fixed values. This sign has a loop unlike the other 7s; it is disclosed under Uncertainties, and I accept k, but the count should note the one variant form.

Disclosed and agreed: `)` unexplained; postmark day (a mark before the 3 at `pm.png`, 3 is the better reading but I cannot exclude 13; the stamp print interferes); Friday problem unresolved.

## What I could not verify

- The HistoCrypt article was not opened.
- The postmark day beyond the above, and so which Friday is meant.
- Who the ángyika and Róza are, and that `Sz. A.` is the Árpád of hcp-1174.
- Sister card readings were taken from their SOLUTION.md files, not re-read from their pixels.
