# HCP494 page4: qualified complete diplomatic working transcription

The whole brown body, dateline and subscription have been inspected. This supplies fuller clear context than Daniel's cipher-focused excerpt. **It does not establish a new cipher value or finish HCP494.**

Source: `source/full/0004.jpg`, 2600×3944, SHA256 `35809fa379c186409309a979e6040452816772587a47d84e9c6e1c8c46dc635b`. All431 earlier source hashes remain unchanged.

The initial30-line reading was frozen before reopening Daniel's `source/bourdeau/reading.txt`: `page4-diplomatic-2026-10-29/original-first-pass.md`, SHA256 `b993e9b7c02ee0a61585f0fe1ff77745f3c9cbbffcfc2aa07d27a8c7cc0d7fd7`. The current complete body is in **`page4-diplomatic-2026-10-29/working-body.txt`**, also structured line by line in **`page4-diplomatic-2026-10-29.json`**. That JSON preserves both passes and every later revision. Prior known glyph hypotheses mean this was not fully blind; importantly, later suggestions were not retroactively made into independent first-pass observations.

## What the original supports

The clear text explicitly references **Landtags Proposition zu Rendsburg**, **beylage Lit. A.**, and a disagreement over12 versus10. The unit sign and the word immediately beforeSchilling remain unclear. The clauses `protestando voneinander geschieden` and `es ad rigorem Executionis ankommen …` are substantially firmer. The transcribed details are suitable to compare against a separately found Landtag proposition; no fiscal unit was inferred just to match a known report.

The separate passage reads **“Was der Anhaltische / Secretarius Raumer an mich begehret gibt die beylage / Lit. B.”** It continues, with the address abbreviation unexpanded, **“Cantzlar schon wißen wie weit Ihme / hierinnen in seinem desiderio Zu fügen.”** Both the main reader and helper support this from brown ink. This identifies an enclosure request and its official context, not an attached cipher key. No given name is present.

The final political clause is transcribed with codes intact: `⟨427⟩ ⟨641⟩ war auch Zu Hamburg, und hat selbiger / eine estroite ⟨303⟩ Zwischen ⟨447⟩ ⟨602⟩ und ⟨834⟩ / unter handlung, und wird selbige ehistes tages Zum / stande kommen.` The adjective immediately before427 is still unresolved. The code pair447602 is not split into two named parties from black ink. The concluding formula addresses aCantzlar; the signature is a short monogram, not an independently spelled-out Lincker name.

The local dateline reads **Hamburg, den4.[small unresolved mark] May, a°1672**. A separate14 was not recovered securely from these pixels. This does not overturn a date derived elsewhere; the reading and a calendar conversion/other source must stay distinct.

## Comparison with Daniel and unresolved readings

| Place | Frozen original pass | After comparison |
|---|---|---|
| After576mit | Unclassified group | Daniel has768; brown is compatible. Working text uses768? and no meaning. |
| 625wird… | Tentativekürzlich/künftig | Independent helper readsvielleicht; Daniel hashierauff. Working text prefersvielleicht? but remains unsettled. |
| nachverflie-/ßung | Independently read from brown | Agrees with Daniel'sVerfliessung; not a new decipherment. |
| zu829… | gehen? | Helper proposesstoßen; leavegehen/stoßen? rather than force a verb. |
| mit einge-/… | hangen | Daniel haseingezogen; line-start letter group still retained ashangen/zogen?. |
| Beforebürgerundbauern | edell | Daniel hasAdell; original initial is compatible, retainedAdell/edell?. No punctuation is invented to decide between compound and enumeration. |
| Latin clause | `/: olim non erat ita :/ in[vi/si?]diosus hostis` | Daniel's excerpt has`si olim non erat …`; the visible first group is punctuation-like, not a securely readsi. The adjective remains uncertain. |
| Page3→4 join | Hagen? after parent'sbrown`ambassadeurs in die` | Helper's same-page brownBürger initial supports literal`Ba[h?]en`; medial tall stroke fits h better than a g descender. Working text uses that unresolved glyph draft. Hagen is not adopted, and no place or familiar idiom is inferred. |

The first cipher passage remains labelled by glyphs, includingBB/PP; the second retainsII/55, a loop-above-bar symbol, an8-like symbol and the final crossed pair. No black gloss supplies obscured strokes. The numeric working sequence contains16 code occurrences on this page, with38 small cipher signs; this is transcription bookkeeping, not successful decryption.

## Evidence and reproduction

Seventeen direct original-pixel crops are recorded in `page4-diplomatic-2026-10-29/crop-manifest.json`. The helper independently examined the ending and five unclear micro-passages; its notes, raw crops and uncertainties are under `page4-diplomatic-2026-10-29/helper-ending/`. No enhanced, erased or reconstructed image was used.

`page4_diplomatic_2026_10_29.py` reproduces main crops. `page4-diplomatic-2026-10-29/finalize_transcription.py` checks the frozen first-pass hash, all crop hashes and all431 earlier source hashes, then reproduces the final JSON and plain working-body text. It verifies provenance and assembly, **not** the correctness of a manual palaeographic reading.

Current solution, shared notes, decoders, source and state markers were not modified.
