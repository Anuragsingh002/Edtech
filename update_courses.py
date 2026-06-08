import shutil
import re
import os

images = {
    'course_btech': 'course_btech_1780941241014.png',
    'course_mbbs': 'course_mbbs_1780941253191.png',
    'course_mba': 'course_mba_1780941265759.png',
    'course_law': 'course_law_1780941278874.png',
    'course_bdes': 'course_bdes_1780941291722.png',
    'course_bca': 'course_bca_1780941306787.png'
}

base_dir = '/Users/anurag/.gemini/antigravity/brain/2898e3b0-e465-44a6-be0a-965938c91405/'
dest_dir = '/Users/anurag/Desktop/Edtech/'

for name, filename in images.items():
    src = os.path.join(base_dir, filename)
    dst = os.path.join(dest_dir, f"{name}.png")
    if os.path.exists(src):
        shutil.copy(src, dst)

html_file = os.path.join(dest_dir, 'singhania-education.html')
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Add hover effect for course images
css_addition = """
    .course-card .course-card-image { position: relative; overflow: hidden; padding: 0 !important; background: transparent !important; }
    .course-card .course-img { width: 100%; height: 100%; object-fit: cover; transition: transform 0.5s ease; display: block; }
    .course-card:hover .course-img { transform: scale(1.1); }
    .course-card-overlay { position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(to bottom, transparent 0%, rgba(10,14,39,0.8) 100%); pointer-events: none; }
"""
if '.course-img {' not in content:
    content = content.replace('</style>', css_addition + '\n  </style>')

def replace_course_image(html, old_emoji, badge_text, img_name, alt_text):
    # Regex to find: <div class="course-card-image">EMOJI<div class="course-card-badge">BADGE</div></div>
    # or if emoji is already removed: <div class="course-card-image"><div class="course-card-badge">BADGE</div></div>
    
    # We will just search for the specific badge text and replace the whole course-card-image div containing it
    pattern = rf'<div class="course-card-image">(?:[^<]*)<div class="course-card-badge">{badge_text}</div></div>'
    
    new_html = f'''<div class="course-card-image">
            <img src="{img_name}.png" alt="{alt_text}" class="course-img">
            <div class="course-card-overlay"></div>
            <div class="course-card-badge">{badge_text}</div>
          </div>'''
    
    return re.sub(pattern, new_html, html)

content = replace_course_image(content, '⚙️', 'Top Rated', 'course_btech', 'B.Tech Engineering')
content = replace_course_image(content, '', 'High Demand', 'course_mbbs', 'MBBS Medical')
content = replace_course_image(content, '', 'Most Popular', 'course_mba', 'MBA Management')
content = replace_course_image(content, '', 'Growing', 'course_law', 'LLB Law')
content = replace_course_image(content, '🎨', 'Creative', 'course_bdes', 'B.Des Design')
content = replace_course_image(content, '🖥️', 'IT Career', 'course_bca', 'BCA IT')

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Course images updated successfully.")
