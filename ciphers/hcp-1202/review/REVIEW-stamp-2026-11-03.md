CORRECTIONS

# Review of the stamp-box message, hcp-1202 (2026-11-03)

Reviewer: Claude Opus 5.5, independent re-read. I changed none of the solver's files.

## What I checked and how

- Original: `work/hires/cpc_--_HU__HU_Rakos-Palota-Ujfalu_jolanka-58_adr.jpg` (3671x2445).
- My own crops are in `review/work/stamp-2026-11-03/`. I made them with `crop.py` (PIL python, `-I`). They include `box.png` (whole box), `row1.png` to `row11.png` (each row at 2.6x), detail crops at 4.5-9x (`r1L_g`, `r1R_g`, `r2R_g`, `r8L`, `r8R`, `r8R_g`, `r9M`, `r10L`, `r10R`, `r10R_g`, `r10tt`, `r10tt_bg`), green-channel versions (`_g`) and a blue-minus-green ink map (`_bg`).
- I read every sign against the Jolanka key: the hcp-1216 table plus the sign notes in NOTES.md. I made no reading of my own before I compared it with the claim.

## Steganography / type change

The change is justified. The stamp has been lifted. A perforation ghost runs along the left edge of the box, and torn fibres sit at the top right. Inside the dashed frame are 11 rows of violet cipher signs. They are in the same hand and key as the main text. There is no plain Hungarian in the box. The type `MASC + Steganography` fits. This card is PARTIAL and has no register entry, so the change affects only SOLUTION.md.

## Sign-by-sign result

These rows agree with the claim, with every sign visible: 3 `len kedvesem`, 4 `üdvözlöm` (both ö have two marks, ü is a dotted diagonal cross, z is the tailed diagonal cross), 5 `jolánka`, 6 `most csak ez`, 7 `van eszembe`, 9 `csókod után` and 11 `teneked`.

Row 1 `[i][s]ten vel e éde[s]`: confirmed. Before the gamma t there is only a faint curved bowl and abraded ink. At the row end there is only a faint blob. The restorations are disclosed and are the only letters that make the words.

Row 2 `fele jt he[t]et`: confirmed. The j+t ligature is clear. In the torn patch between `he` and `et` there is a smudge with traces, and no readable sign.

Row 8 `csókot adt[?á]l`: I accept the doubtful á. I see two faint bars, a short vertical mark above them, and a wave l running down to the right. See the minor finding on ó below.

## Differences (findings)

1. **Row 10, "hi[?tt]em": only one t is written (minor).** In `r10tt.png` and `r10tt_bg.png` the sequence after the dotted-curve i is: one clear gamma t, then a faint block of about three short horizontal bars, then three strokes m. The faint block is the e, smudged and crossed by the descender from row 11. There is no second gamma. The literal reading is therefore `hitem`, and *hittem* is a normalization. This matches the writer's habit of writing single consonants for double ones: *ithon* and *halottam* on this card, *mellet*, *akor* and *kel* on hcp-1216. SOLUTION.md should give the literal as `hit[?e]m` (the e is faint) and normalize it to *hittem*. It should not say that a doubled t is "crowded".
2. **Row 8, ó of "csókot" not visible (minor).** In `r8L.png` the second sign is a plain o (top bar, descender loop) with no accent mark. The accent is supplied in normalization. The literal row should show `csokot`, or the ó should be marked as supplied, as SOLUTION.md already does in other places.
3. **Row 9, fourth sign (o of "csókod") is atypical (minor).** In `r9M.png` the sign is hooked and has two legs. It does not have the usual long descender loop, and its lower left is smudged. *o* is the only value that makes a word, but the sign should be flagged `[?o]` rather than read as certain.

No difference changes the message: *Isten vele, édes felejthetetlen kedvesem! Üdvözlöm, Jolánka. Most csak ez van eszembe: csókot adtál, csókod után mindent hittem teneked.* I confirm this as the normalized text.

## Not verified

- Whether the last sentence quotes a song or poem. I did not search for a source.
- Faint traces under the four restored letters were not examined with any method beyond colour-channel separation.
