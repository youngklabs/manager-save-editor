from pathlib import Path
from html import escape
import json
import math
root=Path(__file__).resolve().parent
T={
'ko':{'nav':['MSE 소개','주요 사용법','업데이트 정보','개인정보처리방침'],'title':'당신의 세이브,<br><em>당신의 이야기.</em>','lead':'Football Manager Mobile 2027의 세이브를 더 자유롭게. 선수부터 구단까지, 당신만의 축구 세계를 만들어 보세요.','guide':'사용법 보기','download':'Google Play 출시 준비 중','qr':'다운로드 QR 준비 중','features':'이것도 할 수 있다고?','features_sub':'선수 한 명에서 시작해, 당신의 축구 세계 전체까지. MSE에서 만날 수 있는 가능성을 살펴보세요.','names':['환생 선수 찾기','실제 계약 성사 금액 찾기','히든 능력치 수정','선수 이적','구단 스왑'],'desc':['새롭게 등장한 선수를 살펴볼 수 있는 기능','계약과 이적에 관련된 금액을 살펴볼 수 있는 기능','선수의 숨겨진 능력치를 확인하고 수정하는 기능','선수의 소속을 변경하는 기능','구단을 바꾸는 기능'],'placeholder':'스크린샷 및 상세 설명 준비 중','wiki_title':'주요 사용법','wiki_sub':'메뉴별 자세한 사용법을 준비하고 있습니다.','select':'목차','topics':['시작하기','세이브 열기와 저장','선수 검색과 필터','선수 정보와 히든 수정','환생 선수 찾기','선수 이적','구단과 스왑','스탭 · 국가 · 대회','그래픽 관리','설정'],'draft':'이 항목의 스크린샷과 단계별 설명은 앱 완성 후 추가됩니다.','backup':'저장 시 원본 세이브 파일이 수정됩니다. 편집하기 전에 반드시 별도로 백업하세요.','updates':'업데이트 정보','updates_sub':'새 버전이 배포될 때마다 변경사항을 이곳에 기록합니다.','empty':'아직 공개된 업데이트 기록이 없습니다.','emptydesc':'첫 배포 이후 새 버전이 나오면 날짜와 변경 내용을 확인할 수 있습니다.','footer':'비공식 앱입니다. 게임 제작사 및 배급사와 관계가 없습니다.','contact':'문의','next':'사용법 보기','label':'FMM27 전용'},
'en':{'nav':['About MSE','User guide','Updates','Privacy policy'],'title':'Your save.<br><em>Your story.</em>','lead':'Make more of your Football Manager Mobile 2027 save. From players to clubs, shape your own football world.','guide':'View the guide','download':'Coming soon to Google Play','qr':'Download QR coming soon','features':'Wait, you can do that too?','features_sub':'Start with one player. Reimagine your whole football world. Explore what MSE is being built to do.','names':['Find regenerated players','Find actual deal amounts','Edit hidden attributes','Transfer players','Swap clubs'],'desc':['Explore newly regenerated players','Explore amounts associated with contracts and transfers','View and edit hidden player attributes','Change a player’s club','Swap clubs'],'placeholder':'Screenshot and detailed explanation coming soon','wiki_title':'User guide','wiki_sub':'Detailed instructions for each area are being prepared.','select':'Contents','topics':['Getting started','Opening and saving','Player search and filters','Player details and hidden attributes','Finding regenerated players','Player transfers','Clubs and swapping','Staff · nations · competitions','Graphics','Settings'],'draft':'Screenshots and step-by-step instructions will be added when the app is ready.','backup':'Saving changes the original save file. Keep a separate backup before editing.','updates':'Updates','updates_sub':'Changes for each new release will be recorded here.','empty':'No public release notes yet.','emptydesc':'After the first release, dates and changes for new versions will appear here.','footer':'An unofficial app, not affiliated with the game’s developer or publisher.','contact':'Contact','next':'Open the guide','label':'FOR FMM27'} }
REL={
'ko':[{'v':'1.0.1','date':'2026-11-21','intro':'첫 릴리스(0.1.0) 이후 바뀐 내용입니다.','groups':[
('새 기능',[
('환생 선수 원본 표시 개편','세이브 슬롯 번호가 한 세계 안에서 바뀌지 않는다는 점을 이용해, 세계별로 슬롯의 처음 주인을 기록합니다. 환생 선수 상세 헤더에 원본 선수의 이름·생년·국적이 표시되고, 편집한 세이브에서도 이어집니다. 기기에서 게임 DB를 읽는 과정(Shizuku)은 더 이상 필요 없습니다. 같은 세계의 이전 세이브를 열어 두면 기록이 더 정확해집니다.'),
('핀치 확대','두 손가락으로 1~3배 확대하고, 확대한 뒤에는 한 손가락으로 끌어 이동합니다. 가장자리에서는 목록 스크롤로 넘어갑니다.'),
('입력 편의','주급·금액 입력칸에서 누른 위치에 커서가 들어갑니다. −/+ 단추를 꾹 누르면 반복되고, 작업 중 화면이 꺼지지 않으며, 목록으로 돌아오면 스크롤 위치를 기억합니다.'),
('대표팀 로고는 국기로','성인·여자·U21 대표팀의 목록·상세·헤더 로고를 국가 국기로 표시합니다. 이 팀의 로고 등록·수정·삭제는 막았습니다.'),
('구단 선수단 탭에 얼굴','선수 이름 옆에 선수 검색 결과와 같은 작은 얼굴이 나옵니다.'),
('영입명단 버튼 위치','[현재 목록 전부 영입명단 추가] 단추를 "결과 N명" 바로 옆으로 옮겼습니다. 영어에서도 줄어들지 않고, 자리가 모자라면 아랫줄로 내려갑니다.')]),
('속도 개선',[
('스크롤·검색·상세','스크롤 렌더링 병목을 줄이고, 선수 검색 결과를 캐시하고(폰 프로파일 빌드 기준 560ms → 23ms), 선수 상세의 재계산을 줄였습니다. 실제 기기의 릴리스 빌드 체감은 기기마다 다를 수 있습니다.')]),
('오류 수정',[
('열리지 않던 세이브','26 때 시작한 일부 세이브가 invalid gameVersion2: unknown 으로 열리지 않던 문제를 고쳤습니다.'),
('영입명단(.lst) 불러오기','게임이 한글·밑줄이 든 파일 이름을 거부했습니다. 내보내기 이름을 영문·숫자로 제한하고 기본 이름을 Shortlist1 로 바꿨습니다.'),
('그래픽 연동 분석 실패','로고 묶음의 폴더 배치가 다른 경우와 목차 꼬리 형식이 다른 경우를 읽도록 고쳤습니다. 합성 파일로만 확인했으니 계속 실패하면 알려 주세요.'),
('입력칸 커서','커서가 항상 끝에 고정되던 문제를 고쳤습니다.')]),
('통칭 한글화',[
('표기 사전 개선','위키 검색 건수와 페이지뷰를 합산해 다시 판정한 322건과 권역 규칙 7건(Victor·Ayew·Tariq·Kasper·Fernandes·Mangas·Rafael)을 반영했습니다. 이미 한글화한 세이브는 설정 › 한글화에서 "전부 다시" 적용을 권장합니다.')]),
('알려진 한계',[
('','환생 원본 기록은 PA 편집 후 환생, 아주 오래 진행한 세이브를 시험하지 못했습니다. 핀치 확대는 실기기 확인이 일부만 됐습니다. 저장은 원본 파일을 덮어쓰므로 반드시 백업 후 사용하세요.')])]}],
'en':[{'v':'1.0.1','date':'2026-11-21','intro':'What changed since the first release (0.1.0).','groups':[
('New',[
('Regen original player, reworked','A save’s slot numbers stay fixed within one world, so the app now keeps a per-world record of each slot’s first owner. A regen’s detail header shows the original player’s name, birth year and nationality, and it carries over to edited saves. Reading the game database on the device (Shizuku) is no longer needed. Opening earlier saves of the same world makes the record more accurate.'),
('Pinch to zoom','Zoom 1x–3x with two fingers, then drag with one finger to move around. At the edge, dragging hands over to list scrolling.'),
('Input improvements','The cursor goes where you tap in wage and money fields. Hold −/+ to repeat, the screen stays awake while you work, and lists remember their scroll position.'),
('National team logos show the flag','Senior, women’s and U21 teams show their flag in lists, details and headers. Logo upload, edit and delete are disabled for these teams.'),
('Faces in the club squad tab','The same small face as in player search results now appears next to each name.'),
('Shortlist button placement','“Add all in current list to shortlist” now sits right next to “N results”. It no longer shrinks in English and drops to the next line if space runs out.')]),
('Performance',[
('Scrolling, search and details','Removed a scroll-rendering bottleneck, cached player search results (560 ms → 23 ms in a phone profile build), and reduced recalculation on the player detail screen. Real-world feel on release builds varies by device.')]),
('Fixes',[
('Saves that would not open','Some saves started in FMM26 failed with invalid gameVersion2: unknown. They open now.'),
('Shortlist (.lst) import','The game rejects file names with certain characters. Export names are now limited to letters and digits, default Shortlist1.'),
('Graphics link analysis failed','Now reads logo packs with a different folder layout and packs whose index tail uses a different format. Verified with synthetic files only. Please report if it still fails.'),
('Input field cursor','Fixed the cursor being stuck at the end.')]),
('Known limitations',[
('','Regen records are untested for editing PA then regenerating, and for very long careers. Pinch zoom has only been partly checked on a real device. Saving overwrites the original file, so back it up first.')])]}]}
ids=['getting-started','save','search','player','regens','transfers','clubs','world','graphics','settings']
def page(lang,section,content):
 t=T[lang];other='en' if lang=='ko' else 'ko'; paths=['index.html','guide.html','updates.html','../privacy/'+lang+'.html']; nav=''.join(f'<a {"aria-current=page" if i==section else ""} href="{p}">{escape(x)}</a>' for i,(x,p) in enumerate(zip(t['nav'],paths)))
 return f'''<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#0d1824"><title>{escape(t['nav'][section])} | Manager Save Editor</title><link rel="icon" href="../assets/icon.png"><link rel="stylesheet" href="../site.css"><link rel="stylesheet" href="../pages.css"><link rel="stylesheet" href="../night.css"><script src="../pages.js?v=night" defer></script></head><body><header class="header"><a class="brand" href="index.html"><img src="../assets/icon.png" alt=""><span>MSE <small>MANAGER SAVE EDITOR</small></span></a><nav id="nav" aria-label="Navigation">{nav}</nav><div class="controls"><a class="language" href="../{other}/{['index.html','guide.html','updates.html'][section]}" aria-label="{'Switch to English' if lang=='ko' else '한국어로 변경'}">{'EN' if lang=='ko' else '한국어'}</a><button class="menu" id="menu" type="button" aria-expanded="false" aria-controls="nav" aria-label="{'메뉴' if lang=='ko' else 'Menu'}"><span></span><span></span></button></div></header>{content}<footer><a class="brand" href="index.html"><img src="../assets/icon.png" alt=""><span>MSE <small>MANAGER SAVE EDITOR</small></span></a><p>{t['footer']}</p><div><a href="../privacy/{lang}.html">{t['nav'][3]}</a><a href="mailto:young.k.labs@gmail.com">{t['contact']}: young.k.labs@gmail.com</a></div><small>© MANAGER SAVE EDITOR</small></footer></body></html>'''
