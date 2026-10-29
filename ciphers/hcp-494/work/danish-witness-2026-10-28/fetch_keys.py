"""Download only the public scan URLs listed by the archive viewer manifest."""
from pathlib import Path
import concurrent.futures
import hashlib
import json
import urllib.request

ROOT = Path(__file__).parent
MANIFEST = json.loads((ROOT / "key-image-references.json").read_text())
(ROOT / "keys").mkdir(exist_ok=True)

def fetch(item):
    i, url = item
    url = "https:" + url if url.startswith("//") else url
    dest = ROOT / "keys" / f"{i:03d}.jpg"
    if not dest.exists():
        data = urllib.request.urlopen(url, timeout=60).read()
        dest.write_bytes(data)
    data = dest.read_bytes()
    assert data.startswith(b"\xff\xd8"), (i, "not JPEG")
    return {"page": i, "url": url, "path": str(dest.relative_to(ROOT)),
            "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}

with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    results = []
    for result in pool.map(fetch, enumerate(MANIFEST["SA_URLs"], 1)):
        results.append(result)
        if len(results) % 25 == 0:
            print("downloaded", len(results), flush=True)
(ROOT / "download-manifest.json").write_text(json.dumps(results, indent=2) + "\n")
print("complete", len(results), sum(r["bytes"] for r in results), flush=True)
