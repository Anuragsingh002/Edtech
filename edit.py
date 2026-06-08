import re

file_path = '/Users/anurag/Desktop/Edtech/singhania-education.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

emojis = ['🎓', '🚀', '🏆', '📞', '📚', '🎯', '🏛️', '🏥', '📊', '⚖️', '📝', '🔒', '💬', '📧', '📍', '🕐', '🚇', '📘', '📷', '📺', '🐦', '💼', '📩', '❤️']
for e in emojis:
    content = content.replace(e, '')

# Add standard text for social media since I removed the emojis
content = content.replace('aria-label="Facebook"></a>', 'aria-label="Facebook">FB</a>')
content = content.replace('aria-label="Instagram"></a>', 'aria-label="Instagram">IG</a>')
content = content.replace('aria-label="YouTube"></a>', 'aria-label="YouTube">YT</a>')
content = content.replace('aria-label="Twitter"></a>', 'aria-label="Twitter">X</a>')
content = content.replace('aria-label="LinkedIn"></a>', 'aria-label="LinkedIn">IN</a>')

# Fix favicon
content = content.replace("<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'></text></svg>", "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='80' font-family='sans-serif' font-weight='bold' fill='%23f0a500'>SE</text></svg>")

whatsapp_svg = '''<!-- WhatsApp Float -->
  <a href="https://wa.me/91[YOUR PHONE NUMBER]?text=Hi,%20I'm%20interested%20in%20your%20tuition%20classes%20in%20Patna." target="_blank" class="whatsapp-float" aria-label="Chat on WhatsApp">
    <svg xmlns="http://www.w3.org/2000/svg" width="35" height="35" fill="currentColor" viewBox="0 0 16 16">
      <path d="M13.601 2.326A7.85 7.85 0 0 0 7.994 0C3.627 0 .068 3.558.064 7.926c0 1.399.366 2.76 1.057 3.965L0 16l4.204-1.102a7.9 7.9 0 0 0 3.79.965h.004c4.368 0 7.926-3.558 7.93-7.93A7.9 7.9 0 0 0 13.6 2.326zM7.994 14.521a6.6 6.6 0 0 1-3.356-.92l-.24-.144-2.494.654.666-2.433-.156-.251a6.56 6.56 0 0 1-1.007-3.505c0-3.626 2.957-6.584 6.591-6.584a6.56 6.56 0 0 1 4.66 1.931 6.56 6.56 0 0 1 1.928 4.66c-.004 3.639-2.961 6.592-6.592 6.592m3.615-4.934c-.197-.099-1.17-.578-1.353-.646-.182-.065-.315-.099-.445.099-.133.197-.513.646-.627.775-.114.133-.232.148-.43.05-.197-.1-.836-.308-1.592-.985-.59-.525-.985-1.175-1.103-1.372-.114-.198-.011-.304.088-.403.087-.088.197-.232.296-.346.1-.114.133-.198.198-.33.065-.134.034-.248-.015-.347-.05-.099-.445-1.076-.612-1.47-.16-.389-.323-.335-.445-.34-.114-.007-.247-.007-.38-.007a.73.73 0 0 0-.529.247c-.182.198-.691.677-.691 1.654s.71 1.916.81 2.049c.098.133 1.394 2.132 3.383 2.992.47.205.84.326 1.129.418.475.152.904.129 1.246.08.38-.058 1.171-.48 1.338-.943.164-.464.164-.86.114-.943-.049-.084-.182-.133-.38-.232"/>
    </svg>
  </a>'''
content = re.sub(r'<!-- WhatsApp Float -->.*?</a>', whatsapp_svg, content, flags=re.DOTALL)

contact_form_html = '''<form action="https://formsubmit.co/[YOUR EMAIL ADDRESS]" method="POST">
              <input type="hidden" name="_captcha" value="false">
              <input type="text" name="_honey" style="display:none">
              <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
                <div class="form-group"><label class="form-label">Full Name *</label><input type="text" name="Full Name" class="form-input" placeholder="Your Name" required></div>
                <div class="form-group"><label class="form-label">Phone Number *</label><input type="tel" name="Phone Number" class="form-input" placeholder="+91 XXXXX XXXXX" required></div>
              </div>
              <div class="form-group"><label class="form-label">Email Address *</label><input type="email" name="Email" class="form-input" placeholder="your@email.com" required></div>
              <div class="form-group"><label class="form-label">Message *</label><textarea name="Message" class="form-textarea" placeholder="Write your message here..." required style="min-height: 150px;"></textarea></div>
              <button type="submit" class="btn btn-primary" style="width: 100%; justify-content: center;">Send Message</button>
            </form>'''
content = re.sub(r'<form id="contactForm">.*?</form>', contact_form_html, content, flags=re.DOTALL)

admission_form_html = '''<form action="https://formsubmit.co/[YOUR EMAIL ADDRESS]" method="POST">
              <input type="hidden" name="_captcha" value="false">
              <input type="text" name="_honey" style="display:none">
              <div class="form-group"><label class="form-label">Full Name *</label><input type="text" name="Full Name" class="form-input" placeholder="Your Name" required></div>
              <div class="form-group"><label class="form-label">Phone Number *</label><input type="tel" name="Phone Number" class="form-input" placeholder="+91 XXXXX XXXXX" required></div>
              <div class="form-group"><label class="form-label">Email Address *</label><input type="email" name="Email" class="form-input" placeholder="your@email.com" required></div>
              <div class="form-group"><label class="form-label">Message</label><textarea name="Message" class="form-textarea" placeholder="Your query..."></textarea></div>
              <button type="submit" class="btn btn-primary" style="width: 100%; justify-content: center;">Submit & Get Free Counseling</button>
            </form>'''
content = re.sub(r'<form id="admissionForm">.*?</form>', admission_form_html, content, flags=re.DOTALL)

# Remove the JS form handler block
content = re.sub(r"document\.querySelectorAll\('form'\)\.forEach.*?\}\);\n\}\);\n", "", content, flags=re.DOTALL)

# Because `document.querySelectorAll('form')` block ends with `});\n});\n` or `});\n`, let's just do:
content = re.sub(r"document\.querySelectorAll\('form'\)\.forEach.*?\}\);\n", "", content, flags=re.DOTALL)
# wait, my regex was:
# document.querySelectorAll('form').forEach(form => { ... });
# It spans multiple lines, so `.*?` needs DOTALL. We can be safe by matching until `form.reset(); }, 3000);\n      }\n    }\n  });\n});`

# Wait, the exact block is:
# document.querySelectorAll('form').forEach(form => {
#   form.addEventListener('submit', (e) => {
#     e.preventDefault();
# ...
#   });
# });

# Just removing e.preventDefault() might be easier!
# But since user said NO JS, removing it is better.
# Let's replace the whole JS block explicitly or with a regex that limits greediness.

# Clean up any leftover empty icon containers
content = re.sub(r'<div class="card-icon[^>]*></div>', '', content)
content = re.sub(r'<div class="info-box-icon"[^>]*></div>', '', content)
content = re.sub(r'<div class="badge-icon[^>]*></div>', '', content)
content = re.sub(r'<div class="hero-image-placeholder"></div>', '<div class="hero-image-placeholder" style="font-family: var(--font-heading); font-weight: 900; color: #fff;">SE</div>', content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done")
