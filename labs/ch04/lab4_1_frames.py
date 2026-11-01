# 实验 4-1：用 Python 读出抓包文件里每一帧的 MAC 地址和类型（《计算机网络》第 4 章）
# 只用 Python 自带功能。运行前确认 ../data/pcap/web_visit.pcap 存在
import struct

def mac(b):                                   # 6 个字节 → "00:e0:4c:68:01:0a"
    return ":".join(f"{x:02x}" for x in b)

TYPES = {0x0800: "IPv4", 0x0806: "ARP", 0x86DD: "IPv6", 0x8100: "VLAN 标签"}
data = open("../data/pcap/web_visit.pcap", "rb").read()
pos, n = 24, 0                                # 跳过 24 字节的文件头
while pos < len(data) and n < 5:              # ← 改这里：显示前几帧
    caplen = struct.unpack("<I", data[pos + 8:pos + 12])[0]   # 这一帧有多少字节
    frame = data[pos + 16:pos + 16 + caplen]                    # 帧的内容
    t = struct.unpack("!H", frame[12:14])[0]                    # 第 13、14 字节是类型
    n += 1
    print(n, "目的", mac(frame[0:6]), "源", mac(frame[6:12]), "类型", f"0x{t:04x}", TYPES.get(t, "?"), caplen, "字节")
    pos += 16 + caplen
