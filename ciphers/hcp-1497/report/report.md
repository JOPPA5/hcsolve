# HCP 1497 / pc_hcp_178 - mixed cursive and Pigpen postcard

## Origin and revised scope

The HC Portal General, Description and Attachments tabs were inspected on
2026-10-26. The card was Not solved, tagged Pigpen and Postcard HCPortal
collection, classified Substitution / Monoalphabetic. The catalogue date is
1904-11-22, location Europe, recipient E. R. Mobsby, sender and language
Unknown. Neither a transcription nor a solution was attached. Both original
scans and the contemporaneous metadata remain unchanged in `source/`;
acquisition URLs are recorded in `SOURCES.md`.

The handwritten address reads **Mr E. R. Mobsby, 9 Carden Road, Peckham,
S.E.** This corrects the initial provisional street reading “Ewerdon” retained
in the immutable metadata capture. The ordinary closing reads Maud. These
names do not establish the correspondents' historical identities. The
picture caption is Dulwich Park; no encrypted writing is observed there.
The postmark is compatible with November 1904, but its day is not independently
legible; 1904-11-22 is catalogue metadata, not a newly read cancellation date.

The revised transcript covers **152 cipher positions in 33 word units**.
Two positions retain explicit shape alternatives. Cancelled ink and ordinary
cursive are documented separately and excluded from that count.

## Key and method

A standard interleaved Pigpen substitution is used consistently. Token names
refer to the strokes present, not to the opening of a cell. The reviewer
independently reconstructed the same key and checked the scan word by word.

| Outline / token | Undotted 0 | Dotted 1 |
|---|---|---|
| bottom/right BR | A | B |
| bottom/left/right B | C | D |
| bottom/left BL | E | F |
| top/bottom/right R | G | H |
| four sides C | I | J |
| top/bottom/left L | K | L |
| top/right TR | M | N |
| top/left/right T | O | P |
| top/left TL | Q | R |
| downward wedge V | S | T |
| right wedge > | U | V |
| left wedge < | W | X |
| upward wedge ^ | Y | Z |

Unused entries complete the conventional alphabet; they do not demonstrate
additional letters on this card. Cipher words are interspersed in ordinary
English handwriting. Repeated words and shapes support the fixed table;
context helps interpret weak signs but cannot prove hidden strokes.

## Decoded cipher words

Body, from “Thanks for P.C.” downward:

```text
BEEN / ABLE / SEE / YOU / WELL / DR / EYE / COME / OUT / TIRED /
WAITING / DARLING / LONELY / SEND / HALF / LETTER / YOU
```

Continuation across the top:

```text
MANAGE / DEAR / WAIT / YOU / NEXT
```

Closing:

```text
YOUR / EVER / LOVING / GIRL
```

Postscript:

```text
ABSEN[S/C]E / HEART / FONDER / [D/H/L]EAR / MY / DARLING / SWEETHEART
```

ABSENSE is the preferred as-seen reading: the sixth sign is V-shaped like S,
although a C/flat-bottomed-cell reading cannot be excluded at this resolution.
ABSENCE is the intended ordinary word, not a silently substituted raw reading.
The PS address word probably means DEAR; its first dotted cell is obscured by
cursive “you”, leaving D/H/L alternatives. EAR is secure. The clear DEAR in
the top continuation is a different occurrence.

## Complete mixed-text reading

This is a best-effort diplomatic reading of the ordinary handwriting combined
with the revised cipher words. Uppercase words are cipher; ordinary case is
already readable cursive. Physical wrapping is mostly retained; brackets
mark doubtful handwriting or cipher alternatives. Punctuation is lightly
spaced for readability. It is not all newly deciphered text.

```text
Thanks for P.C. am so sorry
I have not written or BEEN
ABLE to SEE YOU before, but
I am not at all WELL, had
to go to the DR Monday
evening to have my EYE
seen to, the same as last
time, but I am sorry to say
it is not much better today,
but I shall COME OUT as soon
as possible, so please do not get
TIRED of WAITING DARLING,
Now I am afraid as I am so
LONELY, I must ask you once
more if you will SEND me the
other HALF of my LETTER by the 9.15
post in Dulwich
Wednesday if YOU cannot

MANAGE it DEAR, well then I will ask you to WAIT until I see YOU,
[cancelled N followed by inked-over signs]
NEXT time, which I hope will be Thursday or Friday. Nellie
wishes me to tell you she will be writing you both soon.
[&?] will you please also tell Standly[?] I will answer his
as soon as I can.

YOUR EVER LOVING GIRL
Maud.

P.S. ABSEN[S/C]E makes the HEART grow FONDER
I wonder if it is so with you [D/H/L]EAR.
MY DARLING SWEETHEART.
```

