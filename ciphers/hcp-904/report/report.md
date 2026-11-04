# HCP 904: a German postcard from Leipzig written in Greek letters (1902)

Human solver: Tomáš Pavuk

**Status: fully deciphered apart from the sender's name (one word) and two letters restored under ink blots. Independent review 1 gave the verdict ACCEPT and no decoded letter changed.** Report dated 2026-11-03.

## Origin and context

The cryptogram is record 904 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/904), portal name cpc_1902--_DE_Leipzig_DE_Wolferode bei Eisleben_, part of Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-11-03, the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, with language Unknown, sender Unknown and recipient Pfarrer Martin Laibelein. No transcription or solution was attached. The only reference given is the HistoCrypt paper on the collection (https://ecp.ep.liu.se/index.php/histocrypt/article/view/166).

The card is a picture postcard, "Gruss aus Leipzig – Reichsgericht", published by W. Hagelberg AG, Berlin. It shows the Imperial Court of Justice (Reichsgericht) in Leipzig by night. Six handwritten lines run across the lower part of the picture and the square in front of the building. They look like Greek, but the language is German.

The address side is in plain German Kurrent: **Herrn / Martin Laibelein / Wolferode b/ Eisleben / Pfarre.** This is a parsonage in Wolferode near Eisleben (Saxony-Anhalt). A German 5-pfennig Germania stamp is cancelled at Leipzig. The visible part of the postmark shows ".. 1. 02 5-6 N", so the card was posted in 1902; the exact day is covered.

![Picture side: the six lines in Greek letters below the picture (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side: Herrn Martin Laibelein, Wolferode b/ Eisleben, Pfarre; Leipzig postmark (source/address-large.jpg)](../source/address-large.jpg)

The card's other marks are not cipher text: the printed headings, the publisher's line along the left edge, the stamp and postmark, and the HC Portal watermark. The ink smudges in the sky of the picture are not letters.

## Method

The transcription was made **by hand** from the full-resolution scan (work/hires/), using enlarged crops of each line (work/crops/). No OCR was used. Each sign was identified as a Greek letter shape, and the resulting letters were read as German.

The writer simply spelled German in the Greek alphabet, one Greek letter for each Latin letter. Greek has no letters for German h, w and j, so the writer improvised:

- the rough-breathing mark ʽ stands for h
- the archaic digamma Ϝ (F-shaped) stands for W
- capital Ι stands for J
- χ stands for the digraph ch
- υ stands for u, and once for w ("beantuorten")
- φ stands for f, and once for v ("fier" = vier)

In review, a second Claude Opus 5.5 agent compared the transcription sign by sign with its own crops of the scan. It then decrypted the text with its own script and its own key table (review/work/my_decode.py). Its output was identical to the solver's.

## Key

The cipher is a simple substitution of one Greek letter for each Latin letter. Upper and lower case are kept.

| Sign | Letter | Sign | Letter |
|---|---|---|---|
| α / Α | a / A | ν (written like a Latin r) | n |
| β / Β | b / B | ο | o |
| γ / Γ | g / G (Γ drawn T-shaped in "Gruss") | ρ (written like ς) | r |
| δ / Δ | d / D | σ | s |
| ε | e | τ (hooked, with a top bar) | t |
| ζ | z | υ (v-shaped) | u (once w) |
| ʽ | h (a large free hook at the start of a word) | φ | f (once v) |
| ι (written like a small c) / Ι | i / J | χ | ch |
| κ / Κ | k / K | Ϝ (digamma) | W |
| λ / Λ | l / L | μ / Μ | m / M |

The key accounts for every sign form on the card. No sign is left unexplained, and no letter has more than one sign. The German letters p, q, x and y do not occur, and v occurs only in the spelling "fier".

## Plaintext

Transcription, line by line ([x] = a sign under an ink blot, restored; ? = a sign not identified):

```text
[Λ]. Μ. Κονντε λειδερ Δειν λιεβεν Βριεφ
νιχτ μεʽρ βεαντυορτεν. φιερ Ϝοχεν σινδ
αβε[ρ] λανγ, καννστ Δυ μιρ κεινε ανδε[ρ]
Αδρ. ανγεβεν? σονστ μυστ Δυ Διχ σχον σο λανγε γε-
δυλδιγεν. ʽαβε μιχ σεʽρ υβερ Δεινεν Βριεφ γεφρευτ.
ʽερζλιχεν Γρυσσ υ Κυσσ Δεινε τρ. Ιε??ι.
```

Literal German as decoded, with spelling and grammar as written:

```text
[L]. M. Konnte leider Dein lieben Brief
nicht mehr beantuorten. fier Wochen sind
abe[r] lang, kannst Du mir keine ande[r]
Adr. angeben? sonst must Du Dich schon so lange ge-
duldigen. habe mich sehr uber Deinen Brief gefreut.
herzlichen Gruss u Kuss Deine tr. Je??i.
```

Normalised German (the expansions and corrections are editorial): **L[ieber] M[artin]! Konnte leider Deinen lieben Brief nicht mehr beantworten. Vier Wochen sind aber lang, kannst Du mir keine andere Adr[esse] angeben? Sonst musst Du Dich schon so lange gedulden. Habe mich sehr über Deinen Brief gefreut. Herzlichen Gruss u[nd] Kuss, Deine tr[eue] Je..i.**

English translation: **Dear M[artin]! Unfortunately I was no longer able to answer your dear letter. But four weeks is a long time, can't you give me another address? Otherwise you will have to be patient for that long. I was very glad of your letter. Warm greetings and a kiss, your faithful Je..i.**

Slovak translation: **Milý M[artin]! Žiaľ, na tvoj milý list som už nestihla odpovedať. Štyri týždne sú však dlhé, nemôžeš mi dať inú adresu? Inak sa budeš musieť tak dlho obrniť trpezlivosťou. Tvoj list ma veľmi potešil. Srdečný pozdrav a bozk, tvoja verná Je..i.**

Notes on the reading:

- The literal text keeps the writer's small slips: "Dein lieben Brief" for "Deinen lieben Brief", "must" for "musst", "uber" without the umlaut, the phonetic spellings "beantuorten" and "fier", and "geduldigen", an old or dialect form of "sich gedulden" ("to be patient").
- "Deine tr." is read as "Deine treue" ("your faithful"), a common closing. The feminine form "Deine" shows that the writer is a woman.
- The context appears to be that Martin will be away, or hard to reach, for about four weeks. The writer asks for another address so that she can write to him in the meantime.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-904/work/decode.py
```

The script uses only the Python standard library and writes no files. It first checks the SHA-256 hashes of the four scans (two in source/ and two in work/hires/). It then decodes the hand transcription in work/transcription.txt with the Greek-to-Latin key and prints the six literal German lines shown above. The script does not read the images. The transcription was made by hand and was confirmed independently in review.

## Uncertainties

- **First sign of line 1.** It is under a solid triangular ink blot and looks like a "4" on the scan. Its outline fits Λ, which gives "L. M." = "Lieber Martin" and matches the recipient's first name. A filled-in Δ ("D. M.", for example "Dein M...") cannot be ruled out. Only the "M." is read directly, and the expansion "Lieber Martin" is editorial.
- **abe[r] and ande[r].** The last sign of each word is blotted, and for "ande[r]" it also lies at the card edge. Both are restored as r from the sense of the word. Whether an e followed "ander" ("andere") cannot be seen. The meaning is the same either way.
- **Start of line 5.** The first three signs of "duldigen" (δ, υ, λ) are smudged and written over, and the λ is almost solid ink. They can still be read as d u l, but the reading partly relies on the word "ge-duldigen", which continues from the end of line 4.
- **Sign shapes.** The Γ of "Gruss" is drawn T-shaped and could be taken for τ; the word decides it. The h of "herzlichen" is a large free-standing hook with a dot above it, the same as at the start of "habe". It is not ι or ε.
- **Sender.** The signature reads Ι ε, then an η/ν-like sign with a cross stroke, then a ϑ/δ-like loop, then ι: "Je??i". A pet name such as Jenni or Jetti is possible but not established, so the name is left unread. It is the only unread word on the card.
- **Under the stamp.** The stamp was not lifted and only the scan is available, so it cannot be checked whether anything is written under it. Nothing hidden was found anywhere else on either side.
- **Prior solutions.** No published solution of this card was found or used. The portal status was Not solved, and the AI Decipherment Register had no entry for record 904 when checked on 2026-11-03.

## Review summary

The review was carried out by a separate Claude Opus 5.5 (Anthropic) agent. Round 1 ended with the verdict **ACCEPT**. The reviewer:

- ran the reproduction command (all hash checks OK; output identical to the claimed plaintext)
- decrypted its own transcription with a key it wrote independently, with identical output
- checked every word of the six lines against its own crops of the high-resolution scan, enlarged 2–5 times
- judged the German coherent and fitting for a private postcard of 1902
- confirmed that the address side carries no cipher and that no published solution was used

All five of its minor findings were accepted, and this report reflects them:

- **First sign of line 1.** Δ is now named explicitly as the alternative to Λ, and "Lieber Martin" is marked as an editorial expansion.
- **Smudged start of line 5.** The report now says that δ υ λ partly rely on the sense of the word.
- **Sign shapes.** The T-shaped Γ and the free-standing ʽ hook are now described in the key and in the uncertainties.
- **Signature.** It stays "Je??i", and no name is offered as a reading.
- **Cipher type.** It stays MASC. No steganography was found, and the area under the stamp could not be checked.

No decoded letter changed as a result of the review. All the work on this card was done by Claude Opus 5.5: the transcription, identifying the key, the decipherment, the response to the review and this report. No earlier solver had worked on this number.

## Sources

- HC Portal record 904, General, Description and Attachments tabs, captured 2026-11-03: https://crypto.hcportal.eu/dashboard/cryptograms/904 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/2772/conversions/cpc_1902--_DE_Leipzig_DE_Wolferode-bei-Eisleben__pic-large.jpg (source/picture-large.jpg); original resolution in work/hires/.
- Address side: https://api.hcportal.eu/media/2773/conversions/cpc_1902--_DE_Leipzig_DE_Wolferode-bei-Eisleben__adr-large.jpg (source/address-large.jpg); original resolution in work/hires/.
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-11-03.
