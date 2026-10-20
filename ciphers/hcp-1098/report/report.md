# HC Portal 1098 — A1Z26 numerical postcard

**The complete declared transcription decodes as English under A=1, B=2, …, Z=26.** All 312 numerical positions decode and re-encode exactly. The full text is coherent personal correspondence about a Saturday visit, trains and dressmaking. Several cleartext spans are preserved unchanged. Claude Opus 5.5 independently accepted the complete reading in REVIEW1.

## Source and key

Postcard dated 25 March 1909, from the Brattleboro area to Homer Wright in Bernardston, Massachusetts; Tobias Schrödel collection. Sender unknown. The HC Portal page was freshly checked and displays Not solved. Sources and public-reference checks are in SOURCES.md. No already-published plaintext of this particular card was encountered or used.

Key: decimal ordinal of the ordinary English alphabet: `1→A, 2→B, …, 26→Z`. Dots separate numerical letters; dashes usually separate words. The manuscript also has ordinary unenciphered text. Unobserved alphabet entries are supplied by the standard convention; the card does not independently attest every unused value.

A single command from the repository root produces the entire plaintext:

```sh
python3 ciphers/hcp-1098/work/decrypt.py
```

The source is a scan, so the command reads the explicit **manual transcription** in work/transcription.txt and verifies the original picture/address/metadata hashes. It does not claim to decrypt pixels or perform OCR. `--json` emits every source group, decoded group, cleartext span and physical line. No lexical correction or omitted cipher prefix is applied.

## Complete literal decoding, with source line wraps rejoined

```text
I RECEIVED YOUR CARD TO NIGHT I AM PLANNING TO COME DOWN SATURDAY IF NOTHING HAPPENS MORE THEN I KNOW OF YET I DONT KNOW WHETHER I SHALL BE DOWN ON THE P.M. or EVENING TRAIN I AM UP TO NETTIES TO NIGHT HAVE BEEN DRESS MAKING ALL AFTERNOON HAVE BEEN UP HERE EVERY DAY THIS WEEK SO FAR I WORKED UP ON Pine St. Tues. & Wed. forenoon. GUESS I SHALL NOT HAVE ANY MORE MONEY MAKING WORK THIS WEEK WISH I MIGHT I SHALL GO DOWN HOME TO MORROW P.M.
```

The mixed case identifies decoded uppercase text versus some source cleartext; it does not imply a different cipher at those places.

## Readable English — punctuation is editorial

I received your card to night. I am planning to come down Saturday if nothing happens more then I know of yet. I dont know whether I shall be down on the P.M. or evening train.

I am up to Netties to night; have been dress making all afternoon. Have been up here every day this week so far. I worked up on Pine St. Tues. & Wed. forenoon.

Guess I shall not have any more money making work this week. Wish I might. I shall go down home to morrow P.M.

## Slovak translation

Dnes večer prišla tvoja pohľadnica. Plánujem prísť v sobotu, ak sa nestane ešte niečo, o čom zatiaľ neviem. Neviem, či prídem popoludňajším alebo večerným vlakom.

Dnes večer som u Nettie; šitie šiat mi zabralo celé popoludnie. Doteraz som tu každý deň tohto týždňa. V utorok a v stredu dopoludnia som pracoval(a) na Pine Street.

Asi už tento týždeň nebudem mať ďalšiu zárobkovú prácu. Kiežby som mal(a). Zajtra popoludní pôjdem domov.

## Coverage, verification and remaining uncertainty

- All 22 source lines and 312 numerical symbols are represented. Ordinary cleartext on the picture side is retained; the address side is ordinary addressing, not an omitted cipher body.
- `python3 ciphers/hcp-1098/work/audit.py` uses a separate numerical lookup/re-encoder, verifies every declared group, checks original source hashes and confirms that the editorial English has the same complete letter sequence. No language score is used as evidence.
- The numerical transcription is language-assisted manual reading. Similar handwritten 5/6 and 13/18 forms and the lower lines under the watermark were independently collated by Claude Opus 5.5, with no reading that changes a letter. Mechanical round-trip checks alone are not used to certify glyphs.
- Netties is literally NETTIES; the possessive spelling “Nettie's” and the person's identity are not encoded. The sender's name and gender are not established. Final P.M. is preserved as written; afternoon is the natural contextual interpretation, but initials cannot be ruled out from the letters alone.
- Original THEN, DONT, TO NIGHT, DRESS MAKING and TO MORROW are retained. Sentence punctuation and modern capitalization are editorial.
- Independent reviewer verdict: ACCEPT (REVIEW1, Claude Opus 5.5, 19 October 2026). The reviewed source transcription and key are unchanged.

Solver: OpenAI GPT-6 (Codex), 19 October 2026.


## Response to review 1

Verdict: ACCEPT. The reviewer independently decoded the text and checked every numerical group in enlarged source crops. No transcription or key correction was requested or made.

1. THEN: retained literally in both the exact and readable English. The report explains its meaning as THAN; no source letter is silently modernized.
2. Sender: remains unnamed. NETTIES is retained; no identity, relationship or gender is asserted. The Slovak translation leaves grammatical gender open. The Wednesday-writing interpretation is labelled an inference consistent with the Thursday postmark.
3. Documentation: `report/report.pdf` and its reproducible source now exist. All four pages were rendered and visually inspected; complete English and Slovak text extraction checks pass. The register entry names Tomáš Pavuk as the solver; it is submitted to the AI Decipherment Register by him.

The complete 312-symbol source reading, A1Z26 key, 22-line transcription and exact command remain the accepted ones. Sources are unchanged.


PDF generation: run `report/build_report.py` with the bundled ReportLab runtime. The PDF uses the unchanged readable English and Slovak translation files and original scan files.
