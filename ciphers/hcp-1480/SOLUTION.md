# HCP1480 / pc_hcp_161 — solution (round 1)

Portal status: Not solved (all three tabs read 2026-10-26). No supplied
transcription or solution; no published decipherment found or used.
Postcard: picture "Depot Gateway, Dorchester"; address Mrs Light, Police
Station, Swanage, Dorset, "Local"; Swanage postmark 4.30 PM, 17 JY 10
(portal date 1910-07-17). Pencil notes "CODED MESSAGE TO POLICE STATION",
"13.50", "AR38" are later dealer/collector annotations, not ciphertext.
The picture side carries no cipher writing.

## Credits

Transcription, shape labels, most of the key and the reading
"Dearest Id / just a card with love and kisses ever ...urs ... dearest Idie /
Will" were established on 2026-10-26 by an OpenAI GPT solver (GPT-6 Astra /
GPT-6.1 Sol), with four positions left open. On 2026-10-29 Claude Opus 5.5
re-checked all signs on enlarged crops and resolved the four open positions
(see below). GPT's previous files are kept as
`work/transcription-gpt-2026-10-26.txt` and `work/key-gpt-2026-10-26.json`.

## Cipher type and key

Monoalphabetic substitution with an ad-hoc set of geometric symbols
(not Pigpen, not a known published alphabet), word spaces kept. Key
(shape label -> letter; labels described in `work/transcription-legend.md`):

| Sign | Letter | | Sign | Letter |
|---|---|---|---|---|
| ○ open circle (CIRCLE) | A | | ⊠ box with cross (BOX_CROSS) | K |
| _ low stroke with left upturn (UNDER) | C | | — horizontal bar (BAR, SLANT_BAR) | L |
| △ upright triangle (TRI) | D | | ⊤ bar with stem (T_STEM) | M |
| □ square (BOX, BOX_BAR) | E | | curl like cursive 2 (CURL_N) | N |
| ▷ right-pointing triangle (RIGHT_TRI) | H | | ⊂ / < pointed C (C_SHAPE, DOTTED_C) | O |
| × (CROSS) | I | | ÷ (DIV, CURVED_BAR_TWO_DOTS) | R |
| ⊕ (CROSS_CIRCLE) | J | | ▽ with central stroke (DOWN) | S |
| ▯ tall narrow rectangle (RECT) | T | | Ꮭ stem between curved strokes (CUP) | U |
| ∧ (CARET) | V | | ∿ wave (WAVE) | W |
| ◠ round arch with base, right leg ticked (ARCH) | Y | | | |

Files: `work/transcription.txt` (61 signs, own manual reading of
`source/address-large.jpg`, word spaces `/`, line breaks as on card),
`work/key.json`.

## Plaintext (English, original language)

```
DEAREST ID
JUST A CARD
WITH LOVE AND
KISSES EVER
YOURS MY DEAREST
IDIE
WILL
```

Normalised: "Dearest Id, just a card with love and kisses. Ever yours,
my dearest Idie — Will."

Slovak: „Najdrahšia Id, len pohľadnica s láskou a bozkami. Navždy tvoj,
moja najdrahšia Idie — Will.“

("Id"/"Idie" are kept exactly as enciphered; presumably a pet name, e.g.
for Ida/Edith, but the identity is not established. Nothing links "Will"
to a known person. The recipient on the address is Mrs Light.)

## Reproduce (from repo root)

```
python3 -I ciphers/hcp-1480/work/decode.py
```

Verifies SHA-256 of all three files in `source/`, asserts every sign is
mapped, prints the plaintext above and "61 signs, all mapped".

## What changed in round 1 (Claude, 2026-10-29) and remaining uncertainty

1. **HOOK -> ARCH = Y (pixel match).** The 2nd sign of the 2-sign group in
   line 5 is the same sign as the first sign of "YOURS": a rounded arch on a
   flat base whose right leg ends in a dark tick. Its upper arc is in faded
   (dry-pen) ink, so only the dark base/tick stood out and it was earlier
   labelled HOOK. Side-by-side at 9x: `work/arch-vs-hook-claude.png`.
   ARCH therefore occurs twice. Its value Y comes from context: `?OURS`
   after "kisses ever" leaves YOURS; no other assigned letter uses this sign.
2. **DOTTED_C = O.** Same pointed-C shape with a long flat lower stroke as
   the O of LOVE, plus one small dot above (`work/yours-line5-claude.png`).
   Treated as O with a stray/decorative dot. Disclosed variant.
3. **BAR_LOWER_MARK -> T_STEM = M.** The "lower mark" is a faded vertical
   stem with a small foot under the bar, i.e. a T-shaped sign whose stem is
   in the same faded ink as the arch next to it (`work/my-group-claude.png`).
   It is not BAR=L (no stem there). Singleton; value M from context
   (`?Y` before "dearest" -> MY).
4. Context-only singletons (each appears once, value fixed by the word):
   C (CARD), H (WITH), J (JUST), K (KISSES), M (MY), N (AND); Y occurs
   twice but its value also comes from context. This is normal for a 61-sign text but
   means these letters rest on the readings of their words, not on repeats.
5. Handwriting variants merged: BOX/BOX_BAR = E, BAR/SLANT_BAR = L,
   DIV/CURVED_BAR_TWO_DOTS = R, C_SHAPE/DOTTED_C = O.
6. The UNDER sign (C) lies on the grey watermark letter "E"; only its dark
   stroke is used.
7. Reading order of line 5 into "ever yours, my dearest Idie" follows the
   physical layout (left to right, then line 6).

## Why it is believed correct

All 61 signs are mapped with one consistent key: 23 shape labels collapse
(via the 4 disclosed variant merges) to 19 letters, each sign always the same
letter. Repeated signs agree everywhere (E x9, S x7, D x6, I x6, A x5, R x5,
T x4, L x3, O/U/V/W/Y x2). The text is a fluent,
period-typical English love-postcard formula ("just a card with love and
kisses, ever yours"), with the address salutation "Dearest Id" repeated as
"my dearest Idie" — internal consistency, not forced vocabulary. No
published solution exists on the portal.

## Response to review 1

Review 1 (Claude Opus 5.5, separate agent, 2026-10-30): verdict **ACCEPT**, four minor findings.
No letter of the reading changed.

1. **Context-only singletons (minor).** Agreed; this was already disclosed above (item 4) and
   is repeated in the report's uncertainties. No change to the key.
2. **Stale legend (minor).** Fixed: `work/transcription-legend.md` now opens with a
   "CURRENT LABEL SET" block listing the 23 labels actually used in `work/transcription.txt`
   with their letters, and states that HOOK, CURVED_DIV and BAR_LOWER_MARK are superseded and
   their older descriptions below are history only. The 23 labels listed match exactly the
   label set in the transcription (checked with `grep -o "[A-Z_]\+" work/transcription.txt | sort -u`).
3. **Language / sender (minor).** Accepted: the report states that the established language is
   English (the portal says "Unknown") and that the signature reads "Will" while the sender's
   identity remains unknown; the portal's sender field "Unknown" is left as the portal has it.
4. **Type (minor).** Agreed: type MASC (ad-hoc geometric symbol alphabet, not Pigpen); the
   register entry uses MASC.

Re-run after the fix (from repo root): `python3 -I ciphers/hcp-1480/work/decode.py` prints the
same seven lines (DEAREST ID … WILL) and "-- 61 signs, all mapped; source hashes OK".
