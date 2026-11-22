"""Retire unverified generated chapter claims and expose authored website companions."""
from pathlib import Path
from html import escape
from urllib.parse import urlsplit
import json,re,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
def render():
 d=json.loads((ROOT/'content/website-reading-navigation.json').read_text());retired={r['path']:r['book'] for r in d['retired']};assert len(retired)==25
 ns={'__file__':str(ROOT/'generate_site.py'),'__name__':'website_reading_retirement'};exec(compile((ROOT/'generate_site.py').read_text(),'site-definitions','exec'),ns);books={b['slug']:b for b in ns['BOOKS']};changed=[]
 for p in sorted((ROOT/'books').rglob('index.html')):
  relative='/'+str(p.relative_to(ROOT)).removesuffix('index.html')
  if relative in retired:continue
  slug=p.relative_to(ROOT).parts[1]
  if slug not in books:continue
  text=p.read_text();original=text;book=books[slug]
  if '<aside class="sidebar">' in text:
   active='landing' if relative==f'/books/{slug}/' else 'lessons' if '/key-lessons/' in relative else 'who' if '/who-should-read/' in relative else 'ch'+p.parent.name if '/chapters/' in relative else ''
   text,n=re.subn(r'<aside class="sidebar">[\s\S]*?</aside>',lambda m:ns['book_sidebar'](book,active),text);assert n==1,p
  if relative==f'/books/{slug}/':
   start=text.find('<div class="book-intro">');end=text.find('<h2 style="margin-top:40px;">More from This Book</h2>')
   if start!=-1:
    assert end>start,p;text=text[:start]+ns['website_reading_section'](book)+'\n        '+text[end:]
   else:
    text,n=re.subn(r'<section id="website-companions">[\s\S]*?</section>',lambda m:ns['website_reading_section'](book),text);assert n==1,p
  if relative in d['authoredChapterRoutes']:
   nav='<div style="display:flex;justify-content:space-between;margin-top:40px;padding-top:20px;border-top:1px solid var(--border);"><a href="/books/built-to-run/#website-companions">Original website reading companions</a></div>'
   text,n=re.subn(r'<div style="display:flex;justify-content:space-between;margin-top:40px;padding-top:20px;border-top:1px solid var\(--border\);">[\s\S]*?</div>',lambda m:nav,text);assert n==1,p
  if relative=='/books/built-to-run/chapters/2/':
   companion=d['documentationCompanion'];title=companion['title']+' | Robertson Books';text=re.sub(r'<title>[\s\S]*?</title>','<title>'+escape(title)+'</title>',text,count=1);text=re.sub(r'<h1>[\s\S]*?</h1>','<h1>'+escape(companion['title'])+'</h1>',text,count=1)
   def meta(m):
    tag=m[0];key=re.search(r'(?:name|property)="([^"]+)"',tag)
    if not key:return tag
    value=title if key[1] in ['og:title','twitter:title'] else companion['description'] if key[1] in ['description','og:description','twitter:description'] else None
    return re.sub(r'content="[^"]*"','content="'+escape(value,quote=True)+'"',tag) if value is not None else tag
   text=re.sub(r'<meta\b[^>]*>',meta,text)
   def schema(m):
    obj=json.loads(m[1])
    if obj.get('@type')=='BreadcrumbList':obj['itemListElement'][-1]['name']=companion['title'];return '<script type="application/ld+json">'+json.dumps(obj,indent=2)+'</script>'
    return m[0]
   text=re.sub(r'<script type="application/ld\+json">([\s\S]*?)</script>',schema,text)
   bc=[('Home','/'),('Built to Run','/books/built-to-run/'),(companion['title'],relative)];text,n=re.subn(r'<div class="breadcrumb">[\s\S]*?</div>',lambda m:ns['breadcrumb_html'](bc),text);assert n==1,p
  if text!=original:p.write_text(text);changed.append(relative)
 cfgpath=ROOT/'vercel.json';cfg=json.loads(cfgpath.read_text());forms=set(retired)|{p[:-1] for p in retired};cfg['redirects']=[r for r in cfg['redirects'] if r['source'] not in forms]
 for old,book in retired.items():
  for form in [old,old[:-1]]:cfg['redirects'].append({'source':form,'destination':f'/books/{book}/#website-companions','permanent':True})
 cfgpath.write_text(json.dumps(cfg,indent=2)+'\n')
 p=ROOT/'sitemap.xml';tree=ET.parse(p);space='{http://www.sitemaps.org/schemas/sitemap/0.9}';ET.register_namespace('',space[1:-1]);origin='https://www.drconnorrobertsonbooks.com'
 for entry in list(tree.getroot()):
  route=urlsplit(entry.find(space+'loc').text).path
  if route in retired:tree.getroot().remove(entry)
  elif route in changed:
   date=entry.find(space+'lastmod')
   if date is None:date=ET.SubElement(entry,space+'lastmod')
   date.text=d['reviewed']
 tree.write(p,encoding='utf-8',xml_declaration=True)
 for old in retired:
  p=ROOT/old.lstrip('/')/'index.html'
  if p.exists():p.unlink()
 print(json.dumps({'retiredUnverifiedPreviews':25,'navigationOwnersUpdated':len(changed),'chapterBodies':'three authored fragments retained','routes':'book overview #website-companions'}))
if __name__=='__main__':render()
