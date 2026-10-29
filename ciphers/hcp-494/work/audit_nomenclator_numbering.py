"""Bounded code-number tests; no gloss is used by the primary search.

Decode a three-digit target code as (a * permuted_digits(code) + b) % 1000,
or permute the digits after applying (a * code + b) % 1000.
The unchanged key 255 word-list envelope is generously taken as EVERY integer
180..407, including gaps. Thus a range failure cannot be caused by an omitted
transcribed word. All 6 digit permutations and 400 invertible multipliers are
searched in each order; b runs through all 1000 residues.

This tests one fixed transformation for all word codes. It does not test a new
word list, different transformations per code/block, running keys, or arbitrary
substitutions. It does not decipher the text or prove the transcription.
"""
from collections import Counter
from fractions import Fraction
import hashlib
from itertools import permutations, combinations
import json
from math import gcd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PERMS = tuple(permutations(range(3)))
LO, HI = 180, 407
MULTIPLIERS = tuple(a for a in range(1000) if gcd(a, 1000) == 1)


def digit_permute(n, p):
    digits = f"{n:03d}"
    return int("".join(digits[j] for j in p))


def decode(n, p, a, b, order="digits_then_affine"):
    if order == "digits_then_affine":
        return (a * digit_permute(n, p) + b) % 1000
    return digit_permute((a * n + b) % 1000, p)


def coverage_counts(values):
    """Count values falling in LO..HI for every modular translation b.

    Difference arrays make every circular interval O(1). This returns the
    same counts as checking all 1000 translations against every input.
    """
    delta = [0] * 1001
    for value in values:
        start, end = (LO - value) % 1000, (HI - value) % 1000
        if start <= end:
            delta[start] += 1
            delta[end + 1] -= 1
        else:
            delta[0] += 1
            delta[end + 1] -= 1
            delta[start] += 1
            delta[1000] -= 1
    counts, current = [], 0
    for b in range(1000):
        current += delta[b]
        counts.append(current)
    return counts


def search(codes, order="digits_then_affine"):
    codes = sorted(set(codes))
    best_count = -1
    best_model = None
    all_fit_count = 0
    best_ties = 0
    identity_permutation_all_fit = 0
    for p in PERMS:
        digits = [digit_permute(n, p) for n in codes] if order == "digits_then_affine" else codes
        allowed = [n for n in range(1000) if LO <= digit_permute(n, p) <= HI]
        for a in MULTIPLIERS:
            residues = [a * n % 1000 for n in digits]
            if order == "digits_then_affine":
                counts = coverage_counts(residues)
            else:
                counts = [0] * 1000
                for residue in residues:
                    for target in allowed:
                        counts[(target - residue) % 1000] += 1
            all_fit_count += counts.count(len(codes))
            if p == (0, 1, 2):
                identity_permutation_all_fit += counts.count(len(codes))
            local_best = max(counts)
            if local_best > best_count:
                best_count = local_best
                best_ties = 0
                best_model = (p, a, counts.index(local_best))
            if local_best == best_count:
                best_ties += counts.count(local_best)
    p, a, b = best_model
    diagnostic = [
        {"cipher_code": n, "mapped_number": decode(n, p, a, b, order),
         "within_envelope": LO <= decode(n, p, a, b, order) <= HI}
        for n in codes
    ]
    assert sum(row["within_envelope"] for row in diagnostic) == best_count
    return {
        "order": order,
        "distinct_cipher_codes": codes,
        "transformations_tested": len(PERMS) * len(MULTIPLIERS) * 1000,
        "all_fit_count": all_fit_count,
        "identity_digit_order_all_fit_count": identity_permutation_all_fit,
        "max_distinct_codes_in_envelope": best_count,
        "minimum_distinct_codes_outside_envelope": len(codes) - best_count,
        "number_of_best_ties": best_ties,
        "first_best_diagnostic_only": {
            "digit_order_zero_based": p, "multiplier": a, "offset": b,
            "mapping": diagnostic,
            "accepted": False,
            "reason": "Range coverage only; this model fails other codes and has no demonstrated semantic correspondence."
        },
    }


