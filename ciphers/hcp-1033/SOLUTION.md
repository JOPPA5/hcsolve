# Solution hcp-1033 (cpc_1906-08-23_DE_Munsterlager_DE_Ahlden_)

Solver: Claude Opus 5.5 (claude-opus-5-5), 2026-11-03. No earlier work on this number; no published solution found
(portal status Not solved, no transcription or solution attached). Transcription made by the solver from
work/hires/cpc_1906-08-23_DE_Munsterlager_DE_Ahlden__adr.jpg (the portal attaches none).

## The card

Picture postcard (girl with flowers in her hair), posted at Munsterlager (Bz. Hannover), 23.8.06, to
Fräulein Hertha Tesche (portal: "Tesohe"), per Adr. Herrn Gastwirth(?) Koch, Ahlden a/Aller. The address is plain
German Kurrent; the surname and the occupation word are not certain and are not part of the cipher.
The whole message on the address side is numbers, written along the long edge of the card (turn the card 90 degrees
counter-clockwise), signed "14.9.9.14", plus a two-line postscript written upside down above the printed
"Postkarte" heading. The picture side and the visible stamp surround carry no writing; what lies under the stamp
cannot be checked from the scans.

## Cipher type and key

Number substitution, monoalphabetic (register label: MASC). The 25-letter alphabet (no J) is cut into five blocks of
five letters, and the blocks are numbered in reverse order, the letters inside each block in normal order:

| numbers | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| 21-25 | A | B | C | D | E |
| 16-20 | F | G | H | I | K |
| 11-15 | L | M | N | O | P |
| 6-10  | Q | R | S | T | U |
| 1-5   | V | W | X | Y | Z |

i.e. A=21 B=22 C=23 D=24 E=25, F=16 G=17 H=18 I=19 K=20, L=11 M=12 N=13 O=14 P=15, Q=6 R=7 S=8 T=9 U=10,
V=1 W=2 X=3 Y=4 Z=5. Umlauts are the base number with two dots above (10 with dots = Ü, 14 = Ö, 21 = Ä).
Numbers are separated by dots, words by a dash; "=" or ":" at line end marks a word broken across lines.
Not used on the card: 3 (X), 4 (Y), 6 (Q), 15 (P).

