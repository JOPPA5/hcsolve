# HCP 1395 / pc_hcp_76 — Caesar −1 love postcard, 1907

> **My dearest, I am just going to post. L. & K. [probably "love & kisses"] from your own girl.**

Complete decipherment of every enciphered letter on the card (44 letters, one fixed key). One residual point, the closing initials (letter identity M/N, whether they are enciphered at all, and their expansion), is disclosed below; the expansion "love & kisses" is editorial, not deciphered.

## Source and context

- HC Portal cryptogram 1395, name `pc_hcp_76`, portal status **Not solved** (rendered General / Description / Attachments read 2026-10-26; no attached transcription or solution). Portal date 1907-04-24, language "Unknown", recipient "W. Abboú". Originals in `source/` are unchanged (SHA-256 checked by the decoder).
- Picture side: printed "Branksome Chine, Bournemouth"; no handwriting there.
- Address side (ordinary writing, not enciphered): **Mr Abbott, Stokelake Farm, Chudleigh, Devon**; postmark WIMBORNE, AP 24, 07. The portal's "W. Abboú" is a misreading of "Abbott" (the metadata file is left unchanged). Language: English.
- The message is written in the left half of the address side and is read after rotating the scan 90° counter-clockwise. Its heading "G. H. Wednesday" and the date "April 24th 07." are ordinary writing and are not shifted (same practice as the finished sister card hcp-1397).
- Same correspondence as hcp-1386…1407 (letters from a girl to Mr W. Abbott, Chudleigh, 1907–08), several of which use the same key; hcp-1397 (FINAL) is the closest parallel: "Mpwf gspn Zpvs Pxo Hjsm" = "Love from your own girl".

No published solution of this card was found or used.

## Cipher and key

Monoalphabetic shift (Caesar): each plaintext letter is replaced by the next one in the alphabet. Decrypt by shifting back one:

