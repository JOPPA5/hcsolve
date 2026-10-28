# HCP 995 (cpc_1900-02-10_DE_Bonn_DE_Berlin_mariechen-01): Pigpen lines to Mariechen in Berlin

Human solver: Tomáš Pavuk

**Status: all 66 cipher glyphs deciphered; independent review 1 verdict ACCEPT.** Report dated 2026-10-28.

## Origin and context

The cryptogram is record 995 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/995), portal name cpc_1900-02-10_DE_Bonn_DE_Berlin_mariechen-01, from Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-10-28 the portal listed it as **Not solved**, tagged Postcard, T. Schrödel Collection, Pigpen, category Substitution / Monoalphabetic, date 1900-02-10, language Unknown, location Europe, sender Unknown, recipient Mariechen Kühnast, with no transcription or solution attached. The collection is described in Schrödel's HistoCrypt paper (https://ecp.ep.liu.se/index.php/histocrypt/article/view/166); a bounded check of its illustrations found no matching card or key.

It is a German artist's postcard (Dr. Trenkler & Co., Leipzig, Künstlerpostkarte 507) titled "Im stillen Winkel" ("In a quiet corner"). It shows a couple embracing behind a screen while a row of onlookers peers over the top. The picture side carries a message in ordinary German cursive; five Pigpen initials are set into its last sentence, and two rows of Pigpen run along the bottom edge. The address side is in plain writing: **Fräulein Mariechen Kühnast, Berlin S. 59, Kottbuser Damm 72.** The 5-pfennig stamp is cancelled **BONN 10.2.00 9-10 V** (morning), and the Berlin delivery stamp reads **Bestellt vom Postamte 59, 11/2.00, 7¼-9½ V.** The card was therefore posted in Bonn on Saturday 10 February 1900 and delivered in Berlin the next morning, in agreement with the portal date.

![Picture side: ordinary cursive message with five Pigpen initials in its last line, and two Pigpen rows along the bottom edge (source/picture.jpg)](../source/picture.jpg)

![Address side: Fräulein Mariechen Kühnast, Berlin S. 59; Bonn postmark 10.2.00 and Berlin delivery stamp 11/2.00 (source/address.jpg)](../source/address.jpg)

## Method

The transcription is **manual**: the solver read each glyph from enlarged crops of the original scan and recorded its shape and approximate position in work/transcript.json. No OCR was used and the portal supplied no transcription.

The signs are Pigpen: corner, U-shaped and square cells of a tic-tac-toe grid, with and without a dot, plus an upright stroke, a check-like v and an upward wedge. The key is the German Pigpen grid with J omitted that the solver had already met on the related card HCP 1016 from the same collection. It was taken over as a candidate before this card was read, not fitted to a plaintext. It read the first row (WIE GEFÄLLT DIR DIE KARTE SIND) without any change, and then the second row and the five initials under the same key. There are 66 cipher glyphs: 5 initials, 25 in the first row and 36 in the second.

In review the reviewer re-read every glyph from its own upscaled crops before comparing, and decoded them with an independently written script. Its reading agrees with the solver's in all 66 positions. It checked in particular the R of KARTE under the watermark (⊓·, not □·), the D at the end of SIND, the slanted E in BENEIDEN, R against Z in HERZL, and the K and Ü of KÜSSE.

## Key

One letter per grid cell. The undotted cells give A–I, the dotted cells K–S (J is omitted, so I and J share a cell). Four further signs give T, U, W and Z.

| Sign | ┘ | ⊔ | └ | ⊐ | □ | ⊏ | ┐ | ⊓ | ┌ |
|---|---|---|---|---|---|---|---|---|---|
| Undotted | A | B | C | D | E | F | G | H | I/J |
| Dotted | K | L | M | N | O | P | Q | R | S |

| Sign | upright stroke | check-like v | wedge ^ | dotted wedge ^· |
|---|---|---|---|---|
| Letter | T | U | W | Z |

