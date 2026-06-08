import re

html_file = '/Users/anurag/Desktop/Edtech/singhania-education.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# We need to find the "Why Choose Us" section and replace its grid-3 block.
# Since the regex swallowed cards, the grid-3 block under "हम क्यों हैं सबसे बेहतर?" might be corrupted.
# Let's find it.

start_marker = '<h2 class="section-title">हम <span class="text-gradient">क्यों हैं सबसे बेहतर?</span></h2>'
# Find the next <div class="grid-3 stagger-children reveal"> after start_marker
start_idx = content.find(start_marker)
grid_start = content.find('<div class="grid-3 stagger-children reveal">', start_idx)
grid_end = content.find('</div>\n    </div>\n  </section>', grid_start) # This is the end of the container

correct_grid = """<div class="grid-3 stagger-children reveal">
        <div class="card-3d"><div class="card-3d-inner"><img src="feature_counseling_1780942221371.png" alt="Personalized Counseling" style="width:100%; height:180px; object-fit:cover; border-radius: var(--radius-md); margin-bottom: 1.5rem;"><h3>Personalized Counseling</h3><p>हर student को dedicated counselor मिलता है जो उसकी strengths, interests और budget के हिसाब से best college suggest करता है।</p></div></div>
        <div class="card-3d"><div class="card-3d-inner"><img src="feature_colleges_1780942234549.png" alt="500+ Top Colleges" style="width:100%; height:180px; object-fit:cover; border-radius: var(--radius-md); margin-bottom: 1.5rem;"><h3>500+ Top Colleges</h3><p>IITs, NITs, AIIMS, IIMs, NLUs से लेकर top private universities तक — हमारे पास 500+ verified partner colleges हैं।</p></div></div>
        <div class="card-3d"><div class="card-3d-inner"><img src="feature_support_1780942248813.png" alt="Complete Admission Support" style="width:100%; height:180px; object-fit:cover; border-radius: var(--radius-md); margin-bottom: 1.5rem;"><h3>Complete Admission Support</h3><p>Application form भरने से लेकर document verification, entrance exam preparation, counseling round support और final admission तक।</p></div></div>
        <div class="card-3d"><div class="card-3d-inner"><img src="feature_scholarship_1780942261477.png" alt="Scholarship Assistance" style="width:100%; height:180px; object-fit:cover; border-radius: var(--radius-md); margin-bottom: 1.5rem;"><h3>Scholarship Assistance</h3><p>हम eligible students को government और private scholarships दिलाने में मदद करते हैं। Merit-based, need-based scholarships।</p></div></div>
        <div class="card-3d"><div class="card-3d-inner"><img src="feature_loan_1780942273666.png" alt="Education Loan Help" style="width:100%; height:180px; object-fit:cover; border-radius: var(--radius-md); margin-bottom: 1.5rem;"><h3>Education Loan Help</h3><p>Top banks (SBI, HDFC, ICICI, Bank of Baroda) से education loan दिलाने में complete assistance।</p></div></div>
        <div class="card-3d"><div class="card-3d-inner"><img src="feature_network_1780942287211.png" alt="Pan-India Network" style="width:100%; height:180px; object-fit:cover; border-radius: var(--radius-md); margin-bottom: 1.5rem;"><h3>Pan-India Network</h3><p>Delhi, Mumbai, Bangalore, Chennai, Hyderabad, Kolkata, Pune, Jaipur, Lucknow सहित 25+ cities में हमारे offices हैं।</p></div></div>
      </div>"""

new_content = content[:grid_start] + correct_grid + content[grid_end:]

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Restored 6 cards.")
