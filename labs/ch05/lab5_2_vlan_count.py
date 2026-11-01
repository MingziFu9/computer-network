# 实验 5-2：数一数 Trunk 链路上每个 VLAN 各有几帧（《计算机网络》第 5 章）
# 只用 Python 自带功能。运行前确认 ../data/pcap/vlan_trunk.pcap 存在
import struct

data = open("../data/pcap/vlan_trunk.pcap", "rb").read()
count = {}                                     # VLAN 号 → 帧数
pos = 24                                       # 跳过 24 字节的文件头
while pos < len(data):
    caplen = struct.unpack("<I", data[pos + 8:pos + 12])[0]
    frame = data[pos + 16:pos + 16 + caplen]
    if frame[12:14] == b"\x81\x00":            # 类型位置是 0x8100：带 802.1Q 标签
        vid = struct.unpack("!H", frame[14:16])[0] & 0x0FFF   # 取低 12 位：VLAN 号
        count[vid] = count.get(vid, 0) + 1
    pos += 16 + caplen
for vid, n in sorted(count.items()):
    print(f"VLAN {vid}: {n} 帧")
