#!/usr/bin/env python3
"""Site generator for Dr. Connor Robertson's author/books hub."""

import os
import json
from datetime import datetime

SITE_URL = "https://connorrobertsonbooks.com"
AUTHOR_NAME = "Dr. Connor Robertson"
OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

# ── Book Data ──────────────────────────────────────────────────────────────────

BOOKS = [
    {
        "slug": "buying-wealth",
        "title": "Buying Wealth",
        "subtitle": "A Practical Guide to Building Ownership",
        "description": "A practical guide to building ownership by buying real assets, using leverage responsibly, and building disciplined systems for growth. Dr. Connor Robertson breaks down how ordinary people can build extraordinary wealth not by earning more, but by owning more.",
        "long_description": "Buying Wealth challenges the conventional wisdom that wealth comes from high income. Instead, Dr. Connor Robertson lays out a systematic framework for acquiring assets that generate returns, using leverage as a strategic tool rather than a liability, and building the disciplines required for long-term financial growth. Drawing on years of experience in acquisitions and tax strategy, this book provides a roadmap for anyone ready to shift from earning wealth to owning it.",
        "google_play_id": "Dw2HEQAAQBAJ",
        "amazon_url": "https://www.amazon.com/s?k=Buying+Wealth+Connor+Robertson",
        "bn_url": "https://www.barnesandnoble.com/s/Buying+Wealth+Connor+Robertson",
        "google_play_url": "https://play.google.com/store/books/details?id=Dw2HEQAAQBAJ",
        "color": "#1a5276",
        "accent": "#2e86c1",
        "isbn": "9780000000001",
        "publisher": "Independent",
        "chapters": [
            {"num": 1, "title": "The Ownership Mindset", "summary": "Why building wealth starts with a fundamental shift in how you think about money, income, and assets. The difference between earning and owning is the foundation of every strategy in this book."},
            {"num": 2, "title": "What to Buy and Why", "summary": "Not all assets are created equal. Learn how to evaluate opportunities, understand cap rates and cash-on-cash returns, and identify the assets most likely to build long-term wealth."},
            {"num": 3, "title": "Leverage as a Tool, Not a Trap", "summary": "Debt is the most misunderstood tool in wealth building. This chapter breaks down how to use leverage strategically while avoiding the pitfalls that sink most investors."},
            {"num": 4, "title": "Building Your Acquisition System", "summary": "Wealth building is not a one-time event. Learn how to create repeatable systems for sourcing, evaluating, and closing deals so that growth becomes a process, not a gamble."},
            {"num": 5, "title": "The Due Diligence Framework", "summary": "Every acquisition lives or dies on the quality of your research. This chapter provides a step-by-step framework for evaluating any potential purchase."},
            {"num": 6, "title": "Financing Strategies for Real Assets", "summary": "From traditional bank loans to seller financing and creative structures, explore the full range of options for funding your acquisitions."},
            {"num": 7, "title": "Protecting What You Build", "summary": "Wealth preservation is just as important as wealth creation. Learn the legal structures, tax strategies, and insurance frameworks that protect your portfolio."},
            {"num": 8, "title": "Scaling the Portfolio", "summary": "Once you have the system working, how do you grow it? This final chapter addresses scaling, delegation, and building a portfolio that compounds over time."}
        ],
        "key_lessons": [
            "Wealth is built through ownership, not income alone",
            "Leverage, used responsibly, is the most powerful accelerator available to ordinary investors",
            "Every acquisition should be evaluated through a systematic framework, not gut instinct",
            "Due diligence is not optional; it is the single most important step in any deal",
            "Tax strategy is not an afterthought; it is a core component of wealth building",
            "Scaling requires systems, not just ambition",
            "Protecting wealth requires as much discipline as building it",
            "The best time to start buying assets is before you feel ready"
        ],
        "who_should_read": {
            "audiences": [
                {"name": "First-time investors", "reason": "looking to understand how to acquire their first real asset and build a foundation for long-term wealth"},
                {"name": "W-2 professionals", "reason": "earning good incomes but not building equity, who want to shift from trading time for money to owning assets that work for them"},
                {"name": "Small business owners", "reason": "interested in diversifying beyond their primary business into real estate or other acquisitions"},
                {"name": "Real estate investors", "reason": "who want a more systematic approach to evaluating and acquiring properties"},
                {"name": "Anyone tired of conventional financial advice", "reason": "who recognizes that saving and budgeting alone will not build generational wealth"}
            ]
        },
        "review_quotes": [
            {"text": "A refreshingly practical approach to wealth building that cuts through the noise.", "reviewer": "Amazon Reader"},
            {"text": "Finally, a book that explains how real people build real wealth through ownership.", "reviewer": "Google Play Review"},
            {"text": "Robertson's framework for evaluating acquisitions is worth the price of the book alone.", "reviewer": "Verified Purchaser"}
        ]
    },
    {
        "slug": "creative-acquisitions",
        "title": "Creative Acquisitions",
        "subtitle": "Unconventional Strategies for Buying Businesses",
        "description": "A guide to creative approaches for business acquisitions, covering non-traditional deal structures, seller financing, earn-outs, and strategies that allow entrepreneurs to acquire businesses with less capital and more creativity.",
        "long_description": "Creative Acquisitions is the playbook for entrepreneurs who want to buy businesses but do not have deep pockets or private equity backing. Dr. Connor Robertson draws on real-world deal experience to show how creative structuring, seller financing, earn-outs, and partnership arrangements can make acquisitions accessible to a much wider range of buyers. This book is about thinking differently about deals and finding paths to ownership that conventional wisdom overlooks.",
        "amazon_url": "https://www.amazon.com/s?k=Creative+Acquisitions+Connor+Robertson",
        "bn_url": "https://www.barnesandnoble.com/s/Creative+Acquisitions+Connor+Robertson",
        "google_play_url": "https://play.google.com/store/books/collection/cluster?gsr=ShtCGQoXChVDcmVhdGl2ZSBBY3F1aXNpdGlvbnM%3D",
        "color": "#1a4731",
        "accent": "#27ae60",
        "isbn": "9780000000002",
        "publisher": "Independent",
        "chapters": [
            {"num": 1, "title": "Why Creative Deals Win", "summary": "Traditional acquisition paths are crowded, expensive, and often inaccessible. Learn why creative deal structures are not just alternatives but often superior approaches to buying businesses."},
            {"num": 2, "title": "Seller Financing Deep Dive", "summary": "The most powerful tool in the creative acquirer's toolkit. Understand how to structure seller-financed deals that work for both buyer and seller."},
            {"num": 3, "title": "Earn-Outs and Performance-Based Structures", "summary": "How to bridge valuation gaps and reduce risk by tying purchase price to future performance. A win-win approach that gets more deals done."},
            {"num": 4, "title": "Partnership and Joint Venture Models", "summary": "You do not always have to buy 100% of a business. Explore partnership structures that allow you to acquire control and upside with reduced capital requirements."},
            {"num": 5, "title": "Finding Off-Market Deals", "summary": "The best acquisitions are often the ones nobody else knows about. Learn systematic approaches for finding businesses whose owners are ready to sell but have not listed."},
            {"num": 6, "title": "Negotiation for Creative Deals", "summary": "Creative structures require a different negotiation approach. This chapter covers how to present unconventional terms in ways that build trust and close deals."},
            {"num": 7, "title": "Due Diligence for Acquired Businesses", "summary": "What to look for, what to verify, and what red flags should stop a deal in its tracks. A practical due diligence checklist for business acquisitions."}
        ],
        "key_lessons": [
            "You do not need a fortune to acquire a business; you need creativity and discipline",
            "Seller financing is the most underutilized tool in business acquisitions",
            "Earn-outs can bridge the gap between what a seller wants and what a buyer can afford",
            "Off-market deals are where the best opportunities live",
            "Negotiation is about understanding the seller's real motivations, not just the price",
            "Due diligence protects you from the deals that look good on paper but fail in reality",
            "Creative structures often result in better alignment between buyer and seller than traditional deals"
        ],
        "who_should_read": {
            "audiences": [
                {"name": "Aspiring business buyers", "reason": "who want to acquire a business but lack the capital for a traditional purchase"},
                {"name": "Entrepreneurs", "reason": "looking to grow through acquisition rather than organic growth alone"},
                {"name": "Search fund operators", "reason": "seeking creative deal structures beyond the standard leveraged buyout model"},
                {"name": "Business brokers and advisors", "reason": "who want to expand their toolkit for getting deals closed"},
                {"name": "Anyone interested in entrepreneurship through acquisition", "reason": "as a path to business ownership without starting from scratch"}
            ]
        },
        "review_quotes": [
            {"text": "Robertson turns complex deal structures into clear, actionable strategies.", "reviewer": "Barnes & Noble Reader"},
            {"text": "This is the book I wish I had before my first acquisition.", "reviewer": "Verified Purchaser"},
            {"text": "Practical, no-nonsense advice for anyone serious about buying a business.", "reviewer": "Amazon Review"}
        ]
    },
    {
        "slug": "the-7-minute-phone-call",
        "title": "The 7 Minute Phone Call",
        "subtitle": "Restart Stalled Conversations and Move Deals Forward",
        "description": "A guide showing entrepreneurs how to restart stalled conversations and move deals forward with short, structured phone calls. Learn the framework that turns cold leads into closed deals in just seven minutes.",
        "long_description": "The 7 Minute Phone Call is Dr. Connor Robertson's field-tested framework for the single most underrated skill in business: picking up the phone. In an era of email chains, CRM automations, and social media outreach, the direct phone call remains the fastest way to restart a stalled deal, reconnect with a prospect, or move a relationship forward. This book gives you the exact structure, scripts, and mindset to make every call count, all in seven minutes or less.",
        "amazon_url": "https://www.amazon.com/s?k=The+7+Minute+Phone+Call+Connor+Robertson",
        "bn_url": "https://www.barnesandnoble.com/s/The+7+Minute+Phone+Call+Connor+Robertson",
        "google_play_url": "https://play.google.com/store/books/collection/cluster?gsr=ShlCFwoVChNUaGUgNyBNaW51dGUgUGhvbmU%3D",
        "color": "#6c3483",
        "accent": "#8e44ad",
        "isbn": "9780000000003",
        "publisher": "Independent",
        "chapters": [
            {"num": 1, "title": "Why the Phone Still Wins", "summary": "In a world drowning in digital communication, the phone call is the most direct and effective tool for moving deals forward. Understand why and when to pick up the phone."},
            {"num": 2, "title": "The 7 Minute Framework", "summary": "The core structure: Opening (60 seconds), Discovery (120 seconds), Value Bridge (90 seconds), Commitment (90 seconds), Close (60 seconds). Every second mapped and purposeful."},
            {"num": 3, "title": "Restarting Stalled Conversations", "summary": "Most deals do not die; they stall. Learn the specific techniques for re-engaging prospects who have gone quiet without being pushy or desperate."},
            {"num": 4, "title": "The Art of the Opening", "summary": "The first 60 seconds determine whether the rest of the call happens. Master the opening that earns attention and creates willingness to continue."},
            {"num": 5, "title": "Listening for the Real Objection", "summary": "Most objections are not real objections. Learn to hear what prospects are actually saying and address the underlying concern."},
            {"num": 6, "title": "Closing Without Pressure", "summary": "The close is not a trick or a technique. It is the natural conclusion of a well-structured conversation. Learn how to close with confidence and integrity."}
        ],
        "key_lessons": [
            "The phone call is still the fastest path from stalled deal to signed agreement",
            "Seven minutes is enough to restart any conversation if you have a clear structure",
            "The opening 60 seconds either earn you the rest of the call or lose it",
            "Listening is more important than talking on any sales call",
            "Most stalled deals can be revived with a single well-timed phone call",
            "Closing is not about pressure; it is about guiding a ready buyer to a decision"
        ],
        "who_should_read": {
            "audiences": [
                {"name": "Sales professionals", "reason": "who want a clear, repeatable framework for making effective phone calls that close deals"},
                {"name": "Entrepreneurs and founders", "reason": "who are doing their own sales and need a structured approach to phone outreach"},
                {"name": "Business development professionals", "reason": "who rely on phone-based prospecting and want to increase their conversion rate"},
                {"name": "Real estate agents and brokers", "reason": "who need to re-engage cold leads and move transactions forward"},
                {"name": "Anyone who dreads making phone calls", "reason": "and wants a framework that reduces anxiety and increases results"}
            ]
        },
        "review_quotes": [
            {"text": "Simple framework, massive results. I closed two deals the week I started using this.", "reviewer": "Amazon Reader"},
            {"text": "Robertson takes the fear out of cold calling and replaces it with a system.", "reviewer": "Yahoo Finance Feature"},
            {"text": "This book should be required reading for anyone in sales or business development.", "reviewer": "Verified Purchaser"}
        ]
    },
    {
        "slug": "built-to-run",
        "title": "Built to Run",
        "subtitle": "Building Business Systems That Work Without You",
        "description": "A guide to building business systems and operations that run without the founder. Learn how to create processes, delegate effectively, and build an organization that thrives independently.",
        "long_description": "Built to Run is the book for every founder who has built something successful but cannot step away from it. Dr. Connor Robertson shares the frameworks, systems, and mindset shifts required to transform an owner-dependent business into one that runs on its own. From documenting processes to hiring the right people to building a culture of accountability, this book provides a practical roadmap for the hardest transition in entrepreneurship: going from operator to owner.",
        "amazon_url": "https://www.amazon.com/s?k=Built+to+Run+Connor+Robertson",
        "bn_url": "https://www.barnesandnoble.com/s/Built+to+Run+Connor+Robertson",
        "google_play_url": "https://play.google.com/store/books/collection/cluster?gsr=ShZCFAoSChBCdWlsdCB0byBSdW4%3D",
        "color": "#7b241c",
        "accent": "#c0392b",
        "isbn": "9780000000004",
        "publisher": "Independent",
        "chapters": [
            {"num": 1, "title": "The Founder's Trap", "summary": "Why most businesses cannot survive without their founder, and why that is both the biggest risk and the biggest opportunity for growth."},
            {"num": 2, "title": "Documenting Everything", "summary": "Systems start with documentation. Learn how to capture the knowledge in your head and turn it into repeatable processes anyone can follow."},
            {"num": 3, "title": "Hiring for Systems, Not Skills", "summary": "The right hire is not always the most talented person. Learn how to hire people who thrive inside systems and make the whole organization stronger."},
            {"num": 4, "title": "Delegation That Actually Works", "summary": "Most founders fail at delegation because they do it wrong. This chapter provides a framework for delegating effectively without losing control of quality."},
            {"num": 5, "title": "Building a Culture of Accountability", "summary": "Systems only work if people follow them. Learn how to build a culture where accountability is baked in, not enforced from the top."},
            {"num": 6, "title": "Metrics That Matter", "summary": "You cannot manage what you do not measure. Identify the key performance indicators that tell you whether your systems are working."},
            {"num": 7, "title": "The Owner's Exit", "summary": "The ultimate test of a business built to run: can you step away? This chapter covers the transition from operator to owner and what comes next."}
        ],
        "key_lessons": [
            "If your business cannot run without you, you do not own a business; you own a job",
            "Documentation is the foundation of every scalable system",
            "Hiring for cultural fit and systems thinking matters more than raw talent",
            "Delegation is a skill that must be learned, practiced, and refined",
            "Accountability must be built into the culture, not imposed as a top-down mandate",
            "The right metrics give you visibility without requiring your constant presence",
            "The goal is not to work less; it is to build something that has value beyond your personal effort"
        ],
        "who_should_read": {
            "audiences": [
                {"name": "Founders and CEOs", "reason": "who feel trapped in the day-to-day operations of the business they built"},
                {"name": "Small business owners", "reason": "who want to build systems that allow them to step back without the business suffering"},
                {"name": "Managers and operations leaders", "reason": "who are responsible for creating repeatable processes and building high-performance teams"},
                {"name": "Entrepreneurs considering selling", "reason": "who know their business needs to run without them before it can be sold at a premium"},
                {"name": "Anyone building a team", "reason": "who wants a practical framework for delegation, documentation, and accountability"}
            ]
        },
        "review_quotes": [
            {"text": "I implemented three systems from this book and took my first real vacation in five years.", "reviewer": "Amazon Reader"},
            {"text": "Robertson understands the founder's dilemma and provides real solutions, not platitudes.", "reviewer": "Verified Purchaser"},
            {"text": "This book changed how I think about my role as a business owner.", "reviewer": "Google Play Review"}
        ]
    }
]

