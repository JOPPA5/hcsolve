from pathlib import Path
import argparse,json,html,textwrap,subprocess,sys,re
from reportlab.platypus import SimpleDocTemplate,Paragraph,Preformatted,PageBreak,Table,TableStyle,Image
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT=next(p for p in Path(__file__).resolve().parents if (p/'README.md').exists() and (p/'ciphers').exists());CIPHER=ROOT/'ciphers/hcp-374'
ap=argparse.ArgumentParser();ap.add_argument('--output-dir',type=Path,default=Path(__file__).parent/'draft-report');ap.add_argument('--final',action='store_true');args=ap.parse_args()
if args.final:assert (CIPHER/'REVIEWED1').exists() and not (CIPHER/'FINAL').exists()
args.output_dir.mkdir(parents=True,exist_ok=True)
font=Path('/Users/tomaspavuk/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/libreoffice-headless/libreoffice/LibreOfficeDev.app/Contents/Resources/fonts/truetype')
for name,file in [('DV','DejaVuSans.ttf'),('DVB','DejaVuSans-Bold.ttf'),('DVM','DejaVuSansMono.ttf')]:pdfmetrics.registerFont(TTFont(name,str(font/file)))
styles=getSampleStyleSheet()
for name in ['Normal','Title','Heading2']:styles[name].fontName='DV'
styles['Normal'].fontSize=9;styles['Normal'].leading=13;styles['Normal'].spaceAfter=9
styles['Title'].fontName='DVB';styles['Title'].fontSize=20;styles['Title'].leading=25;styles['Title'].spaceAfter=15
styles['Heading2'].fontName='DVB';styles['Heading2'].fontSize=11;styles['Heading2'].leading=15;styles['Heading2'].spaceBefore=10;styles['Heading2'].spaceAfter=7
mono=ParagraphStyle('mono',fontName='DVM',fontSize=7.5,leading=11,spaceAfter=9)
key=json.loads((CIPHER/'work/key.json').read_text());decoded=json.loads(subprocess.check_output([sys.executable,str(CIPHER/'work/decrypt.py'),'--json']))
story=[];md=[]
def p(text):
    text=re.sub(r'(?<=[^\W\d_])(?=\d)|(?<=\d)(?=[^\W\d_])',' ',text)
    story.append(Paragraph(html.escape(text),styles['Normal']));md.append(text)
def h(text):story.append(Paragraph(html.escape(text),styles['Heading2']));md.append('## '+text)
def literal(text):story.append(Preformatted('\n'.join(textwrap.wrap(text,90)),mono));md.append('```text\n'+text+'\n```')
def footer(canvas,doc):
    canvas.setFont('DV',7);canvas.setFillColor(colors.HexColor('#566174'));canvas.drawString(42,25,'HC Portal 374 | '+('Reviewed partial historical claim' if args.final else 'Review pending - draft')+' | 12 October 2026');canvas.drawRightString(A4[0]-42,25,str(doc.page))

