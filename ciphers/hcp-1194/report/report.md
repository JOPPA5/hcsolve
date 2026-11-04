# HCP 1194: a rune-alphabet love card from Tepl to Anton Schönfelder (1900)

Human solver: Tomáš Pavuk

**Status: deciphered in full (82 cipher signs, all covered by one key); independent review 1 verdict ACCEPT, no change to the decoded letters.** Report dated 2026-11-03.

## Origin and context

The cryptogram is record 1194 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1194), portal name cpc_1900-06-17_AT_Tepi_AT_Wien_schoenfelder-02, part of Tobias Schrödel's collection of cryptographic postcards (private collection). When captured on 2026-11-03 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, language Unknown, sender Unknown, recipient Anton Schönfelder, with no transcription or solution attached. A short web search found no published solution of this card.

The address side is in plain Kurrent handwriting: "Wolgeboren Herrn Anton Schönfelder, Wien IV, Favoritenplatz 7, Th. 29". The Austrian 5-heller stamp is cancelled **TEPL 17.6.(19)00** (Teplá in western Bohemia), with a Vienna arrival mark of 19.6.00. The picture side is a printed art card ("Franz. Künstler Karten No 3", publisher logo "SuS B."). The cipher is written in pencil along one long edge of the picture side, so the card has to be turned 90° to read it.

The sister card HCP 1195 (same recipient, also from Tepl, February 1900) uses the same alphabet; it was not used for this reading.

![Picture side as scanned (source/picture-large.jpg)](../source/picture-large.jpg)

![The cipher text turned upright (work/crop_all.png)](../work/crop_all.png)

![Address side: Anton Schönfelder, Wien IV (source/address-large.jpg)](../source/address-large.jpg)

![Stamp box: intact 5-heller stamp, TEPL 17.6.00 (work/stampbox.png)](../work/stampbox.png)

## Method

The solver (Claude Opus 5.5) worked from the un-converted high-resolution scan, rotated the cipher strip upright, and read it sign by sign from 3–5x enlargements of each line and of every doubtful sign (files in work/). Each sign shape was given a label, the transcription was stored in work/transcription.txt, and the key in work/key.json. The signs look like runes (some resemble futhark letters), but the values are not the futhark ones: the alphabet is home-made. Word gaps and full stops are written, which made the key easy to fix: HERZ, DANK, BRIEF, KUSS, GRUSS and STIMMUNG gave all letters with consistent repeated signs.

The reproduction command, run from the repository root, checks the SHA-256 of the source images and decodes the transcription:

```text
python3 -I ciphers/hcp-1194/work/decode.py
```

The reviewer (a separate Claude Opus 5.5 agent) made its own crops, its own sign labels and its own decoding script and obtained the same plaintext from all 82 enciphered signs.

## Key

Monoalphabetic substitution (MASC) with an invented rune-like alphabet. The shape names describe handwritten signs.

| Sign shape | Letter | Sign shape | Letter |
|---|---|---|---|
| asterisk | H | plain stem | I |
| cross with slanted bar | E | up-arrow | T |
| R-shape | R | stem with hook at top | L |
| down-arrow | Z | stem with closed flag | G |
| stem with two crossing bars | D | lightning | S |
| diagonal meeting a stem | A | fork | M |
| stem with leg down-right (Λ-like) | N | Γ / Π shape | U, Ü |
| stem with one up-right branch | K | B shape | B |
| stem with two up-right branches | F (and W, written heavily) | | |

18 letters are written with 17 distinct shapes. W (in ERWARTE) has no sign of its own: it is the F shape written very heavily, so F/W is a homograph resolved by word sense. U and Ü share one sign.

## Plaintext

Literal output of the decoder:

```text
HERZ. DANK FUR BRIEF. ERWARTE FEILERN
ANGESAGTEN.
INNIGEN GRUSS U. KUSS
STIMMUNG ANHALTEND.
DEI(N) RASA
```

Normalised German: **Herz. Dank für Brief. Erwarte Feilern angesagten. Innigen Gruss u. Kuss. Stimmung anhaltend. Dein Rasa.**

"Stimmung anhaltend." runs along the bottom edge with the signature to its right, so it may also be read before the greeting; the order does not change the content.

English: "Heart [dear heart]. Thanks for the letter. Expecting Feiler, as announced. Fond greeting and kiss. Mood lasting [my good mood continues]. Your Rasa."

Slovak: "Srdce. Vďaka za list. Očakávam Feilera, ako bolo ohlásené. Vrúcny pozdrav a bozk. Nálada trvá. Tvoj/Tvoja Rasa."

The style is the clipped, telegram-like German typical of love and friendship postcards around 1900.

## Uncertainties

1. **FEILERN ANGESAGTEN.** All seven signs F-E-I-L-E-R-N are clear (the L is the hook sign, the same as in ANHALTEND, and differs from the barbed up-arrow T). The meaning is tentative: the best reading is the surname Feiler with the old-fashioned accusative ending -n ("erwarte Feilern" = I expect Feiler) and "angesagten" as telegraphic "as announced". This is the only word whose sense is a hypothesis.
2. **W in ERWARTE** is the heavy F shape; W rests on word sense.
3. **Signature.** The fourth sign of DEIN is overwritten (a G-like sign with a Λ-shaped N written over and above it), so DEIN rests on word sense. If Rasa is a woman, "Deine" would be expected; the overwriting may hide such a correction. The name is given literally as RASA (both A's are clear); a nickname or a misshaped Rosa is possible but not assumed.
4. The first sign of line 2 (A of ANGESAGTEN) is faint, and the first sign of line 4 (S of STIMMUNG) is partly cut at the card edge; both are still recognisable.
5. **Hidden writing.** The stamp is intact and nothing shows around it; the picture side has no other writing. No steganographic text was found, but writing under the stamp cannot be excluded from the scan.
6. Who Feiler and Rasa were is not known; no external source was found.

## Review and changes

Review 1 (independent Claude Opus 5.5 agent) gave the verdict **ACCEPT**. It re-ran the command, made an independent transcription and decoder, checked the disputed signs (L of FEILERN, W of ERWARTE, the faint line starts, the signature) on enlargements, and checked the address side and stamp. It raised four minor findings, all accepted:

1. The solution said "one sign per letter"; corrected to 18 letters with 17 shapes (F/W homograph).
2. FEILERN ANGESAGTEN is presented with its literal reading and a tentative interpretation (uncertainty 1).
3. The DEIN/DEINE question and the overwritten signature sign are noted (uncertainty 3).
4. "für" is shown with its umlaut in the normalised text.

After a remark from the human team that cards of another series hide messages under the stamp, the stamp box and picture side of this card were checked again; nothing hidden was found, so the cipher type stays **MASC**. No decoded letter changed after review.

## Credit

Transcription, key reconstruction, decipherment and report: Claude Opus 5.5 (2026-11-03). Independent review: a separate Claude Opus 5.5 agent. No earlier work on this card existed.
