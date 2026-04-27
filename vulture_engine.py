import datetime
import random
import re
import os

# --- VULTURE 10K CONFIGURATION ---
# These banks allow for thousands of unique title/content combinations
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

def generate_vulture_intel():
    """Generates a unique technical intelligence node."""
    niche = random.choice(NICHES)
    topic = random.choice(CORE_TOPICS)
    prop = random.choice(VALUE_PROPS)
    today = datetime.datetime.now().strftime("%B %d, %Y")
    
    # Generate a random 6-digit Hex ID for 'authenticity'
    node_id = f"0x{random.randint(0x100000, 0xFFFFFF):X}"
    
    html_payload = f"""
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
    return html_payload

def update_blog_file(file_path='blog.html'):
    """Injects the new content into the HTML file, replacing the old daily node."""
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found.")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    new_intel = generate_vulture_intel()

    # Search for the Vulture Comment Tags to replace content
    pattern = r".*?"
    
    if re.search(pattern, content, re.DOTALL):
        # Swap existing content
        updated_content = re.sub(pattern, new_intel, content, flags=re.DOTALL)
        print("Vulture Engine: Successfully updated existing Intel Node.")
    else:
        # First time injection: Look for the opening of the main content container
        # Adjust 'article' or 'container' to match your blog.html structure
        if "<article id=\"main-content\">" in content:
            updated_content = content.replace("<article id=\"main-content\">", f"<article id=\"main-content\">\n{new_intel}")
            print("Vulture Engine: Initial Intel Node injected.")
        else:
            # Fallback: inject after header
            updated_content = content.replace("</header>", f"</header>\n{new_intel}")
            print("Vulture Engine: Header fallback injection used.")

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(updated_content)

if __name__ == "__main__":
    update_blog_file()
