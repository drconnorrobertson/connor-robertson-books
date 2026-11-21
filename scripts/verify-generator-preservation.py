"""Verify generator preservation in an isolated copy; never rebuild live source files."""
import ast,json,pathlib,tempfile,shutil,xml.etree.ElementTree as ET
from html import escape
from html.parser import HTMLParser
from urllib.parse import urlsplit
root=pathlib.Path(__file__).resolve().parents[1];tree=ast.parse((root/'generate_site.py').read_text());nodes=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in ('generate_sitemap','generate_vercel_json')]
with tempfile.TemporaryDirectory(prefix='books-regeneration-') as name:
 out=pathlib.Path(name)
 for p in root.rglob('*.html'):
  if '.git' in p.parts:continue
  dest=out/p.relative_to(root);dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,dest)
 for n in ['sitemap.xml','vercel.json']:shutil.copyfile(root/n,out/n)
 def write(path,content):
  p=out/path;p.write_text(content);return str(p)
 env={'Path':pathlib.Path,'HTMLParser':HTMLParser,'ET':ET,'escape':escape,'urlsplit':urlsplit,'json':json,'OUTPUT_DIR':str(out),'SITE_URL':'https://www.drconnorrobertsonbooks.com','write_file':write}
 exec(compile(ast.Module(body=nodes,type_ignores=[]),'actual-generator-functions','exec'),env)
 def records():
  return {e.find('{*}loc').text:(e.find('{*}lastmod').text if e.find('{*}lastmod') is not None else None) for e in ET.parse(out/'sitemap.xml').getroot()}
 before=records();cfg=json.loads((out/'vercel.json').read_text());env['generate_sitemap']();after=records();assert before==after,(len(before),len(after),set(after)-set(before),set(before)-set(after))
 env['generate_vercel_json']();assert json.loads((out/'vercel.json').read_text())==cfg
 first=(out/'sitemap.xml').read_bytes();env['generate_sitemap']();assert (out/'sitemap.xml').read_bytes()==first
 # A new source fragment and noindex page cannot leak into the sitemap.
 (out/'fragment.html').write_text('<p>Authored fragment</p>')
 (out/'private.html').write_text('<link rel="canonical" href="https://www.drconnorrobertsonbooks.com/private/"><meta name="robots" content="NOINDEX, follow">')
 env['generate_sitemap']();assert records()==before
 # Invalid double-slash canonicals fail loudly instead of creating bad URLs.
 (out/'invalid.html').write_text('<link rel="canonical" href="https://www.drconnorrobertsonbooks.com/books//invalid/">')
 try:env['generate_sitemap']()
 except ValueError as error:assert 'Invalid sitemap canonical' in str(error)
 else:raise AssertionError('Invalid canonical accepted')
 print(f'PASS:{len(before)}canonicalowners and editorial dates preserved; config and8redirects preserved; repeated sitemap build stable; fragments/noindex excluded; double-slash canonical rejected.')
