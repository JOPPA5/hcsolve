"""Independent row-by-row encoder checks every retained whole candidate."""
from pathlib import Path
import json

p = Path(__file__).parent
rows = json.loads((p / 'target-summary.json').read_text())
checks = 0
for result in rows:
    for line in (p / result['top100_file']).read_text().splitlines()[1:]:
        _, keyword, plaintext = line.split()
        key = [ord(c) - 97 for c in keyword]
        width = len(key)
        ciphertext = ''.join(
            plaintext[i]
            for rank in sorted(set(key))
            for row in range((len(plaintext) + width - 1) // width)
            for column in range(width) if key[column] == rank
            for i in [row * width + column] if i < len(plaintext)
        )
        assert ciphertext == result['input'], result
        checks += 1
verification = dict(cases=len(rows), independent_full_candidate_reencryptions=checks,
                    all_exact=True)
(p / 'target-verification.json').write_text(json.dumps(verification, indent=2))
print(verification)
