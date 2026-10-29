#!/usr/bin/env python3
"""One public GET per METS DOWNLOAD URL; no JPEG retry or URL guessing."""
import concurrent.futures
import datetime
import hashlib
import json
from pathlib import Path
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET

BASE=Path(__file__).resolve().parent
METS=BASE.parent.parent/'enclosure-context-2026-10-28'/'lasa-raumer-mets.xml'
NS={'m':'http://www.loc.gov/METS/'}
WANTED=(5,6,8,11)

def fetch(row):
    row={**row,'attempted_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
    try:
        req=urllib.request.Request(row['url'],headers={'User-Agent':'Mozilla/5.0 (historical archive research)'})
        with urllib.request.urlopen(req,timeout=35) as resp:
            data=resp.read()
            row.update(status=resp.status,final_url=resp.url,content_type=resp.headers.get('Content-Type'),bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
        if data.startswith(b'%PDF-'):
            out=BASE/f"{row['page']:03}.pdf"
            out.write_bytes(data)
            row.update(file=out.name,pdf_magic=True)
        else:
            row.update(pdf_magic=False,error='Response is not PDF by magic bytes; not treated as recovered scan.')
    except urllib.error.HTTPError as e:
        data=e.read()
        row.update(status=e.code,error=str(e),error_body_bytes=len(data),error_body_sha256=hashlib.sha256(data).hexdigest())
    except Exception as e:
        row.update(error=f'{type(e).__name__}: {e}')
    return row

if __name__=='__main__':
    dest=BASE/'manifest.json'
    if dest.exists():
        raise SystemExit('manifest.json already exists: stopping to prevent repeated requests')
    rows=[]
    for g in ET.parse(METS).getroot().findall('.//m:fileGrp',NS):
        if g.get('USE')!='DOWNLOAD':
            continue
        for f in g.findall('m:file',NS):
            u=f.find('m:FLocat',NS).get('{http://www.w3.org/1999/xlink}href')
            for page in WANTED:
                if u.endswith(f'__{page:04}.pdf'):
                    rows.append({'page':page,'file_id':f.get('ID'),'declared_mimetype':f.get('MIMETYPE'),'url':u})
    assert sorted(r['page'] for r in rows)==list(WANTED)
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        records=list(pool.map(fetch,rows))
    dest.write_text(json.dumps({'mets_file':str(METS),'mets_sha256':hashlib.sha256(METS.read_bytes()).hexdigest(),'records':records},indent=2)+'\n')
    for row in records:
        print(json.dumps(row))
