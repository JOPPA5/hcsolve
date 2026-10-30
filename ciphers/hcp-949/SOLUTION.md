# HCP 949 — partial German Pigpen reading

**Partial; no DONE or full-message claim.** A pair-filled German Pigpen alphabet and a reversed orientation give the connected opening **HAST DU DICH GUT AMMUS…**. The remaining cipher contains inconsistent-looking letters, overprinting, detached strokes and a nonstandard wedge. They have not been converted into a complete German message.

## Provenance and scope

Root inspected all three rendered portal tabs on 2026-10-28 UTC and recorded status **Not solved**, Pigpen tag, recipient **Erna Garbe**, approximate date **1909**, and no attached individual transcription or solution. Root also inspected all 158 rendered AI-register entries and found no HCP 949 entry. That is a bounded register check, not a claim that no published solution exists elsewhere.

I inspected both originals. The picture side is a woman's portrait, with no observed handwritten cipher. The address side contains ordinary German cursive, the address Erna Garbe / Reddelich, and angular cipher along two margins. The cursive greeting appears to include “süße Erna”; that reading was not used as a plaintext crib. The ordinary cursive body has not been fully transcribed or translated. Portal provenance is in `SOURCES.md` and `source/metadata.md`.

The collection paper linked by the portal is generic; root's bounded inspection found no matching individual solution. No published plaintext was used in this attempt.

## Key and orientation

For the legible opening, rotate the address-side image **270 degrees counterclockwise**. The message starts on the shorter upper line in that orientation, **HAST DU DICH**, then continues along the longer lower line **GUT AMMUS…**. This is 180 degrees from the orientation in which the ordinary cursive is upright. Cipher along the adjacent margin requires its own 90-degree turn to become horizontal.

The useful key is the omitted-J, pair-filled grid. Shape names specify their visible walls, not the direction in which they open:

| Shape | ┘ | ⊔ | └ | ⊐ | □ | ⊏ | ┐ | ⊓ | ┌ |
|---|---|---|---|---|---|---|---|---|---|
| Plain | A | C | E | G | I/J | L | N | P | R |
| Dotted | B | D | F | H | K | M | O | Q | S |

The X-shaped extension is down-pointing wedge = T, dotted = U; right-pointing wedge = V, dotted = W; left-pointing wedge = X, dotted = Y; up-pointing wedge = Z. The final dotted up-pointing wedge is **not assigned an extra alphabet letter**. The 25-letter omitted-J alphabet does not supply a 26th letter for that cell. Not every conventional table cell is independently observed on this card.

Agent HCP 962 reported this same generic key family; no plaintext from that different card supplied the reading here. The family and reading orientation were tested against this scan itself. This is solver collaboration, not independent review.

## Provisional literal decoding

The following is a mechanical rendering of the current manual shape inventory, retaining problematic forms:

```
HAST DU [detached stroke] DICH
GUT AMMUSKMT B E K K [dotted Z-shaped wedge] U [detached stroke] HAURF [detached stroke]
```

Spaces here are editorial. The B near the crossed patch is provisional. The 18 connected letters **HASTDUDICHGUTAMMUS** have support from their repeated shapes and the established key. The short separate margin starts provisionally **GE**, followed by three unresolved angular forms and a canceled hatch.

Partial translation: “Have you … well …”. **AMMUS…** could be the start of a misspelled *amüsiert* (“enjoyed yourself”), but the actual continuation is not established. **AMMUSKMT** has not been replaced with AMUSIERT. The last group may invite *zu Hause*, but the observed forms currently yield a nonstandard dotted wedge plus **U…HAURF**. **ZUHAUSE is a hypothesis, not the reading.**

The central box after AMMUS visibly contains a dark interior mark and gives literal **K**, contrasting with the unmarked I box in DICH. The next bracket was initially misclassified as a dotted cup Q; direct inspection of `work/ammus-controls.png` instead shows a dotted three-sided bracket, provisionally M. Two later boxes over the ordinary greeting likewise appear marked, giving **KK**, not silently II. The terminal R/F forms also must not be normalized to S/E to obtain a familiar word.

## Reproduce

From repository root:

```
python3 ciphers/hcp-949/work/decode.py
```

This verifies the original source hashes and decodes a **manual** inventory. It is not OCR and does not establish its own transcription. `work/inventory.json` has 40 provisional graphic units with approximate original-image pixel coordinates: 32 body forms, three detached strokes and five marginal forms. A canceled hatch is separately excluded. The overall segmentation is provisional, not an accepted count of ciphertext letters.

Reading aids are exact source crops rotated and enlarged. They do not add image information. `work/reading.png`, `work/ammus-controls.png`, and `work/margin-horizontal.png` locate the chief open issues.

## Discovery and validation limits

An arbitrary-substitution screen on the original 35-unit provisional body produced fluent-looking but invalid German fragments. It did not solve the card. An initial LIEBSTE hypothesis was rejected because it did not survive repeated-shape/segmentation constraints.

`work/key-screen.py` then enumerated 26,112 generic key/orientation cases without target plaintext input. It uses an existing German four-gram model, with provenance in `batches/scoring-sol61/german/README.md`. The original draft improperly wrapped the unused 26th cell of the omitted-J key back to A; that implementation error is corrected. The corrected screen treats that cell as unknown, so its numerical ranking cannot be cited as proof of the candidate. After the bracket transcription correction, results were regenerated in `work/key-screen-results.json` and `work/key-screen-summary.txt`.

The opening is supported by actual glyph inspection, not the model score. The adjacent margin was excluded from the key screen. A separate turn of that held-out crop gives compatible **GE** under the same pair-filled table, but the remaining forms do not yet provide a complete predictive word. This is limited corroboration, not full validation. No control experiment establishes search recovery power for this short noisy target, and no independent review has occurred.

## Remaining work

- Resolve the marked box/bracket sequence after AMMUS from the scan; do not force AMUSIERT.
- Re-examine the crossed patch near provisional B and the two marked boxes over cursive Erna.
- Identify the nonstandard dotted Z-shaped wedge and account for each of the three detached strokes.
- Resolve the last two body forms and the three remaining margin forms.
- Audit the inventory against original pixels before treating its 40 graphic units as final segmentation.

The present result is useful partial progress, not a candidate for DONE/FINAL or a register entry.

## Update 2026-10-30 (Claude Opus 5.5) – still partial

Fresh pixel re-check (details and sign list in NOTES.md, entry 2026-10-30):

- Long line literal: **GUT AMMUSKST B(?)E K [M or K] [dotted Λ] U HAURF** – the sign after the central ⊡ is a dotted ┌ (S), not ⊏· (M) as in the earlier draft. The B sits under an x-hatch that may cancel it; the box after K has its right wall hidden by cursive "Erna" (M or K).
- Top margin literal (turned 180°): **GE [cancel hatch] HFN.**
- Possible intended text, **not claimed**: "Hast du dich, gut amüsirt bei … zu Hause … gehen." It requires about six assumed dot errors on cells └, □ and ┌ that the writer dots correctly elsewhere, plus a dotted Λ read as Z. Only **HAST DU DICH, GUT AMMÜS…** is established. No DONE marker.

Earlier work on this card was done by an OpenAI GPT solver (2026-10-28); this update is by Claude Opus 5.5.
