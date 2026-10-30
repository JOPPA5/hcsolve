# HCP 1797 (pc_hcp_478): a shift-by-one love postcard from Wimborne, 29 January 1908

Human solver: Tomáš Pavuk

**Status: PARTIAL. 38 of 38 enciphered letters outside one group are read; one three-sign group, the object of the only sentence, stays unresolved and is not interpreted. Three short initial groups are kept literal, as on the sister cards. Independent review 1 verdict REVISE; the findings are addressed and no decoded word changed.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1797 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1797), portal name pc_hcp_478, part of the HCPortal collection of cryptographic postcards. When it was captured on 2026-10-30 the portal listed it as **Not solved**, tagged Postcard, HCPortal collection, category Substitution, date 1908-01-29, language Unknown, location Europe, sender Unknown, recipient W. Abboú, with no transcription or solution attached.

The picture side is a printed Raphael Tuck & Sons "Oilette" card, *Lynmouth. Tower and Harbour*, with no handwriting. The address side, read with the card turned 90° anticlockwise, is addressed in plain writing to **Mr W. Abbott, Stokelake Farm, Chudleigh, S. Devon** (the portal's "W. Abboú" is a misreading of Abbott). The halfpenny stamp is cancelled **WIMBORNE / 10 PM / JA 29 / 08**. The message starts with the plain heading **"G. H. Wednesday"**; 29 January 1908 was a Wednesday, so heading, postmark and portal date agree.

The card has the same hand and formulas as the Abbott cards in this repository. The nearest in date are HCP 1402 (28 January) and HCP 1404 (30 January). No published solution of this card was found or used, and there was no earlier work on this number.

![Address side turned 90 degrees anticlockwise, the message at the left (work/reading.png)](../work/reading.png)

## Method

The transcription is manual, read from the un-converted original scan (work/hires/pc_hcp_478_adr.JPG) after rotation, with enlarged crops of each line. Letter shapes were compared with clear writing on the same card. The Caesar shift known from the sister cards was tested and gives English for every enciphered group with no adjustment. The script work/solve.py checks the image hashes, decodes the transcription and re-enciphers each decoded group as a round trip.

The first reading of the object group as another capital (giving HAM, MEAL, MAM or JAM) was dropped when a side-by-side comparison with the "W." of the address showed a W-shaped sign. "Morning" was first tried as enciphered `Npsojoh`; it has no p descender and no final h, so it stands in clear, like "Sat:" on HCP 1377.

## Key

Caesar: each plaintext letter is written as the next letter. Decrypt by subtracting one.

```
Cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

The heading and "Sat. Morning." are in clear. Initial groups are kept literal.

## Plaintext

| Written | Reading |
|---|---|
| G. H. Wednesday (clear) | G. H. Wednesday |
| Nz. Pxo E. L. Cpz. | MY. OWN [E. L.] BOY. |
| J. bn. Tfoejoh | I. AM. SENDING |
| **Wbm** Gps. | **[unresolved]** FOR. |
| Sat. Morning. (clear) | Sat. Morning. |
| Nz. Nu. & L. Gspn | MY. [Nu. & L.] FROM |
| Zpvs. Pxo. El. | YOUR. OWN. [El.] |
| Hjsm. | GIRL. |

English: *"G. H. Wednesday. My own E. L. boy, I am sending [Wbm] for Sat. morning. My [Nu. & L.] from your own [El.] girl."*

Slovak: *„G. H. Streda. Môj vlastný E. L. chlapec, posielam [Wbm] na sobotné ráno. Moje [Nu. & L.] od tvojho vlastného [El.] dievčaťa."*

## Uncertainties

- **`Wbm`, the main residual.** The first sign is built like the writer's clear W, and a pale bar runs over the group like the bar on the W of "Wednesday"; a reader could still take that bar as a T-cross, so W is the best reading, not a certainty. The second sign is b or d; `Wdm` gives VCL, no word, so b is preferred on sense only. The rest shows three legs and an exit stroke, so m is preferred over n, but this writer's minims vary and `Wbn` stays as the weaker alternative. Shifted, the group gives VAL (alternative VAM). VAL could be a name, but nothing on the card proves it, and the group might be a clear name or abbreviation instead. No value is substituted. HAM, MEAL, MAM and JAM each need a first sign that is not there. No sister SOLUTION.md has this group.
- **Initial groups.** `E. L.`, `Nu. & L.`, `El.` and the heading `G. H.` are not explained. `Nu.` is N with a small u-like sign on the baseline, where sisters have N. or M. `El.` could be `E. L.` with the dot lost. The heading initial is G or C.
- **"Sat. Morning." as clear.** `Tbu` would give the same word for Sat, so the meaning does not depend on this.
- **Small signs.** `bn` could look like `bu` (AT); AM is the only sense. The e of `Tfoejoh` is a small c-like sign, and the same word occurs on HCP 1392. The z of `Cpz` is a faint flat stroke; BOY is the only sense and matches the sisters.
- **Watermark.** The portal's grey disc overlies parts of lines 2–6; every sign was read through it.

![The unresolved group at high enlargement (review/work/wbn.png)](../review/work/wbn.png)

## Reproduction

From the repository root:

```
python3 -I ciphers/hcp-1797/work/solve.py
```

It prints the reading, 38 enciphered letters, the alternative for the unresolved group and the weekday check.

## Review and what changed

A separate Claude Opus 5.5 agent reviewed the solution with its own decoding script and its own reading of the scan, and confirmed all 38 letters against the pixels. Its verdict was REVISE. Changes:

- The last sign of the group was changed from n to m, so the group is `Wbm` (VAL if shifted), and the claim that the watermark hid the end of the group was withdrawn.
- The bar and spur evidence for W, and the unresolved b/d choice, were added.
- The wording on `Nu.` was corrected, the weak z of `Cpz` was disclosed, and a too-broad claim about the salutation of HCP 1407 was narrowed.
- The solution is labelled partial. Under the project rules a partial solution gets no entry for the AI Decipherment Register, so none is written.
