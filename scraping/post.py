import requests

#指定urlにpost通信
res = requests.post('https://joytas.net/php/calc.php',data={'x':10,'y':7})
#文字化け対策
res.encoding = res.apparent_encoding

print(res.text)
