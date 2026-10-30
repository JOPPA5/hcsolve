# HC Portal 1495 (pc_hcp_176) — solution

Postcard (Rotophot), postmarked [..]IDGE, 21 Mar 1906, to Miss L. Cory,
Bankside Villa, Gravesend, Kent (portal catalogue: "L.Gory"). Portal status
on 2026-10-26: Not solved; no attached transcription or solution. No
published solution of this card was found or used.

## Cipher type and key
Caesar shift (MASC), encryption +1, decryption −1, case and word division
kept: cipher letter = next letter of the alphabet (a→b … z→a).

    plain : ABCDEFGHIJKLMNOPQRSTUVWXYZ
    cipher: BCDEFGHIJKLMNOPQRSTUVWXYZA

## Transcription (own reading of source/address-large.jpg; no transcription attached)
    Ebsmjoh. Mflz
    Uipvhiu zpv xpvme
    mjlf uijt pof zpvs
    dpmmfdujpo, efbs
    Xpvst                (pale, below the message)
60 enciphered letters. Below them a large unenciphered-looking monogram
flourish (not read).

## Plaintext (English, literal output of the −1 shift)
    Darling. Leky
    Thought you would
    like this one your
    collection, dear
    Wours                → most likely intended "Yours" (see uncertainties)

English (normalised): "Darling Leky, thought you would like this one [for]
your collection, dear. [Yours?], [monogram]" (literal "Wours"; if the last
pale sign is k, "Wourj")

Slovak: „Drahá Leky, myslel(a) som, že by sa ti táto (pohľadnica) páčila do
tvojej zbierky, drahá. [Tvoj(a)?], [monogram]" (only if "Wours" = "Yours")

The card's picture side (Lily Brayton & Oscar Asche) carries no cipher.

## Command (run from repo root)
    python3 ciphers/hcp-1495/work/decode.py

It checks SHA-256 of all files in source/, applies the −1 shift to
work/transcription.txt, asserts the exact re-encryption, and prints the
plaintext. `--all-shifts` prints all 26 shifts; only −1 gives English.

## Uncertainties
1. Greeting name: the pixels read **Mflz** → "Leky". The second sign rises
   above x-height and descends (= this writer's f, cf. "mjlf", "pof"); the
   third is a single tall loop like the l of "mjlf", not the humps of an m.
   The earlier reading "Mfmz" → "Lely" is therefore not kept. "Leky" is
   reported literally as a nickname; its initial L agrees with "Miss L. Cory",
   but the name itself is not established (a slip for another name cannot be
   excluded).
2. Closing word "Xpvst" is pale (pencil or faded ink) and overlapped by the
   portal's watermark. Signs read as X, p, v, s, t (last sign could also be
   k: "Xpvsk"). Literal −1 output is "Wours"; the position after the message
   and before the monogram, and "pvst" = "ours", make "Yours" the probable
   intent, i.e. the writer apparently shifted Y the wrong way (Y→X instead of
   Y→Z). This is an interpretation, disclosed as such; the key is not changed
   for it. That this word was written by the same hand at the same time is
   likely (same letter forms, same Caesar cipher) but not proven.
3. The monogram flourish below (looks like J/F/P/H ligature) is not read and
   no sender is identified.
4. Pencil "CODED MESSAGE / 8.50 AR576" at the bottom is a later dealer /
   collector note, not part of the correspondence.
5. Missing "for" before "your collection" is the writer's; comma after
   "dpmmfdujpo" is on the card.

## Why it is believed correct
All 60 enciphered letters decode under one fixed shift; the four-line
message is continuous, grammatical English with no leftover letters; the
content (a picture postcard of a stage couple "for your collection") fits a
1906 postcard sent to a young woman collector; all other 25 shifts give noise.

## Credit
Card capture, the identification of the −1 Caesar shift and the first
reading of the four message lines were done by the earlier OpenAI GPT solver
(2026-10-26). On 2026-10-29 Claude Opus 5.5 re-checked every sign on
enlarged crops, corrected the greeting name (Mfmz→Mflz), added the comma and
the closing word "Xpvst", and completed this solution.

## Response to review 1

Verdict ACCEPT, four minor findings; all addressed, decoded letters unchanged.

1. **Normalised "Yours" unmarked.** Fixed: the normalised English now reads
   "[Yours?]" with the literal "Wours" and the k-alternative "Wourj" stated;
   the Slovak "[Tvoj(a)?]" is marked as conditional. The report does the same.
2. **Dot after the first word.** Agreed; on the 5x crop (review/work/greet.png)
   a clear dot stands between "Ebsmjoh" and "Mflz". Fixed:
   work/transcription.txt line 1 is now "Ebsmjoh. Mflz", work/plaintext.txt
   "Darling. Leky". `python3 -I ciphers/hcp-1495/work/decode.py` re-run:
   hashes and round-trip pass, still 60 enciphered letters, first five
   output lines identical to work/plaintext.txt.
3. **Attribution of "Xpvst".** Agreed; kept as "likely, not proven" here and in
   the report, with the reviewer's point that the wrong-way shift (Y→X) could
   also indicate a later hand.
4. **Stale "55 letters" in NOTES.md.** NOTES.md is a log and stays as written
   (the 2026-10-29 block supersedes it); SOLUTION.md and the report quote only
   the current count, 60 letters.