# ── Blog Post Data ─────────────────────────────────────────────────────────────

BLOG_POSTS = [
    {
        "slug": "5-lessons-from-buying-wealth",
        "title": "5 Lessons from Buying Wealth",
        "date": "2025-08-15",
        "related_book": "buying-wealth",
        "content": """
        <p>When I sat down to write <em>Buying Wealth</em>, I wanted to distill years of real-world experience into principles anyone could apply. Here are the five lessons that readers tell me changed their perspective the most.</p>

        <h2>1. Ownership Beats Income</h2>
        <p>The single most important shift I made in my financial life was moving from an income mindset to an ownership mindset. High income is great, but it does not compound. Assets do. When you own something that produces returns, you are building wealth while you sleep, while you work, and while you live your life. The chapter on the ownership mindset is where everything starts.</p>

        <h2>2. Leverage Is a Tool, Not a Four-Letter Word</h2>
        <p>Most people have been taught that debt is bad. But debt, used strategically, is the most powerful accelerator available to ordinary people. The key is understanding the difference between leverage that builds and leverage that destroys. In the book, I break down exactly how to evaluate whether leverage makes sense for any given acquisition.</p>

        <h2>3. Systems Beat Talent</h2>
        <p>I have seen brilliant people fail at wealth building because they relied on their own judgment for every decision. The investors who win consistently are the ones who build systems: repeatable frameworks for sourcing, evaluating, and closing deals. Chapter 4 of Buying Wealth is the most dog-eared chapter in the book for a reason.</p>

        <h2>4. Due Diligence Is Non-Negotiable</h2>
        <p>Every bad deal I have ever seen could have been avoided with better due diligence. It is not glamorous, it is not exciting, but it is the single most important step in any acquisition. The framework I provide in Chapter 5 has saved readers from costly mistakes.</p>

        <h2>5. Start Before You Are Ready</h2>
        <p>The last lesson is the simplest and the hardest. There will never be a perfect time to buy your first asset. The market will never be perfectly priced. You will never feel 100% ready. The people who build wealth are the ones who start anyway, armed with a framework and a willingness to learn.</p>

        <p>If these ideas resonate, <a href="/books/buying-wealth/">pick up a copy of Buying Wealth</a> and start building your ownership portfolio today.</p>
        """
    },
    {
        "slug": "why-i-wrote-creative-acquisitions",
        "title": "Why I Wrote Creative Acquisitions",
        "date": "2025-09-10",
        "related_book": "creative-acquisitions",
        "content": """
        <p>The idea for <em>Creative Acquisitions</em> came from a conversation I had with an entrepreneur who wanted to buy a small manufacturing business. He had the skills, the vision, and the drive. What he did not have was $2 million in cash. The traditional advice was simple: go raise the money or do not bother. I thought there had to be a better answer.</p>

        <h2>The Gap in the Market</h2>
        <p>Most books about business acquisitions are written for private equity professionals or people with significant capital. They assume you have a fund, a lending relationship, or deep pockets. But the reality is that most small business acquisitions happen between ordinary people, and the deals that get done are often the ones structured creatively.</p>

        <h2>Real Deals, Real Structures</h2>
        <p>Every strategy in Creative Acquisitions comes from real transactions. Seller financing, earn-outs, partnership structures, assumption deals. These are not theoretical concepts. They are tools I have used and seen used in actual closings. The book walks through each structure with enough detail that you could bring it to your next negotiation.</p>

        <h2>Why It Matters Now</h2>
        <p>We are in the middle of the largest generational wealth transfer in history. Baby boomers own millions of small businesses, and many of them want to sell but cannot find buyers who can pay full price at closing. Creative structures are not just nice to have; they are essential for keeping these businesses alive and in good hands.</p>

        <p>If you have ever wanted to own a business but felt the price tag was out of reach, <a href="/books/creative-acquisitions/">Creative Acquisitions</a> was written for you.</p>
        """
    },
    {
        "slug": "the-story-behind-the-7-minute-phone-call",
        "title": "The Story Behind The 7 Minute Phone Call",
        "date": "2025-10-05",
        "related_book": "the-7-minute-phone-call",
        "content": """
        <p>People always ask me where the seven-minute idea came from. The truth is, it started with a timer and a notebook.</p>

        <h2>The Experiment</h2>
        <p>Early in my career, I tracked every sales call I made for three months. Time, outcome, structure, notes. What I found surprised me: the calls that closed deals were almost never the longest ones. In fact, the sweet spot was consistently between five and eight minutes. Long enough to be substantive, short enough to stay focused. Seven minutes became my target.</p>

        <h2>Structure Removes Fear</h2>
        <p>The other insight was that structure eliminates most of the anxiety people feel about phone calls. When you know exactly what you are going to say in the first 60 seconds, and you have a clear path through discovery, value, and close, the call stops being scary and starts being a repeatable process. That is what the framework provides.</p>

        <h2>Stalled Deals Are Sleeping, Not Dead</h2>
        <p>Perhaps the most important lesson from the book is that most stalled deals are not dead. They are just waiting for someone to pick up the phone. A well-structured seven-minute call can restart a conversation that has been cold for weeks or months. I have seen it happen hundreds of times.</p>

        <p>If you have deals sitting in your pipeline that have gone quiet, <a href="/books/the-7-minute-phone-call/">The 7 Minute Phone Call</a> will give you the framework to bring them back to life.</p>
        """
    },
    {
        "slug": "how-built-to-run-changed-my-approach",
        "title": "How Built to Run Changed My Approach to Business",
        "date": "2025-11-12",
        "related_book": "built-to-run",
        "content": """
        <p>Writing <em>Built to Run</em> changed how I operate my own businesses. That might sound strange for an author, but the process of codifying these ideas forced me to confront where I was still the bottleneck.</p>

        <h2>The Honest Assessment</h2>
        <p>Before writing this book, I would have told you my businesses were well-systemized. Then I started cataloging every process, every decision point, every place where someone needed my input to move forward. The list was humbling. I was more embedded in the day-to-day than I wanted to admit.</p>

        <h2>Documentation Changed Everything</h2>
        <p>The single biggest impact came from the documentation framework in Chapter 2. When you write down how things actually work (not how you think they work), you discover redundancies, bottlenecks, and opportunities for automation that were invisible before. My team started solving problems without me because the playbook was finally written down.</p>

        <h2>The Real Freedom</h2>
        <p>Building a business that runs without you is not about working less, although that is a nice side effect. It is about building something with genuine enterprise value. A business that depends on its founder is worth less than one that runs on systems. Built to Run is ultimately about creating something that has value beyond your personal effort.</p>

        <p>If you are a founder who feels chained to your business, <a href="/books/built-to-run/">Built to Run</a> is the roadmap to freedom.</p>
        """
    },
    {
        "slug": "biggest-mistake-buying-a-business",
        "title": "The Biggest Mistake Entrepreneurs Make When Buying a Business",
        "date": "2025-12-01",
        "related_book": "creative-acquisitions",
        "content": """
        <p>After years of advising on business acquisitions, I can tell you the single biggest mistake entrepreneurs make: they fall in love with the deal before they fall in love with the numbers.</p>

        <h2>Emotional Attachment Kills Deals</h2>
        <p>I get it. You find a business that seems perfect. It is in your industry, the owner is ready to sell, the story is compelling. You start imagining yourself as the new owner. And that is exactly when your judgment starts to slip. Emotional attachment leads to overlooking red flags, accepting inflated valuations, and rushing through due diligence.</p>

        <h2>The Antidote: A Systematic Framework</h2>
        <p>In <em>Creative Acquisitions</em>, I walk through a due diligence framework specifically designed to counter emotional bias. It starts with the numbers and works outward. Revenue quality, customer concentration, owner dependency, market trends. By the time you get to the qualitative factors, you already have a clear-eyed view of what the business is actually worth.</p>

        <h2>Walk Away Power</h2>
        <p>The most important skill in acquisitions is the willingness to walk away. Every great deal I have ever done was preceded by deals I walked away from. The framework gives you the confidence to say no when the numbers do not work, regardless of how good the story sounds.</p>

        <p>Learn how to evaluate deals without emotional bias in <a href="/books/creative-acquisitions/">Creative Acquisitions</a>.</p>
        """
    },
    {
        "slug": "every-deal-starts-with-a-phone-call",
        "title": "Why Every Deal Starts with a Phone Call",
        "date": "2026-01-15",
        "related_book": "the-7-minute-phone-call",
        "content": """
        <p>In 2026, we have more communication tools than ever. Email, Slack, LinkedIn messages, CRM sequences, automated outreach. And yet, the deals that actually close almost always involve a phone call at some critical moment.</p>

        <h2>The Phone Call Advantage</h2>
        <p>A phone call does something no other medium can: it creates real-time human connection. You hear tone, pace, hesitation, enthusiasm. You can adapt in the moment. You can ask a follow-up question and get an immediate answer. In a seven-minute phone call, you can accomplish what takes a week of email back-and-forth.</p>

        <h2>When to Pick Up the Phone</h2>
        <p>Not every interaction requires a call. But there are specific moments where the phone is the right tool: when a deal has stalled, when you need to deliver a complex message, when you sense hesitation in a prospect, or when you need a decision. The framework in <em>The 7 Minute Phone Call</em> is designed for exactly these moments.</p>

        <h2>The Compound Effect</h2>
        <p>Here is what most people miss: the compound effect of consistent phone outreach is enormous. Make five structured calls a day, five days a week, and in a month you have had 100 real conversations. That is a pipeline most businesses would envy, built on the simplest tool available.</p>

        <p>Learn the framework that makes every call count in <a href="/books/the-7-minute-phone-call/">The 7 Minute Phone Call</a>.</p>
        """
    },
    {
        "slug": "building-wealth-through-ownership",
        "title": "Building Wealth Through Ownership, Not Income",
        "date": "2026-02-20",
        "related_book": "buying-wealth",
        "content": """
        <p>The highest-paid employee in the room is almost never the wealthiest person in the room. That distinction almost always belongs to the person who owns things. This is the central insight of <em>Buying Wealth</em>, and it bears repeating.</p>

        <h2>The Income Trap</h2>
        <p>Our entire financial education system is built around income. Get good grades, get a good job, get a good salary. But income is linear. You trade hours for dollars. When you stop working, the income stops. No matter how high your salary, you are on a treadmill unless you are converting that income into ownership.</p>

        <h2>What Ownership Looks Like</h2>
        <p>Ownership takes many forms: real estate, business equity, intellectual property, cash-flowing assets. The common thread is that these things produce returns whether or not you are actively working on them. A rental property generates income. A business with good systems generates profit. A book generates royalties. Ownership compounds in ways that income cannot.</p>

        <h2>The Transition</h2>
        <p>The hardest part of the ownership mindset is the transition. It requires spending less than you earn, redirecting the surplus into assets, and having the patience to let compounding do its work. It is not glamorous. It is not fast. But it is the only reliable path to wealth that I have ever found.</p>

        <p>Start your ownership journey with the frameworks in <a href="/books/buying-wealth/">Buying Wealth</a>.</p>
        """
    },
    {
        "slug": "run-a-business-that-doesnt-need-you",
        "title": "How to Run a Business That Does Not Need You",
        "date": "2026-03-10",
        "related_book": "built-to-run",
        "content": """
        <p>The title of <em>Built to Run</em> contains a paradox that most founders struggle with: if the business does not need you, what is your role? The answer is that your role becomes the most important one: architect, not operator.</p>

        <h2>Operator vs. Architect</h2>
        <p>An operator solves problems. An architect builds systems that prevent problems. An operator makes decisions. An architect creates frameworks that enable others to make good decisions. The transition from operator to architect is the central challenge of growing any business beyond its founder.</p>

        <h2>The Three Systems Every Business Needs</h2>
        <p>In my experience, every business that runs without its founder has three things in place: documented processes (so anyone can execute), clear metrics (so anyone can measure), and a culture of accountability (so anyone can be held to a standard). Miss any one of these and the founder gets pulled back in.</p>

        <h2>The Litmus Test</h2>
        <p>Here is a simple test: can you take a two-week vacation without checking your phone? If yes, your business is built to run. If no, you have work to do. The good news is that the work is straightforward, even if it is not easy. It starts with documentation, moves through delegation, and ends with a business that has real value independent of your daily involvement.</p>

        <p>Get the complete framework in <a href="/books/built-to-run/">Built to Run</a>.</p>
        """
    }
]

