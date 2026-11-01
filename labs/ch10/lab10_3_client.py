# 实验 10-3 第三档：用程序发一个 HTTP 请求，看看响应长什么样
import http.client                       # Python 自带的 HTTP 客户端

host = "127.0.0.1"                       # ← 改这里：服务器地址（本机就是 127.0.0.1）
conn = http.client.HTTPConnection(host, 8000, timeout=5)   # 连接服务器的 8000 端口（TCP）
conn.request("GET", "/index.html")       # 发出请求：方法 GET，路径 /index.html  ← 可改成不存在的路径
resp = conn.getresponse()                # 读取响应

print("状态行：", f"HTTP/{resp.version / 10}", resp.status, resp.reason)   # version 10 即 HTTP/1.0
for name, value in resp.getheaders():    # 逐行打印响应头
    print(f"  {name}: {value}")
body = resp.read().decode("utf-8")       # 读出网页内容（字节转成文字）
print("网页内容前 60 个字符：", body[:60].replace("\n", " "))
conn.close()
