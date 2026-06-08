import re
import sys

html_file = '/Users/anurag/Desktop/Edtech/singhania-education.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix About Image missing issue
old_about = '<div style="position: relative; border-radius: var(--radius-xl); overflow: hidden; background: linear-gradient(135deg, rgba(124,58,237,0.2), rgba(240,165,0,0.15)); height: 400px; display: flex; align-items: center; justify-content: center; font-size: 6rem;"></div>'
new_about = '<div style="position: relative; border-radius: var(--radius-xl); overflow: hidden; box-shadow: var(--shadow-xl);"><img src="about-counseling.png" alt="Counseling session" style="width: 100%; height: 400px; object-fit: cover; display: block;"><div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; box-shadow: inset 0 0 40px rgba(10,14,39,0.5); pointer-events: none;"></div></div>'
if old_about in content:
    content = content.replace(old_about, new_about)

# 2. Fix Emojis in Why Choose Us
clipboard_svg = '<svg width="32" height="32" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-3 7h3m-3 4h3m-6-4h.01M9 16h.01"></path></svg>'
money_svg = '<svg width="32" height="32" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M12 2v20m5-17H9.5a3.5 3.5 0 000 7h5a3.5 3.5 0 010 7H6"></path></svg>'
globe_svg = '<svg width="32" height="32" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"></circle><path d="M2 12h20M12 2a15.3 15.3 0 014 10 15.3 15.3 0 01-4 10 15.3 15.3 0 01-4-10 15.3 15.3 0 014-10z"></path></svg>'
content = content.replace('📋', clipboard_svg)
content = content.replace('💰', money_svg)
content = content.replace('🌐', globe_svg)

# 3. WhatsApp and Call SVG
whatsapp_svg = '<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="currentColor" viewBox="0 0 16 16"><path d="M13.601 2.326A7.85 7.85 0 0 0 7.994 0C3.627 0 .068 3.558.064 7.926c0 1.399.366 2.76 1.057 3.965L0 16l4.204-1.102a7.9 7.9 0 0 0 3.79.965h.004c4.368 0 7.926-3.558 7.93-7.93A7.9 7.9 0 0 0 13.6 2.326zM7.994 14.521a6.6 6.6 0 0 1-3.356-.92l-.24-.144-2.494.654.666-2.433-.156-.251a6.56 6.56 0 0 1-1.007-3.505c0-3.626 2.957-6.584 6.591-6.584a6.56 6.56 0 0 1 4.66 1.931 6.56 6.56 0 0 1 1.928 4.66c-.004 3.639-2.961 6.592-6.592 6.592m3.615-4.934c-.197-.099-1.17-.578-1.353-.646-.182-.065-.315-.099-.445.099-.133.197-.513.646-.627.775-.114.133-.232.148-.43.05-.197-.1-.836-.308-1.592-.985-.59-.525-.985-1.175-1.103-1.372-.114-.198-.011-.304.088-.403.087-.088.197-.232.296-.346.1-.114.133-.198.198-.33.065-.134.034-.248-.015-.347-.05-.099-.445-1.076-.612-1.47-.16-.389-.323-.335-.445-.34-.114-.007-.247-.007-.38-.007a.73.73 0 0 0-.529.247c-.182.198-.691.677-.691 1.654s.71 1.916.81 2.049c.098.133 1.394 2.132 3.383 2.992.47.205.84.326 1.129.418.475.152.904.129 1.246.08.38-.058 1.171-.48 1.338-.943.164-.464.164-.86.114-.943-.049-.084-.182-.133-.38-.232"/></svg>'
call_svg = '<svg width="32" height="32" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07 19.5 19.5 0 01-6-6 19.79 19.79 0 01-3.07-8.67A2 2 0 014.11 2h3a2 2 0 012 1.72 12.84 12.84 0 00.7 2.81 2 2 0 01-.45 2.11L8.09 9.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45 12.84 12.84 0 002.81.7A2 2 0 0122 16.92z"></path></svg>'
# In the WhatsApp card, replace the generic svg:
wa_old = '<div class="card-icon card-icon-emerald" style="margin: 0 auto 1rem;"><svg width="32" height="32" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M21 11.5a8.38 8.38 0 01-.9 3.8 8.5 8.5 0 01-7.6 4.7 8.38 8.38 0 01-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 01-.9-3.8 8.5 8.5 0 014.7-7.6 8.38 8.38 0 013.8-.9h.5a8.48 8.48 0 018 8v.5z"></path></svg></div>'
wa_new = f'<div class="card-icon card-icon-emerald" style="margin: 0 auto 1rem;">{whatsapp_svg}</div>'
content = content.replace(wa_old, wa_new)