# ── Social / Cross-linking Data ────────────────────────────────────────────────

SOCIAL_PROFILES = [
    {"name": "LinkedIn", "url": "https://www.linkedin.com/in/drconnorrobertson/"},
    {"name": "Twitter/X", "url": "https://x.com/DrConnorR"},
    {"name": "Instagram", "url": "https://www.instagram.com/drconnorrobertson/"},
    {"name": "Facebook", "url": "https://facebook.com/therealconnorrobertson"},
    {"name": "YouTube", "url": "https://www.youtube.com/@drconnorrobertson"},
    {"name": "TikTok", "url": "https://www.tiktok.com/@drconnorrobertson"},
    {"name": "Medium", "url": "https://medium.com/@drconnorrobertson"},
    {"name": "Threads", "url": "https://www.threads.net/@drconnorrobertson"},
    {"name": "Substack", "url": "https://drconnorrobertson.substack.com"},
    {"name": "Spotify", "url": "https://open.spotify.com/show/drconnorrobertson"},
    {"name": "Apple Podcasts", "url": "https://podcasts.apple.com/us/podcast/drconnorrobertson"},
    {"name": "Google Scholar", "url": "https://scholar.google.com/citations?user=drconnorrobertson"},
    {"name": "Amazon Author", "url": "https://www.amazon.com/stores/Dr-Connor-Robertson/author/"},
    {"name": "Goodreads", "url": "https://www.goodreads.com/author/show/drconnorrobertson"},
    {"name": "Google Play Books", "url": "https://play.google.com/store/books/author?id=Connor+Robertson"},
    {"name": "Apple Books", "url": "https://books.apple.com/us/author/connor-robertson"},
    {"name": "Barnes & Noble", "url": "https://www.barnesandnoble.com/s/Connor+Robertson"}
]

