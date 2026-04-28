import datetime
import random
import os

# --- VULTURE 10K CONFIGURATION ---
NICHES = ["Home-Based Screen Printing", "Boutique Apparel Brands", "Custom Merchandise Startups", "DIY Clothing Lines"]

CORE_TOPICS = [
    "Mesh Tension and Registration Physics",
    "Photosensitive Emulsion Cross-Linking",
    "Flash Cure Temperature Management",
    "Ink Viscosity and Sheer Stress",
    "Substrate Pre-treatment Protocols",
    "Hydrophobic Coating Dynamics"
]

VALUE_PROPS = [
    "Maximizing Profit Margins",
    "Reducing Setup Latency",
    "Ensuring Industrial Durability",
    "2026 Eco-Compliance Standards"
]

START_TAG = "<!-- VULTURE START -->"
END_TAG = "<!-- VULTURE END -->"


def generate_vulture_intel():
    niche = random.choice(NICHES)
    topic = random.choice(CORE_TOPICS)
    prop = random.choice(VALUE_PROPS)
    today = datetime.datetime.now().strftime("%B %d, %Y")

    node_id = f"0x{random.randint(0x100000, 0xFFFFFF):X}"

    return f"""
<div class="daily-intel-node" style="border: 2px solid #e63946; padding: 30px; margin-bottom: 50px; background: #ffffff; border-radius: 15px; box-shadow: 0 10px 20px rgba(0,0,0,0.05);">
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;">
        <span style="background: #e63946; color: white; padding: 5px 12px; font-weight: bold; border-radius: 5px; font-family: monospace; font-size: 0.8rem;">ENGINE SYNC: {today}</span>
        <span style="color: #999; font-family: monospace; font-size: 0.8rem;">NODE_ID: {node_id}</span>
    </div>
    <h2 style="margin-top: 0; color: #111;">Intelligence Report: {topic}</h2>
    <p>Current 2026 data indicates that <strong>{niche}</strong> operations are seeing a shift toward <strong>{topic}</strong> as a primary driver for <strong>{prop.lower()}</strong>.</p>
    <p>Technical Analysis: Mastering the molecular bond between the ink and substrate is the foundation of high-end custom apparel. By optimizing your {topic.lower()} workflow, you reduce waste and increase the wash-fastness of your final product.</p>
    <div style="background: #f8f8f8; padding: 15px; border-left: 5px solid #e63946; font-style: italic; margin: 20px 0;">
        "Automation in the home shop begins with the right chemistry. Don't settle for hobby-grade results when industrial-grade kits are within reach."
    </div>
    <a href="https://www.linkconnector.com/ta.php?lc=007949155911007876&atid=VultureDaily" class="btn" style="text-decoration: none; display: inline-block; background: #e63946; color: white; padding: 12px 25px; border-radius: 5px; font-weight: bold;">UPGRADE EQUIPMENT STACK</a>
</div>
"""


def update_blog_file(file_path='blog.html'):
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found.")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    print("Content size:", len(content))

    # Safety guard
    if len(content) > 2_000_000:
        raise ValueError("blog.html too large — possible duplication bug")

    new_intel = generate_vulture_intel()

    start = content.find(START_TAG)
    end = content.find(END_TAG)

    if start != -1 and end != -1 and start < end:
        # Replace existing block
        updated_content = (
            content[: start + len(START_TAG)] +
            "\n" + new_intel + "\n" +
            content[end:]
        )
        print("Vulture Engine: Updated existing Intel Node.")

    else:
        # First-time injection
        print("Vulture Engine: Markers not found. Injecting fresh block.")

        block = f"\n{START_TAG}\n{new_intel}\n{END_TAG}\n"

        if '<article id="main-content">' in content:
            updated_content = content.replace(
                '<article id="main-content">',
                f'<article id="main-content">{block}'
            )
        elif "</header>" in content:
            updated_content = content.replace("</header>", f"</header>{block}")
        else:
            # Last resort: append
            updated_content = content + block

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(updated_content)


if __name__ == "__main__":
    update_blog_file()
