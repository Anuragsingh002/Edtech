import re

html_file = '/Users/anurag/Desktop/Edtech/singhania-education.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Enquiry Form styling (already uses .form-input, .form-label, .form-textarea, .btn-primary)
# "glassmorphism effect for the form container: semi-transparent dark background (rgba(0,0,0,0.4)), backdrop blur, thin translucent white border"
# Find the container for contact form:
# <div style="background: var(--gradient-card); backdrop-filter: blur(20px); border: 1px solid var(--glass-border); border-radius: var(--radius-xl); padding: 2rem; position: relative; overflow: hidden;">
# We'll replace this specific style with the requested one.
form_container_old = 'background: var(--gradient-card); backdrop-filter: blur(20px); border: 1px solid var(--glass-border); border-radius: var(--radius-xl); padding: 2rem; position: relative; overflow: hidden;'
form_container_new = 'background: rgba(0,0,0,0.4); backdrop-filter: blur(20px); border: 1px solid rgba(255,255,255,0.15); border-radius: var(--radius-xl); padding: 2rem; position: relative; overflow: hidden; box-shadow: var(--shadow-lg);'
content = content.replace(form_container_old, form_container_new)

# "Input fields: dark semi-transparent bg, white text, light gray labels, focus highlight in Golden Yellow"
# The CSS for .form-input is already:
# .form-input, .form-select, .form-textarea { width: 100%; padding: 14px 18px; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); border-radius: var(--radius-md); color: #fff; font-size: 1rem; transition: var(--transition-normal); }
# .form-input:focus, .form-select:focus, .form-textarea:focus { border-color: var(--accent-gold); box-shadow: 0 0 0 3px rgba(240,165,0,0.15); background: rgba(255,255,255,0.08); }
# This matches perfectly! Let's just make sure it's crisp white and light gray labels.
# .form-label is: color: rgba(226,232,240,0.8); -> this is light gray.
# I'll update the CSS slightly to be exact: background: rgba(0,0,0,0.5); for inputs
content = content.replace('background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1);', 'background: rgba(0,0,0,0.5); border: 1px solid rgba(255,255,255,0.15);')

# 2. Polishing Navigation Bar
# .nav-link { ... color: rgba(255,255,255,0.75); ... transition: var(--transition-normal); }
# .nav-link:hover, .nav-link.active { color: #fff; background: rgba(255,255,255,0.08); }
content = content.replace('.nav-link:hover, .nav-link.active { color: #fff; background: rgba(255,255,255,0.08); }', 
                          '.nav-link:hover, .nav-link.active { color: var(--accent-gold); background: rgba(255,255,255,0.05); }')

# 3. Elevating CTA Buttons
# .btn { ... transition: var(--transition-normal); ... }
# .btn-primary { ... } .btn-primary:hover { transform: translateY(-3px); box-shadow: 0 0 50px rgba(240,165,0,0.5); }
# .btn-secondary { ... } .btn-secondary:hover { border-color: var(--accent-gold); color: var(--accent-gold); transform: translateY(-3px); }
content = content.replace('.btn-primary:hover { transform: translateY(-3px); box-shadow: 0 0 50px rgba(240,165,0,0.5); }',
                          '.btn-primary:hover { transform: translateY(-2px); box-shadow: 0 8px 25px rgba(240,165,0,0.6); }')
content = content.replace('.btn-secondary:hover { border-color: var(--accent-gold); color: var(--accent-gold); transform: translateY(-3px); }',
                          '.btn-secondary:hover { border-color: var(--accent-gold); color: var(--accent-gold); transform: translateY(-2px); box-shadow: 0 0 15px rgba(240,165,0,0.4), 0 8px 20px rgba(0,0,0,0.4); }')

# 4. Humanizing the Hero Copy
# .hero-text p { font-size: 1.2rem; color: rgba(226,232,240,0.8); line-height: 1.8; margin-bottom: var(--space-2xl); max-width: 520px; }
content = content.replace('.hero-text p { font-size: 1.2rem; color: rgba(226,232,240,0.8); line-height: 1.8; margin-bottom: var(--space-2xl); max-width: 520px; }',
                          '.hero-text p { font-size: 1.2rem; color: #E2E8F0; font-weight: 400; line-height: 1.6; margin-bottom: var(--space-2xl); max-width: 520px; text-shadow: 0 2px 4px rgba(0,0,0,0.3); }')

# 5. Image Blend and Depth
# Wrap hero image in a container with inset shadow.
# old: <img src="hero-students.png" alt="Students on campus" style="width: 100%; height: 400px; object-fit: cover; border-radius: var(--radius-xl); box-shadow: var(--shadow-xl);">
hero_img_old = '<img src="hero-students.png" alt="Students on campus" style="width: 100%; height: 400px; object-fit: cover; border-radius: var(--radius-xl); box-shadow: var(--shadow-xl);">'
hero_img_new = '<div style="position: relative; border-radius: var(--radius-xl); overflow: hidden; box-shadow: var(--shadow-xl);"><img src="hero-students.png" alt="Students on campus" style="width: 100%; height: 400px; object-fit: cover; display: block;"><div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; box-shadow: inset 0 0 40px rgba(10,14,39,0.9); pointer-events: none; background: linear-gradient(to right, rgba(10,14,39,0.4) 0%, transparent 20%, transparent 80%, rgba(10,14,39,0.4) 100%);"></div></div>'
content = content.replace(hero_img_old, hero_img_new)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated CSS and layout.")
