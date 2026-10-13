from pathlib import Path
import shutil,hashlib,json
root=Path(__file__).resolve().parents[2]
rows=[(1218,'cpc_1912-09-_HU__HU_Jasz-Arokszalas_jolanka-106',3714,3715,'9.1912'),(1217,'cpc_1912-10-02_HU__HU_Jasz-Arokszalas_jolanka-31',3711,3712,'1912-10-02'),(1216,'cpc_--_HU__HU_Jasz-Arokszalas_jolanka-64',3708,3709,'Unknown'),(1213,'cpc_1913--_HU__HU_Jasz-Arokszalas_jolanka-108',3699,3700,'1913'),(1212,'cpc_1912-02-17_HU__HU_Jasz-Arokszalas_jolanka-05',3696,3697,'1912-02-17')]
for n,stem,pic,adr,date in rows:
 p=root/f'ciphers/hcp-{n}';(p/'source').mkdir(parents=True,exist_ok=True);(p/'work').mkdir(exist_ok=True)
 lines=[f'# HCP{n} sources\n','Captured 2026-10-12 through the rendered portal General, Description and Attachments tabs. Status: **Not solved**.\n',f'Portal: https://crypto.hcportal.eu/dashboard/cryptograms/{n}\n']
 for side,suf,media in [('picture','pic',pic),('address','adr',adr)]:
  fname=f'{stem}_{suf}-large.jpg';src=Path('/Users/tomaspavuk/Downloads')/fname;dest=p/'source'/f'{side}.jpg'
  if not dest.exists():shutil.copyfile(src,dest)
  assert src.read_bytes()==dest.read_bytes()
  lines.append(f'- {side}.jpg: https://api.hcportal.eu/media/{media}/conversions/{fname} ; SHA256 {hashlib.sha256(dest.read_bytes()).hexdigest()}')
 metadata=f'''# HCP{n}: rendered portal metadata
Name: {stem.replace('Jasz-Arokszalas','Jasz Arokszalas')}
Status: Not solved
Category: Substitution
Date / Used Around: {date}
Language: Unknown
Location: Europe
Used chars: N/A
Availability: Private collection
Sender: Unknown
Recipient: Tóth Jolánka
Tags: Postcard; T. Schrödel Collection
Description: Tobias Schrödel's cryptographic postards collection.
Attachments: Picture side, Address side. No transcription or solution displayed.
Reference: https://ecp.ep.liu.se/index.php/histocrypt/article/view/166
'''
  
 if not (p/'source/metadata.md').exists():(p/'source/metadata.md').write_text(metadata)
 (p/'SOURCES.md').write_text('\n'.join(lines)+'\n')
 if not (p/'NOTES.md').exists():(p/'NOTES.md').write_text('# Work log\n\n2026-10-12: Selected through the Jolanka name filter in the rendered catalog, status Not solved. All three tabs read, both scans archived unchanged. Testing the alphabet established on HCP1301/1243 against these independent cards.\n')
print('Archived five new records and ten scans.')
