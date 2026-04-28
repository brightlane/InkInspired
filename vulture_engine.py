import os
import datetime

BLOG_FILE = "blog.html"
ARCHIVE_DIR = "blog"

INDEX_START = "<!-- VULTURE INDEX START -->"
INDEX_END = "<!-- VULTURE INDEX END -->"


# -----------------------------
# DAILY CONTENT GENERATION
# -----------------------------
def generate_post():
    today = datetime.datetime.now().strftime("%B %d, %Y")

    return f"""
<div class="intel-node">

<h2>Ink Optimization & Profit Strategy Update — {today}</h2>

<p>
Today's focus is improving ink adhesion consistency for home-based apparel businesses.
Better curing control and fabric prep directly increases product durability and resale value.
</p>

<p>
Small improvements in workflow efficiency can significantly increase margins for DIY custom apparel brands.
</p>

<a class="btn" href="https://www.linkconnector.com/ta.php?lc=007949155911007876&atid=VultureDaily" target="_blank">
Beginner Kit Recommendation
</a>

</div>
"""


# -----------------------------
# ARCHIVE PAGE CREATION
# -----------------------------
def create_archive(date_str, content, prev_day, next_day):
    if not os.path.exists(ARCHIVE_DIR):
        os.makedirs(ARCHIVE_DIR)

    prev_link = f"{prev_day}.html" if prev_day else "../blog.html"
    next_link = f"{next_day}.html" if next_day else "../blog.html"

    html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Daily Intel {date_str}</title>

<style>
body {{ font-family: Arial; background:#f8f8f8; padding:20px; }}
a {{ color:#e63946; }}
.intel-node {{ background:#fff; padding:20px; border-radius:8px; }}
</style>

</head>

<body>

<a href="../blog.html">← Back to Hub</a>

<h1>{date_str}</h1>

{content}

<br><br>

<a href="{prev_link}">← Previous</a> |
<a href="../blog.html">Hub</a> |
<a href="{next_link}">Next →</a>

</body>
</html>
"""

    with open(f"{ARCHIVE_DIR}/{date_str}.html", "w", encoding="utf-8") as f:
        f.write(html)


# -----------------------------
# HUB INDEX UPDATE
# -----------------------------
def update_hub_index(date_str):
    if not os.path.exists(BLOG_FILE):
        raise FileNotFoundError("blog.html not found")

    with open(BLOG_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    link_html = f'<p><a class="post-link" href="blog/{date_str}.html">Daily Intel {date_str}</a></p>'

    start = content.find(INDEX_START)
    end = content.find(INDEX_END)

    if start == -1 or end == -1:
        raise ValueError("Missing VULTURE INDEX markers in blog.html")

    updated = (
        content[:start + len(INDEX_START)] +
        "\n" + link_html + "\n" +
        content[end:]
    )

    with open(BLOG_FILE, "w", encoding="utf-8") as f:
        f.write(updated)


# -----------------------------
# MAIN RUNNER
# -----------------------------
def run():
    today = datetime.datetime.now().strftime("%Y-%m-%d")

    content = generate_post()

    prev_day = None
    next_day = None

    create_archive(today, content, prev_day, next_day)
    update_hub_index(today)

    print(f"[VULTURE ENGINE] Generated: {today}")


if __name__ == "__main__":
    run()