```
cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

## Transcription and plaintext

| Ciphertext (as written) | Literal plaintext |
|---|---|
| Nz. Efbsftu. | MY. DEAREST. |
| J bn. kvtu | I AM. JUST |
| Hpjoh up qptu | GOING TO POST |
| M. & L. gspn. | L. & K. FROM. |
| Zpvs. pxo | YOUR. OWN |
| Hjsm *(inside an ornamental outline)* | GIRL |

Writer's dots are kept in the literal output; sentence punctuation in the reading above is editorial.

**English:** My dearest, I am just going to post [i.e. going to the post / to post this]. L. & K. [probably "love & kisses"] from your own girl.

**Slovak:** Môj najdrahší, práve idem na poštu. L. & K. [pravdepodobne „love & kisses“ = láska a bozky] od tvojho vlastného dievčaťa.

## Reproduce

From the repository root:

```
python3 -I ciphers/hcp-1395/work/decode.py
```

It checks the SHA-256 of every file in `source/`, reads the manual transcript `work/transcription.json`, decrypts each row with the key above, verifies the round trip, and prints the 44-letter plaintext (output saved in `work/plaintext.txt`). The transcript is a manual visual reading, not OCR.

## Uncertainties

1. **Closing initials "M. & L."** (before *gspn* = FROM). Earlier work left this field unclassified (M or N? cipher or plain?).
   - Letter identity: enlarged, the first initial has a hooked stem plus **two** legs (`work/closing-initials.png`), like the "M." of the same formula on hcp-1407 (`work/hcp1407-MandL-comparison.png`) and the plaintext "May" there, and unlike this hand's one-legged N in "Nz" (MY). The second is a looped cursive capital L.
   - Status: read as ciphertext, giving **L. & K.** The writer enciphers everything except heading, date and address. Supporting (not conclusive) evidence: on hcp-1397 she enciphered the full word in this slot ("Mpwf … from your own girl" = LOVE), and on hcp-1388 the enciphered `N yy` = M xx ("M" + kisses) stands before FROM; this shows that the closing formula is enciphered, but not that initials in it are. The expansion "love & kisses" is the usual sense of L. & K. but is interpretation, not deciphered letters.
   - Alternatives: (a) if the first initial is N (this hand's M and N differ only by one short leg), the shift gives **M. & K.**, which matches hcp-1388 (`N yy` → M xx) and the reading `N & Lt` → M & Ks proposed on hcp-1399; (b) if the initials were left in clear, the field is "M. & L." unexpanded. Note that the sister cards hcp-1399 and hcp-1407 keep this same group literal and unclassified ([N & Lt], [M. & L.]); this card classifies it with more confidence only because the enlargement shows two legs, and the classification remains an editorial choice. The literal decoder output is L. & K.
   - A small raised tick and a dash after "L." are taken as punctuation/flourish (the same tick follows "L." on hcp-1407) and are not transcribed.
2. "post" has no object on the card ("going to post" — i.e. going to the post [office], or going to post this card); nothing is added to the deciphered text; the gloss is given in brackets in the translation.
3. Cursive shapes: v in *kvtu* is open and a-like and u ends in a flourish; *kbtu*/*kvtw* give no word, *kvtu* = JUST. The j in *Hjsm* is the long slanted descender, as in *Hpjoh*.
4. The heading initials "G. H." are reported literally (C. H. is also possible from the loop); they are not part of the cipher and are not expanded.

## Why it is correct

- One fixed shift turns all 44 letters into fluent, period-appropriate English with no unknown symbols: MY DEAREST / I AM JUST GOING TO POST / … FROM YOUR OWN GIRL.
- Long words are self-verifying (Efbsftu → DEAREST, Hpjoh → GOING, qptu → POST), and the same key and same phrases recur on the sister cards (hcp-1397 FINAL, 1388, 1407).
- The context fits: ordinary heading/date match the postmark (Wimborne, 24 Apr 1907) and the portal date.

## Credit

Cipher identification, transcription of the main words and the first decoder: OpenAI GPT solver (GPT-6 Astra), 2026-10-26, left partial because of the closing initials. Re-verification on the pixels, classification of the initials (M, enciphered → L & K), rewritten decoder and this document: Claude Opus 5.5, 2026-10-29.

## Response to review 1

Review verdict REVISE; all five findings addressed. The deciphered letters (44, one shift −1) and the decoder output are unchanged.

1. **(major) Expansion presented as read text — fixed.** The headline, the English and the Slovak lines now give the deciphered "L. & K." and mark the expansion as editorial: "L. & K. [probably "love & kisses"]". The opening paragraph says the expansion is not deciphered.
2. **(major) Competing N-reading not disclosed — fixed.** Uncertainty 1 now lists N. & L. → **M. & K.** as an alternative, with the evidence from hcp-1388 (`N yy` → M xx) and hcp-1399 (`N & Lt` → M & Ks), and states plainly that hcp-1399 and hcp-1407 keep the same group literal while this card classifies it. I keep M as the preferred letter: in `review/work/N_vs_M_6x.png` (the reviewer's own crop, which I re-examined) the N of "Nz" has a hooked stem and one arch, while the closing initial has the hooked stem and two descending legs and is visibly wider; the reviewer reached the same preference.
3. **(minor) hcp-1397 argument overstated — fixed.** It is now presented as supporting evidence that the closing formula is enciphered, explicitly not as proof that the initials are.
4. **(minor) NOTES.md entry of 2026-10-26 without spaces — fixed.** The entry was rewritten with normal spacing; content unchanged.
5. **(minor) "going to post" — fixed.** The English now carries the gloss "[i.e. going to the post / to post this]"; uncertainty 2 updated.

Re-run after the edits: `python3 -I ciphers/hcp-1395/work/decode.py` → "source hashes OK", 44 cipher letters, `MY. DEAREST. I AM. JUST GOING TO POST L. & K. FROM. YOUR. OWN GIRL` (identical to before and to `work/plaintext.txt`).
