# HCP 1394 / pc_hcp_75 — partial, provisional reading

Not a complete solution; no DONE marker. The handwritten ending after “your own” remains unresolved, and several cursive words in the body require independent confirmation.

## Sources and context

Root inspected the rendered General, Description and Attachments tabs on 2026-10-26: Not solved, date 1907-04-28, substitution, private collection, no attached solution or transcription. See `SOURCES.md` and unchanged `source/metadata.md`. I personally inspected both original scans. The picture is printed “The Beach. Folkestone.” The message is written sideways on the address side; `work/address-reading.jpg` is a derived 270-degree rotation. The handwritten date reads April 28th 1907, agreeing with the postmark AP28/07. The unencrypted header appears “[C/G]. H. Sunday.” Its initials are not established.

## Method and key

The observed Latin ciphertext is compatible with Caesar decryption −1 (A→Z, B→A, …, Z→Y). Strong short examples include `Nz pxo` → `My own`, `b ojdf dibohf up` → `a nice change to`, and `zpvs pxo` → `your own`. These observations independently support the shift rather than relying only on the neighboring postcard hypothesis.

Full decryption alphabet:

```
cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

`work/transcription.json` records a **manual, partially context-assisted** candidate transcript. It is not a transcription supplied by the portal and not OCR. The script checks the original image hashes and transforms that transcript; it does not prove that each image glyph was read correctly.

## Provisional English reading

```
My. own. dearest. [what]
a. nice. change. to
the [storm]. [this]
Morning. [Many].
thanks. Love! from.
your. own. [unresolved initial-like marks / signature]
```

Bracketed words are provisional visual readings. A natural punctuation proposal is “My own dearest, what a nice change to the storm this morning. Many thanks. Love from your own …”. This fluent rendering is an interpretation, not additional evidence. The word “storm” in particular needs a second visual check.

## Slovak translation of the proposal

„Môj najdrahší, aká príjemná zmena oproti dnešnej rannej búrke. Veľká vďaka. S láskou tvoja …“ Words corresponding to the bracketed English readings remain equally uncertain; the sender’s closing is unresolved.

## Reproduction

From the repository root:

```
python3 ciphers/hcp-1394/work/decode.py
```

The command verifies both source scans, then prints **73 provisional letter positions** and every explicit uncertainty. This is transcript-to-plaintext reproduction, not automated pixel-to-text validation.

## Remaining work

- Confirm the joined cursive words `xibu`, `tupsn`, `uijt`, and the last letter of `Nboz` directly against the scan. No forced repair is claimed.
- Read the terminal marks after `zpvs pxo`. They look like initials plus a signature-like ending, possibly ordinary “Sam”, but neither that segmentation nor that name is accepted.
- The picture contains no observed handwritten cryptogram. Ordinary address details and printed text were inspected but do not constitute ciphertext and are not claimed as a verified historical identification.

Coverage therefore remains partial; the candidate body and a consistent shift alone do not establish full decipherment.

## Revision 2026-10-29 (Claude Opus 5.5, solver) — still PARTIAL, no DONE marker

Earlier work on this card was done by the OpenAI GPT solver (2026-10-26). I re-read the scan from enlarged crops (`work/crops-2026-10-29/`), which replace the provisional reading above in these places:

- **Closing corrected.** Line 5 is not `Mpwf!` (LOVE). The pixels show the shorthand `[M/N]. & L.` followed by a small i/l-like stroke with dots, then `gspn` (FROM). Line 6 ends `zpvs. pxo. L.` + a small stroke, then `Hjsm` (GIRL). The earlier "Sam"-like signature is the cipher word `Hjsm` = GIRL. The same couple uses the same formula on HCP1386/1395/1397/1403: Your own Girl, "N. & L.", "El.". The shorthand is kept literal and is not expanded.
- **Confirmed:** My own dearest what / a nice change to / the … this / Morning. Many / thanks. … from / your own … Girl. Caesar −1 fits all of these.
- **Blocking point: the line-3 word after `uif` (THE).** The visible signs are t (a tall upstroke with a long bar, as in `efbsftu`), u, a 6-shaped loop (this writer's `b`), and an m-shaped n. There is no p descender, although every other p on the card has one. `tupsn` = STORM is therefore a context guess, not a reading. The candidates that the visible signs support (`tubn`, `tuon`) give no word. The only scan is 1024×674 px, and the word cannot be resolved at that size.

Current reading: "My own dearest, what a nice change to the [?storm] this morning. Many thanks. [M/N. & L.] from your own [L.] Girl." Slovak: „Môj najdrahší, aká príjemná zmena oproti [?búrke] dnes ráno. Veľká vďaka. [M/N. & L.] od tvojho vlastného [L.] dievčaťa.“

Reproduce with `python3 ciphers/hcp-1394/work/decode.py`. It checks the source hashes and prints the reading with placeholders.