Two short strokes above ┘ give Ä, and above the check-like v give Ü; they are umlauts, not extra letters. The dotted □, ⊏ and ┐ (O, P, Q) and the letters V, X and Y do not occur on the card; the dotted cells follow from the grid and are not attested.

## Plaintext

Ciphertext as written, in the sign notation of the key table (· = dot, ¨ = umlaut, | = upright stroke, v = check, / = word gap):

```text
└·  /  ┘· ⊔·  /  ┌·  /  └·
^ ┌ □  /  ┐ □ ⊏ ┘¨ ⊔· ⊔· |  /  ⊐ ┌ ⊓·  /  ⊐ ┌ □  /  ┘· ┘ ⊓· | □ ?  /  ┌· ┌ ⊐· ⊐
⊐ ┌ □  /  ⊔ □ ┌ ⊐ □ ⊐·  /  ⊐· ┌ └ ⊓ |  /  ^· v  /  ⊔ □ ⊐· □ ┌ ⊐ □ ⊐· ?
  /  ⊓ □ ⊓· ^· ⊔·  /  ┐ ⊓·  /  u ┘· v¨ ┌· ┌· □ .
```

(The second Pigpen row is one line on the card; it is wrapped here. The "u" in it is ordinary cursive.)

Literal German, as decoded:

```text
[in the prose line "Darf ich bald mal wieder auf einen Brief von … hoffen."]
M. KL. S. M.

WIE - GEFÄLLT - DIR - DIE - KARTE? SIND
DIE - BEIDEN - NICHT - ZU - BENEIDEN? HERZL - GR - u KÜSSE.
```

The dashes are the writer's word separators. The "u" is written in ordinary cursive, not in Pigpen, and is not counted among the 66 glyphs. After KÜSSE there is a crossed cursive monogram with a full stop; it is not a Pigpen sign and is not identified.

Normalized German (spelling of 1900; the stops after Herzl, Gr and u are editorial):

**Wie gefällt dir die Karte? Sind die beiden nicht zu beneiden? Herzl. Gr. u. Küsse** = **Herzliche Grüße und Küsse.**

English translation: **How do you like the card? Aren't the two of them to be envied? Warm greetings and kisses.**

Slovak translation: **Ako sa ti páči pohľadnica? Nie je tým dvom čo závidieť? Srdečné pozdravy a bozky.**

The question refers to the picture: the two lovers in their "quiet corner", watched by the crowd above the screen.

### The embedded initials

The five Pigpen initials M. KL. S. M. stand in the last sentence of the cursive message: "Darf ich bald mal wieder auf einen Brief von M. Kl. S. M. hoffen". On a card addressed to Mariechen, the natural expansion is **von meinem kleinen süßen Mariechen** ("from my little sweet Mariechen"; Slovak "od mojej malej sladkej Mariečky"): dative after "von", with the last M matching the recipient's name. This is an editorial interpretation, not proven; the decoded text stays M. KL. S. M.

### The cursive message (context, not cipher)

The ordinary cursive message, as read by the solver (the opening abbreviation "S. M. Gr." is ordinary script and left unexpanded):

**Seit dem letzten S. M. Gr. haben wir nichts mehr von einander gehört. Ich hoffe dies Deinerseits als ein Zeichen annehmen zu dürfen, daß es Dir recht gut geht. Dann nehme ich Dir auch Dein etwas rätselhaftes Schweigen nicht übel. Darf ich bald mal wieder auf einen Brief von [M. KL. S. M.] hoffen.**

English: Since the last S. M. Gr. we have heard nothing more from each other. I hope I may take this, on your side, as a sign that you are quite well. Then I will not hold your somewhat puzzling silence against you either. May I hope soon again for a letter from [M. Kl. S. M.]?

