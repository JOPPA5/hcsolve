#!/usr/bin/env python3
"""Threshold/connected-component comparison; not an OCR decipherment.
Controls are manually selected from the fixed main-message transcription.
No cropped/resized/filtered pixels are used for measurements.
"""
import hashlib,json,math
from pathlib import Path
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]
for name,digest in json.loads((ROOT/'work/source-sha256.json').read_text()).items():
    assert hashlib.sha256((ROOT/'source'/name).read_bytes()).hexdigest()==digest
im=Image.open(ROOT/'source/picture.jpg').convert('L')
ROIS={
 'R_in_WEARING':(923,148,950,155),
 'R_in_WEAR':(923,486,952,493),
 'S_in_SKULL':(927,199,945,206),
 'terminal_upper':(928,585,972,600),
 'terminal_lower':(928,601,971,614),
}
def components(box,threshold):
    x0,y0,x1,y1=box
    dark={(x,y) for y in range(y0,y1) for x in range(x0,x1) if im.getpixel((x,y))<threshold}
    out=[]
    while dark:
        start=min(dark); dark.remove(start); todo=[start]; pts=[]
        while todo:
            x,y=todo.pop();pts.append((x,y))
            for p in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                if p in dark:dark.remove(p);todo.append(p)
        if len(pts)>=3:
            out.append({'centre':[sum(p[i] for p in pts)/len(pts) for i in (0,1)],'pixels':len(pts)})
    out.sort(key=lambda c:c['centre'][0]);return out
results=[]
for threshold in [90,100,110,120,130,140,150]:
    for name,box in ROIS.items():
        cs=components(box,threshold)
        result={'threshold':threshold,'region':name,'box':box,'components':cs}
        if len(cs)==3:
            gaps=[math.dist(cs[i]['centre'],cs[i+1]['centre']) for i in [0,1]]
            result.update(gaps=gaps,first_to_second_gap_ratio=gaps[0]/gaps[1])
            print(f'{threshold:3d} {name:18s} gaps={gaps[0]:.2f}/{gaps[1]:.2f} ratio={gaps[0]/gaps[1]:.3f}')
        else:print(f'{threshold:3d} {name:18s} {len(cs)} components (no ratio)')
        results.append(result)
(ROOT/'work/terminal-pixel-measurements.json').write_text(json.dumps({'provenance':'Grayscale threshold followed by 4-connected components, area >=3 native pixels. ROI selections manual; no automatic semantic identification or statistically calibrated classifier.','results':results},indent=2)+'\n')
