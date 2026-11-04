ACCEPT

# Review 1 – hcp-992 (cpc_1903-12-04_DE_Munchen_DE_Eschersheim_kellermann-02)

Reviewer: Claude Opus 5.5, 2026-11-03. Round 1, solver's DONE1.

## What I verified and how

1. **Solver command.** `python3 -I ciphers/hcp-992/work/decode.py` prints "source hashes OK" and
   - C1 `MEIN HERZINNIGGELIEBTES HERZENS [BLOT] .... !`
   - C2 `GUNKTE`
   - C3 `DICH ABER UMARMT`
   - C4 `MIT UNZÄHLIGEN GRÜSSEN UND KUSSEN DEIN SICH SEHR NACH DIR SEHNENDES ERICN ...... ....`
   This matches the plaintext in SOLUTION.md, where the last word is given as ERIC[N/H] and "Erich" is
   explicitly put down to word sense.

2. **Independent reading and decryption.** I read the cipher lines again, sign by sign, from my own enlarged crops of
   `work/hires/*_pic.jpg` (review/work/l1a, l1b, l2, gunkte, c3, aber, c4a, c4b, grussen, gru2, kussen, dir, sig).
   I wrote my own sign names and key in `review/work/indep_decode.py`
   (`python3 -I ciphers/hcp-992/review/work/indep_decode.py`). The output is identical to the solver's:
   `mein herzinniggeliebtes herzens / gunkte / dich aber umarmt / mit unzähligen grüssen und kussen dein sich sehr
   nach dir sehnendes eric?`. There are 20 distinct signs and 111 cipher tokens. Every token is covered by one
   one-to-one key, there are no conflicts, and no homophones are needed.

3. **Pixel checks of the critical signs.**
   - φ-like sign (oval loop on a descender) for A in ABER, UMARMT, NACH, and with a diaeresis in UNZÄHLIGEN: it is
     clearly different from the open-loop 9 (G) in GELIEBTES, UNZÄHLIGEN and GRÜSSEN. This confirms the A/G split.
   - Hook sign (open 6 / reversed C with a blob) for R. It is distinct from the plain 6 (B) at the line end of
     GELIEB-TES and in ABER.
   - Double-crossed sign for K in KUSSEN and in the parenthesis group. This matches sister card hcp-993, where the
     two-bar cross is k and the single + is f.
   - Parenthesis group: I read 9 · U · 2 · double cross · 7 · 4 at 3x (the last three signs are faint). That gives
     GUNKTE, as the solver reports. It is not misread.
   - GRÜSSEN: the umlaut dots are not directly over the U. They sit about 50 px higher, between U and S, under the
     R of ABER. Ü is still a fair reading, and the KÜSSEN/GRÜSSEN pair supports it.
   - Inked-out word after HERZENS: a solid horizontal ink bar, so it is unrecoverable. It is the writer's own
     deletion, not unread text.
   - UMARMT: the second sign is a faint 3 under the collection stamp, and the 3rd sign is the φ-sign. The reading
     stands.

4. **Plain Kurrent parts** (crops review/work/k0–k4). These read as the solver says: "Wollte dir noch schnell
   mitteilen, daß du [Herrn?] zum 7. gratulierst, habe versehentlich der letzten Karte u. Paket falsche Adresse
   gegeben, bin kerngesund. Morgen schreibe ich Brief. Grüße bitte alle Lieben ...". Only the word after "daß du"
   stays uncertain (H-like capital, short letters, a superscript hook, n). The solver discloses it.

5. **Address side** (review/work/adr.png): "Fräulein Margarethe Kellermann / p/Adr. Herrn A. Weyhe /
   Hochwohlgeboren / Eschersheim b/Frankfurt a/Main / Frankfurterstr. 49". There is no cipher. The stamp is placed
   diagonally and has not been lifted. The postmarks are München 4 and Eschersheim 5.12.03, which agrees with the
   date "4. Dez. 03". I saw no writing in the picture or along its borders.

6. **Context / sister card.** hcp-993 (same sender, same recipient, München 4.2.03, now DONE1) uses the same key
   and the same phrases: "Mein herzinniggeliebtes Herzens....!", "Bin kerngesund", "Dich aber umarmt mit … Grüßen
   und Küssen Dein Erich". On that card the signature has H = 8. This strongly supports the reading and the name
   Erich. The German is idiomatic 1903 love-letter style.

7. **Sources.** The portal shows "Not solved" and attaches no solution. The solver records a web search that found
   nothing. I found nothing that would suggest a published solution was used.

## Findings

1. **minor – final sign of the signature.** SOLUTION.md treats the last sign of ERIC? as a 2-shaped N sign with a
   blob, and puts "Erich" down to word sense only. In my 4x crop (review/work/sig.png) the sign has a heavy filled
   upper part over a lower loop. That fits this writer's 8s, whose upper loop is often filled (see SEHR, SICH,
   NACH), as well as a 2. Sister hcp-993 signs "Erich" with 8. The solver should mention that the sign may be a
   cramped 8 and cite hcp-993. The decoder could also print ERIC[H] with a note rather than ERICN. This does not
   change the reading.
2. **minor – letter count overstated.** "about 140 enciphered letters" should be 111 cipher tokens (20 distinct
   signs), counted by my script.
3. **minor – GUNKTE gloss.** "Punkte" is well supported by context, because this couple's cards end greetings with
   rows of dots ("Herzens....!", "Erich ......"). "I had written dots for you" therefore makes sense. The solver
   should state that, if this is right, the writer used the G-sign by mistake for P (P is not attested in hcp-992 or
   hcp-993). The solver already reports the word literally. It is a single word, so it does not make the card
   partial.
4. **minor – key description vs sister.** The A sign is described as "9 with filled loop". hcp-993 describes the
   same sign as "oval crossed by a long vertical (φ)". A cross-reference to hcp-993's key, which is now available,
   would help readers. NOTES.md says hcp-993 had no work yet; that was true when written.
5. **minor – address transcription.** "Hochwohlgeboren" is omitted from the address line in SOLUTION.md. This is
   cosmetic.

## Register type

MASC is correct. The card has no steganographic part that can be seen: the stamp is on the address side, is not
lifted, and has no writing visible around it. Mixing plain Kurrent with cipher lines does not change the type.

## Not verified

- The area under the postage stamp, which is not lifted.
- The exact identity of the person to be congratulated ("Herrn"?). I could not read this word better than the
  solver did.
- The content of the inked-out word.
