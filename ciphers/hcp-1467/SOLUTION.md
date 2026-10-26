# HCP1467 / pc_hcp_148 — full alphabetic-message candidate

Fresh Not solved on 2026-10-26. All 62 Pigpen letter positions currently read
under one standard interleaved key. External punctuation cluster preserved
separately. Review 1 required one letter correction, now addressed below.

## Literal reading

Dots between written words retained; spaces editorial:

```text
HOPE. TO.
SEE. YOU. WITH.
LUCK. SOON. LOOK.
OUT. FOR. THREE.
COUNTRY. YOKELS.
LOVE.
BOO [EXTERNAL DOT CLUSTER] BOO.
```

Editorial sentence interpretation: “Hope to see you with luck soon. Look out
for three country yokels. Love, Boo Boo.” The third glyph of LOVE is dotted
>1, which gives V. Review 1 identified the internal dot missed in round 1.

Slovak interpretation: „Pri troche šťastia ťa čoskoro uvidíme. Dávaj pozor
na troch vidieckych truhlíkov. S láskou, Boo Boo.“ English does not explicitly
state singular/plural subject of HOPE; translation uses plural contextually.
No identities for Boo Boo or the three people established; no claim whether
YOKELS is self-mockery or a description of others.

## Key

Standard interleaved Pigpen, undotted/dotted pairs:
BR A/B; B C/D; BL E/F; R G/H; C I/J; L K/L; TR M/N; T O/P; TL Q/R;
V S/T; > U/V; < W/X; ^ Y/Z.

Labels name strokes present: BR=bottom/right, B=bottom/left/right,
BL=bottom/left, R=top/bottom/right, C=all four sides, L=top/bottom/left,
TR=top/right, T=top/left/right, TL=top/left. 0 = no internal dot, 1 = dot.
V,>,<,^ are literal wedge orientations. Orientation is relative to
work/reading.jpg, original rotated 45 degrees clockwise.

## Reproduce

From repository root:
`python3 ciphers/hcp-1467/work/decode.py`

No attached transcription. work/transcription.txt is own manual reading of
source/address-large.jpg. Script verifies source image/metadata hashes,
decodes every one of 62 letter glyphs and checks exact inverse-key roundtrips.
It emits a label for the external dot cluster, not an invented letter.
These mapping checks are not OCR or independent source-pixel validation.
Working enlargements supplied; originals unchanged.

## Points requiring independent review

- LOVE uses dotted V (>1). The internal dot is visible in review/work/love-rot.png
  and differs from the undotted U wedges in LUCK, OUT and COUNTRY.
- Signature begins bottom/right dotted B, not three-sided H. Second BOO repeats
  these shapes. The third glyph of first BOO is undotted top/left/right O;
  several dots sit outside its outline. They are preserved as DOT_CLUSTER,
  not merged into a dotted P. Their exact punctuation/function is unassigned.
  See work/signature-large.jpg and original scan. Current scope is all
  alphabetic Pigpen glyphs, not a semantic interpretation of every mark.
- The first O of LOOK has a smudge outside its lower-right foot, between
  glyphs; it is not an internal dot and does not change O to P.
- Word-separating dots are retained in literal text. Sentence punctuation
  and spacing are editorial, without changing letter order.

The entire letter is coherent with a proposed visit; all main-body tokens
decode consistently. This supports the mapping but cannot independently
validate manual glyph transcription. Ordinary address, postmark, printer
text, crossed-out RAPID stamp and ornamental underline excluded from count.
Picture caption Miss Hope is printed matter, not a decoded personal name.

All three rendered tabs inspected; no attached/published solution used. Register
snapshot of 110 entries has no exact source 1467/name pc_hcp_148 match, no priority
claim. The review correction is implemented; final report and local register preparation are documented below.

## Response to review 1

1. **LOVE correction (major transcription, minor meaning).** Accepted after
   inspecting source/address-large.jpg and review/work/love-rot.png. Corrected
   glyph 55 from >0 to >1 in work/transcription.txt; regenerated decoder output
   and plaintext-check.txt. Literal output is LOVE; removed the erroneous
   LOUE-as-written argument. The fixed alphabet and other 61 letters do not
   change. The reviewer explicitly required no second round for this fix.
2. **Signature dot cluster (minor).** Retained as an external, unassigned
   cluster. review/work/sig-rot.png shows it beyond the third glyph's frame;
   BOO remains BOO rather than BOP. No punctuation function is invented.
3. **LOOK smudge (minor).** Added the scan note above. The blob in
   review/work/look2.png is outside the first O; no alphabet change.
4. **Text quality (minor).** Rewrote the running notes and fixed missing spaces
   in this solution and the report source. No identities, town or historical
   event were inferred from the letter.

Validation: the solver decoder and the reviewer's independent decoder now
produce LOVE and agree on all 62 glyphs. Source/review files remain unchanged.


## Finalization - 2026-10-26

The coordinating solver verified the item-by-item review response, reran the
corrected decoder with original-source hash checks, and produced the report
PDF. All rendered pages were visually inspected after final typography
corrections. The review explicitly permits closure after the specified local
corrections without another round. Remaining reading uncertainties are
preserved; no new independent ACCEPT verdict is claimed.

The local register-entry.txt is prepared with solver TODO because no solver
name was supplied for the entry. Nothing was submitted externally. Original
source files and review files were left unchanged. FINAL records closure
after these review conditions and report checks.
