# HCP 1422 (pc_hcp_103): a cipher postcard from Ivy to Carl Wieler, Mt. Carmel, Illinois

Human solver: Tomáš Pavuk

**Status: deciphered in full (374 of 376 cipher signs read from the scan, 2 restored under the postal cancellation); independent review 1 verdict ACCEPT, no change to the decoded letters.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1422 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1422), portal name pc_hcp_103, part of the HCPortal collection of cryptographic postcards (private collection). When it was captured on 2026-10-26 the portal listed it as **Not solved**, category Substitution, date 1943-02-08, language Unknown, location North America, sender Unknown, recipient Carl Wieler, with no transcription or solution attached.

The cipher text fills the message half of the address side: eighteen lines of small invented symbols, with each word marked by an overline. The other half carries the address to Carl Wieler at **Mt. Carmel, Illinois**, a green 1-cent Washington stamp and a cancellation **MT CARMEL ... FEB 8**. The cancellation crosses lines 3 and 4 of the cipher text and hides parts of two words. The picture side, a hand-painted pansy with a ribbon, carries no cipher.

![Address side with the cipher text on the left and the MT CARMEL cancellation over its upper lines (source/address.jpg)](../source/address.jpg)

![Picture side: hand-painted pansy, no cipher text (source/picture.jpg)](../source/picture.jpg)

**Date.** The portal gives 1943-02-08. The month and day (FEB 8) are clear on the cancellation; the year digits are faint and lie under the pen writing. On a 7-8x enlargement a stamped 9, 1 and 3 can be seen after a first digit lost under ink, i.e. probably **1913**. That fits the stamp, a 1-cent green Washington of the 1908-1922 design, and argues against 1943, when a different 1-cent stamp was current. February 8, 1913 was a Saturday. The year is a reading of a faint postmark, not a certainty.

## Method

The transcription is **manual**: each of the 376 signs was read from enlargements of the address-side scan and written as an ASCII label for its shape in work/transcript_v2.txt, with " / " separating the overlined word groups. No OCR was used and the portal supplied no transcription.

The symbol set is small (22 shapes) and the word divisions are marked, so the cipher is a plain monoalphabetic substitution of English. The key was built from repeated words: the frequent group chevron-circle-backslash is YOU, and the pair COULD / WOULD (two parallel strokes vs zigzag before O-backslash-cup-plus) separated C from W; the dot signs (two dots A, one dot G, dot above the stroke H, dot below I) followed from AM, GOING, HOW and IS. The key was then checked on the whole card. It decodes every visible sign into fluent English, with no unknown or unused sign and no shape mapped to two letters.

Two words lie partly under the cancellation:

- **SAT[U]RDAY (line 3).** Under the stamped "FEB 8" the pen signs S (over the F), A (two dots inside the E), T (a cross over the B), R (a comma stroke right of the 8) and D-A-Y are visible; the U position is covered by the stamped 8. SAT_RDAY admits only U, and SATURDAY is written twice more on the card in clear.
- **[H]ER (line 4).** After FROM, the time line of the cancellation crosses the word. A vertical pen stroke, the hash-shaped E and the 4-shaped R are visible, matching HER as written in clear on line 9; whether the stroke has the dot above that makes it H (rather than the dot below that makes it I) cannot be seen. Only H gives a word.

Both restorations are marked with square brackets in the plaintext.

The work was done in two stages. An earlier session of the OpenAI GPT solver (GPT-6 Astra, 2026-10-26) set up the record, made the first transcript and recovered the key, but left the two postmark spans open. Claude Opus 5.5 (2026-10-29/30) re-checked every line on enlarged crops, read the two postmark spans, corrected one omission (the word IN before CYNTHIANA on line 9, which the first transcript had taken as a comma) and added two punctuation marks.

## Key

Simple monoalphabetic substitution with invented symbols. The labels are ASCII names for the drawn shapes, not exact reproductions.

