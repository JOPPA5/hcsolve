# hcp-1449 (pc_hcp_130) – solution, round 1

Solver: Claude Opus 5.5 (claude-opus-5-5), 2026-10-30. Earlier source capture and triage (2026-10-26) were done by an OpenAI GPT solver (see NOTES.md); that work established no reading. No published solution of this card was found or used; the portal attaches no transcription or solution (status "Not solved").

## Cipher type and key

**English written in Greek letters** (letter-for-letter transliteration, a monoalphabetic substitution of Latin letters by Greek letterforms, with a few Latin letters left in place). The postcard is a Photochrom card of Bangor Cathedral, posted from Menai Bridge ("Sat evening") to Miss L. Thompson, 85 Upper Highgate St, Birmingham; the three cipher lines and a monogram signature sit under the plain-text place/day heading.

| glyph | plain | notes |
|---|---|---|
| Η (cursive, U-shaped with bar) | h | have, him |
| α (written like q) | a | |
| one v-shaped glyph, transcribed υ / ν | **v** (have) and **n** (seen, kind) | one glyph, two values, distinguished by context only |
| η, usually with an over-bar (η̄) | e | over-bar in have, seen |
| ο | u | just, out |
| ω | o | |
| σ | s | |
| τ | t | |
| μ (w-like) | m | |
| γ (y/ʒ-shaped, with descender) | **g** (regards); **g or y** in word 4 | if word 4 is "my", γ serves for both g and y |
| φ: tall looped f (for) and barred descending φ (off) | f | two allographs |
| λ | l | |
| κ | k | |
| ρ | r | |
| ι | i | |
| δ | d | |
| j, w | Latin j, w kept | j in just; final w of tomorrow |

Notes on the key: the sender writes English *u* as ο (cf. Greek ου) and English *o* as ω; *j* (no Greek equivalent) and the final *w* of "tomorrow" are Latin. The v-shaped glyph in "have" (υ) and the n-glyph in "seen"/"kind" (ν) are graphically almost the same; they are distinguished only by context.

## Transcription (work/transcription.txt, my own, from enlarged crops of source/address.jpg)

```
Ηαυη jοστ σηην μγ ωφφ
λωωκ ωοτ φωρ Ηιμ
τωμωρρωw κινδ ρηγαρδσ
```
followed by a monogram signature (two interlaced capitals, possibly "M" / "HM"), not enciphered and not read.

## Command (run from repo root)

```
python3 -I ciphers/hcp-1449/work/decode.py
```
It verifies the SHA-256 of all files in source/ against work/source-sha256.json and prints the mechanical transliteration:

```
have just seen mg off
look out for him
tomorrow kind regards
```

## Plaintext

Literal (as on the card): **Have just seen ⟨mg⟩ off. Look out for him tomorrow. Kind regards.** — signed with a monogram.

Word 4 is exactly two signs ⟨μγ⟩ = "mg", followed directly by "off"; nothing is missing on the card. Possible readings (see uncertainty 1): initials "M.G." of the person seen off (the "him" of line 2), or "my" with γ also used for *y* and a noun omitted by the writer [sic].

- English: Have just seen ⟨M.G.⟩ off. Look out for him tomorrow. Kind regards.
- Slovak: Práve som odprevadil(a) ⟨M.G.⟩. Zajtra ho vyhliadaj (čakaj ho). Srdečné pozdravy.

## Uncertainties

1. **Word 4 ⟨μγ⟩** (line 1). Both glyphs are read from the pixels (a w-like μ as in "him", and the same y/ʒ-shaped glyph as γ in "regards"), but the word is not a normal English word: "mg" mechanically; "my" if γ also serves for *y* (then a noun seems omitted); or initials/nickname of the person seen off. Reported literally; this is the only open point of meaning.
2. **Middle glyph of "out"** (line 2, ⟨ωοτ⟩) is overwritten/blotted; a round ο-shaped core is visible and read as ο (= u, as in "just"). Not a restoration of a missing sign, but the reading is guided by context.
3. υ (v) vs ν (n) are near-identical v-shapes; the key distinguishes them by context only (have / seen, kind).
4. ω stands for o; the last letter of "tomorrow" is larger, read as Latin w. The image resolution (~1024 px card width) is low; every letter was checked at 5–8x enlargement.
5. The monogram signature and the sender's identity are not read. The date is unknown (only "Sat evening").

## Why I believe it is correct

- Every glyph of all three lines is covered by one consistent 19-sign table and yields English words: have, just, seen, off, look, out, for, him, tomorrow, kind, regards – all of them in a coherent short postcard message (someone departed; the recipient should expect him tomorrow).
- The key is internally consistent across repetitions: ω = o in look/for/tomorrow/off; σ = s in just/seen/regards; ρ = r in for/tomorrow/regards; Η = h in have/him; η = e in have/seen/regards; δ = d in kind/regards.
- Greek-letter English is a well-known Edwardian postcard "cipher" for schoolchildren and young adults who learned the Greek alphabet; it fits the plain address (Birmingham) and Welsh holiday location (Menai Bridge, Bangor).

## Response to review 1

Review 1 (Claude Opus 5.5, separate agent) gave the verdict **ACCEPT** with four minor findings and no blocker or major issue. Its independent transcription and decoder gave the same three lines. All four findings are accepted; no decoded letter changed.

1. **Word 4 rendering (minor) – fixed.** The plaintext section now gives one consistent rendering: literal "Have just seen ⟨mg⟩ off", with no inserted gap (the card has exactly two signs ⟨μγ⟩ followed directly by "off", as the reviewer confirmed on thresholded crops). The alternatives (initials "M.G."; "my" with an omitted noun [sic]) are stated as readings, not as text, and "him" is no longer put in the bracket. The English and Slovak lines use the same ⟨M.G.⟩ rendering. The monogram signature is not equated with ⟨μγ⟩: on the scan it is two interlaced capitals whose letters cannot be read with confidence (H/J + M?), and nothing links it to word 4.
2. **γ doing double duty (minor) – fixed.** The key table now states γ = g (regards) and γ = g or y in word 4, i.e. if "my" is read, one glyph serves for two letters. The decoder keeps the mechanical value g.
3. **Allographs (minor) – fixed.** The key table and the header of work/transcription.txt now record e as η with an over-bar (η̄) in "have" and "seen", and the two f-forms (tall looped f in "for", barred descending φ ligature in "off"). The transcription lines themselves are unchanged, so the decoder output is unchanged.
4. **ν/υ (minor) – fixed.** The key table now shows them as one v-shaped glyph with two values (v in "have", n in "seen", "kind"), distinguished by context only.

Re-run after the changes, from the repo root: `python3 -I ciphers/hcp-1449/work/decode.py` → all three source hashes OK; output `have just seen mg off / look out for him / tomorrow kind regards`, identical to round 1.
