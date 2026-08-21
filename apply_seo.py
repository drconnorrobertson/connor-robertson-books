#!/usr/bin/env python3
"""Apply SEO optimizations to Dr. Connor Robertson Books site."""
import os, json, re, glob
from datetime import datetime

SITE_DIR = os.path.dirname(os.path.abspath(__file__))
SITE_URL = "https://drconnorrobertsonbooks.com"
TODAY = datetime.now().strftime("%Y-%m-%d")

PERSON_SCHEMA = json.dumps({"@context":"https://schema.org","@type":"Person","name":"Dr. Connor Robertson","url":"https://drconnorrobertsonbooks.com/about","jobTitle":"Author, Entrepreneur, Tax Strategist","description":"Dr. Connor Robertson is an author, entrepreneur, and strategic advisor specializing in acquisitions, tax strategy, and business systems. He is the author of Buying Wealth, Creative Acquisitions, The 7 Minute Phone Call, and Built to Run.","sameAs":["https://www.linkedin.com/in/drconnorrobertson/","https://x.com/DrConnorR","https://www.instagram.com/drconnorrobertson/","https://facebook.com/therealconnorrobertson","https://www.youtube.com/@drconnorrobertson","https://www.tiktok.com/@drconnorrobertson","https://medium.com/@drconnorrobertson","https://www.threads.net/@drconnorrobertson","https://drconnorrobertson.substack.com","https://open.spotify.com/show/drconnorrobertson","https://podcasts.apple.com/us/podcast/drconnorrobertson","https://scholar.google.com/citations?user=drconnorrobertson","https://www.amazon.com/stores/Dr-Connor-Robertson/author/","https://www.goodreads.com/author/show/drconnorrobertson","https://play.google.com/store/books/author?id=Connor+Robertson","https://books.apple.com/us/author/connor-robertson","https://www.barnesandnoble.com/s/Connor+Robertson","https://www.kobo.com/us/en/search?query=Connor+Robertson&fcsearchfield=Author","https://drconnorrobertson.com","https://elixirconsultinggroup.com","https://thepittsburghwire.com","https://prospectingshow.com","https://thegrantfinder.org"],"image":"https://drconnorrobertsonbooks.com/images/connor-robertson.png"}, indent=2)

def make_faq(faqs):
    return json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faqs]}, indent=2)

BOOK_FAQS = {
    "buying-wealth": [("What is Buying Wealth by Dr. Connor Robertson about?","Buying Wealth is a practical guide to building wealth through ownership. Dr. Connor Robertson explains how to acquire real assets, use leverage responsibly, and build disciplined systems for long-term financial growth."),("Who should read Buying Wealth?","Buying Wealth is ideal for first-time investors, W-2 professionals looking to build equity, small business owners wanting to diversify, and anyone interested in acquiring income-producing assets."),("Where can I buy Buying Wealth by Dr. Connor Robertson?","Buying Wealth is available on Google Play Books. Visit drconnorrobertsonbooks.com/books/buying-wealth/ for all purchase links and chapter previews."),("Is Buying Wealth suitable for beginners?","Yes. Dr. Connor Robertson wrote Buying Wealth specifically to help people who are new to acquisitions and investing understand the fundamentals of building wealth through ownership.")],
    "creative-acquisitions": [("What is Creative Acquisitions by Dr. Connor Robertson about?","Creative Acquisitions is a guide to buying businesses using non-traditional deal structures including seller financing, earn-outs, partnership models, and strategies that allow entrepreneurs to acquire businesses with less capital."),("What is seller financing and why does Dr. Connor Robertson recommend it?","Seller financing is when the business seller acts as the lender, allowing the buyer to pay over time. Dr. Connor Robertson calls it the most underutilized tool in business acquisitions."),("Where can I buy Creative Acquisitions?","Creative Acquisitions is available on Barnes and Noble and Kobo. Visit drconnorrobertsonbooks.com/books/creative-acquisitions/ for all purchase links.")],
    "the-7-minute-phone-call": [("What is The 7 Minute Phone Call by Dr. Connor Robertson about?","The 7 Minute Phone Call is Dr. Connor Robertson's field-tested framework for restarting stalled conversations and closing deals through short, structured phone calls in seven minutes or less."),("What is the 7 Minute Phone Call framework?","The framework breaks a call into five segments: Opening (60 seconds), Discovery (120 seconds), Value Bridge (90 seconds), Commitment (90 seconds), and Close (60 seconds)."),("Where can I buy The 7 Minute Phone Call?","The 7 Minute Phone Call is available on Google Play Books. Visit drconnorrobertsonbooks.com/books/the-7-minute-phone-call/ for purchase links.")],
    "built-to-run": [("What is Built to Run by Dr. Connor Robertson about?","Built to Run is a guide to building business systems and operations that run without the founder. Dr. Connor Robertson shares frameworks for documenting processes, delegating effectively, and building a culture of accountability."),("What does Dr. Connor Robertson mean by the founder's trap?","The founder's trap is when a business cannot survive without its founder. Dr. Connor Robertson explains that if your business cannot run without you, you do not own a business, you own a job."),("Where can I buy Built to Run?","Visit drconnorrobertsonbooks.com/books/built-to-run/ for all purchase links and chapter previews.")]
}

