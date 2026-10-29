"""Retrieve selected public DTA ZIP members with HTTP ranges and CRC validation.

No verification cookies, login or challenge bypass. The openly downloadable
archive serves ordinary HTTP 206 responses. Original extracted XML is immutable.
The cached central-directory index was parsed from the public ZIP directory.
"""
from pathlib import Path
import concurrent.futures, hashlib, json, struct, subprocess, tempfile, zlib

ROOT=Path(__file__).resolve().parents[1]
URL='https://media.dwds.de/dta/download/dta_kernkorpus_2020-07-20.zip'
IDS='butschky_kantzeley_1649 seckendorff_fuerstenstaat_1656 pufendorf_bericht_1667 wartmann_germania01_1650 wartmann_germania0203_1650 wartmann_germania04_1652 wartmann_germania05_1653 olearius_reise_1647 grimmelshausen_simplicissimus_1669'.split()
index=json.loads((ROOT/'work/dta-archive-index.json').read_text())
outdir=ROOT/'source/dta-period';outdir.mkdir(exist_ok=True)

def fetch(identifier):
    name=identifier+'.TEI-P5.xml'
    row=next(r for r in index if Path(r['name']).name==name)
    out=outdir/name
    if out.exists():
        data=out.read_bytes()
    else:
        # Up to 512 bytes for the local header; actual data start is read below.
        start=row['offset'];end=start+row['compressed']+511
        data_range=subprocess.check_output(['curl','-fsSL','--max-time','45',
            '--max-filesize',str(row['compressed']+1024),'-r',f'{start}-{end}',URL])
        header=struct.unpack('<4s5H3I2H',data_range[:30])
        assert header[0]==b'PK\x03\x04' and header[3]==8
        nlen,xlen=header[9:11]
        assert data_range[30:30+nlen].decode()==row['name']
        offset=30+nlen+xlen
        assert offset<=512
        data=zlib.decompress(data_range[offset:offset+row['compressed']],-15)
    assert len(data)==row['uncompressed'] and zlib.crc32(data)==row['crc']
    if not out.exists():out.write_bytes(data)
    return {**row,'archive_url':URL,'local_path':str(out.relative_to(ROOT)),
            'sha256':hashlib.sha256(data).hexdigest(),'crc_validated':True}

with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
    records=list(pool.map(fetch,IDS))
(ROOT/'work/period-corpus-sources.json').write_text(json.dumps(records,indent=2)+'\n')
print(json.dumps({'files':len(records),'compressed_bytes':sum(r['compressed'] for r in records),
                  'xml_bytes':sum(r['uncompressed'] for r in records),'crc_validated':True}))