Slovak: Od posledného S. M. Gr. sme o sebe nič nepočuli. Dúfam, že to z tvojej strany smiem brať ako znamenie, že sa ti darí celkom dobre. Potom ti ani tvoje trochu záhadné mlčanie nebudem zazlievať. Smiem čoskoro znova dúfať v list od [M. Kl. S. M.]?

## Reproduction

From the repository root:

```sh
python3 ciphers/hcp-995/work/decode.py
```

The script checks the SHA-256 hashes of both scans, decodes the manual, position-indexed transcription with the key above, prints the initials and the two rows (M KL S M / WIE GEFÄLLT DIR DIE KARTE SIND / DIE BEIDEN NICHT ZU BENEIDEN HERZL GR KÜSSE) and the total of 66 glyphs, and lists the shape assignments used. It does not read the image; the transcription step is manual (and was confirmed independently in review). Its "Editorial punctuation" line still shows "KARTE," and "u."; as found in review, the card has "KARTE?" and "u" (see Review summary). The decoded letters are not affected.

## Uncertainties

- The expansion of the embedded initials (meinem kleinen süßen Mariechen) is an editorial interpretation.
- The crossed monogram after KÜSSE is not identified; no sender name is asserted. The sender is unknown.
- The faint pencil writing up the left margin of the picture side is ordinary cursive and not cipher, but it is not transcribed; in review only the words "Sonntag" and "angek…" were partly legible.
- The opening abbreviation "S. M. Gr." in the cursive message is not expanded. The cursive message is the solver's contextual reading, not cipher output.
- Whether the writer put abbreviation stops after HERZL and GR cannot be told from the dashes; they are given as editorial.
- There was no blind test: the key came from the related card HCP 1016 and was applied to this card in sequence. It is the standard grid, and it decodes all 66 glyphs into German, including the rare letters K, W, Z, Ä and Ü.
- No search for a prior publication was made beyond the portal status (Not solved), the AI Decipherment Register (158 contributions, this card absent) and a bounded check of Schrödel's paper, all on 2026-10-28.

## Review summary

Reviewer: Claude Opus 5.5 (Anthropic), round 1, verdict **ACCEPT**. The reviewer ran the reproduction command, read all 66 glyphs from its own crops of the scan before comparing, decoded them with an independently written script, and found no differences. It confirmed that one key covers every glyph and that no Pigpen elsewhere on the card was left out. Its five findings were minor and are reflected here:

- The mark after KARTE is a question mark, like the one after BENEIDEN, not a comma.
- The postmark date is resolved: Bonn 10.2.00, and the Berlin delivery stamp 11/2.00 rules out the 16th. The full address (Berlin S. 59, Kottbuser Damm 72) is now given.
- The cursive "u" has no full stop: the only dot there belongs to the following K.
- The embedded initials are offered with the expansion "meinem kleinen süßen Mariechen", labelled unverified.
- The closing is presented as "Herzl. Gr. u. Küsse" with the stops editorial.

No change to the decoded letters resulted from the review. The closing steps (response to review, this report, the register entry) were prepared by Claude Opus 5.5 on the solver's behalf at the human's request; the decipherment itself was made by the solver, OpenAI GPT (GPT-6 Astra).

## Sources

- HC Portal record 995, General, Description and Attachments tabs, captured 2026-10-28: https://crypto.hcportal.eu/dashboard/cryptograms/995 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/3045/conversions/cpc_1900-02-10_DE_Bonn_DE_Berlin_mariechen-01_pic-large.jpg (source/picture.jpg).
- Address side: https://api.hcportal.eu/media/3046/conversions/cpc_1900-02-10_DE_Bonn_DE_Berlin_mariechen-01_adr-large.jpg (source/address.jpg).
- T. Schrödel, collection paper in HistoCrypt: https://ecp.ep.liu.se/index.php/histocrypt/article/view/166 (copy in ciphers/hcp-1081/source/schrodel-2021.pdf).
- Related card with the same key: HCP 1016 (ciphers/hcp-1016).
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-28.
