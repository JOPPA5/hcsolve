ACCEPT

# Review 1 of hcp-976 (reviewer: Claude Opus 5.5, 2026-11-03)

## What I verified and how

1. Ran the solver's command from the repo root: `python3 -I ciphers/hcp-976/work/decode.py`. Source hashes OK; the output matches the claimed plaintext line by line (Meinen Lieben! / Heute sende / euch die Ansich- / ten von Brück- / enau. Diese ist / die - Mitte, Nr 2 / die linke Seite, / + Nr 3 die rech- / te Seite. onsre / Vila steht).
2. Wrote my own decoder, `review/work/mydec.py` (regex-based, separate handling of {literal}, [struck], 5^ = ü), and ran it on work/transcription.txt: identical output. All ten digits 0-9 occur; each has one value; no digit is left undecoded. The key (a e i o u = 1-5, l m n r s = 6-0) is the same as the one on sister card hcp-974 (same addressee, "3)"), which I read in its SOLUTION.md; on this card every key value is fixed by at least one unambiguous word (Heute, sende, Ansichten, von, Brückenau, linke, Mitte).
3. Checked the transcription against the original scan work/hires/..._adr.jpg, rotated 90 degrees clockwise (review/work/msg_rot.png), in eight enlarged strips (review/work/s00-s31.png) plus close-ups z_bottom_left.png, z_cross.png, z_mitte.png. Every row was checked sign by sign: H25t2 02nd2 / euch D32 1803ch / t28 V48 B95^ck / 2815. D3202 30t / D32 - 73tt2, Nr 2 / D32 638k2 023t2, / + Nr 3 D32 92ch / t2 [cross-mark] 023t2. 48092 / V361 0t2ht. I agree with all digit readings. "48092" really begins with 4 (o), not 5, so "onsre" is what is written; the solver reports it literally and discloses it.
4. Stamp box (review/work/stamp_enh.png, contrast-enhanced): the stamp has been removed; only paper residue and the postmark remain, with no writing in the box. Picture side (review/work/pic_small.png): only the printed captions (Bad Brückenau, Kurpark, Hotel Füglein) and the handwritten "1)". I found no steganographic message, so the `MASC + Steganography` label that applies to the Jolánka series does not apply here. `MASC` is correct.
5. Context: Brückenau matches the picture, the publisher imprint (Hans Brust, Brückenau) and the postmark BRÜCKEN[AU]. The text describes a numbered three-card panorama (this card is "1)", the middle; 2 = left side, 3 = right side), which is consistent with the "1)" marking. The German is natural for 1910. The plain-Kurrent address reading "Emma Krumbholz, Heidelberg, Mittelstr. 18" agrees with the scan.
6. Sources: the portal has no attached solution. The solver states that no published solution was found and credits the work correctly.

## Findings

1. (minor) The "+" before "Nr 3" (line 8) is very probably the common handwritten abbreviation for "und": "Nr. 2 die linke Seite, + [und] Nr. 3 die rechte Seite". The line-by-line plaintext keeps "+", but the running text and the English and Slovak translations drop it without comment. Render it as "und / and / a", or at least note this reading in uncertainty 4.
2. (minor) The cross-mark before "Seite" in line 9 (a long dark stroke crossed by three uprights, review/work/z_cross.png) is in darker ink, like the heavily retraced 3 in "Seite", the 0 of "steht" and the margin "+". This may be a later retracing or annotation pass. The solver correctly leaves the mark out of the plaintext and discloses it. It does not affect the reading, but uncertainty 4 could mention the darker ink.
3. (minor, cosmetic) The decoder prints "Die" and "Von" with capitals in mid-sentence because the transcription uses D and V for the writer's looped forms. SOLUTION.md normalises them to lower case. The two forms differ only in case; this needs no action beyond consistency in the report.

## What I could not verify

- Cards 2 and 3 of the series are not in this collection entry, so the continuation of "unsre Vila steht ..." cannot be checked.
- Whether the darker-ink marks are by the sender or a later hand cannot be decided from the scan.
- I did not repeat a web search for a published solution; I rely on the portal's "Not solved" status and the solver's statement.

## Overall

The whole card is read, every cipher sign decodes with one consistent key, and the plaintext is coherent and fits the context. The card ends mid-sentence because the text continues on the next card in the series, not because anything is unread. The verdict is ACCEPT, with the minor wording fix in finding 1 recommended for the report.
