"""Verify transition cash/date arithmetic, source links and consolidation boundaries."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit
from datetime import date,timedelta
import csv,json,hashlib,subprocess,tempfile,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1];base='https://www.drconnorrobertsonbooks.com';overview='/books/buying-wealth/';route=overview+'transition-review/'
d=json.loads((ROOT/'content/transition-review-guide.json').read_text());html=(ROOT/(route.strip('/')+'/index.html')).read_text()
rows=list(csv.DictReader((ROOT/'workflow-assets/fictional-transition-review.csv').open()))
assert [r['packet_id'] for r in rows]==['E01','X01','L01'] and all(r['fictional']=='true' and r['observed_review']=='' for r in rows)
assert 900000-45000==855000 and 900000-45000-420000==435000
transfer=date(2026,11,20);identification=transfer+timedelta(days=45);receipt180=transfer+timedelta(days=180);assumedReturnDue=date(2027,4,15)
assert identification==date(2027,1,4) and receipt180==date(2027,5,19) and min(receipt180,assumedReturnDue)==assumedReturnDue
for phrase in ['not a manuscript excerpt','not a determination of a real taxpayer','Do not substitute the $420,000 debt balance for adjusted basis','Timing alone does not establish qualification','not a finding that no authority exists anywhere']:
 assert phrase in html,phrase
for source in d['sources']:assert 'href="'+source['url']+'"' in html
assert len(d['sources'])==3 and 'Publication 544 (2025)' in html and 'Form 8824 (2026)' in html
class Page(HTMLParser):
 def __init__(self):super().__init__();self.ids=[];self.links=[];self.canonicals=[];self.noindex=False
 def handle_starttag(self,t,a):
  a=dict(a)
  if 'id' in a:self.ids.append(a['id'])
  if t=='a':self.links.append(a.get('href',''))
  if t=='link' and a.get('rel')=='canonical':self.canonicals.append(a.get('href'))
  if t=='meta' and a.get('name')=='robots' and 'noindex' in a.get('content','').lower():self.noindex=True
p=Page();p.feed(html);assert p.canonicals==[d['canonical']] and not p.noindex and len(p.ids)==len(set(p.ids));assert all(s['id'] in p.ids for s in d['sections'])
cfg=json.loads((ROOT/'vercel.json').read_text());rules={r['source']:r for r in cfg['redirects']};assert len(rules)==len(cfg['redirects'])==476
retired={overview+f'chapters/{n}/' for n in [9,10]}
for number,anchor in [(9,'sale'),(10,'authority')]:
 old=overview+f'chapters/{number}/';assert not (ROOT/(old.strip('/')+'/index.html')).exists()
 for form in [old,old[:-1]]:assert rules[form]=={'source':form,'destination':route+'#'+anchor,'permanent':True}
for path in ROOT.rglob('*.html'):
 if '.git' in path.parts:continue
 q=Page();q.feed(path.read_text())
 for link in q.links:
  u=urlsplit(link)
  if not u.netloc or u.netloc=='www.drconnorrobertsonbooks.com':assert u.path not in retired and u.path+'/' not in retired,(path,link)
records=lambda b:{e.find('{*}loc').text:ET.tostring(e) for e in ET.fromstring(b)}
before=records(subprocess.check_output(['git','show','HEAD:sitemap.xml'],cwd=ROOT));after=records((ROOT/'sitemap.xml').read_bytes());assert len(after)==409 and set(before)-set(after)=={base+x for x in retired} and set(after)-set(before)=={d['canonical']};assert all(before[u]==after[u] for u in before.keys()&after.keys() if u!=base+overview)
protected=['books/built-to-run/chapters/'+str(n)+'/index.html' for n in [1,2,6]]+['books/built-to-run/operations-review/index.html','books/creative-acquisitions/decision-review/index.html','books/the-7-minute-phone-call/follow-up-review/index.html','blog/real-estate-ownership-mistakes/index.html','blog/operating-systems-mistakes/index.html','resources/read-function-composition-before-ai-explanation/index.html','resources/read-book-equation-before-ai-explanation/index.html','resources/read-conditional-probabilities-before-ai-summary/index.html','resources/read-appendix-before-ai-book-summary/index.html']
for path in protected:assert (ROOT/path).read_bytes()==subprocess.check_output(['git','show','HEAD:'+path],cwd=ROOT),path
for match in __import__('re').findall(r'<script type="application/ld\+json">([\s\S]*?)</script>',html):json.loads(match)
def snapshot():return {str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in ROOT.rglob('*') if p.is_file() and '.git' not in p.parts and '__pycache__' not in p.parts}
old=snapshot();subprocess.run(['python3','scripts/render-transition-review-guide.py'],cwd=ROOT,check=True);assert snapshot()==old
source=(ROOT/'generate_site.py').read_text();previous=subprocess.check_output(['git','show','HEAD:generate_site.py'],cwd=ROOT,text=True)
with tempfile.TemporaryDirectory(prefix='books-followup-generator-') as name:
 outputs=[]
 for i,code in enumerate([previous,source]):
  stage=Path(name)/str(i);stage.mkdir();ns={'__file__':str(ROOT/'generate_site.py'),'__name__':'follow_up_verification'};exec(compile(code,'actual-book-generator','exec'),ns);ns['OUTPUT_DIR']=str(stage)
  for book in ns['BOOKS']:ns['generate_book_landing'](book)
  outputs.append({book['slug']:(stage/f"books/{book['slug']}/index.html").read_bytes() for book in ns['BOOKS']})
  if i==1:assert route.encode() in outputs[-1]['buying-wealth']
 assert all(outputs[0][book]==outputs[1][book] for book in outputs[0] if book!='buying-wealth')
print('PASS:409owners;476redirects;threefictionalpackets;cashanddatearithmeticverified;12authoredpagespreserved;otherthreebookgeneratorsidentical;rendererstable;nostaleinternallinks;primarysourceslinked')
