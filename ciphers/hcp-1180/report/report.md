# HCP 1180 (cpc_--___CH_Neuchatel_): a Swiss postal card written as mock algebra

Human solver: Tomáš Pavuk

**Status: deciphered in full; one word ("Stosmonat") is read but not understood. Independent review 1 verdict ACCEPT, no change to the decoded text.** Report dated 2026-11-03.

## Origin and context

The cryptogram is record 1180 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1180), portal name cpc_--___CH_Neuchatel_, part of Tobias Schrödel's collection of cryptographic postcards (private collection). When captured on 2026-11-03 the portal listed it as **Not solved**, tags Postcard and T. Schrödel Collection, language Unknown, sender Unknown, recipient Oskar Egli, with no transcription or solution attached.

It is a Swiss 5-centime "Carte-correspondance" (postal card with an imprinted stamp). The address side is in plain writing: **Monsieur Oskar Egli au Crédit Mutuel à Neuchâtel**. The cancellation reads "-VI 75", i.e. June 1875; the year digits are faint, so 1876 cannot be fully excluded, but the decade is secure. The message side is covered with thirteen lines of what looks like algebra (brackets, plus and minus signs, root signs, equals signs), and two further lines run vertically along the left margin, from top to bottom on the card.

![Message side (source/picture-large.jpg)](../source/picture-large.jpg)

![Left margin, cropped from the high-resolution scan and turned 90° counter-clockwise (work/margin_upright.png)](../work/margin_upright.png)

![Address side: Oskar Egli, Crédit Mutuel, Neuchâtel (source/address-large.jpg)](../source/address-large.jpg)

Other marks, none of them cipher: the printed card headings, the imprinted stamp and its cancellation, the HC Portal collection stamp (which partly covers the word "must" in line 8), and a faint pencil numeral above line 1 in a different medium, probably a later annotation. Because the stamp is imprinted there is no stamp box to hide anything under, and the card has no picture side; neither solver nor reviewer found hidden, reversed or edge writing.

## Method

The transcription is manual (Claude Opus 5.5), made sign by sign from enlarged crops of the un-converted high-resolution scan (3468 × 2298 px). No OCR was used and the portal supplied no transcription.

The key emerged at once from short recurring groups: "3c-h" occurs several times and, if digits are vowels, gives ICH; "b-2f+3n+d-2" gives BEFINDE and "s-2+3t" gives SEIT. Testing the rule "digits 1–5 are the vowels a, e, i, o, u; all other letters are themselves; operators are decoration" on the whole card turned every group into German. The two fractions that occur, 1/1 and 5/5, fit ä and ü (vorläufig, Altbüron, Grüsse, Plüs).

The decoder (work/decode.py) checks the SHA-256 of the four scan files and decodes work/transcription.txt; one command, run from the repository root, reproduces the whole plaintext:

```text
python3 -I ciphers/hcp-1180/work/decode.py
```

In review a separate Claude Opus 5.5 agent wrote its own tokenizer and decoder, made its own crops, checked all thirteen main lines and both margin lines group by group, and obtained an identical output.

## Key

A partial substitution: **only the vowels are enciphered**, by digits; consonants are written as themselves inside a mock-algebra disguise. The register label used is MASC, the nearest allowed type.

| Cipher | Plain | Cipher | Plain |
|---|---|---|---|
| 1 | a | 5 | u |
| 2 | e | 1/1 | ä |
| 3 | i | 5/5 | ü |
| 4 | o | consonant | itself |

The signs + − = ( ) . and the root sign √ carry no letter value. Words are often, but not always, separated by "=". Sign counts in the transcription: 173 consonant letters; digits 1:13, 2:48, 3:36, 4:10, 5:8; fractions 1/1:2, 5/5:3. No digit outside 1–5 occurs and no plain vowel letter occurs anywhere, so the rule covers the entire message. Example: "(w-2r+d)2 = 3c-h = d-3r" gives "werde ich dir".

## Plaintext

Transcription, line by line ("|" marks editorial word breaks, V the root sign):

```text
(w-2r+t)(h-2r) = | k-1m+p-f . Vg-2n+4s-s+2 !
3c-h = | b-2f+3n+d-2 - | m-2c+h = | s-2+3t = | 2(3n-3g+2n =
t-1g+2n = | 3n = | 2t-t+3s-w+3l . = | (s-4b+1-l)d = | 3c-h =
w-3+2d+2r = | 3n = | 1-l(t+b-5/5r-4n- | (r+2s)(3d-3-2r+2 =
(w-2r+d)2 = | 3c-h = | d-3r = | (2+3)(n-2n) = | b-r+V3.2f = | s+c
h+r-2+3b-V2n = . | 3c-h = | (m-2l+d)2 = | d-3r = | h3-2m+3t =
(v+4r)(l-1/1+5f)-3g = | d-1+s = | d-5 = | m-3r = | (k+2+3n)2 =
[struck] (z-3.2t)(5n-g) = | 1b-4n-3+2r+2n = | m-5s+t =
w(2r-d+2) = | d-3r = . | d-1+n+n = | d+3-2 = | 5r-s+1-c-h+2
m-3t+t-h-2V3l-2n . =
2m-p+f-1n-g+2 = | 5n-t+2rVd-2s-s+2n = | d-3.2
(s-1+5m-1/1s)(3g-s-t)-2n = | g+r-5/5s-s+2 = | v-4n
p-l-5/5s = | s-4l+3
margin:
2t-t+3s+w-3l = | d-2n = | 35. = | s+t-4s+m-
4n-1-t = | 1n+4 = | t+5b-1+k .
```

