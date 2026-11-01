"""录制抓包用：像浏览器一样请求一个网址。用法：python fetch.py 网址 [POST数据] [CA证书]"""
import ssl
import sys
import urllib.request

url = sys.argv[1]
data = sys.argv[2].encode() if len(sys.argv) > 2 else None
ctx = ssl.create_default_context(cafile=sys.argv[3]) if len(sys.argv) > 3 else None
req = urllib.request.Request(url, data=data, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/141.0"})
opener = urllib.request.build_opener(urllib.request.ProxyHandler({}), urllib.request.HTTPSHandler(context=ctx))
with opener.open(req, timeout=5) as r:
    print(r.status, len(r.read()))
