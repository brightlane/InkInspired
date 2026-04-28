import datetime
import random
import os

BLOG_FILE = "blog.html"

START_TAG = "<!-- VULTURE START -->"
END_TAG = "<!-- VULTURE END -->"

MAX_POSTS = 7


def generate_post():
    today = datetime.datetime.now().strftime("%B %d, %Y")

    topics = [
        "Ink Flow Optimization",
        "Heat Cure Consistency",
        "Fabric Bond Strength",
        "Low Cost Scaling Systems",
        "Print Quality Control Loops"
    ]

    niche = "DIY Custom Apparel Business"

    return f"""
<div class="intel-node">
<h3>{today} — {random.choice(topics)}</h3>

<p>
The <strong>{niche}</strong> continues to grow as creators shift toward home-based production systems with higher profit control.
</p>

<p>
Small improvements in workflow efficiency, ink handling, and curing accuracy can significantly increase product quality and resale value.
</p>

<p>
Operators who focus on consistency rather than speed tend to outperform in long-term customer retention.
</p>

<a class="btn" href="https://www.linkconnector.com/ta.php?lc=007949155911007876&atid=VultureDaily" target="_blank">
Upgrade Setup
</a>
</div>
"""


def update_blog():
    if not os.path.exists(BLOG_FILE):
        raise FileNotFoundError("blog.html not found")

    with open(BLOG_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    print("Content size:", len(content))

    # safety guard (prevents corruption like your 85MB issue)
    if len(content) > 2_000_000:
        raise ValueError("File too large — reset required")

    start = content.find(START_TAG)
    end = content.find(END_TAG)

    if start == -1 or end == -1:
        raise ValueError("VULTURE markers missing")

    old_block = content[start + len(START_TAG):end].strip()

    # split safely into posts
    posts = []
    for part in old_block.split('<div class="intel-node">'):
        if part.strip():
            posts.append('<div class="intel-node">' + part)

    # add new post
    posts.insert(0, generate_post())

    # keep last N posts only
    posts = posts[:MAX_POSTS]

    new_block = "\n".join(posts)

    updated = (
        content[:start + len(START_TAG)] +
        "\n" + new_block + "\n" +
        content[end:]
    )

    with open(BLOG_FILE, "w", encoding="utf-8") as f:
        f.write(updated)

    print(f"Updated blog successfully. Posts: {len(posts)}")


if __name__ == "__main__":
    update_blog()
