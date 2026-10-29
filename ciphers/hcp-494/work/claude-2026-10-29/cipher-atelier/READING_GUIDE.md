# Read this investigation

[Repository overview](README.md) · [Technical verification](verification/README.md)

## Understand the document

A cipher letter from Lincker to Vultejus, written in Hamburg in May 1672 and catalogued as HCP494. A related historical key from 1666 survives.

Start with the [source catalogue or manuscript](https://crypto.hcportal.eu/dashboard/cryptograms/494). It identifies the historical object. The source image is the evidence; the tables in this repository are recorded readings of that evidence.

## Read the current result

The surviving key supports two short sequences, with source corrections and unresolved word codes. The main-block literal is shown below. The available vocabulary does not contain the higher-number codes needed for a complete reading.

Open [Saved outputs for sequences A and B](verification/readings/VERIFIED_REPLAY_RESULTS.json) and the [research account](lincker-1672/README.md). A literal preserves the recorded output before making it smoother to read. An English explanation or translation adds interpretation and should not silently repair it.

Example:

```text
disgustirtundertanin[634]
```

This is the literal output before deciding word boundaries or syntax. [634] stays an unresolved code; Holstein is not an established dictionary value for it.

A full translation would need matching missing vocabulary and better source readings. The source date evidence and the portal date differ; the research account preserves that distinction.

## Check one example by hand

1. Open the [main-block alignment](verification/readings/evidence/Lincker_1672_partial_key_audit/main_key_alignment.csv). `sequence` gives the sign’s order; `visible_token` is its source transcription; `key255_value` is the proposed historical-key output.

| Sequence | Visible token | Key output |
| --- | --- | --- |
| 1 | `FF` | `d` |
| 2 | `67` | `i` |
| 3 | `85` | `s` |
| 17 | `PP` | `n` |
| 20 | `634` | `[634]` |

2. The first three outputs give `dis`. Concatenating the complete table gives `disgustirtundertanin[634]`, the [saved sequence-A output](verification/readings/VERIFIED_REPLAY_RESULTS.json).
3. Compare the signs with the [letter source](https://arcinsys.hessen.de/arcinsys/showArchivalDescriptionDetails.action?archivalDescriptionId=3352629), then consult the [surviving alphabet sheet](https://digitalisate-he.arcinsys.de/hstam/4_d/1234/hstam_4_d_nr_1234_0013.jpg). Sequence 17 was corrected from a BB-like reading to `PP`; the record explains its comparison with the same writer’s clear word *Proposition*.

**Correction history:** the [2 October record](verification/readings/evidence/Lincker_1672_partial_key_audit/correction_2026-10-02.json) changes `BB → z` to `PP → n` at group 17. The [diplomatic inventory](verification/readings/evidence/Lincker_1672_partial_key_audit/diplomatic_inventory.txt) retains older observations below its notice; those `BB/z` passages are superseded. Use the current alignment for the literal.

The key’s available vocabulary ends at 407; the letter contains word codes in the 600–800 range. The alphabet agreement does not supply those missing words. The letter already carries historical marginal/interlinear readings; reproducing them is not a first decipherment of unannotated text.

## Choose the check you want

- **Understand the result:** read the literal/test result beside the research account. You can do this in GitHub without installing anything.
- **Check the calculation:** follow the example above, then [run the supported Python check](verification/README.md). This verifies the saved transformation or declared model.
- **Check the source:** compare recorded signs with the original image and retain disagreements. Scans/crops are not included; obtain access under the provider’s terms. Original coordinates, when present, refer to the specified image version.
- **Evaluate the historical reading:** examine alternative signs, key evidence, language, document boundaries and prior readings. A successful calculation does not settle these questions.

To report a problem, use [Work on existing research](https://github.com/Cipher-Atelier/lincker-to-vultejus-cipher-letter-1672/issues/new?template=research.yml). Give the file, row/position, source reference, your observation, and what changes in the output. Distinguish a different source reading from a changed key or an editorial interpretation.

## What the files mean

| Open this | It contains |
| --- | --- |
| [Research account](lincker-1672/README.md) | Historical context, method, interpretation, credits and limits |
| [Saved outputs for sequences A and B](verification/readings/VERIFIED_REPLAY_RESULTS.json) | The saved text or bounded test result |
| [Main-block sign/key alignment](verification/readings/evidence/Lincker_1672_partial_key_audit/main_key_alignment.csv) | The recorded input/assignments used in the example |
| [Historical-key catalogue](https://crypto.hcportal.eu/dashboard/cipher-keys/255) | The proposed transformation, historical key, or tested assumptions |
| [Technical verification](verification/README.md) | Setup, command, expected output and what the check covers |
| [Source scope](verification/TOPIC_SCOPE_INDEX.json) | Machine-readable release boundaries and omitted material |
| [Publication provenance](SOURCE_PROVENANCE.json) | Where this package came from and what documentation changed |

CSV and TSV are tables: GitHub or a spreadsheet can display them. TSV uses tabs between columns. JSON stores named fields and lists; `null` means no value in that field, and its interpretation depends on the record. You do not need to start by reading every JSON file.

## Terms used in the research

- **Ciphertext:** the recorded encrypted signs or letters.
- **Key/mapping:** the rule assigning output to a cipher sign. It may be a hypothesis, a surviving historical key, or an assumption in a test; those are different kinds of evidence.
- **Literal reading:** the saved output with gaps and awkward wording retained, before editorial translation or repair.
- **Coverage:** how many recorded positions receive a value. It does not measure how many values are historically correct.
- **Frozen:** saved unchanged at a particular stage so a later correction cannot replace an earlier test result.
- **Replay:** applying saved rules to saved inputs again. It checks reproducibility within the declared scope.
- **Training/heldout:** material used to fit a rule, and material excluded from that fitting. Prior viewing or later correction can limit how independent a heldout test is; read the case-specific account.
