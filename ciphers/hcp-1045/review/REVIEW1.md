ACCEPT

# Review 1 – hcp-1045 (reviewer: Claude Opus 5.5, 2026-11-03)

## What I verified and how

1. **Solver command.** `python3 -I ciphers/hcp-1045/work/decode.py` from the repo root: all three SHA-256 checks print OK. The output
   (WO BIST DU HEUT? / LIEBER FRITZ! EBEN DEIENE KARTE ERHALTEN. ÜBER WAS IST DENN DASZ FÜR EIN FORTWÄRENDES GEZANKE? IST DAS DIE
   FREUDE AUF MEINE GESUNDHEIT? MIT GRUSZ SUSI) is the same as the plaintext claimed in SOLUTION.md, letter for letter.
2. **Independent decryption.** I wrote `review/work/my_decode.py` with my own table (A=2 … Z=26, no J) and my own transcription,
   read word by word from my own crops of the hi-res address scan (`review/work/block_full.png`, the block turned 90° clockwise,
   `r1_4.png`, `r5_8.png`, `r9_12.png`; the corner note turned −38° and contrast-stretched in `corner_rm38.png`). The output is
   identical to the solver's. Every number on the card (2 3 5 6 7 8 9 10 11 12 13 14 15 18 19 20 21 23 26) decodes under the one
   table; there are no leftover signs.
3. **Transcription against the pixels.** I read all 11 block lines and the 3-line corner note. All numbers in work/transcription.txt
   match what I see. Specific checks at 3x (`review/work/`):
   - `dasz.png`: "5.2 19.26": the 2 and 1 stand very close with no dot. The 2|19 split rests on word sense, as disclosed.
   - `mit.png`: the first numeral of MIT is a long down-stroke with a looped lead-in at the foot, and no upper bow like the 2 of the
     "20" beside it. I read it as a German 1 with its entry stroke, which gives 13 = M. It is disclosed as partly word sense; I consider
     13 the better reading of the pixels too.
   - `corner_rm38.png`: "23.15.–" / "3.10.19.20.–" / "5.21.– 9.6.21.2(0)." followed by a large, dark "2"-shaped mark with a heavy dot.
     The 0 of the final 20 is faint, as disclosed. The big mark is clearly this writer's question mark.
   - `gezanke_q.png`, `gesund_q.png`: the dark marks after GEZANKE and GESUNDHEIT have the same shape as the corner-note `?` (a 2-like
     hook over a dot or dash) and are drawn in the same darker pencil. Reading them as `?` is justified.
   - Umlaut ticks over the 21 of FÜR and over the 2 of FORTWÄR are clearly visible. The bar over 14 in DENN is clear.
4. **Picture side and stamp.** The picture side carries only the printed Faust/Gretchen caption and the publisher number; there is no
   handwriting. The stamp (`review/work/stamp.png`) is affixed and shows no pencil traces at its edges. Nothing under it can be
   checked on these scans, and the solver says so. I found no other hidden writing along the edges.
5. **Language and context.** The text is natural colloquial German of the period ("Über was ist denn das für ein fortwährendes
   Gezanke?"). The writer's slips DEIENE, DASZ for "das" and FORTWÄRENDES without H are kept and disclosed. Name, signature and tone
   fit the sister cards hcp-1113 and 1134 (same recipient, signature "Susi", same table). The key is a trivial shifted-number alphabet.
   I found no published solution, and the solver's claim of one web search with no hit is plausible.

## Findings

1. **(minor) The ÜBER umlaut is misdescribed.** SOLUTION.md (uncertainty 5) says the ticks stand "just over the 21 that begins line 3".
   In the transcription, though, that 21 is at the end of line 3 ("… 6.14. – 21"x.3.6.18."), not at its start. In `review/work/uber2.png`
   the two ticks sit between lines 2 and 3 at the far right, above the final "18." of ÜBER on the printed "Briefkart". They are not
   over the 21, which stands about 25 mm to the left. So the Ü of ÜBER is not actually marked over its number, and it rests on word
   sense (UBER would be the literal reading). The ticks could also be a ditto or end mark. Please correct the description; the meaning
   is unchanged.
2. **(minor) A second missing separator is not disclosed.** In GESUNDHEIT the scan shows "9.610.20" (`review/work/gesund_q.png`), with
   no dot between 6 and 10. The transcription silently writes 9.6.10.20. The split is unambiguous (61 is outside the table), but
   "Why I believe it is correct" claims only one missing separator dot. Mention this one as well.
3. **(minor) The translation of "Freude auf meine Gesundheit" is uncertain.** "auf meine Gesundheit" is the formula of a toast ("to my
   health"). The sentence may therefore be ironic ("is that the celebration / toast to my health?") rather than "joy at my (regained)
   health". The English and Slovak translations should note the alternative, or give a neutral "joy over my health".
4. **(minor) Address street name.** "Alte …straße" is left unread. It is a single word in the plain address and not part of the
   message, so the card still counts as complete. A best reading (it looks like "Alte Lan…schaftstraße") or an explicit "[street
   name unread]" in the report would make this clearer.
5. **(minor) Sister-card status.** SOLUTION.md says the key is "already proven" on hcp-1113 and 1134. Both are only at REVIEWED1, not
   FINAL. The key stands on this card alone (about 90 numbers, fluent text), so this changes nothing, but the wording should not claim
   more than that.

None of these affects the reading. Register type label: MASC (the steganography check is negative on the visible scans).

## What I could not verify

- The underside of the affixed stamp.
- The exact postmark day (only "…10.09" is legible under the stamp); I took the 12.10.1909 date from the portal metadata.
- Identity of "Susi" and the exact street of the address.
