import requests
from bs4 import BeautifulSoup

# 크롤링 해당 주소 붙이기
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)

# HTML을 BeautifulSoup 라이브러리 
soup = BeautifulSoup(data.text, 'html.parser')
# select를 이용해서, tr들을 불러오기
musics = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for music in musics:
    rankup = music.select_one('td.number').text.strip().split()[0]        # 문자열자르기
    title = music.select_one('td.info > a.title.ellipsis').text.strip()   # 공백제거
    artist = music.select_one('td.info > a.artist.ellipsis').text.strip() # 공백제거 

    print(rankup, title, artist)