import requests
from bs4 import BeautifulSoup

res = requests.get('https://joytas.net/kaba/')
res.encoding=res.apparent_encoding
#html全体を取得
soup = BeautifulSoup(res.text,'html.parser')

#print(soup)

#タグで要素取得
ele = soup.find('title')#<title>コビトカバ</title>
#要素のtextコンテントを表示
print(ele.text)#コビトカバ

#要素を結果セット(ResultSet)として取得
imgs = soup.find_all('img')
for img in imgs:
    #属性にアクセスするにはgetメソッドを使う
    print(img.get('src'))

#その他の要素の取得方法

#idを指定
div = soup.find(id = 'headerImageBox')

#classで取得
imgs = soup.select('.headerImage')
for img in imgs:
    print(img.get('src'))

tds = soup.select('tr td:first-child')
soup = BeautifulSoup(res.text,'html.parser')
for td in tds:
    print(td.text)
