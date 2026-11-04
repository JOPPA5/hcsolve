CONFIRMED

# Review of the stamp-box message, HCP1211 (2026-11-03)

Reviewer: Claude Opus 5.5 (independent pass). I wrote only to `review/`. I did not change the solver's files, `source/` or any markers.

## What I checked

- Original: `work/hires/cpc_1912-02-10_HU__HU_Jasz-Arokszalas_jolanka-04_adr.jpg` (3421x2176).
- My own crops are in `review/work/stamp-2026-11-03/`:
  - `full_small.jpg`: the whole address side at 1/3, used to find the box (top right, beside the GYÖN... postmark).
  - `box_rot_2x_full.jpg` and `box_wide_green_2x.jpg`: the box crop (2780-3200 x 100-800), rotated 90 degrees clockwise, in colour and as an autocontrasted green channel.
  - `line2_5x*.jpg`, `line3_5x*.jpg` and `line4_5x*.jpg`: single lines at 5x, colour and green channel.
- Box state: the stamp is lifted. Torn paper with green printing and perforation edges remains at both short ends. The box holds four lines of pink-ink plain Latin cursive in the same ink as the cipher text. The wide green-channel crop shows no cipher signs and no further writing anywhere in the box.

## My reading, sign by sign (made before comparing)

1. `c s o k o l o m   a`. All clear. The final a is a filled loop with an exit stroke.
2. `c s o k r o v   a -`. The sign after r is a closed round loop. The final a has the same form as the a in line 1, and a short hyphen follows it.
3. `l ó   k i s   s z a`. The o is heavily inked and has a separate dot/accent above it. The i of *kis* has its dot. *sza* is paler but every letter is readable.
4. `j á t   F e r i`. The j is a stroke that rises from the left and then drops into a long descender. The á has an accent dot and the t has its cross. *Feri* is a large looped F followed by e, r and i.

Normalized: *Csókolom a csókra való kis száját. Feri*. This matches the claim word for word. Nothing is left unread.

## Differences and notes (all minor; none changes the reading)

1. **Word gap in line 2.** In `line2_5x.jpg` the v sits close to the preceding o, and the clear gap comes after v, before the final a. The literal grouping is therefore closer to `csokrov a-` than to the solver's `csokro va-`. This is only spacing. It does not change *csókra va-ló*.
2. **o for a in *csókra*.** The sign really is a closed round loop. The writer's a in this box (end of lines 1 and 2) is also a closed loop with an exit stroke, so an o-like a is part of his hand. The solver discloses this reading, and I accept it as disclosed.
3. **Blot in line 3.** A dark round ink dot stands low between the s and the z of *sza* (`line3_5x.jpg`). It is a blot, not a letter. The solver does not mention it.
4. **i-dot of *Feri*.** I see no separate dot over the final i (`line4_5x.jpg`). The signature is still legible, and the same name is signed in the cipher. The solver calls it "clear", which slightly overstates it.
5. **j of *száját*.** The shape alone could be taken for a cursive z with a descender. Only j gives a word (*sza-ját*), and the solver's "read by shape plus word sense" covers this.

## Type change

The writing under the stamp is physically present (a hidden message in the stamp box), so "MASC + Steganography" is justified. `register-entry.txt` already carries `type: "MASC + Steganography"`.

## What I could not verify

- Whether anything was written on the back of the lifted stamp. The stamp is not on the card.
- The original colour fidelity of the paler *kis sza*. I read it from the hires scan only.
