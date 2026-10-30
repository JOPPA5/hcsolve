# HCP1310: Feri to Jolánka Tóth, a carriage attacked on the road (Gyöngyös, 1 July 1912)

**Status: whole message read, every sign decoded; one word, *Darasztin*, is not identified as a place (see Uncertainties item 1). Revised after review 1.** Claude Opus 5.5, 2026-10-30.

Credit: reading, ledger and interpretation by Claude Opus 5.5. No earlier work exists on this number. The key comes from the finished Jolánka cards, chiefly HCP1216, whose key was first transferred by the OpenAI GPT solver and completed by Claude Opus 5.5. The portal shows status Not solved and attaches no transcription or solution; no published solution was found or used.

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented graphic signs, written continuously. It is the Jolánka family key, unchanged:

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | section mark (S, 8, 5 forms) | k | F-like | r |
| six | b | wave | l | right bowl | s |
| opposed bowls | cs | three short strokes | m | gamma | t |
| short stroke left + tall stroke right | d | two short strokes | n | plain cross x | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross + | f | tall stroke left + short right | h (p near-homograph; no p occurs here) | hooked descender | y |
| open loop with descender | g | crossed curve, usually dotted | i | crossed diagonal with tail | z |
| that loop + hooked descender | gy | inverted T | j | | |

