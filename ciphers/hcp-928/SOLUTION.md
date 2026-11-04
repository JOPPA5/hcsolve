# hcp-928 — Solution (round 1)

Card: HC Portal cryptogram 928, "cpc_1908-09-08_USA_Vance, Alabama_USA_Birmingham, Alabama_", T. Schrödel collection. Postmark VANCE, ALA., SEP 8 1908; one-cent Franklin stamp; addressed in plain writing to Miss Delia Fischer, #42 Woodland Ave., Birmingham, Ala. Picture side: comic "RAPID TRANSIT" (a boy riding a pig), publisher K-Win & Co., Chicago.

Work: transcription, key reconstruction and decipherment by Claude Opus 5.5 (2026-11-03). No earlier work on this number; no published solution was found or used (the portal page lists none; no web search was made beyond the portal capture).

Note on files: the image names are swapped against their content. `source/address-large.jpg` and `work/hires/..._adr.jpg` show the PICTURE side; `source/picture-large.jpg` and `work/hires/..._pic.jpg` show the ADDRESS side. All reading was done on enlarged crops of the work/hires originals (crops in `work/crops/`).

## Cipher type and key

Simple monoalphabetic substitution (MASC) with invented signs (digits, letters and symbols), English. Words are separated by dashes. Two diacritic conventions:

- a small caret written under a sign = capital letter (This, Take, Delia, That, Will, Please, Yours);
- two short strokes above a sign = the letter is doubled (moon, honeymoon, soon, letter, Will).

| plain | sign | plain | sign | plain | sign |
|---|---|---|---|---|---|
| a | X | i | P | r | a |
| b | 9 with straight stem (q) | j | y with dot below | s | ) |
| c | 6 | k | round 9 / reversed e | t | cent-like sign |
| d | pi-like sign | l | d | u | ( |
| e | 8 | m | 7 | v | : |
| f | o (plain small circle) | n | / | w | division-like sign |
| g | 2 | o | 5 | y | circle crossed by a bar (-o-) |
| h | 3 | p | n | | |

Not attested on the card: q, x, z. One extra sign, K, occurs only in the signature.

ASCII transcription (one character per sign, legend at its head): `ciphers/hcp-928/work/transcription.txt`.

## Command

From the repo root:

```
python3 -I ciphers/hcp-928/work/decode.py
```

It checks the SHA-256 of the four source images and prints the literal decipherment of both sides.

## Plaintext (literal decoder output)

Picture side:

    Take me back back back to bir[m]ingham. Delia, is thet trip you intend
    taking a honeymoon? if not, please do'nt go soon. That letter was a god
    send to me. Will yos be so kind as to write another? Please, Yours truly
    we[K], w

Address side (correspondence half):

    This is a fine moon light night and i'd give the world just to be
    walking with you. we[K].

## Normalised reading (English)

Take me back, back, back to Birmingham. Delia, is that [the] trip you intend taking a honeymoon? If not, please don't go soon. That letter was a godsend to me. Will you be so kind as to write another? Please. Yours truly, We[K], W[.]

This is a fine moonlight night and I'd give the world just to be walking with you. We[K].

## Slovak translation

Vezmi ma späť, späť, späť do Birminghamu. Delia, je tá cesta, na ktorú sa chystáš, svadobná cesta? Ak nie, prosím, nechoď [tak] skoro. Ten list mi bol darom z nebies. Budeš taká láskavá a napíšeš ďalší? Prosím. S úctou, We[K], W.

Je krásna mesačná noc a dal by som celý svet za to, aby som sa mohol prechádzať s tebou. We[K].

## Uncertainties (all disclosed)

1. Birmingham: the 4th sign is an ink blot (filled triangle) over the letter; m is restored from word sense and the address on the card (only m fits "Bir_ingham"). Elsewhere m is 7.
2. "thet" (picture side, line 3): the four signs are clearly t-h-e-t (8 = e, the same as in "the", "letter"). Read as a slip for "that" or "the"; the sentence reads either way.
3. "yos" in "Will yos be": the third sign is clearly ")" (s) where "(" (u) is meant; the writer used the mirror pair. "you" rests on sense.
4. "do'nt": the o of "don't" carries two short strokes and a dot (review 1), not the plain two-stroke doubling mark; I take it as the apostrophe. "don't" rests on sense.
5. Signature "÷8K" (both sides) decodes as "We" + K, where K is a sign not used anywhere else on the card (possibly a plain letter or an initial). Reported literally; the sender's name is not established. The picture side adds a comma and one more division-like sign (w) with an extra dot under the signature: reported literally as "W".
6. After "DelPX" (Delia) a short vertical stroke crosses the following dash; taken as a comma. In line 1 the dash between "take" and "me" carries a dot above it; taken as a stray mark, not a letter.
7. Capital marks are not written on every sentence start (e.g. "if", Birmingham); the decoder prints what is marked.
8. Steganography: the stamp box was inspected; nothing is visible around or under the edges of the stamp, but what lies under the affixed stamp cannot be seen on the scans. No hidden writing was found in the picture or along the edges.

## Why I believe it is correct

- Every sign on both sides is covered by one fixed key; 22 letters are each attested several times in different words (e.g. P23C in light/night, P/2 in taking/walking, X) in as/was/please), with no conflicts other than the disclosed slips.
- The text is coherent, period-appropriate English of a 1908 love note, and fits the card: "Take me back ... to Birmingham" captions the "Rapid Transit" pig ride, and the recipient lives in Birmingham, Ala.
- The doubling and capital conventions are applied consistently (oo in moon/honeymoon/soon, tt in letter, ll in Will).

## Register

Proposed type label: MASC. Register entry to be written only after an accepted review.

## Response to review 1

Review 1 (Claude Opus 5.5, separate agent, 2026-11-03): verdict ACCEPT, four minor findings. No change to the key or the decoded letters; the reproduction command was re-run after this response (`python3 -I ciphers/hcp-928/work/decode.py`: "source hashes OK", output unchanged).

1. Signature sign K unread. Agreed; kept as the single unresolved item. The signature is reported literally as "We[K]" (address side) and "We[K], W" (picture side); the sender's name is not established. The rest of the card reads in full, so the solution is complete under the run's rule (one un-understood item, everything else read).
2. Mark above o in "don't". Re-checked on work/crops/z_dont.png (enlarged): the mark is two short strokes with a dot above them, as the reviewer says, not a clean three-dot sign. Uncertainty 4 is amended accordingly: the mark is "two strokes and a dot"; it differs from the plain two-stroke doubling mark by the extra dot and is taken as the apostrophe; "don't" rests on sense.
3. Web search. A short web search was made on 2026-11-03 (query: "Delia Fischer" Birmingham postcard cipher 1908 Vance). It returned only unrelated postcard posts on Klaus Schmeh's Cipherbrain blog (scienceblogs.de/klausis-krypto-kolumne); none mentions Delia Fischer, Vance or this card. No published solution of this card was found; the reading is the solver's own.
4. Swapped file names. Repeated in the report (source/address-large.jpg shows the picture side and source/picture-large.jpg the address side).

Steganography check (also in answer to the general request to look under stamps): the stamp box on the address side was inspected again on source/picture-large.jpg and the hires original; the one-cent Franklin stamp is affixed and nothing is written around it, on the margins, in the "Post Card" heading or in the picture. Whatever may be under the stamp cannot be seen on the scans. The type therefore stays MASC, not "MASC + Steganography".
