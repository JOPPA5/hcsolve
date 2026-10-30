# HCP 1093 (cpc_1913-04-15_UK_Shawford_UK_Winchester Hants_): a Pigpen postcard from Bob to Betty

Human solver: Tomáš Pavuk

**Status: deciphered in full (152 of 152 cipher signs); independent review 1 verdict ACCEPT, one count corrected (nine kisses, not eight), no change to the message.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1093 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1093), portal name cpc_1913-04-15_UK_Shawford_UK_Winchester Hants_, part of Tobias Schrödel's collection of cryptographic postcards (private collection; reference: https://ecp.ep.liu.se/index.php/histocrypt/article/view/166). When it was captured on 2026-10-25 the portal listed it as **Not solved**, tagged Postcard, T. Schrödel Collection, Pigpen, category Substitution / Monoalphabetic, date 1913-04-15, language Unknown, sender Unknown, recipient Miss Unsworth, with no transcription or solution attached.

The picture side is a sepia photographic card of a long-haired collie-type dog with the printed caption "Don't make me laugh." (series 9428/3). It carries no cipher.

The address side is addressed in plain writing to **Miss Unsworth, Park Lane, Twyford, Nr Winchester, Hants.** It has a green halfpenny King George V stamp cancelled SHAWFORD with "AP 15" legible; the year 1913 comes from the portal catalogue. Shawford and Twyford are neighbouring villages just south of Winchester in Hampshire. The printed publisher line names E. A. Schwerdtfeger & Co., London. The cipher message, eleven rows of Pigpen signs, is written in the lower half of the address side, perpendicular to the address; a short pencil note at the left edge ("M.13.8. D", apparently a dealer's or collector's mark) is not cipher.

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side turned so that the cipher reads upright; the address now runs sideways (work/upright.jpg, a pure rotation of source/address-large.jpg)](../work/upright.jpg)

## Method

The card was read with a **known, transferred key**: the same "interleaved" Pigpen alphabet had already been established on two sister cards of the Schrödel collection, HCP 1187 and HCP 1188 (also 1913), deciphered and accepted earlier in this repository. The key was not recovered blind from this card, but it decodes every sign here without change.

The transcription is manual. An OpenAI GPT solver (GPT-6 Astra / GPT-6.1 Sol) captured the portal record and scans on 2026-10-25, rotated the address side upright, applied the sister-card key and produced a partial reading in which the B of BRUCE, the two words in the middle of row 6, the signature and the blotted sign were left open. On 2026-10-30 Claude Opus 5.5 re-read every sign on 3–10× enlarged crops, resolved those points, added the final row of kisses, and wrote the transcription file and decoder. Each sign is recorded as an outline (which strokes of the Pigpen grid are present, or which way a wedge points) plus a dot flag.

## Key

Each outline stands for a pair of consecutive letters: the undotted sign is the first letter, the dotted sign the second. This differs from the common textbook Pigpen, which puts A–I in an undotted grid and J–R in a dotted one.

| Outline (strokes present) | Undotted | Dotted |
|---|---|---|
| bottom + right (⅃) | A | B |
| bottom + left + right (⊔) | C | D |
| bottom + left (L) | E | F |
| top + bottom + right (⊐) | G | H |
| four sides (□) | I | J |
| top + bottom + left (⊏) | K | L |
| top + right (⌝) | M | N |
| top + left + right (⊓) | O | P |
| top + left (⌜) | Q | R |
| V, point down | S | T |
| >, point right | U | V |
| <, point left | W | X |
| ^, point up | Y | Z |

23 of the 26 letters occur on the card; J, Q and Z do not.

## Plaintext

Literal decipherment, row by row as written (lower-case e = restored under an ink blot):

```text
DEAREST BETTY
WHAT ABOUT THIS
FOR A PHOTO OF
BRUCE SHALL GO TO
BED EARLY TONIGHT
FAALS TIRAD OR SOME
THING COLD A LITTLE
BeTTER WITH FONDEST
LOVE AND KISSES FROM YOURS
EVER BOB
XXXXXXXXX
```

Row 6 literally reads **FAALS TIRAD**: in three places the writer drew the ⅃ outline (A) where the sense needs E (the L outline). With these three signs emended, the message reads:

**DEAREST BETTY, WHAT ABOUT THIS FOR A PHOTO OF BRUCE? SHALL GO TO BED EARLY TONIGHT, FEELS TIRED OR SOMETHING. COLD A LITTLE BETTER. WITH FONDEST LOVE AND KISSES FROM YOURS EVER BOB  XXXXXXXXX**

Punctuation is editorial; the card has commas or full stops after most words. "Shall go to bed" and "feels tired" have no expressed subject, as is common in postcard style; they may refer to the writer or to Bruce. Bruce is most likely the dog shown on the picture side ("what about this for a photo of Bruce?").

