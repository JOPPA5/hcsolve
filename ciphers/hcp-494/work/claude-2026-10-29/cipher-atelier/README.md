# Lincker’s cipher letter to Vultejus (May 1672)

A cipher letter from Lincker to Vultejus, written in Hamburg in May 1672 and catalogued as HCP494. A related historical key from 1666 survives.

[Cipher Atelier](https://github.com/Cipher-Atelier) · [Research index](https://github.com/Cipher-Atelier/research-index) · [Reading guide](READING_GUIDE.md) · [Verification](verification/README.md)

## Current status — 11 October 2026

This is a partial application of surviving 1666 key 255 to two short recorded sequences. Sequence A gives `disgustirtundertanin[634]`; sequence B gives `[678?]{g}ottgebdasallw{d/o}lablau{u/ff}`. Word division is editorial. `[634]` is an unknown word code, braces preserve alternatives or tentative identification, and the possible marginal “Holstein” does not establish `634 = Holstein`.

| Evidence layer | Open this |
| --- | --- |
| Original / surviving key | [Letter](https://arcinsys.hessen.de/arcinsys/showArchivalDescriptionDetails.action?archivalDescriptionId=3352629) · [key 255](https://crypto.hcportal.eu/dashboard/cipher-keys/255) |
| Current signs / key application | [Main alignment](verification/readings/evidence/Lincker_1672_partial_key_audit/main_key_alignment.csv) · [token application](verification/readings/evidence/Lincker_1672_partial_key_audit/partial_key_check.json) |
| Literal | [Saved outputs](verification/readings/VERIFIED_REPLAY_RESULTS.json) |
| Interpretation / correction history | [Research account](lincker-1672/README.md) · [2 October correction](verification/readings/evidence/Lincker_1672_partial_key_audit/correction_2026-10-02.json) |

`FF → d`, `67 → i`, `85 → s` gives `dis`. Group 17 is now `PP → n`; the [diplomatic inventory](verification/readings/evidence/Lincker_1672_partial_key_audit/diplomatic_inventory.txt) preserves superseded `BB → z` observations below its correction notice. Start with the current alignment and [manual check](READING_GUIDE.md#check-one-example-by-hand).

**Unresolved / missing:** the available vocabulary ends at 407, while the letter uses 600–800 codes. A matching supplement and better source readings are needed; the bounded neighboring-key search does not prove no supplement exists. No complete translation is included. The manuscript’s 4 May, endorsement’s 4/14 May and portal’s conflicting 3 May date remain distinct evidence.

## Start here

1. [Read the plain-language guide](READING_GUIDE.md): the document, result, file meanings and one worked check. No programming is required.
2. Open [Saved outputs for sequences A and B](verification/readings/VERIFIED_REPLAY_RESULTS.json) to inspect the saved text or test result itself.
3. Read the [research account](lincker-1672/README.md) for historical context, methods, earlier work and unresolved questions.

## Reproduce the checks

Follow the worked example in [the reading guide](READING_GUIDE.md#check-one-example-by-hand). It connects a source record, a key or model assumption, and the saved output. For an independent source check, use the [original-source entry](https://crypto.hcportal.eu/dashboard/cryptograms/494); images are linked, not redistributed here.

If you use Python, follow the [complete verification instructions](verification/README.md), including download/setup, expected results and troubleshooting. The command from this repository’s top-level folder is:

```sh
python3 verification/check_all.py
```

A successful run means the published files and declared calculation reproduce. It does not establish that every source sign or historical interpretation is correct.

The [Evidence checks workflow](.github/workflows/verify.yml) runs this offline baseline on Python 3.10 and 3.13, without installing dependencies, and checks changed-file whitespace.

## Research scope and limitations

Two short sequences reconstructed using the surviving 1666 key. Existing historical glosses are not new plaintext; high-number word codes remain unresolved.

## Contribute

This is part of [Cipher Atelier](https://github.com/Cipher-Atelier), founded by [Maxim Egorov](https://github.com/cayde-6). Explore the [research index](https://github.com/Cipher-Atelier/research-index), [contribution guide](https://github.com/Cipher-Atelier/.github/blob/main/CONTRIBUTING.md), and [step-by-step research workflow](https://github.com/Cipher-Atelier/research-index/blob/main/START_HERE.md).

Read the current result and source limitations, then coordinate a bounded task in an existing issue or use [Work on existing research](https://github.com/Cipher-Atelier/lincker-to-vultejus-cipher-letter-1672/issues/new?template=research.yml). Fork the repository and submit a focused pull request with your evidence and checks. Independent replication and constructive alternative readings are welcome. See [Start here](https://github.com/Cipher-Atelier/research-index/blob/main/START_HERE.md) for the shared workflow.

## Sources and rights

Source credit and item-specific restrictions remain in the research records. Scans, crops, restricted materials and private correspondence are excluded. No new blanket licence is asserted. AI-assisted work requires evidence checking and does not constitute external human expert review.

[Publication provenance](SOURCE_PROVENANCE.json) records the source commit, retained file hashes and deliberate code/navigation adaptations. The original repository history remains intact.
