ACCEPT

# HCP 995 – Review round 1

Reviewer: Claude Opus 5.5 (claude-opus-5-5), 2026-10-28.
Object: `SOLUTION.md` / `work/decode.py` / `work/transcript.json` as of DONE1 (`2026-10-28T18:07:50Z OpenAI GPT-6 Codex`).

## Summary

The decipherment is correct. I read all 66 geometric glyphs from the scan independently and decoded them with my own script under the omitted-J Pigpen key. My reading agrees with the solver's in every position. The five embedded initials and the two bottom rows are covered completely. No Pigpen anywhere else on the card was left out. The findings below are minor and concern punctuation, postmark evidence and the presentation of context.

Confirmed reading of the cipher:

```
[embedded in the prose line "Darf ich bald mal wieder auf einen Brief von … hoffen."]
M. KL. S. M.

WIE GEFÄLLT DIR DIE KARTE? SIND
DIE BEIDEN NICHT ZU BENEIDEN? HERZL. GR. u KÜSSE.
```

The `u` is ordinary cursive and is not a cipher glyph. On punctuation after KARTE see finding 1, and on `u.` versus `u` see finding 3.

## What I verified and how

1. **Reproduction command.** I ran `python3 -I ciphers/hcp-995/work/decode.py` without `--write-transcript`, so nothing in `work/` was rewritten. Its output is `M KL S M` / `WIE GEFÄLLT DIR DIE KARTE SIND` / `DIE BEIDEN NICHT ZU BENEIDEN HERZL GR KÜSSE`. It reports 66 glyphs (5 + 25 + 36), and both scan hashes are verified. This matches the plaintext claimed in `SOLUTION.md`. I did not run `work/make-aids.py`, because it rewrites PNGs in `work/` and needs Pillow.
2. **Independent decoder.** `review/work/review_decode.py` does not import any solver code. It uses its own notation: grid cells 1–9 by position, `*` for a dot, `"` for umlaut strokes, `|` for the upright stroke, `chk` for the check-like V and `^` for the upward wedge. It builds the key A–I (undotted) and K–S (dotted) on the 3×3 grid, J omitted, plus T = `|`, U = check, W = `^`, Z = `^*`. `python3 -I ciphers/hcp-995/review/work/review_decode.py` gives the reading above, with **66 cipher glyphs** and 21 distinct signs.
3. **Key consistency.** It is one fixed key for all 66 positions. ┘/┘· = A/K, ⊔/⊔· = B/L, └/└· = C/M, ⊐/⊐· = D/N, □ = E, ⊏ = F, ┐ = G, ⊓/⊓· = H/R, ┌/┌· = I/S. This is the standard grid with a dot marking the second nine letters. It produces correct German in every word, including rare letters such as Z, W, K, Ä and Ü, so it is not fitted word by word. The plain and dotted wedge (W in WIE, Z in ZU and HERZL) and the plain and umlauted check (U in ZU, Ü in KÜSSE) are internally consistent.
4. **Sign-by-sign reading of the scan.** I made upscales of `source/picture.jpg` with ffmpeg (lanczos, 4–14×) into `review/work/` and read every glyph from them before comparing with `decode.py`:
   - initials: `r0.png`, `init.png`
   - row 1: `m1a–c.png`, `gefaellt.png`, `karte.png`, `karte_r.png`, `sind.png`, `sind_d.png`
   - row 2: `m2a–e.png`, `benei.png`, `herzl.png`, `kuesse.png`
   - question marks: `qmark1.png`, `qmark2.png`

   Points I checked specifically:
   - **Embedded initials** (`init.png`): └· . ┘· ⊔· . ┌· . └· . All five dots are clearly interior, giving M. KL. S. M. The ordinary cursive `von` before them and `hoffen.` after them are not cipher.
   - **GEFÄLLT**: ┘ with two short strokes above = Ä, then ⊔· ⊔· = LL, then the upright stroke = T.
   - **KARTE** (`karte.png`, `karte_r.png`): ┘· = K, ┘ = A (no dot), ⊓· = R, | = T, □ = E. The watermark lies over the R. The black ink shows ⊓ with a dot. The faint grey lower bar belongs to the watermark letter H and is not a fourth wall, so the sign is not □· = O.
   - **SIND, final glyph** (`sind_d.png`): it has a weak but present bottom bar, so ⊐ = D and not ┐ = G.
   - **BENEIDEN, 2nd glyph** (`benei.png`): a slanted □ = E, not ⊓.
   - **HERZL** (`herzl.png`): ⊓ = H, □ = E, ⊓· = R with a flat top, ^· = Z with a pointed apex, ⊔· = L. R and Z are clearly distinguished.
   - **KÜSSE** (`kuesse.png`): a cursive `u`, then ┘· = K, check with umlaut = Ü, ┌· ┌· = SS, □ = E.
