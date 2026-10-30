# HCP 1401 / pc_hcp_82 — Caesar (+1) New Year postcard, 30 Dec 1907

Status: **whole message read; handed to review (DONE1).** It is a very short message (a closing formula). One abbreviation, `E. L.`, is kept literal, exactly as on the sister card hcp-1386.

## Origin

HC Portal cryptogram 1401 (`pc_hcp_82`), portal status *Not solved*, no attached transcription or solution (`SOURCES.md`, `source/metadata.md`). Portal date 1907-12-30; 30 Dec 1907 was a Monday, matching the plain heading "C. H. Monday". Picture side: printed Tuck "Oilette" view *Bickleigh Vale, South Devon* with the printed greeting "A Bright and Happy New Year to you"; no handwriting. Address side: penny Edward VII stamp, addressed to Mr W. Abbott, [farm name uncertain], Chudleigh, Devon (portal spells "W. Abboú"; metadata left unchanged). The message is on the address side (rotate 270° clockwise). The card belongs to the Abbott correspondence in Caesar +1 (hcp-1386…1407). No published solution of this card was found or used.

## Cipher and key

Caesar shift: each plaintext letter is written as the next letter of the alphabet; decrypt by subtracting one (A→Z).

```
Cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

Heading "C. H. Monday" is ordinary writing, not enciphered. `E. L.` is an abbreviation kept literal (shifted value would be D. K.), as on hcp-1386 ("My own E. L. boy … from your own E. L. girl").

## Transcription and plaintext (all ciphertext on the card)

| Ciphertext | Plaintext |
|---|---|
| gspn. Zpvs. | FROM. YOUR. |
| Pxo. E. L. | OWN. [E. L.] |
| Hjsm ' | GIRL ' |

15 enciphered letters, all decoded by the one key; 2 abbreviation letters kept literal.

- English: *"From your own E. L. girl."*
- Slovak: *„Od tvojho vlastného E. L. dievčaťa."*

(English is the plaintext language; the portal lists Unknown.)

## Command (from the repo root)

```sh
python3 -I ciphers/hcp-1401/work/v2/decode.py
```

Checks the SHA-256 of the three files in `source/`, decodes every token of `work/v2/transcription.json`, checks the round trip and the letter counts, and prints the plaintext above. (`work/decode.py` and `work/transcription.json` are the earlier partial version, kept for history.)

## Uncertainties

1. **Second letter of `E. L.`** The earlier partial reading left it as h/l/1. Enlarged (`work/c2/eh.png`, `work/c2/line2.png`) it is a single rising slanted stroke from a small closed loop at its foot, followed by a dot — the same construction as the writer's capital L in `E. L.` and `N. & L.` on hcp-1386 (`ciphers/hcp-1386/work/crops/band5.png`, `band6.png`), not a lowercase h (no separate arch/second stem). Read as L. Its meaning (e.g. "ever loving") is not established; it is kept literal, and whether it is shifted is undecided.
2. Small detached wedge after `Hjsm` (`work/c2/tail.png`): a pen mark, apostrophe/comma-like; carries no letter and is not interpreted.
3. Heading initial C or G (sister cards differ); not enciphered. Farm name in the address not established.
4. Message is short; the key rests on four words here plus the many accepted sister cards with the same key and the same formula.

## Why it is correct

One fixed shift turns every enciphered token into English (15/15 letters: FROM YOUR OWN GIRL), the exact closing formula of accepted sister cards (hcp-1397 "Your own girl", hcp-1386 "from your own E. L. girl"). Date, weekday and New Year greeting are consistent.

## Credits

Download, metadata, key identification and a 16-letter partial reading with one unresolved sign: OpenAI GPT solver (GPT-6 Astra / GPT-6.1 Sol), 2026-10-26. Re-inspection from the pixels, resolution of the sign as `L` by comparison with hcp-1386, new transcription and decoder: Claude Opus 5.5 acting as solver, 2026-10-29.

## Response to review 1

Review 1 (Claude Opus 5.5, separate agent), verdict **ACCEPT**, three minor findings. No decoded letter changes.

1. **Farm name (minor) — fixed.** Rechecked on `source/address.jpg` and the reviewer's crop `review/work/addr_farm.png`: the second address line reads clearly **Stokelake Farm**, as on sister cards hcp-1388, 1397, 1402, 1403. The address is therefore Mr W. Abbott, Stokelake Farm, Chudleigh, Devon. The statement "farm name not established" in Origin and Uncertainty 3 is superseded. Not part of the cipher.
2. **Postmark (minor) — fixed.** The cancellation over the red ONE PENNY Edward VII stamp reads "…MBORN[E] / 10 PM / DE 30 / 07" (Wimborne), visible on `source/address.jpg`. It confirms the portal date 30 Dec 1907 (a Monday, matching the heading "Monday") and the Wimborne origin shared with the sister cards. Now named in the report.
3. **L reading rests partly on family comparison (minor) — agreed, no change.** On this card the foot of the L is a blotted ink mass; the identification relies also on the identical formula "Pxo. E. L. Hjsm" on hcp-1386 (and hcp-1404). This is disclosed in Uncertainty 1 and in the report.

Re-run after the response (repo root): `python3 -I ciphers/hcp-1401/work/v2/decode.py` → "source hashes OK", `FROM. YOUR. / OWN. [E. L.] / GIRL '`, 15 enciphered letters decoded, 2 abbreviation letters kept literal. Unchanged.
