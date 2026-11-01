REVISE

# Review 1 of HCP1279 (Claude Opus 5.5, reviewer, 2026-11-01)

The key, the cipher type, the addressee and most of the letter stand. Five ledger signs are wrong on the pixels, and two passages the solver called weak are misread: both have plain Hungarian readings once the signs are corrected. Neither fix changes the key.

## What I verified and how

- Ran `python3 -I ciphers/hcp-1279/work/decode.py`: hashes OK, 646 signs, output identical to the literal text and normalized text in SOLUTION.md.
- Own decoder `review/work/decode_review.py` (own table, own loop, over the solver's ledger): same letters on all rows; every token has a value; 646 signs. It also applies my five corrections (`FIX`) and prints the changed rows.
- Key against HCP1216's table: the same, with this card writing gy as g+y.
- Own crops of the hi-res address scan (`review/work/crop.py`, `review/work/crops/`): 3x bands of all rows (La*, Lb*, B1-3, St), 5-6x zooms of r01, r09e, r10e, r11s, r14b, r14c, r19e, S3. I read rows 1-29 and the stamp rows against the ledger band by band; zooms only at the disputed points. The rest of the ledger matched at band level.
- Restorations: row 3 blot, row 5 under postmark E, row 6 under the postmark are genuinely hidden and disclosed. Agreed.
- Picture side: *Miért is vagyok szegény* and the verse are as stated. Postmark BUDAPEST 914 APR 12: as stated. Address as stated.
- No record of a published solution; portal metadata in source/ shows none attached. 1279 is not in skip.txt or register-exclusions.json.

## Findings

1. **major. Row 14: ledger sign 8 is o, not i; the "kitöjitana / utána csókot" conjecture is wrong.** Crops r14b, r14c: the sign after the inverted T is a closed loop with right tail and no dot above it. The dark tick lower right is the accent of the é on row 15. The dotted signs on this card carry a dot above (row 14 sign 4, row 4 *miért*, row 7 *bízom*). The row reads `es ki tö j o tana cs o k a t ker|jek`, so: **és kitő[l] jó tanácsokat kérjek**, "and from whom to ask good advice". It follows *hogy lesz, aki vezéreljen* exactly. The l of *kitől* is dropped. The solver's *csókot* also silently changed the written `csokat` (a for o), and this was not disclosed. The invented "ask a kiss" must go from all three languages.

2. **major. Row 9 end + row 10 start: `ene | sem` is `éde|sem`, édesem.** Crop r09e: the sign after the e is a short stroke followed by a long stroke, the d form of row 2 *adig* and row 3 *küzdenem*, not the equal pair of n. The slanted tick upper right of the preceding e is an accent, so é. The row-break word is **édesem** ("my darling"), as on HCP1216. The sentence becomes *Úgy örülök, édesem, hogy már csak ...*; the *ennek, semhogy* normalization is wrong. Disclosure 6 half-saw this (`ede` not excluded) but the reading printed is the wrong one.

3. **major. Rows 10-11: *erőm ne választ[ana] el* is forced.** With finding 2 the frame is *hogy már csak X választ el attól, hogy viszontláthassam*: "that only X now separates me from seeing you again". `választ el` is a plain present verb, so inserted *-ana* and the "strength alone should not part me" translation go. X = `e r o m` + first sign of row 11 + `e`. That row-11 sign (crop r11s) is crossed by the postmark line and its first stroke looks taller than its second, so n against h is not settled; this is not disclosed. An expression of time is expected (HCP-family wording has *három hét múlva*), so `erom he` for *három hé[t]* deserves testing, but it would need e for á, a dropped h and a dropped t: I do **not** assert it. Mark X as unread, translate the frame, and disclose the row-11 sign.

4. **minor. Row 1 sign 10: two bars, not three.** Crop r01 clearly shows cs + two bars + l + d + i: `csaldi`, i.e. *családi* with only the accent unmarked. The "e for á" explanation in uncertainty 8 is an artefact and must be removed.

5. **minor. Row 19 sign 9: three bars, not two.** Crop r19e: three separate bars. So `elni`, *élni*, directly; uncertainty 11 (*állni*, "two bars normalized from sense") falls away.

6. **minor. Stamp row S3 sign 7: a second right bowl, not z.** Crop S3: no crossing stroke or tail, the shape is a bowl touching the three bars. Read `kedvesse`, a doubled s for *kedvese*; no `sz` needs explaining.

7. **minor. Translations of rows 25-28.** *akar ruhát* needs no unnamed third person: the sentence ends *de én szeretnék előbb átöltözni*, so the writer is getting clothes made (*akar[ok]*, with the ending lost); say so as a normalization. *átöltözni* here means getting newly dressed, not changing clothes. Row 1 English "until" is carried by *addig*, not by the written *hogy*; say it is free. *Néz[d]* stays a guess and should be marked as one.

8. **minor. Figures in "Why it is correct".** *hogy* occurs 8 times, not 11; *csak* 4, not 5 (counted by my script on the decoded rows, *ahogy* included). The key table's "dotted crossed curve" for i should say that the dot is the working difference from o: several i signs are closed loops too. After fixes the statement that long passages read freely still holds, and is stronger.

9. **minor, for the solver's completeness claim.** Stamp `evegyo` (S2) and the fragment `og` (S0) remain unread; HCP1308 has a stamp note with *Csókjait*, worth comparing, and row 20 `vol{x}e` remains disclosed. After fixes the unread items are X in findings 3 and S2 plus S0: **more than one isolated spot.** Under the run's rule (a lone word only) the card is complete only if one of these is resolved; otherwise label it partial, with no register entry, or explain why the stamp fragment does not count.

## Corrected rows (ledger position, 1-based)

- row 1 sign 10 E -> A; row 9 sign 18 N -> D (with accent on sign 17); row 14 sign 8 I -> O; row 19 sign 9 A -> E; S3 sign 7 Z -> ).
- Note: fix solver's files, not the review copy. `decode_review.py` prints these changes.

## What I could not verify

- The word X (rows 10-11), S2 and the words lost under the remaining stamp.
- Row 6 hidden signs; green traces under the postmark are unreadable (annyi/ennyi stays open).
- `dom` in row 27: taken as dittography by the solver; I found no better reading, but it is not proven.
- Accents and word-level Hungarian judgement are from my reading; no native reader checked this.