5. **Search for untranscribed cipher.**
   - **Left margin** (`left_rot.png` / `left_rot2.png`): faint ordinary pencil cursive running up the margin. The words "Sonntag" and "angek…" are partly legible. There is no Pigpen there.
   - **First prose line** (`line1.png`): "S. M. Gr." is ordinary Latin cursive and not Pigpen.
   - **Final mark** (`monogram.png`): a cursive crossed capital with a full stop. It is not a grid or wedge sign. The solver rightly leaves it out of the cipher inventory and does not assert a name.
   - **Address side**: no cipher.
   - **Result**: I found no missed group.
6. **Context.**
   - **Address**: *Fräulein Mariechen Kühnast, Berlin S. 59, Kottbuser Damm 72.*
   - **Bonn postmark** (`bonn_stamp.png`): `BONN 10.2.00 9-10 V`.
   - **Berlin delivery stamp** (`berlin_stamp.png`): **`Bestellt vom Postamte 59 / 11/2.00 / 7¼-9½ V.`**, which agrees with the postal district S. 59 in the address.
   - 10 February 1900 was a Saturday.
   - The picture "Im stillen Winkel" shows a couple behind a screen, watched by onlookers. This fits *Wie gefällt dir die Karte? Sind die beiden nicht zu beneiden?* The register (affectionate closing, abbreviated "Herzl. Gr. u. Küsse") is ordinary German of 1900.
7. **Honesty and sources.** The portal status is Not solved and no solution is attached. The HCP 1016 key is disclosed as a method lead. The untranscribed pencil margin, the unexpanded initials and the monogram are all disclosed. I found no undisclosed use of a published solution.

## Findings

1. **minor – Punctuation after KARTE is a question mark, not a comma.** `SOLUTION.md` gives "KARTE, SIND" in the literal reading and in the German reading text, although the translation uses "?". On the scan (`qmark1.png`) the mark after KARTE is a raised hook with a short horizontal tail and a separate tick below. This is the same form as the mark after BENEIDEN (`qmark2.png`), which the solver itself reads as "?". The hook is merged with the dash separator in both places. The literal line should read `WIE - GEFÄLLT - DIR - DIE - KARTE? SIND`, and the German text *Wie gefällt dir die Karte? Sind die beiden nicht zu beneiden?*
2. **minor – The postmark day is resolvable, and the delivery stamp is not mentioned.**
   - `SOLUTION.md` and `NOTES.md` say the Bonn day digits are "10/16 visually possible" and not resolved. The address side carries a Berlin delivery stamp, `Bestellt vom Postamte 59, 11/2.00, 7¼-9½ V.`, which the solver does not mention.
   - A card delivered in Berlin on the morning of 11 February must have been posted on 10 February, not 16 February.
   - This independently confirms the portal date 1900-02-10. The report should cite both stamps and the full address, including the district S. 59 and *Kottbuser Damm 72*.
3. **minor – "u." has no full stop on the card.** The solver writes `GR - u. KÜSSE`. The only dot between the cursive `u` and Ü (`kuesse.png`) lies inside the corner of the following ┘. It is the interior dot that makes that sign K rather than A, and the solver's own key uses it that way. Counting it again as the full stop of "u." uses the same mark twice. The literal reading should be `u` (abbreviating *und*). The expansion is editorial.
4. **minor – Plausible expansion of the embedded initials not mentioned.** The initials stand in "auf einen Brief von **M. Kl. S. M.** hoffen", on a card addressed to *Mariechen*. This reads naturally as *von **m**einem **kl**einen **s**üßen **M**ariechen*: dative after *von*, with M. matching the recipient's name. Encrypting exactly this affectionate phrase is typical of these cards. The solver rightly does not put an expansion into the decoded text. It should, however, offer this one as the obvious editorial interpretation and label it unverified, instead of saying only "expansion unknown".
5. **minor – Abbreviation marks after HERZL and GR.** Each of `HERZL` and `GR` is followed by a dash separator. Whether the writer also put abbreviation stops after them cannot be told apart from the dash on the scan. The solver's editorial "Herzliche Grüße und Küsse" is fine, but the report should present it as an expansion of *Herzl. Gr. u. Küsse*.

## What I could not verify

- **The pencil margin.** I could not read the faint pencil cursive in the left margin with confidence. I agree with the solver that it is ordinary script and not cipher, but I cannot rule out that it contains information relevant to context, for example a postscript about "Sonntag".
- **The monogram.** The cursive monogram after KÜSSE could not be identified as specific initials.
- **The embedded initials.** Their expansion (finding 4) is a contextual inference and cannot be proven.
- **Novelty.** I did not repeat the portal, AI-register and Schrödel-paper checks. I relied on `SOURCES.md` and `source/metadata.md`.
