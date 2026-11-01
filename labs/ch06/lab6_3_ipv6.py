# 实验 6-3：IPv6 地址的完整写法与缩写（《计算机网络》第 6 章）
import ipaddress

for s in ["2001:0db8:0000:0000:0000:ff00:0042:8329",    # ← 改这里：换成你电脑上的 IPv6 地址
          "fe80:0000:0000:0000:02e0:4cff:fe68:010a",
          "0000:0000:0000:0000:0000:0000:0000:0001"]:
    a = ipaddress.ip_address(s)
    print("完整：", a.exploded)
    tag = "（链路本地地址）" if a.is_link_local else "（环回地址）" if a.is_loopback else ""
    print("缩写：", a.compressed, tag)