Marks over a sign are accents (double dots for ö, ű). Acutes are not transcribed. Portal language "Unknown" is resolved: the text is Hungarian. The pencil note and the red address are not enciphered.

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1310/work/decode.py
```

It checks the SHA-256 of both `source/` scans and both `work/hires/` originals, decodes `work/ledger.txt` (one token per written sign, read by eye on enlarged crops of the hires scan), and prints the literal rows and the normalized text. Crops: `work/crops/`, made by `work/crop*.py`.

## Literal decipherment

```
01 kedvesegyetlenre      12 ennemtalakoztam
02 menyemtudatomhogy     13 meolyaneberekel
03 szerencsesenmegerkez  14 sehalaistennekezel
04 temazutbantalalkoz    15 bezaromsoraim
05 tamegykocsivalame     16 mertmarkevesaid
06 lyiketmegtamad        17 jomulataskivanok
07 takahogyvisznek       18 darasztinistenve
08 felölbejotekarok      19 edesematavolbol
09 szalasbanmegrais      20 imadokadvasseferi
10 lovödöztekdene        21 tiszteleakedvasmamat
11 kiisvoltfegyvere
Under the stamp: csokja / idra / szom / jazok / hükadve / sedferi
Below the address: szeretetel
```

## Hungarian (normalized)

Kedves egyetlen reményem! Tudatom, hogy szerencsésen megérkeztem. Az útban találkoztam egy kocsival, amelyiket megtámadtak, ahogy Visznek felől bejöttek Árokszállásban, még rá is lövö[l]döztek, de neki is volt fegyvere. Én nem találkoztam mé[g] olyan e[m]berekkel se, hála Istennek. Ezzel bezárom soraim, mert már kevés a[z] id[ő]. Jó mulatás[t] kívánok Darasztin[?]. Isten ve[l]ed, édesem, a távolból imádó kedvese Feri. Tisztele[m] a kedves mamát.

Under the stamp: Csókjaidra szomjazok. Hű kedvesed Feri.

Below the address: szeretettel.

## Plaintext on the card (not enciphered)

- Address, red ink: Szép reményű Tóth Jolánka úrleánynak, Jász Árokszálás.
- Bottom edge, red ink: Kelt Gyöngyös 1912 Júl. 1 reggel.
- Bottom right corner, red: a small number, apparently 7/27 (uncertain).
- Top, faint pencil under the postmark, partly illegible: it starts *sziv...*, has a capital J-like form, and ends *...ák hoz*; perhaps *Szívem Jolánkához* ("to my heart's Jolánka"). A hypothesis, not relied on.
- Picture side, printed: Hej cigány hallod-e? (song verse; publisher number 3077/78).

## English

My dear only hope! I inform you that I have arrived safely. On the way I met a carriage that had been attacked: as they came in from the direction of Visznek at Árokszállás, they even fired at him, but he had a weapon too. Thank God, I have not yet met such people myself. With this I close my lines, for time is now short. I wish you a good time at Darasztin[?]. God be with you, my sweet; from afar, your adoring sweetheart Feri. I respect the dear mother.
Under the stamp: I thirst for your kisses. Your faithful sweetheart Feri.
Below the address: with love.

## Slovak

Moja drahá, jediná nádej! Oznamujem, že som šťastne dorazil. Na ceste som stretol koč, ktorý prepadli: keď prichádzali od Visznek v Árokszállási, ešte aj naň strieľali, ale aj on mal zbraň. Ja som sa, chvalabohu, s takými ľuďmi ešte nestretol. Tým končím svoje riadky, lebo už je málo času. Želám dobrú zábavu v Daraszti[?]. S Bohom, moja milá; z diaľky ťa zbožňujúci milý Feri. Úctivo pozdravujem drahú mamu.
Pod známkou: Túžim po tvojich bozkoch. Tvoj verný milý Feri.
Pod adresou: s láskou.

## Uncertainties

1. **Row 18, `darasztin`, then `istenve`:** all signs are read; the ninth is two strokes on the baseline (n), unlike the h of this card, whose short tick sits at the top right. The word itself is not identified. It has a sister parallel: HCP1305 row 5 reads `mulatharasztin` (*Hogy mulat ...?*), the same eight letters after the first sign, in the same *mulat-* context, so this is probably one place or jocular name where Jolánka amuses herself. The first sign differs: d (short + tall) here, h/p (tall + short) on HCP1305. These are the same strokes in opposite order, so one card may hold a slip. *Darasztin* / *Harasztin* ("at Haraszt[i]") is a hypothesis; I could not confirm such a place. The translations mark it [?].
2. **Row 18/19, `istenve | edesem`:** normalized *Isten veled, édesem*. The writer lost `l` and one `ed`; this rests on word sense. The signs are as printed.
3. **Row 7, third sign:** a 5-like form of the section mark. Read k, giving *megtámadtak, ahogy*. The alternative s gives *megtámadta, s ahogy* and the same story. The k form is chosen on shape.
4. **Row 19, `T` of *távolból*:** a gamma whose lower right is crossed by the first bar of the following a, so it resembles F. Read t on word sense (*a távolból*; r would give no word).
5. **Stamp row 6, `d` of *kedvesed*:** two strokes, the right one faded; n would give *kedvesen*, which makes no sense, and *kedvesed* matches the *te* form of *csókjaidra*. Word sense decides. The cross of *Feri* is tilted and the final i is blurred by a wet smear; the upper stamp signs (first c of *csókja*, x of *hű*) are also smeared but their identities are fixed by the words. The ű marks are visible. The first sign of that row shows only one thick stroke, so its h rests entirely on word sense (*hű*).
6. **Address line, sixth sign of `szeretetel`:** blotted, closer to F than gamma. Read t on word sense.
7. **`=` versus three bars:** the writer sometimes puts two bars for e: *kadvasse*, *hükadve*, *kedvas*. The ledger keeps what is written; the normalization corrects them.
8. **Other writer spellings normalized:** *jotek* → jöttek; *talakoztam* → találkoztam; *mé olyan* → még olyan (g absent); *eberekal* → emberekkel (m absent); *lovödöztek* → lövöldöztek (l absent); *a id* → az idő (z and ő absent; the row ends at d); *mulatas kivanok* → mulatást kívánok (t absent); *tiszteleakedvas* → tisztelem a kedves (m absent); *kadvasse* → kedvese (doubled s); *megrais* → még rá is (a clear acute stands over the e); *szalasban* → Árokszállásban (card has `szálás` in both cipher and address, as is usual for this writer); `sehala` divides as *se, hála*. Word division and most accents are editorial. The formal *kedvese* in row 20 sits beside informal *veled* and *kedvesed*; it is kept as written.
9. **Row 11, `t` of *volt*:** the gamma has a doubled stroke under its top bar and leans towards F. Read t on word sense (*neki is volt fegyvere*); r would give no word.
10. **Row 21:** a pink blot lies under the wave, but the sign is still a wave. The dropped m of *tisztelem* is an interpretation, not a hidden sign.
11. The events are the writer's report; I could not check them. "Him" for the carriage's occupant comes from *neki*, which has no gender in Hungarian.

## Why it is correct

- The unchanged family key turns all 21 rows, the six rows under the stamp and the address line into Hungarian, with no sign outside the key.
- The sense runs across row breaks (*megérkez|tem*, *ame|lyiket*, *ne|ki*) and the stamp rows join into *csókjaidra szomjazok*.
- The context fits. Visznek lies near Gyöngyös (the dateline) and Jászárokszállás (the addressee's town); the dateline Júl. 1 agrees with the postmarks (July 1 and a Jászárokszállás mark reading Jul 3). The signature Feri and *a távolból imádó* match HCP1216 and the family's closing style.
- Repeated words decode identically: *találkoz-* in rows 4 and 12, *Feri* twice, *kedve-* three times.

## Response to review 1

Verdict REVISE. All six findings are accepted after checking the crops myself. The story and the key are unchanged; two ledger signs and one normalized word changed.

1. **Row 13, last sign but one: fixed.** On `work/crops/r13b.png` and `review/work/z_r13cmp.png` the sign after the section mark has three bars, the third short and low. Ledger now `S E ~`, the row reads `meolyaneberekel`, and "`-kal` for *-kel*" is removed from uncertainty 7. It was a misreading, not a spelling of the writer. The other a-for-e slips stand.
2. **Row 18, ninth sign: fixed, and my claim of no sister match withdrawn.** On `work/crops/r18a.png` and `review/work/z_r18h.png` the short stroke stands low beside the long one; on `work/crops/r7a.png` the h of *ahogy* has its tick at the top right. Ledger now n, the row reads `darasztinistenve`, and the "false start" idea is dropped. The HCP1305 parallel `mulatharasztin` is recorded in uncertainty 1. The first sign stays d in the ledger, and the word is given as a hypothesis in the normalized text and the translations.
3. **Row 9, *még rá is*: fixed.** The acute over the e is clear on `review/work/z_r9acute.png`. Changed in `work/normalized.txt`, the normalized text and uncertainty 8.
4. **Undisclosed pixel calls: disclosed.** The h of *hű* (stamp row 5) is in uncertainty 5, the t of *volt* (row 11) in the new uncertainty 9. Both signs stay in the ledger as read on word sense, with a comment there.
5. **Pencil note: taken up** in the plaintext section as a hypothesis, matching `review/work/z_pencil.png`.
6. **Status line, uncertainty 1 and NOTES.md: updated.** "Between" for Visznek is softened to "near", as the reviewer asked; I have no map source either.

The reproduction command was re-run after these changes: all four hashes pass and the output matches the literal rows and normalized text above.