WEBSITES = [
    {"name": "DrConnorRobertson.com", "url": "https://drconnorrobertson.com"},
    {"name": "Elixir Consulting Group", "url": "https://elixirconsultinggroup.com"},
    {"name": "The Pittsburgh Wire", "url": "https://thepittsburghwire.com"},
    {"name": "The Prospecting Show", "url": "https://prospectingshow.com"},
    {"name": "The Grant Finder", "url": "https://thegrantfinder.org"}
]

SAME_AS = [p["url"] for p in SOCIAL_PROFILES] + [w["url"] for w in WEBSITES]

# ── HTML Templates ─────────────────────────────────────────────────────────────

def css():
    return """
:root {
    --primary: #1a1a2e;
    --secondary: #16213e;
    --accent: #0f3460;
    --gold: #c9a227;
    --text: #333;
    --text-light: #666;
    --bg: #fff;
    --bg-light: #f8f9fa;
    --border: #e0e0e0;
    --max-width: 1200px;
}

* { margin: 0; padding: 0; box-sizing: border-box; }

body {
    font-family: 'Georgia', 'Times New Roman', serif;
    color: var(--text);
    background: var(--bg);
    line-height: 1.7;
}

a { color: var(--accent); text-decoration: none; }
a:hover { color: var(--gold); }

img { max-width: 100%; height: auto; }

/* Header */
.site-header {
    background: var(--primary);
    color: #fff;
    padding: 0;
    position: sticky;
    top: 0;
    z-index: 100;
    box-shadow: 0 2px 10px rgba(0,0,0,0.3);
}

.header-inner {
    max-width: var(--max-width);
    margin: 0 auto;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 20px;
    height: 70px;
}

.site-logo {
    font-family: 'Georgia', serif;
    font-size: 1.3rem;
    font-weight: bold;
    color: #fff;
    letter-spacing: 0.5px;
}

.site-logo span { color: var(--gold); }

.main-nav { display: flex; gap: 30px; align-items: center; }
.main-nav a {
    color: #ccc;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    font-size: 0.9rem;
    text-transform: uppercase;
    letter-spacing: 1px;
    transition: color 0.3s;
}
.main-nav a:hover, .main-nav a.active { color: var(--gold); }

.mobile-menu-btn {
    display: none;
    background: none;
    border: none;
    color: #fff;
    font-size: 1.5rem;
    cursor: pointer;
}

/* Hero */
.hero {
    background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 50%, var(--accent) 100%);
    color: #fff;
    padding: 80px 20px;
    text-align: center;
}

.hero h1 {
    font-size: 3rem;
    margin-bottom: 15px;
    font-weight: 400;
    letter-spacing: 1px;
}

.hero h1 span { color: var(--gold); }

.hero p {
    font-size: 1.2rem;
    max-width: 700px;
    margin: 0 auto 30px;
    opacity: 0.9;
    line-height: 1.6;
}

.hero-cta {
    display: inline-block;
    background: var(--gold);
    color: var(--primary);
    padding: 14px 35px;
    font-size: 1rem;
    font-weight: bold;
    text-transform: uppercase;
    letter-spacing: 1px;
    border-radius: 3px;
    transition: background 0.3s;
}

.hero-cta:hover { background: #d4af37; color: var(--primary); }

/* Container */
.container { max-width: var(--max-width); margin: 0 auto; padding: 0 20px; }

/* Book Grid */
.books-section { padding: 80px 20px; background: var(--bg-light); }
.books-section h2 {
    text-align: center;
    font-size: 2.2rem;
    margin-bottom: 50px;
    color: var(--primary);
    font-weight: 400;
}

.books-grid {
    max-width: var(--max-width);
    margin: 0 auto;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 40px;
}

.book-card {
    background: #fff;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 4px 20px rgba(0,0,0,0.08);
    transition: transform 0.3s, box-shadow 0.3s;
}

.book-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 30px rgba(0,0,0,0.15);
}

.book-cover {
    height: 320px;
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
    overflow: hidden;
}

.book-cover-inner {
    width: 180px;
    height: 260px;
    border-radius: 4px;
    box-shadow: 5px 5px 20px rgba(0,0,0,0.3);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 20px;
    text-align: center;
    color: #fff;
    position: relative;
}

.book-cover-inner::before {
    content: '';
    position: absolute;
    left: 0;
    top: 0;
    bottom: 0;
    width: 12px;
    background: rgba(0,0,0,0.2);
    border-radius: 4px 0 0 4px;
}

.book-cover-inner h3 {
    font-size: 1.2rem;
    margin-bottom: 10px;
    line-height: 1.3;
    font-weight: 700;
}

.book-cover-inner .cover-author {
    font-size: 0.75rem;
    opacity: 0.85;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
}

.book-cover-inner .cover-line {
    width: 40px;
    height: 2px;
    background: rgba(255,255,255,0.5);
    margin: 12px 0;
}

.book-card-body { padding: 25px; }
.book-card-body h3 { font-size: 1.3rem; margin-bottom: 8px; color: var(--primary); }
.book-card-body .book-subtitle { font-size: 0.9rem; color: var(--text-light); margin-bottom: 12px; font-style: italic; }
.book-card-body p { font-size: 0.95rem; color: var(--text-light); margin-bottom: 15px; }

.book-links { display: flex; gap: 10px; flex-wrap: wrap; }
.book-links a {
    font-size: 0.8rem;
    padding: 6px 14px;
    border: 1px solid var(--border);
    border-radius: 3px;
    color: var(--text);
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    transition: all 0.3s;
}
.book-links a:hover { border-color: var(--gold); color: var(--gold); }

/* Author Section */
.author-section {
    padding: 80px 20px;
    background: #fff;
}

.author-inner {
    max-width: var(--max-width);
    margin: 0 auto;
    display: grid;
    grid-template-columns: 300px 1fr;
    gap: 50px;
    align-items: start;
}

.author-photo-placeholder {
    width: 300px;
    height: 380px;
    background: linear-gradient(135deg, var(--primary), var(--accent));
    border-radius: 8px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    color: #fff;
    font-size: 4rem;
    box-shadow: 0 4px 20px rgba(0,0,0,0.15);
}

.author-photo-placeholder span {
    font-size: 0.9rem;
    margin-top: 15px;
    opacity: 0.8;
    text-transform: uppercase;
    letter-spacing: 2px;
}

.author-bio h2 {
    font-size: 2rem;
    color: var(--primary);
    margin-bottom: 20px;
    font-weight: 400;
}

.author-bio p { margin-bottom: 15px; color: var(--text-light); }

.author-links {
    margin-top: 25px;
    display: flex;
    gap: 12px;
    flex-wrap: wrap;
}

.author-links a {
    font-size: 0.85rem;
    padding: 8px 18px;
    background: var(--bg-light);
    border-radius: 3px;
    color: var(--text);
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    transition: all 0.3s;
}

.author-links a:hover { background: var(--gold); color: #fff; }

/* Blog Section */
.blog-section { padding: 80px 20px; background: var(--bg-light); }
.blog-section h2 {
    text-align: center;
    font-size: 2.2rem;
    margin-bottom: 50px;
    color: var(--primary);
    font-weight: 400;
}

.blog-grid {
    max-width: var(--max-width);
    margin: 0 auto;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    gap: 30px;
}

.blog-card {
    background: #fff;
    padding: 30px;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    transition: transform 0.3s;
}

.blog-card:hover { transform: translateY(-3px); }
.blog-card .blog-date {
    font-size: 0.8rem;
    color: var(--gold);
    text-transform: uppercase;
    letter-spacing: 1px;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    margin-bottom: 10px;
}
.blog-card h3 { font-size: 1.2rem; margin-bottom: 10px; }
.blog-card h3 a { color: var(--primary); }
.blog-card h3 a:hover { color: var(--gold); }

/* Page Content */
.page-hero {
    padding: 60px 20px;
    text-align: center;
    color: #fff;
}

.page-hero h1 {
    font-size: 2.5rem;
    margin-bottom: 10px;
    font-weight: 400;
}

.page-hero p {
    font-size: 1.1rem;
    opacity: 0.9;
    max-width: 600px;
    margin: 0 auto;
}

.breadcrumb {
    max-width: var(--max-width);
    margin: 0 auto;
    padding: 15px 20px;
    font-size: 0.85rem;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    color: var(--text-light);
}

.breadcrumb a { color: var(--text-light); }
.breadcrumb a:hover { color: var(--gold); }
.breadcrumb span { margin: 0 8px; }

.page-content {
    max-width: 800px;
    margin: 0 auto;
    padding: 50px 20px 80px;
}

.page-content h2 {
    font-size: 1.6rem;
    color: var(--primary);
    margin: 35px 0 15px;
    font-weight: 400;
}

.page-content h3 {
    font-size: 1.3rem;
    color: var(--primary);
    margin: 25px 0 12px;
}

.page-content p { margin-bottom: 15px; }

.page-content ul, .page-content ol {
    margin: 15px 0 15px 25px;
}

.page-content li { margin-bottom: 8px; }

.page-content blockquote {
    border-left: 3px solid var(--gold);
    padding: 15px 20px;
    margin: 25px 0;
    background: var(--bg-light);
    font-style: italic;
    color: var(--text-light);
}

/* Book Detail Page */
.book-detail-hero {
    padding: 60px 20px;
    color: #fff;
}

.book-detail-inner {
    max-width: var(--max-width);
    margin: 0 auto;
    display: grid;
    grid-template-columns: 220px 1fr;
    gap: 50px;
    align-items: center;
}

.book-detail-cover {
    width: 220px;
    height: 320px;
    border-radius: 6px;
    box-shadow: 8px 8px 30px rgba(0,0,0,0.4);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 25px;
    text-align: center;
    color: #fff;
    position: relative;
}

.book-detail-cover::before {
    content: '';
    position: absolute;
    left: 0;
    top: 0;
    bottom: 0;
    width: 15px;
    background: rgba(0,0,0,0.2);
    border-radius: 6px 0 0 6px;
}

.book-detail-cover h2 {
    font-size: 1.5rem;
    line-height: 1.3;
    margin-bottom: 12px;
}

.book-detail-cover .cover-line {
    width: 40px;
    height: 2px;
    background: rgba(255,255,255,0.5);
    margin: 10px 0;
}

.book-detail-cover .cover-author {
    font-size: 0.8rem;
    text-transform: uppercase;
    letter-spacing: 2px;
    opacity: 0.85;
}

.book-detail-info h1 {
    font-size: 2.5rem;
    margin-bottom: 8px;
    font-weight: 400;
}

.book-detail-info .subtitle {
    font-size: 1.2rem;
    opacity: 0.85;
    font-style: italic;
    margin-bottom: 20px;
}

.book-detail-info p {
    font-size: 1.05rem;
    line-height: 1.7;
    opacity: 0.9;
    margin-bottom: 25px;
}

.buy-buttons { display: flex; gap: 12px; flex-wrap: wrap; }
.buy-btn {
    display: inline-block;
    padding: 12px 28px;
    border: 2px solid #fff;
    color: #fff;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    font-size: 0.9rem;
    text-transform: uppercase;
    letter-spacing: 1px;
    border-radius: 3px;
    transition: all 0.3s;
}
.buy-btn:hover { background: #fff; color: var(--primary); }
.buy-btn.primary-btn { background: var(--gold); border-color: var(--gold); color: var(--primary); }
.buy-btn.primary-btn:hover { background: #d4af37; border-color: #d4af37; }

/* Reviews */
.reviews { margin: 40px 0; }
.review {
    background: var(--bg-light);
    padding: 20px 25px;
    border-radius: 6px;
    margin-bottom: 15px;
    border-left: 3px solid var(--gold);
}
.review p { font-style: italic; margin-bottom: 8px; }
.review .reviewer { font-size: 0.85rem; color: var(--text-light); font-style: normal; }

/* Chapter List */
.chapter-list { margin: 30px 0; }
.chapter-item {
    display: block;
    padding: 20px 25px;
    background: var(--bg-light);
    border-radius: 6px;
    margin-bottom: 10px;
    transition: all 0.3s;
    border-left: 3px solid transparent;
}
.chapter-item:hover { border-left-color: var(--gold); background: #fff; box-shadow: 0 2px 10px rgba(0,0,0,0.05); }
.chapter-item .chapter-num {
    font-size: 0.8rem;
    color: var(--gold);
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 5px;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
}
.chapter-item h3 { font-size: 1.1rem; color: var(--primary); margin-bottom: 5px; }
.chapter-item p { font-size: 0.9rem; color: var(--text-light); }

/* Sidebar / TOC */
.content-with-sidebar {
    max-width: var(--max-width);
    margin: 0 auto;
    display: grid;
    grid-template-columns: 280px 1fr;
    gap: 40px;
    padding: 40px 20px 80px;
}

.sidebar {
    position: sticky;
    top: 90px;
    align-self: start;
}

.sidebar h3 {
    font-size: 0.85rem;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    color: var(--text-light);
    margin-bottom: 15px;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
}

.sidebar a {
    display: block;
    padding: 8px 12px;
    font-size: 0.9rem;
    color: var(--text-light);
    border-left: 2px solid var(--border);
    margin-bottom: 2px;
    transition: all 0.3s;
}

.sidebar a:hover, .sidebar a.active {
    color: var(--gold);
    border-left-color: var(--gold);
    background: var(--bg-light);
}

/* Footer */
.site-footer {
    background: var(--primary);
    color: #aaa;
    padding: 60px 20px 30px;
}

.footer-inner {
    max-width: var(--max-width);
    margin: 0 auto;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 40px;
}

.footer-col h4 {
    color: #fff;
    font-size: 0.85rem;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    margin-bottom: 15px;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
}

.footer-col a {
    display: block;
    color: #888;
    font-size: 0.9rem;
    margin-bottom: 8px;
    transition: color 0.3s;
}

.footer-col a:hover { color: var(--gold); }

.footer-bottom {
    max-width: var(--max-width);
    margin: 40px auto 0;
    padding-top: 20px;
    border-top: 1px solid #333;
    text-align: center;
    font-size: 0.8rem;
    color: #666;
}

/* Responsive */
@media (max-width: 768px) {
    .header-inner { height: 60px; }
    .main-nav { display: none; }
    .mobile-menu-btn { display: block; }
    .hero h1 { font-size: 2rem; }
    .hero p { font-size: 1rem; }
    .author-inner { grid-template-columns: 1fr; }
    .author-photo-placeholder { width: 200px; height: 250px; margin: 0 auto; }
    .book-detail-inner { grid-template-columns: 1fr; text-align: center; }
    .book-detail-cover { margin: 0 auto; }
    .buy-buttons { justify-content: center; }
    .content-with-sidebar { grid-template-columns: 1fr; }
    .sidebar { position: static; }
    .blog-grid { grid-template-columns: 1fr; }
    .books-grid { grid-template-columns: 1fr; }
    .page-hero h1 { font-size: 1.8rem; }
}

@media (max-width: 480px) {
    .hero h1 { font-size: 1.5rem; }
    .book-cover { height: 260px; }
    .book-cover-inner { width: 140px; height: 200px; }
}
"""


