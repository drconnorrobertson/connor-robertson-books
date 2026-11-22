"""Consolidate four unsupported chapter pages into an original follow-up exercise."""
from pathlib import Path
from html import escape
import csv,io,json,re,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
def render():
 d=json.loads((ROOT/'content/follow-up-review-guide.json').read_text());ns={'__file__':str(ROOT/'generate_site.py'),'__name__':'follow_up_render'};exec(compile((ROOT/'generate_site.py').read_text(),'site-definitions','exec'),ns)
 route='/books/the-7-minute-phone-call/follow-up-review/';overview='/books/the-7-minute-phone-call/';bc=[('Home','/'),('The 7 Minute Phone Call',overview),(d['title'],route)]
 body='<main class="page-content" style="max-width:900px;min-width:0"><h1>'+escape(d['title'])+'</h1><p><strong>Original website companion.</strong> This is not a manuscript excerpt or verified chapter summary. Its four packets and call-count log are fictional teaching examples, not client outcomes.</p><nav aria-label="Guide sections">'+''.join('<p><a href="#'+s['id']+'">'+escape(s['heading'])+'</a></p>' for s in d['sections'])+'</nav>'
 for s in d['sections']:body+='<section id="'+s['id']+'" style="scroll-margin-top:90px"><h2>'+escape(s['heading'])+'</h2>'+''.join('<p>'+escape(x)+'</p>' for x in s['paragraphs'])+'</section>'
 body+='<h2>Four fictional follow-up packets</h2>'
 for c in d['cases']:body+='<section><h3>'+c['id']+': '+escape(c['topic'])+'</h3><dl><dt>Supplied record</dt><dd>'+escape(c['source'])+'</dd><dt>Supported interpretation</dt><dd>'+escape(c['interpretation'])+'</dd><dt>Review question</dt><dd>'+escape(c['question'])+'</dd></dl></section>'
 body+='<p><a class="follow-up-download" href="/workflow-assets/fictional-follow-up-review-cases.csv" download style="display:inline-flex;min-height:44px;align-items:center">Download the fictional review packets CSV</a>.</p><p><a class="follow-up-download" href="/workflow-assets/fictional-follow-up-attempt-log.csv" download style="display:inline-flex;min-height:44px;align-items:center">Download the fictional twelve-attempt log CSV</a>.</p><p>Return to <a href="'+overview+'">The 7 Minute Phone Call overview</a> for book purchase options and other website reading companions. Use the book itself to verify its contents and chapter sequence.</p><p>Original website exercise by Robertson Books. Reviewed '+d['reviewed']+'.</p></main>'
 target=ROOT/(route.strip('/')+'/index.html');target.parent.mkdir(parents=True,exist_ok=True);target.write_text(ns['head'](d['title']+' | Robertson Books',d['description'],route,[ns['breadcrumb_schema'](bc)])+ns['header']('the-7-minute-phone-call')+ns['breadcrumb_html'](bc)+body+ns['footer']()+ns['page_end']())
 out=io.StringIO(newline='');w=csv.writer(out,lineterminator='\n');w.writerow(['packet_id','topic','supplied_record','supported_interpretation','review_question','observed_review','fictional'])
 for c in d['cases']:w.writerow([c[k] for k in ['id','topic','source','interpretation','question']]+['','true'])
 (ROOT/'workflow-assets/fictional-follow-up-review-cases.csv').write_text(out.getvalue())
 out=io.StringIO(newline='');w=csv.writer(out,lineterminator='\n');w.writerow(['attempt_id','status','recipient_alias','appointment_outcome','fictional'])
 for a in d['attempts']:w.writerow([a['id'],a['status'],a['recipientAlias'],'','true'])
 (ROOT/'workflow-assets/fictional-follow-up-attempt-log.csv').write_text(out.getvalue())
 card='<section id="follow-up-companion"><h2>Original website follow-up exercise</h2><p><a href="'+route+'">Review voicemail, referral and team handoff records</a> using fictional packets and an attempt log. This is a website companion, not verified chapter content.</p></section>'
 p=ROOT/(overview.strip('/')+'/index.html');s=p.read_text();s=re.sub(r'<!-- ownership-review:companion-nav:start -->[\s\S]*?<!-- ownership-review:companion-nav:end -->','',s)
 if card not in s:
  marker='<h2 style="margin-top:40px;">More from This Book</h2>';assert marker in s;s=s.replace(marker,card+'\n'+marker,1)
 p.write_text(s)
 cfgpath=ROOT/'vercel.json';cfg=json.loads(cfgpath.read_text());retired={f'{overview}chapters/{n}/' for n in [7,8,9,10]};anchors={7:'voicemail',8:'review',9:'referrals',10:'handoffs'}
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
 print('Rendered one original follow-up companion; consolidated four legacy chapter pages.')
if __name__=='__main__':render()
