import pyqrcode

s = "https://twitter.com/alee_n2"

url = pyqrcode.create(s)
url.svg("mytwitter.svg", scale=8)
