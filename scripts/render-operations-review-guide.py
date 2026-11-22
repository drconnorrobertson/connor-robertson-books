"""Render an original operations exercise and consolidate three legacy chapter claims."""
from pathlib import Path
from html import escape
import json,csv,io,re,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
def render():
 d=json.loads((ROOT/'content/operations-review-guide.json').read_text());ns={'__file__':str(ROOT/'generate_site.py'),'__name__':'operations_render'};exec(compile((ROOT/'generate_site.py').read_text(),'site-definitions','exec'),ns)
 route='/books/built-to-run/operations-review/';bc=[('Home','/'),('Built to Run','/books/built-to-run/'),(d['title'],route)]
 body='<main class="page-content" style="max-width:900px;min-width:0"><h1>'+escape(d['title'])+'</h1><p><strong>Original website companion.</strong> This guide is not a manuscript excerpt or verified chapter summary. The former chapter-numbered URLs now lead to the relevant exercise sections below; their chapter titles, quotations and outcome claims are not retained as verified book content.</p><p>Use the fictional packets to test preparation, review and authority boundaries before relying on a handoff.</p><nav aria-label="Guide sections">'+''.join('<p><a href="#'+s['id']+'">'+escape(s['heading'])+'</a></p>' for s in d['sections'])+'</nav>'
 for s in d['sections']:body+='<section id="'+s['id']+'" style="scroll-margin-top:90px"><h2>'+escape(s['heading'])+'</h2>'+''.join('<p>'+escape(t)+'</p>' for t in s['paragraphs'])+'</section>'
 body+='<h2>Three fictional review packets</h2>'
 for c in d['cases']:body+='<section><h3>'+c['id']+': '+escape(c['topic'])+'</h3><dl><dt>Source packet</dt><dd>'+escape(c['source'])+'</dd><dt>Expected action</dt><dd>'+escape(c['expected'])+'</dd><dt>Exception control</dt><dd>'+escape(c['exception'])+'</dd></dl></section>'
 body+='<p><a href="/workflow-assets/fictional-operations-review.csv" download style="display:inline-flex;min-height:44px;align-items:center">Download the fictional review worksheet CSV</a>. Observed action and unresolved issue are blank for your test notes.</p><p>Continue with the <a href="/books/built-to-run/chapters/1/">blocked decision queue</a>, <a href="/books/built-to-run/chapters/2/">workflow documentation companion</a> or <a href="/books/built-to-run/chapters/6/">weekly metrics ledger</a>. Return to the <a href="/books/built-to-run/">Built to Run overview</a> for book purchase options.</p><p>Original website exercise by Robertson Books. Reviewed '+d['reviewed']+'.</p></main>'
 html=ns['head'](d['title']+' | Robertson Books',d['description'],route,[ns['breadcrumb_schema'](bc)])+ns['header']('built-to-run')+ns['breadcrumb_html'](bc)+body+ns['footer']()+ns['page_end']()
 target=ROOT/'books/built-to-run/operations-review/index.html';target.parent.mkdir(parents=True,exist_ok=True);target.write_text(html)
 out=io.StringIO(newline='');w=csv.writer(out,lineterminator='\n');w.writerow(['test_id','topic','source_packet','expected_action','exception_control','observed_action','unresolved_issue','fictional'])
 for c in d['cases']:w.writerow([c[k] for k in ['id','topic','source','expected','exception']]+['','','true'])
 (ROOT/'workflow-assets/fictional-operations-review.csv').write_text(out.getvalue())
 card='<section id="operations-companion"><h2>Original website operations exercise</h2><p><a href="/books/built-to-run/operations-review/">Review automation, exception packets and owner-absence decisions</a> using three fictional handoff tests. This is a website companion, not verified chapter content.</p></section>'
 p=ROOT/'books/built-to-run/index.html';s=p.read_text();s=re.sub(r'<!-- ownership-review:companion-nav:start -->[\s\S]*?<!-- ownership-review:companion-nav:end -->','',s)
 if card not in s:
  marker='<h2 style="margin-top:40px;">More from This Book</h2>';assert marker in s;s=s.replace(marker,card+'\n'+marker,1)
 p.write_text(s)
 cfgpath=ROOT/'vercel.json';cfg=json.loads(cfgpath.read_text());routes={str(n):'/books/built-to-run/chapters/'+str(n)+'/' for n in [8,9,10]};retired=set(routes.values());anchors={'8':'automation','9':'review','10':'absence'}
 cfg['redirects']=[r for r in cfg['redirects'] if r['source'] not in retired and r['source']+'/' not in retired]
 for n,old in routes.items():
  for form in [old,old[:-1]]:cfg['redirects'].append({'source':form,'destination':route+'#'+anchors[n],'permanent':True})
 if not any(r['source']==route[:-1] for r in cfg['redirects']):cfg['redirects'].append({'source':route[:-1],'destination':route,'permanent':True})
 cfgpath.write_text(json.dumps(cfg,indent=2)+'\n')
 p=ROOT/'sitemap.xml';tree=ET.parse(p);space='{http://www.sitemaps.org/schemas/sitemap/0.9}';ET.register_namespace('',space[1:-1]);base='https://www.drconnorrobertsonbooks.com'
 for e in list(tree.getroot()):
  url=e.find(space+'loc').text
  if url in {base+x for x in retired}:tree.getroot().remove(e)
  elif url==base+'/books/built-to-run/':
   mod=e.find(space+'lastmod')
   if mod is None:mod=ET.SubElement(e,space+'lastmod')
   mod.text=d['reviewed']
 if not any(e.find(space+'loc').text==d['canonical'] for e in tree.getroot()):
  e=ET.SubElement(tree.getroot(),space+'url');ET.SubElement(e,space+'loc').text=d['canonical'];ET.SubElement(e,space+'lastmod').text=d['reviewed']
 tree.write(p,encoding='utf-8',xml_declaration=True)
 for old in retired:
  p=ROOT/(old.strip('/')+'/index.html')
  if p.exists():p.unlink()
 print('Consolidated three legacy chapter routes into one original operations review guide.')
if __name__=='__main__':render()
