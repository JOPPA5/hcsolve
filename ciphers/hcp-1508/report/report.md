# HCP 1508 (pc_hcp_189): an English courting note to Miss Leah Doane, June 1913

Human solver: Tomáš Pavuk

**Status: deciphered (200 of 201 numeral signs mapped; the one unmapped sign is a `2` in the signature). Independent review 1 verdict ACCEPT; its four minor findings changed descriptions and disclosures only, not the decoded text.** Report dated 2026-10-29.

## Origin and context

The cryptogram is record 1508 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1508), portal name pc_hcp_189, part of the HCPortal collection of cryptographic postcards (private collection). When it was captured on 2026-10-26 the portal listed it as **Not solved**, category Substitution / Monoalphabetic, date 1913-06-13, language Unknown, location North America, sender Unknown, recipient "Leeah Doane", with no transcription or solution attached.

The address side is written to **Miss Leah Doane, Little Marsh, Pa.** and carries a green one-cent U.S. stamp and a postmark **KNOXVILLE JUN 13 1913 PA** (Knoxville and Little Marsh are neighbouring places in Tioga County, Pennsylvania). The message on the left half of the address side is written almost entirely as dot-separated numbers in dash-separated words, with a few plain cursive words (*morning*, *Sat.*, *disappointed*, *you*). The picture side is a printed comic card in mock-Dutch dialect, "LUF IS A GOOT TING TO GET INTO YOUR SYSTEM"; it carries no cipher.

Two other cards to the same recipient from the same year, HCP 1506 and HCP 1507, are deciphered in this repository and use the same number key.

![Address side: numeric message at the left, address to Miss Leah Doane, Little Marsh, Pa., Knoxville postmark of 13 June 1913 (source/address-large.jpg)](../source/address-large.jpg)

![Picture side: printed comic card, no cipher (source/picture-large.jpg)](../source/picture-large.jpg)

**Credits.** The capture of the portal page and scans, the first transcription and most of the key were done by the OpenAI GPT solver (GPT-6 Astra / GPT-6.1 Sol) on 2026-10-26/27. On 2026-10-29 Claude Opus 5.5 re-read every sign on enlarged crops, corrected five readings, aligned the key with the companion cards and completed the decipherment. An independent Claude Opus 5.5 reviewer checked the result.

## Method

The transcription is **manual**: each row was read sign by sign from enlarged (3-4x), contrast-stretched crops of the address-side scan and recorded in a plain-text transcription, with letter-shaped signs and plain cursive words marked separately. No OCR was used.

The cipher is a simple substitution of numbers for letters. Word patterns and obvious cribs (MY DEAR GIRL at the start, the kisses XX before the signature, THE, WHEN, LOOK, PLACE) give the key quickly, and it turned out to be identical to the key of the companion cards HCP 1506 and 1507. The key was then applied to the whole card without change; every word comes out as English except one evident writer's slip.

In the re-reading of 2026-10-29 the following earlier readings were corrected on the pixels (none by changing the key):

- line 4: `15.23` → `15.25` (the stroke taken as the upper bow of a 3 is the descender of the *g* of *morning*);
- lines 6 and 13: the K sign is **14** (curved 1 + cursive 4), not 2, as in hcp-1507's LOOK `6.7.7.14`;
- line 8: the last sign of BELL is 6, not 8;
- line 11: `4.12` (RA) → `4.17` (RI), giving RI|NG = RING;
- line 14: `17.11` (IF) → `18.7` (DO);
- signature: EKRA → E[2]RA (the `2` there is an ordinary 2, not the K sign).

![Enlarged control crops of every changed or doubtful sign (work/controls-v2.png)](../work/controls-v2.png)

## Key

Monoalphabetic substitution, number → letter:

| No. | 1 | 3 | 4 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Letter | M | E | R | L | O | T | P | S | F | A | G | K |

| No. | 15 | 16 | 17 | 18 | 20 | 21 | 22 | 24 | 25 | 26 | (5) | 2 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Letter | B | U | I | D | C | W | H | X | N | Y | (V) | unknown |

Every numeral value in the table except 5 is attested on this card. 5=V is the value from HCP 1506; on this card V is written three times as a V-shaped letter sign instead. One N (in WINDOW) and one I (in I AM) are also written as letter-like signs. The number 2 occurs once, in the signature, and has no established value.

Count: 201 numeral signs, of which 200 map through the key and 1 (`2`) does not, plus 5 letter-shaped signs; the plain cursive words are not counted.

## Plaintext

Literal decoder output, line by line as on the card (lower case = plain cursive words on the card; [2] = unmapped number):

