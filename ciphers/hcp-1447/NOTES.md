# Triage notes — 2026-10-26

All three rendered tabs read; fresh status Not solved. Neither skip.txt nor markers excluded this item. No watcher or reviewer was started, following the user override.

Both sides contain extensive dark handwritten custom-symbol cipher, spread in lines with changing orientation; address-side text also enters the address/stamp region. A few ordinary-English comments are visible on the address side, but were not decrypted and do not establish the key. Picture depicts a large building and street.

The cipher uses a mixed inventory of numeral-like signs, crosses, curves and rotated letters. A monoalphabetic substitution is plausible but unproved. No frozen full transcription or reliable alphabet mapping was produced during quick triage. This is source capture only, not a partial solution; no SOLUTION.md and no DONE1. Further work should rotate each region separately, inventory repeated glyphs and use an independently checked transcription before solving.

# 2026-10-30 — Claude Opus 5.5 (solver): key found, reading PARTIAL, no marker

Earlier entry above (2026-10-26, GPT solver) was source capture/triage only; no decipherment had been made.

## Cipher and key (established)
Not a symbol cipher: ordinary English longhand in which vowels and four consonants are replaced by digits; all
other letters are written in clear. Key: 1=a 2=e 3=i 4=o 5=u 6=l 7=m 8=n 9=r (vowels a-u, then l m n r in
alphabetical order). The writer is inconsistent with 7/8: `7` is used for **m** (S472 some, t372 time, 72 me) but
also for **n** in Ly7chb59g (Lynchburg), b227 (been), S17c2 (since, also with 1 for i); `8` for n in g138 (again),
648g (long), C45S38 (cousin), C18 (can). So decode 7 as m/n by context. Digit 9 vs letter g are similar in this hand.
Script: `python3 -I work/decode.py work/partial_transcription.txt`. Crops used: work/crops/ (z_*, box*, sig30, B*, C*).

## What is read (picture side, main body, rotate 90 deg CCW)
"Jr.(? 'J9.') Parker Rorer: Sep. 10/09 / Lynchburg, Va. / I thought I would write you to-day as it has been so long
since I saw you. I hope you are well & happy. Hope I'll see you again some time. Your little cousin Della(?)
Ch19 3?? R4669(?) Mo.(?) ... I hate to go." Addressee on the address side: Parker Rorer(?), ... Brook ..., Lynchburg,
Virginia. The address side also carries plaintext in brown ink by a different hand (\"Hello Mr. Parker ... Aug 12 '09
... You ought to have been with us in Washington. We wished for you.\", \"Oh! you kid!!\", \"O you dear little kid\").
Address-side top-right block begins \"If you love me like [..] I love you [..] we bo[th?] love the same ... yours
lovingly, Della\".

## Why it stops (no DONE1)
Only ~1024 px scans exist; the address side has about eight further small cipher blocks written in loops, a heart and
ovals in every orientation, many signs 4-6 px high, crossed by the address flourishes, the postmark ring and the
watermark, and one circled block has an ink smear that physically covers several signs (more than one letter, so no
single-letter restoration applies). The signature line (Ch193??, R4669) and the boxed P.S. on the picture side are
only partly legible. A complete pixel-verified reading of all ciphertext is therefore not achievable from these
images; the partial transcription is in work/partial_transcription.txt with unread parts marked. No SOLUTION.md
written (nothing to hand over as complete). Next step if pursued: obtain higher-resolution scans; then transcribe
the remaining address-side blocks one by one with the key above.
