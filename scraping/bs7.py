import requests
from bs4 import BeautifulSoup
#フォルダ操作モジュール
from pathlib import Path
#url走査モジュール
import urllib
#時間走査モジュール
import time

load_url = 'https://joytas.net/kaba/'
res = requests.get(load_url)
res.encoding = res.apparent_encoding
soup=BeautifulSoup(res.text,'html.parser')

#Pathオブジェクト作成
out_folder=Path('downloaded')
#Pathオブジェクトがdownloadedフォルダを作成
#(downloadedという名のフォルダが既にあってもエラーにしない)
out_folder.mkdir(exist_ok=True)

#img要素を全部取得
imgs = soup.select('img')

#ファイル書き込み
for img in imgs:
    src = img.get('src')

    #画像相対URLを絶対URLに変換
    img_url = urllib.parse.urljoin(load_url,src)

    #get通信で画像をロード
    loaded_img=requests.get(img_url)

    #ファイル名取得
    file_name=img.get('src').split('/')[-1]

    #保存画像パス
    out_path=out_folder.joinpath(file_name)

    #weはバイナリ書き込み
    with open(out_path,"wb")as file:
        #contentはバイナリデータ
        file.write(loaded_img.content)

    #DOS攻撃にならないように時間（１秒）をあける
    time.sleep(1)
