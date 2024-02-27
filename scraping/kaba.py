import requests

#指定urlにget通信
res = requests.get('http://joytas.net/kaba/')
#文字化け対策
res.encoding=res.apparent_encoding

print(res.text)
