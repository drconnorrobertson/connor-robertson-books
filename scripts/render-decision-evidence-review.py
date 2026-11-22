"""Replace eighty near-identical frameworks with one original worked review guide."""
from pathlib import Path
from html import escape
from urllib.parse import urlsplit
import csv,io,json,re,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
def render():
 d=json.loads((ROOT/'content/decision-evidence-review.json').read_text());route='/resources/decision-evidence-review/';origin='https://www.drconnorrobertsonbooks.com';ns={'__file__':str(ROOT/'generate_site.py'),'__name__':'decision_evidence_render'};exec(compile((ROOT/'generate_site.py').read_text(),'site-definitions','exec'),ns)
 bc=[('Home','/'),('Resources','/resources/'),(d['title'],route)]
 body='<main class="page-content" style="max-width:900px;min-width:0"><h1>'+escape(d['title'])+'</h1>'+''.join('<p>'+escape(p)+'</p>' for p in d['introduction'])+'<nav aria-label="Worked decision examples">'+''.join('<p><a href="#'+c['id']+'">'+escape(c['topic'])+': '+c['packet']+'</a></p>' for c in d['cases'])+'</nav>'
 for c in d['cases']:body+='<section id="'+c['id']+'" style="scroll-margin-top:90px"><h2>'+escape(c['heading'])+'</h2>'+''.join('<p>'+escape(p)+'</p>' for p in c['paragraphs'])+'<p><strong>Next review question:</strong> '+escape(c['question'])+'</p></section>'
 body+='<section><h2>Record your own reading finding</h2>'+''.join('<p>'+escape(p)+'</p>' for p in d['closing'])+'<p><a class="decision-download" href="/workflow-assets/fictional-decision-review-packets.csv" download style="display:inline-flex;min-height:44px;align-items:center">Download the eight fictional review packets CSV</a>.</p><p><a class="decision-download" href="/workflow-assets/fictional-diligence-file-inventory.csv" download style="display:inline-flex;min-height:44px;align-items:center">Download the twelve-file metadata inventory CSV</a>.</p><p>All observed_review and content_review fields are intentionally empty. Add only non-sensitive exercise notes; these downloads are not a client document portal.</p></section><section><h2>Primary sources and scope</h2><ul>'+''.join('<li><a href="'+escape(s['url'],quote=True)+'">'+escape(s['title'])+'</a>: '+escape(s['scope'])+'</li>' for s in d['sources'])+'</ul><p>Sources checked '+d['reviewed']+'. The eight packets and all figures are original fictional teaching examples, not examples quoted from those sources.</p></section><section><h2>Continue with a narrower worked example</h2><ul><li><a href="/blog/real-estate-ownership-mistakes/">Trace business and property cash</a></li><li><a href="/blog/operating-systems-mistakes/">Test an operating handoff</a></li><li><a href="/books/buying-wealth/transition-review/">Review sale cash, exchange timing and authority records</a></li></ul></section><p>Original website exercise by Robertson Books. Reviewed '+d['reviewed']+'. Verify book contents against the published book itself.</p></main>'
 target=ROOT/'resources/decision-evidence-review/index.html';target.parent.mkdir(parents=True,exist_ok=True);target.write_text(ns['head'](d['title']+' | Robertson Books',d['description'],route,[ns['breadcrumb_schema'](bc)])+ns['header']('blog')+ns['breadcrumb_html'](bc)+body+ns['footer']()+ns['page_end']())
 out=io.StringIO(newline='');w=csv.writer(out,lineterminator='\n');w.writerow(['packet_id','topic','supplied_record','supported_interpretation','next_review_question','observed_review','fictional'])
 for c in d['cases']:w.writerow([c['packet'],c['topic'],c['source'],c['interpretation'],c['question'],'','true'])
 (ROOT/'workflow-assets/fictional-decision-review-packets.csv').write_text(out.getvalue())
 out=io.StringIO(newline='');w=csv.writer(out,lineterminator='\n');w.writerow(['file_id','readable','matching_entity','content_review','fictional'])
 for f in d['files']:w.writerow([f['id'],str(f['readable']).lower(),str(f['matchingEntity']).lower(),'','true'])
 (ROOT/'workflow-assets/fictional-diligence-file-inventory.csv').write_text(out.getvalue())
 retired={old:topic for topic,paths in d['retired'].items() for old in paths};assert len(retired)==80
 archive=ROOT/'blog/index.html';text=archive.read_text()
 def remove_old_link(m):
  href=re.search(r'href="([^"]+)"',m[0])
  return '' if href and urlsplit(href[1]).path in retired else m[0]
 text=re.sub(r'<a\b[^>]*>[\s\S]*?</a>',remove_old_link,text);card=ns['decision_evidence_navigation']();pattern=r'<!-- decision-evidence-nav:start -->[\s\S]*?<!-- decision-evidence-nav:end -->';text=re.sub(pattern,'',text);marker='<footer class="site-footer">';assert marker in text;text=text.replace(marker,card+marker,1);archive.write_text(text)
 resource=ROOT/'resources/index.html';text=re.sub(pattern,'',resource.read_text());assert '</main>' in text;resource.write_text(text.replace('</main>',card+'</main>',1))
 cfgpath=ROOT/'vercel.json';cfg=json.loads(cfgpath.read_text());forms=set(retired)|{x[:-1] for x in retired}|{route[:-1]};cfg['redirects']=[rule for rule in cfg['redirects'] if rule['source'] not in forms]
 for old,topic in retired.items():
  for source in [old,old[:-1]]:cfg['redirects'].append({'source':source,'destination':route+'#'+topic,'permanent':True})
 cfg['redirects'].append({'source':route[:-1],'destination':route,'permanent':True});cfgpath.write_text(json.dumps(cfg,indent=2)+'\n')
 p=ROOT/'sitemap.xml';tree=ET.parse(p);space='{http://www.sitemaps.org/schemas/sitemap/0.9}';ET.register_namespace('',space[1:-1])
 for entry in list(tree.getroot()):
  url=entry.find(space+'loc').text
  if url in {origin+x for x in retired}:tree.getroot().remove(entry)
  elif url in {origin+'/blog/',origin+'/resources/'}:
   date=entry.find(space+'lastmod')
   if date is None:date=ET.SubElement(entry,space+'lastmod')
   date.text=d['reviewed']
 if not any(entry.find(space+'loc').text==d['canonical'] for entry in tree.getroot()):
  entry=ET.SubElement(tree.getroot(),space+'url');ET.SubElement(entry,space+'loc').text=d['canonical'];ET.SubElement(entry,space+'lastmod').text=d['reviewed']
 tree.write(p,encoding='utf-8',xml_declaration=True)
 for old in retired:
  p=ROOT/old.lstrip('/')/'index.html'
  if p.exists():p.unlink()
 print('Rendered eight original decision packets; consolidated eighty repeated framework pages.')
if __name__=='__main__':render()
