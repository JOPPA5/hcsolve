# HCP 1400 / pc_hcp_81 — partial Caesar decipherment

**Partial; no DONE1.** Most of the body is read, while one body letter, short upper fields and the closing remain unresolved.

Root read the rendered General, Description and Attachments tabs: Not solved, no supplied transcription/solution. Both immutable scans were inspected by this solver. Picture caption: Kirkstall Abbey, Leeds. No handwritten cipher continuation was seen on the picture. The ordinary address is Miss Dean, Court House, Wimborne, Dorset. Portal date is 1908-02-15. No published decipherment or external plaintext corpus was used.

## Establishing the cipher independently

A rough manual Latin-letter transcript was screened through all 26 Caesar shifts and Atbash, rather than assuming that the key from the preceding Abbott correspondence applied. Subtracting one gave the exact words EXCUSE (fydvtf) and CARDS (dbset), while the provisional Jibuf gave IHATE. This prompted a fresh visual reading of the surrounding joins, yielding qmfbtf PLEASE, uxp TWO, pomz ONLY and ljoe KIND. The initial screen's misread joins are retained in `work/transcription.json` for reproducibility; they are not passed off as a validated ciphertext.

The independently supported key is:

```
Cipher: ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain:  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

## Body reading

```
qmfbtf fydvtf   -> PLEASE EXCUSE
uxp dbset       -> TWO CARDS
pomz ljoe Jib?f -> ONLY KIND IHA?E
```

32 body letters map to the key, with one remaining ambiguous position in the final group. Cipher w would give I HAVE; cipher u would give I HATE. The context strongly favours:

> Please excuse two cards, only kind I have.

That is a **contextual reading of the ambiguous word**, not an excuse to silently replace the source glyph. No missing “the” is inserted into the literal output. Word spacing between I and HAVE/HATE is editorial: the writer joins the group.

Slovak translation of the contextual body reading:

> Prepáčte tie dve pohľadnice; mám iba tento druh.

The literal output with the unresolved position takes priority over this explanation.

## Remaining handwritten fields

- The top dotted field resembles S. followed by a Z/7-like sign and a horizontal flourish. It may be initials, a number or shorthand; no interpretation is asserted.
- The next short line begins with an Nz/Sz-like group, then E-like and b-like dotted signs and a joined final group. MY is possible for Nz, but is not frozen solely to create a greeting. The remaining signs are not expanded into names or terms of address.
- The lower closing begins with a joined zpvst/zpst-like group, possibly YOURS or YORS. Exact letter count and the u/v join are not established.
- The closing includes S.b., which would become R.A. if it uses the established cipher. Its status as ciphered initials rather than ordinary initials is not independently certain.
- The final group appears C[b/h]z. Under the shift it would be B[A/G]Y. It is not silently repaired to DAY, BYE or a familiar surname. A better reading of the middle ascender and the capital is needed.

These fields are preserved as unresolved in the working transcript and decoder. No part of them has been discarded as irrelevant to completion.

## Reproduction

Run from the repository root:

```
python3 ciphers/hcp-1400/work/decode.py
```

This checks immutable source hashes, prints the frozen body reading and both final-word alternatives, and exposes the unresolved fields. It decodes a manual transcription, not image pixels.

The original bounded diagnostic is reproduced by:

```
python3 ciphers/hcp-1400/work/screen.py
```

It prints 26 Caesar outputs and Atbash for the original **provisional** transcription. These are hypotheses, not 27 decipherments. Its failure to produce a fully fluent message from the imperfect input would not exclude a Caesar reading after correction.

No reviewer, watcher, report, register entry or FINAL was created.

## Re-examination 2026-10-29 (Claude Opus 5.5) — status unchanged: PARTIAL

Earlier work (transcription, key, body reading) was done by the OpenAI GPT solver; Claude Opus 5.5 re-checked it on the pixels and confirms the Caesar −1 body reading PLEASE EXCUSE / TWO CARDS / ONLY KIND I HA?E. The ambiguous letter's outline (two downstrokes) looks more like cipher u (HATE) than w (HAVE), against the context, which favours HAVE; still unresolved.

Still unread: the third group of the salutation line ("Nz E.h. ???" — a k/H-like sign, long descender, bowl, n/m with long tail) and the closing "z?s S.h. C?z." (possible YOR/YOUR … R.G. … BOY if the middle signs are p, but h readings are not excluded). Details and crop files in NOTES.md (2026-10-29 entry). No DONE1: a complete reading would require forcing words onto these groups.