German (1870s Swiss spelling kept; punctuation editorial; writer's slips in square brackets):

Werther Kampfgenosse! Ich befinde mech [= mich] seit einigen Tagen in Ettiswil. Sobald ich wieder in Altbüron residiere, werde ich dir einen Brief schreiben. Ich melde dir hiemit vorläufig, das[s] du mir keine Zietung [= Zeitung] abonieren must; werde dir dann die Ursache mittheilen. Empfange unterdessen die saumäsigsten Grüsse von Plüs = Soli.

Margin: Ettiswil, den 35. Stosmonat anno Tubak.

**English.** Worthy comrade-in-arms! I have been in Ettiswil for some days. As soon as I am residing in Altbüron again I will write you a letter. For now I just let you know that you need not take out a newspaper subscription for me; I will then tell you the reason. Meanwhile receive the most tremendous ("saumässig", Swiss slang) greetings from Plüs = Soli. Margin: Ettiswil, the 35th of "Stosmonat", anno Tubak (a joke date; "anno Tubak" means roughly "in the year dot").

**Slovak.** Vážený spolubojovník! Už niekoľko dní som v Ettiswile. Len čo budem opäť bývať v Altbürone, napíšem ti list. Zatiaľ ti len oznamujem, že mi nemusíš predplácať noviny; dôvod ti potom poviem. Medzitým prijmi tie najstrašnejšie (švajčiarsky slang „saumässig") pozdravy od Plüs = Soli. Okraj: Ettiswil, 35. „Stosmonat", anno Tubak (žartovný dátum, „za dávnych čias").

The text is coherent Swiss German of the period: the old spellings "Werther" and "mittheilen", "hiemit", "residiere", the slang "saumässig" and "anno Tubak". Ettiswil and Altbüron are neighbouring villages in the canton of Lucerne; the recipient worked in Neuchâtel.

## Uncertainties

1. **h / k.** The hand uses one looped letter for both. It is read k only in Kampf, keine and Tubak, on word sense; elsewhere h.
2. **Writer's slips, decoded literally.** "m-2c+h" gives "mech" for "mich" (the digit is clearly a looped 2, unlike this hand's open 3). "(z-3.2t)" gives "Zietung" for "Zeitung" (the 3 stands before the 2; the same 3.2 group gives "die" correctly elsewhere). A first attempt before it is struck through by the writer and not decoded.
3. **must.** "m-5s+t" is partly under the collection stamp; the order 5 then s is visible, and s is read on word sense (this hand's s resembles a 5).
4. **saumäsigsten.** In "3g-s-t" the s again resembles a 5, which would give no word; read s on word sense.
5. **Stosmonat.** Read sign by sign (s t o s m o n a t) but not understood. It is the one unexplained word: probably a joke month, perhaps a play on the old Swiss month names (Brachmonat, Heumonat), matching the joke day "35" and "anno Tubak". It is not claimed to be a known word.
6. **Signature** "Plüs = Soli" is read literally; perhaps the surname Plüss and a nickname. Identities of the writer and of Oskar Egli were not established.
7. **Postmark year** "75" is faint (possibly "76").
8. Word division is editorial.

No published solution of this card was found (a short web search, including Klaus Schmeh's blog, which features Schrödel cards).

## Review and what changed

Review 1 (separate Claude Opus 5.5 agent) gave the verdict **ACCEPT**. It re-ran the command (hash checks OK, output identical), decoded the transcription with its own script (identical), checked every group against its own crops of the high-resolution scan, and inspected the address side for hidden writing (none). It raised four minor findings, all addressed without changing the decoded text:

1. The margin was described as reading upwards; it in fact runs top to bottom on the card. Description corrected and an upright crop added.
2. "must" was translated as a prohibition; it now reads "you need not" (Slovak "nemusíš").
3. "Stosmonat" must stay flagged as unexplained; it is.
4. The MASC label should be explained as a vowel-only substitution; the key section now says so. There is no steganographic part, so "MASC + Steganography" does not apply.

## Credits

Transcription, key reconstruction and decipherment by Claude Opus 5.5 (2026-11-03); independent review by a separate Claude Opus 5.5 agent. No earlier AI work on this number.