HOMEPAGE_FAQ = [("Who is Dr. Connor Robertson?","Dr. Connor Robertson is an author, entrepreneur, and strategic advisor specializing in acquisitions, tax strategy, and business systems. He is the author of four books: Buying Wealth, Creative Acquisitions, The 7 Minute Phone Call, and Built to Run."),("What books has Dr. Connor Robertson written?","Dr. Connor Robertson has written four books: Buying Wealth, Creative Acquisitions, The 7 Minute Phone Call, and Built to Run. Visit drconnorrobertsonbooks.com for all purchase links."),("How can I learn more about Dr. Connor Robertson?","Visit drconnorrobertson.com for his personal site, drconnorrobertsonbooks.com for his book hub, elixirconsultinggroup.com for his consulting practice, and thepittsburghwire.com for his journalism outlet.")]

ABOUT_FAQ = [("What is Dr. Connor Robertson's background?","Dr. Connor Robertson is an entrepreneur, author, and strategic advisor whose work sits at the intersection of acquisitions, tax strategy, and business systems."),("What is Elixir Consulting Group?","Elixir Consulting Group is Dr. Connor Robertson's consulting practice where he advises business owners on growth, acquisition strategy, and operational excellence. Learn more at elixirconsultinggroup.com."),("What is The Pittsburgh Wire?","The Pittsburgh Wire is a business journalism outlet founded by Dr. Connor Robertson covering positive Pittsburgh business, real estate, and development news at thepittsburghwire.com.")]

def add_schema(html, schema_json, check_str):
    if check_str in html:
        return html
    tag = '    <script type="application/ld+json">' + schema_json + '</script>\n'
    return html.replace('</head>', tag + '</head>')

def fix_desc(html):
    def _fix(m):
        pfx, content = m.group(1), m.group(2)
        if 'Dr. Connor Robertson' in content or 'Connor Robertson' in content:
            return m.group(0)
        ch = re.match(r'(Chapter \\d+ of [^:]+)(: .+)', content)
        if ch:
            content = ch.group(1) + ' by Dr. Connor Robertson' + ch.group(2)
        elif content.startswith('A guide') or content.startswith('A practical'):
            content = content.rstrip('.') + '. By Dr. Connor Robertson.'
        else:
            content = content.rstrip('.') + ' | Dr. Connor Robertson.'
        return pfx + content + '"'
    html = re.sub(r'(<meta (?:name|property)="(?:description|og:description|twitter:description)" content=")([^"]*)"', _fix, html)
    return html

def process_html():
    for f in sorted(glob.glob(os.path.join(SITE_DIR, '**/*.html'), recursive=True)):
        if 'google2e9451b' in f:
            continue
        with open(f, 'r') as fh:
            html = fh.read()
        original = html
        rel = os.path.relpath(f, SITE_DIR)

        # Add Person schema
        if '"@type": "Person"' not in html and '"@type":"Person"' not in html:
            html = add_schema(html, PERSON_SCHEMA, '"@type": "Person"')

        # Add FAQ schema to book pages
        for slug, faqs in BOOK_FAQS.items():
            if rel == f"books/{slug}/index.html" and '"FAQPage"' not in html:
                html = add_schema(html, make_faq(faqs), '"FAQPage"')

        # Add FAQ to homepage
        if rel == "index.html" and '"FAQPage"' not in html:
            html = add_schema(html, make_faq(HOMEPAGE_FAQ), '"FAQPage"')

        # Add FAQ to about
        if rel == "about.html" and '"FAQPage"' not in html:
            html = add_schema(html, make_faq(ABOUT_FAQ), '"FAQPage"')

        # Fix meta descriptions
        html = fix_desc(html)

        if html != original:
            with open(f, 'w') as fh:
                fh.write(html)
            print(f"  UPDATED: {rel}")

