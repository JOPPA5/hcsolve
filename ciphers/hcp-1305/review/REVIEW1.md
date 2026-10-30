REVISE

# Review 1 of HCP1305 (reviewer: Claude Opus 5.5, 2026-10-30)

The key, cipher type and overall reading stand: this is the Jolánka family key, and the text is real Hungarian of the period. Two concrete corrections are needed. Both replace a shaky reading with a better one, and neither needs a new round of review if made as below.

## What I verified and how

- **Solver's command.** `python3 -I ciphers/hcp-1305/work/decode.py` ran. All four SHA-256 checks print OK. Its output matches the claimed literal table, apart from the hyphen in finding 6.
- **Independent decoder.** `review/work/my_reading.txt` is my own sign-by-sign transcription, made from my own crops (`review/work/crop*.py`, `review/work/crops/`). `review/work/my_decode.py` decodes it with `ciphers/hcp-1216/work/graphic-key.json`, not with the solver's script, and diffs it against the solver's output. Result: 345 signs, 26 rows, **1 difference** (finding 1). The two signs the solver leaves open are excluded from that count: `{a|e}` in rows 7 and 20 are `?` in my reading.
- **Transcription against the scan.** I read every row and the stamp block on crops from the hires address scan, enlarged to about 1800 px per half row. This covers all the items the solver flags: rows 1, 5, 7, 11, 12, 13, 14, 15, 18, 19, 20 and the stamp block.
- **Key coverage.** Every sign has a value in the family key; nothing is left over. No value on this card is new to the family.
- **h/p.** The h of *hogy* and the signs in row 5 and row 13 are the same form (tall stroke, then a short one to its right). The d form is the reverse (short, then tall), so `d` in row 14 and in *tudatom* is sound. Nothing on this card distinguishes h from p, though `graphic-key.json` keeps separate h and p classes.
- **Row 14 `migy`.** The sign is the dotted crossed curve, and its dot is visible. *megy* is excluded by the shape as well as the dot, since e is bars. The solver's *mi így* stands as the literal reading.
- **Row 18 `hatok`.** There is a struck-over sign with two heavy bars after h. a is a fair reading and it is disclosed.
- **Stamp block.** *üdvöz / lome / tavol / bol / hüked / vesefery* reads as claimed. The smear over the second row is disclosed.
- **Language and context.** The formulas match HCP1216, 1217 and 1218. "Kath. Leg." is visibly in plain script and joins the cipher *egy-leti*. *Koth* is what the pen wrote; the solver discloses that and normalizes to *Kath.*
- **Picture side.** The only marks are pink ink splashes at the upper left (`review/work/crops/z_pic_mark.png`). They are not text.
- **Sources.** SOLUTION.md credits and sources are consistent with SOURCES.md and metadata.md. Nothing in the directory suggests an undisclosed published solution.

## Findings

1. **major: row 17, first sign is j, not f; read *éjjel*, not *éjfél*.** The ledger has `F E L V O L T`. The sign is an inverted T with its bar at the foot and no stem below it, not an upright cross. `review/work/crops/z_jf_compare.png` puts it beside the j of rows 8, 13 and 3 and the f of rows 7 and 16: it matches the j signs and not the f signs. Row 16 ends `éj` and row 17 begins `jel`, giving *éjjel* ("at night"): **Hétfőn éjjel volt egy kis tüzünk is** = "On Monday night we also had a small fire." This removes the smoothing in uncertainty 11 (no *-kor* is needed, and the missing acute on `fel` goes too) and it is a natural sentence. Fix `work/ledger.txt` row 17, the literal table, `work/normalized.txt`, the English and Slovak, uncertainty 11 and the NOTES log.

2. **major: row 5 `harasztin` should stay h and be read as the place name *Harasztin*, "at Haraszti".** The solver changes h to p to get *parasztin*, a form it admits is odd, and renders it "among the peasants". The sign is the same one as in *hogy*, so no change of letter is needed. Haraszti is a Hungarian place name (for example Dunaharaszti in Pest county), and *-n* is the regular locative for it, so **Hogy mulat Harasztin?** = "How are you enjoying yourself at Haraszti?" reads without emendation. An emendation is not justified when the literal text is a real name. Which Haraszti is meant cannot be shown from the card, and the card is addressed to Jászárokszállás, so say that the identification is by word sense. Update the normalized text, both translations and uncertainty 2. Row 13 *Pest* still needs p and stays as it is, because *hest* is no word. HCP1305 is the only Jolánka card whose SOLUTION.md contains this name (a grep of the family files).

3. **minor: the translations overstate `tustkantek`.** The signs are as claimed: t u s t k a n t e k. The third bar of the e is detached and there are no dots on the u. "Unread" is right. But the English says 'probably "have gone up in smoke"' and the Slovak says *asi*, while uncertainty 1 calls this a guess at the sense only. Other senses fit equally well: *tönkrementek* ("were ruined") shares the opening t and the ending *-ntek*. I am not proposing that reading, because too many signs differ. Write "sense unknown; perhaps something like 'came to nothing'" and drop "probably".

4. **minor: the corner (rows 18/20) can be separated further than uncertainty 8 says.** On `review/work/crops/z_corner.png`, the thick stroke with the thin horizontal arm running right from its top forms a normal gamma, so the t of *mint* is visible and does not come only from context. The strokes left over for the edge row are the long thin line and the two short ones: three bars, so the vowel of *l_tásra* is more likely literally e (a slip for á) than a. This is my reading of a tangle, not a certainty. Keep `{a|e}` if you disagree, but `{t?}` can lose its query, or the text should at least say the stem and arm are seen.

5. **minor: row 1 `( )`.** Uncertainty 6 treats this as left bowl plus right bowl. HCP1216 lists "opposed bowls" as the sign for **cs**, so the pair may be that digraph sign written by mistake or as a false start. Mention it. The normalization *Szeretet[t]* is unaffected.

6. **minor: hyphens.** The card has a hyphen after `egy` in row 9 and after `re` in row 14. The literal table shows `re-`, but the command prints `remigydazénre`, so table and output differ by that mark, and row 9's hyphen is shown in neither. Record both in the ledger or say that hyphens are omitted.

7. **minor: status line and supporting claims need refreshing after the fixes.** The header's "two others rest on a guess" no longer matches once *parasztin* goes.

## What I could not verify

- **The date.** The enlarged postmark (`review/work/crops/z_pm_rot.png`) shows blurred figures that I cannot read as a date. I can neither confirm nor refute 1912, which comes only from the file name. The solver's statement that the date is not established is right.
- **Which Haraszti is meant**, and whether Jolánka's trip to Pest is the same as anything in the sister cards.
- **The meaning of `tustkantek`,** the bare `le` in row 12 and the bare `d` in row 14. All three are disclosed as unresolved, and the signs are as transcribed.
- **External search.** I ran no web search for a published solution and did not re-open the portal. I relied on SOURCES.md and the orchestrator's register check.

## Outcome for the solver

Make the fixes for findings 1 and 2 and answer the rest in `## Response to review 1`. No other sign differs from my independent reading, so these changes do not need a second review round.
