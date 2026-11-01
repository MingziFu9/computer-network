# 第 9 章 传输层：TCP 与 UDP：实验文件

本章实验的完整步骤见教材[第 9 章“本章实验”](https://mingzifu9.github.io/computer-network/chapters/09-transport/)。

| 实验 | 用到的文件 |
|---|---|
| 实验 9-1 ★ 在抓包里找三次握手和四次挥手 | `../data/pcap/tcp_udp_chat.pcap`、`../data/pcap/web_visit.pcap`；Wireshark |
| 实验 9-2 ★ 两人聊天程序 | `lab9_2_tcp_client.py`、`lab9_2_tcp_server.py` |
| 实验 9-3 ☆ TCP 与 UDP 对比 | `lab9_2_udp_client.py`、`lab9_2_udp_server.py`、`../data/pcap/tcp_udp_chat.pcap`；Wireshark |

## 程序说明

| 文件 | 作用 |
|---|---|
| `lab9_2_tcp_client.py` | 实验 9-2：TCP 聊天的客户端，服务器运行后再运行它 |
| `lab9_2_tcp_server.py` | 实验 9-2：TCP 聊天的服务器端，先运行它 |
| `lab9_2_udp_client.py` | 实验 9-2 改一改：UDP 版客户端 |
| `lab9_2_udp_server.py` | 实验 9-2 改一改：UDP 版服务器 |

运行方法：用 Thonny 打开后点“运行”，或在命令提示符中进入本文件夹后执行 `python 文件名.py`。程序只用 Python 标准库，不需要安装第三方库。
