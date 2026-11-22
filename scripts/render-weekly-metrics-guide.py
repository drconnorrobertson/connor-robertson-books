"""Render an original fictional metrics companion, preserving the chapter route."""
from pathlib import Path
from html import escape
import json,re,csv,io,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
def render():
 d=json.loads((ROOT/'content/weekly-metrics-guide.json').read_text())
 style='<style id="weekly-metrics-style">.page-content{min-width:0;width:100%;max-width:100%}.metrics-scroll{max-width:100%;overflow-x:auto;border:1px solid #cbd5df}.metrics-scroll:focus{outline:3px solid #9a742c;outline-offset:3px}.metrics-ledger{border-collapse:collapse;width:100%;min-width:700px}.metrics-ledger th,.metrics-ledger td{padding:12px;text-align:left;border-bottom:1px solid #cbd5df}.metrics-ledger th{background:#eef2f7}.metrics-ledger caption{text-align:left;padding:12px;font-weight:bold}.metrics-download{display:inline-flex;min-height:44px;align-items:center}@media print{.metrics-ledger{min-width:0;font-size:10px}.metrics-scroll{overflow:visible}}</style>'
 body=style+'<p><strong>Original website reading companion.</strong> '+escape(d['sourceBoundary'])+'</p>'
 for i,section in enumerate(d['sections']):
  body+='<section><h2>'+escape(section['heading'])+'</h2>'+''.join('<p>'+escape(x)+'</p>' for x in section['paragraphs'])
  if i==1:
   body+='<div class="metrics-scroll" role="region" tabindex="0" aria-label="Fictional weekly work ledger"><table class="metrics-ledger"><caption>Eight fictional work items; review cutoff November 20, 2026</caption><thead><tr>'+''.join('<th scope="col">'+h+'</th>' for h in ['Item','Received','Due','Accepted','Cancelled','Source records','Revisions'])+'</tr></thead><tbody>'
   for x in d['items']:
    body+='<tr><th scope="row">'+x['id']+'</th>'+''.join('<td>'+escape(str(x[k]) or '—')+'</td>' for k in ['received','due','accepted','cancelled','sourceRecords','revisions'])+'</tr>'
   body+='</tbody></table></div><p>Scroll the ledger horizontally on a narrow screen. <a class="metrics-download" href="/workflow-assets/fictional-weekly-work-ledger.csv" download>Download the fictional work ledger CSV</a>.</p>'
  body+='</section>'
 body+='<p><a href="/books/built-to-run/chapters/1/">Review a blocked decision queue</a> or <a href="/books/built-to-run/chapters/2/">document a recurring workflow</a>. Return to the <a href="/books/built-to-run/">Built to Run overview</a> for purchase options and other website companions.</p><p>Original website exercise by Robertson Books. Reviewed '+d['reviewed']+'.</p>'
 (ROOT/'chapter-guides/built-to-run-6.html').write_text(body+'\n')
 out=io.StringIO(newline='');keys=['id','received','due','accepted','cancelled','sourceRecords','revisions'];w=csv.writer(out,lineterminator='\n');w.writerow(keys+['fictional'])
 for x in d['items']:w.writerow([x[k] for k in keys]+['true'])
 (ROOT/'workflow-assets/fictional-weekly-work-ledger.csv').write_text(out.getvalue())
 p=ROOT/'books/built-to-run/chapters/6/index.html';s=p.read_text();s=re.sub(r'<title>.*?</title>','<title>'+escape(d['title'])+' | Robertson Books</title>',s,count=1,flags=re.S)
 for key in ['description','og:title','og:description','twitter:title','twitter:description']:
  value=d['description'] if 'description' in key else d['title'];s=re.sub(r'(<meta\s+(?:name|property)="'+re.escape(key)+r'"\s+content=")[^"]*(")',lambda m:m[1]+escape(value,quote=True)+m[2],s)
 s=re.sub(r'<h1>.*?</h1>','<h1>'+escape(d['title'])+'</h1>',s,count=1,flags=re.S)
 pattern=r'(<div class="page-content" style="padding-top:0;">)[\s\S]*?(<div style="display:flex;justify-content:space-between;margin-top:40px;)'
 s,n=re.subn(pattern,lambda m:m[1]+'\n'+body+'\n'+m[2],s,count=1);assert n==1
 s=s.replace('<span>/</span> Chapter 6</div>','<span>/</span> '+escape(d['title'])+'</div>')
 def breadcrumb(match):
  obj=json.loads(match[1])
  if obj.get('@type')=='BreadcrumbList':obj['itemListElement'][-1]['name']=d['title']
  return '<script type="application/ld+json">'+json.dumps(obj,indent=2)+'</script>'
 s=re.sub(r'<script type="application/ld\+json">([\s\S]*?)</script>',breadcrumb,s);p.write_text(s)
 p=ROOT/'sitemap.xml';tree=ET.parse(p);ns='{http://www.sitemaps.org/schemas/sitemap/0.9}';ET.register_namespace('',ns[1:-1]);hits=0
 for entry in tree.getroot():
  if entry.find(ns+'loc').text==d['canonical']:
   hits+=1;mod=entry.find(ns+'lastmod')
   if mod is None:mod=ET.SubElement(entry,ns+'lastmod')
   mod.text=d['reviewed']
 assert hits==1;tree.write(p,encoding='utf-8',xml_declaration=True)
 print('Rendered fictional weekly metrics ledger; canonical owner preserved')
if __name__=='__main__':render()
