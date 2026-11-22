"""Check the consolidation's ownership, route, worksheet and regeneration boundaries."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit
import json,csv,subprocess,tempfile,xml.etree.ElementTree as ET,hashlib
ROOT=Path(__file__).resolve().parents[1];route='/books/built-to-run/operations-review/';base='https://www.drconnorrobertsonbooks.com'
d=json.loads((ROOT/'content/operations-review-guide.json').read_text());html=(ROOT/'books/built-to-run/operations-review/index.html').read_text();rows=list(csv.DictReader((ROOT/'workflow-assets/fictional-operations-review.csv').open()))
assert [r['test_id'] for r in rows]==['R01','R02','R03'];assert all(r['fictional']=='true' and not r['observed_action'] and not r['unresolved_issue'] for r in rows)
assert 'do not send' in rows[0]['expected_action'] and 'Hold promise' in rows[1]['expected_action'] and 'hold commitment' in rows[2]['expected_action']
class Page(HTMLParser):
 def __init__(self):super().__init__();self.links=[];self.ids=[];self.canonical=[];self.noindex=False
 def handle_starttag(self,t,a):
  a=dict(a)
  if 'id' in a:self.ids.append(a['id'])
  if t=='a':self.links.append(a.get('href',''))
  if t=='link' and a.get('rel')=='canonical':self.canonical.append(a.get('href'))
  if t=='meta' and a.get('name')=='robots' and 'noindex' in a.get('content','').lower():self.noindex=True
p=Page();p.feed(html);assert p.canonical==[d['canonical']] and not p.noindex and len(p.ids)==len(set(p.ids));assert all(x['id'] in p.ids for x in d['sections'])
for phrase in ['not a manuscript excerpt','not retained as verified book content','Observed action and unresolved issue are blank']:assert phrase in html
retired={f'/books/built-to-run/chapters/{n}/' for n in [8,9,10]};cfg=json.loads((ROOT/'vercel.json').read_text());rules={r['source']:r for r in cfg['redirects']};assert len(rules)==len(cfg['redirects'])
for n,anchor in [(8,'automation'),(9,'review'),(10,'absence')]:
 old=f'/books/built-to-run/chapters/{n}/';assert not (ROOT/(old.strip('/')+'/index.html')).exists()
 for form in [old,old[:-1]]:assert rules[form]=={'source':form,'destination':route+'#'+anchor,'permanent':True}
for path in ROOT.rglob('*.html'):
 if '.git' in path.parts:continue
 q=Page();q.feed(path.read_text())
 for link in q.links:
  u=urlsplit(link)
  if u.netloc and u.netloc!='www.drconnorrobertsonbooks.com':continue
  assert u.path not in retired and u.path+'/' not in retired,(path,link)
records=lambda b:{e.find('{*}loc').text:ET.tostring(e) for e in ET.fromstring(b)}
before=records(subprocess.check_output(['git','show','HEAD:sitemap.xml'],cwd=ROOT));after=records((ROOT/'sitemap.xml').read_bytes());assert len(after)==415 and set(before)-set(after)=={base+x for x in retired} and set(after)-set(before)=={d['canonical']}
assert all(before[u]==after[u] for u in before.keys()&after.keys() if u!=base+'/books/built-to-run/')
protected=['books/built-to-run/chapters/'+str(n)+'/index.html' for n in [1,2,6]]+['blog/real-estate-ownership-mistakes/index.html','blog/operating-systems-mistakes/index.html','resources/read-function-composition-before-ai-explanation/index.html','resources/read-book-equation-before-ai-explanation/index.html','resources/read-conditional-probabilities-before-ai-summary/index.html','resources/read-appendix-before-ai-book-summary/index.html']
for path in protected:assert (ROOT/path).read_bytes()==subprocess.check_output(['git','show','HEAD:'+path],cwd=ROOT),path
# Repeated renderer cannot rewrite unrelated files or reorder redirects.
def snapshot():return {str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in ROOT.rglob('*') if p.is_file() and '.git' not in p.parts and '__pycache__' not in p.parts}
old=snapshot();subprocess.run(['python3','scripts/render-operations-review-guide.py'],cwd=ROOT,check=True);assert snapshot()==old
source=(ROOT/'generate_site.py').read_text();previous=subprocess.check_output(['git','show','HEAD:generate_site.py'],cwd=ROOT,text=True)
with tempfile.TemporaryDirectory(prefix='books-operations-generator-') as name:
 outputs=[]
 for i,code in enumerate([previous,source]):
  stage=Path(name)/str(i);stage.mkdir();ns={'__file__':str(ROOT/'generate_site.py'),'__name__':'operations_verification'};exec(compile(code,'actual-book-generator','exec'),ns);ns['OUTPUT_DIR']=str(stage)
  for book in ns['BOOKS']:ns['generate_book_landing'](book)
  outputs.append({book['slug']:(stage/f"books/{book['slug']}/index.html").read_bytes() for book in ns['BOOKS']})
  if i==1:assert route.encode() in outputs[-1]['built-to-run']
 assert all(outputs[0][book]==outputs[1][book] for book in outputs[0] if book!='built-to-run')
print(json.dumps({'canonicalOwners':415,'retiredOwners':3,'directRedirectForms':6,'fictionalPackets':3,'blankObservedFields':6,'protectedAuthoredPages':len(protected),'otherBookGenerators':'three byte-identical','rendererRepeat':'stable','staleInternalLinks':0}))
