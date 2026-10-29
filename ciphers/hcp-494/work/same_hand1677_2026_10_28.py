"""Bounded 1672/1677 handwriting comparison and auxiliary whole-insert decoding.

Handwriting judgments are manual, not identification probabilities. The 1677
key is used only on its own auxiliary letter, never transferred to HCP 494.
"""
from pathlib import Path
import hashlib
import json
import textwrap
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / "work"
OUT = WORK / "same-hand-1677-2026-10-28"
SPECS = {
    "1672-hamburg": ("full/0002.jpg", (510, 1610, 1020, 1810), "1672: Hamburg, original body"),
    "1677-hamburg": ("arcinsys/daenemark145-0003.jpg", (1340, 1910, 1760, 2100), "1677: Hamburg, original body"),
    "1672-nicht": ("full/0003.jpg", (1780, 750, 2070, 960), "1672: nicht, original body"),
    "1677-nicht": ("arcinsys/daenemark145-0003.jpg", (590, 1160, 1050, 1360), "1677: nicht, original body"),
    "1672-und": ("full/0003.jpg", (1440, 570, 1810, 750), "1672: und, original body"),
    "1677-und": ("arcinsys/daenemark145-0003.jpg", (1260, 1030, 1520, 1240), "1677: und, original body"),
    "1672-subscription": ("full/0004.jpg", (1190, 3490, 2320, 3800), "1672: abbreviated subscription; no full surname control"),
    "1677-subscription": ("arcinsys/daenemark145-0005.jpg", (1200, 3260, 2510, 3830), "1677: full Lincker subscription; differing formula"),
    "1677-insert-p3": ("arcinsys/daenemark145-0003.jpg", (570, 2310, 2460, 2670), "1677 p3: complete selected numeric insert, two physical lines"),
    "1677-insert-p4": ("arcinsys/daenemark145-0004.jpg", (440, 1160, 1570, 1390), "1677 p4: repeated numeric name"),
    "1677-175": ("arcinsys/daenemark145-0003.jpg", (1930, 2700, 2390, 2910), "1677 p3: separate code 175 in original context"),
    "key1235-alphabet": ("arcinsys/key1235-0001.jpg", (30, 40, 3450, 770), "Key1235 alphabet: numeric groups and a graphic alphabet with repeated plaintext headings"),
}


