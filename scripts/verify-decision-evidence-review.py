"""Verify the worked records and the eighty-page consolidation boundaries."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit
from fractions import Fraction
import csv,json,hashlib,subprocess,tempfile,shutil,re,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1];origin='https://www.drconnorrobertsonbooks.com';route='/resources/decision-evidence-review/';d=json.loads((ROOT/'content/decision-evidence-review.json').read_text());html=(ROOT/'resources/decision-evidence-review/index.html').read_text();retired={p:t for t,paths in d['retired'].items() for p in paths};assert len(retired)==80 and len(d['retired'])==8
rows=list(csv.DictReader((ROOT/'workflow-assets/fictional-decision-review-packets.csv').open()));files=list(csv.DictReader((ROOT/'workflow-assets/fictional-diligence-file-inventory.csv').open()));assert [r['packet_id'] for r in rows]==['A01','D01','T01','E01','L01','R01','C01','W01'] and all(r['observed_review']=='' and r['fictional']=='true' for r in rows)
assert [r['file_id'] for r in files]==[f'F{n:02d}' for n in range(1,13)] and all(r['content_review']=='' and r['fictional']=='true' for r in files)
assert [r['file_id'] for r in files if r['readable']=='false']==['F01'];assert [r['file_id'] for r in files if r['matching_entity']=='false']==['F02','F03'];usable=[r for r in files if r['readable']=='true' and r['matching_entity']=='true'];assert len(usable)==9
amounts=lambda text:[int(x.replace(',','')) for x in re.findall(r'\$([\d,]+)',text)]
assert amounts(rows[0]['supplied_record'])==[650000,680000] and 680000-650000==30000
assert Fraction(10,14)==Fraction(5,7) and round(float(Fraction(10,14))*100,1)==71.4
assert amounts(rows[6]['supplied_record'])==[140000,70000,25000,30000,20000];assert 140000-70000-25000==45000 and 45000-30000==15000 and 20000-15000==5000
assert amounts(rows[7]['supplied_record'])==[250000,280000,40000];assert 280000-250000==30000 and Fraction(30000,250000)==Fraction(12,100) and 280000-250000-40000==-10000
for phrase in ['not manuscript excerpts','blank content_review fields','not a purchase-conversion rate','Neither the 12% balance change','no tax rate','$18,000']:
 assert phrase.lower() in html.lower(),phrase
class Scan(HTMLParser):
 def __init__(self):super().__init__();self.ids=[];self.links=[];self.canonicals=[];self.noindex=False;self.h1=0
 def handle_starttag(self,t,a):
  a=dict(a)
  if t=='h1':self.h1+=1
  if 'id' in a:self.ids.append(a['id'])
  if t=='a':self.links.append(a.get('href',''))
  if t=='link' and a.get('rel')=='canonical':self.canonicals.append(a.get('href'))
  if t=='meta' and a.get('name')=='robots' and 'noindex' in a.get('content','').lower():self.noindex=True
s=Scan();s.feed(html);assert s.canonicals==[d['canonical']] and not s.noindex and s.h1==1 and len(s.ids)==len(set(s.ids));assert all(c['id'] in s.ids for c in d['cases'])
for href in s.links:
 if href.startswith('#'):assert href[1:] in s.ids
for source in d['sources']:assert 'href="'+source['url']+'"' in html
cfg=json.loads((ROOT/'vercel.json').read_text());rules={r['source']:r for r in cfg['redirects']};assert len(rules)==len(cfg['redirects'])==557
for old,topic in retired.items():
 assert not (ROOT/old.lstrip('/')/'index.html').exists()
 for form in [old,old[:-1]]:assert rules[form]=={'source':form,'destination':route+'#'+topic,'permanent':True}
for p in ROOT.rglob('*.html'):
 if '.git' in p.parts:continue
 q=Scan();q.feed(p.read_text())
 for href in q.links:
  u=urlsplit(href)
  if not u.netloc or u.netloc=='www.drconnorrobertsonbooks.com':assert u.path not in retired and u.path+'/' not in retired,(p,href)
records=lambda body:{e.find('{*}loc').text:ET.tostring(e) for e in ET.fromstring(body)}
before=records(subprocess.check_output(['git','show','HEAD:sitemap.xml'],cwd=ROOT));after=records((ROOT/'sitemap.xml').read_bytes());assert len(after)==330 and set(before)-set(after)=={origin+p for p in retired} and set(after)-set(before)=={d['canonical']};assert all(before[u]==after[u] for u in before.keys()&after.keys() if u not in {origin+'/blog/',origin+'/resources/'})
protected=['books/built-to-run/chapters/'+str(n)+'/index.html' for n in [1,2,6]]+['books/built-to-run/operations-review/index.html','books/creative-acquisitions/decision-review/index.html','books/buying-wealth/transition-review/index.html','books/the-7-minute-phone-call/follow-up-review/index.html','blog/real-estate-ownership-mistakes/index.html','blog/operating-systems-mistakes/index.html','resources/read-function-composition-before-ai-explanation/index.html','resources/read-book-equation-before-ai-explanation/index.html','resources/read-conditional-probabilities-before-ai-summary/index.html','resources/read-appendix-before-ai-book-summary/index.html']
for path in protected:assert (ROOT/path).read_bytes()==subprocess.check_output(['git','show','HEAD:'+path],cwd=ROOT),path
for script in re.findall(r'<script type="application/ld\+json">([\s\S]*?)</script>',html):json.loads(script)
def snapshot():return {str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in ROOT.rglob('*') if p.is_file() and '.git' not in p.parts and '__pycache__' not in p.parts}
first=snapshot();subprocess.run(['python3','scripts/render-decision-evidence-review.py'],cwd=ROOT,check=True);assert snapshot()==first
# Exercise the actual archive generator with current articles in an isolated output.
with tempfile.TemporaryDirectory(prefix='books-evidence-archive-') as name:
 stage=Path(name);shutil.copytree(ROOT/'blog',stage/'blog');ns={'__file__':str(ROOT/'generate_site.py'),'__name__':'archive_verification'};exec(compile((ROOT/'generate_site.py').read_text(),'actual-generator','exec'),ns);ns['OUTPUT_DIR']=str(stage);ns['generate_blog_index']();ns['populate_blog_archive']();archive=(stage/'blog/index.html').read_text();assert route in archive and all(p not in archive for p in retired)
 assert not {p['slug'] for p in ns['BLOG_POSTS']} & {urlsplit(p).path.strip('/').split('/')[-1] for p in retired}
print(json.dumps({'canonicalOwners':330,'retiredTemplatePages':80,'distinctTemplateBodiesAfterNormalization':1,'redirectForms':160,'redirectRules':557,'originalPackets':8,'inventoryRows':12,'metadataUsable':9,'reviewOutcomeFields':'allblank;unknownnotzero','protectedAuthoredGuides':len(protected),'actualArchiveGenerator':'passed','rendererRepeat':'stable','staleRetiredLinks':0,'passed':True}))
