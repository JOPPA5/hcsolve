# HCP 1492: a numeric greeting from Flossie

## Origin and scope

HC Portal catalogues this postcard as pc_hcp_173 (portal 1492), dated 11 June 1911, Europe, private collection, sender Flossie and recipient J. Stalland. General, Description and Attachments were read in the rendered portal on 26 October 2026. The portal then showed Not solved and supplied no transcription or solution. Both original scans and captured metadata remain preserved in source/.

The address side combines an ordinary cursive note with four numeric lines and a separate three-number group in the same pencil. The encrypted portion contains **40 values**. The written dateline appears 10 June 1911, while the postmark/catalogue indicate 11 June; these are distinct observations. The picture side is a landscape with no observed encrypted continuation. Ordinary cursive, address, postal numerals and dealer-like notes are outside the cipher count.

## Cipher and full numeric transcription

The key is direct A1Z26: 1=A, 2=B, …, 26=Z. No shift, keyword or special value is needed. Dots divide numeric letters; larger gaps divide words. The following diplomatic record retains the original dash and question mark, and the separate group below the printed heading.

```text
4.5.1.18.  3.8.9.3.11.5.14.
8.15.23-  1.18.5.  25.15.21?
12.15.20.19  15.6.  12.15.22.5.
6.12.15.19.19.9.5.
24 24 24.
```

## Decoded text and translation

```text
DEAR CHICKEN
HOW- ARE YOU?
LOTS OF LOVE
FLOSSIE
X X X.
```

The dash after HOW and question mark after YOU are written marks, not editorial additions. Numeric letter-separating dots are not rendered as periods between decoded letters. The literal separate group is three Xs; in this affectionate note it is reasonably interpreted as kisses.

Readable English: “Dear Chicken, how are you? Lots of love, Flossie. XXX.” Chicken remains the writer's affectionate form of address rather than a substituted personal name.

Slovak: „Miláčik [doslova kuriatko], ako sa máš? Veľa lásky, Flossie. Tri bozky [interpretácia XXX].“

## Independent review and corrections

Claude Opus 5.5 independently re-read every numeric value and wrote a separate A1Z26 decoder on 26 October 2026. Review 1's verdict was REVISE: the four original lines and their 37 values were correct, but coverage missed the separate 24 24 24. group. The reviewer required no further round after the specified record corrections.

1. The three 24s were added to both transcripts and the decoder. The plaintext, translation and count now cover all 40 values and include X X X.
2. The numeric punctuation is preserved in a diplomatic record. The dash after HOW and question mark after YOU are identified as source marks.
3. The inaccurate warning about closely written 3 and 8 was removed: a clear dot separates them.
4. The actual physical overlap is disclosed: the 1 of the first 12 in LOTS partly touches the inverted JUN postmark. The visible lower stroke and clear 2 support 12, independently confirmed by the reviewer.

## Evidence, limitations and reproduction

The key decodes all 40 numeric values into a coherent greeting, closing name and kisses. Agreement of the decoded FLOSSIE with the ordinary signature and catalogue is supporting context; it is not identification of a historical person. Attribution of the dealer-like top-corner mark remains uncertain. No published target plaintext was used; a register snapshot does not establish priority.

Run from the repository root:

```sh
python3 ciphers/hcp-1492/work/decode.py
```

The command verifies original source hashes, checks that normalised and diplomatic records contain identical numbers, then prints 40 decoded letters with the recorded source punctuation. It does not read pixels. Source integrity checks and arithmetic decoding complement the independent scan collation; they do not replace it.

Source: https://crypto.hcportal.eu/dashboard/cryptograms/1492. Review record: review/REVIEW1.md. This report source incorporates all requested record corrections; final PDF verification and state marking are separate production steps.
