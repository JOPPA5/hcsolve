# Solved386 public-context source audit

This is public context, not an AI decipherment. No cipher directory or solved marker is created. The original attachments remain unchanged; their hashes are in cipher-reading-uncertainties.json. Metadata/source acquisition is maintained by the main solver.

## What was read

The ciphertext has eight rows of seven groups, **56 groups /280 letters**. Header `8280`, `SIDOR`, `Mračna` and record number80212 are recorded separately, not folded into the ciphertext. Header role is unknown;280 also happens to be the literal body length but no key interpretation follows.

`cipher-groups.txt` is a tentative pixel-led transcription. Watermark interference is material, especially rows5/6. `cipher-reading-uncertainties.json` retains13 groups with alternatives, including independent-reader disagreements. A favored readable line is not declared certified. In particular PEAND/PSDHD, ACEKR/SCEIR and OIIIY/OIRIV remain unresolved; alternatives were not selected by matching an expected plaintext or key.

The publicly attached plaintext draft is headed `Sidorovi` and annotated `1) telegram`. Its complete surviving/adopted body normalizes to **574–591 letters**, depending on declared correction variants. It therefore cannot simply be treated as the full plaintext of this280-letter ciphertext. The first section before `burzio` is348–355 letters; the tail starting `burzio` is226 or236 letters, depending on adoption of `zaviedol na`.

`published-plaintext-transcription.md` separates surviving typewritten text, unreadable overtype/strikeout layers, interlinear correction and uncertain pencil/editorial material. First-line six-letter `ZIVYEH`/`ZIVYCH` remains C/E ambiguous; no five-letter `ZIVEH` or spelling repair is silently adopted. The inserted `zaviedol na` is a disclosed correction. No missing pronoun is invented. Exact overtyped-X counts and struck underlying words cannot be recovered from these pixels, so they are not treated as normal prepared letters.

## Conservative inventory check

Sixteen transparent variants combine adoption of the interlinear correction, retention/omission of struck `presne`, retention/omission of an uncertainX after `zakazana`, and ZIVYEH/ZIVYCH. Normalization concatenates ASCII letters, retaining secure visibleX markers. There is no I/J merger, modern spelling repair, numeric conversion or guessed struck word.

For each variant, `inventory-audit.py` tests **every contiguous275- and280-letter window**, plus first/last windows with0–4 minimal endX padding. All56 possible five-letter group omissions are tested for275; the whole ciphertext is tested for280.

There are **zero exact inventory matches** against the tentative favored ciphertext. The best contiguous275 window, omitting group7 `STEEE`, has an inventory distance of **22 letter replacements**. It starts at normalized offset60 without PRESNE, or52 in a variant retaining PRESNE, and runs from `letcov...` to `...rodinamvychvaluju`. The omitted group and window are numerical minima, not inferred indicators or confirmed plaintext boundaries.

With the reference adopted/PRESNE/X-after-ZAKAZANA/ZIVYEH variant, first275 has best distance29, last275 distance39; first280 distance32 and last280 distance42. All-window results and inventories are preserved rather than corrected toward equality.

Loose per-letter bounds over all documented cipher-group alternatives still give a minimum **15 replacement gap** for every tested window/omission. These bounds ignore covariance within words and can permit impossible letter combinations; they are necessary bounds only. The result is conditional on the documented finite readings and normalization, not an exhaustive claim about every unreadable glyph or preparation.

The source material therefore does **not yet provide an exact known-plaintext/ciphertext pair** for a transposition key attack. Possible explanations include a different or partial transmitted draft, different preparation, unresolved transcription, or another cipher mechanism. Neither R nor shared daily keys are established or excluded. No key solver was run.

## Reproduce

From repo root:

```
python3 batches/solved-context-main/386/inventory-audit.py
```

Read normalized-plaintext-variants.json, inventory-all-omissions.json and inventory-summary.json for exact variants, window offsets, omission indices, count excesses and bounded uncertainty. Coordinates use zero-based normalized letters; displayed cipher group numbers are one-based. The report compares inventory only and does not infer letter order.
