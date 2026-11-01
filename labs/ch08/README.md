# 第 8 章 网络层的好帮手：ARP、ICMP、DHCP 与 NAT：实验文件

本章实验的完整步骤见教材[第 8 章“本章实验”](https://mingzifu9.github.io/computer-network/chapters/08-arp-dhcp-nat/)。

| 实验 | 用到的文件 |
|---|---|
| 实验 8-1 ★ 看 ARP 和 DHCP 的包 | `lab8_1_dhcp_steps.py`、`../data/pcap/dhcp_arp.pcap`；Wireshark |
| 实验 8-2 ★ 在 Packet Tracer 中配置 DHCP 和 NAT | Packet Tracer |
| 实验 8-3 ☆ 动手验证 TTL | —（按教材步骤操作） |

## 程序说明

| 文件 | 作用 |
|---|---|
| `lab8_1_dhcp_steps.py` | 实验 8-1：从抓包文件中找出 DHCP 的四个报文 |

运行方法：用 Thonny 打开后点“运行”，或在命令提示符中进入本文件夹后执行 `python 文件名.py`。程序只用 Python 标准库，不需要安装第三方库。
