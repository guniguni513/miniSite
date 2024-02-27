import requests
from bs4 import BeautifulSoup

res = requests.get('https://joytas.net/kaba/')
res.encoding=res.apparent_encoding
#html全体を取得
soup = BeautifulSoup(res.text,'html.parser')

#li要素の中のaを全部取得
links = soup.select('li a')

#ファイル書き込み
with open('zoo.txt','w',encoding='utf-8') as file:
    for link in links:
        file.write(f'{link.text}:{link.get("href")}\n')