The key was found from the opening "12.25.19.13.25 - 11.19.25.22.25 - 18.25.7.9.18.21 !" = MEINE LIEBE HERTHA!
(the recipient's name) and confirmed by every other word on the card.

## Command

From the repo root:

    python3 -I ciphers/hcp-1033/work/decode.py

It checks the SHA-256 of the four scan files, prints the key and decodes work/transcription.txt line by line.

## Plaintext (as decoded, card lines)

    meine liebe hertha!
    für deine liebe karte
    meinen besten dank! bleibt
    denn deine mutter auch so
    lange dort wie du, oder
    ist sie wegen deines
    heimwehs dorthingekom=
    men gestern habe ich
    mich mit dem oberleu=
    tnant vertragen und aus=
    gesöhnt näheres darü=
    ber werde ich dir näch=
    stens brieflich mitteilen
    wie geht es dir da drüben
    herzlichen gruss und
    innigen ukss dein
    otto
    [postscript, upside down at the top]
    grusse bitte deine mut=
    ter von mir

Normalised German:

Meine liebe Hertha! Für deine liebe Karte meinen besten Dank! Bleibt denn deine Mutter auch so lange dort wie du,
oder ist sie wegen deines Heimwehs dorthin gekommen? Gestern habe ich mich mit dem Oberleutnant vertragen und
ausgesöhnt; Näheres darüber werde ich dir nächstens brieflich mitteilen. Wie geht es dir da drüben? Herzlichen Gruß
und innigen Kuss, dein Otto.
P.S. Grüße bitte deine Mutter von mir.

English:

My dear Hertha! Many thanks for your dear card! Is your mother staying there as long as you, or did she come there
because of your homesickness? Yesterday I made up and was reconciled with the first lieutenant; I will tell you more
about it soon by letter. How are you over there? Warm greetings and a fond kiss, your Otto.
P.S. Please give my regards to your mother.

Slovensky:

Moja milá Hertha! Za tvoju milú pohľadnicu ti zo srdca ďakujem! Zostane tvoja mama tam tak dlho ako ty, alebo tam
prišla kvôli tvojej túžbe po domove? Včera som sa s nadporučíkom udobril a zmieril; podrobnosti ti čoskoro napíšem
v liste. Ako sa ti tam darí? Srdečný pozdrav a vrúcny bozk, tvoj Otto.
P.S. Pozdravuj, prosím, odo mňa mamu.

## Uncertainties (all disclosed; none affects the sense)

1. "10.20.8.8" decodes to UKSS: the writer swapped the first two numbers of KUSS (20.10.8.8). Both numbers are
   clearly 10 and 20 on the scan; the reading "Kuss" is an editorial correction of a writer's slip.
2. The writer's 25 (a 2 with a hooked "ſ"-like 5) and 21 (a 2 with a plain 1) are usually distinct, but three
   numbers look closer to 21 or are cramped and are read by word sense (marked {n} in work/transcription.txt):
   line 12 "22.{25}.7" = (darü)BER; postscript line 2 "9.{25}.7" = (Mut)TER.
   Also postscript line 1 "{12}.10.9" = MUT, where the first number looks like 11 (L) but MUT=TER needs 12 (M).
3. Line 14 "24.7.10".{22}.25.{13}" = DRÜBEN: the 22 is written like "21" and the last number is cramped at the edge
   and looks like 11; DRÜBEN rests on word sense ("wie geht es dir da drüben").
4. Line 6 "19.8.9" = IST: the middle 8 is small and squashed but has the 8 shape.
5. Postscript first word "17.7.10.8.8.25" = GRUSSE; a dot above the 10 may be one umlaut dot (GRÜSSE) merged with
   the printed letter "t" of "postale"; not decided.
6. "14.9.9.14" (signature) = OTTO; it looks like a date (14.9.9.14) but decodes cleanly and stands where a name is
   expected after "dein".
7. Under the stamp: not inspectable from the scans. The picture side and the margins have no extra writing.

## Why it is correct

- The single 25-letter key, built from a regular rule (reversed five-letter blocks), decodes every number on the card
  (330 numbers, about 68 words) into grammatical German of the period with no unexplained residue except the one
  swapped KUSS.
- The opening names the addressee (Hertha), and the context fits: Munsterlager was the army training ground in
  the Lüneburg Heath, and the writer, a soldier, mentions his Oberleutnant; the letter-writer signs "Otto".
- Spellings of the time (Heimwehs, Gruss, brieflich mitteilen, nächstens) and the umlaut dots placed on exactly the
  numbers for U, O, A where German needs Ü, Ö, Ä are an independent check of the key.

## Response to review 1

Review 1 verdict: ACCEPT, four minor findings. The reading is unchanged.

1. Word-sense calls (BER, DRÜBEN, MUT, TER, UKSS). All five were already disclosed and are kept as they are.
   On DRÜBEN the reviewer reads the 4th number as a fairly clear 22. On review/work/z_druben.jpg I see the second
   digit of that number as a short upright stroke with no clear foot, so it stays closer to "21" than to a clear "22".
   Here I disagree in part, so the {22} mark stays in work/transcription.txt. Either way it is one sign inside a word
   that otherwise reads, and B is the only letter that fits "dr-ü-?-e-n". The final 13 (looks like 11) is still read
   by sense. I re-ran `python3 -I ciphers/hcp-1033/work/decode.py` and all four hash checks print OK. The output is
   unchanged.
2. Published-solution check. On 2026-11-03 I downloaded and searched the full text of the paper the portal cites:
   T. Schrödel, "Cryptographic postcards", HistoCrypt 2021
   (https://ecp.ep.liu.se/index.php/histocrypt/article/download/166/122/65). It is a survey and classification of the
   collection. It does not mention Munsterlager, Ahlden, Hertha or Otto. Its only 1906 card is one sent from Finland to
   Russia, and it prints no key or reading of this card. I found no other published solution. The portal attaches none.
   (SOURCES.md lists only the downloaded files, so the check is recorded here.)
3. Values 3 (X), 4 (Y), 6 (Q) and 15 (P) are not seen on the card. They come from the block rule only, and the report
   presents them that way.
4. GRUSSE vs GRÜSSE in the postscript stays open. The possible umlaut dot merges with the printed "t" of "postale".
   The sense is the same either way.

Steganography (prompted by the human's note on the Jolánka cards): this is a German 1906 card, not one from the
Jolánka series. The picture side has no writing. The stamp is intact, and there is no writing visible around it or in
the margins (work/crops/stamp.jpg, review/work/stamp.jpg). Nothing visible supports a hidden message, so the type stays
MASC. What lies under the stamp cannot be checked from the scans.
