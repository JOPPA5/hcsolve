# Notes hcp-1242

2026-11-02: captured by Claude Opus 5.5 (orchestrator).

## 2026-11-02 Claude Opus 5.5 (solver): PARTIAL, no marker

Result: all 18 enciphered rows are read with the Jolánka family key (hcp-1216), unchanged. The card as a whole stays partial because the unenciphered 8-line note in the stamp box has a clause I cannot read (lines 3-5 and most of 8). Under the run's rule that makes it partial with no register entry. No DONE1. No published solution was found; portal status Not solved. Sister cards were used for the key only; no earlier work exists on this number.

Reproduce: `python3 -I ciphers/hcp-1242/work/decode.py` (hash check plus ledger decode; ledger work/ledger.txt, normalized work/normalized.txt). Crops in work/crops/ (stamp_red*, st*, L3-L8 use the blue channel, where the blue printed stamp nearly vanishes).

Normalized Hungarian: Drága csillagom! Tudatom, hogy szerencsésen megérkeztem. Édes Jolánkám, ha Ön ma itt lett volna, nevetett volna egy jót rajtunk, hogy ezek a bol[on]dok hogy koptatják a gyöngyö[s]i járdát. Ami Bélát illeti, teljesen meg van elégedve Margitkával. A Margitka véleményé[t] talán Ön jobban tudja. Ezzel bezárom soraim. Maradok sírig hű tisztelője, Feri. A szerelem szár[ny]án rep[ü]ljön e lap.

English: My dear star! I inform you that I have arrived safely. Sweet Jolánka, had you been here today, you would have had a good laugh at us, at how these fools are wearing out the Gyöngyös pavement. As for Béla, he is completely satisfied with Margitka. Margitka's opinion you perhaps know better. With this I close my lines. I remain, faithful unto the grave, your admirer, Feri. May this card fly on the wings of love.

Slovak: Moja drahá hviezda! Oznamujem, že som šťastne dorazil. Sladká Jolánka, keby ste tu dnes boli, dobre by ste sa na nás zasmiali, ako títo blázni šúchajú gyöngyösský chodník. Čo sa týka Bélu, je s Margitkou úplne spokojný. Margitkin názor azda poznáte lepšie Vy. Týmto končím svoje riadky. Zostávam do hrobu verný Váš ctiteľ, Feri. Nech tento lístok letí na krídlach lásky.

Points in the cipher reading:
1. Row 9 [s] of gyöngyösi: the sign is under an ink blot, restored; only s gives the place name. Row 18 [ü] of repüljön: under a blot, two dot-like bumps on top, restored.
2. Row 8 p of koptat: tall + short stroke, p rests on word sense (h/p near-homograph, n-like too). Row 8 p and the phrase koptatják a járdát carry each other.
3. Row 8 `boldok` is literal. Normalized bol[on]dok ("fools"), which suits "laugh at us"; boldogok ("happy ones", also with omission) is the alternative. The sense of that one word is therefore a call.
4. Row 18 `szarjan` is literal, with j where ny is expected; normalized szárnyán. Row 14 `menye talan`: t of -ét omitted or shared with talán.
5. Row 12 `Margitka`: the a shows two bars and a small tick below (a, e not excluded); row 13 is clearly e (`Mergitka`), same name. Row 5 first m and the n of volna are written over or blotted but the strokes are countable.
6. Writer spellings: vetet, jaká, illeti with one l, evel. Accents mostly invisible and supplied.
7. Row 7 `ezeká`: tick over the bars of a; the division ezek a is editorial.

Plain text on the card: Szépreményű Tóth Jolánka úrleánynak s.k. / szeretetel (= szeretettel; first letters weak) / Jász Árokszállás / Andrási út Visznek felé (Visznek partly under the HCPortal stamp; rests on word sense, the village is near and named on hcp-1310). Postmarks: ÁROKSZÁLLÁS and one ending ...GYÖ..., 1912 MÁ[J]. Printed verse on the picture side is not a cipher. hcp-1310 opens with the same "Tudatom, hogy szerencsésen megérkeztem".

Why it stops: stamp box lines are 1 csokolom, 2 szamtalan, 3 m... with a descender and a tall letter, ending in a comma (unread), 4 starts with a short word, then something like T o a l t e (unread), 5 a long wavy word ending -a (unread), 6 maradok(?) (m a r/n ... o k), 7 szívének, 8 oh(?) + m.l.. + smeared end. Tried colour, redness and blue-channel separation at 3-6x. The strokes show but give no words I can defend; the family formulas do not fit the letter shapes, and forcing one would be invented text. Only csokolom számtalan and szívének are firm.
