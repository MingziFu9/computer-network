# 实验 8-1：从抓包文件中找出 DHCP 的四个报文（《计算机网络》第 8 章）
# 只用 Python 自带功能。运行前确认 ../data/pcap/dhcp_arp.pcap 存在
import struct

NAMES = {1: "Discover 发现", 2: "Offer 提供", 3: "Request 请求", 5: "ACK 确认"}
data = open("../data/pcap/dhcp_arp.pcap", "rb").read()
pos, no = 24, 0
while pos < len(data):
    caplen = struct.unpack("<I", data[pos + 8:pos + 12])[0]
    f = data[pos + 16:pos + 16 + caplen]
    no += 1
    if f[12:14] == b"\x08\x00" and f[23] == 17 and f[36:38] in (b"\x00\x43", b"\x00\x44"):   # IPv4、UDP、端口 67/68
        your_ip = ".".join(str(b) for b in f[58:62])         # DHCP 报文里“分给你的地址”
        mtype = f[f.index(b"\x35\x01", 282) + 2]              # 选项 53：DHCP 报文类型
        print(f"第 {no} 帧  {NAMES.get(mtype, mtype)}  分配地址 {your_ip}")
    pos += 16 + caplen
