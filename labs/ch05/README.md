# 第 5 章 VLAN 与无线局域网：实验文件

本章实验的完整步骤见教材[第 5 章“本章实验”](https://mingzifu9.github.io/computer-network/chapters/05-vlan-wlan/)。

| 实验 | 用到的文件 |
|---|---|
| 实验 5-1 ★ 按部门划分 VLAN | Packet Tracer |
| 实验 5-2 ★ 两台交换机之间的 Trunk，看 802.1Q 标签 | `lab5_2_vlan_count.py`、`../data/pcap/vlan_trunk.pcap`、`../data/pcap/web_visit.pcap`；Packet Tracer、Wireshark |
| 实验 5-3 ☆ 设置无线路由器 | Packet Tracer |

## 程序说明

| 文件 | 作用 |
|---|---|
| `lab5_2_vlan_count.py` | 实验 5-2：数一数 Trunk 链路上每个 VLAN 各有几帧 |

运行方法：用 Thonny 打开后点“运行”，或在命令提示符中进入本文件夹后执行 `python 文件名.py`。程序只用 Python 标准库，不需要安装第三方库。