English (normalised): **Dearest Betty, what about this for a photo of Bruce? [I] shall go to bed early tonight, feel(s) tired or something. Cold a little better. With fondest love and kisses from yours ever, Bob. xxxxxxxxx**

Slovak translation: **Najdrahšia Betty, čo povieš na toto ako fotku Brucea? Dnes večer pôjdem skoro spať, som (je) unavený alebo čo. Nádcha je trochu lepšia. S najvrúcnejšou láskou a bozkami, navždy tvoj Bob. xxxxxxxxx**

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1093/work/decode.py
```

The script uses only the Python standard library and writes no files. It checks the SHA-256 hashes of the two scans, decodes the manual transcription in work/transcription.txt with the key above, prints both the literal and the emended reading, asserts that the emended text equals the plaintext above, and ends with `152 signs decoded; source hashes OK; emended text matches SOLUTION.md.` It does not read the image; the transcription step is manual and was checked independently in review.

## Uncertainties

- **Three emended signs (FAALS TIRAD → FEELS TIRED).** The signs are clearly written as ⅃ (A); both the solver and the reviewer read them so on the enlargements. Everywhere else on the card E (15 times) and A (8 times) are kept apart, and the emendation to E is the only reading that gives sense. Why the writer slipped is not known; a left–right (mirror) confusion of the two outlines is a guess, not an established fact.
- **TIRED, signs 3–4** (dotted ⌜ and ⅃) are written close together and could be misread as one dotted box (J); the top stroke stops short of the right-hand vertical, so they are two signs. The alternative gives no English.
- **Ink blot.** The second sign of BETTER is under an ink blot; a left vertical and a bottom stroke running right are visible (the L outline, E/F), the dot cannot be seen. Restored as E.
- **The dot in the first B of BOB** lies over the upside-down printed publisher line. Its pixels are darker and greyer than the orange print around it and match the pen dots elsewhere, so it is read as a pen dot (B, not A).
- **The dot in the T of TIRED** is faint but present; the undotted reading (S, "SIRED") gives no sense.
- The identities of Bob, Betty (Miss Unsworth) and Bruce are not established; no genealogical search was made. Betty is taken as a pet name of the addressee.
- The year of the postmark is not legible; the date 1913-04-15 rests on "AP 15" on the cancellation and the portal catalogue.
- Readings rest on a single 1024-pixel scan per side; the physical card was not seen.
- No published solution of this card was found or used; the portal status was Not solved.

## Review summary

Reviewer: Claude Opus 5.5 (Anthropic), a separate agent, round 1, verdict **ACCEPT**. The reviewer ran the reproduction command (output identical to the claimed plaintext), decoded the transcription with its own independently written table and parser (0 unparsed tokens, same literal text), checked the transcription sign by sign against its own 3–9× crops of the scan, including FEELS, TIRED, the blotted sign, BRUCE and the signature BOB, and judged the plaintext natural Edwardian English consistent with the card. Its three findings were minor:

1. **The kiss row has nine signs, not eight.** Confirmed on a fresh 4× crop: a ninth dotted < stands a little apart at the left of the row. The transcription, decoder, plaintext and sign count (now 152) were corrected. The message did not change.
2. **The "mirror slip" explanation is speculative.** Agreed; it is now presented as a guess, and the literal FAALS TIRAD is shown next to the emended text in this report.
3. **Faint dot in the T of TIRED.** Already disclosed; no change.

## Credit

Portal capture, key transfer from HCP 1187/1188 and a partial reading: OpenAI GPT (GPT-6 Astra / GPT-6.1 Sol), 2026-10-25. Full re-collation, completion of the decipherment, response to review and this report: Claude Opus 5.5, 2026-10-30. Independent review: a separate Claude Opus 5.5 agent.

## Sources

- HC Portal record 1093, General, Description and Attachments tabs, captured 2026-10-25: https://crypto.hcportal.eu/dashboard/cryptograms/1093 (source/metadata.md).
- Address side: https://api.hcportal.eu/media/3340/conversions/cpc_1913-04-15_UK_Shawford_UK_Winchester-Hants__adr-large.jpg (source/address-large.jpg).
- Picture side: https://api.hcportal.eu/media/3339/conversions/cpc_1913-04-15_UK_Shawford_UK_Winchester-Hants__pic-large.jpg (source/picture-large.jpg).
- Tobias Schrödel, cryptographic postcards collection: https://ecp.ep.liu.se/index.php/histocrypt/article/view/166
- Sister cards with the same key: ciphers/hcp-1187 and ciphers/hcp-1188 in this repository.
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-29: no record for this card.
