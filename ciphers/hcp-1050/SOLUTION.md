# hcp-1050 – Solution

Card: HC Portal cryptogram 1050, `cpc_1910-03-17_DE_Schweidnitz_DE_Konigszelt_fritzlehmann-11`, T. Schrödel collection.
Address side: Germania 5 Pf stamp (still affixed), postmark SCHWEIDNITZ 17.3.10; addressed in plain Kurrent "Herrn Fritz Lehmann,
Königszelt, Bahnhofstr. N. 1". The enciphered message (17 lines of dotted numbers, pencil) fills the left half. An upside-down
plain-Kurrent pencil sender note sits at the top centre. Picture side: printed photo card "Kommt ein Vogel geflogen!" with the
printed verse "Denn ich kann dich nicht begleiten, weil ich hier bleiben muss" and publisher number 3309/6; no handwriting found.
Portal status: Not solved; no transcription or solution attached. Transcription and decipherment are my own (Claude Opus 5.5,
2026-11-03) from the high-resolution scan in work/hires/. No earlier work existed in this directory. One web search (2026-11-03)
found no published solution of this card. The key is the one already established on the Lehmann sister cards hcp-1134 / hcp-1113
(also used on hcp-1060); I transferred it and checked it against every number here.

## Cipher type and key

Number substitution (MASC), German. The 25-letter alphabet without J, numbered from 2:

| A | B | C | D | E | F | G | H | I | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |10 |11 |12 |13 |14 |15 |16 |17 |18 |19 |20 |21 |22 |23 |24 |25 |26 |

Dots separate numbers, dashes separate words, a double tick over a number is an umlaut (15" = Ö, 21" = Ü), a bar over 13 doubles
it (MM), "=" at a line end is the German hyphenation sign. Numbers used: 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 18 19 20 21 22 23 26.

## Transcription

work/transcription.txt (17 lines; conventions in its header).

## Plaintext

Decoded (as written):
LIEBER FRITZ ENDLICH EIN LEBENS ZEICHEN VOIN DIR UND FREUE MICH SEHR DAS ES SCHON BESSER GEHT VIELEICHT KÖNTEN WIER SONTAG
WIEDER ZUSAMMEN SEIN WAS IST DENN SO PLÖTZLICH ÜBER DICH GEKOMMEN? GUTE BESSERUNG BALDIGEN WIEDERSEHN GRUSZ KUSZ MINNA

Normalised German: "Lieber Fritz! Endlich ein Lebenszeichen von dir, und [ich] freue mich sehr, dass es [dir] schon besser geht.
Vielleicht könnten wir Sonntag wieder zusammen sein. Was ist denn so plötzlich über dich gekommen? Gute Besserung, [auf] baldiges
Wiedersehen. Gruß, Kuss, Minna."

English: "Dear Fritz! At last a sign of life from you, and I am very glad that you are already better. Perhaps we could be together
again on Sunday. Whatever came over you so suddenly? Get well soon, see you soon. Greetings, a kiss, Minna."

Slovak: "Milý Fritz! Konečne od teba znak života a veľmi sa teším, že ti je už lepšie. Možno by sme mohli byť v nedeľu znova spolu.
Čo ťa to tak náhle prepadlo? Skoro sa uzdrav, dovidenia čoskoro. Pozdrav, bozk, Minna."

Plain sender note (upside down, top centre, not enciphered), read: "Abs. M. L.(?) b. Fr. Sch...tke(?) / Schweidnitz Graben(?)str. /
N. 3 II Hof" = "Sender: M. L., c/o Mrs Sch...tke, Schweidnitz, Grabenstr.(?) no. 3, 2nd floor, rear building". It is the return
address; the initial "M" fits the signature Minna. Second initial and the landlady's surname are reported literally/uncertainly.

## Command (from repo root)

```
python3 -I ciphers/hcp-1050/work/decode.py
```

It checks the SHA-256 of both source scans and both hi-res originals, then decodes work/transcription.txt with the key above.

## Uncertainties

1. Writer's spellings, decoded as written, not corrected: VOIN (22.15.10.14, the 10 is clear; = "von"), VIELEICHT (one L across
   the line break), KÖNTEN (umlaut ticks over the 15, single T and single N; = "könnten"), WIER (= "wir"), SONTAG (single N), GRUSZ / KUSZ (ß written as SZ),
   BALDIGEN (for "baldiges"), WIEDERSEHN.
2. SO (line 12): the 15 is heavily retraced/overwritten and looks blotted; 1 and the flag of the 5 are visible. 15 = O rests partly
   on word sense (work/crops/so.png).
3. BESSE= (line 14, 3.6.19.19.6): the two 19s are written without a separating dot, the second partly on the green divider line
   (work/crops/besse.png); read as 19.19 = SS.
4. ZUSAMMEN: the bar over 13 is clear (work/crops/bar13.png), so MM; GEKOMMEN also has a barred 13.
5. "?" after GEKOMMEN is a question-mark-shaped sign on the card, taken as punctuation.
6. Sender note: second initial ("L"?), the landlady's surname (Kurrent "Sch...tke") and the street name ("Graben-"?) are not
   firmly read; they are names/addresses and are reported literally. They do not affect the message.
7. Steganography: the stamp is still on, so nothing beneath it can be inspected on these scans; no traces at its edges. Picture side:
   only printed text.

## Why I believe it is correct

One fixed table, identical to the one independently established on two sister cards to the same recipient, decodes all 17 lines
(200 numbers) into coherent colloquial German with no leftover signs: a girlfriend's note glad that Fritz is recovering,
proposing Sunday, wishing him well, signed Minna. Doubling bars fall exactly on the MM of ZUSAMMEN and GEKOMMEN, umlaut ticks on
KÖNTEN, PLÖTZLICH and ÜBER, and the hyphenation signs fall on real word breaks (VIE=LEICHT, PLÖTZ=LICH, BESSE=RUNG, WIE=DERSEHN). The
return address in Schweidnitz matches the postmark.

## Response to review 1

Verdict ACCEPT, four minor findings. No change to the key; one letter changed (O to Ö).

1. KÖNTEN umlaut: agreed. On the reviewer's 3x crop (review/work/konten.png) a double tick stands above the 15 of 11.15.14.20.6.14,
   placed high above the number exactly like the tick over the 21 of ÜBER (review/work/ueber.png). I had taken it for a stray mark
   belonging to line 7. Fixed: work/transcription.txt line 8 now reads `11.15".14.20.6.14`; the plaintext and uncertainty 1 above say
   KÖNTEN. Re-ran `python3 -I ciphers/hcp-1050/work/decode.py`: all four SHA-256 checks OK, output now ends line 8 with KÖNTEN and is
   otherwise unchanged; it is identical to the reviewer's independent decoding.
2. Number count: agreed. Counting the numbers in work/transcription.txt gives 200, not "about 95". Fixed in "Why I believe".
3. SO (line 12): agreed; the disclosure stays (uncertainty 2) and is carried into the report.
4. Sender note: agreed; second initial, landlady's surname and the street-name vowel stay marked uncertain in the report.

Register: the reviewer and I both keep the type MASC. The human asked (2026-11-03) to label cards with hidden messages under the stamp
as `MASC + Steganography`; that remark concerns the Jolánka series. On this card the stamp is still affixed and the scans show nothing
at its edges or on the printed picture side, so no hidden message can be shown and the label stays MASC; the unchecked area under the
stamp is stated as an uncertainty.
