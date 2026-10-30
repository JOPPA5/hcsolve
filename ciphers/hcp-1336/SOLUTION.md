# hcp-1336 (pc_hcp_17) — PARTIAL, not a closed decipherment

Solver: Claude Opus 5.5, 2026-10-30. No earlier work on this number; no published solution found (none attached on the portal; no web search was done).

## Cipher type

No cipher with a key. This is an **initial-letter abbreviation (initialism)**: each capital, followed by a dot, is the first letter of an English word. Because it discards information, it has no key and no unique inverse. Every word below is an inference.

## Transcription (all 35 signs, read from the hires scan)

    M O D A A H Q S
    D H [J/L/H/F?] G [B/R] A D
    H Y A F B D W E
    L T A F K F Y E
    A A D C

The address side reads Miss Wooster, The Grange, Shenley, Herts; postmark Barnet 9 AM, 24 Jan 1910 (a Monday). The picture side ("The Mossy Bank") has no writing. The large disc is the portal's watermark, not part of the card.

## Provisional reading

    My own darling A., arrived home quite safe(ly), dear.
    Had [?] [G] [B/R] [A] [D] -- not resolved.
    Hope you are feeling better, dear.
    With every love, take a fond kiss from your ever affectionate and devoted C.

English is the original language, so the above stands as both. Slovak of the same provisional text:

    Moja drahá A., prišiel som domov celkom bezpečne, drahá.
    [Veta v 2. riadku nerozlúštená.]
    Dúfam, že sa cítiš lepšie, drahá.
    S láskou, prijmi nežný bozk od svojho navždy láskavého a oddaného C.

## Command

    python3 -I ciphers/hcp-1336/work/expand.py

It checks the source hashes and prints the signs, the expansion and a confidence tier per word (A sister formula, B sense plausible, C guess, - left as initial). The table is a record of conjecture, not a key.

## Uncertain

- **Second clause, "H ? G B/R A D" (6 signs): unresolved.** Sign 3 of line 2 has a heavy ink blot on its top; the lower part is a loop with a rising cross stroke and a short second stem, so J, L, H or F are all possible. Sign 5 is a stem and bowl with an inward-curled leg: B or R. "Had jolly good rest all day" fits only if the signs are J and R and is a guess; I do not offer it as the reading. The final D could also be "Dear", opening the next clause.
- "A." after "Darling" is probably a personal name or a pet word; not resolved. "C." is the sender's signature initial.
- Alternatives remain for O, Q, S, F, B, A in the reading above: the words fit, but other words with those initials could too. The first A of line 5 is written with a left hook and could be U; the sister formula favours A.
- "W E L" as "With Every Love" could be "With Everlasting Love" or similar.

## Why the method is believed

- Every letter has a dot, and the letters are normal capitals in a mixed hand.
- All seven Wooster cards are visibly one series in one hand and share fixed slots. Opening: MODA/MGDA + AHQS D on 1322, 1334–1339. Closing: W E L T A F K F Y E (A A) D C or close variants on 1335–1339. A substitution of English would not give a nearly identical multi-word opening and closing on every card with different middles.
- hcp-1322 has "A H A 15 to 11" with the time in clear, which reads naturally as "arrived home at 15 to 11". This is the strongest single anchor for A H.
- Postmarks are all Sunday evening or Monday morning (27 Dec, 3, 10, 16, 24, 31 Jan, 13 Feb), consistent with a weekly note after a Sunday visit.
- Sister cards here were read from their scans for this comparison only; none of them is solved.

## Status

Partial: no DONE marker. A closed plaintext would require something this card does not contain, such as the same message in clear. No register entry.