# Update the WhatsApp popup animation using CSS. I already added whatsappPopup but maybe it needs a stronger effect or to be correctly applied.
if '@keyframes whatsappPopup' not in content:
    css_popup = """
    @keyframes whatsappPopup {
      0% { transform: scale(1); box-shadow: 0 4px 15px rgba(37,211,102,0.3); }
      50% { transform: scale(1.15); box-shadow: 0 10px 25px rgba(37,211,102,0.6); }
      100% { transform: scale(1); box-shadow: 0 4px 15px rgba(37,211,102,0.3); }
    }
    """
    content = content.replace('</style>', css_popup + '\n  </style>')

# Ensure the floating button has the animation
if 'whatsappPopup' not in content.split('class="whatsapp-float"')[1][:100] if 'class="whatsapp-float"' in content else False:
    content = content.replace('class="whatsapp-float"', 'class="whatsapp-float" style="animation: whatsappPopup 2s infinite ease-in-out;"')

# Ensure "Call Us" link is correct (it should be tel:7256890906 from previous step, but let's double check)
content = content.replace('href="tel:+919876543210"', 'href="tel:+917256890906"')
content = content.replace('href="https://wa.me/919876543210"', 'href="https://wa.me/917256890906"')
content = content.replace('>+91 98765 43210<', '>+91 72568 90906<')


# 4. Remove the redundant contact form section entirely, and center the map.
# Looking at the code:
# <div class="grid-2" style="gap: 3rem;">
#         <div class="reveal-left">
#           <div class="section-label">Send Message</div>...
#         </div>
#         <div class="reveal-right">
#           <div class="section-label">Our Locations</div>...
#         </div>
# </div>

# Let's extract that block and replace it.
pattern = r'<div class="grid-2" style="gap: 3rem;">.*?<div class="reveal-left">.*?<div class="reveal-right">(.*?)</div>\s*</div>'
# We will just write a regex to replace the grid-2 and reveal-left with just the map.

def remove_form_and_center_map(html):
    # Find the start of grid-2 under <!-- Contact Form -->
    parts = html.split('<!-- Contact Form -->')
    if len(parts) < 2: return html
    
    before = parts[0]
    after = parts[1]
    
    # In 'after', find the map part
    map_start = after.find('<div class="section-label">Our Locations</div>')
    if map_start == -1: return html
    
    # We want to keep everything from 'Our Locations' down to the end of the reveal-right.
    # The end of that block is before </section>
    section_end = after.find('</section>')
    
    # Let's just do a manual string manipulation
    # Find the map iframe and info boxes
    iframe_start = after.find('<iframe')
    iframe_end = after.find('</iframe>') + 9
    iframe_html = after[iframe_start:iframe_end]
    
    # Find the office hours info box
    office_box_start = after.find('<div class="info-box"', iframe_end)
    office_box_end = after.find('</div></div>', office_box_start) + 12
    office_box = after[office_box_start:office_box_end]
    
    # Find the reach info box
    reach_box_start = after.find('<div class="info-box"', office_box_end)
    reach_box_end = after.find('</div></div>', reach_box_start) + 12
    reach_box = after[reach_box_start:reach_box_end]
    
    new_map_section = f'''
      <div class="reveal text-center" style="max-width: 900px; margin: 0 auto;">
        <div class="section-label" style="justify-content: center;">Our Locations</div>
        <h2 class="section-title">Visit <span class="text-gradient">Our Office</span></h2>
        <div style="border-radius: var(--radius-xl); overflow: hidden; box-shadow: var(--shadow-lg); margin-bottom: 2rem; border: 1px solid var(--glass-border);">
          {iframe_html.replace('height="350"', 'height="450"')}
        </div>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; text-align: left;">
          {office_box.replace('margin-bottom: 1rem;', '')}
          {reach_box}
        </div>
      </div>
    '''
    
    # Now replace everything in 'after' up to the end of the section with the new map section
    end_of_grid = after.find('</section>')
    new_after = new_map_section + '\n    </div>\n  ' + after[end_of_grid:]
    
    return before + '<!-- Location Map -->\n' + new_after

content = remove_form_and_center_map(content)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixes applied successfully.")
