"""Check the real founder companion renderer, records and chapter generator."""
from pathlib import Path
import json,csv,subprocess,tempfile,shutil,re,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
d=json.loads((ROOT/'content/founder-decision-guide.json').read_text());fragment=(ROOT/'chapter-guides/built-to-run-1.html').read_text().strip();target=ROOT/'books/built-to-run/chapters/1/index.html';html=target.read_text()
rows=list(csv.DictReader((ROOT/'workflow-assets/fictional-founder-decision-queue.csv').open()))
assert [r['message_id']for r in rows]==['Q01','Q02','Q03','Q04','Q05','Q06'];assert len({r['distinct_decision_id']for r in rows})==5;assert sum(r['owner_reserved']=='true'for r in rows)==1;assert all(r['fictional']=='true'for r in rows)
assert rows[5]['distinct_decision_id']=='Q02'
assert fragment in html;assert html.count('<h1>')==1;assert 'rel="canonical" href="'+d['canonical']+'"'in html
for phrase in ['tested approaches grounded in actual outcomes','readers consistently cite','foundation laid in earlier chapters']:assert phrase not in html
assert d['sourceBoundary']in html;assert '71.43'not in html
for path in ['resources/read-function-composition-before-ai-explanation/index.html','resources/read-book-equation-before-ai-explanation/index.html','resources/read-conditional-probabilities-before-ai-summary/index.html','resources/read-appendix-before-ai-book-summary/index.html','books/built-to-run/chapters/2/index.html','blog/real-estate-ownership-mistakes/index.html','blog/operating-systems-mistakes/index.html']:
 assert (ROOT/path).read_bytes()==subprocess.check_output(['git','show','HEAD:'+path],cwd=ROOT),path
# Repeating the actual renderer cannot touch any other source or public file.
def snapshot():return {str(p.relative_to(ROOT)):p.read_bytes()for p in ROOT.rglob('*')if p.is_file()and'.git'not in p.parts and'__pycache__'not in p.parts}
before=snapshot();subprocess.run(['python3','scripts/render-founder-guide.py'],cwd=ROOT,check=True);assert snapshot()==before
records=lambda text:{e.find('{*}loc').text:ET.tostring(e)for e in ET.fromstring(text)}
old=records(subprocess.check_output(['git','show','HEAD:sitemap.xml'],cwd=ROOT));new=records((ROOT/'sitemap.xml').read_bytes());assert old.keys()==new.keys()
# This companion verifier owns its entry; later reviewed companions may revise theirs.
entry=ET.fromstring(new[d['canonical']]);assert entry.find('{*}lastmod').text==d['reviewed']
# Execute actual generator definitions without invoking its legacy main rebuild.
source=(ROOT/'generate_site.py').read_text();baseline=subprocess.check_output(['git','show','HEAD:generate_site.py'],cwd=ROOT,text=True)
with tempfile.TemporaryDirectory(prefix='books-founder-generator-')as name:
 out=Path(name);outputs=[]
 for i,code in enumerate([baseline,source]):
  stage=out/str(i);(stage/'chapter-guides').mkdir(parents=True);(stage/'content').mkdir()
  for path in ['chapter-guides/built-to-run-1.html','chapter-guides/built-to-run-2.html','content/founder-decision-guide.json']:shutil.copyfile(ROOT/path,stage/path)
  ns={'__file__':str(ROOT/'generate_site.py'),'__name__':'chapter_verification'};exec(compile(code,'actual-chapter-generator','exec'),ns);ns['OUTPUT_DIR']=str(stage)
  book=next(b for b in ns['BOOKS']if b['slug']=='built-to-run');ns['generate_chapter_page'](book,book['chapters'][1]);outputs.append((stage/'books/built-to-run/chapters/2/index.html').read_bytes())
  if i==1:
   ns['generate_chapter_page'](book,book['chapters'][0]);generated=(stage/'books/built-to-run/chapters/1/index.html').read_text();assert fragment in generated;assert '<h1>'+d['title']+'</h1>'in generated;assert 'tested approaches grounded in actual outcomes'not in generated
 assert outputs[0]==outputs[1]
print(json.dumps({'messages':6,'distinctDecisions':5,'ownerReserved':1,'protectedAuthoredPages':7,'actualGeneratorTarget':'passed','otherGeneratorChapter':'byte-identical','rendererRepeat':'stable','sitemapOwners':len(new),'ownSitemapEntry':'reviewed date matches'}))
