# HCP 995 — German Pigpen message

**Complete reading of the 66 geometric cipher glyphs; solver candidate for root verification. No DONE or review claim is made by this collaborator.** The ordinary cursive pencil margin and final monogram are not fully transcribed; they are explicitly outside the cipher inventory, rather than represented as decoded text.

## Provenance and scope

The postcard is `cpc_1900-02-10_DE_Bonn_DE_Berlin_mariechen-01`, addressed to **Fräulein Mariechen Kühnast, Berlin**. The portal metadata gives 10 February 1900. The address side has a Bonn postmark, but its day digits are not independently resolved here (10/16 are visually possible); the metadata date is not claimed as a verified reading of that stamp. The picture shows a couple behind a screen and is captioned “Im stillen Winkel.”

Root inspected all three rendered portal tabs on 2026-10-28: **Not solved**, tagged **Pigpen**, no individual transcription or solution attached. Root also checked all 158 visible AI Decipherment Register contributions, finding no HCP 995 entry. This bounded check is not proof that the card was never deciphered elsewhere. Source URLs and metadata are in `SOURCES.md` and `source/metadata.md`. Both originals were visually inspected by this solver collaborator and remain unchanged.

The generic Schrödel collection paper is shared at `../hcp-1081/source/schrodel-2021.pdf`. Root inspected its illustrated addendum again and found no matching individual illustration or key for this card. No published plaintext was supplied to the decoding.

## Key

This uses the omitted-J German Pigpen grid convention already independently observed in the related HCP 1016 source. The convention was taken as a candidate key before reading this card; it was not fitted to a supplied plaintext. It transfers directly to all observed grid symbols.

Shape names specify the lines drawn. `SE` is ┘, `S` is ⊔, `SW` is └, `E` is ⊐, `O` is □, `W` is ⊏, `NE` is ┐, `N` is ⊓, and `NW` is ┌. A trailing period denotes an interior dot, distinct from punctuation after a word.

| Shape | SE | S | SW | E | O | W | NE | N | NW |
|---|---|---|---|---|---|---|---|---|---|
| Undotted | A | B | C | D | E | F | G | H | I/J |
| Dotted | K | L | M | N | O | P | Q | R | S |

Additional observed shapes are a straight upright `I` = T, a check-like V = U, an upward wedge ∧ = W, and a dotted upward wedge = Z. Two short strokes above the A-shaped symbol give **Ä**, and above the U-shaped symbol give **Ü**. They are umlauts, not additional encrypted letters.

The unused O/P/Q dotted cells in the conventional table are not attested assignments from this card. Every assignment needed for the actual 66 glyphs is listed by the decoder.

## Literal cipher reading

Five encrypted initials are embedded in the final line of the ordinary prose, between ordinary **von** and **hoffen**:

```text
M. KL. S. M.
```

The two geometric rows below read:

```text
WIE - GEFÄLLT - DIR - DIE - KARTE, SIND
DIE - BEIDEN - NICHT - ZU - BENEIDEN? HERZL - GR - u. KÜSSE.
```

**u.** is ordinary cursive on the source, between the final separator and the K-shaped glyph. It is not counted among the encrypted symbols. The five initials are preserved literally and not expanded into an assumed affectionate phrase.

Reading with word separators normalized and abbreviations expanded editorially:

> Wie gefällt dir die Karte, sind die beiden nicht zu beneiden? Herzliche Grüße und Küsse.

Translation:

> How do you like the card? Aren't the two to be envied? Warm greetings and kisses.

There are **66 encrypted positions: 5 initials + 25 on the first main row + 36 on the second**. No encrypted glyph remains unassigned. Punctuation, separators, umlaut strokes, the ordinary cursive `u.`, and the final ordinary monogram are separately classified rather than included as extra letters.

## Ordinary text and unresolved material

The clear ordinary prose asks why the recipient has been silent. A reading for context, with its unexpanded opening abbreviation, is:

> Seit dem letzten S. M. Gr. haben wir nichts mehr von einander gehört. Ich hoffe dies Deinerseits als ein Zeichen annehmen zu dürfen, daß es Dir recht gut geht. Dann nehme ich Dir auch Dein etwas rätselhaftes Schweigen nicht übel. Darf ich bald mal wieder auf einen Brief von **[M. KL. S. M.]** hoffen.

This cursive transcription supplies context; it is not output of the cipher substitution. The bracketed initials are the separately decoded geometric characters. The opening ordinary abbreviation is not expanded here. The word “dürfen” crosses an ordinary line break.

The last mark after KÜSSE is a connected, crossed monogram with a final dot. Its intertwined diagonal strokes differ from the separated simple geometric symbols. It may represent ordinary initials, but a name such as Theo is **not established**. The faint left margin, approximately x35–126/y17–475 in the source, contains ordinary connected cursive pencil writing, partial blots and erasure. It has not been reliably transcribed. No second sequence of Pigpen glyphs was identified there. See the rotated original-pixel reading aid `work/left-audit.png`; no words have been inferred from faint traces.

The address side contains ordinary address and postal markings, no identified cipher. These residual cursive uncertainties limit a claim of a complete transcription of every mark on the postcard, but not the stated 66-glyph decipherment.

## Reproduction and evidence

From repository root:

```sh
python3 ciphers/hcp-995/work/decode.py
```

The command decodes **a manual, coordinate-indexed transcription**, verifies the fixed SHA-256 hashes of both original scans, prints all three cipher regions and the position totals. It does **not** recognize symbols from pixels. `work/transcript.json` records every glyph's shape, reading, approximate original-image location and bounding box. The evidence still requires comparison with the scan.

