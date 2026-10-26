# HCP1450 / pc_hcp_131 — complete main-message candidate

Solver candidate awaiting independent review. This is not an accepted
solution, and several heavy/merged dots require visual review.

## Provenance and scope

Fresh rendered portal status Not solved on 2026-10-26. General,
Description and Attachments read. No attached transcript or solution.
The original picture has four kittens in bed, a handwritten Warrenton,
Mo., May 26, '05 heading and seven rows of Pigpen signs. The ordinary
address names Miss Emma Alwin, New Ulm, Minn.; the portal spells Ema.
The decrypted correspondence is in English although portal language is
Unknown. Sender identity is not established from the final EDW.

The claim covers all 118 Pigpen letters in the seven picture-side rows.
Two ordinary question marks and the cursive word won't are retained,
not counted as encrypted letters. Printed text, date, address, postmarks
and faint address-side pencil strokes/numerals are outside this claim.
The faint pencil marks are not assigned invented words or a key function.

## Key

Nine grid outlines, each containing one, two or three dots. Token names
describe strokes PRESENT, not the direction of the missing opening:
BR bottom/right; B bottom/left/right; BL bottom/left;
R top/bottom/right; C all four; L top/bottom/left;
TR top/right; T top/left/right; TL top/left.

| Outline | 1 dot | 2 dots | 3 dots |
|---|---|---|---|
| BR | A | J | S |
| B | B | K | T |
| BL | C | L | U |
| R | D | M | V |
| C | E | N | W |
| L | F | O | X |
| TR | G | P | Y |
| T | H | Q | Z |
| TL | I | R | unused |

This is the conventional three-count Pigpen layout, applied uniformly.
Unused alphabet entries are completion of the key, not extra observations.

## Literal reading

```text
DEAREST EMMA
WELL SWEETNESS
HOW BE YOU? I DONT THINK
I CAN COME HOME UNTIL
AFTER EXAMINATIONS DR {won't}
EXCUSE US CAN YOU READ
THIS? WITH LOVE DEAREST EDW
```

Braces distinguish ordinary cursive from cipher. DONT is not silently
rewritten in literal output; punctuation beyond the two source question
marks is editorial. HOW BE YOU is retained. DR and EDW are not expanded
into identified names. An idiomatic punctuated reading is: “Dearest Emma,
well, sweetness, how be you? I don't think I can come home until after
examinations. Dr won't excuse us. Can you read this? With love, dearest,
Edw.” The sentence boundaries and interpretation of Dr are editorial.

Slovak sense: „Najdrahšia Emma, nuž, miláčik, ako sa máš? Nemyslím si,
že budem môcť prísť domov skôr než po skúškach. Dr nás neospravedlní.
Dokážeš toto prečítať? S láskou, najdrahšia, Edw.“

## Reproduction

From repository root:

```sh
python3 ciphers/hcp-1450/work/decode.py
```

The command verifies immutable source hashes and decodes all 118 manual
outline/dot tokens from work/transcription.txt, then checks inverse-key
roundtrips. It does not perform OCR. The transcript was manually made from
source/picture.jpg and the saved row crops; roundtrips validate key
application, not independent accuracy of reading the source pixels.

## Evidence and uncertainty

The fixed key gives continuous English across all seven lines. Repeated
letters and words agree in DEAREST/DEAREST, EMMA/HOME/COME, YOU/YOU,
THINK/THIS, UNTIL/US and the closing. The recipient's visible Emma agrees
with the independently decoded salutation, without altering the key.

Some signs are overdrawn, and several dots merge. EXAMINATIONS is the
least clean word: X has heavy upper ink; both A signs have merged blots;
the T outline/count and final S dots need care. The frozen choices are
explicit in the transcript, rather than silently normalized by the
decoder. A second solver helper visually read this word as EXAMINATIONS
and the final signs as EDW from separate crops, but also identified the
same merged-dot uncertainties. This assistance is not a formal review
or acceptance. The initial E of EDW has a broad connected dot that could
be oversegmented; no full writer name is asserted.

Other heavy signs include X in EXCUSE and several W/E/N boxes. Review
must compare their outlines and dot counts with the source. A wrong dot
count can change a letter by nine positions; linguistic coherence alone
does not prove it. The full candidate proposes a reading for every main
cipher glyph, with these visual qualifications.

The public register snapshot contains 110 records, with no exact match
for this source URL or pc_hcp_131. This is not proof of historical novelty.
No published plaintext was consulted. No FINAL, PDF or register entry is
claimed before an independent accepted review.

## Response to review 1

Reviewer: Claude Opus 5.5, verdict ACCEPT (review/REVIEW1.md, 2026-10-26). The reviewer read all 118 Pigpen signs in the seven rows of source/picture.jpg independently, checking the heavy and blotted signs at 7–14×, and decoded them with its own script built from the grid geometry. Its reading agrees with work/transcription.txt in every one of the 118 signs, including the word divisions (the slashes on the card) and the two plain question marks. It found no untranscribed Pigpen; the faint pencil strokes on the address side contain no grid signs or dots. The plaintext is unchanged.

1. The D of DR has an oversized dot; MR as an alternative (minor). Accepted as a disclosed visual uncertainty. In review/work/z5d.png the dot inside the ] outline is one continuous elongated blob, about twice the length of a single dash-dot and running diagonally like the two dots of M in EMMA, so ]1 = D and ]2 = M cannot be separated from the pixels alone. DR remains the reading: a bare title without a name ("Dr won't excuse us") is natural for the head of a school, a bare "Mr" is not, and the single-dot D in row 1 is also dash-shaped (zd_r1.png). The uncertainty list now reads DR (alternative MR, visually possible; IS rejected). The reading is not changed.
2. Confirmation of the other flagged signs (minor). Accepted. The X of EXAMINATIONS and of EXCUSE, both A's of EXAMINATIONS and the E of EDW are heavy blots whose dots cannot be counted, but each outline is clear ([ for X, ┘ for A, □ for E). Every other dot count gives a non-word (EFAMINATIONS, EOCUSE, EJAMINATIONS…), so these readings are fixed by the outline and the word. For the E of EDW, N (NDW) or W (WDW) would be possible in principle; EDW. with its full stop on the card is the usual abbreviation of Edward, so E is the natural reading. No full name is asserted.
3. Postmarks and weekday not recorded (minor). Accepted. The address side carries the cancel WARRENTON MAY 26 … PM 1905 MO. and the receiving mark NEW ULM MINN. MAY 2? 9- 1905 (day not legible), next to a machine RECEIVED cancel. Together with the handwritten heading "Warrenton, Mo. May. 26, '05." they give Friday 26 May 1905 (`datetime.date(1905,5,26).strftime('%A')` → Friday). End-of-term examinations in late May fit the message. These details are in the report; source/metadata.md is unchanged.

Remaining uncertainties carried into the report: who Edw. and Dr were (a college at Warrenton, Mo. would fit "examinations" and "Dr", but this was not checked and the solution does not rely on it); the day on the New Ulm receiving mark; the possible MR for DR and the uncountable dots of the blotted signs; the register snapshot is not proof that no decipherment was published elsewhere.

Closing steps (this response, report, register entry, FINAL) prepared by Claude Opus 5.5 on the solver's behalf at the human's request, 2026-10-26.
