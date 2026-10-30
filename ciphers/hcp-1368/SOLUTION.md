# HCP 1368 / pc_hcp_49 — Caesar (+1) love postcard, 26 July 1907

Status: **whole message read; review 1 (REVISE) addressed.** All running words and the closing group `M. & L.t` are decoded by one key. The group's expansion "love and kisses" is an inference, and the separate group `M. h` (twice) is unresolved. See Uncertainties and the Response to review 1.

## Origin

HC Portal cryptogram 1368 (`pc_hcp_49`), portal status *Not solved*, no attached transcription or solution (`SOURCES.md`, `source/metadata.md`). No published solution of this card was found or used. Picture side: printed Valentine's view "The Choir, West, Westminster Abbey", no cipher. Address side: halfpenny Edward VII stamp, postmark ending "BORNE" (the visible part of the WIMBORNE seen on the sister cards), 10 PM, JY 26 07; addressed in clear to Mr W. Abbott, Stokelake Farm, Chudleigh, Devon (portal spells the recipient "W. Abboú"). 26 July 1907 was a Friday, matching the plain heading "G. H. Friday" and the plain date "July 26th 07". The message is on the address side, written up the card (rotate 90 degrees anticlockwise; `work/crops/reading.png`). Same couple, hand and formulae as the finished Caesar cards hcp-1378 (`dbse`), hcp-1395 (`M. & L.`) and hcp-1402 (the same salutation slot, read `N. L.` there). Same writing day as hcp-1369 (DONE1 / REVIEWED1, no FINAL yet), which reads `M-h`.

## Cipher and key

Monoalphabetic Caesar shift: each plaintext letter is written as the **next** letter of the alphabet; decrypt by subtracting one. The heading and date are ordinary writing and are not shifted. The closing group `M. & L.t` is treated as enciphered like the rest of the message and gives L. & K.S. The group `M. h` is unresolved: it is printed as written, with its shifted value L. G. shown only for information, because neither form gives a word and no card here establishes its meaning.

