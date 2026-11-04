# HCP 928: a 1908 love note from Vance, Alabama, to Delia Fischer

Human solver: Tomáš Pavuk

**Status: deciphered in full except the sender's signature sign; independent review 1 verdict ACCEPT, no change to the decoded letters.** Report dated 2026-11-03.

## Origin and context

The cryptogram is record 928 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/928), portal name "cpc_1908-09-08_USA_Vance, Alabama_USA_Birmingham, Alabama_", part of the T. Schrödel collection of cryptographic postcards (private collection). When it was captured on 2026-11-03 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, language Unknown, sender Unknown, recipient Delia Fischer, with no transcription or solution attached.

The address side carries a green one-cent Franklin stamp and the postmark **VANCE, ALA., SEP 8, 1908** (Vance is a small town in Tuscaloosa County, Alabama, south-west of Birmingham). It is addressed in plain writing to **Miss Delia Fischer, #42 Woodland Ave., Birmingham, Ala.** The left half ("This space may be used for correspondence") holds six cipher lines and a cipher signature. The picture side is a comic card titled "RAPID TRANSIT" (a boy riding a pig), published by K-Win & Co., Chicago; its free space holds eleven cipher lines and a second signature.

Note on file names: the portal's image names are swapped against their content. source/address-large.jpg shows the **picture** side and source/picture-large.jpg shows the **address** side; the same holds for the full-size originals in work/hires/.

![Picture side, "Rapid Transit", with eleven cipher lines (source/address-large.jpg; the file name is swapped)](../source/address-large.jpg)

![Address side: six cipher lines and signature at the left, the plain address to Miss Delia Fischer, Birmingham, at the right (source/picture-large.jpg; the file name is swapped)](../source/picture-large.jpg)

Other marks, none of them cipher: the printed headings, the publisher's line, the plain address, stamp, postmark and the portal watermark. The stamp box, the margins, the "Post Card" heading and the picture were inspected for hidden writing (steganography is common on cards of this collection): nothing was found. The stamp is affixed, so whatever may lie under it cannot be seen on the scans.

## Method

The transcription is manual. All reading was done on 3 to 5 times enlarged crops of the full-size originals in work/hires/ (crops in work/crops/), sign by sign, and written into work/transcription.txt with one ASCII character per sign. Words are separated by short dashes, which made the word lengths visible from the start. Short, frequent words gave the first letters: the doubled-mark words (see below), the repeated three-sign word on the first line ("back back back"), "to", "me", "the", "is", and the long word on line 2 that matches the address, "bir_ingham". The rest of the key followed from word sense and was then checked against every occurrence on both sides. work/decode.py applies the key to the transcription and prints the plaintext.

Two diacritic conventions are used by the writer:

- a small caret written under a sign marks a capital letter (This, Take, Delia, That, Will, Please, Yours);
- two short strokes above a sign mark a doubled letter (moon, honeymoon, soon, letter, Will).

In review a separate Claude Opus 5.5 agent read both sides from its own crops, entered its own sign names and its own key in an independent script, and obtained the same text with the same key and no conflict (25 distinct signs, 233 sign tokens).

## Key

Simple monoalphabetic substitution (MASC) with invented signs, English plaintext. Sign labels are approximate names for handwritten shapes.

