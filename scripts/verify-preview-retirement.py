"""Check retired claims, authored-body preservation and actual generation boundaries."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit
import json,re,hashlib,subprocess,tempfile,shutil,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1];origin='https://www.drconnorrobertsonbooks.com';d=json.loads((ROOT/'content/website-reading-navigation.json').read_text());retired={r['path']:r['book'] for r in d['retired']};assert len(retired)==25
class Scan(HTMLParser):
 def __init__(self):super().__init__();self.links=[];self.ids=[];self.canonicals=[];self.noindex=False
 def handle_starttag(self,t,a):
  a=dict(a)
  if t=='a':self.links.append(a.get('href',''))
  if 'id' in a:self.ids.append(a['id'])
  if t=='link' and a.get('rel')=='canonical':self.canonicals.append(a.get('href'))
  if t=='meta' and a.get('name')=='robots' and 'noindex' in a.get('content','').lower():self.noindex=True
rules=json.loads((ROOT/'vercel.json').read_text())['redirects'];bySource={r['source']:r for r in rules};assert len(bySource)==len(rules)==582
for path,book in retired.items():
 assert not (ROOT/path.lstrip('/')/'index.html').exists()
 for form in [path,path[:-1]]:assert bySource[form]=={'source':form,'destination':f'/books/{book}/#website-companions','permanent':True}
for path in ROOT.rglob('*.html'):
 if '.git' in path.parts:continue
 s=Scan();s.feed(path.read_text())
 for href in s.links:
  u=urlsplit(href)
  if not u.netloc or u.netloc=='www.drconnorrobertsonbooks.com':assert u.path not in retired and u.path+'/' not in retired,(path,href)
for book,links in d['readingLinks'].items():
 html=(ROOT/f'books/{book}/index.html').read_text();s=Scan();s.feed(html);assert s.ids.count('website-companions')==1 and s.canonicals==[origin+f'/books/{book}/'] and not s.noindex
 assert 'not verified chapter summaries' in html and 'Chapter by Chapter' not in html and 'Start with a chapter' not in html
 for label,href in links:assert href in s.links
 for purchase in re.findall(r'<a href="(https:[^"]+)" class="buy-btn',html):assert purchase in subprocess.check_output(['git','show','HEAD:'+f'books/{book}/index.html'],cwd=ROOT,text=True)
for n in [1,2,6]:
 route=f'books/built-to-run/chapters/{n}/index.html';before=subprocess.check_output(['git','show','HEAD:'+route],cwd=ROOT,text=True);after=(ROOT/route).read_text();fragment=(ROOT/f'chapter-guides/built-to-run-{n}.html').read_text().strip();assert fragment in before and fragment in after
 assert '<blockquote' not in after and 'Original website reading companions' in after
 if n==2:
  assert '<title>'+d['documentationCompanion']['title']+' | Robertson Books</title>' in after and '<h1>'+d['documentationCompanion']['title']+'</h1>' in after
protected=['books/built-to-run/operations-review/index.html','books/creative-acquisitions/decision-review/index.html','books/buying-wealth/transition-review/index.html','books/the-7-minute-phone-call/follow-up-review/index.html','blog/real-estate-ownership-mistakes/index.html','blog/operating-systems-mistakes/index.html','resources/read-function-composition-before-ai-explanation/index.html','resources/read-book-equation-before-ai-explanation/index.html','resources/read-conditional-probabilities-before-ai-summary/index.html','resources/read-appendix-before-ai-book-summary/index.html','resources/decision-evidence-review/index.html']
for path in protected:assert (ROOT/path).read_bytes()==subprocess.check_output(['git','show','HEAD:'+path],cwd=ROOT),path
records=lambda body:{e.find('{*}loc').text:ET.tostring(e) for e in ET.fromstring(body)}
before=records(subprocess.check_output(['git','show','HEAD:sitemap.xml'],cwd=ROOT));after=records((ROOT/'sitemap.xml').read_bytes());assert len(after)==305 and set(before)-set(after)=={origin+p for p in retired} and not set(after)-set(before)
changedNav={origin+f'/books/{b}/{tail}' for b in d['readingLinks'] for tail in ['','key-lessons/','who-should-read/']}|{origin+p for p in d['authoredChapterRoutes']};assert all(before[u]==after[u] for u in before.keys()&after.keys() if u not in changedNav)
def snapshot():return {str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in ROOT.rglob('*') if p.is_file() and '.git' not in p.parts and '__pycache__' not in p.parts}
first=snapshot();subprocess.run(['python3','scripts/retire-unverified-chapter-previews.py'],cwd=ROOT,check=True);assert snapshot()==first
source=(ROOT/'generate_site.py').read_text();assert 'readers consistently cite' not in source and 'tested approaches grounded in actual outcomes' not in source
with tempfile.TemporaryDirectory(prefix='books-preview-boundary-') as name:
 stage=Path(name);shutil.copytree(ROOT/'content',stage/'content');shutil.copytree(ROOT/'chapter-guides',stage/'chapter-guides');ns={'__file__':str(ROOT/'generate_site.py'),'__name__':'preview_boundary_verification'};exec(compile(source,'actual-generator','exec'),ns);ns['OUTPUT_DIR']=str(stage);outputs=[]
 for book in ns['BOOKS']:
  ns['generate_book_landing'](book);landing=(stage/f"books/{book['slug']}/index.html").read_text();assert 'id="website-companions"' in landing and all(p not in landing for p in retired)
  for chapter in book['chapters']:
   result=ns['generate_chapter_page'](book,chapter)
   if book['slug']=='built-to-run' and chapter['num'] in [1,2,6]:assert result is not None;outputs.append(result)
   else:assert result is None and not (stage/f"books/{book['slug']}/chapters/{chapter['num']}/index.html").exists()
 assert len(outputs)==3
crosslinks=json.loads((ROOT/'scripts/contextual-crosslinks.json').read_text());assert len(crosslinks)==1 and crosslinks[0]['file']=='books/built-to-run/chapters/2/index.html'
print(json.dumps({'canonicalOwners':305,'retiredUnverifiedPreviews':25,'directRetiredURLForms':50,'redirectRules':582,'bookOverviewReadingSections':4,'authoredChapterFragments':'3byte-preserved','otherAuthoredGuides':'11wholepagesbyte-preserved','actualGenerator':'25previewsrefused;3authoredpagesrendered;4companionoverviews','repeat':'stable','stalePreviewLinks':0,'purchaseLinks':'preserved','passed':True}))
