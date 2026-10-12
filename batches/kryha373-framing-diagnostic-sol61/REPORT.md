# 373 framing and alternate-machine diagnosis — GPT-6.1 Sol

No new decipherment or machine identification is claimed. Public Solved373 is contextual material for unresolved374; its published prose is not automatically a literal machine input. README was reread fully; user override forbids watchers/reviewer. The ongoing comma-only Kryha solver was not repeated.

## Direct source framing

Independently inspected immutable373/plaintext.jpg and cryptogram.jpg. Both visibly place “Legación Eslovaquia” and underlined/spaced “Madrid” above the message. The plaintext body's first actual line begins “Roessner Madrid oznamil Ústredni celuloziek,že Syndikát”; those first two words are part of the body line, not a detached salutation or header. There is no visible greeting before them. The handwritten d inserted above the typed Ústreni is real; both chronological versions have already been retained as hypotheses. Thus this inspection supplies no source basis for deleting ROESSNER, MADRID, or replacing their words. The ciphertext separately prints650, followed by KIDAH and the other129 groups. It does not visibly mark20 letters as an indicator. The signature Országh and80172 are outside the grouped ciphertext. Heading resemblance across PT/CT does not prove exact body preparation.

## Necessary reflector/Enigma test

Turing's primary wartime Treatise on Enigma, chapter1, original printedp2, states that a letter cannot encipher to itself, and describes contact pairs/Umkehrwalze. Faithfully retyped authorized archival edition, NARA RG457 Box201 Nr964: https://cryptocellar.org/turing/turchap1.pdf . The National Museum of Computing's working Bombe account corroborates the necessary property: https://www.tnmoc.org/bombe . The mathematical reason is that each per-position substitution is F-inverse × fixed-point-free reflector × F, including a consistently applied plugboard. Arbitrary rotor machinery without that reflector property is not covered.

The diagnostic checks exact p_i!=c_i without guessing new words. It includes corrected/unamended d, naturalJ/I, no comma or commaJ/X, source53 L/I and90 E/A, and source offsets0..25:1248 cases. An independent92/93-length architecture-only positive control uses new random permutation conjugates of a fixed paired reflector; no-self passes, while identity-cipher negative fails. This is a filter calibration, not a working historical Enigma rotor/stepping control or recovered key.

**32 cases survive the necessary condition;1216 violate it.** For faithful93 letters (d retained, naturalJ, comma removed), only offset20 survives among0..25, for all4 source glyph branches. NaturalJ→I does not change that offset result. Faithful94 with commaJ orX has no surviving offset. Unamended92 plus commaJ/X (thus93 emitted letters) can survive at offsets10 or20 depending glyph branch. All conflicts, exact inputs and survivors are in results.json/summary.json. The literal93 no-offset case conflicts at3 positions, including plaintext26 E versus source26 E and plaintext49 T versus source49 T. Offset5 likewise conflicts3 times.

Passing the filter is weak: independent random letters have expected roughly93/26 self matches and occasional zero-match windows. Offset20 is neither source-marked nor established; no key/rotor/configuration is recovered. This does not justify substituting an Enigma model for Kryha or claiming373 employed Enigma. A complete independently verified rotor-key fit and held-out prediction would be needed.

## Primary historical context changes the interpretation of preparation

Visually reread Antal/Grošek/Zajac2020 printedpp99–101 (local pages05–07), original research citing archival documents, available at https://www.vhu.sk/data/att/178/20273.07b25c.pdf . Page99 distinguishes old borrowed Czech machines/systemK from later Kryha Standard. Page100 explicitly lists Kryha introduction in Helsinki1943; Bucharest, **Madrid**, Budapest1944; Berlin1945. This supports Kryha availability in Madrid during1944 but gives no exact issue date or identification of the373 machine/wheel/rings. It does not establish350/373 shared hardware, key or preparation.

A **concrete new preparation clue** is page100 footnote55, citing SNA MZVkr41 document80.002/1941: January1941 instructions changed number entry from written words to **Roman numerals** to reduce length/cost. Therefore previously hypothesized digit-word640+separator/header650 equality is not historically privileged. The paper does not specify how6000 (requiring a representation beyond ordinary subtractiveI..MMM), thousands separators, or every number should be typed on a26-letter machine. No invented overline, prefix, additiveMMMMMM or other numeral encoding is introduced here. Obtaining the actual instruction would make that a source-supported finite full-message preparation branch. It cannot explain failure before the first numeral, so it does not rescue existing exact-prefix Kryha models.

Page101 requires stored cover content to be thoroughly reformulated and describes instructions to burn deciphering paper. Hence archival text can be a rewritten semantic account rather than exact ciphertext preparation. This is a legitimate limitation, not a license to invent paraphrases or arbitrary cribs. The visibly detailed typed373 draft may be closer to the actual original, but no source proves it is character-for-character input. Historical systemK reconstruction is a distinct future family, not validated by Enigma's reflector filter.

## Reproduction and preservation

```sh
python3 batches/kryha373-framing-diagnostic-sol61/run.py
```

No number token is evaluated by this pre-number filter; no ongoing Kryha case is rerun. results.json preserves all1248 transparent cases; summary.json includes source hashes. All original sources, cipher directories and markers were read-only. No374 published solution was searched or imported; portal provenance remains the parent's previously rendered three-tab capture. No process remains running.
