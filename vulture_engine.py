import datetime
import random
import os

BLOG_FILE = "blog.html"
START_TAG = "<!-- VULTURE START -->"
END_TAG = "<!-- VULTURE END -->"
MAX_POSTS = 7  # keep last 7 days

NICHES = [
    "Home-Based Screen Printing",
    "Boutique Apparel Brands",
    "Custom Merchandise Startups",
    "DIY Clothing Lines"
]

TOPICS = [
    "Ink Adhesion Optimization",
    "Flash Cure Temperature Control",
    "High-Margin Print Strategies",
    "Fabric Compatibility Engineering",
    "Low-Cost Production Scaling"
]


def generate_post():
    today = datetime.datetime.now().strftime("%B %d, %Y")
    niche = random.choice(NICHES)
    topic = random.choice(TOPICS)

    return f"""
<div class="intel-node">
<h3>{today} — {topic}</h3>

<p>
In the current custom apparel landscape, <strong>{niche}</strong> businesses are gaining a competitive edge by focusing on <strong>{topic.lower()}</strong>. 
Operators who refine this process consistently outperform competitors in both quality and profit margins.
</p>

<p>
The key advantage of DIY production is control. When you manage printing in-house, you eliminate outsourcing delays, reduce cost per unit, and unlock the ability to rapidly test new designs.
</p>

<p>
Most beginners underestimate how quickly small optimizations compound. Adjusting ink flow, improving curing consistency, and selecting better garments can dramatically increase perceived value.
</p>

<p>
At scale, these improvements translate directly into higher margins and repeat customers. This is why serious operators invest early in proper systems instead of treating printing as a hobby.
</p>

<a class="btn" href="https://www.linkconnector.com/ta.php?lc=007949155911007876&atid=VultureDaily" target="_blank">
Upgrade Your Setup
</a>
</div>
"""


def update_blog():
    if not os.path.exists(BLOG_FILE):
        raise FileNotFoundError("blog.html not found")

    with open(BLOG_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    if len(content) > 2_000_000:
        raise ValueError("File too large — reset required")

    start = content.find(START_TAG)
    end = content.find(END_TAG)

    if start == -1 or end == -1:
        raise ValueError("Markers not found")

    existing_block = content[start + len(START_TAG):end].strip()

    # Split existing posts
    posts = [p for p in existing_block.split('<div class="intel-node">') if p.strip()]

    # Rebuild posts cleanly
    posts = ['<div class="intel-node">' + p for p in posts]

    # Add new post at top
    new_post = generate_post()
    posts.insert(0, new_post)

    # Trim to max posts
    posts = posts[:MAX_POSTS]

    combined = "\n".join(posts)

    updated_content = (
        content[: start + len(START_TAG)] +
        "\n" + combined + "\n" +
        content[end:]
    )

    with open(BLOG_FILE, "w", encoding="utf-8") as f:
        f.write(updated_content)

    print("Blog updated. Total posts:", len(posts))


if __name__ == "__main__":
    update_blog()
