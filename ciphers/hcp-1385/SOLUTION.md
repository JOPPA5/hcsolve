# HCP 1385 / pc_hcp_66 — Caesar −1 postcard to W. Abbott, 21 Nov 1907

**Status: PARTIAL. No marker created.** Every sign is transcribed, but one three-sign group in the body (`yef`?) gives no word and is not resolved. Nothing is restored into it.

## Source
HC Portal 1385, status Not solved, no transcription or solution attached (`source/metadata.md`, `SOURCES.md`). No published solution of this card was found. Picture side: printed "Goodrington Beach, Paignton", no writing. Address side: Mr W. Abbott, Stokelake Farm, Chudleigh, S. Devon; halfpenny stamp, postmark …ORNE 10 PM NO 21 07. Message on the left half, read after rotating 90° counter-clockwise (`work/crops/msg.png`). Plain heading "G. H. Thursday."; plain date "Nov. 21st 1907" (a Thursday, agreeing with the postmark).

## Cipher and key
Caesar: each plaintext letter is written as the next letter (decrypt −1). Same hand and key as the W. Abbott cards hcp-1386…1407.

## Transcription and reading
| Ciphertext | Plaintext |
|---|---|
| Nz. Pxo. E. L. Cpz. | MY. OWN. [E. L.] BOY. |
| Wfsz. xfu. ojhiu | VERY. WET. NIGHT |
| yef(?). Nz. N. & L. | {XDE — unresolved}. MY. [N. & L.] |
| gspn. zpvs Pxo. | FROM. YOUR OWN. |
| E. L. Hjsm. | [E. L.] GIRL. |

English: "G. H., Thursday. My own E. L. boy, very wet night {unread}. My N. & L. from your own E. L. girl. Nov. 21st 1907."

Slovak: „G. H., štvrtok. Môj vlastný E. L. chlapec, veľmi daždivá noc {neprečítané}. Moje N. & L. od tvojho vlastného E. L. dievčaťa. 21. nov. 1907."

## Command (repo root)
```sh
python3 -I ciphers/hcp-1385/work/decode.py
```
Checks source hashes, decodes `work/transcription.json`, checks the round trip and the weekday, prints the reading and letter counts. The transcription is manual.

## Uncertainties
1. **Blocking: the group at the start of row 3** (`work/crops/w4.png`). Sign 1 looks like a cursive y with a closed looped descender; sign 2 is ε-shaped, like this writer's capital E, with a thin tail joining sign 3; sign 3 is an f with a closed foot loop (same form as word-final f in `xsjuf` on hcp-1403). Literal value XDE is no word. Tried and not supported by the pixels: `xfe` = WED (the natural sense, last night being Wednesday, but it needs f before e and an ordinary x; the x in `xfu` on this card is a plain cross); `zfu` = YET, `Zft` = YES, `czf` = BYE; `y & y` = kisses (sign 3 lacks a y head, and the `&` on this card has another form). It may be an abbreviation, but nothing shows that.
2. **Smudged `Nz` in row 3** (`work/crops/smudge.png`): the ink is flaked; the N stem and fragments of the z survive. Read from the traces and the fixed formula `Nz. N. & L. gspn`; treat as a disclosed restoration of a damaged sign.
3. **`ojhiu`**: after h there are two minims, then the i-dot stands above the last one, right of its expected place. Read as i + this writer's uncrossed t (cf. `up-ojhiu` on hcp-1403); no other word fits.
4. **`E. L.`, `N. & L.`** kept literal, as on the sister cards; meaning and whether they are shifted are undecided.
5. Heading initial G or C (as on hcp-1386/1397). Row 4 `Pxo` is faint but legible; its large P flourish spans row 4.

## Credit
All work on this card: Claude Opus 5.5 as solver, 2026-10-30. Sister cards consulted for hand and key only.