| Shape | Label | Plain | Shape | Label | Plain |
|---|---|---|---|---|---|
| two dots side by side | `:` | A | dash with dot above and below (÷) | `=` | M |
| curved 2-like stroke, flat foot | `2` | B | dash followed by a dot | `-.` | N |
| two parallel strokes | `//` | C | circle | `O` | O |
| short plus | `+` | D | loop with stem | `p` | P |
| hash (sometimes π-like) | `#` | E | comma-shaped stroke | `,` | R |
| low wavy m-shaped stroke | `~` | F | v-shaped stroke | `v` | S |
| single dot | `.` | G | long cross | `t` | T |
| stroke with dot above | `i` | H | backslash | `\` | U |
| stroke with dot below | `!` | I | caret | `^` | V |
| 2-like stroke ending in a v-hook | `n` | K | zigzag | `N` | W |
| cup with dot | `u` | L | chevron | `>` | Y |

J, Q, X and Z do not occur. Two pairs are easily confused: B and K are both 2-like (B has a flat foot, K ends in an upward hook), and H and I differ only in whether the dot is above or below the stroke. The R sign has the same shape as the writer's comma; a comma-shape is taken as punctuation only where it stands outside a word.

## Plaintext

As decoded, line by line of the card. `[ ]` marks the two restored letters. The punctuation marks `?`, `/`, `,` and `.` are the solver's readings of pen marks standing outside the words, not cipher letters; the `/` after COMING (a separator of uncertain kind) and the stop at the end of line 4 are guesses.

```text
WELL KID HOW IS YOUR
COLD ? HOPE IT IS BETTER
I AM NOT GOING HOME SAT[U]RDAY
AS I HAD A LETTER FROM [H]ER .
AND SHE IS COMING / IF YOU ARE
ABLE , WOULD LIKE TO HAVE YOU BE
IN MT . CARMEL SATURDAY
NIGHT I AM GOING TO MEET
HER IN CYNTHIANA I WOULD
LIKE TO SEE YOU BEFORE THEN
IF YOU COULD COME TO THE
DEPOT I HAVE SOME THING TO TELL
YOU , I HAV SOMETHING REAL
CANADISH FOR YOU IF I DONT
GET TO SEE YOU BEFORE SATURDAY
BE SURE AND BE AT THE CITY
WHEN WE ARRIVE OR ELSE MEET US
AT SKELTON LOVINGLY IVY
```

Normalised English (punctuation and the apostrophe in "don't" are editorial; HAV is kept as written):

**Well kid, how is your cold? Hope it is better. I am not going home Saturday, as I had a letter from her, and she is coming. If you are able, would like to have you be in Mt. Carmel Saturday night. I am going to meet her in Cynthiana. I would like to see you before then; if you could come to the depot, I have something to tell you. I hav[e] something real "Canadish" for you. If I don't get to see you before Saturday, be sure and be at the city when we arrive, or else meet us at Skelton. Lovingly, Ivy.**

Slovak translation (the feminine forms follow the name Ivy; the writer's gender is not stated):

**No, drobec, ako je s tvojou nádchou? Dúfam, že je lepšie. V sobotu nejdem domov, lebo som dostala list od nej a ona prichádza. Ak budeš môcť, chcela by som, aby si bol v sobotu večer v Mt. Carmel. Idem sa s ňou stretnúť v Cynthiane. Rada by som ťa videla ešte predtým; keby si mohol prísť na stanicu, mám ti niečo povedať. Mám pre teba niečo naozaj „kanadské“ [CANADISH]. Ak sa s tebou neuvidím pred sobotou, určite buď v meste, keď prídeme, alebo nás stretni v Skeltone. S láskou Ivy.**

Notes on the reading:

- **Places.** Mt. Carmel, Illinois, is the address on the card and the town of the cancellation. Cynthiana is a small town in Posey County, Indiana, across the Wabash about 30 miles from Mt. Carmel. "The depot" is the railway station and "the city" presumably a larger town nearby.
- **HAV** (line 13) has no E on the card; it is a writer's omission. HAVE is written in full twice elsewhere.
- **CANADISH** (line 14) is clearly written C-A-N-A-D-I-S-H. Its meaning is unexplained, perhaps a jocular "Canadian-ish" thing. It is not a decoding error and is not altered.
- **SKELTON** (line 18) is clearly S-K-E-L-T-O-N, with K in the same hooked form as in KID and LIKE. It is probably a local place or station near Mt. Carmel or Cynthiana where Carl could meet the travellers; it has not been identified and is not normalised to another name.
- **Ivy** is the signature; who Ivy is, and who "her" is, is not known.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1422/work/decode_v2.py
```

The script uses only the Python standard library and writes no files. It checks the SHA-256 hashes of the files in source/, decodes the manual transcript work/transcript_v2.txt with the key in work/key.json (checking that no plain letter is assigned twice), prints the eighteen lines above and ends with `# 374 glyphs read from the scan, 2 restored under the postmark; 22 key classes; source hashes OK`. It does not read the image; the transcription step is manual and was checked independently in review.

## Uncertainties

- **Two restored letters** under the cancellation: the U of SAT[U]RDAY (line 3) and the H of [H]ER (line 4). Each is forced by the visible neighbours and by clear occurrences of the same word elsewhere on the card.
- **Punctuation** is the solver's interpretation of pen marks outside words; the `/` after COMING and the stop at the end of line 4 are guesses. None changes the reading.
- **Small signs.** The scan is only 1024 px wide and some distinguishing dots (H vs I) are 2-3 px; readings were confirmed by consistency across repeated words.
- **CANADISH** and **SKELTON** are read with certainty but not explained (see above).
- **Date.** Year probably 1913 from the postmark and the stamp; the portal's 1943 is very likely wrong, but the first year digit is not visible.
- **People.** The identity of Ivy and of "her" is unknown; Carl Wieler is known only from the address.
- No search for a prior publication of this card was made beyond the portal status (Not solved, no attached solution, 2026-10-26) and the AI Decipherment Register (no entry for this card, checked 2026-10-29).

## Review summary

Reviewer: a separate Claude Opus 5.5 agent (Anthropic), round 1, verdict **ACCEPT**. The reviewer ran the reproduction command (output identical to the claimed plaintext), decoded the transcript with its own script and a key retyped from the solution table (identical output, all 22 key classes used, none twice), and checked all eighteen lines glyph by glyph on its own enlargements of the scan. It confirmed the inserted word IN on line 9, the K/B distinction (KID, LIKE, SKELTON vs BETTER, BE, BEFORE), and both postmark restorations, and found the English fluent and consistent with the places on the card. Its three findings were minor and are reflected in this report:

- **Postmark year.** The reviewer read the year digits as ...913; the solver confirmed this on the same enlargement, and the date is now given as probably 1913 rather than left open.
- **Punctuation.** The report now says that punctuation marks are readings of pen marks, not cipher letters.
- **CANADISH and SKELTON.** The report now explains that both are written so on the card and that Skelton is probably an unidentified local place.

No decoded letter changed as a result of the review.

## Sources

- HC Portal record 1422, General, Description and Attachments tabs, captured 2026-10-26: https://crypto.hcportal.eu/dashboard/cryptograms/1422 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/4326/conversions/pc_hcp_103_pic-large.jpg (source/picture.jpg).
- Address side: https://api.hcportal.eu/media/4327/conversions/pc_hcp_103_adr-large.jpg (source/address.jpg).
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-29.
