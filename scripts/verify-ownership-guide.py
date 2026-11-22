"""Check rendered cash boundaries and the selective ownership consolidation."""
from pathlib import Path
from html.parser import HTMLParser
from decimal import Decimal
import csv,json,re,subprocess,hashlib,importlib.util,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1];O='https://www.drconnorrobertsonbooks.com';PATH='/blog/real-estate-ownership-mistakes/'
class Page(HTMLParser):
 def __init__(self):super().__init__();self.tables=[];self.row=None;self.cell=None;self.meta={};self.canon=[];self.h1=0;self.schemas=[];self.script=None;self.links=[];self.regions=[]
 def handle_starttag(self,t,a):
  a=dict(a)
  if t=='h1':self.h1+=1
  if t=='meta':self.meta[a.get('name',a.get('property',''))]=a.get('content','')
  if t=='link'and a.get('rel')=='canonical':self.canon.append(a['href'])
  if t=='a'and a.get('href'):self.links.append(a['href'])
  if a.get('role')=='region':self.regions.append(a)
  if t=='table':self.tables.append([])
  if t=='tr':self.row=[]
  if t in['th','td']:self.cell=[]
  if t=='script'and a.get('type')=='application/ld+json':self.script=[]
 def handle_data(self,d):
  if self.cell is not None:self.cell.append(d)
  if self.script is not None:self.script.append(d)
 def handle_endtag(self,t):
  if t in['th','td']and self.cell is not None:self.row.append(''.join(self.cell));self.cell=None
  if t=='tr':self.tables[-1].append(self.row);self.row=None
  if t=='script'and self.script is not None:self.schemas.append(json.loads(''.join(self.script)));self.script=None

def check(html):
 p=Page();p.feed(html);assert p.h1==1 and p.canon==[O+PATH];assert 'noindex'not in p.meta['robots']
 assert len(p.tables)==1 and len(p.tables[0])==4 and all(len(r)==6 for r in p.tables[0])
 expected=[['$14,000','$6,000','$8,000','$1,000','$9,000'],['$10,000','$6,000','$4,000','$1,000','$5,000'],['$10,000','$4,000','$6,000','−$1,000','$5,000']]
 assert [r[1:]for r in p.tables[0][1:]]==expected,'Rendered monthly cash cells changed'
 for row in p.tables[0][1:]:
  nums=[Decimal(x.replace(',','').replace('$','').replace('−','-'))for x in row[1:]];b,r,br,pr,total=nums;assert b-r==br and r-1800-3200==pr and br+pr==total==b-1800-3200
 nodes=[n for obj in p.schemas for n in obj.get('@graph',[obj])];article=next(n for n in nodes if n.get('@type')=='Article');assert article['datePublished']=='2026-09-23' and article['dateModified']=='2026-11-21' and article['author']['name']=='Robertson Books';assert not any(n.get('@type')=='FAQPage'for n in nodes)
 assert article['headline']==p.meta['og:title']==p.meta['twitter:title'];assert article['description']==p.meta['description']==p.meta['og:description']==p.meta['twitter:description'];assert p.regions and p.regions[0]['tabindex']=='0'
 for text in['fictional','not financial statements','not a consolidation procedure','not permission to reduce','cash available to distribute']:assert text in html
 return p
html=(ROOT/PATH.lstrip('/')/'index.html').read_text();p=check(html)
bad=html.replace('<td>$9,000</td>','<td>$9,001</td>',1);assert bad!=html
try:check(bad)
except AssertionError:pass
else:raise AssertionError('Incorrect cash result accepted')
rows=list(csv.reader((ROOT/'assets/fictional-business-property-cash.csv').open(newline='')));assert len(rows)==4 and all(len(r)==8 for r in rows)
for row in rows[1:]:
 b,r,c,d,br,pr,total=map(Decimal,row[1:]);assert b-r==br and r-c-d==pr and br+pr==total==b-c-d
spec=importlib.util.spec_from_file_location('renderer',ROOT/'scripts/render-ownership-guide.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
retired={O+'/blog/'+s+'/'for s in m.RETIRED};cfg=json.loads((ROOT/'vercel.json').read_text());rules=cfg['redirects'];assert len(rules)==26 and len({r['source']for r in rules})==26
for s in m.RETIRED:
 for slash in['','/']:
  rule=next(r for r in rules if r['source']=='/blog/'+s+slash);assert rule['destination']==PATH and rule['permanent']is True
ns='{http://www.sitemaps.org/schemas/sitemap/0.9}'
def records(text):return {e.find(ns+'loc').text:ET.tostring(e)for e in ET.fromstring(text)}
old=records(subprocess.check_output(['git','show','HEAD:sitemap.xml'],cwd=ROOT));new=records((ROOT/'sitemap.xml').read_text());assert len(new)==426 and set(old)-set(new)==retired and not set(new)-set(old)
for url in new:
 if url!=O+PATH:assert old[url]==new[url],url
archive=Page();archive.feed((ROOT/'blog/index.html').read_text());assert archive.links.count(PATH)==1
for f in ROOT.rglob('*.html'):
 if '.git'in f.parts:continue
 page=Page();page.feed(f.read_text());assert not any((O+link if link.startswith('/')else link)in retired for link in page.links),f
for route in['resources/read-function-composition-before-ai-explanation/index.html','resources/read-book-equation-before-ai-explanation/index.html','resources/read-conditional-probabilities-before-ai-summary/index.html','resources/read-appendix-before-ai-book-summary/index.html','books/built-to-run/chapters/2/index.html']:
 assert (ROOT/route).read_bytes()==subprocess.check_output(['git','show','HEAD:'+route],cwd=ROOT),route
before={str(f.relative_to(ROOT)):hashlib.sha256(f.read_bytes()).hexdigest()for f in ROOT.rglob('*')if f.is_file()and'.git'not in f.parts and'__pycache__'not in f.parts}
m.render()
after={str(f.relative_to(ROOT)):hashlib.sha256(f.read_bytes()).hexdigest()for f in ROOT.rglob('*')if f.is_file()and'.git'not in f.parts and'__pycache__'not in f.parts};assert before==after,'Selective renderer not idempotent'
print(json.dumps({'cashCases':3,'csvColumns':8,'actualRenderedArithmetic':'passed','wrong9001NegativeControl':'rejected','sitemapOwners':426,'retiredVariants':9,'permanentRules':26,'unrelatedSitemapDates':'preserved','protectedAuthoredPages':5,'rendererRepeat':'stable','staleFAQSchema':'removed','archiveTopicLinks':1}))
