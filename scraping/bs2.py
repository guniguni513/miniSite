import requests
from bs4 import BeautifulSoup

res = requests.get('https://joytas.net/kaba/')
res.encoding=res.apparent_encoding
#第１引数にhtml文字列、第２引数にパーサーを指定する。今回は追加ライブラリ不要な'html.parser'を指定
soup = BeautifulSoup(res.text,'html.parser')

#BeautifulSoupオブジェクトをprintにそのまま渡すと全文を表示する
#print(soup)

#タグで要素取得
ele = soup.find('title')#<title>コビトカバ</title>
#要素のtextコンテントを表示
print(ele.text)#コビトカバ