story.append(Paragraph('HC374: madridský telegram',styles['Title']));md.append('# HC374: madridský telegram')
p('Obnovené telo správy a pracovný kľúč Kryha. Dešifrovaných je80 znakov. KIDAH je spoločný indikátor rovnakého štartu ako v373; spôsob kódovania nastavenia jeho písmenami zostáva otvorený. Historické neistoty sú výslovne označené.')
h('Pôvod a obsah')
p('MZV80174/1944, 20. máj1944, Šulík pre slovenské vyslanectvo v Madride. Slovenský národný archív, MZV, škatuľa42. Portál pri získaní uvádzal Not solved. Sken obsahuje počet85 a17 skupín po5 písmen. Názov opisuje žiadosť o opakovanie15 posledných skupín80172; nový80-znakový blok nie je vyhlásený za presne rovnaký75-znakový výrez.')
p('Zverejnený vyriešený telegram373 (80172/1944, 17. máj1944) poskytol archívny otvorený návrh a šifrotext. Jeho záverečná veta slúžila ako známy text na obnovu strojového kľúča. Obchodný obsah je týmto zdrojom doložený a už bol zverejnený; nové je získanie kľúča a jeho prenos na374.')
h('Doslovný výstup z nezávislého prepisu')
literal(decoded['body_plaintext_literal'].upper())
p('Samostatný indikátor: KIDAH, spoločný s373 a rovnakým štartom stroja. Recenzovaný znak35 je N; alternatíva M dáva PROTIBODVVKY. SPANLELSKE a PROTIBODAVKY zachovávajú dve chybné písmená tejto kópie. Zdroj sa neupravuje podľa správnych slov. XXXX je výplň X doložená vetnými X a záverečnými XX v373.')
h('Čitateľný obsah doložený návrhom 373')
p('A upozorňuje španielské protidodávky už pevne kúpené na základe pôvodných cien celulózy.')
p('Význam: španielske protidodávky sú už pevne kúpené podľa pôvodných cien celulózy. Anglicky: And points out that the Spanish counter-deliveries have already been firmly purchased on the basis of the original cellulose prices. Toto je obsahová obnova podľa zverejneného návrhu, nie doslovný strojový výstup bez chýb.')
h('Ako sa kľúč získal')
p('Posledná186-písmenová veta373 neobsahuje čísla. Jej posúvanie cez celý šifrotext a skúšanie periód2-52 dáva jeden výsledok z94 656 prípadov: J na I, bez Q, posun462, perióda23. Všetkých183 neistotami nevynechaných rovníc súhlasí. Tri nezávislé fyzické kontrolné správy sa obnovia celé. Dva odlišné audity potvrdili jednu kompatibilnú23-stopovú masku na52-otvorovom kolese.')
p('Pri374 je zo598 dvojíc fázy a posunu jednoznačne najlepší prenos3/8: recenzované čítanie súhlasí v74 zo76 obsahových písmen; ďalší kandidát iba21, medián3. Nezávislé čítania vznikli pred znalosťou kľúča. Ten istý kľúč otvára celý645-znakový šifrovaný blok373:459 znakov mimo použitého186-znakového úseku. Súvislá slovenčina s vypísanými číslami a vetnými X je silné nezávislé potvrdenie; jednotlivé zdrojové chyby sú zachované.')

