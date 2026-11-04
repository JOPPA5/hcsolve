# Solution hcp-1077 (cpc_1908-01-10_DE_Fechenheim)

Solver: Claude Opus 5.5, 2026-11-03. No earlier work on this number. No published solution was found (portal status Not solved, no attachment; a short web search for this card found nothing).

## Cipher type and key

Number substitution (MASC with numbers) over the 24/25-letter German school alphabet without J (I = J = 9), U and V separate:

| A | B | C | D | E | F | G | H | I | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 |

Only the sender's name is enciphered. Plain A=1..Z=26 (with J) gives KTDVIG / JAKBHEMM, which is not language; omitting J gives a clean name on both lines.

## Whole card

Picture side ("Behüt' dich Gott", trumpeter with horse; printer Heinr. & Aug. Brüning, Hanau, Dep. 579), plain Kurrent:

    Herzlichen Gruß sendet

then, in numbers (my transcription, work/transcription.txt):

    11. 20. 4. 22. 9. 7.
    10. 1. 11. 2. 8. 5. 13. 13.

= LUDWIG KALBHENN

followed by a large decorative pen flourish (paraph), possibly containing the initials L K; it is not text and carries no further message.

Address side (plain Kurrent): "An Fräulein Gerda Diehl. in Fechenheim, Jubiläumstr. No 18." Postmark FECHENHEIM 10.1.08 10–11 N, 5-Pfennig Germania stamp. Pencil "6G" is a later dealer/collector note. The portal metadata gives the recipient as "Gerda Vinth ?"; I read the Kurrent surname as Diehl (D-i-e-h-l, the h with its descending loop).

## Plaintext and translations

- German: Herzlichen Gruß sendet Ludwig Kalbhenn.
- English: Ludwig Kalbhenn sends warm greetings.
- Slovak: Srdečný pozdrav posiela Ludwig Kalbhenn.

## Command (from the repo root)

    python3 -I ciphers/hcp-1077/work/decode.py

It checks the SHA-256 of source/picture-large.jpg, source/address-large.jpg and the hi-res picture scan, then prints the greeting and the decoded name.

## Uncertainties

1. Group 2 of line 1 ("20"): the 0 is heavily overwritten (a blot over another stroke); read as 20 = U. LUDWIG needs it.
2. Group 4 of line 2 ("2"): a German-style 2 with a long tail; it is a 2 on the pixels, = B.
3. Group 6 of line 2 ("5"): a small blob with a thin rising tail squeezed between two dots; the digit shape is weak on the scan. The reading 5 = E rests partly on word sense (KALBHENN). This is the one weakest call.
4. The surname Kalbhenn is a rare but attested Hessian surname; I did not verify that a Ludwig Kalbhenn lived in or near Fechenheim in 1908.
5. Recipient surname Diehl is a Kurrent reading (plain text, not cipher); the portal's "Vinth ?" is different.
6. Stamp: the scan cannot show anything under the stamp; nothing is visible around its edges. No hidden writing was found on the picture side or edges of the scan.

## Why I believe it is correct

All 14 number groups decode under one fixed standard key with no exceptions into a German first name and surname, exactly at the place where "Herzlichen Gruß sendet" expects the sender's name. The first line gives LUDWIG with no ambiguous digit.

## Response to review 1

Review 1 (Claude Opus 5.5, separate agent) gave verdict ACCEPT with four minor findings. The decoded text is unchanged.

1. Weak digit, line 2 position 6. Agreed. The reading 5 = E rests on word sense: on the pixels it is a heavy blob with a thin rising tail and a tick that may belong to the 5's flag or to the next stroke. The reviewer's script tried 1, 3, 6 and 8 in that slot (KALBHANN, KALBHCNN, KALBHFNN, KALBHHNN); none gives an attested name, while 5 gives the attested Hessian surname Kalbhenn. This wording is carried into the report unchanged.
2. Dark hook at the top of the flourish. On the review crop (review/work/flourish2.png) the flourish below the numbers starts with a heavy dark hook (written with more ink pressure, the same ink as the digits), runs down through a looped stroke crossing a long diagonal, and ends in a hook with a small dot at its foot. I do not read it as a further cipher group (for example "2." = B) because: (a) it is about four to five times taller than the digits of the number lines and stands well below and to the left of them, not on a line; (b) it is drawn in one continuous movement with the loops and long horizontal sweeps of the paraph, whereas every number group is written separately and closed by its own dot; (c) a single letter B after LUDWIG KALBHENN would add nothing to the formula "Herzlichen Gruß sendet <name>". It is a signature flourish (paraph), possibly built on the initials L K; the small dot is an ending tick of the pen. No message is lost if this is wrong, but it is stated here as a reading, not a certainty.
3. Recipient surname. The portal metadata gives "Fräulein Gerda Vinth ?" (with its own question mark). On the address side I read the Kurrent surname as Diehl (D, i, e, h with descending loop, l, then a full stop); the reviewer agrees. This is a plain-text reading that corrects the portal entry; it is not part of the cipher, and the report says so explicitly rather than replacing the portal value silently.
4. Register type. Agreed: number substitution with a fixed A=1 alphabet (without J) is MASC. No steganography was found: the stamp on the address side is cancelled and nothing protrudes from beneath it, and the picture and the card edges carry no hidden writing on the scans. The register type is therefore "MASC", not "MASC + Steganography". What lies under the stamp cannot be checked from a scan; this stays listed as unverifiable.

Reproduction command re-run after this response (python3 -I ciphers/hcp-1077/work/decode.py): three SHA-256 checks OK, output "Herzlichen Gruss sendet" / "LUDWIG KALBHENN", unchanged.
