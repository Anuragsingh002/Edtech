import re
import shutil
import os

html_file = '/Users/anurag/Desktop/Edtech/singhania-education.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Copy images
artifact_dir = '/Users/anurag/.gemini/antigravity/brain/2898e3b0-e465-44a6-be0a-965938c91405'
dest_dir = '/Users/anurag/Desktop/Edtech'

images = {
    'feature_counseling': 'feature_counseling_1780942221371.png',
    'feature_colleges': 'feature_colleges_1780942234549.png',
    'feature_support': 'feature_support_1780942248813.png',
    'feature_scholarship': 'feature_scholarship_1780942261477.png',
    'feature_loan': 'feature_loan_1780942273666.png',
    'feature_network': 'feature_network_1780942287211.png'
}

for img in images.values():
    shutil.copy(os.path.join(artifact_dir, img), os.path.join(dest_dir, img))

# 2. Update Why Choose Us section cards
def inject_image(card_title, img_filename):
    global content
    img_tag = f'<img src="{img_filename}" alt="{card_title}" style="width:100%; height:180px; object-fit:cover; border-radius: var(--radius-md); margin-bottom: 1.5rem;">'
    pattern = r'(<div class="card-3d-inner">).*?(<h3>' + re.escape(card_title) + r'</h3>)'
    content = re.sub(pattern, r'\1' + img_tag + r'\2', content, flags=re.DOTALL)

inject_image('Personalized Counseling', images['feature_counseling'])
inject_image('500+ Top Colleges', images['feature_colleges'])
inject_image('Complete Admission Support', images['feature_support'])
inject_image('Scholarship Assistance', images['feature_scholarship'])
inject_image('Education Loan Help', images['feature_loan'])
inject_image('Pan-India Network', images['feature_network'])

# 3. Remove "Get in Touch With Us" and Contact Info Cards
parts = content.split('<!-- ================= CONTACT SECTION ================= -->')
if len(parts) > 1:
    subparts = parts[1].split('<!-- Location Map -->')
    if len(subparts) > 1:
        new_start = '\n  <section class="section-padding" id="contact">\n    <div class="container">\n      '
        parts[1] = new_start + '<!-- Location Map -->' + subparts[1]
        content = '<!-- ================= CONTACT SECTION ================= -->'.join(parts)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Images inserted and contact section cleaned successfully.")