story.append(PageBreak());h('Pracovný fyzický kľúč')
p('P a O určujú súradnicu písmena0-25; O(c)=P(p)+d modulo26. P(A)=O(A)=0 je súradnicová konvencia. Tabuľka dopĺňa nepoužité F/G/J/Q/W do permutácie; tieto historické názvy sa nezískali. M24 pochádza z nezávislého známeho MADRID v373, X19 potvrdzujú tamojšie vetné hranice a výplň XX. Nepoužité doplnenia nemenia telo374.')
for start in [0,13]:
    letters=[chr(65+i) for i in range(start,start+13)]
    rows=[['Písmeno']+letters,['P']+key['input_positions'][start:start+13],['O']+key['output_positions'][start:start+13]]
    table=Table(rows,colWidths=[52]+[34]*13,hAlign='LEFT');table.setStyle(TableStyle([('FONTNAME',(0,0),(-1,-1),'DV'),('FONTSIZE',(0,0),(-1,-1),8),('BACKGROUND',(0,0),(-1,0),colors.HexColor('#edf1f5')),('GRID',(0,0),(-1,-1),0.3,colors.HexColor('#cad2dc')),('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5)]));story.append(table);md.append('\n'.join('| '+' | '.join(map(str,row))+' |' for row in rows))
p('Vybrané otvory v poradí od prvého znaku tela, NULOVÉ indexovanie0-51 (pre čísla1-52 pripočítajte1):')
literal(' '.join(map(str,key['holes_zero_based'])))
p('Počiatočný posun1 modulo26 (ekvivalent27). Po každom znaku sa ide k nasledujúcemu vybranému otvoru po susedných hranách. Ich52 vzdialeností:')
literal(' '.join(map(str,key['adjacent_distances'])))
p('Súčet jedného obehu je179. Pri dekódovaní sa od O odčíta aktuálny posun a v P sa vyhľadá výsledná súradnica. Historická poloha ručičky, význam úvodného hesla a každý nepoužitý názov abecedy zostávajú nepreukázané. Jedinečnosť masky platí iba pre uvedenú geometriu a obnovený rozvrh.')
h('Opakovateľnosť a nezávislé overenie')
literal('python3 ciphers/hcp-374/work/decrypt.py')
p('Spustiť z koreňa repozitára. Python overí hash pôvodného JPEG a ručného prepisu; nerobí OCR. Vráti všetkých80 písmen a indikátor zvlášť. --alternate-35-m volí druhé čítanie. Samostatné verify.py používa absolútne súradnice a počet obehov. Interný audit GPT-6.1 Sol použil vlastný priebežný mechanický algoritmus bez importu týchto funkcií: obe80-písmenové verzie presne reprodukujú skutočný prepis.')
h('Recenzia a hranice výsledku')
review=CIPHER/'review/REVIEW1.md'
if args.final:
    verdict=review.read_text().splitlines()[0];p('Claude Opus5.5: '+verdict+', bez potreby druhého kola. Vlastný decoder overil celé telo, 598 nastavení a celý blok373 mimo prvého rámca. Zapracované: N na35 so zachovaným M, silný test459 znakov mimo fitu, doložené X a dve chyby tejto kópie. Pôvodné15 skupín sa pri opakovaní rozšíria na slovo a zaokrúhlia na16; ide o vysvetľujúci úsudok. Plné odpovede sú v SOLUTION.md.')
else:p('Externá recenzia prebieha. Tento pracovný návrh nie je konečný report ani potvrdenie úplného historického riešenia.')
p('Zdroj9/25/60 čitatelia preferujú G/Q/V. Na35 je predvolené staršie nezávislé N, novší čitateľ M zostáva alternatívou. Zdroj21S a32L sa nemenia na W/A: ide o chyby tejto kópie, s neurčeným pôvodom. Aktualizovaná recenzia potvrdzuje KIDAH a spoločný štart (prvá vybraná stopa, posun1). V373 veta začína až po567 znakoch, v374 znova od štartu: z76 šifrových písmen nesúhlasí žiadne, z otvorených74. Text bol zašifrovaný znova, nie prekopírovaný; kódovanie indikátora zostáva otvorené. Register bez osobitného súhlasu človeka nevzniká, obsah už bol publikovaný.')
p('Zdroje: crypto.hcportal.eu/dashboard/cryptograms/374 a /373, všetky tri pôvodne zobrazené záložky a prílohy zaznamenané v SOURCES.md; Antal/Zajac/Grošek, Diplomatic Ciphers Used by Slovak Attaché During the WW2, HistoCrypt2020; geometria Callimahos, Military Cryptanalytics Part III, §52. Hlavný solver OpenAI GPT, matematická obnova a interné audity GPT-6.1 Sol; externý reviewer podľa REVIEW1.md.')

story.append(PageBreak());h('Pôvodný dokument 374')
p('Nezmenený archívny obraz zo zaznamenanej portálovej prílohy. Ručný prepis a alternatívy sú od obrazu oddelené.')
image=Image(str(CIPHER/'source/cryptogram.jpg'));image.drawWidth=505;image.drawHeight=505*image.imageHeight/image.imageWidth;story.append(image)
md.append(f'![Pôvodný sken]({CIPHER}/source/cryptogram.jpg)')
(args.output_dir/'report.md').write_text('\n\n'.join(md)+'\n')
SimpleDocTemplate(str(args.output_dir/'report.pdf'),pagesize=A4,leftMargin=42,rightMargin=42,topMargin=38,bottomMargin=42,title='HCP374: reviewed Madrid telegram',author='OpenAI GPT solver; GPT-6.1 Sol solver team; Claude Opus5.5 review').build(story,onFirstPage=footer,onLaterPages=footer)
print(args.output_dir/'report.pdf')