def main():
    OUT.mkdir(exist_ok=True)
    manifest = json.loads((WORK / "source-sha256-2026-10-23-key1236.json").read_text())
    changed = [name for name, sha in manifest.items()
               if hashlib.sha256((ROOT / "source" / name).read_bytes()).hexdigest() != sha]
    if changed:
        raise SystemExit(f"Source preservation failure: {changed}")
    crops, records = {}, []
    for name, (source, box, label) in SPECS.items():
        path = ROOT / "source" / source
        im = Image.open(path).convert("RGB")
        assert 0 <= box[0] < box[2] <= im.width
        assert 0 <= box[1] < box[3] <= im.height
        crop = im.crop(box)
        crop.save(OUT / f"{name}.png")
        crops[name] = crop
        records.append({"name": name, "source": "source/" + source,
                        "rectangle_xyxy": box, "scale": 1,
                        "source_sha256": hashlib.sha256(path.read_bytes()).hexdigest(), "label": label})
    font_path = "/System/Library/Fonts/Supplemental/Arial.ttf"
    font = ImageFont.truetype(font_path, 24) if Path(font_path).exists() else ImageFont.load_default()
    board = Image.new("RGB", (1600, 1040), "white")
    draw = ImageDraw.Draw(board)
    for row, word in enumerate(("hamburg", "nicht", "und")):
        for col, year in enumerate(("1672", "1677")):
            name = f"{year}-{word}"
            x, y = 10 + col * 800, 10 + row * 310
            draw.text((x, y), SPECS[name][2], font=font, fill="black")
            board.paste(crops[name], (x, y + 45))
    for line_no, line in enumerate(textwrap.wrap(
        "Broad cursive similarities are not individual identification. Hamburg has differing capital/script forms; nicht and und are common cursive controls. No same-hand attribution is established. Native pixels, no ink alteration.", 120)):
        draw.text((10, 945 + line_no * 28), line, font=font, fill="black")
    board.save(OUT / "body-comparison.png")
    board = Image.new("RGB", (1360, 1110), "white")
    draw = ImageDraw.Draw(board)
    for name, y in (("1672-subscription", 10), ("1677-subscription", 410)):
        draw.text((10, y), SPECS[name][2], font=font, fill="black")
        board.paste(crops[name], (10, y + 45))
    draw.text((10, 1050), "Initials versus a full name do not supply a surname-to-surname hand comparison.", font=font, fill="black")
    board.save(OUT / "subscriptions.png")

    alphabet = "abcdefghiklmnopqrstuwxyz"
    key = {str(41 + 4*i + r): char for i, char in enumerate(alphabet) for r in range(4)}
    key.update({"320": "<General>", "175": "<King>"})
    rows = [
        {"page": 3, "tokens": "45 57 109 44 65 113 55 107 320 46 43 117 54 73 113 133".split(),
         "gloss_assisted_candidate": "besagter<General>bauditz"},
        {"page": 4, "tokens": "47 43 120 56 76 116 135".split(),
         "gloss_assisted_candidate": "bauditz"},
    ]
    for row in rows:
        row["literal_key_output"] = "".join(key[t] for t in row["tokens"])
    assert rows[0]["literal_key_output"] == "besagtdr<General>bauditz"
    assert rows[1]["literal_key_output"] == "bauditz"
    result = {
        "status": "SAME HAND NOT ESTABLISHED; no new HCP494 plaintext",
        "scope": "Existing original 1672 pages2-4 and auxiliary1677 pages2-5, plus key1235. Wrapper1677 page1 is archival description, not a writer control.",
        "manual_handwriting_assessment": {
            "Hamburg": "1672 has a broad two-stem/crossbar capital H; 1677 has a looped, differently linked form. This may be script choice or variation, and is not proof of different writers.",
            "nicht": "Both use a long descending/looping h-associated stroke. The 1677 form is larger and more angular; this is a common cursive construction, not distinctive enough to identify a writer.",
            "und": "Both have connected minims and a final rising d-form; length, height and connection differ. Shared ordinary cursive structure is insufficient to identify the hand.",
            "subscriptions": "The1672 subscription is abbreviated whereas1677 gives a full Lincker name. No secure full-name comparison or given-name assignment is made.",
            "confounders": "Five-year interval, script switching, pen/nib/ink, writing speed, formula and possible secretary/copyist. Authorship and the identity of the writing hand are separate questions.",
            "decision": "Do not promote the1677 samples to authenticated same-hand controls. Neither the same writer nor a different writer is proved."
        },
        "cipher_inventory": {
            "selected_inserts_total_tokens": sum(len(row["tokens"]) for row in rows),
            "letter_tokens": 22,
            "graphic_doubled_capital_tokens_found_in_inserts": 0,
            "additional_visible_numeric_code": {"page": 3, "token": "175", "key1235_output": "<King>", "limit": "Auxiliary letter only; does not transfer to HCP494."},
            "special_sign_control": "No independently identified PP/BB/II/XX or special ff in this1677letter. Key1235 has numeric and graphic alphabets; its repeated A-Z row supplies headings, not established additional single-capital ciphertext values. No key255-style doubled-capital/ff syllable row is displayed."
        },
        "selected_whole_insert_verification": rows,
        "known_difference": {"page": 3, "one_based_token_position": 7, "token": "55", "key1235": "d", "annotation_candidate": "e", "status": "Unresolved; no local override. Not proof of scribal error or a changed table."},
        "letter_matches_to_candidate": 21,
        "letter_tokens_compared": 22,
        "accuracy_limit": "This count describes only the selected auxiliary inserts after seeing annotations; it is not decipherment accuracy for HCP494 or independent validation.",
        "crops": records,
        "source_preservation": {"checked": len(manifest), "changed": changed},
        "changed_hcp494_key_cells": 0,
        "new_hcp494_plaintext": False,
        "independent_review": False,
    }
    (WORK / "same-hand-1677-2026-10-28.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"literal_auxiliary_outputs": [r["literal_key_output"] for r in rows], "source_preservation": result["source_preservation"]}))


if __name__ == "__main__":
    main()
