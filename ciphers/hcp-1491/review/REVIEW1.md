ACCEPT

# Review 1 — HCP 1491 / pc_hcp_172 (round DONE1)

Reviewer: claude-opus-5-5, 2026-10-26. Short version: **the reading is correct.** The message is ordinary English cursive written mirror-wise and turned 90° on the card; one fixed geometric transform makes it legible, and my own sign-by-sign reading of the transformed scan agrees with `SOLUTION.md` word for word. The findings below are corrections of the record (addressee name, metadata) and do not change the plaintext.

## What I verified and how

1. **The documented command.** `python3 -I ciphers/hcp-1491/work/decode.py ciphers/hcp-1491/review/work/solver-decoded.png` runs, the source hashes pass, and the output image is byte-identical to `work/decoded.png` (`cmp` silent). The printed text equals the code block in `SOLUTION.md` (`diff` empty), 234 letters. As the solver says, the script produces the image transform and then prints a hand reading; it does not decode text itself. For mirror writing this is the appropriate kind of reproduction.
2. **Independent transform.** `review/work/transform.sh` (my own, sips only; PIL is not installed): crop the message area of `source/address-large.jpg`, rotate 270° clockwise, mirror horizontally, upscale ≈4×. Output `review/work/msg_rm_big.png`, plus `sig_big.png` for the last two lines. The text becomes normal left-to-right cursive in both crops; the printed publisher line `Meissner & Buch, Leipzig …` and "Printed in Germany" come out mirrored, confirming that only the handwriting was reversed.
3. **Independent reading of the scan**, line by line, from my crops (not from `work/plaintext.txt`):

   | Card line | My reading | vs. solver |
   |---|---|---|
   | 1 | I got back quite safely and | same |
   | 2 | delivered your little parcel and | same |
   | 3 | messages. I did not meet Lawrence | same |
   | 4 | or see him at the station but I | same |
   | 5 | met an old "B" and he kept me talking | same |
   | 6 | til I had to run for my train in | same (see finding 3) |
   | 7 | the end. I hope you will keep "well | same |
   | 8 | and warm" as you said in your | same |
   | 9 | message. Au revoir | same |
   | 10 | Ever your own Browning | same (no full stop visible after `Browning`) |

   Line breaks also agree. Coverage: the whole handwritten message area is accounted for; nothing written on the picture side (`source/picture-large.jpg`, painted landscape, no handwriting).
4. **Language and context.** Natural Edwardian English ("I got back quite safely", "kept me talking", "Au revoir", "Ever your own …"). The postmark is VICTORIA DOCKS (London E.), `3.15 PM / ·A 18 / 09` (crop `review/work/pm2_big.png`; the J of JA is lost on the stamp), matching the portal date 1909-01-18; a trip home by train after a visit fits a sender leaving London. Addressee: a student at the Home & Colonial (Training) College, Wood Green, N. — consistent with the parcel/messages content.
5. **Prior solutions.** `work/register-snapshot.json` has no entry for URL 1491 or `pc_hcp_172` (grep); 1491 is not in `skip.txt`. I found no sign that a published solution was used.

## Findings

1. **minor — addressee surname is `Mantz`, not `Mandy`.** Crop `review/work/addr_big.png`: "Miss Frances Mant**z**" — a `t` with crossbar followed by a long-tailed `z`; there is no `d` or `y`. `source/metadata.md` records the portal's "recipient Frances Mandy" (fine, that is what the portal says) but then also describes the *image* as "Miss Frances Mandy", which is a misreading. The report should give the card's reading and note the portal's discrepancy.
2. **minor — cipher type.** The portal tag is "Transposition"; what is on the card is mirror writing rotated 90°. `SOLUTION.md` describes it correctly; the report and any register entry should use `Mirror writing` and mention that the portal tag differs.
3. **minor — `til`.** Detail `review/work/till3_big.png` vs. `will_big.png`: in `will` the writer makes two separate looped ascenders; in this word there is `t`, a dotted `i`, and **one** looped ascender with an exit stroke. I agree with `til`. Since it is the only spelling oddity in an otherwise standard text, keep it listed as a reading judgement (a second `l` could be lost in a cramped loop at this resolution).
4. **minor — reproduction script default output path.** `decode.py` writes to `/tmp/hcp-1491-decoded.png` by default; harmless, but the report should point to `work/decoded.png` as the evidence image.

## What I could not verify

- Identity of "Browning" (surname, nickname or pet name), of "Lawrence" and of the quoted "B". The solver makes no identity claim, correctly.
- The postmark month: only `·A` is legible (JA fits; AP/MA cannot be fully excluded). Day 18 and year 09 are clear enough and match the portal date.
- Whether a decipherment has been published elsewhere; I relied on the register snapshot and did not repeat a web search.
