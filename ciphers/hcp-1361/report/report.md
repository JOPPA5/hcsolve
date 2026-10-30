# HCP 1361 (pc_hcp_42): a Caesar-shift love postcard to W. Abbott, 6 July 1907

Human solver: Tomáš Pavuk

**Status: whole message read (50 of 50 enciphered letters, one fixed key); two short abbreviation groups are left undecided; independent review 1 verdict ACCEPT, no change to the decoded letters.** Report dated 2026-10-30.

> **My own loving boy. Cricket match to-day. Gaunt won. M & L. [t?].. Your own M-h. girl.**

## Origin and context

The cryptogram is record 1361 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1361), portal name pc_hcp_42, part of the HCPortal collection of cryptographic postcards. When it was captured on 2026-10-30 the portal listed it as **Not solved**, tagged Postcard and HCPortal collection, category Substitution, date 1907-07-06, language Unknown, location Europe, sender Unknown, recipient "W. Abboú", with no transcription or solution attached. The catalogue spelling comes from the writer's "tt" with a bar over it. The text is in English.

The picture side is a printed view, "Houses of Parliament Westminster, London", with no handwriting. The address side has a halfpenny Edward VII stamp and a postmark reading WIMBORNE, 10 PM, day 6, year 07; the month is not clear under the cancel. It is addressed in clear to **Mr W. Abbott, Stokelake Farm, Chudleigh, Devon**. The message stands on the left half of the address side and must be turned 90 degrees anticlockwise to read. The heading "G. H. Saturday" and the date "July 6th 07" are in clear, and 6 July 1907 was indeed a Saturday. The circular disc and building logo over the scan are a modern scanning overlay.

The card belongs to a correspondence of one couple in the same hand, with the same closing formula and the same shift, deciphered in this repository as hcp-1386 to hcp-1407. No person in it has been identified beyond the addressee's name.

![Address side as supplied by the portal (source/address-large.jpg)](../source/address-large.jpg)

![The message turned upright (work/crops/reading.png)](../work/crops/reading.png)

## Method

The transcription is manual: the un-converted scan was rotated, enlarged 2 to 6 times and read sign by sign (no OCR; the portal gives no transcription). The key was taken from the sister cards as a hypothesis and tested here unchanged. It worked at once on the words classed as enciphered. A first pass misread the third row as "Dsjalgu"; closer reading gave signs d and f, hence CRICKET beside MATCH. No sign was changed to fit the key.

Neither CRICKET nor GAUNT occurs on any other solved card in this repository, so these words were not carried over from sister cards.

## Key

Caesar shift: each plaintext letter is written as the next letter of the alphabet. To decipher, subtract one (A becomes Z).

```text
Cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

## Plaintext

| Ciphertext | Plaintext |
|---|---|
| Nz. Pxo. Mpwjoh Cpz | MY. OWN. LOVING BOY |
| Dsjdlfu . Nbudi | CRICKET . MATCH |
| up. Ebz. Hbvou | TO. DAY. GAUNT |
| xpo. M & L. [t?].. | WON. [M & L. [t?]..] |
| Zpvs Pxo. M-h. | YOUR OWN. [M-h.] |
| Hjsm. | GIRL. |

**English:** G. H. Saturday. My own loving boy. Cricket match to-day. Gaunt won. M & L. [t?].. Your own M-h. girl. July 6th 07.

**Slovak:** G. H., sobota. Môj vlastný milujúci chlapec. Dnes kriketový zápas. Gaunt vyhral. M & L. [t?].. Tvoje vlastné M-h. dievča. 6. júla 1907.

"G. H.", "Saturday" and the date are in clear on the card.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1361/work/decode.py
```

The command checks the hashes of the scans, decodes the manual transcription in work/transcription.json, checks the round trip and prints the plaintext and the count of 50 letters. It decodes the transcription, not the image.

## Uncertainties

- **GAUNT.** This is a proper name or side, not confirmed by anything on the card, and no such person or team was identified. The word `Hbvou` is pale at the start. A word-list test (work/gaunt_wordlist.py) finds no competitor: GAINS, GAULT, GAMUT, GALET and GRUNT, and words like COUNT or HAUNT, would need signs that are not on the card. It is not "Abbott" in clear either.
- **`M & L. [t?]..`** Kept literal. The capital has three downstrokes, so M. The signs after L are a dot, a slanted stroke, a detached bar and two dots; t is a weak identification, and it may be a flourish or an exclamation mark. If the group is enciphered, `M & L` shifts to **L. & K.**, the reading accepted on sister card hcp-1395 and read there as "love & kisses". With sister hcp-1368 it could be "L. & K.s". This is an analogy, not a deciphered fact, and treating the group as outside the cipher is itself an assumption.
- **`M-h.`** Kept literal; meaning unknown. The second sign could be h or L. Shifted, it would give L-g. Sister cards have `N-L`, `E-L`, `E. L.` and `M-h` in this place.
- **Pale or doubtful signs.** `up` could be misread as `wp`, and `Ebz` as `Cbz` (BAY), but `up Ebz` is a fixed phrase on the sister cards. Two signs in `Dsjdlfu` look like a and g at first sight; only d and f give a word.
- **Heading.** The first initial is read G (large loop); sister cards vary between C. H. and G. H. Its meaning is unknown.
- **Postmark.** The month is not legible, so July rests on the handwritten date and the portal.
- **Prior publication.** None was found: the portal status is Not solved, and the AI Decipherment Register had no record on 2026-10-30.

## Review summary

Reviewer: a separate Claude Opus 5.5 agent, round 1, verdict **ACCEPT**. The reviewer and the solver are the same model and vendor, so the review is independent in method but not in provider, although the project normally uses a different provider for review. The reviewer ran the command, decoded its own independently typed word list, made its own crops and checked every row sign by sign. It also checked the date, address, postmark and the claims about sister cards. Three minor findings were made, all addressed:

- **Shifted value of `M & L`.** The hypothesis L. & K. and the sister cards are now stated, and the classification of the groups as outside the cipher is called an assumption.
- **Doubt on `t`.** It is now marked `[t?]` in the transcription and the texts.
- **Word test for GAUNT.** It was widened, with each alternative excluded on form.

No decoded letter changed. The reviewer could not verify that a Gaunt played on that day, nor the meaning of the abbreviation groups or the heading.

## Sources

- HC Portal record 1361, all three tabs, captured 2026-10-30: https://crypto.hcportal.eu/dashboard/cryptograms/1361 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/4143/pc_hcp_42_pic.JPG
- Address side: https://api.hcportal.eu/media/4144/pc_hcp_42_adr.JPG
- Sister cards in this repository: hcp-1386 to hcp-1407, hcp-1368, hcp-1369, hcp-1371. Their earlier work is credited on those cards.
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-30.