def controls():
    # Exhaustive b comparison for fixed varied residues, including repeats,
    # boundaries and intervals crossing zero; independent direct calculation.
    residues = [0, 1, 179, 180, 407, 408, 999, 180]
    fast = coverage_counts(residues)
    direct = [sum(LO <= (x + b) % 1000 <= HI for x in residues)
              for b in range(1000)]
    assert fast == direct
    # Constructed positive control, not a historical sample. Every clear code
    # is in the envelope; generate ciphertext via a nontrivial invertible
    # multiplier, offset, then a digit permutation.
    old_codes = [180, 211, 228, 232, 253, 311, 407]
    cipher = [digit_permute((37 * n + 183) % 1000, (2, 0, 1))
              for n in old_codes]
    a = pow(37, -1, 1000)
    b = (-a * 183) % 1000
    recovered = [decode(n, (1, 2, 0), a, b) for n in cipher]
    assert recovered == old_codes
    assert coverage_counts([a * digit_permute(n, (1, 2, 0)) % 1000
                            for n in cipher])[b] == len(old_codes)
    positive = search(cipher)
    assert positive["all_fit_count"] > 0
    second_cipher = [(37 * digit_permute(n, (2, 0, 1)) + 183) % 1000
                     for n in old_codes]
    second_recovered = [decode(n, (1, 2, 0), a, b, "affine_then_digits")
                        for n in second_cipher]
    assert second_recovered == old_codes
    second_positive = search(second_cipher, "affine_then_digits")
    assert second_positive["all_fit_count"] > 0
    return {
        "direct_vs_interval_counts": "all 1000 translations agree",
        "synthetic_positive": {
            "historical_evidence": False, "key_codes": old_codes,
            "generated_cipher_codes": cipher, "recovered": recovered,
            "all_fit_models_found": positive["all_fit_count"],
            "known_inverse": {"digit_order": [1, 2, 0], "a": a, "b": b},
        },
        "synthetic_positive_other_order": {
            "historical_evidence": False, "key_codes": old_codes,
            "generated_cipher_codes": second_cipher, "recovered": second_recovered,
            "all_fit_models_found": second_positive["all_fit_count"],
            "known_inverse": {"digit_order": [1, 2, 0], "a": a, "b": b},
        },
    }


def semantic_check():
    # Separate secondary test: target meanings below come from annotations,
    # not from the number-only test above. They are CONDITIONAL anchors.
    anchors = [
        {"meaning": "France", "key": 228, "target": 576,
         "key_source": "source/full/key255.jpg"},
        {"meaning": "Holstein", "key": 253, "target": 634,
         "key_source": "source/full/key255-0014.jpg"},
        {"meaning": "Holland", "key": 232, "target": 774,
         "key_source": "source/full/key255.jpg"},
        {"meaning": "Denmark (country entry)", "key": 212, "target": 601,
         "key_source": "source/full/key255.jpg"},
        {"meaning": "Alliance", "key": 311, "target": 303,
         "key_source": "source/full/key255-0015.jpg"},
    ]
    xs, ys = [r["key"] for r in anchors], [r["target"] for r in anchors]
    offset = [y - x for x, y in zip(xs, ys)]
    slope = Fraction(ys[1] - ys[0], xs[1] - xs[0])
    intercept = ys[0] - slope * xs[0]
    predictions = [slope * x + intercept for x in xs]
    affine_mod = []
    # More generous than a permutation: allow all multipliers, even those
    # which are not invertible. The first two anchors alone reject them.
    for a in range(1000):
        b = (ys[0] - a * xs[0]) % 1000
        if all((a * x + b) % 1000 == y for x, y in zip(xs, ys)):
            affine_mod.append([a, b])
    inversions = []
    for left, right in combinations(sorted(anchors, key=lambda r: r["key"]), 2):
        if left["target"] >= right["target"]:
            inversions.append([left["meaning"], right["meaning"]])
    return {
        "depends_on_auxiliary_annotations": True,
        "not_recovered_codebook_values": True,
        "anchors": anchors,
        "integer_offsets": offset,
        "one_offset_fits": len(set(offset)) == 1,
        "rational_affine_through_first_two": {
            "slope": str(slope), "intercept": str(intercept),
            "predictions": [str(x) for x in predictions],
            "all_fit": predictions == ys,
        },
        "affine_mod1000_all_fit": affine_mod,
        "order_preserving_insertion_model_inversions": inversions,
        "digit_substitution_obstruction": "Key 228 has repeated digits, target 576 has three different digits. A position permutation followed by a single consistent digit substitution cannot do this.",
        "qualification": "These semantic rejections are conditional on the five annotation-derived target meanings. They are independent of the primary range rejection, which uses none of them."
    }


