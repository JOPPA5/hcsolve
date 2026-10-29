"""Bounded retrieval of manifest-listed public Raumer scans, no enumeration.

Use: ...py thumbs ; ...py default 1 2 3 ; ...py sheets
"""
from pathlib import Path
import concurrent.futures
import hashlib
import io
import json
import sys
import time
import urllib.request
import urllib.error
import xml.etree.ElementTree as ET
from PIL import Image, ImageDraw, ImageFont

WORK = Path(__file__).resolve().parent
OUT = WORK / "raumer-screen-2026-10-29"
METS = WORK / "enclosure-context-2026-10-28/lasa-raumer-mets.xml"
NS = {"m": "http://www.loc.gov/METS/"}


def urls(use):
    root = ET.fromstring(METS.read_bytes())
    group = root.find(f".//m:fileGrp[@USE='{use.upper()}']", NS)
    return [f.find("m:FLocat", NS).attrib["{http://www.w3.org/1999/xlink}href"]
            for f in group]


def fetch(job):
    index, url, folder = job
    target = folder / f"{index:03d}.jpg"
    if not target.exists():
        for attempt in range(4):
            try:
                with urllib.request.urlopen(url, timeout=40) as response:
                    data = response.read()
                break
            except urllib.error.HTTPError as error:
                if error.code not in (429, 500, 502, 503, 504) or attempt == 3:
                    return {"page": index, "url": url, "error": f"HTTP {error.code}"}
                time.sleep(2 ** attempt)
        im = Image.open(io.BytesIO(data))
        im.verify()
        target.write_bytes(data)
    data = target.read_bytes()
    im = Image.open(io.BytesIO(data))
    return {"page": index, "url": url, "path": str(target.relative_to(WORK)),
            "bytes": len(data), "width": im.width, "height": im.height,
            "sha256": hashlib.sha256(data).hexdigest()}


def download(use, selected):
    folder = OUT / use
    folder.mkdir(parents=True, exist_ok=True)
    entries = urls(use)
    numbers = selected or list(range(1, len(entries)+1))
    assert all(1 <= i <= len(entries) for i in numbers)
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
        records = list(pool.map(fetch, [(i, entries[i-1], folder) for i in numbers]))
    manifest = OUT / f"{use}-manifest.json"
    existing = {r["page"]: r for r in json.loads(manifest.read_text())} if manifest.exists() else {}
    existing.update({r["page"]: r for r in records})
    manifest.write_text(json.dumps([existing[i] for i in sorted(existing)], indent=2)+"\n")
    print(json.dumps({"use": use, "downloaded_or_reused": sum('error' not in r for r in records),
                      "errors": [r for r in records if 'error' in r],
                      "total_bytes_this_batch": sum(r.get("bytes",0) for r in records)}))


def sheets():
    folder = OUT / "sheets"
    folder.mkdir(exist_ok=True)
    count = len(urls("thumbs"))
    font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 24)
    for start in range(0, count, 12):
        selected = list(range(start+1, min(start+13, count+1)))
        canvas = Image.new("RGB", (1680, 1080), "white")
        draw = ImageDraw.Draw(canvas)
        for i, number in enumerate(selected):
            path = OUT / "thumbs" / f"{number:03d}.jpg"
            x, y = (i % 4)*420, (i//4)*360
            draw.text((x+10, y+5), f"Page {number}", fill="black", font=font)
            if not path.exists():
                draw.text((x+10,y+45), "Thumbnail unavailable", fill="black", font=font)
                continue
            im = Image.open(path).convert("RGB")
            im = im.resize((410, round(im.height*410/im.width)), Image.Resampling.NEAREST)
            canvas.paste(im, (x+5, y+40))
        canvas.save(folder / f"{start+1:03d}-{start+len(selected):03d}.jpg", quality=95)
    print(json.dumps({"sheets": len(list(folder.glob('*.jpg')))}))


if __name__ == "__main__":
    if sys.argv[1] == "sheets":
        sheets()
    else:
        download(sys.argv[1].lower(), [int(x) for x in sys.argv[2:]])