```
Cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

## Transcription and plaintext (all ciphertext on the card)

| Ciphertext | Literal plaintext |
|---|---|
| (plain) G. H. Friday | G. H. Friday |
| Nz. Pxo. M. h Cpz. | MY. OWN. [M. h] BOY. |
| qptu. dbset | POST. CARDS |
| up Ebz. wfsz. | TO DAY. VERY. |
| ojdf. M. & L.t | NICE. L. & K.S |
| zpvs. Pxo. M. h | YOUR. OWN. [M. h] |
| Hjsm. | GIRL. |
| (plain) July 26th 07 | July 26th 07 |

44 enciphered letters, all decoded by the one key: 41 in running words, 3 in the group `M. & L.t`. The 4 letters of the two `M. h` groups are unresolved.

English (plaintext language; portal says Unknown): *"G. H., Friday. My own M. h boy. Post cards to-day. Very nice. L. & K.s [probably "love and kisses"], your own M. h girl. July 26th 07."*

Slovak: *„G. H., piatok. Môj vlastný M. h chlapec. Pohľadnice dnes. Veľmi pekné. L. & K.s [pravdepodobne „love and kisses" = láska a bozky], tvoje vlastné M. h dievča. 26. júla 1907."*

(`M. h` is left unexpanded in the translations. The bracketed expansion is an editorial inference, not deciphered text.)

## Command (from the repo root)

```sh
python3 -I ciphers/hcp-1368/work/decode.py
```

It checks the SHA-256 of the two source images and the two hi-res originals, decodes `work/transcription.json`, checks the inverse round trip, and prints the plaintext and letter counts. The `M. h` groups print as `[M. h = L. G?]`, meaning written form and shifted value.

## Uncertainties

1. **Closing group `M. & L.t`.** The letters are firm: M with hook, stem and two further downstrokes (`review/work/z_amp_N.png`), L with head stroke, stem and foot, and an unmistakable crossed t (`work/crops/z_dot_t.png`, `review/work/z_L.png`). The upper loop over the L belongs to the f descender of `wfsz` above. That the group is enciphered, and that L. & K.S means "love and kisses", are inferences. Support: the initial, initial and final letters of `Mpwf & Ljttft` give exactly `M. & L.t`; the phrase is spelled out as `Mpwf boe. Ljttft.` on hcp-1362 (ACCEPT, no FINAL yet); hcp-1395 (FINAL) reads `M. & L.` as L. & K. in the same closing slot. If the capital were N the shift would give M. & K.S, but the pixels here are M (next point). Pointing is also open: "very nice L. & K.s" could be one phrase, though two sentences read better.
2. **`M. h` (salutation and closing).** The first letter has the same three-stroke build as the M of `M. & L.t`, unlike the two-stroke N of `Nz` (`review/work/cmp_N_rev.png`), so N is rejected by form on this card. The second sign is a stem with a small foot or arch at the base, h-like in the salutation (`review/work/c_L2b.png`), h- or b-like in the closing (`review/work/c_L6b.png`), and in both clearly unlike the L of `& L`. So I transcribe h. L is the alternative, since sister cards report this slot as `N. L.` (hcp-1402) and `N. h.` or `M-h` (hcp-1349, 1366, 1369). In the closing a dash-like lead-in stands before the first capital. Meaning and cipher status are unknown: shifted it is L. G., unshifted M. h, and neither is expanded.
3. **`dbset`.** The third sign is the writer's cursive s run into a pointed e, the same ligature as `dbse` on hcp-1378 (`work/crops/w4.png` there; here `work/crops/z_cards.png`, partly in dry pen over the portal watermark). The t's crossbar is detached and floats to the right, the same long bar form as the trailing t. At first sight the cluster looks like "e c", which gives no word; CARDS is the shape-supported reading.
4. **`ojdf`.** The pen ran nearly dry on this word and the descender of f is faint; o, the j slash, the d with ascender and the f loop are all visible (`work/crops/r_l5a.png`). The dark spot at the top of the f descender is an ink drop.
5. **`zpvs`.** The v has a rising terminal and could be taken as w (YOWR/“YOVR” gives no word); the rest of the couple's cards have `zpvs`.
6. **Punctuation and the end.** Separator dots follow the manuscript and are not significant. `Hjsm` ends in a minim group read as m; the V-shaped stroke and flourish under it are the writer's J-like slash and a paraph, not extra letters. Heading initial G may be C (as on sister cards).
7. **Salutation sense.** The sentence is terse: "Post cards to-day. Very nice." is read as the writer thanking for or commenting on cards received; the card itself does not say who sent them.

## Why it is correct

One fixed shift turns every running word into English with no adjustment (41/41 letters), including POST, CARDS, VERY, NICE and the couple's standing frame "My own … boy", "your own … girl", found on finished sister cards such as hcp-1402. The same shift gives the group `M. & L.t` the value L. & K.S, which fits the "love and kisses" closing of the correspondence. The key is the same as on those cards, and the plain Friday heading agrees with the real weekday of the postmark and written date. The message is short, so the frame words alone would not prove it; the proof rests on the independent, non-formula words POST CARDS and VERY NICE decoding under the unchanged shift.

## Credits

Solved by Claude Opus 5.5 acting as solver, 2026-10-30. No earlier work on this number. Key and formulae were taken as hypotheses from the finished sister cards and tested on this card's pixels.

## Response to review 1

Verdict REVISE, five findings. Re-run after the edits: `python3 -I ciphers/hcp-1368/work/decode.py` gives "source hashes OK", the plaintext above and 44 enciphered letters. No running word changed. The transcription of the abbreviation groups changed, and the plaintext line of the closing group changed with it.

1. **Major, trailing `t`: fixed.** Literal `N. & L.` with a shifted S could not both hold. The whole group is now one enciphered token, `M. & L.t` = L. & K.S, in `work/transcription.json`. The old "plural on a literal group" explanation and the bracketed `[s]` are gone. `work/decode.py` now counts letters in a token rather than characters, so `&`, dots and spaces do not inflate the count.
2. **Major, M not N, love and kisses: accepted and fixed.** I checked `review/work/cmp_N_rev.png` and `z_amp_N.png`: `Nz` has hook, stem and one leg, and all three group capitals have one more downstroke. The transcription now reads M. The value L. & K.S is reported as decoded and "love and kisses" only as a marked inference, in the translations too. Sister cards were not edited. `M. h` stays unresolved and printed as written, as the review asked me to state, because neither form gives a word.
3. **Minor, second initial of the `M. h` group: accepted, and taken further than asked.** The review asked me to name the alternative h. On `c_L2b.png` and `c_L6b.png` the sign has no head stroke and differs from the `& L` of the same card, so normalising it to L was the formula speaking, not the pixels. I transcribe h and name L as the alternative, because that is what the ink shows. Hence `M. h`, not the review's `M. L.`.
4. **Minor, count: fixed.** The figures are now 41 running letters, 3 group letters and 4 unresolved letters. The "no adjustment" claim is limited to the 41 running letters.
5. **Minor, "accepted" sisters: fixed.** Origin and "Why it is correct" now cite only finished cards (hcp-1378, 1395, 1402). The hcp-1400 and hcp-1396 citations are gone. Cards not yet final (hcp-1349, 1362, 1366, 1369) are labelled, or cited only for a reported form. CARDS rests on this card's pixels and hcp-1378.