The name Standly and initial connective before “will you please” are uncertain
ordinary handwriting, not cipher-key uncertainties. The upward wedge-like
stroke between Wednesday and if belongs to the descender of the ordinary h
in Dulwich; it is not an extra Y. The cancelled dotted N and blot after YOU
are excluded from the 152 live cipher positions, with NEXT restarted on the
next line. Decipherment does not recover unreadable cancelled content.

## Slovak translation

The following translates the intended sense of the complete mixed text,
including the ordinary handwriting. It retains the unresolved name and marks
the uncertain PS address word; ABSEN[S/C]E is translated by its intended meaning.

„Ďakujem za pohľadnicu. Veľmi ma mrzí, že som nenapísala ani ťa predtým
nemohla vidieť. Vôbec sa necítim dobre; v pondelok večer som musela ísť
k lekárovi, aby mi pozrel oko, tak ako minule. Žiaľ, dnes to nie je oveľa
lepšie. Vyjdem však von hneď, ako to bude možné, preto sa, miláčik, neunav
čakaním. Keďže som taká osamelá, musím ťa ešte raz poprosiť, či by si mi
poslal druhú polovicu môjho listu stredajšou poštou o 9.15 v Dulwichi.
Ak to, drahý, nemôžeš zariadiť, poprosím ťa, aby si počkal, kým sa nabudúce
uvidíme; dúfam, že to bude vo štvrtok alebo v piatok. Nellie ti odkazuje,
že vám obom čoskoro napíše. Prosím, povedz aj Standlymu [meno neisté],
že mu odpoviem hneď, ako budem môcť.

Tvoje stále milujúce dievča, Maud.

P.S. Neprítomnosť posilňuje lásku. Zaujímalo by ma, či je to tak aj u teba,
[drahý - prvý znak neistý]. Môj najdrahší miláčik.“

Feminine grammar follows the literal GIRL and the apparent Maud signature;
it does not identify a historical person. The reference to an eye problem
is the writer's account, not a medical conclusion.

## Reproduction and evidential limits

From repository root:

```sh
python3 ciphers/hcp-1497/work/decode.py
```

The script checks original source hashes and decodes the own manual
sign-by-sign transcript in `work/transcription.txt`, preserving `V0/B0` and
`B1/R1/L1` alternatives. It emits all 152 positions and 33 word units; output
is saved as `work/plaintext.txt`. The portal supplied no transcript. This is
not OCR. A token round trip does not independently validate the image; the
independent visual comparison is documented in review 1 and was rechecked
by the solver against the original and the cited crops.

Other weak but compatible dots include D in FONDER and F in HALF. EYE's
middle wedge is crossed by the y of ordinary Monday. These readings are
retained with that visual limitation, not represented as high-resolution proof.
No published solution was used. The stored register check records no exact
URL/name match at capture time; it is not a claim of historical priority.

## Response to review 1

Reviewer: Claude Opus 5.5, 2026-10-26, verdict **REVISE**. The fixed key stands.
The reviewer explicitly stated that exact local corrections require no further
full review round. All six findings are addressed as follows.

1. **Body LOVING → WAITING - corrected.** `review/work/z_waiting.png` and
   the source show seven signs, `<0 BR0 C0 V1 C0 TR1 R0`, not the six-sign
   LOVING previously entered. Replaced only this body occurrence; the closing
   YOUR EVER LOVING GIRL remains unchanged. Raw tokens, decoded list, mixed
   reading and translation now correctly say “tired of waiting”.
2. **Missing PS word - added with uncertainty.** The lower word beneath HEART
   in `review/work/z_ps_dear.png` is entered `B1/R1/L1 BL0 BR0 TL1`:
   [D/H/L]EAR, probably DEAR. No unseen first outline is forced. With WAITING's
   extra sign, this raises coverage from 147/32 to 152 positions/33 words.
3. **ABSENCE sixth sign - recorded as seen.** `z_ps1b.png` and `z_ps1c.png`
   show a V-like sixth sign. The transcript now uses `V0/B0`, emitting
   ABSEN[S/C]E, with S preferred visually. Intended ABSENCE is only editorial.
4. **Cancelled ink and stray stroke - documented.** Dotted N plus over-inked
   start after top-line YOU is recorded as cancelled, not counted. The
   Wednesday/if wedge is identified as the ordinary Dulwich h descender,
   consistent with `z_struck.png` and `z_wed.png`; no extra cipher letter added.
5. **Address and identities - corrected and bounded.** `z_address.png` reads
   9 Carden Road. This report and SOLUTION correct the provisional Ewerdon
   reading; immutable `source/metadata.md` is intentionally not overwritten.
   The review notes matching names/address/context on HCP 1498, useful as
   companion-card context but not identification of the persons historically.
6. **Mixed-text scope - expanded.** Replaced the elided summary by a complete
   best-effort diplomatic mixed reading above, marking doubtful ordinary
   connective/name and both cipher alternatives. Reproduction limits remain
   explicit. `work/revision-annotations.json` indexes the corrections and crops;
   `work/plaintext.txt` has been regenerated from the corrected tokens.

