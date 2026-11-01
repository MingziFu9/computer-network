# 实验 12-3：网络巡检小工具——批量 ping 一组地址，检查网站能否打开
import platform, subprocess, urllib.request     # 系统信息、运行命令、访问网页
from datetime import datetime

hosts = {"本机": "127.0.0.1", "不存在的设备": "10.255.255.1"}   # ← 改这里：换成网关、服务器等的地址
sites = ["http://127.0.0.1:8000/", "http://127.0.0.1:8001/"]  # ← 改这里：要检查的网站
flag = "-n" if platform.system() == "Windows" else "-c"       # Windows 的 ping 用 -n 指定次数


def ping_ok(ip):
    r = subprocess.run(["ping", flag, "1", ip], capture_output=True)   # ping 一次，收集输出
    return r.returncode == 0 and b"TTL=" in r.stdout.upper()           # 收到带 TTL 的回复才算通


def web_status(url):
    try:
        with urllib.request.urlopen(url, timeout=3) as resp:   # 像浏览器一样请求网页
            return f"正常（状态码 {resp.status}）"
    except Exception as e:                                     # 连不上、超时、404 等都会到这里
        return "异常：" + type(e).__name__


print("网络巡检报告", datetime.now().strftime("%Y-%m-%d %H:%M"))
for name, ip in hosts.items():
    print(f"  [ping] {name}  {ip}  {'正常' if ping_ok(ip) else '不通'}")
for url in sites:
    print(f"  [网站] {url}  {web_status(url)}")
