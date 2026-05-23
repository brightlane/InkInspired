#!/usr/bin/env python3
"""
DIY Custom Apparel Affiliate Site Generator
Generates 10 SEO-optimized HTML pages with affiliate links intact.
Run: python3 generate_site.py
Output: ./site/ folder with all pages ready to upload.
"""

import os
import json
from datetime import datetime

# ============================================================
# CONFIGURATION — Edit these to customize your site
# ============================================================
AFFILIATE_URL = "https://www.linkconnector.com/ta.php?lc=007949155911007876&atid=ScreenPrintingWeb"
SITE_NAME = "DIY Custom Apparel HQ"
SITE_TAGLINE = "Print It. Sell It. Profit."
OUTPUT_DIR = "site"
YEAR = datetime.now().year

# ============================================================
# SHARED HTML COMPONENTS
# ============================================================
SHARED_CSS = """
  <style>
    *{box-sizing:border-box;margin:0;padding:0}
    body{font-family:'Segoe UI',Arial,sans-serif;background:#f5f5f5;color:#222;line-height:1.8}
    header{background:linear-gradient(135deg,#1a1a2e,#e63946);color:#fff;padding:60px 20px;text-align:center}
    header h1{font-size:2.4rem;margin-bottom:10px}
    header p{font-size:1.1rem;opacity:.9}
    nav{background:#111;position:sticky;top:0;z-index:99;text-align:center;padding:12px 0}
    nav a{color:#fff;margin:0 12px;text-decoration:none;font-weight:bold;font-size:.95rem}
    nav a:hover{color:#e63946}
    .container{max-width:900px;margin:30px auto;padding:0 15px}
    .card{background:#fff;border-radius:10px;padding:35px;margin-bottom:25px;box-shadow:0 2px 8px rgba(0,0,0,.08)}
    h2{color:#1a1a2e;font-size:1.7rem;margin-bottom:15px;border-left:4px solid #e63946;padding-left:12px}
    h3{color:#333;margin:20px 0 10px}
    p{margin-bottom:12px}
    ul{padding-left:22px;margin-bottom:12px}
    ul li{margin-bottom:6px}
    .btn{display:inline-block;background:#e63946;color:#fff;padding:14px 28px;border-radius:6px;
         text-decoration:none;font-weight:bold;font-size:1rem;transition:.3s;margin:8px 4px}
    .btn:hover{background:#c0392b;transform:translateY(-1px)}
    .btn-outline{background:transparent;border:2px solid #e63946;color:#e63946}
    .btn-outline:hover{background:#e63946;color:#fff}
    .cta-box{background:linear-gradient(135deg,#1a1a2e,#e63946);color:#fff;
              border-radius:10px;padding:35px;text-align:center;margin:25px 0}
    .cta-box h2{color:#fff;border:none;padding:0}
    .cta-box p{opacity:.9}
    table{width:100%;border-collapse:collapse;margin:20px 0}
    th{background:#e63946;color:#fff;padding:12px;text-align:left}
    td{padding:11px;border-bottom:1px solid #eee}
    tr:hover td{background:#fef5f5}
    .check{color:#27ae60;font-weight:bold}
    .cross{color:#e74c3c;font-weight:bold}
    .tag{display:inline-block;background:#f0f0f0;border-radius:20px;padding:4px 12px;
         font-size:.82rem;margin:3px;color:#555}
    .hero-stats{display:flex;justify-content:center;gap:30px;flex-wrap:wrap;margin-top:25px}
    .stat{text-align:center;background:rgba(255,255,255,.15);border-radius:8px;padding:15px 25px}
    .stat-num{font-size:2rem;font-weight:bold;display:block}
    footer{background:#111;color:#aaa;text-align:center;padding:30px 20px;margin-top:40px}
    footer a{color:#e63946;text-decoration:none}
    .disclosure{background:#fff3cd;border:1px solid #ffc107;border-radius:6px;
                padding:12px;font-size:.85rem;text-align:center;margin-bottom:20px}
    @media(max-width:600px){header h1{font-size:1.7rem}nav a{margin:0 6px;font-size:.85rem}}
  </style>
"""

def nav_links(current_slug=""):
    pages = [
        ("index.html", "Home"),
        ("beginners-guide.html", "Beginners"),
        ("equipment.html", "Equipment"),
        ("profit-strategies.html", "Profit"),
        ("niche-ideas.html", "Niches"),
        ("comparison.html", "Compare"),
        ("products.html", "Products"),
        ("selling-online.html", "Sell Online"),
        ("faq.html", "FAQ"),
        ("about.html", "About"),
    ]
    links = ""
    for slug, label in pages:
        active = ' style="color:#e63946"' if slug == current_slug else ""
        links += f'<a href="{slug}"{active}>{label}</a>'
    return f"<nav>{links}</nav>"

def cta_button(label="Get Your Beginner Kit →"):
    return f'<a class="btn" href="{AFFILIATE_URL}" target="_blank" rel="noopener">{label}</a>'

def cta_box(heading, sub, btn_label="Get Your Kit Now →"):
    return f"""
    <div class="cta-box">
      <h2>{heading}</h2>
      <p>{sub}</p>
      <br>
      <a class="btn" href="{AFFILIATE_URL}" target="_blank" rel="noopener"
         style="background:#fff;color:#e63946">{btn_label}</a>
    </div>"""

