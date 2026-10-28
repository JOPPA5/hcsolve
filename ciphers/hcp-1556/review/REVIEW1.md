ACCEPT

# Review 1 — HCP 1556 (pc_hcp_237), round DONE1

Reviewer: claude-opus-5-5, 2026-10-28.

In short: **the solution is right.** I re-read all 18 cipher rows sign by sign from `source/picture.jpg`, independently of the solver's transcription. My reading agrees with the solver's in **all 336 positions**. That covers 16 main rows and the 2-line bottom continuation, giving 338 letters with 2 CH. The family key decodes every sign. The one writer's slip on the card (literal TIK for DÍK) is kept literal and disclosed, not silently normalized. I found no cipher text the solver missed. The findings below are minor and do not change the plaintext.

## What I verified and how

1. **The documented command.** I ran the command from SOLUTION.md as written (codex runtime python):
   ```
   VERIFY: 18 rows; 336 mapped cipher positions; CH=2; unknown=0; literal letters=338; ...
   M01 vrely tik, dusin-  ...  B02 tobe zaslany. kde vezi toho asi pricina?
   ```
   The output is identical to the "Exact literal Czech" block in SOLUTION.md. The same script also passes under `python3 -I ciphers/hcp-1556/work/decode.py`. It is read-only: afterwards no file in `work/` is newer than `DONE1` (`find work -newer DONE1` is empty).
2. **Independent decoder.** `review/work/my_decode.py` contains my own sign-by-sign transcription, my own shape labels (documented in its docstring) and my own statement of the key. It imports nothing from the solver and reads `work/literal-cz.txt` only as data for a diff. Run it with `python3 -I ciphers/hcp-1556/review/work/my_decode.py`:
   ```
   rows=18 units=336 letters=338 CH=2
   key one-to-one: True | labels used: 22/22
   diff vs solver literal-cz.txt: none
   ```
   The key is one-to-one. All 22 sign classes occur, and no sign needs a second value. The key therefore covers the entire ciphertext.
3. **Reading the scans.** I rotated the picture 90° clockwise with `ffmpeg -vf transpose=1` (`review/work/cw.png`). I read every row from 4× half-row crops (`r0L/R … r6L/R.png`) and the bottom two lines from `b1L/b1R.png` in the original orientation. Disputed signs got 8×–14× detail crops (`z-*.png`, `k-*.png`, `s-*.png`, `w-*.png`) and comparison sheets (`cmp-s-vs-1.png`, `cmp-pricina.png`). I checked these points specifically:
   - **Paired-sign slips.**
     - D/T: every looped-d (T) and crossed-t (D) in all 18 rows.
     - S/C: round c (S) against angular s (C) in SRDECKU, ŘÍDÍCÍ, TISÍC, NAJÍCÍ, PŘÍČINA and the rest.
     - B/P, M/N (one-hump against two-hump) and I/Y (4 against 1).
     
     Apart from TIK, every sign is the expected one for its word. There is no silent normalization.
   - **K/Z.** On this card K has a bowl with a top-right flick and a looped tail (`k-listek.png`, `k-radky.png`, `k-kvetna.png`, `k-anunko.png`). Z is a "9" whose tail hooks left with no flick (`z-jemuz.png`, `z-zemrela.png`, `z-ko-za.png`). The solver's K/Z choices are all confirmed, including M09 TÝŽ (`z-tyz.png`), M10 ZEMŘELA, B01 ZTRATIL, JIŽ and B02 VĚZÍ (`w-ztratil.png`, `w-jiz.png`, `w-vezi.png`).
   - **M01 TIK.** The first sign of the second word is the looped d (= T), clearly distinct from the crossed t (= D) that opens DUŠIN- in the same row (`r0R.png`). The literal TIK is correct, and DÍK is the writer's intended word.
   - **M14 CH.** Both capped-r signs in VŘELÝCH and VÁŠNIVÝCH are visible (`r5L.png`, `r5R.png`).
   - **B01 ZTRATIL.** The final 8 crosses the printed green stem, but both lobes are visible (`b1L.png`).