```text
MY DEAR GIRL
I FELT AWFUL
THIS morning WHEN
I WENT BN TO FIND
THAT YOU DID
NOT LOOK OUT THE
WINDOW I RUNG
THE BELL ALL THE
WAY TO YOUR
PLACE BUT DID
NOT WANT TO RI
NG IT TOO LOUD
TO AWAKEN MY
DEAR DO YOU
WANT ME TO STOP
Sat. EVE IAM VERY
SORRY I disappointed
you LAST NIGHT
EVER YOUR FRIEND
XX E[2]RA
```

Normalised English (punctuation editorial; BN read as BY):

**My dear girl, I felt awful this morning when I went by to find that you did not look out the window. I rung the bell all the way to your place but did not want to ring it too loud to awaken my dear. Do you want me to stop Sat[urday] eve? I am very sorry I disappointed you last night. Ever your friend, XX [kisses], E?ra [probably Ezra].**

The bell is presumably a buggy or sleigh bell rung while driving past her house.

Slovak translation: **Moje drahé dievča, dnes ráno mi bolo hrozne, keď som šiel okolo a zistil som, že si sa nepozrela z okna. Zvonil som zvončekom celou cestou k tebe, ale nechcel som zvoniť príliš nahlas, aby som nezobudil svoju drahú. Chceš, aby som sa zastavil v sobotu večer? Veľmi ma mrzí, že som ťa včera večer sklamal. Navždy tvoj priateľ, XX [bozky], E?ra [asi Ezra].**

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1508/work/decode2.py
```

The script uses only the Python standard library. It checks the SHA-256 hashes of the three files in source/, decodes the manual transcription in work/transcription-v2.txt with the key above, and prints the twenty literal lines and the counts `numeral signs: 201, mapped: 200, unmapped: 1; non-numeral letter signs: 5`. Its output is identical to work/plaintext-v2.txt. The control crops are regenerated by work/controls-v2.py (needs Pillow).

## Uncertainties

- **BN for BY (line 4).** The sign after 15 has the writer's 5 form, exactly as in WENT's 25 on the same line, so the card literally reads BN; the sentence requires BY (15.26). Treated as a writer's slip and kept literal in the output.
- **Signature E[2]RA.** The `2` occurs nowhere else; of the letters not used by the key (J, Q, Z), Z gives the most plausible name, EZRA. But on HCP 1506 the same writer wrote a lone `2` where `26` was meant, so this `2` may be a truncated number rather than a key value. No 2=Z entry is put into the key, and the sender's identity is not established.
- **The I of I AM.** Before `12.1` (AM) on the watermark band stands a small closed loop on a faint stem, which looks rather like a small 9. As 9 (P) the word would be PAM, not a word; the loop may also be stray ink. I AM rests on the context ("I am very sorry I disappointed you"), not on the shape.
- **Letter-shaped signs.** The V of EVE, VERY and EVER is written as a V/Y-shaped letter, not as the numeral 5; the N of WINDOW as a letter-like N. Each decodes to the same letter either way.
- **BELL.** The last sign crosses a grey watermark band; its visible stem and lower loop give 6, not 8.
- **RUNG / RING** are as written. The cursive word is normalised as *disappointed*; on the scan it looks closer to "dissapointed". It is plain text, not cipher.
- The lives of the sender and recipient beyond the three cards were not researched. No published reading of this card was found: the portal status was Not solved, and the AI Decipherment Register (checked 2026-10-29) has no entry for it.

## Review summary

Reviewer: Claude Opus 5.5 (Anthropic), a separate agent, round 1, verdict **ACCEPT**. The reviewer ran the reproduction command (output byte-identical to the stated plaintext), then made its own crops, typed its own transcription and derived the key independently from twelve cribs (MY, DEAR, GIRL, THE, LOOK, PLACE, BUT, XX, FELT, AWFUL, WHEN, STOP). Its key was one-to-one, agreed with the solver's in all 22 values and with the companion cards, and gave the same text word for word over all 201 numeral signs. It confirmed the corrections BN (25), the K sign 14, RING, DO and BELL on the scan, and judged the text to be idiomatic American English of 1913 fitting the postmark and the address. Its four minor findings were addressed without changing the decoded text:

- **The I of I AM.** It had been described as a single faint stroke; it is a small 9-like loop. The description now says so and names the PAM and stray-ink alternatives; the control crop was enlarged to show the sign.
- **Signature.** The possibility that the `2` is a truncated `26` (as on HCP 1506) is now disclosed, and "only Z gives a name" was softened to "Z gives the most plausible name".
- **Wording.** An inconsistent statement about which key values are attested on this card was harmonised (all except 5).
- **Spelling.** The cursive word looks like "dissapointed" on the scan; this is now noted.
