# HCP 1404 (pc_hcp_85) — solution, round 1

Postcard (Raphael Tuck "Oilette", The Norfolk Broads series III; picture: Fritton Decoy, Norfolk Broads), postmarked 30 Jan 1908, to Mrs W. Abbott, (Stokelake?) Farm, Chudleigh, S. Devon (portal records the recipient as "W. Abboú"). Portal status: Not solved; no transcription or solution attached; no published decipherment of this card found. One of the Caesar-shift sweetheart cards hcp-1386…1407 written by the same couple (1907–08).

## Cipher type and key

Monoalphabetic Caesar shift: each plaintext letter is written as the **next** letter of the alphabet (encryption +1, decryption −1).

```
cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

The heading "G. H. Thursday." and the date "January 30th = 08" are ordinary writing, not enciphered (as on every card of this family).

## Transcription and plaintext (all writing in the message area)

| Ciphertext (manual, from the scan) | Literal plaintext |
|---|---|
| G. H. Thursday. *(plain)* | G. H. Thursday. |
| Zpvs. Pxo. | YOUR. OWN. |
| E. L. Hjsm. | [E. L.] GIRL. |
| January 30th = 08 *(plain)* | January 30th 1908 |

11 enciphered letters, all decoded by the one key; 2 abbreviation letters (E. L.) kept literal (shifted value D. K. printed alongside by the command).

English: *"G. H. Thursday. Your own E. L. girl. January 30th '08."*

Slovak: *„G. H. Štvrtok. Tvoje vlastné E. L. dievča. 30. januára 1908."*

(Language of the plaintext: English; the portal lists the language as Unknown.)

## Command (from the repo root)

```sh
python3 -I ciphers/hcp-1404/work/v2/decode.py
```

It checks the SHA-256 of all three files in `source/` (`work/source-sha256.json`), decodes every token of `work/v2/transcription.json`, checks the round trip, and prints the plaintext above (saved in `work/v2/plaintext.txt`). The transcription is manual (from enlarged crops `work/v2/crops/`), not OCR. The older `work/decode.py` / `work/transcription.json` are the earlier partial GPT version, kept for the record.

## Uncertainties

1. **`E. L.`** before GIRL: an abbreviation group, kept literal and not expanded (e.g. "ever loving" is a possible reading, but nothing on the card proves it; whether the initials are themselves shifted is undecided). On this card the separator between E and L is a short dash-like stroke, and the L is a tall stroke with a looped foot (`work/v2/crops/EL-field.png`). The reading is based on the pixels and confirmed by the identical closing formula `Pxo. E. L. Hjsm` on sister card hcp-1386 (same hand, same letter shapes: `ciphers/hcp-1386/work/crops/band6.png`). The earlier GPT notes left this field unresolved ("E + small mark + tall l/t/1-like stroke"); a reading as numeral "1" is rejected because the stroke has the same looped foot as the L of the hcp-1386 group.
2. The final `s` of `Zpvs` is written as this writer's c-like terminal s (same form in `zpvs` on hcp-1386); `P` of `Pxo` has its long top stroke extending to the right over the line, as in hcp-1386.
3. Heading initials G. H. (or C. H.) and the farm name in the address are not ciphertext and not established exactly; they do not affect the decipherment. The picture side has only the printed caption.

## Why it is correct

One fixed shift turns every enciphered word into English (YOUR, OWN, GIRL — 11/11 letters), with the same key established independently on many sister cards of this couple (hcp-1397 FINAL: "from your own girl"; hcp-1386: "your own E. L. girl"). The message is the writer's standard closing formula, which fits a short one-line sweetheart postcard of 1908 and its postmark.

## Credits

Download of the sources, key identification and a 12-letter partial transcript (field before GIRL left unresolved): OpenAI GPT solver (GPT-6 Astra / GPT-6.1 Sol), 2026-10-26. Completion (re-transcription from the pixels, reading of the E. L. field by comparison with hcp-1386, new decoder): Claude Opus 5.5 acting as solver, 2026-10-29.

## Response to review 1

Review 1 (Claude Opus 5.5, separate agent, 2026-10-30), verdict **ACCEPT**, four minor findings. No decoded letter changes; the reading is unchanged.

1. **Family inconsistency over the initials (minor) — agreed, disclosed; no change to the reading.** On hcp-1395 the closing initials "M. & L." were read as ciphertext (L. & K., "Love & Kisses" as a possible expansion), while on hcp-1386, hcp-1401 and this card "E. L." is kept literal. The two treatments rest on different evidence: on hcp-1395 the shifted value gives a standard closing (L. & K.), here the shifted value D. K. has no obvious expansion while the literal E. L. admits one ("ever loving"), which mildly favours literal. Neither is proven. The report states this family-level inconsistency explicitly and gives both values; the command prints both (`[E. L. | shifted: D. K.]`).
2. **Normalisation "E-l." → "E. L." (minor) — agreed.** On the card the E and L are joined by a short dash and the L is a tall stroke with a looped foot (`work/v2/crops/EL-field.png`); the transcription normalises this to "E. L." (already noted in `work/v2/transcription.json`). The report shows the field as written ("E-l.") and states the normalisation.
3. **Heading initial G or C (minor) — agreed.** The heading is plain writing, not ciphertext; the first letter could be C (hcp-1386 reads "C. H." in the same slot). The report gives it as "G. H. (or C. H.)" and does not assert G.
4. **Superseded files (minor) — agreed.** `work/decode.py`, `work/transcription.json` and `work/plaintext.txt` are the earlier partial GPT version (they decode the E with the cipher and leave the field unresolved). They are kept for the record only; the report cites only `work/v2/`.

Re-run after the response (repo root): `python3 -I ciphers/hcp-1404/work/v2/decode.py` → "hashes OK", `YOUR. OWN. / [E. L. | shifted: D. K.] GIRL.`, heading `G. H. Thursday.`, date `January 30th = 08`, 11 enciphered letters decoded + 2 abbreviation letters kept literal. Unchanged.
