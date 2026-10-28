ACCEPT

# Review 1 — HCP 1533 / pc_hcp_214 (round DONE1)

Reviewer: claude-opus-5-5, 2026-10-28. Short version: **the reading is correct.** I read all 19 rows from the upright scan independently, sign by sign. My 236-sign transcription is identical to the solver's. The two source spellings the solver kept, ANUNKO and VZDIT, are really on the card. I found no cipher text that was missed. The findings below are minor.

## What I verified and how

1. **The documented command.** `python3 -I ciphers/hcp-1533/work/decode.py` exits 0. It prints the 19 literal rows exactly as given in `SOLUTION.md`, and then reports `3 immutable source hashes; 3 record hashes; 19 indexed rows; 236 active cipher units, including 4 CH units -> 240 base letters`. The script does not write any files.
2. **Independent decoder.** `review/work/decode_review.py` is my own decoder and does not import solver code. `key_review.json` is equal to `work/key.json`. I decoded my own transcription, `review/work/reading_review.txt`, and got `reading_review_decoded.txt`: 236 units, 0 unknown signs. Its output is byte-identical (`diff` empty) to rows 1–19 of the solver's output. The key is a 22-shape bijection, and every sign is covered.
3. **Independent reading of the scan.** I made the upright frame with `ffmpeg -vf transpose=1` (`upright_review.png`, 674×1024). From it I cut overlapping 5× strips of block A (`a_1…a_6.png`) and block B (`b_1…b_5.png`), plus 8–10× details of ZARMUTKU, JENZ, SRDECKEM, BUD, ANUNKO, VZDIT and MYSLEN (`z_*.png`). The reading is A01–A11, then B01–B08, as the arrow after A11 indicates.
   - ANUNKO `6m2mg3` (`z_anunko.png`): the 3rd sign is the curved `2` (U), the same form as in BUD. It is not `4` (I). Confirmed.
   - VZDIT `fqt4d` (`z_vzdit.png`): the 4th sign is the crossed `4` (I), not the `1` (Y) of SVYM. Confirmed. This is a genuine writer's I/Y slip, and the solver correctly keeps it in the literal text.
   - SRDECKEM `cht5sg5n`: the sign after K is the `5` (E). Confirmed.
   - MYSLEN- `n1c85m` (`z_myslen.png`): the first sign is an M-shaped `n` that has been inked over. It is one sign, with no recoverable cancelled letter. I agree with the solver.
   - All four CH glyphs (CHOROBU, VRELYCH, UPRIMNYCH, KACH) are present.
   - **No missed text.** The top of the picture side (`z_top.png`), the image area and the address side (`source/address.jpg`) carry no other cipher signs. The only non-cipher marks are the date `28./X.1903` (`b_5.png`) and the continuation arrow.
4. **Language and context.** The text is natural Czech of 1903: a message of condolence and comfort ("vřelou soustrast … v zármutku, jenž na tebe dolehl … pan bratr je mlád a zajisté chorobu vítězně přemůže"), followed by a question ("Kdy přijede slečna do Žirovnice?") and a closing from PEPOUSE, the same signature as on HCP 1532 and 1535. 28 October 1903 was a **Wednesday**. The address reads "Velectěná Slečna / slečna Anna Tichá / učitelka v Žirovnici / u Počátek". The postmarks are PRAHA (stamp) and ŽIROVNICE ✱ SEROWITZ (arrival, day partly legible as `2…`). All of this agrees with the metadata.
5. **Disclosure.** The solver discloses the transferred family key and the published Egorov / Cipher-Atelier partial key. It keeps the source spellings ANUNKO and VZDIT and documents them, and it presents the editorial *vždiť* as its own editorial choice. It also says the solver's "root" checks were collaboration and not independent review. I found nothing undisclosed.

## Findings

1. **minor — "Accents … are editorial" vs. visible diacritics.** The writer puts caron-like marks on several signs, for example over `ř` and some vowels. `SOLUTION.md` says it ignores them for the base text, and that is fine. It could still say in one sentence whether any visible mark was used as a guide for the editorial accents (for example *zármutku*, *mlád*). This is a matter of documentation only.
2. **minor — the vocative ANUNKO and HCP 1535.** HCP 1535 (same writer, 13 Oct 1903) has the nominative ANUNKA, and that supports reading ANUNKO as the writer's real pet form of the name rather than a slip. It would help to say this in the report. It is better evidence than "unusual nickname retained".
3. **minor — stale status text.** In `SOLUTION.md`, the closing paragraphs ("There is no independent reviewer…", "root must inspect …") should be updated for FINAL, and the update should summarise this review.

## What I could not verify

- The exact accents and punctuation intended by the writer. The base letters are certain, but the diacritic marks are small at 1024 px.
- The arrival postmark's full date, and anything about the brother's illness or the "slečna" who is to arrive. These are not part of the cipher claim.
- Whether pc_hcp_214 has been deciphered somewhere outside the sources the solver checked.
