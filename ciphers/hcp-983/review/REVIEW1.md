ACCEPT

# Review 1 of hcp-983 (Claude Opus 5.5, reviewer, 2026-11-03)

## What I verified and how

1. **Command from SOLUTION.md.** `python3 -I ciphers/hcp-983/work/decode.py` (run from repo root): all four SHA-256 hashes OK; output `I/JOH HERBST` / `SCHREI/JBE BALD`, identical to the claim.
2. **Independent transcription.** I rotated the hi-res address side (`work/hires/cpc_--___DE_Endsee__adr.jpg`, 3469x2298) myself and read every number at 2x enlargement (crops `review/work/line_start.png`, `line_mid.png`, `line_end.png`, `rot_overview.png`). My reading, sign by sign:
   - line 1: `9.14.8.  8.5.17.2.18.19.`
   - line 2: `18.3.8.17.5.9.2.5.  2.1.11.4.`
   This matches `work/transcription.txt` exactly (21 numbers). The hooked 7 in both 17s is clearly distinct from the crossed 4 in 14 and in the final 4; the "v"-shaped 2 in `2.1.11.4` has the same form as the 2 in `17.2` and `9.2.5`. The first `18` of line 2 sits at the card edge but is complete.
3. **Independent decode.** `review/work/indep_decode.py` tests plain A1Z26 and a 25-letter alphabet with I=J merged. A1Z26 gives `INH HEQBRS / RCHQEIBE BAKD` (nonsense); the I/J-merged alphabet gives `IOH HERBST / SCHREIBE BALD`. Every one of the 21 numbers decodes; values used are 1–19 only, so the key is fully determined by the I/J merge and nothing beyond T is attested. No number is left over and none is forced.
4. **Plain part.** Read on `review/work/verse12.png` and `gruss.png`: "Zum Zeichen daß ich dein geden-/ke / Ich dir dieses Kärtchen sende, / Grŭß und Kŭß sendet Dir". Gruß/Kuß are written with a u-bow over a closed letter; reading as Gruß/Kuß is by word sense and is disclosed. The whole verse reads; there is no unread clause.
5. **Stamp box / steganography check.** (Also prompted by the general instruction to inspect stamp boxes for hidden messages.) Crop `review/work/stamp.png`: no stamp was ever affixed (field post), the box holds the printed red triangle, the "K.B. ..." postmark ring and a few greenish specks that do not form letters. The picture side (`review/work/pic_small.png` and the hi-res file) shows only the printed "Beste Ostergrüsse" and publisher mark R 5204/3; I found no handwriting in the picture or along the edges. No steganographic part, so `MASC` (not `MASC + Steganography`) is the right type.
6. **Context.** Soldier's WWI Bavarian Feldpost Easter card; a ciphered signature and "write soon" on a card to a girl is typical. Endsee (Middle Franconia) fits "Post Steinach a/E" (see finding 2). No published solution exists (portal: Not solved, no attachments); the solver claims none.
7. **Pencil annotation.** The block capitals above the numbers (JOH HERBST / SCHTEJBEBTLD) are visible in a different medium and hand; line 2's pencil is wrong in places (T for 17 where R is meant, T for 1 where A is meant). Correctly treated as a later reader's attempt and not used.

## Findings

1. **minor** – Script misnamed. SOLUTION.md calls the message and address "German Kurrent". The pixels show Latin cursive (lateinische Schreibschrift): Latin-form e, h, r, n, d, the "Z" with descender is the Latin-cursive Z; only the long ſ in "daß/Gruß/Kuß" and the u-bow are German habits. Please correct the description (and in the report).
2. **minor** – "Post Steinach a/E(?)": the "a/E" is most likely "an der Ens" (Steinach an der Ens, the postal place for Endsee near Rothenburg o.d.T.). The word is written "Steinach" with an overwritten letter. Can be stated as the likely reading rather than left bare.
3. **minor** – `decode.py` uses `ALPH = 'ABCDEFGHIKLMNOPQRSTUWXYZ'` (drops V). Only values 1–19 occur, so this has no effect on the output, but the 20+ part of the key is not attested; SOLUTION.md already says so. Either drop the unattested tail or keep it clearly marked as assumption.
4. **minor** – Surname: the pixels show "Bot" + overwritten letter(s) + "ch" ("Botsch" or "Botach"); portal says "Botch". Disclosed as uncertain; fine, not part of the cipher.
5. **minor** – "J" in JOH and "I" in SCHREIBE rest on word sense (merged sign 9); disclosed. "Joh." = Johann(es) is an expansion, disclosed.

## What I could not verify

- The field-post unit and date in the "K.B. ..." postmark ring (only "K.B." and a fragment of the ring legend are legible), so the exact year (1914–18) is not established.
- Identity of Joh. Herbst and Lina Botsch/Botach.
- Whether anything was ever written under a removed stamp: there is no evidence a stamp was ever affixed (field post, red triangle printed in the box).

## Register

Type `MASC` (number substitution with I/J-merged alphabet) is appropriate; no steganographic component found. The solution is complete (both enciphered words and the full plain verse read).
