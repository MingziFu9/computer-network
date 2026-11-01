"""生成 vlan_trunk.pcap：两台交换机之间 Trunk 链路上带 802.1Q 标签的帧（第 5 章实验 5-2）。
设计部（VLAN 10）和财务部（VLAN 20）各有一台电脑 ping 另一层楼的同事，每个帧都带上所属 VLAN 的标签。
用法：python make_vlan_pcap.py 输出文件"""
import sys

from scapy.all import ARP, Dot1Q, Ether, ICMP, IP, wrpcap

pkts = []
t = 1761960000.0
pcs = [  # VLAN, 源 MAC, 源 IP, 目的 MAC, 目的 IP
    (10, "00:e0:4c:10:00:11", "192.168.10.11", "00:e0:4c:10:00:21", "192.168.10.21"),
    (20, "00:e0:4c:20:00:11", "192.168.20.11", "00:e0:4c:20:00:21", "192.168.20.21"),
]
for vid, smac, sip, dmac, dip in pcs:
    req = Ether(src=smac, dst="ff:ff:ff:ff:ff:ff") / Dot1Q(vlan=vid) / ARP(op=1, hwsrc=smac, psrc=sip, pdst=dip)
    rep = Ether(src=dmac, dst=smac) / Dot1Q(vlan=vid) / ARP(op=2, hwsrc=dmac, psrc=dip, hwdst=smac, pdst=sip)
    for p in (req, rep):
        p.time = t; t += 0.0004; pkts.append(p)
    for seq in (1, 2):
        e = Ether(src=smac, dst=dmac) / Dot1Q(vlan=vid) / IP(src=sip, dst=dip, ttl=64) / ICMP(type=8, id=0x1a2b, seq=seq) / (b"abcdefghijklmnopqrstuvwabcdefghi")
        r = Ether(src=dmac, dst=smac) / Dot1Q(vlan=vid) / IP(src=dip, dst=sip, ttl=64) / ICMP(type=0, id=0x1a2b, seq=seq) / (b"abcdefghijklmnopqrstuvwabcdefghi")
        e.time = t; t += 0.0006; r.time = t; t += 0.3
        pkts += [e, r]
    t += 0.5
wrpcap(sys.argv[1], pkts)
print("已生成", sys.argv[1], len(pkts), "个帧")
