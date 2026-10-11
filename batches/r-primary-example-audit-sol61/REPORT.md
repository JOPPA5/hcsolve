# Independent primary R/XQ worked-example audit

The ordinary three-stage encoder is supported by the actual published worked example, not just invented round trips. Independent visual transcription of Figure 5 and a new row-write / ascending-column-label implementation reproduce both complete 55-letter intermediate grids at widths 21, 19 and 20. The existing `analysis-395-396/joint_r.cpp` encoder/inverse and `shared-r-sol61/joint.cpp` inverse pass the same fixture, including aligned and canonically rotated representations. No transposition-direction or ragged-column-length defect was found in these implementations.

The full 60-letter assembled cryptogram is **not** unambiguously verified. Handwriting in the final grouped output and the separate indicator note remains ambiguous, and the older tentative assembly helper uses a potentially different insertion convention.

## Evidence and independence

Primary source: Eugen Antal, Pavol Zajac and Otokar Grošek, *Diplomatic Ciphers Used by Slovak Attaché During the WW2*, HistoCrypt 2020. Original local PDF `batches/analysis-395-396/context-paper.pdf`; SHA in independent-transcription.json. Relevant printed pages 22, 23 and 28 (PDF pages 2,3,8). Figure 5 reproduces an archival example from SNA, MZV box 507. Figures 1 and 2 are separate manual material from box 580.

I first rendered the original PDF, read all three handwritten label arrays and grids, and saved independent-transcription.json before opening the existing verification scripts. Initial handwriting readings produced five discrepancies. Close source crops resolved stage-II X/K and P/T and stage-III small-I/L glyphs; the first-pass readings remain preserved. The collated transcription then matched both intermediate grids in the independent encoder. Only afterwards were the existing algorithms read and tested. The source-led transcription sequence is visible in the separate first-pass and collated JSON/scripts, so this is not an unexplained assertion that program output equals program output.

Prepared plaintext, exactly as represented by the first printed grid:

```
STAHOVANIEVYSLANECTVANUTNEXPOSLITESEMIHNEDSLUZOBNYVOZXX
```

Figure 5 physical column labels, already aligned to 7:

```
I   7 10 21 3 18 6 20 1 19 15 9 13 5 16 2 17 4 12 8 11 14
II  7 15 8 6 18 3 10 9 17 14 2 13 1 19 11 5 12 4 16
III 7 20 3 12 6 19 8 16 2 17 1 18 11 5 9 4 10 15 14 13
```

The first output, laid out under the 19-column second key, is exactly:

```
NOYAEHNZEISEXVXBSNS
TNVIZTULVECHYTXADEL
OLSNMOEOISVAPNATU
```

The second output, laid out under the 20-column third key, is exactly:

```
XYPSCVHTONEBATAINNTO
YVSZLONUEXXASDUEHAIE
SONLSLEVIEZMVTN
```

Computed third-stage payload:

```
EXZOE IPSNI ETDTC LSXYS HNEAU NNHAS VSZLO ETINA TUVNX EBAMV OLYVO
```

This is compatible with the handwritten final groups except for the second group's final I/L-looking glyph. The independent literal first reading was IPSNL; the third-grid small-I cell gives IPSNI. It would overstate the evidence to call an unambiguous literal 55/55 final handwritten match. The historical-context verification already accurately limits its claim to the intermediate grids and inverse, with final grouping/indicator not independently verified.

## Alignment is physical, not a rotated read order

Printed page 22 says the permutation numbers retain their order while being rearranged to start at 7. Figure 1 has different daily example keys (widths 21,18,24), so it must not be silently substituted for Figure 5's keys. Independently reading Figure 1's unaligned and aligned arrays verifies all three rotations exactly. The existing encoders rotate the *physical label array* before row filling and read columns by ascending label, consistent with that primary evidence. Canonicalizing a cyclic key to start at 1 then rotating to 7 also gives the same physical layout.

The progressive n,n+1,n+2 convention is stated as another option in the article, but this particular Figure 5 uses 7,7,7. This audit does not claim a worked example of the progressive option.

## Indicator, placement and the `360` note

The article explicitly gives n=7 and ip=5. Its rule expands 7 to decimal 78901, then chooses letters from a daily re-encryption table. Figure 5 visibly writes a separate handwritten five-letter annotation, which is not confidently transcribed here. It does not present one clean 60-letter line with that group already inserted. The V-shaped arrow appears between HNEAU (payload group 5) and NNHAS (6), suggesting insertion **after five payload groups**. The article phrase “insert N to position ip” does not itself disambiguate before/after indexing.

The older `analysis-395-396/check_paper_example.py`, explicitly marked TENTATIVE, uses `groups.insert(4,'JGEMU')`, i.e. before payload group 5. That assembled line is not a primary-certified known-answer vector. I preserve both after-four and after-five layouts with an unresolved-indicator placeholder in alignment-and-assembly.json. No new indicator is guessed or assembled. This does not imply that prior all-position omission searches excluded the correct position.

The old helper's tentative JGEMU maps to 78401 under Figure 2's separate 1939 manual table, not the article's required 78901. This is an additional reason not to certify that helper's guessed indicator. The table is not established as Figure 5's daily table, so the mismatch cannot justify changing the handwritten note or inferring another indicator. No same-daily-table transfer was assumed.

The literal note `360` is visible at the bottom. There are 55 prepared payload letters and a five-letter indicator, consistent with a total of 60. The article's reproduced figure does not explain the initial 3 or prove a general header-parsing rule. Its semantics remain unavailable, rather than inferred from unrelated target headers.

## Scope and reproducibility

From the repository root:

```
batches/r-primary-example-audit-sol61/reproduce.sh
```

The primary images and first-pass/collated data are retained. The C++ harnesses include the original existing implementations read-only and call their encoder/inverse functions on this actual fixture; they do not rerun searches or modify their source files. Their saved outputs confirm all three stage checks. The renamed unused original main in joint_r.cpp causes a compiler return-type warning; the tested stage/cascade functions pass.

Result: actual primary validation for the transposition core and physical alignment; incomplete primary validation for final indicator spelling/insertion/header semantics. No target cipher, source, marker or register was modified.

## Impact of the insertion boundary on previous target tests

A targeted repository-wide code search finds only two relevant `insert(4, ...)` uses. The first is the tentative Figure-5 assembly helper. The second is a deliberately planted HCP-395 two-segment control in `work/segment_constraints.py`, which inserts synthetic indicators before payload group 5 and removes exactly those five bytes (`block[:20]+block[25:]`). That control is internally consistent, but it does not validate the historical meaning of ip=5.

The inspected actual searches do not inherit a fixed index4/5 from Figure 5. HCP-395 route and split searches enumerate every group omission; HCP-393 routes and HCP-364 known-quote tests do likewise. HCP-399 indicator/sweep scripts enumerate compatible physical groups. Joint 395/396 constraints enumerate observed one-based group positions, and the uncalibrated shared-R batch retains compatible positions 5 and 6 rather than applying an ip conversion. Its target search was not run. Earlier restricted 395/396 group8 tests derive from the separate conditional header-as-alignment 9/7 hypothesis, not from Figure 5's ip.

Therefore I found no actual target result that needs rerunning solely because the tentative worked-example helper inserted at index4. The helper's final assembled “known answer” must remain uncertified; its synthetic-control analogue must not be promoted to primary procedural evidence. Exact paths, lines, distinctions and search limits are in placement-impact.json. This is a targeted source audit, not a blanket coverage guarantee over every historical attack log.