def disclosure():
    return f"""<div class="disclosure">
      ⚠️ <strong>Affiliate Disclosure:</strong> Some links on this page are affiliate links.
      If you purchase through them, we may earn a commission at no extra cost to you.
      We only recommend products we believe in.
    </div>"""

def base_page(slug, title, meta_desc, body_html, keywords=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width,initial-scale=1.0">
  <title>{title} | {SITE_NAME}</title>
  <meta name="description" content="{meta_desc}">
  {"<meta name='keywords' content='" + keywords + "'>" if keywords else ""}
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{meta_desc}">
  <meta name="robots" content="index,follow">
  {SHARED_CSS}
</head>
<body>
  <header>
    <h1>{SITE_NAME}</h1>
    <p>{SITE_TAGLINE}</p>
  </header>
  {nav_links(slug)}
  <div class="container">
    {disclosure()}
    {body_html}
  </div>
  <footer>
    <p>&copy; {YEAR} {SITE_NAME} &nbsp;|&nbsp;
       <a href="about.html">About</a> &nbsp;|&nbsp;
       <a href="about.html#privacy">Privacy Policy</a> &nbsp;|&nbsp;
       <a href="about.html#terms">Terms</a>
    </p>
    <p style="margin-top:8px;font-size:.82rem">
      Affiliate Disclosure: We earn commissions from qualifying purchases.
    </p>
  </footer>
</body>
</html>"""

# ============================================================
# PAGE DEFINITIONS
# ============================================================

def page_index():
    body = f"""
    <div class="card">
      <div style="text-align:center">
        <h2 style="border:none;padding:0;font-size:2rem">Start Your Custom Apparel Business at Home</h2>
        <p style="font-size:1.1rem;margin:15px 0">
          Screen printing, heat transfer, and personalized merch — all from your garage or spare room.
          No commercial equipment. No huge upfront costs.
        </p>
        {cta_button("Get Your Beginner Kit →")}
        <a class="btn btn-outline" href="beginners-guide.html">Read the Guide</a>
      </div>
      <div class="hero-stats">
        <div class="stat"><span class="stat-num">2–4×</span>Average markup on custom apparel</div>
        <div class="stat"><span class="stat-num">$0</span>Experience needed to start</div>
        <div class="stat"><span class="stat-num">1–2 days</span>To print your first shirt</div>
      </div>
    </div>

    <div class="card">
      <h2>What You Can Make</h2>
      <ul>
        <li>🎽 Custom T-shirts, hoodies, sweatshirts, jackets</li>
        <li>🧢 Hats, beanies, caps, and visors</li>
        <li>☕ Mugs, tumblers, and drinkware</li>
        <li>👜 Tote bags, aprons, pouches, and accessories</li>
        <li>🎁 Personalized gifts: keychains, notebooks, wristbands</li>
        <li>🏫 Team uniforms, event merch, corporate branded gear</li>
      </ul>
      {cta_button("Shop Beginner Kits")}
    </div>

    <div class="card">
      <h2>Why DIY Beats Outsourcing</h2>
      <table>
        <tr><th>Factor</th><th>DIY at Home</th><th>Outsourcing</th></tr>
        <tr><td>Profit per shirt</td><td class="check">$15–$30+</td><td class="cross">$3–$8</td></tr>
        <tr><td>Turnaround time</td><td class="check">Same day</td><td class="cross">5–14 days</td></tr>
        <tr><td>Minimum order</td><td class="check">1 piece</td><td class="cross">12–24 pieces</td></tr>
        <tr><td>Design control</td><td class="check">Full</td><td class="cross">Limited</td></tr>
        <tr><td>Startup cost</td><td class="check">Low (kit)</td><td class="cross">None upfront but low margin</td></tr>
      </table>
    </div>

    {cta_box("Ready to Start Printing?","Join thousands of home entrepreneurs who've launched with a beginner kit.")}

    <div class="card">
      <h2>Explore the Site</h2>
      <p>
        <a href="beginners-guide.html" style="color:#e63946">📘 Beginner's Guide</a> — step-by-step walkthrough<br>
        <a href="equipment.html" style="color:#e63946">🔧 Equipment Guide</a> — what you actually need<br>
        <a href="profit-strategies.html" style="color:#e63946">💰 Profit Strategies</a> — how to price and sell<br>
        <a href="niche-ideas.html" style="color:#e63946">🎯 Niche Ideas</a> — who to target<br>
        <a href="comparison.html" style="color:#e63946">⚖️ Competitor Comparison</a> — vs Printful, Printify, etc.<br>
        <a href="faq.html" style="color:#e63946">❓ FAQ</a> — common questions answered
      </p>
    </div>
    """
    return base_page("index.html", "DIY Custom Apparel at Home",
                     "Start a home-based custom apparel business. Print shirts, hoodies, mugs, and more with beginner-friendly kits. No experience needed.",
                     body, "custom apparel home business, DIY screen printing, personalized merchandise")

def page_beginners_guide():
    body = f"""
    <div class="card">
      <h2>Complete Beginner's Guide to DIY Custom Apparel</h2>
      <p>You don't need a fancy shop or expensive machines. This guide walks you from zero
         to printing your first shirt and selling it — step by step.</p>
      {cta_button("Get Your Beginner Kit First →")}
    </div>

    <div class="card">
      <h2>Step 1: Choose Your Printing Method</h2>
      <h3>🖥️ Screen Printing</h3>
      <p>Best for bold designs and bulk orders. Uses screens, ink, and a squeegee. Higher upfront
         learning curve, but the highest quality and profit margin.</p>
      <h3>🔥 Heat Transfer / HTV</h3>
      <p>Great for beginners. Cut vinyl designs and press them with a heat press.
         Works on shirts, bags, hats, and more.</p>
      <h3>🖨️ Sublimation</h3>
      <p>Best for polyester fabrics and mugs. Full-color photo-quality prints.
         Requires sublimation-coated blanks.</p>
      <h3>✍️ DTG (Direct to Garment)</h3>
      <p>Inkjet-style printing directly on fabric. Great for complex designs, but
         machines are expensive — not ideal for pure beginners.</p>
    </div>

    <div class="card">
      <h2>Step 2: Pick Your Niche</h2>
      <p>Don't try to sell to everyone. Pick one audience to start:</p>
      <ul>
        <li>Local sports teams needing jerseys and practice gear</li>
        <li>Small businesses wanting branded uniforms</li>
        <li>Schools and clubs needing event shirts</li>
        <li>Bachelorette/bachelor parties (huge demand!)</li>
        <li>Holiday and seasonal gifts</li>
        <li>Pet owners wanting custom pet apparel</li>
      </ul>
      <a href="niche-ideas.html" style="color:#e63946">→ See all niche ideas with profit estimates</a>
    </div>

    <div class="card">
      <h2>Step 3: Design Your Artwork</h2>
      <p>Free and paid tools to create printable designs:</p>
      <ul>
        <li><strong>Canva</strong> — free, beginner-friendly, great for text-based designs</li>
        <li><strong>Adobe Express</strong> — free tier, professional templates</li>
        <li><strong>Inkscape</strong> — free, vector graphics (best for screen printing)</li>
        <li><strong>Affinity Designer</strong> — one-time purchase, professional grade</li>
      </ul>
      <p><strong>Tip:</strong> Screen printing works best with vector files (SVG, AI, EPS).
         For heat transfer, PNG with transparent background is ideal.</p>
    </div>

    <div class="card">
      <h2>Step 4: Order Your Kit and Practice</h2>
      <p>Beginner kits include everything: screens, squeegees, emulsion, ink, and instructions.
         Practice on scrap fabric before printing on actual product.</p>
      <p>Most beginners produce their first wearable shirt within 1–2 practice sessions.</p>
      {cta_button("Order a Beginner Kit →")}
    </div>

    <div class="card">
      <h2>Step 5: Cure and Quality-Check</h2>
      <p>Curing sets the ink so it lasts through washing. Options:</p>
      <ul>
        <li><strong>Heat press</strong> — most consistent, recommended</li>
        <li><strong>Flash dryer</strong> — faster for production batches</li>
        <li><strong>Household oven</strong> — works for small batches (use separate oven)</li>
        <li><strong>Clothes dryer</strong> — budget option, less reliable</li>
      </ul>
      <p>Always wash test one shirt before fulfilling a bulk order.</p>
    </div>

    <div class="card">
      <h2>Step 6: Price, List, and Sell</h2>
      <p>Rule of thumb: price at <strong>2.5–4× your material cost</strong>. Include your time.
         Sell on Etsy, local Facebook groups, or your own website.</p>
      <a href="profit-strategies.html" style="color:#e63946">→ Full pricing and selling guide</a>
    </div>

    {cta_box("Start Today — Kits Ship Fast","Everything you need is in one box. No guesswork.", "Get My Kit →")}
    """
    return base_page("beginners-guide.html", "Beginner's Guide to DIY Custom Apparel",
                     "Step-by-step beginner guide to screen printing and custom apparel at home. No experience needed. Start with a beginner kit.",
                     body, "how to start custom apparel, screen printing beginners guide, DIY shirt printing")

def page_equipment():
    body = f"""
    <div class="card">
      <h2>Equipment Guide: What You Actually Need</h2>
      <p>The internet will tell you that you need thousands of dollars of gear.
         You don't — at least not to start. Here's the honest breakdown.</p>
    </div>

    <div class="card">
      <h2>Beginner Kit (Start Here)</h2>
      <p>A good beginner kit includes:</p>
      <ul>
        <li>✅ Silk screen frame(s)</li>
        <li>✅ Photo emulsion + sensitizer</li>
        <li>✅ Squeegee</li>
        <li>✅ Plastisol or water-based inks</li>
        <li>✅ Transparency sheets for film positives</li>
        <li>✅ Step-by-step tutorial</li>
      </ul>
      <p><strong>Cost:</strong> $50–$150 for a solid beginner kit vs $5,000+ for commercial equipment.</p>
      {cta_button("See Beginner Kits →")}
    </div>

    <div class="card">
      <h2>Ink Types Explained</h2>
      <table>
        <tr><th>Ink Type</th><th>Best For</th><th>Beginner Friendly</th></tr>
        <tr><td>Plastisol</td><td>Cotton shirts, durability</td><td class="check">Yes</td></tr>
        <tr><td>Water-based</td><td>Soft feel, eco-friendly</td><td class="check">Yes</td></tr>
        <tr><td>Discharge</td><td>Dark fabrics, vintage look</td><td class="cross">Intermediate</td></tr>
        <tr><td>Sublimation</td><td>Polyester, mugs, drinkware</td><td class="check">Yes (with blanks)</td></tr>
        <tr><td>UV/LED</td><td>Hard surfaces, specialty</td><td class="cross">Advanced</td></tr>
      </table>
    </div>

    <div class="card">
      <h2>Optional Upgrades (Add Later)</h2>
      <ul>
        <li><strong>Heat Press ($200–$400)</strong> — for consistent curing and HTV projects</li>
        <li><strong>Flash Dryer ($150–$300)</strong> — speeds up production between colors</li>
        <li><strong>Exposure Unit ($200–$600)</strong> — consistent screen burning vs sun exposure</li>
        <li><strong>Multi-color press ($800+)</strong> — for 2–6 color designs at scale</li>
      </ul>
      <p>Start with a kit. Upgrade only when orders justify the investment.</p>
    </div>

    <div class="card">
      <h2>Fabrics That Print Best</h2>
      <ul>
        <li>🥇 <strong>100% Cotton</strong> — best ink absorption, most beginner-friendly</li>
        <li>🥈 <strong>50/50 Cotton-Poly blend</strong> — softer feel, slightly less vivid</li>
        <li>🥉 <strong>100% Polyester</strong> — needs sublimation or special ink</li>
        <li>⚠️ <strong>Dark fabrics</strong> — require white underbase layer first</li>
      </ul>
    </div>

    {cta_box("Get Everything in One Kit","Stop researching and start printing. Kits have everything listed above.","Shop Kits Now →")}
    """
    return base_page("equipment.html", "Screen Printing Equipment Guide for Beginners",
                     "What equipment do you actually need to start screen printing at home? Honest guide covering kits, inks, heat presses, and more.",
                     body, "screen printing equipment beginners, DIY printing supplies, home apparel printing kit")

def page_profit():
    body = f"""
    <div class="card">
      <h2>Profit Strategies for Home Custom Apparel</h2>
      <p>The real money in custom apparel is in <strong>margin control</strong>.
         When you print yourself, you keep 60–80% of the sale price vs 10–20% with drop shipping.</p>
    </div>

    <div class="card">
      <h2>Pricing Formula</h2>
      <h3>Formula: (Material Cost × 2.5) + Labor</h3>
      <table>
        <tr><th>Item</th><th>Your Cost</th><th>Sell For</th><th>Profit</th></tr>
        <tr><td>Plain T-shirt + ink</td><td>$4–$6</td><td>$20–$28</td><td>$14–$22</td></tr>
        <tr><td>Custom Hoodie</td><td>$12–$16</td><td>$45–$65</td><td>$29–$49</td></tr>
        <tr><td>Custom Mug</td><td>$3–$5</td><td>$18–$25</td><td>$13–$20</td></tr>
        <tr><td>Tote Bag</td><td>$3–$4</td><td>$18–$22</td><td>$14–$18</td></tr>
        <tr><td>12-shirt Bulk Order</td><td>$60–$80</td><td>$240–$300</td><td>$160–$240</td></tr>
      </table>
    </div>

    <div class="card">
      <h2>Top Revenue Streams</h2>
      <ul>
        <li>🏆 <strong>Bulk orders</strong> — teams, schools, corporate (highest $/hour)</li>
        <li>🎉 <strong>Event shirts</strong> — bachelorettes, reunions, fundraisers</li>
        <li>🛒 <strong>Etsy shop</strong> — ongoing passive orders, low overhead</li>
        <li>📱 <strong>Local Facebook/Instagram</strong> — zero platform fees</li>
        <li>🎓 <strong>Teach workshops</strong> — $50–$100/person for printing classes</li>
        <li>🎁 <strong>Holiday bundles</strong> — Christmas, Valentine's, Mother's Day</li>
        <li>🏪 <strong>Consignment with local shops</strong> — no upfront buyer needed</li>
      </ul>
    </div>

    <div class="card">
      <h2>First 30 Days Action Plan</h2>
      <ol style="padding-left:20px;line-height:2">
        <li>Order beginner kit → practice until consistent quality</li>
        <li>Make 5–10 sample pieces (your portfolio)</li>
        <li>Post samples on Instagram/Facebook with price list</li>
        <li>Reach out to 3 local sports teams or businesses</li>
        <li>Open Etsy shop with 5–10 listings</li>
        <li>Reinvest first $200 profit into a heat press</li>
      </ol>
      {cta_button("Start with a Beginner Kit →")}
    </div>

    <div class="card">
      <h2>Scale Checklist</h2>
      <ul>
        <li>☐ Consistent print quality (wash test every batch)</li>
        <li>☐ Pricing sheet ready for quick quotes</li>
        <li>☐ Turnaround time defined (standard 5 days, rush 48h)</li>
        <li>☐ Bulk discount tiers (12+, 24+, 48+ pieces)</li>
        <li>☐ Simple invoice template</li>
        <li>☐ Repeat customer follow-up system</li>
      </ul>
    </div>

    {cta_box("Your First Sale Starts With a Kit","Get the supplies. Make the samples. Close your first order.","Get My Kit →")}
    """
    return base_page("profit-strategies.html", "Profit Strategies for DIY Custom Apparel",
                     "How to price, sell, and scale a home-based custom apparel business. Real profit numbers and a 30-day action plan.",
                     body, "custom apparel profit, how to price custom shirts, sell custom merchandise")

def page_niches():
    niches = [
        ("⚽ Youth Sports Teams", "$150–$400/order", "Jerseys, practice shirts, bags — parents pay fast and reorder every season."),
        ("🎉 Bachelorette Parties", "$80–$200/order", "High urgency, emotional buy, great for Etsy. 'Bride Squad' designs sell constantly."),
        ("🏫 Schools & PTA", "$200–$800/order", "Spirit wear, field day shirts, staff uniforms. High volume, repeat annually."),
        ("🍺 Bar & Restaurant Staff", "$100–$300/order", "Uniform polos, branded aprons, event tees. Reorder every 6–12 months."),
        ("💼 Small Local Businesses", "$150–$500/order", "Branded uniforms, promotional giveaways. Often repeat clients."),
        ("🐾 Pet Lovers", "$20–$40/item", "Custom pet portrait tees are viral on Etsy. High margin, easy design."),
        ("🎗️ Fundraisers & Charities", "$200–$1,000/campaign", "Usually bulk, upfront payment, great PR for your business."),
        ("🎓 College Clubs & Greek Life", "$300–$900/order", "Rush shirts, socials, philanthropies — ordered 3–5× per year."),
        ("👶 Baby & Kids Custom Gear", "$25–$50/item", "Personalized onesies, kids shirts — gift market is huge year-round."),
        ("🎮 Gaming & Fan Merch", "$20–$35/item", "Etsy shop play — niche communities pay premium for inside-joke designs."),
    ]

    rows = ""
    for name, revenue, tip in niches:
        rows += f"<tr><td><strong>{name}</strong></td><td style='color:#27ae60;font-weight:bold'>{revenue}</td><td>{tip}</td></tr>"

    body = f"""
    <div class="card">
      <h2>Best Niches for Home Custom Apparel</h2>
      <p>Don't sell to everyone — pick one niche to dominate first.
         Here are the most profitable and easiest to reach.</p>
    </div>

    <div class="card">
      <h2>Niche Comparison Table</h2>
      <table>
        <tr><th>Niche</th><th>Revenue / Order</th><th>Why It Works</th></tr>
        {rows}
      </table>
      {cta_button("Get Equipped to Serve Any Niche →")}
    </div>

    <div class="card">
      <h2>How to Land Your First Client in a Niche</h2>
      <ul>
        <li>Sports teams: Show up to a game with sample shirts. Coaches love it.</li>
        <li>Bachelorette: Post mockups on Pinterest and Etsy — people are already searching.</li>
        <li>Schools: Email the PTA president directly with a price sheet.</li>
        <li>Businesses: Walk in with a branded sample made for THEM (their logo, their colors).</li>
      </ul>
    </div>

    {cta_box("Pick Your Niche. Get Your Kit. Go.","The best time to start was last year. The second best time is today.","Shop Beginner Kits →")}
    """
    return base_page("niche-ideas.html", "Best Niches for Custom Apparel Business",
                     "Top 10 profitable niches for a home-based custom apparel business. Revenue estimates and tips to land your first client.",
                     body, "custom apparel niche, who to sell custom shirts to, best screen printing customers")

def page_comparison():
    body = f"""
    <div class="card">
      <h2>DIY vs. Print-on-Demand Services: Full Comparison</h2>
      <p>Printful, Printify, and Redbubble are popular — but do they actually make you more money?
         Let's compare honestly.</p>
    </div>

    <div class="card">
      <h2>Platform Comparison</h2>
      <table>
        <tr><th>Factor</th><th>DIY (Your Kit)</th><th>Printful</th><th>Printify</th><th>Redbubble</th></tr>
        <tr><td>Profit per shirt</td><td class="check">$14–$25</td><td>$3–$8</td><td>$3–$7</td><td>$1–$4</td></tr>
        <tr><td>Upfront cost</td><td>$50–$150 (kit)</td><td class="check">Free</td><td class="check">Free</td><td class="check">Free</td></tr>
        <tr><td>Quality control</td><td class="check">Full</td><td>Partial</td><td>Partial</td><td class="cross">None</td></tr>
        <tr><td>Custom 1-piece orders</td><td class="check">Yes</td><td class="check">Yes</td><td class="check">Yes</td><td class="check">Yes</td></tr>
        <tr><td>Turnaround</td><td class="check">Same day</td><td>3–7 days</td><td>3–10 days</td><td>5–14 days</td></tr>
        <tr><td>Local sales possible</td><td class="check">Yes</td><td class="cross">No</td><td class="cross">No</td><td class="cross">No</td></tr>
        <tr><td>Build real skills</td><td class="check">Yes</td><td class="cross">No</td><td class="cross">No</td><td class="cross">No</td></tr>
        <tr><td>Long-term scalability</td><td class="check">High</td><td>Medium</td><td>Medium</td><td>Low</td></tr>
      </table>
    </div>

    <div class="card">
      <h2>When to Use Each</h2>
      <h3>Use DIY Printing When:</h3>
      <ul>
        <li>You want to maximize profit per sale</li>
        <li>You're doing local/bulk orders</li>
        <li>You want to build a real skill and brand</li>
        <li>You need fast turnaround (same day)</li>
      </ul>
      <h3>Use Printful/Printify When:</h3>
      <ul>
        <li>You're testing a design idea before investing in supplies</li>
        <li>You want truly passive income (no physical work)</li>
        <li>You're selling 1-2 units/month in a niche</li>
      </ul>
      <p><strong>Best strategy:</strong> Use POD to test designs → switch to DIY once you know what sells.</p>
    </div>

    {cta_box("DIY Gives You the Best Margins","Start with a kit and keep 3–5× more profit than POD platforms.","Get Your Kit →")}
    """
    return base_page("comparison.html", "DIY vs Printful vs Printify: Custom Apparel Comparison",
                     "Honest comparison of DIY screen printing vs Printful, Printify, and Redbubble. Which gives you the most profit?",
                     body, "Printful vs DIY, Printify alternative, screen printing vs print on demand")

def page_products():
    products = [
        ("Custom T-Shirts", "The classic. Cotton tees are the easiest to print on and have the widest market."),
        ("Custom Hoodies & Sweatshirts", "Higher price point, great margins. Popular for teams and events."),
        ("Custom Hats & Beanies", "Embroidery or HTV works great. Sells year-round."),
        ("Custom Mugs & Tumblers", "Sublimation printing. Gift market is massive, especially around holidays."),
        ("Custom Tote Bags", "Eco-friendly angle. Popular with boutiques, farmers markets, and corporate gifts."),
        ("Custom Aprons", "Restaurants, bakeries, and hobbyists all want these. B2B goldmine."),
        ("Custom Patches & Emblems", "Iron-on or sew-on. Great add-on product for team and club orders."),
        ("Custom Baby Clothes", "Personalized onesies and toddler tees are top Etsy sellers."),
        ("Custom Wristbands & Keychains", "Low cost, high volume. Fundraisers love these."),
        ("Custom Jackets", "High ticket item. Corporate clients and sports teams pay premium."),
    ]

    cards = ""
    for name, desc in products:
        cards += f"""<div style="border:1px solid #eee;border-radius:8px;padding:15px;margin-bottom:12px">
          <strong>{name}</strong><br><span style="color:#555">{desc}</span>
        </div>"""

    body = f"""
    <div class="card">
      <h2>Products You Can Print & Sell</h2>
      <p>One beginner kit opens the door to all of these. Pick 2–3 to start and expand.</p>
      {cards}
      {cta_button("Get Your Kit and Start Printing →")}
    </div>

    <div class="card">
      <h2>Best Sellers by Season</h2>
      <table>
        <tr><th>Season</th><th>Top Products</th><th>Target Market</th></tr>
        <tr><td>Spring</td><td>Event tees, fundraiser shirts</td><td>Schools, charities</td></tr>
        <tr><td>Summer</td><td>Team jerseys, beach totes, hats</td><td>Sports leagues, tourists</td></tr>
        <tr><td>Fall</td><td>Hoodies, spirit wear</td><td>Schools, football teams</td></tr>
        <tr><td>Winter</td><td>Mugs, beanies, holiday gifts</td><td>Gift buyers, businesses</td></tr>
      </table>
    </div>

    {cta_box("Every Product Starts With the Right Supplies","One kit. Infinite products. Start today.","Shop Kits Now →")}
    """
    return base_page("products.html", "Custom Apparel Products You Can Make at Home",
                     "Full list of custom products you can print and sell from home: shirts, hoodies, mugs, bags, hats, and more.",
                     body, "what can I print at home, custom products to sell, screen printing product ideas")

def page_selling():
    body = f"""
    <div class="card">
      <h2>Where and How to Sell Your Custom Apparel</h2>
      <p>Making great shirts is half the battle. Here's how to turn prints into profit.</p>
    </div>

    <div class="card">
      <h2>Platform Breakdown</h2>
      <table>
        <tr><th>Platform</th><th>Best For</th><th>Fees</th><th>Difficulty</th></tr>
        <tr><td>Etsy</td><td>Custom gifts, pet items, bachelorette</td><td>6.5% + listing</td><td>Low</td></tr>
        <tr><td>Facebook Marketplace</td><td>Local bulk orders, events</td><td class="check">Free</td><td>Very Low</td></tr>
        <tr><td>Instagram/TikTok</td><td>Brand building, DM orders</td><td class="check">Free</td><td>Medium</td></tr>
        <tr><td>Your own website</td><td>Long-term brand, full margin</td><td>Hosting only</td><td>Medium</td></tr>
        <tr><td>Local markets/events</td><td>Face-to-face sales, samples</td><td>Booth fee</td><td>Low</td></tr>
        <tr><td>Direct B2B outreach</td><td>Corporate, restaurants, teams</td><td class="check">Free</td><td>Medium</td></tr>
      </table>
    </div>

    <div class="card">
      <h2>Etsy Optimization Tips</h2>
      <ul>
        <li>Use all 13 tags per listing — include size, occasion, style keywords</li>
        <li>Upload 5–7 mockup photos per listing (lifestyle photos outsell flat lays)</li>
        <li>Offer personalization — it boosts Etsy algorithm ranking</li>
        <li>Respond to messages within 1 hour (affects search ranking)</li>
        <li>Price slightly higher than competitors — perceived value matters</li>
        <li>Offer bundles: "Buy 3 get 10% off" increases average order value</li>
      </ul>
    </div>

    <div class="card">
      <h2>Social Media Strategy (Simple Version)</h2>
      <ol style="padding-left:20px;line-height:2">
        <li>Post a "process video" of printing a shirt — these go viral on TikTok</li>
        <li>Show before/after: plain shirt → finished design</li>
        <li>Feature happy customer photos (ask permission)</li>
        <li>Post "would you wear this?" polls to find what designs resonate</li>
        <li>Add your affiliate or shop link to every bio</li>
      </ol>
    </div>

    <div class="card">
      <h2>Landing Bulk Orders</h2>
      <p>One bulk order can equal weeks of individual sales. Here's how to get them:</p>
      <ul>
        <li>Create a PDF price sheet with quantity breaks (12/24/48 pieces)</li>
        <li>Offer a free sample shirt to coaches or business owners</li>
        <li>Partner with a local event company or wedding planner</li>
        <li>Attend small business expos and bring samples</li>
      </ul>
    </div>

    {cta_box("Get the Tools. Make the Products. Make the Sales.","Your kit is step one.","Order My Kit →")}
    """
    return base_page("selling-online.html", "How to Sell Custom Apparel Online and Locally",
                     "Where to sell custom apparel: Etsy, Facebook, Instagram, local markets. Platform comparison and tips to land bulk orders.",
                     body, "sell custom shirts online, Etsy custom apparel, how to get bulk t-shirt orders")

def page_faq():
    faqs = [
        ("What is the best beginner kit for screen printing?",
         "Look for a kit that includes at minimum: a pre-stretched screen, squeegee, photo emulsion, sensitizer, and at least one color of ink. Plastisol ink is most beginner-friendly. Full kits under $100 are widely available and give you everything to make your first shirt."),
        ("How much money can I make from home custom apparel?",
         "Part-time (10 hrs/week): $500–$1,500/month. Full-time: $3,000–$8,000+/month. Margins are 60–80% when you print yourself. A single bulk order of 24 shirts can earn $200–$400 profit in a few hours of work."),
        ("Do I need any experience to start?",
         "No. Beginner kits are designed for people with zero experience. Most people produce their first printable shirt within 1–2 practice sessions. The hardest part is exposing your screen correctly — kits include instructions for this."),
        ("What fabric works best for beginners?",
         "100% cotton is the easiest to work with. It absorbs ink well and gives vibrant, durable results. Avoid 100% polyester to start — it requires sublimation or special inks."),
        ("How do I cure my prints so they don't wash out?",
         "Use a heat press (best option), flash dryer, or a household oven at 320°F for about 90 seconds. Always do a wash test before fulfilling bulk orders."),
        ("Can I print multi-color designs as a beginner?",
         "Start with single-color designs. Once you're consistent, try two-color with a simple registration system. Multi-color requires careful alignment — most beginners do this within their first month."),
        ("Where is the best place to sell?",
         "Etsy for online (low competition for custom/personalized items), Facebook Marketplace for local orders, and direct outreach to local businesses and sports teams for bulk orders."),
        ("Is it eco-friendly?",
         "Water-based inks are the most eco-friendly option. Reusable screens reduce waste significantly compared to disposable print methods. You can market this as a selling point."),
        ("How do I handle rush orders?",
         "Charge a rush fee (20–50% premium). Most home printers can do same-day for small orders (under 12 pieces). Set clear cutoff times in your shop policies."),
        ("What should I sell first?",
         "Custom t-shirts for a local group you're already part of — a sports team, club, church, school. Warm market + you control the design = fastest first sale."),
    ]

    faq_html = ""
    schema_entities = []
    for q, a in faqs:
        faq_html += f"""
        <div style="border-bottom:1px solid #eee;padding:18px 0">
          <strong style="color:#1a1a2e;font-size:1.05rem">Q: {q}</strong>
          <p style="margin-top:8px">{a}</p>
        </div>"""
        schema_entities.append({
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {"@type": "Answer", "text": a}
        })

    schema = json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": schema_entities}, indent=2)

    body = f"""
    <script type="application/ld+json">{schema}</script>
    <div class="card">
      <h2>Frequently Asked Questions</h2>
      {faq_html}
      <br>
      {cta_button("Still have questions? Get a kit and start learning →")}
    </div>
    {cta_box("Ready to Start?","Your beginner kit comes with full instructions and support.","Order Now →")}
    """
    return base_page("faq.html", "Custom Apparel FAQ — Common Questions Answered",
                     "Answers to common questions about starting a home-based custom apparel business: cost, profit, equipment, fabrics, and selling.",
                     body, "custom apparel FAQ, screen printing questions, how to start custom shirt business")

def page_about():
    body = f"""
    <div class="card">
      <h2>About {SITE_NAME}</h2>
      <p>We're a resource for home entrepreneurs who want to build a custom apparel business
         without commercial-scale equipment or huge startup costs. We cover screen printing,
         heat transfer, sublimation, and everything in between.</p>
      <p>This site contains affiliate links. When you purchase through our links,
         we may earn a small commission — at no extra cost to you. This helps us keep
         the site free and updated.</p>
    </div>

    <div class="card" id="privacy">
      <h2>Privacy Policy</h2>
      <p><strong>Last updated: {datetime.now().strftime('%B %Y')}</strong></p>
      <p>This website does not collect personal information unless you voluntarily provide it.
         We use standard web analytics (no personally identifiable data stored).</p>
      <h3>Affiliate Links</h3>
      <p>This site participates in affiliate programs. We earn commissions on qualifying purchases
         made through affiliate links on this site. Prices are the same whether or not you use
         our affiliate link.</p>
      <h3>Cookies</h3>
      <p>We use minimal cookies for site functionality and analytics. No personal data is
         sold to third parties.</p>
      <h3>Third-Party Links</h3>
      <p>We link to third-party sites. We are not responsible for their privacy practices.
         Please review their policies before purchasing.</p>
      <h3>Contact</h3>
      <p>For privacy questions, contact us through the affiliate program we participate in.</p>
    </div>

    <div class="card" id="terms">
      <h2>Terms & Conditions</h2>
      <p><strong>Last updated: {datetime.now().strftime('%B %Y')}</strong></p>
      <p>By using this website, you agree to these terms. Content is provided for informational
         purposes only. We make no guarantees about income potential — results vary based on
         effort, market, and individual skill.</p>
      <h3>Affiliate Disclosure</h3>
      <p>In compliance with FTC guidelines: this site contains affiliate links and we may earn
         a commission from qualifying purchases. This does not affect our editorial independence.</p>
      <h3>Accuracy</h3>
      <p>We strive for accuracy but prices, features, and availability of products change.
         Always verify information directly with vendors before purchasing.</p>
      <h3>Limitation of Liability</h3>
      <p>This site is not liable for any decisions made based on content published here.
         Use information at your own discretion.</p>
    </div>
    """
    return base_page("about.html", "About Us | Privacy Policy | Terms",
                     "About DIY Custom Apparel HQ. Privacy policy, terms and conditions, and affiliate disclosure.",
                     body)

# ============================================================
# SITEMAP GENERATOR
# ============================================================
def generate_sitemap(base_url="https://yourdomain.com"):
    pages = [
        "index.html", "beginners-guide.html", "equipment.html",
        "profit-strategies.html", "niche-ideas.html", "comparison.html",
        "products.html", "selling-online.html", "faq.html", "about.html"
    ]
    urls = "\n".join([
        f"""  <url>
    <loc>{base_url}/{p}</loc>
    <changefreq>monthly</changefreq>
    <priority>{'1.0' if p == 'index.html' else '0.8'}</priority>
  </url>""" for p in pages
    ])
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{urls}
</urlset>"""

def generate_robots():
    return "User-agent: *\nAllow: /\nSitemap: https://yourdomain.com/sitemap.xml\n"

# ============================================================
# MAIN BUILDER
# ============================================================
def build_site():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    pages = {
        "index.html":           page_index(),
        "beginners-guide.html": page_beginners_guide(),
        "equipment.html":       page_equipment(),
        "profit-strategies.html": page_profit(),
        "niche-ideas.html":     page_niches(),
        "comparison.html":      page_comparison(),
        "products.html":        page_products(),
        "selling-online.html":  page_selling(),
        "faq.html":             page_faq(),
        "about.html":           page_about(),
    }

    for filename, html in pages.items():
        path = os.path.join(OUTPUT_DIR, filename)
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"  ✅  {filename}")

    with open(os.path.join(OUTPUT_DIR, "sitemap.xml"), "w") as f:
        f.write(generate_sitemap())
    print("  ✅  sitemap.xml")

    with open(os.path.join(OUTPUT_DIR, "robots.txt"), "w") as f:
        f.write(generate_robots())
    print("  ✅  robots.txt")

    # Verify affiliate URL is present in every page
    # about.html is a legal/privacy page — exempt from CTA requirement
    EXEMPT_PAGES = {"about.html"}
    print("\n🔍 Affiliate link audit:")
    all_good = True
    for filename in pages:
        path = os.path.join(OUTPUT_DIR, filename)
        with open(path, "r") as f:
            content = f.read()
        count = content.count(AFFILIATE_URL)
        if filename in EXEMPT_PAGES:
            status = "ℹ️ "
            print(f"  {status}  {filename} — legal page (exempt)")
        else:
            status = "✅" if count > 0 else "❌ MISSING"
            if count == 0:
                all_good = False
            print(f"  {status}  {filename} — {count} affiliate link(s)")

    print(f"\n{'✅ All content pages have your affiliate link!' if all_good else '❌ Some pages are missing the affiliate link — check above.'}")
    print(f"\n📁 Site built in ./{OUTPUT_DIR}/ — {len(pages)} pages + sitemap.xml + robots.txt")
    print(f"🔗 Affiliate ID: lc=007949155911007876&atid=ScreenPrintingWeb")
    print("\n📋 Next steps:")
    print("  1. Update 'yourdomain.com' in sitemap.xml with your real domain")
    print("  2. Upload the /site/ folder contents to your web host (root directory)")
    print("  3. Submit sitemap.xml to Google Search Console")
    print("  4. Share individual pages on Pinterest, Reddit, and Facebook groups")

if __name__ == "__main__":
    print(f"🚀 Building {SITE_NAME}...\n")
    build_site()
