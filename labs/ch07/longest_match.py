# 7.2.3 节示例：用最长前缀匹配查路由表（《计算机网络》第 7 章）
import ipaddress

table = [("192.168.8.0/26", "直接交付，接口 Gi0/0"),      # (目的网络, 怎么走)
         ("192.168.9.0/24", "下一跳 10.0.12.2"),
         ("192.168.9.128/25", "下一跳 10.0.13.2"),
         ("0.0.0.0/0", "下一跳 203.0.113.1（默认路由）")]
for dst in ["192.168.9.20", "192.168.9.200", "192.168.8.30", "114.114.114.114"]:   # ← 改这里
    ip = ipaddress.ip_address(dst)
    hits = [(ipaddress.ip_network(n), how) for n, how in table if ip in ipaddress.ip_network(n)]
    best = max(hits, key=lambda h: h[0].prefixlen)    # 前缀最长的那一条
    print(f"{dst:<16} 匹配 {len(hits)} 条，选 {best[0]}：{best[1]}")
