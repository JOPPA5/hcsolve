# HCP 1077 (cpc_1908-01-10_DE_Fechenheim_DE_Fechenheim_): a sender's name in numbers, Fechenheim 1908

Human solver: Tomáš Pavuk

**Status: deciphered in full (14 of 14 number groups); independent review 1 verdict ACCEPT, no change to the decoded text.** Report dated 2026-11-03.

## Origin and context

The cryptogram is record 1077 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1077), portal name cpc_1908-01-10_DE_Fechenheim_DE_Fechenheim_, part of Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-11-03 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, language Unknown, sender Unknown, recipient "Fräulein Gerda Vinth ?", with no transcription or solution attached. The portal links the HistoCrypt paper on the collection (https://ecp.ep.liu.se/index.php/histocrypt/article/view/166).

The picture side is a chromolithograph titled "Behüt' dich Gott" (a trumpeter of the Thirty Years' War period standing by his horse, with a tavern scene in a medallion), printed by Heinr. & Aug. Brüning, Hanau (Dep. 579). In the free space on the right the sender wrote, in plain German Kurrent script, **Herzlichen Gruß sendet** ("warm greetings sends"), followed by two lines of numbers separated by dots, and a large pen flourish below them.

The address side is in plain Kurrent: **An Fräulein Gerda Diehl. in Fechenheim, Jubiläumstr. No 18.** It carries a 5-Pfennig Germania stamp cancelled FECHENHEIM 10.1.08 (10 January 1908) and a later pencil dealer's note "6G". Fechenheim, then a separate town east of Frankfurt am Main, lies close to Hanau, where the card was printed; the card was evidently sent locally.

The recipient's surname differs from the portal entry: the portal gives "Vinth ?" with its own question mark, while solver and reviewer both read the Kurrent letters as D, i, e, h (with its descending loop), l: **Diehl**. This is a reading of plain writing, not of the cipher, and it is offered as a correction of the portal metadata.

![Picture side: Kurrent greeting, two lines of numbers, and the paraph below them (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side: Fräulein Gerda Diehl, Fechenheim, Jubiläumstr. No 18; stamp cancelled FECHENHEIM 10.1.08 (source/address-large.jpg)](../source/address-large.jpg)

No published solution of this card was found (portal: none attached; a short web search found nothing).

## Method

The digits were read by hand from 4–8x enlargements of the un-converted high-resolution scan of the picture side (3468 x 2298 pixels). The transcription is:

```text
11. 20. 4. 22. 9. 7.
10. 1. 11. 2. 8. 5. 13. 13.
```

The position of the numbers, right after "Herzlichen Gruß sendet", calls for the sender's name. The simplest school cipher of the period, A = 1, B = 2 and so on, was tried first. With the full 26-letter alphabet it gives KTDVIG JAKBHEMM, which is not language. The German school alphabet of the time often omits J (I and J share one number); with that 25-letter alphabet, U and V kept separate, the same numbers give **LUDWIG KALBHENN** on both lines with no exception. An alphabet that also merges U and V gives LUDXIG, so it is excluded.

The reviewer read the digits independently from its own crops and decoded them with its own script under all three alphabets; its digits agreed with the solver's in all 14 positions.

## Key

Number substitution (monoalphabetic substitution with numbers), 25-letter alphabet without J:

| A | B | C | D | E | F | G | H | I/J | K | L | M | N |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 |

| O | P | Q | R | S | T | U | V | W | X | Y | Z |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 |

Only the sender's name is enciphered; the rest of the card is plain.

## Plaintext and translations

Line 1: 11 L, 20 U, 4 D, 22 W, 9 I, 7 G = LUDWIG.
Line 2: 10 K, 1 A, 11 L, 2 B, 8 H, 5 E, 13 N, 13 N = KALBHENN.

- German: **Herzlichen Gruß sendet Ludwig Kalbhenn.**
- English: Ludwig Kalbhenn sends warm greetings.
- Slovak: Srdečný pozdrav posiela Ludwig Kalbhenn.

Kalbhenn is a rare but attested surname in Hesse; Ludwig is a common Hessian first name.

## Reproduction

From the repository root:

```text
python3 -I ciphers/hcp-1077/work/decode.py
```

The script checks the SHA-256 hashes of the two portal images and the high-resolution picture scan, then decodes work/transcription.txt with the key above and prints "Herzlichen Gruss sendet" and "LUDWIG KALBHENN".

## Uncertainties

1. Line 2, position 6 (the "5" = E) is the weakest sign: on the scan it is a heavy blob with a thin rising tail and a tick that may be the flag of the 5 or the start of the next stroke. The reading 5 rests partly on word sense. The alternatives 1, 3, 6 and 8 give KALBHANN, KALBHCNN, KALBHFNN and KALBHHNN, none of which is an attested name.

![Line 2, position 6, enlarged with autocontrast (review/work/five.png)](../review/work/five.png)

2. Line 1, group 2 ("20" = U): the 0 is heavily overwritten, but it is a closed loop. LUDWIG needs it.
3. Line 2, group 4 ("2" = B) is a German-style 2 with a long tail; it is a 2 on the pixels.
4. The pen flourish below the numbers begins with a heavy dark hook and ends with a small dot. It is read as the writer's paraph (signature flourish), possibly built on the initials L K, not as a further cipher group such as "2." = B: it is four to five times taller than the digits, stands off the number lines, and is drawn in one continuous movement with the long loops of the flourish, while every number group is written separately and closed by its own dot.

![The paraph below the numbers, with the dark hook at its top (review/work/flourish2.png)](../review/work/flourish2.png)

5. It was not verified that a Ludwig Kalbhenn lived in or near Fechenheim in 1908.
6. The recipient surname Diehl is a reading of plain Kurrent and differs from the portal's "Vinth ?".
7. Hidden writing: the stamp box, the picture and the edges of both sides were inspected. Nothing protrudes from under the cancelled stamp and no hidden writing was found elsewhere, but what lies beneath the stamp cannot be seen on a scan. The card is therefore classed as a plain MASC, not as MASC with steganography.

## Review summary

An independent Claude Opus 5.5 agent reviewed the solution (review/REVIEW1.md). It re-ran the reproduction command, decoded its own reading of the digits with its own script under three alphabets, checked every digit, the greeting and the address on 3–8x crops of the high-resolution scans, and looked for hidden writing. Verdict: **ACCEPT**, with four minor findings:

1. The weak digit 5 rests on word sense: kept in the uncertainties, with the alternatives listed.
2. The dark hook at the top of the flourish should be described and its exclusion as a cipher group justified: done (uncertainty 4).
3. The recipient surname Diehl should be presented as a correction of the portal's "Vinth ?", not a silent replacement: done (Origin and context).
4. The register type should be MASC, not MASC + Steganography, since no steganography was found: adopted.

No reading changed as a result of the review.

## Sources

- HC Portal record 1077: https://crypto.hcportal.eu/dashboard/cryptograms/1077 (metadata, picture and address scans, high-resolution originals; see ciphers/hcp-1077/SOURCES.md).
- Collection paper linked from the portal: https://ecp.ep.liu.se/index.php/histocrypt/article/view/166

Solver: Claude Opus 5.5 (Anthropic), 2026-11-03; reviewer: a separate Claude Opus 5.5 agent.