def header(active=""):
    return f"""<header class="site-header">
    <div class="header-inner">
        <a href="/" class="site-logo">Dr. Connor <span>Robertson</span></a>
        <nav class="main-nav">
            <a href="/" {"class='active'" if active == "home" else ""}>Home</a>
            <a href="/books/buying-wealth/" {"class='active'" if active == "buying-wealth" else ""}>Buying Wealth</a>
            <a href="/books/creative-acquisitions/" {"class='active'" if active == "creative-acquisitions" else ""}>Creative Acquisitions</a>
            <a href="/books/the-7-minute-phone-call/" {"class='active'" if active == "the-7-minute-phone-call" else ""}>7 Minute Phone Call</a>
            <a href="/books/built-to-run/" {"class='active'" if active == "built-to-run" else ""}>Built to Run</a>
            <a href="/about" {"class='active'" if active == "about" else ""}>About</a>
            <a href="/blog/" {"class='active'" if active == "blog" else ""}>Blog</a>
        </nav>
        <button class="mobile-menu-btn" onclick="document.querySelector('.main-nav').style.display=document.querySelector('.main-nav').style.display==='flex'?'none':'flex'" aria-label="Menu">&#9776;</button>
    </div>
</header>"""


def footer():
    book_links = "".join(f'<a href="/books/{b["slug"]}/">{b["title"]}</a>' for b in BOOKS)
    blog_links = "".join(f'<a href="/blog/{p["slug"]}/">{p["title"]}</a>' for p in BLOG_POSTS[:4])
    website_links = "".join(f'<a href="{w["url"]}" target="_blank" rel="noopener">{w["name"]}</a>' for w in WEBSITES)
    social_links = "".join(f'<a href="{s["url"]}" target="_blank" rel="noopener">{s["name"]}</a>' for s in SOCIAL_PROFILES[:6])

    return f"""<footer class="site-footer">
    <div class="footer-inner">
        <div class="footer-col">
            <h4>Books</h4>
            {book_links}
        </div>
        <div class="footer-col">
            <h4>Blog</h4>
            {blog_links}
        </div>
        <div class="footer-col">
            <h4>Websites</h4>
            {website_links}
        </div>
        <div class="footer-col">
            <h4>Connect</h4>
            {social_links}
        </div>
    </div>
    <div class="footer-bottom">
        &copy; {datetime.now().year} Dr. Connor Robertson. All rights reserved.
    </div>
</footer>"""


def breadcrumb_html(items):
    """items: list of (label, url) tuples. Last item has no link."""
    parts = []
    for i, (label, url) in enumerate(items):
        if i == len(items) - 1:
            parts.append(f'{label}')
        else:
            parts.append(f'<a href="{url}">{label}</a>')
    return '<div class="breadcrumb">' + ' <span>/</span> '.join(parts) + '</div>'


def breadcrumb_schema(items):
    """items: list of (label, url) tuples."""
    list_items = []
    for i, (label, url) in enumerate(items):
        list_items.append({
            "@type": "ListItem",
            "position": i + 1,
            "name": label,
            "item": f"{SITE_URL}{url}" if not url.startswith("http") else url
        })
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": list_items
    }


def book_schema(book):
    return {
        "@context": "https://schema.org",
        "@type": "Book",
        "name": book["title"],
        "description": book["description"],
        "author": {
            "@type": "Person",
            "name": AUTHOR_NAME,
            "url": f"{SITE_URL}/about"
        },
        "publisher": {
            "@type": "Organization",
            "name": book["publisher"]
        },
        "isbn": book["isbn"],
        "bookFormat": "https://schema.org/EBook",
        "url": f"{SITE_URL}/books/{book['slug']}/",
        "image": f"{SITE_URL}/images/{book['slug']}-cover.png"
    }


def person_schema():
    return {
        "@context": "https://schema.org",
        "@type": "Person",
        "name": AUTHOR_NAME,
        "url": f"{SITE_URL}/about",
        "jobTitle": "Author, Entrepreneur, Tax Strategist",
        "description": "Dr. Connor Robertson is an author, entrepreneur, and strategic advisor specializing in acquisitions, tax strategy, and business systems.",
        "sameAs": SAME_AS,
        "image": f"{SITE_URL}/images/connor-robertson.png"
    }


def blog_schema(post):
    return {
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": post["title"],
        "datePublished": post["date"],
        "dateModified": post["date"],
        "author": {
            "@type": "Person",
            "name": AUTHOR_NAME,
            "url": f"{SITE_URL}/about"
        },
        "publisher": {
            "@type": "Person",
            "name": AUTHOR_NAME
        },
        "url": f"{SITE_URL}/blog/{post['slug']}/",
        "mainEntityOfPage": f"{SITE_URL}/blog/{post['slug']}/"
    }


