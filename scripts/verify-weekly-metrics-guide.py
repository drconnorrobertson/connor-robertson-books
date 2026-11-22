"""Check ledger arithmetic, authored content, sitemap scope and real generator behavior."""
from pathlib import Path
from fractions import Fraction
import csv,json,re,subprocess,tempfile,shutil,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
d=json.loads((ROOT/'content/weekly-metrics-guide.json').read_text());rows=list(csv.DictReader((ROOT/'workflow-assets/fictional-weekly-work-ledger.csv').open()))
assert len(rows)==8 and len({r['id'] for r in rows})==8
start,end='2026-11-16','2026-11-20'
arrivals=[r for r in rows if start<=r['received']<=end];active=[r for r in arrivals if not r['cancelled']]
accepted=[r for r in active if r['accepted'] and r['accepted']<=end]
due=[r for r in active if r['due']<=end];on_time=[r for r in due if r['accepted'] and r['accepted']<=r['due']]
period=[r for r in rows if r['accepted'] and start<=r['accepted']<=end]
opening=[r for r in rows if r['received']<start and (not r['accepted'] or r['accepted']>=start)]
cancelled=[r for r in rows if r['cancelled'] and start<=r['cancelled']<=end]
ending=[r for r in rows if not r['accepted'] and not r['cancelled']]
assert sum(int(r['sourceRecords']) for r in arrivals)==8 and len(arrivals)==6
assert Fraction(len(accepted),len(active))==Fraction(3,5)
assert Fraction(len(on_time),len(due))==Fraction(1,2)
assert Fraction(len(on_time),len(accepted))==Fraction(2,3)
assert len(period)==5 and len(opening)+len(arrivals)-len(period)-len(cancelled)==len(ending)==2
assert [r['id'] for r in ending if r['due']<=end]==['D']
assert sum(int(r['revisions']) for r in period)==1
assert all(r['fictional']=='true' and not(r['cancelled'] and r['accepted']) for r in rows)
fragment=(ROOT/'chapter-guides/built-to-run-6.html').read_text().strip();html=(ROOT/'books/built-to-run/chapters/6/index.html').read_text()
assert fragment in html and '<h1>'+d['title']+'</h1>' in html and 'rel="canonical" href="'+d['canonical']+'"' in html
for phrase in ['tested approaches grounded in actual outcomes','readers consistently cite','foundation laid in earlier chapters']:assert phrase not in html
for match in re.findall(r'<script type="application/ld\+json">([\s\S]*?)</script>',html):json.loads(match)
records=lambda b:{e.find('{*}loc').text:ET.tostring(e) for e in ET.fromstring(b)}
before=records(subprocess.check_output(['git','show','HEAD:sitemap.xml'],cwd=ROOT));after=records((ROOT/'sitemap.xml').read_bytes());assert before.keys()==after.keys() and len(after)==417
assert all(before[u]==after[u] for u in before if u!=d['canonical'])
def snapshot():return {str(p.relative_to(ROOT)):p.read_bytes() for p in ROOT.rglob('*') if p.is_file() and '.git' not in p.parts and '__pycache__' not in p.parts}
old=snapshot();subprocess.run(['python3','scripts/render-weekly-metrics-guide.py'],cwd=ROOT,check=True);assert snapshot()==old
source=(ROOT/'generate_site.py').read_text();baseline=subprocess.check_output(['git','show','HEAD:generate_site.py'],cwd=ROOT,text=True)
with tempfile.TemporaryDirectory(prefix='books-metrics-generator-') as name:
 outputs=[]
 for i,code in enumerate([baseline,source]):
  stage=Path(name)/str(i)
  for folder in ['chapter-guides','content']:shutil.copytree(ROOT/folder,stage/folder)
  ns={'__file__':str(ROOT/'generate_site.py'),'__name__':'metrics_verification'};exec(compile(code,'actual-chapter-generator','exec'),ns);ns['OUTPUT_DIR']=str(stage)
  book=next(b for b in ns['BOOKS'] if b['slug']=='built-to-run')
  preserved=[]
  for number in [1,2,3,4,5,7]:
   ns['generate_chapter_page'](book,next(c for c in book['chapters'] if c['num']==number));preserved.append((stage/f'books/built-to-run/chapters/{number}/index.html').read_bytes())
  outputs.append(preserved)
  if i==1:
   ns['generate_chapter_page'](book,next(c for c in book['chapters'] if c['num']==6));target=(stage/'books/built-to-run/chapters/6/index.html').read_text();assert fragment in target and '<h1>'+d['title']+'</h1>' in target
 assert outputs[0]==outputs[1]
print(json.dumps({'incomingRecords':8,'distinctArrivals':6,'activeCohort':5,'cohortCompletion':'3/5','dueCohortOnTime':'2/4','completedSubsetOnTime':'2/3','periodAccepted':5,'endingBacklog':2,'overdue':['D'],'otherGeneratorChapters':'six byte-identical','rendererRepeat':'stable','sitemapOwners':417}))