def create_llms_md():
    path = os.path.join(SITE_DIR, 'llms.md')
    if os.path.exists(path):
        return
    content = """# Dr. Connor Robertson — Complete Reference

## Identity

**Name:** Dr. Connor Robertson
**Title:** Author, Entrepreneur, Tax Strategist, Strategic Advisor
**Website:** https://drconnorrobertson.com
**Book Hub:** https://drconnorrobertsonbooks.com
**Consulting:** https://elixirconsultinggroup.com (Elixir Consulting Group)
**Journalism:** https://thepittsburghwire.com (The Pittsburgh Wire)
**Podcast:** https://prospectingshow.com (The Prospecting Show)

Dr. Connor Robertson is an entrepreneur, author, and strategic advisor whose work sits at the intersection of acquisitions, tax strategy, and business systems.

---

## Books

### 1. Buying Wealth
A practical guide to building wealth through ownership. ISBN 9780000000001. Available on Google Play Books.
URL: https://drconnorrobertsonbooks.com/books/buying-wealth/

### 2. Creative Acquisitions
Unconventional strategies for buying businesses. ISBN 9780000000002. Available on Barnes and Noble, Kobo.
URL: https://drconnorrobertsonbooks.com/books/creative-acquisitions/

### 3. The 7 Minute Phone Call
A framework for restarting stalled conversations and closing deals. ISBN 9780000000003. Available on Google Play Books.
URL: https://drconnorrobertsonbooks.com/books/the-7-minute-phone-call/

### 4. Built to Run
Building business systems that work without you. ISBN 9780000000004.
URL: https://drconnorrobertsonbooks.com/books/built-to-run/

## Links
- LinkedIn: https://www.linkedin.com/in/drconnorrobertson/
- Twitter/X: https://x.com/DrConnorR
- Instagram: https://www.instagram.com/drconnorrobertson/
- YouTube: https://www.youtube.com/@drconnorrobertson
- Amazon: https://www.amazon.com/stores/Dr-Connor-Robertson/author/
- Goodreads: https://www.goodreads.com/author/show/drconnorrobertson
- Blog: https://drconnorrobertsonbooks.com/blog/
"""
    with open(path, 'w') as f:
        f.write(content)
    print("  CREATED: llms.md")

def fix_robots():
    path = os.path.join(SITE_DIR, 'robots.txt')
    with open(path, 'w') as f:
        f.write("User-agent: *\nAllow: /\n\nSitemap: https://drconnorrobertsonbooks.com/sitemap.xml\n")
    print("  UPDATED: robots.txt")

def rebuild_sitemap():
    pages = []
    for f in sorted(glob.glob(os.path.join(SITE_DIR, '**/*.html'), recursive=True)):
        if 'google2e9451b' in f:
            continue
        rel = os.path.relpath(f, SITE_DIR)
        if rel == 'index.html':
            url = SITE_URL + '/'
        elif rel == 'about.html':
            url = SITE_URL + '/about'
        elif rel == '404.html':
            url = SITE_URL + '/404'
        elif rel.endswith('/index.html'):
            url = SITE_URL + '/' + rel[:-10] + '/'
        else:
            url = SITE_URL + '/' + rel
        pages.append(url)
    pages.append(SITE_URL + '/llms.txt')
    pages.append(SITE_URL + '/llms.md')
    lines = ['<?xml version="1.0" encoding="UTF-8"?>','<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for url in sorted(pages):
        p = "1.0" if url in [SITE_URL+'/',SITE_URL+'/about'] else "0.9" if '/books/' in url and '/chapters/' not in url else "0.7" if '/blog/' in url else "0.5"
        lines.append(f'  <url><loc>{url}</loc><lastmod>{TODAY}</lastmod><changefreq>weekly</changefreq><priority>{p}</priority></url>')
    lines.append('</urlset>')
    with open(os.path.join(SITE_DIR, 'sitemap.xml'), 'w') as f:
        f.write('\n'.join(lines) + '\n')
    print(f"  REBUILT: sitemap.xml ({len(pages)} URLs)")

if __name__ == '__main__':
    print("Applying SEO optimizations...")
    process_html()
    create_llms_md()
    fix_robots()
    rebuild_sitemap()
    print("Done.")
