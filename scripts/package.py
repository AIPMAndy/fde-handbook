"""Validate the static source and build the download package and print HTML."""
from pathlib import Path
import re,zipfile
R=Path(__file__).resolve().parents[1]
html=(R/'index.html').read_text(encoding='utf-8')
ids=re.findall(r'id="chapter-(\d+)"',html)
assert ids==[f'{i:02d}' for i in range(1,25)]
assert all((R/'chapters'/f'{x}.md').is_file() for x in ids)
templates=re.findall(r'href="templates/([^"]+)"',html)
assert len(templates)==len(set(templates))==13
for name in templates:assert (R/'templates'/name).is_file(),name
assert all(x in html for x in ['AIPMAndy','https://metaver.vip/','https://www.a6no1.cn/'])
(R/'downloads').mkdir(exist_ok=True)
with zipfile.ZipFile(R/'downloads'/'templates.zip','w',zipfile.ZIP_DEFLATED) as z:
 for name in templates:z.write(R/'templates'/name,'templates/'+name)
lessons=re.findall(r'<details class="card lesson"[^>]*>(.*?)</details>',html,re.S)
def clean(s):
 s=re.sub(r'<button\b[^>]*>.*?</button>','',s,flags=re.S)
 s=re.sub(r'<label class="check">.*?</label>','',s,flags=re.S)
 s=re.sub(r'<summary>','<h2>',s).replace('</summary>','</h2>')
 s=re.sub(r'<details\b[^>]*>','<div>',s).replace('</details>','</div>')
 return s
def section(name):
 return re.search(r'<section id="'+name+r'">(.*?)</section>',html,re.S).group(1)
css='@page{size:A4;margin:17mm 18mm 18mm}body{font:11pt/1.55 "Noto Sans CJK SC",sans-serif;color:#172126}a{color:#17614e;overflow-wrap:anywhere}h1{font-size:32pt}h2{font-size:21pt;line-height:1.3}h3{font-size:13pt}p{margin:2mm 0}.sheet{break-before:page}.prompt{border-left:3px solid #17614e;background:#f1f5f1;padding:3mm}.tag{font-size:9pt;color:#17614e;padding:0 4px}.small{font-size:9pt}pre{white-space:pre-wrap;overflow-wrap:anywhere}'
cover='<h1>FDE 保姆级攻略</h1><p>从需求发现到可验收的 AI 系统</p><p>24 章 · 5 个教学案例 · 30 天学习计划 · 12 周交付训练</p><p>AI 酋长 Andy · 微信 AIPMAndy · <a href="https://metaver.vip/">个人官网</a> · <a href="https://www.a6no1.cn/">星觉科技</a></p><p>独立原创，非官方教材；模拟案例不是生产结果。</p><h2>目录</h2>'
toc=[]
for i,s in zip(ids,lessons):
 title=re.search(r'</span>([^<]+)<span class="tag">',s).group(1)
 toc.append(f'<p><a href="#p{i}">{i} {title}</a></p>')
body=cover+''.join(toc)+''.join(f'<section class="sheet" id="p{i}">{clean(s)}</section>' for i,s in zip(ids,lessons))
for name in ['cases','plan','resources']:
 body+='<section class="sheet">'+clean(section(name))+'</section>'
(R/'docs'/'print.html').write_text('<!doctype html><html lang="zh-CN"><meta charset="utf-8"><style>'+css+'</style><body>'+body+'</body></html>',encoding='utf-8')
print(f'Validated {len(ids)} chapters, {len(templates)} templates; built ZIP and print HTML.')
