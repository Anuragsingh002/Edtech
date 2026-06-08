import shutil
import re

# Copy images
hero_src = '/Users/anurag/.gemini/antigravity/brain/2898e3b0-e465-44a6-be0a-965938c91405/hero_students_1780940174843.png'
about_src = '/Users/anurag/.gemini/antigravity/brain/2898e3b0-e465-44a6-be0a-965938c91405/about_counseling_1780940187573.png'

hero_dst = '/Users/anurag/Desktop/Edtech/hero-students.png'
about_dst = '/Users/anurag/Desktop/Edtech/about-counseling.png'

shutil.copy(hero_src, hero_dst)
shutil.copy(about_src, about_dst)

html_file = '/Users/anurag/Desktop/Edtech/singhania-education.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace hero placeholder with image
hero_placeholder = '<div class="hero-image-placeholder" style="font-family: var(--font-heading); font-weight: 900; color: #fff;">SE</div>'
hero_img = '<img src="hero-students.png" alt="Students on campus" style="width: 100%; height: 400px; object-fit: cover; border-radius: var(--radius-xl); box-shadow: var(--shadow-xl);">'
content = content.replace(hero_placeholder, hero_img)
# Also if it's still `<div class="hero-image-placeholder">SE</div>` without the style:
content = content.replace('<div class="hero-image-placeholder">SE</div>', hero_img)

# Replace about placeholder with image
about_placeholder = '<div style="position: relative; border-radius: var(--radius-xl); overflow: hidden; background: linear-gradient(135deg, rgba(124,58,237,0.2), rgba(240,165,0,0.15)); height: 400px; display: flex; align-items: center; justify-content: center; font-size: 6rem;">SE</div>'
about_img = '<img src="about-counseling.png" alt="Counseling session" style="width: 100%; height: 400px; object-fit: cover; border-radius: var(--radius-xl); box-shadow: var(--shadow-lg);">'
content = content.replace(about_placeholder, about_img)

# We need to re-insert SVG icons where we removed the empty icon divs.
# To do this reliably, we can search for `<h3>` and inject an SVG before it based on the text.

svgs = {
    'Personalized Counseling': '<div class="card-icon card-icon-gold"><svg width="32" height="32" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg></div>',
    'IIM Ahmedabad': '<div class="card-icon card-icon-gold"><svg width="32" height="32" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M3 21h18M5 21V7l7-4 7 4v14M9 21v-4a2 2 0 012-2h2a2 2 0 012 2v4"></path></svg></div>',
    'IIM Bangalore': '<div class="card-icon card-icon-cyan"><svg width="32" height="32" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M3 21h18M5 21V7l7-4 7 4v14M9 21v-4a2 2 0 012-2h2a2 2 0 012 2v4"></path></svg></div>',
    'IIM Calcutta': '<div class="card-icon card-icon-purple"><svg width="32" height="32" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M3 21h18M5 21V7l7-4 7 4v14M9 21v-4a2 2 0 012-2h2a2 2 0 012 2v4"></path></svg></div>',
    'Call Us': '<div class="card-icon card-icon-gold" style="margin: 0 auto 1rem;"><svg width="32" height="32" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07 19.5 19.5 0 01-6-6 19.79 19.79 0 01-3.07-8.67A2 2 0 014.11 2h3a2 2 0 012 1.72 12.84 12.84 0 00.7 2.81 2 2 0 01-.45 2.11L8.09 9.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45 12.84 12.84 0 002.81.7A2 2 0 0122 16.92z"></path></svg></div>',
    'WhatsApp': '<div class="card-icon card-icon-emerald" style="margin: 0 auto 1rem;"><svg width="32" height="32" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M21 11.5a8.38 8.38 0 01-.9 3.8 8.5 8.5 0 01-7.6 4.7 8.38 8.38 0 01-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 01-.9-3.8 8.5 8.5 0 014.7-7.6 8.38 8.38 0 013.8-.9h.5a8.48 8.48 0 018 8v.5z"></path></svg></div>',
    'Email Us': '<div class="card-icon card-icon-cyan" style="margin: 0 auto 1rem;"><svg width="32" height="32" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><path d="M22 6l-10 7L2 6"></path></svg></div>',
    'Head Office': '<div class="card-icon card-icon-purple" style="margin: 0 auto 1rem;"><svg width="32" height="32" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z"></path><circle cx="12" cy="10" r="3"></circle></svg></div>',
}

# The cards for Why Choose Us might be named differently depending on Hindi translation, let's check:
# We know the contact cards have `h3 style="font-size: 1.1rem;">Call Us</h3>`
for key, svg in svgs.items():
    if key in ['Call Us', 'WhatsApp', 'Email Us', 'Head Office']:
        content = re.sub(rf'(<h3[^>]*>{key}</h3>)', rf'{svg}\1', content)
    else:
        content = re.sub(rf'(<h3>{key}</h3>)', rf'{svg}\1', content)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updates completed.")