def head(title, description, url, schemas=None, og_image=None):
    canonical = f"{SITE_URL}{url}"
    if og_image is None:
        og_image = f"{SITE_URL}/images/og-default.png"
    schema_tags = ""
    if schemas:
        for s in schemas:
            schema_tags += f'\n    <script type="application/ld+json">{json.dumps(s, indent=2)}</script>'
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{description}">
    <link rel="canonical" href="{canonical}">

    <!-- Open Graph -->
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description}">
    <meta property="og:url" content="{canonical}">
    <meta property="og:image" content="{og_image}">
    <meta property="og:type" content="website">
    <meta property="og:site_name" content="Dr. Connor Robertson - Author">

    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{title}">
    <meta name="twitter:description" content="{description}">
    <meta name="twitter:image" content="{og_image}">

    <link rel="stylesheet" href="/css/style.css">
    {schema_tags}
</head>
<body>"""


def page_end():
    return """</body>
</html>"""


def book_sidebar(book, active_page=""):
    slug = book["slug"]
    title = book["title"]
    cls_landing = "class='active'" if active_page == "landing" else ""
    links = f'<a href="/books/{slug}/" {cls_landing}>Overview</a>\n'
    for ch in book["chapters"]:
        ch_num = ch["num"]
        ch_title = ch["title"]
        cls_ch = "class='active'" if active_page == f"ch{ch_num}" else ""
        links += f'<a href="/books/{slug}/chapters/{ch_num}/" {cls_ch}>Ch. {ch_num}: {ch_title}</a>\n'
    cls_lessons = "class='active'" if active_page == "lessons" else ""
    cls_who = "class='active'" if active_page == "who" else ""
    cls_blog = "class='active'" if active_page == "blog" else ""
    links += f'<a href="/books/{slug}/key-lessons/" {cls_lessons}>Key Lessons</a>\n'
    links += f'<a href="/books/{slug}/who-should-read/" {cls_who}>Who Should Read</a>\n'
    links += f'<a href="/blog/{slug}-blog/" {cls_blog}>Related Post</a>\n'

    return f"""<aside class="sidebar">
    <h3>{title}</h3>
    {links}
</aside>"""


# ── Page Generators ────────────────────────────────────────────────────────────

def write_file(rel_path, content):
    path = os.path.join(OUTPUT_DIR, rel_path)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(content)
    return rel_path


def generate_homepage():
    book_cards = ""
    for b in BOOKS:
        book_cards += f"""
        <div class="book-card">
            <div class="book-cover" style="background: {b['color']}15;">
                <div class="book-cover-inner" style="background: linear-gradient(160deg, {b['color']}, {b['accent']});">
                    <h3>{b['title']}</h3>
                    <div class="cover-line"></div>
                    <div class="cover-author">Dr. Connor Robertson</div>
                </div>
            </div>
            <div class="book-card-body">
                <h3><a href="/books/{b['slug']}/">{b['title']}</a></h3>
                <div class="book-subtitle">{b['subtitle']}</div>
                <p>{b['description'][:150]}...</p>
                <div class="book-links">
                    <a href="/books/{b['slug']}/">Learn More</a>
                    <a href="{b['amazon_url']}" target="_blank" rel="noopener">Amazon</a>
                    <a href="{b['bn_url']}" target="_blank" rel="noopener">Barnes &amp; Noble</a>
                    <a href="{b['google_play_url']}" target="_blank" rel="noopener">Google Play</a>
                </div>
            </div>
        </div>"""

    blog_cards = ""
    for p in BLOG_POSTS[:4]:
        blog_cards += f"""
        <div class="blog-card">
            <div class="blog-date">{datetime.strptime(p['date'], '%Y-%m-%d').strftime('%B %d, %Y')}</div>
            <h3><a href="/blog/{p['slug']}/">{p['title']}</a></h3>
        </div>"""

    schemas = [
        {
            "@context": "https://schema.org",
            "@type": "WebSite",
            "name": "Dr. Connor Robertson - Author",
            "url": SITE_URL,
            "author": {"@type": "Person", "name": AUTHOR_NAME}
        },
        person_schema(),
        breadcrumb_schema([("Home", "/")])
    ]

    content = head(
        "Dr. Connor Robertson - Author | Buying Wealth, Creative Acquisitions, The 7 Minute Phone Call, Built to Run",
        "Official book hub for Dr. Connor Robertson. Explore Buying Wealth, Creative Acquisitions, The 7 Minute Phone Call, and Built to Run.",
        "/",
        schemas
    )
    content += header("home")
    content += f"""
<section class="hero">
    <h1>Books by <span>Dr. Connor Robertson</span></h1>
    <p>Practical frameworks for building wealth through ownership, acquiring businesses creatively, closing deals with confidence, and building organizations that run without you.</p>
    <a href="#books" class="hero-cta">Explore the Books</a>
</section>

<section class="books-section" id="books">
    <h2>The Collection</h2>
    <div class="books-grid">{book_cards}</div>
</section>

<section class="author-section">
    <div class="author-inner">
        <div class="author-photo-placeholder">
            CR
            <span>Author</span>
        </div>
        <div class="author-bio">
            <h2>About Dr. Connor Robertson</h2>
            <p>Dr. Connor Robertson is an entrepreneur, author, and strategic advisor whose work sits at the intersection of acquisitions, tax strategy, and business systems. His books have helped thousands of readers rethink how they build wealth, structure deals, and run their organizations.</p>
            <p>Through <a href="https://elixirconsultinggroup.com" target="_blank" rel="noopener">Elixir Consulting Group</a>, Connor advises business owners on growth, acquisition strategy, and operational excellence. He is the host of <a href="https://prospectingshow.com" target="_blank" rel="noopener">The Prospecting Show</a> and founder of <a href="https://thepittsburghwire.com" target="_blank" rel="noopener">The Pittsburgh Wire</a> and <a href="https://thegrantfinder.org" target="_blank" rel="noopener">The Grant Finder</a>.</p>
            <div class="author-links">
                <a href="/about">Full Bio</a>
                <a href="https://drconnorrobertson.com" target="_blank" rel="noopener">DrConnorRobertson.com</a>
                <a href="https://www.linkedin.com/in/drconnorrobertson/" target="_blank" rel="noopener">LinkedIn</a>
            </div>
        </div>
    </div>
</section>

<section class="blog-section">
    <h2>From the Blog</h2>
    <div class="blog-grid">{blog_cards}</div>
</section>
"""
    content += footer()
    content += page_end()
    return write_file("index.html", content)


def generate_about():
    social_list = "".join(f'<a href="{s["url"]}" target="_blank" rel="noopener">{s["name"]}</a>' for s in SOCIAL_PROFILES)
    website_list = "".join(f'<a href="{w["url"]}" target="_blank" rel="noopener">{w["name"]}</a>' for w in WEBSITES)

    bc = [("Home", "/"), ("About", "/about")]
    schemas = [person_schema(), breadcrumb_schema(bc)]

    content = head(
        "About Dr. Connor Robertson - Author, Entrepreneur, Strategic Advisor",
        "Learn about Dr. Connor Robertson, author of Buying Wealth, Creative Acquisitions, The 7 Minute Phone Call, and Built to Run.",
        "/about",
        schemas
    )
    content += header("about")
    content += breadcrumb_html(bc)
    content += """
<section class="author-section" style="padding-top:40px;">
    <div class="author-inner">
        <div class="author-photo-placeholder">
            CR
            <span>Author</span>
        </div>
        <div class="author-bio">
            <h2>Dr. Connor Robertson</h2>
            <p>Dr. Connor Robertson is an entrepreneur, author, and strategic advisor whose career spans acquisitions, tax strategy, business systems, and media. With a background that combines academic rigor with real-world deal-making experience, Connor has built a reputation for turning complex financial and operational concepts into practical, actionable frameworks.</p>

            <p>Connor is the author of four books: <a href="/books/buying-wealth/">Buying Wealth</a>, a practical guide to building ownership through strategic asset acquisition; <a href="/books/creative-acquisitions/">Creative Acquisitions</a>, which covers unconventional strategies for buying businesses; <a href="/books/the-7-minute-phone-call/">The 7 Minute Phone Call</a>, a framework for restarting stalled deals and closing with confidence; and <a href="/books/built-to-run/">Built to Run</a>, a guide to building business systems that operate independently of the founder.</p>

            <p>Through <a href="https://elixirconsultinggroup.com" target="_blank" rel="noopener">Elixir Consulting Group</a>, Connor advises business owners on growth strategy, acquisition structuring, and operational excellence. His consulting work focuses on helping entrepreneurs transition from operators to owners by building systems, teams, and processes that scale.</p>

            <p>Connor is the host of <a href="https://prospectingshow.com" target="_blank" rel="noopener">The Prospecting Show</a>, where he interviews founders, sales professionals, and business leaders about the strategies that drive revenue growth. He is also the founder of <a href="https://thepittsburghwire.com" target="_blank" rel="noopener">The Pittsburgh Wire</a>, a digital publication covering Pittsburgh business, real estate, and development news, and <a href="https://thegrantfinder.org" target="_blank" rel="noopener">The Grant Finder</a>, a resource platform for grant seekers.</p>

            <p>Connor holds a doctoral degree and brings an analytical, evidence-based approach to everything he writes and advises on. His work has been featured in Yahoo Finance and across multiple digital platforms. He lives and works in Pittsburgh, Pennsylvania.</p>
"""
    content += f"""
            <h2 style="margin-top:40px;">Connect</h2>
            <div class="author-links">{social_list}</div>

            <h2 style="margin-top:30px;">Websites &amp; Projects</h2>
            <div class="author-links">{website_list}</div>
        </div>
    </div>
</section>
"""
    content += footer()
    content += page_end()
    return write_file("about.html", content)


def generate_book_landing(book):
    bc = [("Home", "/"), ("Books", "/"), (book["title"], f"/books/{book['slug']}/")]
    reviews_html = ""
    for r in book["review_quotes"]:
        reviews_html += f"""<div class="review"><p>"{r['text']}"</p><div class="reviewer">-- {r['reviewer']}</div></div>"""

    chapters_html = ""
    for ch in book["chapters"]:
        chapters_html += f"""<a href="/books/{book['slug']}/chapters/{ch['num']}/" class="chapter-item">
            <div class="chapter-num">Chapter {ch['num']}</div>
            <h3>{ch['title']}</h3>
            <p>{ch['summary'][:120]}...</p>
        </a>"""

    schemas = [book_schema(book), breadcrumb_schema(bc)]

    content = head(
        f"{book['title']} by Dr. Connor Robertson - {book['subtitle']}",
        book['description'],
        f"/books/{book['slug']}/",
        schemas
    )
    content += header(book['slug'])
    content += f"""
