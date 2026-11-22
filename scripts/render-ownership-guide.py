"""Render the authored ownership guide and reconcile its retired template variants."""
from pathlib import Path
from html import escape
from urllib.parse import urlsplit
import json,re,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
O='https://www.drconnorrobertsonbooks.com'
SLUG='real-estate-ownership-mistakes';PATH='/blog/'+SLUG+'/'
RETIRED=['real-estate-ownership-'+lens for lens in ['field-guide','scorecard','questions','checklist','examples','red-flags','implementation','faq','advanced']]

def render():
 data=json.loads((ROOT/'content/ownership-cash-guide.json').read_text());assert data['canonical']==O+PATH
 target=ROOT/PATH.lstrip('/')/'index.html';s=target.read_text()
 s=re.sub(r'<title>[\s\S]*?</title>','<title>'+escape(data['title'])+' | Robertson Books</title>',s,count=1)
 values={'description':data['description'],'og:title':data['title'],'og:description':data['description'],'twitter:title':data['title'],'twitter:description':data['description'],'article:published_time':data['originalPublication'],'article:modified_time':data['revision']}
 for key,value in values.items():
  pattern=r'<meta\b[^>]*(?:name|property)="'+re.escape(key)+r'"[^>]*>'
  tag='<meta '+('property'if key.startswith(('og:','article:'))else'name')+'="'+key+'" content="'+escape(value,quote=True)+'">'
  if re.search(pattern,s):s=re.sub(pattern,lambda m:tag,s)
  else:s=s.replace('</head>',tag+'</head>',1)
 s=re.sub(r'<h1>.*?</h1>','<h1>'+escape(data['h1'])+'</h1>',s,count=1,flags=re.S)
 s=re.sub(r'<p class="dek">.*?</p>','<p class="dek">'+escape(data['description'])+'</p>',s,count=1,flags=re.S)
 s=re.sub(r'<p class="eyebrow">.*?</p>','<p class="eyebrow">Ownership cash · Worked guide</p>',s,count=1,flags=re.S)
 s=re.sub(r'<div class="meta">.*?</div>','<div class="meta"><span>Published '+data['originalPublication']+'</span><span>Updated '+data['revision']+'</span><span>Robertson Books educational guide</span></div>',s,count=1,flags=re.S)
 s=re.sub(r'<article class="article">[\s\S]*?</article>',lambda m:'<article class="article">'+data['body']+'</article>',s,count=1)
 def schema(match):
  obj=json.loads(match.group(1));nodes=obj.get('@graph',[obj]);nodes=[n for n in nodes if n.get('@type')!='FAQPage']
  for n in nodes:
   if n.get('@type')=='Article':n.update(headline=data['title'],description=data['description'],datePublished=data['originalPublication'],dateModified=data['revision'],author={'@type':'Organization','name':'Robertson Books','url':O+'/'})
   if n.get('@type')=='BreadcrumbList':n['itemListElement'][-1]['name']=data['title']
  if'@graph'in obj:obj['@graph']=nodes
  return '<script type="application/ld+json">'+json.dumps(obj,ensure_ascii=False,indent=2).replace('<','\\u003c')+'</script>'
 s=re.sub(r'<script type="application/ld\+json">([\s\S]*?)</script>',schema,s)
 s=s.replace('</style>','\n/* Authored comparison: keep wide tables inside a keyboard-accessible region. */\n.article{min-width:0}.article [role="region"]{max-width:100%}.article table{min-width:560px}.article th,.article td{vertical-align:top;padding:.65rem}.article h2[id]{scroll-margin-top:100px}\n</style>',1)if'Authored comparison: keep wide tables'not in s else s
 s=s.replace("Browse all 100 guides","Browse the learning library")
 target.write_text(s)
 # HTTP redirects are authoritative; these source fallbacks cannot re-enter a regenerated sitemap.
 for slug in RETIRED:
  p=ROOT/'blog'/slug/'index.html';p.write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Guide moved | Robertson Books</title><meta name="robots" content="noindex,follow"><link rel="canonical" href="'+O+PATH+'"></head><body><main><h1>Ownership guide moved</h1><p><a href="'+PATH+'">'+escape(data['title'])+'</a></p></main></body></html>\n')
 aliases={O+'/blog/'+slug+'/'for slug in RETIRED}|{'/blog/'+slug+'/'for slug in RETIRED}|{O+PATH,PATH}
 for p in ROOT.rglob('*.html'):
  if'.git'in p.parts or p==target or p.parent.name in RETIRED:continue
  html=p.read_text();seen=set()
  def anchor(m):
   tag=m.group(0);href=re.search(r'href="([^"]+)"',tag)
   if not href or href.group(1).rstrip('/')+'/'not in aliases:return tag
   class_match=re.search(r'class="([^"]+)"',tag);kind=class_match.group(1)if class_match else'plain'
   # The archive formerly listed the same topic ten times; retain one current destination.
   if kind=='archive-link'and kind in seen:return ''
   seen.add(kind);tag=tag.replace(href.group(1),PATH,1)
   if'<strong>'in tag:tag=re.sub(r'<strong>.*?</strong>','<strong>'+escape(data['title'])+'</strong>',tag,flags=re.S)
   elif kind=='archive-link':tag='<a class="archive-link" href="'+PATH+'">'+escape(data['title'])+' <span aria-hidden="true">→</span></a>'
   return tag
  html=re.sub(r'<a\b[^>]*>[\s\S]*?</a>',anchor,html)
  html=html.replace('Browse all 100 guides','Browse the learning library')
  if html!=p.read_text():p.write_text(html)
 # Existing additional pages have distinct topic bodies; expose them as reading
 # companions without presenting their content as verified manuscript excerpts.
 for book,numbers in [('built-to-run',[8,9,10]),('buying-wealth',[9,10]),('the-7-minute-phone-call',[7,8,9,10])]:
  overview=ROOT/'books'/book/'index.html';html=overview.read_text();start='<!-- ownership-review:companion-nav:start -->';end='<!-- ownership-review:companion-nav:end -->'
  html=re.sub(re.escape(start)+r'[\s\S]*?'+re.escape(end),'',html)
  items=[]
  for number in numbers:
   route='/books/'+book+'/chapters/'+str(number)+'/'
   page=(ROOT/route.lstrip('/')/'index.html').read_text()
   headings=re.findall(r'<h2[^>]*>([\s\S]*?)</h2>',page)
   label=re.sub('<[^>]+>','',headings[0]) if headings else 'Companion '+str(number)
   label=re.sub(r'^Chapter \d+:\s*','',label)
   items.append('<li><a href="'+route+'">'+label+'</a></li>')
  section=start+'<section class="section"><div class="container"><h2>Additional reading companions</h2><p>Explore these existing website discussions alongside the book overview. They are companion pages, not verified manuscript excerpts.</p><ul>'+''.join(items)+'</ul></div></section>'+end
  assert '<footer'in html
  html=html.replace('<footer',section+'<footer',1);overview.write_text(html)
 cfg=json.loads((ROOT/'vercel.json').read_text());rules=cfg.setdefault('redirects',[])
 for slug in RETIRED:
  for slash in['','/']:
   source='/blog/'+slug+slash;rule=next((r for r in rules if r['source']==source),None)
   expected={'source':source,'destination':PATH,'permanent':True}
   if rule:assert rule==expected,source
   else:rules.append(expected)
 (ROOT/'vercel.json').write_text(json.dumps(cfg,indent=2)+'\n')
 p=ROOT/'sitemap.xml';tree=ET.parse(p);root=tree.getroot();ns='{http://www.sitemaps.org/schemas/sitemap/0.9}';ET.register_namespace('',ns[1:-1])
 for entry in list(root):
  loc=entry.find(ns+'loc')
  if loc is None:continue
  if urlsplit(loc.text).path.strip('/').split('/')[-1]in RETIRED:root.remove(entry)
  elif loc.text==O+PATH:
   mod=entry.find(ns+'lastmod')
   if mod is None:mod=ET.SubElement(entry,ns+'lastmod')
   mod.text=data['revision']
 tree.write(p,encoding='utf-8',xml_declaration=True)
 assert sum(e.find(ns+'loc').text==O+PATH for e in root)==1
 assert not any(e.find(ns+'loc').text in {O+'/blog/'+x+'/'for x in RETIRED}for e in root)
 print('Rendered ownership guide;9retiredvariants;18slash-specificredirects;'+str(len(root))+'sitemapowners')
if __name__=='__main__':render()
