# Triage notes — 2026-10-26

All three rendered tabs read; fresh status Not solved. Neither skip.txt nor markers excluded this item. No watcher or reviewer was started, following the user override.

The address side has ordinary cursive above a short three-line transformed handwritten passage and a monogram. The picture is Bangor Cathedral, nave, with no visible handwritten message. A 270-degree rotation is saved in work/address-rotated.jpg; work/message.jpg crops the passage.

The ordinary cursive appears to include “Menai Bridge / Sat evening”, while the addressee is Miss L. Thompson in Birmingham. These are contextual readings, not deciphered cipher text. The three-line passage uses Latin-like, Greek-like or transformed letterforms; a trustworthy complete glyph segmentation and mapping were not established. Superficial guesses such as “Have ... tomorrow ...” were rejected as insufficient evidence.

This is source capture and triage only. There is no verified plaintext, no key, no SOLUTION.md, and no DONE1. A next attempt should freeze a glyph inventory against an enlarged crop before trying MASC or systematic character transformations. Do not silently normalize the shapes to expected English.

## Offline revisit, 2026-10-26

Inspected saved full scan and message crop again. Generated and visually checked a horizontal mirror and a 180-degree rotation of the crop (work/message-mirror.jpg and work/message-180.jpg). Neither provides an immediately readable ordinary-English passage; this is a bounded visual observation only, not exclusion of all mirror/rotation mechanisms. No full Latin transcription was frozen because several strokes cannot yet be distinguished from transformed or custom glyphs. Consequently a Caesar/Atbash computation over guessed Latin letters would have weak evidential value and was not passed off as key testing. No new plaintext or marker.

## 2026-10-30 – Claude Opus 5.5 (solver)

Recognised the passage as English written in Greek letters (Η=h, α=a, υ=v, η=e, ο=u, ω=o, σ, τ, ν, μ, γ, φ=f, λ, κ, ρ, ι, δ; Latin j and final w). Transcribed all three lines from 5–8x enlarged crops of work/message.jpg (work/transcription.txt), key in work/key.json, decoder work/decode.py (checks source hashes). Reading: "Have just seen ⟨μγ⟩ off / look out for him / tomorrow kind regards". Residuals: word 4 ⟨μγ⟩ ("mg" literal; "my" or initials), blotted middle glyph of "out" read as ο, υ/ν near-identical. The earlier rejected guess "Have ... tomorrow" was right in direction; the GPT triage did not identify the system. SOLUTION.md written; DONE1 created.

## 2026-10-30 – Claude Opus 5.5 (solver), after review 1 (ACCEPT)

Addressed the four minor findings: consistent literal rendering of word 4 ⟨mg⟩ (alternatives M.G. / "my" [sic]); key table now shows γ g/y, υ/ν as one glyph, η̄ and the two f-forms; allograph notes added as comments to work/transcription.txt (decoder output unchanged, re-run OK). Wrote report/report.md + report.pdf and register-entry.txt; FINAL.