def main():
    rows = []
    for line in (ROOT / "source/bourdeau/codes.txt").read_text().splitlines():
        if line.startswith(("f2r", "f3r", "f4r")):
            page, code, _unused_annotation = line.split(maxsplit=2)
            rows.append({"page": page, "code": int(code)})
    assert len(rows) == 26 and rows[20]["code"] == 447
    borrowed = [r["code"] for r in rows]
    preferred = borrowed.copy()
    preferred[20] = 427
    manifest = json.loads((ROOT / "work/source-sha256-2026-10-23-key1236.json").read_text())
    changed = [p for p, h in manifest.items()
               if hashlib.sha256((ROOT / "source" / p).read_bytes()).hexdigest() != h]
    assert not changed, changed
    preferred_result = {order: search(preferred, order)
                        for order in ("digits_then_affine", "affine_then_digits")}
    borrowed_result = {order: search(borrowed, order)
                       for order in ("digits_then_affine", "affine_then_digits")}
    result = {
        "status": "PARTIAL; bounded renumbering family rejected, no new plaintext",
        "primary_test_uses_annotations": False,
        "prior_exposure": "Earlier annotations and readings were known. The primary computation uses only code numbers and the old word-list range; it is not claimed as a blind experiment.",
        "transcription": {
            "source": "source/bourdeau/codes.txt",
            "occurrences": 26,
            "primary_revision": "Occurrence 21: 447 to preferred 427, as in the existing original-image comparison work/427-vs-447.png; uncorrected branch also tested.",
            "preferred_counts": dict(sorted(Counter(preferred).items())),
            "limitation": "Not automatic OCR or an independent review of every digit; existing original-image transcription is the input."
        },
        "key_envelope": {"from": LO, "through": HI,
                         "source": ["source/full/key255.jpg", "source/full/key255-0014.jpg", "source/full/key255-0015.jpg", "source/full/key255-0016.jpg"],
                         "generous": "Every integer admitted, including gaps; no word transcription is needed for the primary search."},
        "family": {"decode": ["(a * digit_permutation(cipher_code) + b) modulo 1000", "digit_permutation((a * cipher_code + b) modulo 1000)"],
                   "digit_permutations": len(PERMS), "invertible_multipliers": len(MULTIPLIERS),
                   "offsets": 1000,
                   "orders": 2, "parameter_choices_per_transcription": 4800000,
                   "counting_note": "Parameter choices, not necessarily distinct functions: the two orders overlap.",
                   "scope": "One fixed transformation of the whole word-code list, not separate mappings per word or per region."},
        "preferred_427": preferred_result,
        "borrowed_447": borrowed_result,
        "controls": controls(),
        "secondary_semantic_test": semantic_check(),
        "source_preservation": {"checked": len(manifest), "changed": changed},
        "not_tested": ["new or expanded codebook", "separate transformations for individual blocks", "arbitrary code substitution", "running-key reciphering", "every possible transcription error"],
        "accepted_new_plaintext": None,
        "independent_review": False,
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