4. **Search for missed cipher text.** On the picture side I found:
   - the 16-row block;
   - the 2-line continuation along the bottom edge;
   - the plain date `26./IV.1903.`;
   - flowers, the border and the collection watermark.

   On the address side I found only plain script ("Velectěná Slečna / slečna Anna Tichá / učitelka v / Žirovnici / u Počátek"), printed postcard headings, the printer line with "563", the stamp and two postmarks. There is no cipher region the solver missed and no missed sign inside a word.
5. **Context.**
   - 26 April 1903 was a **Sunday**, which suits a private letter.
   - "Sejdeme se … během května?" (shall we meet during May?) fits a late-April date.
   - The recipient, a teacher in Žirovnice near Počátky, matches the address side and the portal.
   - The sender's pet name Pepouš and the addressee's Anunka/Anuška match the rest of the Anna Tichá family.
   - The plaintext is natural Czech of the period: "Je p. řídící Šedivý týž, jemuž nedávno zemřela paní?" and the complaint about lost cards in the bottom lines. It is not words forced onto noise.
6. **Prior solutions.**
   - The portal page shows no attached solution or transcription (per `source/metadata.md`).
   - The AI register JSON (`curl https://ai.hcportal.eu/register/?format=json`, fetched 2026-10-28) has no entry for `cryptograms/1556` or `pc_hcp_237`.
   - Cipher-Atelier `anna-ticha/readings.md` (fetched 2026-10-28) does not mention card 237.
   - The generic family key (Egorov / Cipher-Atelier) and the transfer of the key from `ciphers/hcp-1520` are disclosed in SOURCES.md and SOLUTION.md.

   **No prior published solution of this card exists**, and nothing was used without credit.

## Findings

1. **minor: B02 PŘÍČINA, 4th sign, is an unusual form and is not flagged.** See `review/work/w-pricina14.png` and `cmp-pricina.png`. The sign has a hook at the top-left and a long stroke that curls left at the bottom. It is taller and more open than the closed, pointed angular s (= C) used in ŘÍDÍCÍ, NAJÍCÍ and TISÍC. It also has no horizontal foot, so it is not the digit-1 Y sign (see ZASLANÝ, `cmp-1-zaslany.png`). I agree that s/C is the best reading, and PŘÍČINA is certain from context. SOLUTION.md lists other glyph cautions but not this one, so add it to the uncertainties for completeness.
2. **minor: the reproduction command is not portable.** SOLUTION.md gives an absolute path into `/Users/tomaspavuk/.cache/codex-runtimes/...`. The script needs only the standard library and passes under `python3 -I ciphers/hcp-1556/work/decode.py`. Give that as the single command, as in HCP 1558.
3. **minor (editorial): ŠEDIVÝ may be an adjective, not a surname.** "Je p. řídící šedivý týž, jemuž…" can also mean "is the grey-haired headmaster the same one whose wife recently died". SOLUTION.md already calls the capital a "possible surname", which is adequate. The PDF should state both readings.
4. **minor (documentation): stale wording.** SOLUTION.md says "no reviewer acceptance … The human override forbids watchers and reviewers" and "No independent human or separate-provider review has occurred". Update this when you respond to this review, so that the PDF does not repeat it.

## What I could not verify

- **Postmark dates.**
  - The Prague departure postmark is largely covered by the stamp. I can see only "6" and "03".
  - The Žirovnice arrival postmark is upside down. Rotated, it shows "27", then a mark, then a roman month whose visible part is **V**, then "03" (`review/work/pm-zir-rot.png`). I cannot see whether an "I" precedes the V. If the month is V, the card arrived on 27 May, a month after the written date. That would be odd but not impossible, given the card's own complaint about lost cards.

  The solver rightly made no claim here. I treat the postmark as unreadable, not as evidence against the solution.
- **Accents and civil identities.** The exact accents (editorial) and the civil identities behind "Pepouš" and "p. řídící Šedivý" cannot be checked from the card.
