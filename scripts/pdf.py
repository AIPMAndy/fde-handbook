from pathlib import Path
from playwright.sync_api import sync_playwright
R=Path(__file__).resolve().parents[1]
with sync_playwright() as p:
 browser=p.chromium.launch(args=['--no-sandbox'])
 page=browser.new_page()
 page.set_content((R/'docs/print.html').read_text(encoding='utf-8'))
 page.evaluate('document.fonts.ready')
 page.pdf(path=str(R/'downloads/fde-handbook.pdf'),print_background=True,prefer_css_page_size=True,display_header_footer=True,header_template='<span></span>',footer_template='<div style="font-size:8px;color:#68776e;width:100%;text-align:center">FDE 保姆级攻略 · <span class="pageNumber"></span> / <span class="totalPages"></span></div>')
 browser.close()
assert (R/'downloads/fde-handbook.pdf').read_bytes()[:4]==b'%PDF'
