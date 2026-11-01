REVISE

# Review 1 of HCP1281 (Claude Opus 5.5, reviewer, 2026-11-01)

The decipherment stands: same key, same message, same plot. The fixes below concern one error in the stamp text, four sign calls where the ledger does not match the pixels, and normalizations in rows 7, 17 and 22 that say more than the card supports. None of them changes the sense of the message, except that the hour "five" is less firm than the translations show.

## What I verified and how

- **Solver's command.** `python3 -I ciphers/hcp-1281/work/decode.py` ran. All 4 SHA-256 checks print OK, and the literal rows and normalized text match SOLUTION.md. The script only prints the ledger, so the command proves consistency, not the reading (SOLUTION.md says this).
- **Own decoder.** `review/work/my_decode.py` holds my own shape-code transcription of all 24 rows and 7 stamp rows, typed from my crops in `review/work/crops/` (made by `review/work/crop.py` from `work/hires/..._adr.jpg`, 1.6x to 4x), with the key table of `ciphers/hcp-1216/SOLUTION.md`. It is not blind, because I had read the ledger first. Result: 453 of 463 ledger tokens agree (with `gy` split into two signs). The differences are in rows 7, 8, 11, 16, 22, 23 and S7, all covered below.
- **Sign checks on pixels.** I read every row on crops, and enlarged further rows 7, 8, 10, 11, 16, 17, 22, 23, 24 and the stamp block. The ordinary rows 1 to 6, 9, 12 to 15 and 18 to 21 agree with the ledger sign for sign. Key coverage is complete: no sign needs a value outside the family key.
- **Language and context.** The text is real period Hungarian love-letter prose, with one coherent plot. *Kívánom hogy … találja soraim* is on HCP1213 and *számtalanszor, sírig hű* on HCP1216 as cited. *Bizony öt napig nem látnom magát* uses a correct personal infinitive. *1/4 10* = 9:15 is correct, in the Slovak too.
- **Postmark.** The right cancel reads `[1]914 JUN.10 N4`, Budapest, as claimed. The left cancel lies under the writing and agrees with JUN.10 but is not sharp.
- **Plain text.** Address as stated. The top line reads as *Szépreményű*, plausibly, and SOLUTION.md hedges it correctly.
- **Sources.** Nothing suggests use of a published solution. The portal shows no solution, per `source/metadata.md`.

## Findings

1. **minor (error): the stamp text is not missing -ja.** SOLUTION.md item 1 and the normalization say *csokol* "lacks -ja" and print *Csókol[ja]*. But row S2 begins with inverted T + two bars, j a, which the ledger itself gives as `j a s z a m`. The word runs across the rows: *csókol|ja szám|talan|szor*. Fix: remove the brackets and the remark. Crop: `crops/zs.png`.

2. **major: row 22 normalization *[ór]akor* is not supported, and "five" is stated too firmly.** The literal letters after the overwritten sign are t, o, k, k, o, r. *Órakor* needs o r a k o r, so the proposed form shares only the outer letters and has no r or a in the middle. *Öt … kor* (*ötkor*, "at five") or an unexplained *okkor* are closer to the pixels; *akkor* ("then") would need o for a. The overwritten sign is a loop rewritten darker, with marks above it that may be two or three, and with an extra stroke at its right tail (`crops/r22z.png`). The t after it is also rewritten, with a second arc. A corrected digit or word cannot be excluded. Item 8 discloses the doubt, but the Hungarian, English and Slovak all give "five o'clock" without a mark. Fix: mark the hour as uncertain in all three versions, and print the word as read rather than as *[ór]akor*.

3. **major: row 7, the ledger drops a visible mark, and *Sámon* is a conjecture presented as a name.** Two clear green ticks stand above the loop (`crops/z7.png`, `crops/pm1.png`), the same as the ö marks in rows 15 and 17, so the literal is *s a m ö n n e l*, or at least needs `[ö]`. They are not disclosed. Also, *Sámonnél* breaks vowel harmony: a back-vowel name takes *-nál*. No other card in the repository has this name (grep of all `SOLUTION.md`). *Sám-* with *-ön* is not explained either, and the four strokes lie across the postmark ring. Fix: correct the ledger, and in the translations write something like "at dear S[…]'s (unidentified word in -nél)". Under the run's rule this stays one un-understood word, so the card remains complete.

4. **minor: row 22 start, `fogo[n]` should probably be *fogom*.** On `crops/z22.png` the arm of the o turns down into a full stroke, followed by two free strokes. That makes three strokes, with no need to place a third under the overwritten sign as item 8 suggests. Compare other o's, whose arm stops short. Fix: ledger `f o g o m`, and adjust item 8.

5. **minor: row 17, *ep[ed]ő* is one option among others and the h/p call is not forced.** The literal is *a z e n e h ö s z i v e m n e k*. *Hő szívemnek* ("my ardent heart") needs only one stray e (for *én*-*e*), and takes the sign at its h value, while *ep[ed]ő* inserts two letters. The notes in fact began with *ho szivemnek*. Item 6 does not mention this. Fix: list *hő* as an alternative. I do not ask you to prefer it. The sense is the same.

6. **minor: row 16, ledger `[m]` hides a clean gamma.** After two strokes comes a full-size gamma, not a short stroke with a tick (`crops/zm.png`, width about 150 against 180 px for the t before it). The literal is *l a t n o n t a g a t*. *Látnom magát* remains the right reading, but as an emendation of a miswritten sign. Fix: state the literal in item 5.

7. **minor: row 23, undisclosed sense call in *maradok*.** The sign after *marado* has the descending shape of the g sign, not the k shapes of rows 1, 12, 18 and 22 (`crops/zk.png`). Sense requires k. Neither SOLUTION.md nor the ledger mentions it. Fix: add one line.

8. **minor: ledger `gy` is two signs, and the header is wrong.** The ledger header says one token = one written sign, and the key says *gy* is a joined sign. On this card each of the 8 `gy` tokens is the g sign followed by the separate y sign, the same y as in *bizony* and *meny* (rows 2, 13, 19, 20: `crops/a.png`, `crops/i.png`). Fix: split the tokens or correct the header and the sign list.

9. **minor: row 11, `[m]` is two strokes plus a dot-like tail, as easily n + comma.** See `crops/e.png`: the strokes are `||` with a short mark at the base. It is left out of the normalization in any case, so this changes only the ledger note. *Erkeztem[,]* is a possibility the item could name.

10. **minor: the timing argument leans on the doubtful hour.** "30 hours later is the afternoon of 11 June, near five o'clock" uses "five" as support, while item 8 rests "five" on the same sense. Holding the two together is fine, but it is not independent evidence. Counting back 30 hours from 17:00 on 11 June gives 11:00 on 10 June, before the `N4` cancel, so it is consistent only. Fix: one clause in *Why it is correct*.

Items 3, 4, 7, 9, 10 and 11 of SOLUTION.md (rows 8, 20–21, 23, 24 and the spellings, including *késéssel* written *k e s s e s e l*) match the pixels and are properly disclosed. S7 is correctly left unread: a cross, then bars of an e, then tear; I add nothing to it.

## Could not verify

- The hour written in row 22 (see finding 2), and the word in row 7.
- The identity of *S…* and the journey behind the late arrival.
- S5 and S6 in full detail: they lie on the stamp residue, and I accept *sirig hű feri* as fitting the visible shapes and the family formula. The ű has no double mark I can see.
- S3 has a doubled-looking wave (*t a l a n*), which reads but is not clean.
- The time of writing, and the meaning of `N` in the cancel.
