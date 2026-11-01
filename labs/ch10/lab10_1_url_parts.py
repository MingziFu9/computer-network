# 实验 10-1 第三档：把一个网址拆成几部分
from urllib.parse import urlsplit, parse_qs   # Python 自带的网址处理工具

url = "https://www.xiaohe.com:443/news/list.html?page=2&type=design#top"   # ← 改这里，换成别的网址
p = urlsplit(url)                  # 按 URL 的规则拆开

print("协议   ：", p.scheme)       # https
print("主机名 ：", p.hostname)     # 要交给 DNS 查询的域名
print("端口   ：", p.port)         # 没写端口时为 None，表示用默认端口
print("路径   ：", p.path)         # 服务器上的哪个资源
print("查询   ：", parse_qs(p.query))   # ? 后面的参数，拆成字典
print("片段   ：", p.fragment)     # # 后面的部分，只在浏览器里用，不发给服务器
