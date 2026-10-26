# HCP 1442 / pc_hcp_123 — complete solver candidate

Three-count Pigpen on the address side. The main passage and central continuation/signature account for **46 cipher letters**. This is a solver candidate awaiting independent review, not an accepted solution. No published solution was used.

## Source and scope

Fresh rendered General, Description and Attachments were captured by the root solver on 2026-10-26. Status Not solved, tags Postcard HCPortal collection and Pigpen; date 1907-12-16, recipient Ray Bartley, North America, private collection. Both original scans and metadata are immutable in source/. The picture side is a flower illustration with a small ordinary cursive mark at lower-left; no evident Pigpen continuation.

The main cipher is read after rotating the address scan clockwise90°. The central passage under ordinary cursive is read after rotating clockwise270°. Work crops preserve these frames. Ordinary date/addressee and cursive are not counted among the46 cipher letters. Manual transcription is work/transcription.json, not OCR or an attached transcript.

## Key

Each outline has one, two or three dots. The table records **present ink borders** (B bottom,T top,L left,R right; C closed square).

| Outline | Shape | 1 dot | 2 dots | 3 dots |
|---|---|---|---|---|
| BR | ┘ | A | J | S |
| B | ⊔ | B | K | T |
| BL | └ | C | L | U |
| R | ] | D | M | V |
| C | □ | E | N | W |
| L | [ | F | O | X |
| TR | ┐ | G | P | Y |
| T | ⊓ | H | Q | Z |
| TL | ┌ | I | R | — |

The same conventional key was independently being used by the root solver on neighboring1440 and supplied as a hypothesis. All tokens here were then manually checked against the actual1442 scan. Cross-card agreement is supporting context, not proof of any glyph identity.

## Plaintext

Main passage, preserving spelling/punctuation and line order:

```text
MON,
IF, YOU, DONT, GO
TO-NIGHT, CALL
ME UP.
```

Central cipher, following ordinary cursive “This is”:

```text
SAT
AFTERNOON
NANCY.
```

Word spaces in ME UP and TO-NIGHT are editorial segmentation of the decoded letter stream. DONT is literal, with no apostrophe added. SAT is the recorded three-glyph reading; MON is the separate main heading. Ordinary cursive appears to read “Dec16-07 / Received your / card Sat morning / This is”; it is context transcription, not a decoded cipher output.

## Slovak translation

„PON[DELOK]. Ak dnes večer nepôjdeš, zavolaj mi.“

Central continuation: „[Toto je] sobotné popoludnie. Nancy.“

These translations expand MON and SAT contextually; the actual decoded words remain MON and SAT. The apparent date/day mismatch between MON, SAT and the written/postal date is retained, not repaired.

## Reproduction

From the repository root:

```sh
python3 ciphers/hcp-1442/work/decode.py
```

The command verifies source checksums, decodes the manual glyph tokens with the above key, verifies all46 letters against the displayed text and checks re-encoding. It does not extract text from pixels; the scan-to-token stage is explicitly manual. Round-trip consistency is not independent transcription proof.

## Evidence and uncertainties

All46 recorded cipher letters use one key with no ad hoc exceptions. The main message and central signature are coherent. The second letter of MON is an open-right bracket with a short/faint upper border, rather than the corner that its low-resolution outline can resemble. Central SAT has outlines┘3,┘1,⊔3; diagonal watermark lines cross these signs and are excluded as non-ink borders. These deserve particular independent visual checking.

The central date/day wording is temporally awkward and does not justify changing a glyph. Nancy is a decoded signature, not a confirmed historical sender identity. No attribution beyond that is asserted. No independent review, PDF, register entry or FINAL exists yet.

## Response to review 1

Reviewer: Claude Opus 5.5, verdict ACCEPT (review/REVIEW1.md, 2026-10-26). The reviewer read all 46 Pigpen signs from source/address.jpg independently, in its own notation and from its own crops, and decoded them with its own script built from the grid geometry; the result agrees with work/transcription.json letter for letter (46 = 46), including the two signs flagged above (the second sign of MON, [2 = O, with a faint but present top stroke and no right stroke; and the third sign of SAT, ⊔3 = T, with the crossing watermark lines excluded). It found no untranscribed Pigpen on either side. The plaintext is unchanged.

1. Date/day "mismatch" (minor). Accepted and corrected here and in the report. 16 December 1907 was a Monday (`datetime.date(1907,12,16).strftime('%A')` → Monday), so the main heading MON agrees with both the handwritten date "Dec. 16-07" and the DEC 16 postmark; this is positive evidence for the reading, not a problem. Only the centre note ("Received your card Sat morning / this is SAT AFTERNOON NANCY") refers back to Saturday 14 December. The natural interpretation is that the centre note was written on Saturday afternoon and the main message added on Monday, when the card was dated and posted. The earlier sentence that "the apparent date/day mismatch between MON, SAT and the written/postal date is retained, not repaired" is superseded by this paragraph. No glyph was changed.
2. Card context not recorded (minor). Accepted. The card itself is addressed in plain writing to "Ray E. Bartley, Rutland, Iowa" (the portal gives "Ray Bartley", location North America), and the cancel reads RUTLA[ND] DEC 16 … IOWA with no legible year; the stamp is a US one-cent Franklin. The card was therefore local mail within Rutland, which fits the request "call me up" (by telephone). The year 1907 comes from the handwritten "Dec. 16-07" and the portal. These details are in the report; source/metadata.md is unchanged.
3. Underline not recorded (minor). Accepted. In main line 4 a pen stroke runs under the two signs of ME (review/work/l4.png), most likely emphasis ("call ME up"). It is not a cipher sign and does not change the reading; the report's literal transcription notes it.
4. Protocol (minor). Acknowledged. A file in work/ was apparently created or removed seconds after DONE1; the source hashes still match and the decoded output is identical to work/plaintext-check.txt, so the result is unaffected. No watcher was started for this cipher during solving. The report adds an English normalized reading alongside the Slovak translation.

Additional note from the closing pass: the mark after the last centre word looks like a comma on the scan (the reviewer transcribed it as "NANCY,"), whereas work/transcription.json displays "NANCY."; this is punctuation only and does not affect any decoded letter. The small cursive mark at the lower left of the picture side (read by the reviewer as something like "23" or "JB") is not Pigpen and is not read securely.

Remaining uncertainties carried into the report: the identity of "Nancy" and her relation to Ray E. Bartley are not established; the cursive context lines are only partly legible under the watermark ("morn…"); the postmark year is illegible; no search for a prior publication was made beyond the portal status, skip.txt and the AI Decipherment Register snapshot.

Closing steps (this response, report, register entry, FINAL) prepared by Claude Opus 5.5 on the solver's behalf at the human's request, 2026-10-26.
