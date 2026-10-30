# HCP 1389 / pc_hcp_70 — partial reading

**Partial, not a complete solution candidate.** The body uses Caesar substitution with decryption shift −1: cipher `ABCDEFGHIJKLMNOPQRSTUVWXYZ` → plaintext `ZABCDEFGHIJKLMNOPQRSTUVWXY`. The readable main text supports this key directly, independently of the related-postcard hypothesis.

## Sources and method

Root read all three rendered portal tabs and supplied the original scans and metadata. The portal was **Not solved**, with no supplied transcription or solution. I inspected both original images. All transcribed text is a manual visual reading, not OCR. `work/address-270.jpg` rotates the address side for reading; `work/message-large.jpg` is only an enlarged working crop. Original files remain unchanged.

Forty cipher letters are frozen in `work/transcript.json`:

```text
Nz Pxo Efbsftu J
 dbo tbz. bn
jo. gbwpvs. xjui
Qb. usvtu.
```

The decoder preserves punctuation rather than silently normalizing it:

```text
My Own Dearest I
can say. am
in. favour. with
Pa. trust.
```

A cautiously normalized reading of this portion is: “My own dearest, I can say [I] am in favour with Pa. Trust …” The bracketed second “I” is editorial English grammar, **not an extra cipher letter**. “Pa” is decoded `Qb`, not an identified person.

Slovak translation of the supported portion: „Môj najdrahší, môžem povedať, [že] som u otca v priazni. Dúfam …“ The translation of *trust* is conditional on its incomplete continuation.

## Reproduction

From the repository root:

```sh
python3 ciphers/hcp-1389/work/decode.py
```

This verifies SHA-256 hashes of both original images and metadata, then decodes the frozen **manual transcription**. It does not automatically recognize handwriting from pixels or decode the unresolved remainder.

## Unresolved scope

- After `usvtu` (“trust”) on the fourth body row are compressed apparent initials, tentatively `N,, L.` → `M,, K.` under this key. Letter identity, small intervening marks, and intended meaning remain unverified; these are excluded from the frozen 40 letters.
- The fifth row looks like `Gsp[n/o]. Zpvs. …`: `Gspn` would give “From”, while literal `Gspo` gives “Fron”. I cannot yet decide the final character from the image; “From” is therefore a contextual hypothesis, not a frozen reading. `Zpvs` suggests “Your”; the following short token and raised marks remain unresolved.
- The signature below the cipher is ordinary writing, unclear initials; it must not be blindly shifted. The heading appears `G. H. Thursday.` and date `May 2nd 1907`, also ordinary writing.
- Portal recipient spelling and ordinary handwritten address are not independently established identity evidence. The picture has no cipher writing; its printed caption reads “Toll Gate Lower Sand Gate Road. Folkestone.”

The long coherent reading, consistent Caesar shift, and 1907 postcard context support the decipherment method, but do not settle the remaining handwriting. No DONE marker, PDF, register entry, or FINAL is warranted.

## Update 2026-10-29 (Claude Opus 5.5) — still PARTIAL

Earlier sections are by the OpenAI GPT solver (2026-10-26). This update re-read the scan sign by sign (crops in `work/crops/`, transcription `work/transcription_v2.json`). Status remains **partial**: one body word is unresolved, so no DONE1.

Command (repo root): `python3 -I ciphers/hcp-1389/work/decode_v2.py` — checks source hashes, decodes the read lines with Caesar −1 (cipher letter = plaintext letter + 1), and prints the unresolved fields literally.

Current reading (48 cipher letters decoded):

| Cipher | Plaintext |
|---|---|
| Nz Pxo Efbsftu J | My Own Dearest I |
| dbo tbz. j. bn | can say. i. am |
| jo. gbwpvs. xjui | in. favour. with |
| Qb. | Pa. |
| **[usjot.]** | **unresolved** |
| [M/N]..[&?] L. | closing abbreviation field, not expanded |
| Gspn. zpvs. | From. your. |
| N.. + raised mark | unresolved initial/abbreviation field |
| Hjsm. | Girl. |

Reading: "My own dearest, I can say I am in favour with Pa. [unresolved word] [L. & K.?] From your [N.. field] Girl."

Changes against the earlier partial:
1. **Line 2 has a cipher `j`** between `tbz.` and `bn` (light long slash with a lower-left hook, the writer's j). The second "I" is therefore read, not editorial.
2. **The "signature" H/S/m is cipher `Hjsm` = Girl**, the same closing as hcp-1395/1397/1390 (j drawn as a long slash with a hook; visible in `work/crops/signature-hjsm-5x.png`).
3. **`usvtu` (trust) is withdrawn.** The pixels show u, s, a long slash with a lower-left hook (identical to this writer's j in `Hjsm`, line 2, and `Hpjoh` on hcp-1395), a closed o, and a 7-shaped stroke with a detached bar (probably t, crossbar written to the right as in `Efbsftu`). Literal `usjot` → "trins", not English. Reading the slash+o as p gives `uspt` → "tros", also not English. No v and no final u are visible, so "trust" would require two unseen letters. The word is left unresolved.
4. **Closing fields**: after the line-4 word stands the family's recurrent `M & L`-type field (on hcp-1395 read L[ove] & K[isses]); here the left part of the "M/N" is mixed with the descender of j in `xjui`, and the "&" is two small strokes. After `zpvs.` stands `N..` plus a raised mark, the same kind of field as "M + raised letter" on hcp-1390 and "M/N + 1-like stroke" on hcp-1402. Neither is expanded.
5. The first letter of `Qb.` is a capital with a top bar, left curl and looped descender; Q (→ Pa) fits the sense but U (→ Ta) or G (→ Fa) are not excluded by shape alone.

Slovak (supported part): „Môj najdrahší, môžem povedať, že som v priazni u otca. [nečitateľné slovo] [skratka] Od tvojho [skratka] dievčaťa."
English as above.

Why it stops: the scan is 1024 px wide; at that resolution the line-4 word cannot be reconciled with any English word without inventing letters. Not forced.
