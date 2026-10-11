# Physical audit of short Budapest telegrams334/332

Original1024×768images and metadata were inspected, including every cipher group of334. No source or working transcription was changed. This audit does not identify a cipher, recover plaintext, or make a25-letter alphabet fit by changing W. All derivative crops preserve original pixels enlarged by nearest neighbor; blue-channel versions are supplementary contrast views only, not retouched originals. Raw original-image inspection rectangles and hashes are in evidence.json.

##334: independent visible transcription and damage

```
HQLKR LTOXP OKTQS FOSZO
JCKUM UBABP HKPZB UVJPT TNGXT HKYTB TNECS
IGOST BOAJY HXSUN [obscured]DZQR HSFPX TZHMG RD[I/1]BX FWXX[edge loss?]
FQXXQ SLMQJ VCNXK IVZGU ZNXVY HLLQS GMJHE
SGNAN HSPRG IVPRS BVBDE
```

Rows contain4,7,8,7,4visible grouped fragments, total30. Treating every fragment as fivepositions gives150, with148read alphabetic characters and the existing two unknown-slot hypotheses. That arithmetic is conditional, not a physical proof of exactly150original letters or exactlytwo missing characters.

At original rectangle(383,492,485,539), a triangular folded/overlapping flap covers the left of DZQR and part of the upper D. The regular character pitch and exposed low stroke before D are compatible with one occupied, obscured firstslot, as in working `?DZQR`. The lower stroke does not determine its letter. It is not a source-supported free choice of any preferred cryptanalytic letter. More underlying material could be covered; the scan cannot reveal it, so one missing initialslot is a geometric hypothesis rather than a counted loss. If all groups are regular fives, it is position71.

At(827,497,950,555), four adjacent regularly spaced glyphs F W X X are visible. The W has multiple down/up strokes and two lower junctions, unlike the single-valley V elsewhere in IVZGU, ZNXVY and BVBDE. **W is the preferred source reading; V has no positive support from the visible stroke topology.** No W→V or W→VV alphabet normalization is justified. Under the regular-five model W is position92. The next expected character position falls into the torn/folded right edge. A terminal unknown fifthletter after FWXX is consequently plausible and more physically natural than inserting an unknown inside its four regular visible letters. Still, there is no legible fifth glyph and no proof of the original group length; `FWXX?` remains a hypothesis, not an observed fiveletter string. If regular fives, the unknown is position95.

Other originally noted groups were reinspected: UVJPT, TNGXT, VCNXK, HLLQS remain preferred direct readings without a newly supported alternative. RD[I/1]BX has a narrow upright thirdglyph; I versus digit1 cannot be firmly settled at this resolution/overprint. The rest of the independent grouped reading agrees with the working transcript. No variants were selected by language score or cipher fit.

The large space before TNECS spans a paste-strip transition rather than an unambiguously printed sequence of empty character cells. It cannot count a missing group. Damage at the right edge and the flap, plus this layout uncertainty, prevent concluding that the two placeholder slots exhaust all possible incompleteness.

Clear address fields read approximately `AALLAMI MINISTERSTVO ZAHRANICIA BRATISLAVA` (routing-word spelling is not used as a cipher constraint). Service strip reads `BUDAPEST 72 7951 35 18 1933`;35is beneath Počet slov,18beneath Deň,1933is consistent with a time. Ending outside grouped text is `10465 SPISIAK +`.35administrative words does not prove175cipherletters: addresses, signatures and numeric fields also occur, and their charging/counting convention is not supplied. The image contains no separate explanatory cover letter or readable instruction stating an exact number/location of lost cipher characters. Portal title mentions incompleteness/telephone inquiry; it does not specify the missing slots.

##332: TRC placement and O/D ambiguity

The visible strip reads:

```
TRC KDUFA VHSFC OYAUB EJFNK QTNZE UG[O/D]ZR UBCIE GZZYK +
```

TRC consists of three visibly printed uppercase letters followed by eightfiveletter groups:40bodyletters,43includingTRC. The initial T is close to the left paste-edge, but no additional preceding letters are legible. TRC uses the same type size, ink appearance and baseline as KDUFA and the other groups; the space after it resembles ordinary word/group spacing. There is no colon, special ruling, newline or equals sign isolating it as a cryptographic indicator. No separate sixletter indicator is visible. TRC may be a short prefix/indicator or part of incomplete framing, but source appearance alone does not prove any of those interpretations or its encryption status.

The OYAUB opening glyph is a rounded O, distinguishable from D in KDUFA. The thirdglyph of UG[O/D]ZR is partly crossed by blue overprint and remains unresolved: it can look more stemmed than that O, but the source pixels do not securely select O or D. Preserve both. This is bodyposition28, or position31if TRC is counted. Both variants are physical-reading alternatives, not scoring-selected repairs. The40bodyletters contain no W under either reading, which is compatibility only and does not identify a25-letter machine.

Clear service strip is `SS BUDAPEST 72 6087 12 14 1325 =`; address is `ETAT = MINISTERSTVO ZAHRANICIA / BRATISLAVA =`. Ending has a plus sign. There is no readable cleartext key, key number, missing-indicator instruction or separate explanatory cover in the one supplied attachment. Portal description says a key was not included; that is externally recorded metadata, not an independently visible instruction on this telegram scan. Absence of a visible sixletter group is not proof that the historical protocol required one.

## Concrete consequence

A25-letter Štolba interpretation cannot currently absorb334by silently normalizing its visible W. It must explain a genuinely present W via a historically supported alphabet/framing/error mechanism or remain incompatible with the preferred source reading.332remains physically compatible with aW-free alphabet, but TRCis not a verified machine indicator and unknown pins/selectors are still unknown. For further cryptanalysis, retain332O/D as twoexplicitsourcevariants and334damage as uncertain geometry rather than adding arbitrary letters to complete a desired length.

Reproduce counts/hashes with `python3 batches/short-source-audit-sol61/evidence.py`. No browser redownload, image generation, retouch, published solution lookup, cipher write, marker, watcher or reviewer operation was performed.