| plain | sign | plain | sign | plain | sign |
|---|---|---|---|---|---|
| a | X | i | P | r | a |
| b | 9 with straight stem (q) | j | y with a dot | s | ) |
| c | 6 | k | round 9 / reversed e | t | cent-like sign |
| d | pi-like sign | l | d | u | ( or a larger C-shape |
| e | 8 | m | 7 | v | : |
| f | o (small plain circle) | n | / | w | division-like sign |
| g | 2 | o | 5 | y | circle crossed by a bar |
| h | 3 | p | n | | |

Not attested on the card: q, x, z. One extra sign, written like a K, occurs only in the signature and is not read.

## Plaintext

Literal decipherment (from work/decode.py; [m] is a letter restored under an ink blot, [K] the unread signature sign):

```text
[picture side]
Take me back back back
to bir[m]ingham.
Delia, is thet trip
you intend taking
a honeymoon?
if not, please do'nt
go soon.
That letter was a
god send to me.
Will yos be so kind as to write
another? Please, Yours truly we[K], w
[address side]
This is a fine
moon light night
and i'd give the
world just to
be walking with
you.
we[K].
```

English, normalised (punctuation and spelling slips corrected editorially):

**Take me back, back, back to Birmingham. Delia, is that trip you intend taking a honeymoon? If not, please don't go soon. That letter was a godsend to me. Will you be so kind as to write another? Please. Yours truly, We[K], W.**

**This is a fine moonlight night and I'd give the world just to be walking with you. We[K].**

Slovak translation:

**Vezmi ma späť, späť, späť do Birminghamu. Delia, je tá cesta, na ktorú sa chystáš, svadobná cesta? Ak nie, prosím, nechoď [tak] skoro. Ten list mi bol darom z nebies. Budeš taká láskavá a napíšeš ďalší? Prosím. S úctou, We[K], W.**

**Je krásna mesačná noc a dal by som celý svet za to, aby som sa mohol prechádzať s tebou. We[K].**

The opening "Take me back ... to Birmingham" plays on the "Rapid Transit" pig ride of the picture; the writer, in Vance, misses the addressee in Birmingham and worries that a trip she plans might be a honeymoon.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-928/work/decode.py
```

The script uses only the Python standard library, checks the SHA-256 hashes of the four source images, and prints the literal plaintext above. The transcription step itself is manual; it was confirmed independently in review.

## Uncertainties

- **Signature.** Both signatures read "We" followed by a sign written like a K that occurs nowhere else; it may be a plain letter or an initial. The picture side adds a comma and one more w-sign. The sender's name is not established. This is the one unread item on the card.
- **Birmingham.** The 4th sign is covered by an ink blot; m is restored from word sense and from the address on the card.
- **"thet".** The signs are clearly t-h-e-t; read as a slip for "that".
- **"yos".** In "Will yos be" the third sign is ")" (s) where "(" (u) is meant; "you" rests on sense.
- **"do'nt".** The o carries two short strokes and a dot, unlike the plain two-stroke doubling mark; taken as the apostrophe. "don't" rests on sense.
- Small marks taken as punctuation or strays: a vertical stroke after "Delia" (comma), a dot above the first dash of line 1 (stray). Capital marks are not written at every sentence start.
- What lies under the affixed stamp cannot be seen.
- A short web search (2026-11-03) found no published solution of this card; the portal lists none.

## Review summary

Reviewer: Claude Opus 5.5 (Anthropic), a separate agent, round 1, verdict **ACCEPT**. The reviewer ran the reproduction command (output identical to the claimed plaintext), read both sides sign by sign from its own enlargements, and decoded its own transcription with its own script and key: same text, same key, no conflict, every word covered. It confirmed the hard calls (straight-stemmed b against round k, e in "thet", ")" in "yos", the doubling and capital marks) and found no hidden writing around the stamp or in the picture, so MASC rather than "MASC + Steganography" is the label on the evidence. Its four minor findings and what changed:

- **Signature sign unread.** Kept and disclosed as the single unresolved item.
- **Mark in "don't".** Re-checked; now described as two strokes and a dot.
- **Web search.** A short search was made; nothing relevant was found, and this is recorded.
- **Swapped file names.** Repeated in this report.

No decoded letter changed as a result of the review. Transcription, key reconstruction, decipherment and this report were made by Claude Opus 5.5; there was no earlier work on this card.

## Sources

- HC Portal record 928, General, Description and Attachments tabs, captured 2026-11-03: https://crypto.hcportal.eu/dashboard/cryptograms/928 (source/metadata.md).
- Picture side (file named address): https://api.hcportal.eu/media/2845/conversions/cpc_1908-09-08_USA_Vance,-Alabama_USA_Birmingham,-Alabama__adr-large.jpg
- Address side (file named picture): https://api.hcportal.eu/media/2844/conversions/cpc_1908-09-08_USA_Vance,-Alabama_USA_Birmingham,-Alabama__pic-large.jpg
- Full-size originals: the same URLs without "conversions/" and "-large" (work/hires/).
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-11-03: no entry for this card.
