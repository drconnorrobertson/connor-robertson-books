"""Check the authored handoff, its CSV and the selective consolidation."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit
import json,re,csv,subprocess,hashlib,importlib.util
ROOT=Path(__file__).resolve().parents[1];O='https://www.drconnorrobertsonbooks.com';ROUTE='/blog/operating-systems-mistakes/'
data=json.loads((ROOT/'content/operating-handoff-guide.json').read_text());s=(ROOT/ROUTE.lstrip('/')/'index.html').read_text()
assert len(re.findall(r'<h1\b',s))==1 and '<link rel="canonical" href="'+O+ROUTE+'"'in s
assert '2026-09-23'in s and '2026-11-21'in s
assert 'not a manuscript excerpt'in s and 'fictional'in s
for raw in re.findall(r'<script[^>]*application/ld\+json[^>]*>(.*?)</script>',s,re.S):
 obj=json.loads(raw)
 for n in obj.get('@graph',[obj]):
  assert n.get('@type')!='FAQPage'
  if n.get('@type')=='Article':assert n['datePublished']=='2026-09-23'and n['dateModified']=='2026-11-21'
ids=set(re.findall(r'id="([^"]+)"',s));assert all(x in ids for x in re.findall(r'href="#([^"]+)"',s))
rows=list(csv.DictReader((ROOT/'workflow-assets/fictional-operating-handoff-review.csv').open(newline='')));assert len(rows)==5 and all(x['fictional']=='true'for x in rows)
assert len({x['record']for x in rows})==5
assert sum(x['active_unique_request']=='yes'for x in rows)==3
assert {state:sum(x['state']==state for x in rows)for state in ['accepted','blocked','duplicate','withdrawn']}=={'accepted':2,'blocked':1,'duplicate':1,'withdrawn':1}
class Cells(HTMLParser):
 def __init__(self):super().__init__();self.inside=False;self.row=None;self.cell=None;self.rows=[]
 def handle_starttag(self,t,a):
  if t=='tbody':self.inside=True
  if self.inside and t=='tr':self.row=[]
  if self.inside and t in ['td','th']:self.cell=[]
 def handle_data(self,d):
  if self.cell is not None:self.cell.append(d)
 def handle_endtag(self,t):
  if t in ['td','th']and self.cell is not None:self.row.append(''.join(self.cell));self.cell=None
  if t=='tr'and self.row is not None:self.rows.append(self.row);self.row=None
  if t=='tbody':self.inside=False
p=Cells();p.feed(data['body']);assert len(p.rows)==5
for c,h in zip(rows,p.rows):assert c['record']==h[0]and c['active_unique_request']==h[2].lower()
retired=['operating-systems-'+x for x in ['field-guide','scorecard','questions','checklist','examples','red-flags','implementation','faq','advanced']]
config=json.loads((ROOT/'vercel.json').read_text());rules={r['source']:r for r in config['redirects']}
for slug in retired:
 for slash in['','/']:assert rules['/blog/'+slug+slash]=={'source':'/blog/'+slug+slash,'destination':ROUTE,'permanent':True}
import xml.etree.ElementTree as E
entries=E.parse(ROOT/'sitemap.xml').getroot();urls=[e.find('{*}loc').text for e in entries];assert len(urls)==len(set(urls))==417 and O+ROUTE in urls
assert all(O+'/blog/'+slug+'/'not in urls for slug in retired)
for p in ROOT.rglob('*.html'):
 if '.git'in p.parts or p.parent.name in retired:continue
 for href in re.findall(r'href="([^"]+)"',p.read_text()):assert urlsplit(href).path.rstrip('/').split('/')[-1]not in retired,(p,href)
protected=['resources/read-book-equation-before-ai-explanation/index.html','resources/read-conditional-probabilities-before-ai-summary/index.html','resources/read-appendix-before-ai-book-summary/index.html','resources/read-function-composition-before-ai-explanation/index.html','books/built-to-run/chapters/2/index.html','blog/real-estate-ownership-mistakes/index.html']
for file in protected:assert (ROOT/file).read_bytes()==subprocess.check_output(['git','show','HEAD:'+file],cwd=ROOT),file
# The real authored renderer must be stable on a second run.
files=[p for p in ROOT.rglob('*.html')if '.git'not in p.parts]+[ROOT/'sitemap.xml',ROOT/'vercel.json'];before={str(p):hashlib.sha256(p.read_bytes()).hexdigest()for p in files}
spec=importlib.util.spec_from_file_location('operating_renderer',ROOT/'scripts/render-operating-guide.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);m.render()
assert before=={str(p):hashlib.sha256(p.read_bytes()).hexdigest()for p in files}
print(json.dumps({'fictionalRows':5,'activeRequests':3,'accepted':2,'blocked':1,'tableCSVBridge':'passed','protectedAuthoredPages':6,'retiredVariants':9,'directRules':18,'sitemapOwners':417,'rendererRepeat':'stable'}))