def annotation(number):
 marks=json.loads((root/'annotations.json').read_text(encoding='utf-8')).get(str(number),[])
 if not marks:return ''
 paths=[]
 for cx,cy,rx,ry in marks:
  for pass_no in range(2):
   points=[]
   for j in range(73):
    angle=j/72*math.tau
    wobble=1+0.018*math.sin(angle*5+pass_no)+0.012*math.cos(angle*3)
    x=cx+rx*wobble*math.cos(angle)+pass_no*3
    y=cy+ry*wobble*math.sin(angle)+pass_no*2
    points.append(f'{x:.1f},{y:.1f}')
   paths.append(f'<path d="M {" L ".join(points)}" fill="none" stroke="#ff4545" stroke-width="{5 if pass_no==0 else 2.5}" opacity="{.95 if pass_no==0 else .65}" stroke-linecap="round" stroke-linejoin="round"/>')
 return '<svg class="pencil-mark" viewBox="0 0 2280 1080" aria-hidden="true">'+''.join(paths)+'</svg>'
for lang,t in T.items():
 d=root/lang;d.mkdir(exist_ok=True)
 stories=json.loads((root/'features.json').read_text(encoding='utf-8'))[lang]
 features=''.join(f'''<article class="discovery feature-story" id="feature-{i+1}"><div class="discovery-copy"><p class="discovery-kicker">{escape(name)}</p><h3>{escape(headline)}</h3><p>{escape(description)}</p><a href="guide.html#{anchor}">{'관련 사용법' if lang=='ko' else 'Related guide'}</a></div><figure class="real-screen"><a href="../assets/screens/{filename}" class="screenshot-link"><img src="../assets/screens/{filename}" alt="{escape(caption)}" loading="lazy" width="2280" height="1080">{annotation(i+1)}</a><figcaption>{escape(caption)}<span>{'눌러서 크게 보기' if lang=='ko' else 'Select to enlarge'}</span></figcaption></figure></article>''' for i,(headline,name,description,filename,caption,anchor) in enumerate(stories))

 groups = [
  ('스카우팅', 'Scouting', [2, 3, 4, 12, 13]),
  ('선수 편집', 'Player editing', [1, 5, 6, 7, 8]),
  ('구단 운영', 'Club management', [9, 10, 11]),
  ('그래픽·한글화', 'Graphics', [14, 15]),
 ]
 feature_nav = ''.join(
  f'<div class="feature-group"><h3>{ko if lang == "ko" else en}</h3>'
  + ''.join(f'<a href="#feature-{n}">{escape(stories[n-1][1])}</a>' for n in numbers if n <= len(stories))
  + '</div>' for ko, en, numbers in groups
 )
 title = '나만의 축구 세계를<br><em>만들어보세요.</em>' if lang == 'ko' else 'Create your own<br><em>football world.</em>'
 arena = '주요 기능 살펴보기' if lang == 'ko' else 'Explore features'
 lead = '선수를 찾고, 팀을 바꾸고, 새로운 이야기를 시작하세요.' if lang == 'ko' else 'Find players, change your team, and start a new story.'
 download_title = 'Google Play에서 만나보세요' if lang == 'ko' else 'Coming to Google Play'
 home=f'''<main>
 <section class="hero night-hero">
  <div class="hero-inner">
   <div class="hero-copy">
    <p class="kicker">FOOTBALL MANAGER MOBILE 2027</p>
    <h1>{title}</h1><p class="lead">{lead}</p>
    <div class="actions"><a class="button primary" href="#features">{arena}</a><a class="button ghost" href="guide.html">{t['guide']}</a></div>
   </div>
   <figure class="hero-shot">
    <a class="screenshot-link" href="../assets/screens/05_rating.png"><img src="../assets/screens/05_rating.png" width="2280" height="1080" fetchpriority="high" alt="{'선수 프로필과 포지션별 레이팅' if lang=='ko' else 'Player profile and position ratings'}"></a>
    <figcaption>{'선수 프로필과 포지션별 레이팅' if lang=='ko' else 'Player profile and position ratings'}</figcaption>
   </figure>
  </div>
 </section>
 <section class="section scout-section" id="features">
  <div class="section-heading"><h2>{'주요 기능' if lang=='ko' else 'Features'}</h2></div>
  <div class="scout-console">
   <nav class="scout-nav" aria-label="{'기능 선택' if lang=='ko' else 'Choose a feature'}">{feature_nav}</nav>
   <div class="discovery-list scout-reports">{features}</div>
  </div>
 </section>
 <section class="download-section">
  <div class="section download-inner"><div><h2>{download_title}</h2><p>{'출시 후 다운로드 링크와 QR 코드를 이곳에서 확인할 수 있습니다.' if lang=='ko' else 'The download link and QR code will appear here once the app is available.'}</p><span class="button ghost disabled" aria-disabled="true">{t['download']}</span></div><div class="qr-placeholder">{t['qr']}</div></div>
 </section>
 </main>'''

 (d/'index.html').write_text(page(lang,0,home),encoding='utf-8')
 nav=''.join(f'<a href="#{id}">{escape(name)}</a>' for id,name in zip(ids,t['topics']))
 articles=''.join(f'<article id="{id}" class="wiki-article"><h2>{escape(name)}</h2><p>{t["draft"]}</p>{f"<div class=\"warning\"><strong>{t['backup']}</strong></div>" if i==1 else ""}<div class="wiki-placeholder"><span>▧</span><small>{t["placeholder"]}</small></div></article>' for i,(id,name) in enumerate(zip(ids,t['topics'])))
 guide=f'''<main class="wiki-wrap"><div class="wiki-top"><h1>{t['wiki_title']}</h1><p>{t['wiki_sub']}</p></div><div class="wiki-layout"><aside class="wiki-nav"><strong>{t['select']}</strong><nav aria-label="{t['select']}">{nav}</nav></aside><div class="wiki-content">{articles}</div></div></main>'''
 (d/'guide.html').write_text(page(lang,1,guide),encoding='utf-8')
 def rel_html(r):
  g=''.join('<h3>'+escape(h)+'</h3><ul>'+''.join('<li>'+('<strong>'+escape(a)+'</strong> ' if a else '')+escape(b)+'</li>' for a,b in items)+'</ul>' for h,items in r['groups'])
  return f'<article class="release"><header><h2>{r["v"]}</h2><time>{r["date"]}</time></header><p>{escape(r["intro"])}</p>{g}</article>'
 updates=f'''<main class="updates-wrap"><h1>{t['updates']}</h1><p class="updates-lead">{t['updates_sub']}</p>{''.join(rel_html(r) for r in REL[lang])}</main>'''
 (d/'updates.html').write_text(page(lang,2,updates),encoding='utf-8')
(root/'index.html').write_text('''<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Manager Save Editor</title><script>const lang=new URLSearchParams(location.search).get('lang');location.replace((lang==='ko'||lang==='en'?lang:(navigator.language.toLowerCase().startsWith('ko')?'ko':'en'))+'/index.html')</script></head><body><a href="ko/index.html">한국어</a> · <a href="en/index.html">English</a></body></html>''',encoding='utf-8')