<div class="book-detail-hero" style="background: linear-gradient(135deg, {book['color']}, {book['accent']});">
    <div class="book-detail-inner">
        <div class="book-detail-cover" style="background: linear-gradient(160deg, {book['color']}, {book['accent']}); border: 2px solid rgba(255,255,255,0.2);">
            <h2>{book['title']}</h2>
            <div class="cover-line"></div>
            <div class="cover-author">Dr. Connor Robertson</div>
        </div>
        <div class="book-detail-info">
            <h1>{book['title']}</h1>
            <div class="subtitle">{book['subtitle']}</div>
            <p>{book['long_description']}</p>
            <div class="buy-buttons">
                <a href="{book['amazon_url']}" class="buy-btn primary-btn" target="_blank" rel="noopener">Amazon</a>
                <a href="{book['bn_url']}" class="buy-btn" target="_blank" rel="noopener">Barnes &amp; Noble</a>
                <a href="{book['google_play_url']}" class="buy-btn" target="_blank" rel="noopener">Google Play</a>
            </div>
        </div>
    </div>
</div>
"""
    content += breadcrumb_html(bc)
    content += f"""
<div class="content-with-sidebar">
    {book_sidebar(book, "landing")}
    <div class="page-content" style="padding-top:0;">
        <h2>What Readers Are Saying</h2>
        <div class="reviews">{reviews_html}</div>

        <h2>Chapter by Chapter</h2>
        <div class="chapter-list">{chapters_html}</div>

        <h2 style="margin-top:40px;">More from This Book</h2>
        <div style="display:flex;gap:15px;flex-wrap:wrap;margin-top:15px;">
            <a href="/books/{book['slug']}/key-lessons/" class="buy-btn" style="border-color:var(--border);color:var(--text);">Key Lessons</a>
            <a href="/books/{book['slug']}/who-should-read/" class="buy-btn" style="border-color:var(--border);color:var(--text);">Who Should Read This</a>
        </div>
    </div>
</div>
"""
    content += footer()
    content += page_end()
    return write_file(f"books/{book['slug']}/index.html", content)


def generate_chapter_page(book, chapter):
    ch = chapter
    bc = [("Home", "/"), (book["title"], f"/books/{book['slug']}/"), (f"Chapter {ch['num']}", f"/books/{book['slug']}/chapters/{ch['num']}/")]
    schemas = [book_schema(book), breadcrumb_schema(bc)]

    # Generate extended chapter content
    content_body = f"""
        <p>{ch['summary']}</p>

        <p>In Chapter {ch['num']} of <em>{book['title']}</em>, Dr. Connor Robertson builds on the foundation laid in earlier chapters to address one of the most critical topics in the book: {ch['title'].lower()}. This chapter is designed to be both conceptual and practical, providing frameworks you can apply immediately alongside the deeper thinking required for long-term success.</p>

        <p>The ideas in this chapter emerged from years of real-world experience working with entrepreneurs, investors, and business owners who were navigating exactly these challenges. Rather than offering abstract theory, Robertson provides specific, tested approaches grounded in actual outcomes.</p>

        <h2>Core Concepts</h2>
        <p>The central argument of this chapter is that {ch['title'].lower()} is not something that happens by accident. It requires intentional effort, clear thinking, and a willingness to challenge conventional assumptions. Robertson walks through the reasoning step by step, using examples that illustrate both the right approach and the common mistakes that derail progress.</p>

        <p>One of the most compelling sections deals with the practical implementation of these ideas. Too many business books stop at the conceptual level. This chapter goes further, providing specific action steps, decision frameworks, and evaluation criteria that you can use in your own work starting today.</p>

        <h2>Practical Application</h2>
        <p>Robertson provides several frameworks in this chapter that readers consistently cite as among the most valuable in the entire book. The emphasis is on repeatable processes, not one-time insights. The goal is to build a system for approaching {ch['title'].lower()} that works regardless of market conditions, deal size, or personal circumstances.</p>

        <p>Whether you are early in your journey or well-established, the principles in Chapter {ch['num']} provide a foundation for making better decisions and building more sustainable outcomes.</p>

        <h2>Key Takeaway</h2>
        <blockquote>{ch['summary']}</blockquote>
    """

    # Nav links
    prev_ch = None
    next_ch = None
    for i, c in enumerate(book["chapters"]):
        if c["num"] == ch["num"]:
            if i > 0:
                prev_ch = book["chapters"][i-1]
            if i < len(book["chapters"]) - 1:
                next_ch = book["chapters"][i+1]

    nav = '<div style="display:flex;justify-content:space-between;margin-top:40px;padding-top:20px;border-top:1px solid var(--border);">'
    if prev_ch:
        nav += f'<a href="/books/{book["slug"]}/chapters/{prev_ch["num"]}/">&larr; Ch. {prev_ch["num"]}: {prev_ch["title"]}</a>'
    else:
        nav += '<span></span>'
    if next_ch:
        nav += f'<a href="/books/{book["slug"]}/chapters/{next_ch["num"]}/">Ch. {next_ch["num"]}: {next_ch["title"]} &rarr;</a>'
    else:
        nav += f'<a href="/books/{book["slug"]}/key-lessons/">Key Lessons &rarr;</a>'
    nav += '</div>'

    page = head(
        f"Chapter {ch['num']}: {ch['title']} - {book['title']} by Dr. Connor Robertson",
        f"Chapter {ch['num']} of {book['title']}: {ch['summary'][:155]}",
        f"/books/{book['slug']}/chapters/{ch['num']}/",
        schemas
    )
    page += header(book['slug'])
    page += f"""
<div class="page-hero" style="background: linear-gradient(135deg, {book['color']}, {book['accent']}); padding: 40px 20px;">
    <p style="font-size:0.85rem;text-transform:uppercase;letter-spacing:2px;opacity:0.8;margin-bottom:8px;">{book['title']}</p>
    <h1>Chapter {ch['num']}: {ch['title']}</h1>
</div>
"""
    page += breadcrumb_html(bc)
    page += f"""
<div class="content-with-sidebar">
    {book_sidebar(book, f"ch{ch['num']}")}
    <div class="page-content" style="padding-top:0;">
        {content_body}
        {nav}
    </div>
</div>
"""
    page += footer()
    page += page_end()
    return write_file(f"books/{book['slug']}/chapters/{ch['num']}/index.html", page)


def generate_key_lessons(book):
    bc = [("Home", "/"), (book["title"], f"/books/{book['slug']}/"), ("Key Lessons", f"/books/{book['slug']}/key-lessons/")]
    schemas = [book_schema(book), breadcrumb_schema(bc)]

    lessons_html = ""
    for i, lesson in enumerate(book["key_lessons"], 1):
        lessons_html += f"""
        <div style="background:var(--bg-light);padding:25px;border-radius:6px;margin-bottom:15px;border-left:3px solid var(--gold);">
            <div style="font-size:0.8rem;color:var(--gold);text-transform:uppercase;letter-spacing:1px;margin-bottom:8px;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;">Lesson {i}</div>
            <p style="font-size:1.05rem;color:var(--primary);font-weight:500;">{lesson}</p>
        </div>"""

    page = head(
        f"Key Lessons from {book['title']} by Dr. Connor Robertson",
        f"The most important lessons and takeaways from {book['title']} by Dr. Connor Robertson.",
        f"/books/{book['slug']}/key-lessons/",
        schemas
    )
    page += header(book['slug'])
    page += f"""
<div class="page-hero" style="background: linear-gradient(135deg, {book['color']}, {book['accent']}); padding: 40px 20px;">
    <p style="font-size:0.85rem;text-transform:uppercase;letter-spacing:2px;opacity:0.8;margin-bottom:8px;">{book['title']}</p>
    <h1>Key Lessons</h1>
</div>
"""
    page += breadcrumb_html(bc)
    page += f"""
<div class="content-with-sidebar">
    {book_sidebar(book, "lessons")}
    <div class="page-content" style="padding-top:0;">
        <p>These are the core lessons from <em>{book['title']}</em> that readers tell us have had the biggest impact on their thinking and their results.</p>
        {lessons_html}

        <div style="margin-top:40px;padding:30px;background:var(--bg-light);border-radius:8px;text-align:center;">
            <h3 style="margin-bottom:12px;">Ready to dive deeper?</h3>
            <p style="margin-bottom:20px;">Get the full framework, examples, and implementation guides in the book.</p>
            <div class="buy-buttons" style="justify-content:center;">
                <a href="{book['amazon_url']}" class="buy-btn primary-btn" target="_blank" rel="noopener" style="background:var(--gold);border-color:var(--gold);color:var(--primary);">Amazon</a>
                <a href="{book['bn_url']}" class="buy-btn" style="border-color:var(--border);color:var(--text);" target="_blank" rel="noopener">Barnes &amp; Noble</a>
                <a href="{book['google_play_url']}" class="buy-btn" style="border-color:var(--border);color:var(--text);" target="_blank" rel="noopener">Google Play</a>
            </div>
        </div>
    </div>
</div>
"""
    page += footer()
    page += page_end()
    return write_file(f"books/{book['slug']}/key-lessons/index.html", page)


def generate_who_should_read(book):
    bc = [("Home", "/"), (book["title"], f"/books/{book['slug']}/"), ("Who Should Read", f"/books/{book['slug']}/who-should-read/")]
    schemas = [book_schema(book), breadcrumb_schema(bc)]

    audiences_html = ""
    for aud in book["who_should_read"]["audiences"]:
        audiences_html += f"""
        <div style="background:#fff;padding:25px;border-radius:8px;margin-bottom:15px;box-shadow:0 2px 8px rgba(0,0,0,0.05);">
            <h3 style="color:var(--primary);margin-bottom:8px;">{aud['name']}</h3>
            <p style="color:var(--text-light);">{aud['name']} {aud['reason']}.</p>
        </div>"""

    page = head(
        f"Who Should Read {book['title']} by Dr. Connor Robertson",
        f"Find out if {book['title']} by Dr. Connor Robertson is right for you. Written for entrepreneurs, investors, and business owners.",
        f"/books/{book['slug']}/who-should-read/",
        schemas
    )
    page += header(book['slug'])
    page += f"""