`work/embedded-initials-indexed.png`, `work/main-1-indexed.png`, and `work/main-2-indexed.png` label the complete cipher inventory. Their source panels show the actual glyphs below the manual labels. `work/make-aids.py` regenerates reading aids with Pillow; source images are never modified.

The conventional grid transferred from HCP 1016 yielded the first row without changing assignments. The second-row sequence **DIE BEIDEN NICHT ZU BENEIDEN** was then checked separately under the same key, and the independently inspected closing **HERZL / GR / KÜSSE** and embedded initials followed that key. This is a sequential internal validation, not a pre-registered blind experiment or independent reviewer acceptance. The check-like U/Ü pair and plain/dotted wedge W/Z are shape controls within the target. All dots were checked on enlarged source panels; in particular the watermark-obscured K/A/R/T/E group still carries the required separate black strokes.

No watcher, reviewer, final PDF, register entry, or state marker was launched or created by this collaborator.


## Root verification before handover

Root personally inspected both original scans, all six enlarged main-row segments, embedded initials and final closing/monogram. The geometric inventory and omitted-J key agree with those source panels. Reran the documented command successfully: all 66 positions, fixed scan hashes and declared readings pass. Rechecked the nine-file source manifest for this new batch: originals unchanged. These solver checks do not constitute independent review. The incomplete ordinary pencil margin, unknown initial expansions and final cursive monogram remain disclosed. No watcher/reviewer launched under the user override. DONE1 is created next as the last cipher-directory mutation.

## Response to review 1

Reviewer: Claude Opus 5.5, verdict ACCEPT (review/REVIEW1.md, 2026-10-28). The reviewer read all 66 geometric glyphs from its own upscaled crops of source/picture.jpg before comparing, decoded them with an independently written script (review/work/review_decode.py), and found its reading identical to the solver's in every position: the five embedded initials M. KL. S. M. and the two bottom rows. It checked the contested signs (R in KARTE under the watermark, D at the end of SIND, E in BENEIDEN, R and Z in HERZL, K and Ü in KÜSSE) and found no Pigpen elsewhere on the card. The decoded letters are unchanged.

1. Punctuation after KARTE (minor). Accepted. The mark after KARTE is a raised hook with a tail and a separate tick below, the same form as the "?" after BENEIDEN; both hooks are merged with the dash separator. The literal line is therefore `WIE - GEFÄLLT - DIR - DIE - KARTE? SIND`, and the German reading "Wie gefällt dir die Karte? Sind die beiden nicht zu beneiden?". The comma in the literal reading and in the reading text above, and in the "Editorial punctuation" line printed by work/decode.py, is superseded. work/decode.py is left unchanged (its decoded letters are not affected), so the command still prints the comma; the report gives "?".
2. Postmark date and delivery stamp (minor). Accepted. The address side reads in full: "Fräulein Mariechen Kühnast, Berlin S. 59, Kottbuser Damm 72." The departure stamp reads BONN 10.2.00 9-10 V (morning), and the Berlin delivery stamp at the left, struck upside down, reads "Bestellt vom Postamte 59, 11/2.00, 7¼-9½ V." A card delivered in Berlin on the morning of 11 February was posted on 10 February, not 16 February. The earlier "10/16 visually possible" is superseded: the date 10 February 1900 (a Saturday) is confirmed by both stamps and agrees with the portal. Postamt 59 matches the district S. 59 in the address. These details are in the report; source/metadata.md is unchanged.
3. "u." has no full stop (minor). Accepted. The only dot between the cursive u and the Ü is the interior dot of the following ┘·, which makes that sign K; it cannot also be a full stop. The literal closing is `HERZL - GR - u KÜSSE.` ("u" for "und"; the expansion is editorial). The "u." in the literal reading above and in the decode.py message is superseded.
4. Expansion of the embedded initials (minor). Accepted as an editorial interpretation. The initials stand in "Darf ich bald mal wieder auf einen Brief von M. Kl. S. M. hoffen", on a card addressed to Mariechen. The natural expansion is "von **m**einem **kl**einen **s**üßen **M**ariechen" ("from my little sweet Mariechen"): dative after "von", the last M matching the recipient's name. It is unverified and is not put into the decoded text, which stays M. KL. S. M.
5. Abbreviation marks after HERZL and GR (minor). Accepted. Each of HERZL and GR is followed by a dash separator; whether the writer also put abbreviation stops there cannot be told on the scan. The report presents the closing as "Herzl. Gr. u. Küsse" with the stops editorial, expanded to "Herzliche Grüße und Küsse".

Additional notes from the closing pass: in the review the faint pencil margin on the left of the picture side yielded the partly legible words "Sonntag" and "angek…" (ordinary cursive, not cipher); it remains untranscribed. The opening abbreviation "S. M. Gr." in the first prose line is ordinary Latin cursive, not Pigpen, and remains unexpanded.

Remaining uncertainties carried into the report: the expansion of the embedded initials (and of "S. M. Gr."); the faint pencil margin; the final crossed monogram after KÜSSE, which is not identified (no sender name is asserted); the cursive prose is a contextual reading and not cipher output; the key was taken over from the related HCP 1016 card as a method lead, so there was no blind test; novelty rests on the bounded checks recorded in SOURCES.md, which the reviewer did not repeat.

Closing steps (this response, report, register entry, FINAL) prepared by Claude Opus 5.5 on the solver's behalf at the human's request, 2026-10-28.
