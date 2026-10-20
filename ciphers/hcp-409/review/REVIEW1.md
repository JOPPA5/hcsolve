REVISE

# Review 1 — HCP 409 (round DONE1)

Reviewer: claude-opus-5-5, 2026-10-19. **The message is deciphered.** The Kryha key reviewed on HCP 374 decrypts this ciphertext into continuous Slovak from the first to the last letter, and my own decoder reproduces the solver's output exactly. The verdict is REVISE for one reason: four of the remaining "garbles" that `SOLUTION.md` attributes to the encipherer are **transcription errors**. With the letters as typed on the scan, `RKO`, `ZATMNUSIE` and `CESKKCH` become `AKO`, `ZATKNUTIE` and `CESKYCH` (finding 1). That is a correction of the record, not of the solution; no further review round is needed if it is made.

## What I verified and how

1. **The documented commands.** `python3 ciphers/hcp-409/work/decrypt.py` and `… --json` exit 0, verify the source and transcription hashes, and print 295 letters; `reencryption_equal` is true. `python3 ciphers/hcp-409/work/verify.py` reports 295/295 and the 598 mechanical roundtrips.
2. **The key really is the reviewed 374 key.** `shasum` of `ciphers/hcp-374/work/key.json` matches the `provenance_sha256` in `work/key.json`. Input ring, output ring and the 52 adjacent distances are identical; the 23-hole mask is the same set, listed from a different starting hole (4 instead of 34). No ring value was fitted to this ciphertext.
3. **Independent decoder.** `review/work/kryha_review.py` reads the rings and mask from the *374* key file, not from 409's copy, and computes every displacement in closed form (`d_i = d0 + walk(h_phase → h_{phase+i}) + 179·⌊(phase+i)/23⌋`) instead of stepping edge by edge as `decrypt.py` does. With phase 1 (hole 4) and `d0 = 12` it prints the solver's 295-letter output character for character.
4. **Is the setting found, or forced?** `python3 review/work/kryha_review.py ciphers/hcp-409/work/transcription.txt --search` tries all 23 × 26 = 598 phase/displacement settings of the 374 key and counts hits of eleven Slovak word stems. The solver's setting scores 17; the best other setting scores 1. Only one setting is language. Given a fixed, previously reviewed key and 295 letters, that is not an accident of search.
5. **The solver's seven post-decoding corrections.** `review/work/rows*.png` (4× crops). All seven are what the scan shows: `xvibk` (33), `qppeb` (107), `oawed` (117), `cqpjm` (184), `qfoat` (198), `ixyxr` (207) — the exception is position 164, see finding 1. Because a Kryha displacement depends only on the position, a wrong cipher letter garbles exactly one plaintext letter; decoding the frozen first pass (`work/transcription-first-pass.txt`) confirms that each change affects only its own position. Post-hoc correction therefore could not have manufactured the message, only polished single letters, and the solver discloses that it was not blind.
6. **History and wording.** Dated 9 September 1944, eleven days after the outbreak of the Slovak National Uprising; Ministry of Foreign Affairs in Bratislava to the Slovak legation in Madrid (the cover's `Bern` struck through and `Madrid` typed over). The content — no Czechoslovak troops, "saboteurs" and misled Slovaks, the rumour of Tiso's murder and the government's arrest, "Inform the Slovaks in the USA" — is exactly the regime's line of those days. The solver labels it as propaganda and does not present its claims as fact; that is the right treatment.

## Findings

1. **major (transcription) — four letters are typed differently from the ledger, and they remove three of the "garbles".** For each garbled plaintext letter I computed which cipher letter would give the expected Slovak letter at that position, then looked at the scan (`review/work/rows3-4-b.png`, `rows5-7-b.png`):

   | 0-based pos. | group | ledger | needed for | scan |
   |---|---|---|---|---|
   | 120 | 25 `?hgul` | `l` → `RKO` | `h` → `AKO` | **`hhgul`**: two h's, the first crossed by a watermark line |
   | 160 | 33 `?xz?o` | `e` → `ZATM…` | `a` → `ZATK…` | **`axzyo`**: clear `a` |
   | 163 | 33 | `v` → `…NUSIE` | `y` → `…NUTIE` | **`axzyo`**: clear `y` (the first pass had `y`; the change to `v` in `transcription-changes.json` was wrong) |
   | 223 | 45 `iia?y` | `e` → `CESKKCH` | `a` → `CESKYCH` | **`iiaay`**: `a` |

   The reviewer's ledger with these four letters is `review/work/transcription-reviewer.txt`; it decodes to `…POVSTANIE AKO POMSTU…`, `…A ZATKNUTIE SLOV. VLADY…`, `…SPOMENUTYCH CESKYCH AWETOV…`. In every case the letter on the paper is the one that gives correct Slovak, which is also independent confirmation of the key and the setting. `SOLUTION.md` § "Source and unresolved points" items 2–3 and the list of editorial repairs must be corrected: these are not errors of the encipherer.

2. **minor — what remains genuinely irregular.** After finding 1 only two items are left, and both are real:
   - `DAKONCUIE` (pos. 269, group 54 `frrqp`): `o` would need cipher `f`; the scan clearly has `p`. A slip by the encipherer or the typist.
   - `AWETOV` for `agentov`: an `N` is missing. A dropped plaintext letter does not desynchronise a Kryha (displacement follows the count of keystrokes), so this is an omission at encryption time, not a transcription problem.
   Plus the alphabet conventions below. These should be the only "repairs" listed.

3. **minor — `W` = G and `J` = sentence break are well supported.** The output contains `W` exactly twice, both in `A?ENT-` where G is required, and the canonical G position never occurs. `J` occurs three times, each at a sentence boundary, while the word-internal j is written `I` (`VOISK`, `IE`, `DAKONCUIE`). The solver states both as interpretations of labels left unbound by 374; I agree, and with this text they are close to established for coordinate 22.

4. **minor — the "300".** The number before the first group is handwritten (`review/work/count.png`), not typed with the ciphertext, and has a pencil note above it. It is most likely a clerk's count for the telegram (charging or check count), not evidence of a missing five-letter group. The decoded text starts and ends with complete sentences; I agree with the solver not to invent a group.

5. **minor — numbering.** `transcription-changes.json` uses 0-based positions (`163`), `SOLUTION.md` speaks of "161–165" and "position 164" (1-based). State the convention once.

6. **minor — prior-solution search.** Two web queries. Acceptable as stated ("not proof of novelty").

## Required for closing

- Change the four letters (or show from the scan why not), regenerate `transcription.txt` and its hash in `key.json`, and rewrite the plaintext, the editorial reconstruction and the "unresolved points" accordingly. `KTORYM` at 76–80 stays as is: the scan has `qmqhh`.
- Then produce the report and `FINAL`. No `DONE2` is needed from my side.

## What I could not verify

- Letters under the heaviest watermark lines (rows 2–4, groups 4–7) beyond those listed; I found nothing else that changes the plaintext.
- Whether the original Kryha alphabet labels for the unused input positions are as canonically completed.
- Novelty of the decipherment beyond the solver's two searches.
