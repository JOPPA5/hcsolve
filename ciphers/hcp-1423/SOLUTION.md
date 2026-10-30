# HCP 1423 / pc_hcp_104 — unresolved visual screen

No decipherment is claimed. No DONE marker is warranted.

The portal was observed as **Not solved**, with no attached transcription or solution. The picture identifies the building as “The Temporary Home for Children, Mineola, L. I.” The reverse is an unused address side: no sender, addressee, stamp, or postmark was observed. The tiny pencil inscription alongside the printed caption is not securely read.

## Evidence and tentative method

The original picture has two faint rows of horizontal and short upright/slanted strokes in its right margin. Turning the picture 90 degrees clockwise places both rows horizontally below the photograph. These look compatible with Morse notation, but the standard, direction, and letter boundaries are not established.

`work/transcript.json` freezes **18 tentative strokes in the upper row only**, with a seven-group spacing hypothesis. It is a manual reading of the scan, not an attached transcription and not OCR. Under International Morse that grouping reads:

```
-.. -.. .... --- . .. -.
 D   D   H   O   E  I  N
```

This is a screen result, not plaintext. Reversing the groups and/or the strokes inside each group likewise gives no supported reading. The lower row includes at least two overwritten or crossed clusters and remains untranscribed. Round dark spots close to some strokes must not automatically be treated as Morse dots. In particular, near the upper row's last dash, the round spot above and the vertical pencil stroke below are visually different.

## Reproduction

Run from the repository root:

```
python3 ciphers/hcp-1423/work/screen.py
```

The script checks hashes of all immutable source files and reproduces the four bounded International-Morse direction/grouping screens from the manual transcript. It does **not** extract symbols from image pixels. There is no established key, full plaintext, translation, or validated completion.

## Remaining work

A higher resolution scan or a justified reading of the lower row and gap sizes is needed before a complete Morse hypothesis can be tested. Other encodings remain possible. No published solution was used. No register entry or completion marker has been written.

## Update 2026-10-30 (Claude Opus 5.5) — still partial

Independent re-reading of both columns (`work/mark-inventory-claude.json`) confirms the GPT conclusion: no decipherment can be claimed. The top stroke is a paper crease; the right column contains an overwritten cluster and a crossed mark that cannot be resolved at the available resolution; the role of the round spots is undecided; there are no letter separators. Dictionary-constrained Morse segmentation of the readable stretches in both directions gave no supported text. See NOTES.md (2026-10-30). No marker has been created.
