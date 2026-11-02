# hcp-1172 solution: PARTIAL (no marker, no register entry)

Solver: Claude Opus 5.5, 2026-11-02. No earlier work on this number. The portal shows Not solved and attaches nothing. The HistoCrypt article it links was not checked. Transcription is my own, from work/hires/.

The digit block is read except for one word. The card stays partial because the struck-through open cover note has a clause I cannot read (see below), and the rule counts open text too.

## Card

To Szépreményű Sziber Margitka kisasszonynak, Szomolya, u. p. Bogács; postmark day 2, file name 1915-11-02. Signed Sz. A. Open text addressed to "Kedves Angyika" (compare "Ángyika" on hcp-1175), then a digit block of 122 signs, later struck through in brown ink.

## Cipher and key

MASC, family key from FINAL hcp-1174, 1178, 1179. Digit plus mark is one sign. Attested here: 0 o/ó; 1 i/í; 1. a; 1: e/é; 1' á; 2, cs; 2. é; 3 d; 3, r; 3. v; 4, g; 5 h; 5, l; 7 k; 7, s; 7. sz; 8 m; 8, t; 8. t (as on 1179).

New values from this card, each fixed by words:
- 4. = gy (hogy, twice), 6 = j (tudja, mindnyájatokat), 6, = n, 6. = ny (mindnyájatokat), .1 = u (tudja; dot left of the stem).
- 2 (plain) occurs once and has no value.

## Reading (Hungarian; everything from "Kedves Margitkám" on is enciphered)

Open: Kedves Angyika! Tisztelettel értesítem, hogy már [unread word, about 12 letters, ends in -én?] [unread word, P..., ends -ról or -ről].

(Kedves Margitkám) Sz. A. [Sz. A. is open]

A kártában aszt kérdesztem, hogy kere[2]e te is írnál mindig számokkal, hogy ne tudja seki a olvasni. Számtalanszor csókollak mindnyájatokat.

Normal spellings: kártyában, azt, kérdeztem, senki. Commas and capitals are mine. "kárta" matches "kartim" on hcp-1179; "Mindnyájatokat számtalanszor csókollak" stands in clear on hcp-1171.

English: Dear Angyika! I respectfully inform you that already [unread]. (Dear Margitka) Sz. A. In the card I asked that [unread word] you too would write always in numbers, so that nobody can read it. Countless times I kiss you all.

Slovak: Milá Angyika! S úctou Vám oznamujem, že už [neprečítané]. (Milá Margitka) Sz. A. V pohľadnici som sa pýtal, či [neprečítané slovo] aj ty by si písala vždy číslami, aby to nikto nevedel prečítať. Nespočetnekrát vás všetkých bozkávam.

## Command

    python3 -I ciphers/hcp-1172/work/decode.py

It checks the four hashes and decodes work/transcription.txt, printing `[2]` for the unknown sign. Word division and the normal reading are mine.

## Uncertainties

1. **Open clause, why this is partial.** After "hogy már" two words lie under heavy brown strokes. Colour, ratio and channel filters (work/ink*.py) did not separate them. Tempting guesses such as a place name in Péter- or Péti- are not supported letter by letter, so none is claimed. "Angyika" and "értesítem" are readable but overstruck.
2. **kere[2]e.** The 2 is clear, with no mark. No family value fits. Unproved ideas: a slip for 3, giving kéred-e; a lost comma or dot gives kerecse, kereée, which are not words. The sentence sense holds without it.
3. **seki a.** Signs read `7, 1: 7 1 1.`: no n sign before k (nothing is hidden there), so seki = senki by sense. The following 1. has no place in the sentence; its top is under a stroke, so 1: cannot be excluded. Treated as a slip.
4. **csókollak.** Two signs after `2,` lie under the printed publisher's mark. A crossed 7 and a possible 0 are visible, the 0 not cleanly. Restored as `0 7`, the only reading giving the word. The second 5, comma is partly under print text, and the 1. dot too.
5. **Kedves.** The fifth sign's upper dot lies under the brown band; only the lower dot is seen, so `1:` (not `1.`) rests on the word.
6. **Signs 8. / 8,** both t. In kártában 1' after 8. is a dot at mid-height, on a stroke.
7. Faint blue-grey pencil traces below lines 3 to 9 were not read. They look like an erased or offset layer; I cannot say whether they carry text.

## Why I believe the block is right

The transferred key, unchanged, gives 122 signs of connected Hungarian with one unknown sign. The four new values each appear in a word of several otherwise known signs. The sentence about writing in numbers suits a card written in numbers, and the closing formula matches hcp-1171.
