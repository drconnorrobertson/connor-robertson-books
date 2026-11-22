"""Consolidate two unsupported chapter pages into an original sourced transition exercise."""
from pathlib import Path
from html import escape
import csv,io,json,re,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
def render():
 d=json.loads((ROOT/'content/transition-review-guide.json').read_text());ns={'__file__':str(ROOT/'generate_site.py'),'__name__':'transition_review_render'};exec(compile((ROOT/'generate_site.py').read_text(),'site-definitions','exec'),ns)
 route='/books/buying-wealth/transition-review/';overview='/books/buying-wealth/';bc=[('Home','/'),('Buying Wealth',overview),(d['title'],route)]
 body='<main class="page-content" style="max-width:900px;min-width:0"><h1>'+escape(d['title'])+'</h1><p><strong>Original website companion.</strong> This is not a manuscript excerpt or verified chapter summary. Its three independent packets are fictional teaching examples, not completed transactions or client outcomes.</p><nav aria-label="Guide sections">'+''.join('<p><a href="#'+s['id']+'">'+escape(s['heading'])+'</a></p>' for s in d['sections'])+'</nav>'
 for s in d['sections']:body+='<section id="'+s['id']+'" style="scroll-margin-top:90px"><h2>'+escape(s['heading'])+'</h2>'+''.join('<p>'+escape(x)+'</p>' for x in s['paragraphs'])+'</section>'
 body+='<h2>Three fictional transition record packets</h2>'
 for c in d['cases']:body+='<section><h3>'+c['id']+': '+escape(c['topic'])+'</h3><dl><dt>Supplied record</dt><dd>'+escape(c['source'])+'</dd><dt>Supported interpretation</dt><dd>'+escape(c['interpretation'])+'</dd><dt>Review question</dt><dd>'+escape(c['question'])+'</dd></dl></section>'
 body+='<section aria-label="Primary sources"><h2>Primary sources and scope</h2><ul>'+''.join('<li><a href="'+escape(source['url'],quote=True)+'">'+escape(source['title'])+'</a>: '+escape(source['supports'])+'</li>' for source in d['sources'])+'</ul><p>Sources checked '+d['reviewed']+'. The worked packets and figures are original fictional examples; they are not examples quoted from these sources.</p></section>'
 body+='<p><a class="transition-download" href="/workflow-assets/fictional-transition-review.csv" download style="display:inline-flex;min-height:44px;align-items:center">Download the fictional review packets CSV</a>.</p><p>Return to <a href="'+overview+'">Buying Wealth overview</a> for book purchase options and other website reading companions. Use the book itself to verify its contents and chapter sequence.</p><p>Original website exercise by Robertson Books. Reviewed '+d['reviewed']+'.</p></main>'
 target=ROOT/(route.strip('/')+'/index.html');target.parent.mkdir(parents=True,exist_ok=True);target.write_text(ns['head'](d['title']+' | Robertson Books',d['description'],route,[ns['breadcrumb_schema'](bc)])+ns['header']('buying-wealth')+ns['breadcrumb_html'](bc)+body+ns['footer']()+ns['page_end']())
 out=io.StringIO(newline='');w=csv.writer(out,lineterminator='\n');w.writerow(['packet_id','topic','supplied_record','supported_interpretation','review_question','observed_review','fictional'])
 for c in d['cases']:w.writerow([c[k] for k in ['id','topic','source','interpretation','question']]+['','true'])
 (ROOT/'workflow-assets/fictional-transition-review.csv').write_text(out.getvalue())
 card='<section id="transition-companion"><h2>Original website transition exercise</h2><p><a href="'+route+'">Review sale cash, exchange timing and authority records</a> using three independent fictional packets. This is a website companion, not verified chapter content.</p></section>'
 p=ROOT/(overview.strip('/')+'/index.html');s=p.read_text();s=re.sub(r'<!-- ownership-review:companion-nav:start -->[\s\S]*?<!-- ownership-review:companion-nav:end -->','',s)
 if card not in s and 'id="website-companions"' not in s:
  marker='<h2 style="margin-top:40px;">More from This Book</h2>';assert marker in s;s=s.replace(marker,card+'\n'+marker,1)
 p.write_text(s)
 # Route resource references directly to the current owner, preserving their label.
 for resource in [ROOT/'resources/index.html']:
  text=resource.read_text()
  for number,anchor in [(9,'sale'),(10,'authority')]:
   text=text.replace('href="'+overview+'chapters/'+str(number)+'/"','href="'+route+'#'+anchor+'"')
  resource.write_text(text)
 cfgpath=ROOT/'vercel.json';cfg=json.loads(cfgpath.read_text());retired={f'{overview}chapters/{n}/' for n in [9,10]};anchors={9:'sale',10:'authority'}
 cfg['redirects']=[r for r in cfg['redirects'] if r['source'] not in retired and r['source']+'/' not in retired and r['source']!=route[:-1]]
 for number,anchor in anchors.items():
  old=overview+'chapters/'+str(number)+'/'
  for form in [old,old[:-1]]:cfg['redirects'].append({'source':form,'destination':route+'#'+anchor,'permanent':True})
 if not any(r['source']==route[:-1] for r in cfg['redirects']):cfg['redirects'].append({'source':route[:-1],'destination':route,'permanent':True})
 cfgpath.write_text(json.dumps(cfg,indent=2)+'\n')
 p=ROOT/'sitemap.xml';tree=ET.parse(p);space='{http://www.sitemaps.org/schemas/sitemap/0.9}';ET.register_namespace('',space[1:-1]);base='https://www.drconnorrobertsonbooks.com'
 for e in list(tree.getroot()):
  url=e.find(space+'loc').text
  if url in {base+x for x in retired}:tree.getroot().remove(e)
  elif url==base+overview:
   mod=e.find(space+'lastmod')
   if mod is None:mod=ET.SubElement(e,space+'lastmod')
   mod.text=d['reviewed']
 if not any(e.find(space+'loc').text==d['canonical'] for e in tree.getroot()):
  e=ET.SubElement(tree.getroot(),space+'url');ET.SubElement(e,space+'loc').text=d['canonical'];ET.SubElement(e,space+'lastmod').text=d['reviewed']
 tree.write(p,encoding='utf-8',xml_declaration=True)
 for old in retired:
  p=ROOT/(old.strip('/')+'/index.html')
  if p.exists():p.unlink()
 print('Rendered one original transition companion; consolidated two legacy chapter pages.')
if __name__=='__main__':render()
