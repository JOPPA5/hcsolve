# HCP 976: a postcard from Bad Brückenau to Emma Krumbholz in Heidelberg (1910)

Human solver: Tomáš Pavuk

**Status: deciphered in full; every cipher digit on the card decodes with one key. Independent review 1 verdict ACCEPT, no change to the decoded letters.** Report dated 2026-11-03.

## Origin and context

The cryptogram is record 976 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/976), portal name cpc_1910-03-21_DE_Bruckenau_DE_Heidelberg_heidelberg-01, part of Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-11-03 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, language Unknown, sender Unknown, recipient "Emma Kr", with no transcription or solution attached. The portal file name dates the card 1910-03-21.

The picture side is a printed view of **Bad Brückenau, Kurpark**, with the Hotel Füglein in the background (publisher Hans Brust, Brückenau, "Malerische Motive No. 15"). It carries a handwritten "1)" in the top left corner. The address side, written in plain German Kurrent, is addressed to **Frau Emma Krumbholz, Heidelberg, Mittelstr. 18**; the postmark reads BRÜCKEN[AU]. The stamp has been removed. The message is written sideways on the left half of the address side, marked "1)" again.

The card is the first of a numbered series sent by the same writer to the same addressee. A sister card in the same collection, HCP 974 (marked "3)", Bad Brückenau, Kgl. Kurhaus), uses exactly the same cipher (its first line decodes to "Mein Zustand ist"). Card "2)" of the series is not in the collection.