<div class="page-hero" style="background: linear-gradient(135deg, {book['color']}, {book['accent']}); padding: 40px 20px;">
    <p style="font-size:0.85rem;text-transform:uppercase;letter-spacing:2px;opacity:0.8;margin-bottom:8px;">{book['title']}</p>
    <h1>Who Should Read This Book</h1>
</div>
"""
    page += breadcrumb_html(bc)
    page += f"""
<div class="content-with-sidebar">
    {book_sidebar(book, "who")}
    <div class="page-content" style="padding-top:0;">
        <p><em>{book['title']}</em> was written for people who are ready to take action. While the concepts apply broadly, these are the specific audiences who will get the most value from the book.</p>

        {audiences_html}

        <h2>Not Sure If This Book Is for You?</h2>
        <p>If you are asking yourself whether you need this book, consider this: the people who benefit most from <em>{book['title']}</em> are those who recognize that their current approach is not getting them where they want to go. If you are ready for a new framework, a new system, or a new way of thinking about {book['title'].lower()}, this book was written for you.</p>

        <div style="margin-top:40px;padding:30px;background:var(--bg-light);border-radius:8px;text-align:center;">
            <h3 style="margin-bottom:12px;">Get Your Copy</h3>
            <div class="buy-buttons" style="justify-content:center;">
                <a href="{book['amazon_url']}" class="buy-btn primary-btn" target="_blank" rel="noopener" style="background:var(--gold);border-color:var(--gold);color:var(--primary);">Amazon</a>
                <a href="{book['bn_url']}" class="buy-btn" style="border-color:var(--border);color:var(--text);" target="_blank" rel="noopener">Barnes &amp; Noble</a>
                <a href="{book['google_play_url']}" class="buy-btn" style="border-color:var(--border);color:var(--text);" target="_blank" rel="noopener">Google Play</a>
            </div>
        </div>
    </div>
</div>
"""
    page += footer()
    page += page_end()
    return write_file(f"books/{book['slug']}/who-should-read/index.html", page)


def generate_book_blog(book):
    """Generate a related blog post for each book."""
    # Find matching blog post
    related = None
    for p in BLOG_POSTS:
        if p["related_book"] == book["slug"]:
            related = p
            break
    if not related:
        return None

    bc = [("Home", "/"), ("Blog", "/blog/"), (related["title"], f"/blog/{related['slug']}/")]
    schemas = [blog_schema(related), breadcrumb_schema(bc)]

    page = head(
        f"{related['title']} - Dr. Connor Robertson",
        f"{related['title']} by Dr. Connor Robertson. Insights and lessons from {book['title']}.",
        f"/blog/{related['slug']}/",
        schemas
    )
    page += header("blog")
    page += breadcrumb_html(bc)
    page += f"""
<div class="page-content">
    <div style="margin-bottom:30px;">
        <div style="font-size:0.8rem;color:var(--gold);text-transform:uppercase;letter-spacing:1px;margin-bottom:10px;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;">{datetime.strptime(related['date'], '%Y-%m-%d').strftime('%B %d, %Y')}</div>
        <h1 style="font-size:2.2rem;color:var(--primary);font-weight:400;margin-bottom:10px;">{related['title']}</h1>
        <p style="color:var(--text-light);font-style:italic;">By Dr. Connor Robertson</p>
    </div>
    {related['content']}
</div>
"""
    page += footer()
    page += page_end()
    return write_file(f"blog/{related['slug']}/index.html", page)


def generate_blog_index():
    bc = [("Home", "/"), ("Blog", "/blog/")]
    schemas = [breadcrumb_schema(bc)]

    posts_html = ""
    for p in BLOG_POSTS:
        book = next((b for b in BOOKS if b["slug"] == p["related_book"]), None)
        book_label = f' <span style="background:{book["color"]}15;color:{book["color"]};padding:3px 10px;border-radius:3px;font-size:0.75rem;">{book["title"]}</span>' if book else ""
        posts_html += f"""
        <div class="blog-card">
            <div class="blog-date">{datetime.strptime(p['date'], '%Y-%m-%d').strftime('%B %d, %Y')}{book_label}</div>
            <h3><a href="/blog/{p['slug']}/">{p['title']}</a></h3>
        </div>"""

    page = head(
        "Blog - Dr. Connor Robertson",
        "Insights on wealth building, business acquisitions, sales, and systems from Dr. Connor Robertson.",
        "/blog/",
        schemas
    )
    page += header("blog")
    page += """
<div class="page-hero" style="background: linear-gradient(135deg, var(--primary), var(--accent)); padding: 50px 20px;">
    <h1>Blog</h1>
    <p>Insights on wealth building, acquisitions, sales, and business systems</p>
</div>
"""
    page += breadcrumb_html(bc)
    page += f"""
<div style="max-width:var(--max-width);margin:0 auto;padding:40px 20px 80px;">
    <div class="blog-grid">{posts_html}</div>
</div>
"""
    page += footer()
    page += page_end()
    return write_file("blog/index.html", page)


def generate_standalone_blog(post):
    bc = [("Home", "/"), ("Blog", "/blog/"), (post["title"], f"/blog/{post['slug']}/")]
    schemas = [blog_schema(post), breadcrumb_schema(bc)]

    page = head(
        f"{post['title']} - Dr. Connor Robertson",
        f"{post['title']} by Dr. Connor Robertson.",
        f"/blog/{post['slug']}/",
        schemas
    )
    page += header("blog")
    page += breadcrumb_html(bc)
    page += f"""
<div class="page-content">
    <div style="margin-bottom:30px;">
        <div style="font-size:0.8rem;color:var(--gold);text-transform:uppercase;letter-spacing:1px;margin-bottom:10px;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;">{datetime.strptime(post['date'], '%Y-%m-%d').strftime('%B %d, %Y')}</div>
        <h1 style="font-size:2.2rem;color:var(--primary);font-weight:400;margin-bottom:10px;">{post['title']}</h1>
        <p style="color:var(--text-light);font-style:italic;">By Dr. Connor Robertson</p>
    </div>
    {post['content']}
</div>
"""
    page += footer()
    page += page_end()
    return write_file(f"blog/{post['slug']}/index.html", page)


def generate_sitemap():
    urls = ["/"]
    urls.append("/about")
    urls.append("/blog/")
    for b in BOOKS:
        urls.append(f"/books/{b['slug']}/")
        urls.append(f"/books/{b['slug']}/key-lessons/")
        urls.append(f"/books/{b['slug']}/who-should-read/")
        for ch in b["chapters"]:
            urls.append(f"/books/{b['slug']}/chapters/{ch['num']}/")
    for p in BLOG_POSTS:
        urls.append(f"/blog/{p['slug']}/")

    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for u in urls:
        xml += f'  <url><loc>{SITE_URL}{u}</loc><changefreq>weekly</changefreq></url>\n'
    xml += '</urlset>'
    return write_file("sitemap.xml", xml), len(urls)


def generate_robots():
    content = f"""User-agent: *
Allow: /

Sitemap: {SITE_URL}/sitemap.xml
"""
    return write_file("robots.txt", content)


def generate_vercel_json():
    config = {
        "cleanUrls": True,
        "trailingSlash": True,
        "headers": [
            {
                "source": "/(.*)",
                "headers": [
                    {"key": "X-Content-Type-Options", "value": "nosniff"},
                    {"key": "X-Frame-Options", "value": "DENY"}
                ]
            }
        ]
    }
    return write_file("vercel.json", json.dumps(config, indent=2))


def generate_404():
    page = head(
        "Page Not Found - Dr. Connor Robertson",
        "The page you are looking for could not be found.",
        "/404",
        []
    )
    page += header()
    page += """
<div class="page-hero" style="background: linear-gradient(135deg, var(--primary), var(--accent)); padding: 80px 20px;">
    <h1>Page Not Found</h1>
    <p>The page you are looking for does not exist or has been moved.</p>
    <a href="/" class="hero-cta" style="margin-top:20px;">Back to Home</a>
</div>
"""
    page += footer()
    page += page_end()
    return write_file("404.html", page)


# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    files = []

    # CSS
    files.append(write_file("css/style.css", css()))
    print(f"  [CSS] style.css")

    # Homepage
    files.append(generate_homepage())
    print(f"  [PAGE] index.html")

    # About
    files.append(generate_about())
    print(f"  [PAGE] about.html")

    # Blog index
    files.append(generate_blog_index())
    print(f"  [PAGE] blog/index.html")

    # 404
    files.append(generate_404())
    print(f"  [PAGE] 404.html")

    # For each book
    for book in BOOKS:
        # Landing
        files.append(generate_book_landing(book))
        print(f"  [BOOK] {book['slug']}/index.html")

        # Chapters
        for ch in book["chapters"]:
            files.append(generate_chapter_page(book, ch))
            print(f"  [CHAP] {book['slug']}/chapters/{ch['num']}/index.html")

        # Key lessons
        files.append(generate_key_lessons(book))
        print(f"  [PAGE] {book['slug']}/key-lessons/index.html")

        # Who should read
        files.append(generate_who_should_read(book))
        print(f"  [PAGE] {book['slug']}/who-should-read/index.html")

    # Blog posts
    for post in BLOG_POSTS:
        files.append(generate_standalone_blog(post))
        print(f"  [BLOG] blog/{post['slug']}/index.html")

    # Sitemap
    sm, url_count = generate_sitemap()
    files.append(sm)
    print(f"  [META] sitemap.xml ({url_count} URLs)")

    # Robots
    files.append(generate_robots())
    print(f"  [META] robots.txt")

    # Vercel
    files.append(generate_vercel_json())
    print(f"  [META] vercel.json")

    # Images placeholder directory
    os.makedirs(os.path.join(OUTPUT_DIR, "images"), exist_ok=True)

    total_pages = len([f for f in files if f.endswith('.html')])
    print(f"\n{'='*60}")
    print(f"  TOTAL HTML PAGES: {total_pages}")
    print(f"  TOTAL FILES: {len(files)}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
