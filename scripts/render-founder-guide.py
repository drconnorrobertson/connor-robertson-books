"""Render original website companion without inventing manuscript contents."""
from pathlib import Path
from html import escape
import json,re,csv,io,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
def render():
 d=json.loads((ROOT/'content/founder-decision-guide.json').read_text())
 assert len(d['packets'])==6 and len({x['distinctDecision'] for x in d['packets']})==5
 assert sum(x['ownerReserved'] for x in d['packets'])==1
 style='<style id="founder-queue-style">.page-content{min-width:0}.founder-queue-scroll{max-width:100%;overflow-x:auto;border:1px solid #cbd5df}.founder-queue-scroll:focus{outline:3px solid #9a742c;outline-offset:3px}.founder-queue{border-collapse:collapse;width:100%;min-width:520px}.founder-queue th,.founder-queue td{padding:12px;text-align:left;border-bottom:1px solid #cbd5df}.founder-queue th{background:#eef2f7}.founder-queue caption{text-align:left;padding:12px;font-weight:bold}.founder-queue th[scope="row"]{position:sticky;left:0}.founder-queue-download{display:inline-flex;min-height:44px;align-items:center}@media print{.founder-queue{min-width:0;font-size:10px}.founder-queue-scroll{overflow:visible}}</style>'
 body=style+'<p><strong>Original website reading companion.</strong> '+escape(d['sourceBoundary'])+'</p>'
 for i,section in enumerate(d['sections']):
  body+='<section><h2>'+escape(section['heading'])+'</h2>'+''.join('<p>'+escape(x)+'</p>' for x in section['paragraphs'])
  if i==1:
   body+='<div class="founder-queue-scroll" role="region" tabindex="0" aria-label="Fictional decision queue"><table class="founder-queue"><caption>Six fictional messages; five distinct decisions</caption><thead><tr><th scope="col">Message</th><th scope="col">Decision ID</th><th scope="col">Next action</th></tr></thead><tbody>'+''.join('<tr><th scope="row">'+x['id']+'</th><td>'+x['distinctDecision']+'</td><td>'+escape(x['nextAction'])+'</td></tr>'for x in d['packets'])+'</tbody></table></div><p>On a narrow screen, scroll the table horizontally. <a class="founder-queue-download" href="/workflow-assets/fictional-founder-decision-queue.csv" download>Download the fictional queue CSV</a>.</p>'
  body+='</section>'
 body+='<p><a href="/blog/the-founder-bottleneck-audit/">Start a broader founder bottleneck audit</a>, or <a href="/books/built-to-run/chapters/2/">document a recurring workflow</a>. Return to the <a href="/books/built-to-run/">Built to Run overview</a> for book purchase options and other website companions.</p><p>Original website exercise by Robertson Books. Reviewed '+escape(d['reviewed'])+'.</p>'
 (ROOT/'chapter-guides/built-to-run-1.html').write_text(body+'\n')
 out=io.StringIO(newline='');w=csv.writer(out,lineterminator='\n');w.writerow(['message_id','distinct_decision_id','next_action','owner_reserved','fictional'])
 for x in d['packets']:w.writerow([x['id'],x['distinctDecision'],x['nextAction'],str(x['ownerReserved']).lower(),'true'])
 (ROOT/'workflow-assets/fictional-founder-decision-queue.csv').write_text(out.getvalue())
 p=ROOT/'books/built-to-run/chapters/1/index.html';s=p.read_text();s=re.sub(r'<title>.*?</title>','<title>'+escape(d['title'])+' | Robertson Books</title>',s,count=1,flags=re.S)
 for key in ['description','og:title','og:description','twitter:title','twitter:description']:
  value=d['description']if'description'in key else d['title'];s=re.sub(r'(<meta\s+(?:name|property)="'+re.escape(key)+r'"\s+content=")[^"]*(")',lambda m:m[1]+escape(value,quote=True)+m[2],s)
 s=re.sub(r'<h1>.*?</h1>','<h1>'+escape(d['title'])+'</h1>',s,count=1,flags=re.S)
 pattern=r'(<div class="page-content" style="padding-top:0;">)[\s\S]*?(<div style="display:flex;justify-content:space-between;margin-top:40px;)'
 s,n=re.subn(pattern,lambda m:m[1]+'\n'+body+'\n'+m[2],s,count=1);assert n==1
 s=s.replace('<span>/</span> Chapter 1</div>','<span>/</span> '+escape(d['title'])+'</div>')
 def breadcrumb(match):
  obj=json.loads(match.group(1))
  if obj.get('@type')=='BreadcrumbList':obj['itemListElement'][-1]['name']=d['title']
  return '<script type="application/ld+json">'+json.dumps(obj,indent=2)+'</script>'
 s=re.sub(r'<script type="application/ld\+json">([\s\S]*?)</script>',breadcrumb,s)
 p.write_text(s)
 p=ROOT/'sitemap.xml';tree=ET.parse(p);ns='{http://www.sitemaps.org/schemas/sitemap/0.9}';ET.register_namespace('',ns[1:-1]);hits=0
 for entry in tree.getroot():
  if entry.find(ns+'loc').text==d['canonical']:
   hits+=1;mod=entry.find(ns+'lastmod')
   if mod is None:mod=ET.SubElement(entry,ns+'lastmod')
   mod.text=d['reviewed']
 assert hits==1;tree.write(p,encoding='utf-8',xml_declaration=True)
 print('Rendered original founder queue companion,6messages/5decisions;417owners retained')
if __name__=='__main__':render()