![Picture side: Bad Brückenau, Kurpark, with the handwritten "1)" (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side as scanned (source/address-large.jpg)](../source/address-large.jpg)

![Message turned upright, from the original high-resolution scan (work/crops/msg_rot.png)](../work/crops/msg_rot.png)

## Method

The transcription is **manual**: the original high-resolution scan of the address side was turned 90 degrees clockwise and read sign by sign from enlarged crops (work/crops/). The message mixes two kinds of writing: ordinary German Kurrent letters (H, d, c, h, t, D, V, B, k, N, r) and digits. The digits never stand where consonants such as h, t, c or k are needed, and every word turns into German as soon as 1–5 are read as the five vowels. Words such as "H25t2" (Heute), "02nd2" (sende), "V48" (von), "B95^ck2815" (Brückenau) and "638k2" (linke) fix each digit's value. The same key was found independently on the sister card HCP 974.

The stamp box and the picture side were inspected for hidden writing, because other postcard series in the collection (for example the Jolánka cards) carry a steganographic message under the stamp. Here the stamp box shows only paper residue and the postmark, and the picture side only the printed captions and the "1)". There is no hidden message, so the type is plain MASC.

## Key

Partial monoalphabetic substitution with digits (register label MASC): only ten letters are enciphered; all other letters are written in plain Kurrent.

| Digit | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 |
|---|---|---|---|---|---|---|---|---|---|---|
| Letter | a | e | i | o | u | l | m | n | r | s |

The five vowels in order take 1–5, then l m n r s take 6 7 8 9 0. The umlaut ü is written as 5 with a stroke above.

## Plaintext

Transcription, line by line (digits are cipher; letters are plain Kurrent; "/" marks a word broken over the line):

```text
Meinen Lieben!          (plain Kurrent)
H25t2 02nd2
25ch D32 1803ch/
t28 V48 B95^ck/
2815. D3202 30t
D32 - 73tt2, Nr 2
D32 638k2 023t2,
+ Nr 3 D32 92ch/
t2 [cross-mark] 023t2. 48092
V361 0t2ht
```

Decoded, line by line:

```text
Meinen Lieben!
Heute sende
euch die Ansich-
ten von Brück-
enau. Diese ist
die - Mitte, Nr 2
die linke Seite,
+ Nr 3 die rech-
te Seite. onsre
Vila steht
```

German, running text: **Meinen Lieben! Heute sende euch die Ansichten von Brückenau. Diese ist die Mitte, Nr. 2 die linke Seite, und Nr. 3 die rechte Seite. Onsre [unsre] Vila steht …**

English translation: **My dear ones! Today I am sending you the views of Brückenau. This one is the middle, No. 2 the left side, and No. 3 the right side. Our villa stands …**

Slovak translation: **Moji milí! Dnes vám posielam pohľady z Brückenau. Toto je stred, č. 2 ľavá strana a č. 3 pravá strana. Naša vila stojí …**

The sentence breaks off because it continues on card 2 of the series, which is not in the collection. The text describes the series itself: three views that together form a panorama, with this card (marked "1)") as the middle.

## Uncertainties

- **"Nr 2" and "Nr 3".** Here the digits 2 and 3 are plain numerals, not cipher; read as cipher they would give "Nre" and "Nri", which make no sense. The numeral reading rests on context (the card is "1)", its sister "3)"). This is the only place where digits are not cipher.
- **"onsre".** The signs are clearly 4 8 0 9 2 = o n s r e, with 4 = o fixed by "von". It is read as a slip or dialect form of "unsre" (our) and reported as written.
- **"Vila"** is written with one l (V-3-6-1).
- **The "+" before "Nr 3"** is read as the common handwritten abbreviation for "und" (and) and is rendered so in the running text and translations.
- **A cross-mark before "Seite" in line 9**: a long dark stroke crossed by three uprights, perhaps a cancelled letter. It is left out of the plaintext. This mark, the "+", the retraced 3 in "Seite" and the 0 of "steht" are in darker ink than the rest; they may come from a later retracing by the writer or by another hand, which cannot be decided from the scan.
- **Kurrent letters read partly by word sense**: c+h in "euch", "Ansichten" and "rechte"; ck in "Brückenau"; k in "linke"; the doubled t in "Mitte"; d in "sende". The digits themselves are unambiguous.
- **The opening "Meinen Lieben!"** and the address are plain Kurrent; the surname "Krumbholz" is partly read by sense (the portal gives only "Emma Kr").
- **The continuation** of "unsre Vila steht …" on card 2 cannot be read, because that card is not in the collection.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-976/work/decode.py
```

The script uses only the Python standard library. It checks the SHA-256 hashes of the four source images (two portal conversions in source/ and the two original scans in work/hires/), then decodes the manual transcription in work/transcription.txt with the key above and prints the ten decoded lines and the running text. It does not read the images; the transcription step is manual and was confirmed independently in review. In the script output the writer's looped d and V forms appear as capital "Die" and "Von"; this is a transcription convention only.

## Review summary

Reviewer: a separate Claude Opus 5.5 agent, round 1, verdict **ACCEPT**. The reviewer ran the reproduction command (output identical to the claimed plaintext), wrote its own decoder (review/work/mydec.py) with identical output, checked every row of the transcription sign by sign against the original scan in enlarged strips and close-ups, confirmed that all ten digits occur and each has a single value fixed by at least one unambiguous word, confirmed that "48092" really begins with 4 (so "onsre" is what is written), and inspected the stamp box and the picture side, finding no hidden message. Its three findings were minor and are reflected here:

- **"+" = "und".** The running text and both translations now render the "+" as "und / and / a"; the uncertainties state the reading.
- **Darker ink.** The darker-ink marks (cross-mark, "+", retraced 3 and 0) are now named as a possible later retracing.
- **Capitals in script output.** Explained as a transcription convention; this report uses normal German case.

No decoded letter changed as a result of the review. Transcription, key reconstruction, decipherment, the response to review and this report were made by Claude Opus 5.5; there was no earlier work on this number.

## Sources

- HC Portal record 976, General, Description and Attachments tabs, captured 2026-11-03: https://crypto.hcportal.eu/dashboard/cryptograms/976 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/2988/conversions/cpc_1910-03-21_DE_Bruckenau_DE_Heidelberg_heidelberg-01_pic-large.jpg (source/picture-large.jpg); original scan in work/hires/.
- Address side: https://api.hcportal.eu/media/2989/conversions/cpc_1910-03-21_DE_Bruckenau_DE_Heidelberg_heidelberg-01_adr-large.jpg (source/address-large.jpg); original scan in work/hires/.
- Sister card HCP 974 in this repository (same writer, addressee and key).
- Reference listed on the portal: HistoCrypt article, https://ecp.ep.liu.se/index.php/histocrypt/article/view/166
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-11-03 by the orchestrator: no entry for this card.
