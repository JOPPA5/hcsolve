# HCP 1390 — Caesar −1 love card (pc_hcp_71)

**Status (current, 2026-10-29 after review 1): message body deciphered in full (56/56 letters); two short closing groups (a capital with raised small letter after “to day”, and the abbreviation before “Girl”) remain unread. Review 1 verdict ACCEPT.** The sections below the first heading are kept as a historical record of the earlier partial state (2026-10-26, OpenAI GPT solver); where they disagree with this line or with “Response to review 1”, the later text wins.

## Source and context

Postcard `pc_hcp_71`, portal status Not solved when root read General, Description and Attachments on 2026-10-26. No attached transcription or solution was displayed. The supplied originals were personally inspected. Printed picture caption: The Exchange, Liverpool. Address is to Mr W. Abbott, a farm in Chudleigh, S. Devon; the exact farm spelling is not securely transcribed here. The handwritten date is May 6th 1907. The heading appears to be C. H. Monday; its initials are not expanded. Portal metadata is preserved unchanged, including its different machine-rendered recipient spelling.

## Method and key

The message uses a Caesar substitution: subtract one position from each cipher letter, wrapping A to Z.

```text
Cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

Manual transcription is in `work/transcription.json`. It was made directly from the address-side original rotated 270 degrees, not taken from an attached transcription. Ordinary punctuation is not fully normalized or exhaustively transcribed. Word divisions follow the handwriting.

## Supported text

```text
My Own Dearest
Many thanks For
grand Letter
to day [unresolved initial-like group and two cross-like marks]
From your own
[unresolved abbreviation] Girl
```

Running reading, retaining unresolved material:

“My own dearest, many thanks for grand letter to day. [unresolved group] From your own [unresolved abbreviation] girl.”

Slovak translation:

„Môj najdrahší, veľmi ďakujem za skvelý list dnes. [nevyriešená skupina] Od tvojho vlastného [nevyriešená skratka] dievčaťa.“

## Reproduction and limits

From the repository root:

```bash
python3 ciphers/hcp-1390/work/decode.py
```

This verifies SHA-256 hashes of every original source, reads the separately recorded manual transcript, and decodes its **56 confirmed alphabetic positions**. It does not extract handwriting from pixels. Its output labels the omissions. The script also verifies that the inverse key re-encodes every confirmed position without exception. Coverage is limited to those confirmed positions; it is not a complete-message proof.

After “to day” a large M-like form and two cross-like marks remain uncertain; whether they represent an initial, encoded letter, or ordinary notation is not established. Before “Girl”, two marks resemble `Mu`, possibly `Mj`: conditionally these decode to `Lt` or `Li`. Although “little girl” is linguistically plausible, neither the exact abbreviation nor its expansion is established. [Superseded 2026-10-29: the body is complete; see Completion and Response to review 1.]

No published solution was consulted. Caesar −1 is independently supported by multiple complete words throughout the card, rather than inferred from one fluent fragment. Source provenance is in SOURCES.md.

## Completion and handover — Claude Opus 5.5 as solver, 2026-10-29

Status: **message complete; two initials reported literally. Handed to review
(DONE1).**

All six lines of the message decode under Caesar −1 (work/message-large.jpg):

> My own dearest, many thanks for grand letter to day. [M] ×× From your own
> [Mu.] Girl

- **The marks after “to day.”** are a cursive capital `M` followed by **two
  crosses ×× (kisses)**. Crosses are not letters and pass through
  unchanged. Whether the `M` was enciphered (→ L) or written plain (an
  initial M) cannot be decided from this card alone. Both are reported:
  *M* (plain) / *L* (Caesar −1).
- **Signature line** `Mu. Hjsm` → “[Mu.] Girl”. `Hjsm` = GIRL is certain.
  `Mu.` is an abbreviation, enciphered *Lt.* or plain *Mu.*, and remains a
  name abbreviation of unknown expansion.

Neither initial changes the content of the message. They are the only
residual points. Slovak: „Môj vlastný najdrahší, veľká vďaka za skvelý list
dnes. [M] ×× Od tvojho vlastného [Mu.] dievčaťa.“

## Response to review 1

Review 1 (Claude Opus 5.5, verdict ACCEPT) raised four minor findings. All are accepted.

1. **Stale status text — fixed.** The top of this file now carries one current status
   (body complete, two closing groups unread, review ACCEPT); the obsolete sentence
   forbidding DONE/FINAL is marked superseded. `work/decode.py` no longer prints
   “PARTIAL”.
2. **“Mu.” not supported by the pixels — agreed, withdrawn.** At 3x
   (`work/signature-3x.png`) the sign after the (apparently retraced) capital M is a
   small raised letter with a tall ascender and a closing stroke, followed by a dot; there
   is no u-shape. The `Mu`/`Mj` readings and the conditional `Lt`/`Li` (“little”) are
   withdrawn. The field is now described as “M + raised h/k/b-like letter, unread” in
   `work/transcription.json`, the decoder output and the report. Observation: the group
   after “to day” has the same build (a large capital, a small raised h-like letter, a
   dot; `work/line4-tail-3x.png`), so the two may be the same abbreviation, but neither is
   read.
3. **“××” may be cursive y y — agreed.** On `work/line4-tail-3x.png` each mark has a
   small hook at top-left and a long descending diagonal. Read as cipher `y y` they decode
   (−1) to `x x`; read as plain crosses they are `× ×`. Either way they are kisses; both
   possibilities are now stated.
4. **Command reproduces only the body — agreed, stated.** The command
   `python3 -I ciphers/hcp-1390/work/decode.py` reproduces the 56 letters of the body and
   prints the two closing groups as notes; this is now said in its output and in the
   report. Re-run on 2026-10-29: hashes verified, 56 confirmed positions, body identical.

Current reading: “My own dearest, many thanks for grand letter to day. [unread group]
xx (kisses). From your own [unread abbreviation] girl.” The deciphered body is unchanged.
