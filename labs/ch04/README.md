# 第 4 章 数据链路层与以太网交换：实验文件

本章实验的完整步骤见教材[第 4 章“本章实验”](https://mingzifu9.github.io/computer-network/chapters/04-datalink/)。

| 实验 | 用到的文件 |
|---|---|
| 实验 4-1 ★ 在抓包里看以太网帧 | `lab4_1_frames.py`、`../data/pcap/vlan_trunk.pcap`、`../data/pcap/web_visit.pcap`；Wireshark |
| 实验 4-2 ★ Packet Tracer 第一次组网 | Packet Tracer |
| 实验 4-3 ☆ 用模拟模式看帧怎么走 | Packet Tracer |

## 程序说明

| 文件 | 作用 |
|---|---|
| `crc_demo.py` | 4.1.3 节示例：改动一个比特，CRC 校验值就完全不同 |
| `lab4_1_frames.py` | 实验 4-1：用 Python 读出抓包文件里每一帧的 MAC 地址和类型 |

运行方法：用 Thonny 打开后点“运行”，或在命令提示符中进入本文件夹后执行 `python 文件名.py`。程序只用 Python 标准库，不需要安装第三方库。
