# 实验数据说明

## 抓包文件 `pcap/`

全部由编者在自己搭建的实验网络中录制或生成，不含任何真实用户的数据，可以放心用 Wireshark 打开（菜单“文件 → 打开”）。

录制网络：`PC (192.168.1.10/24) ── R1 ── R2 ── 服务器 (203.0.113.10)`，服务器上运行 DNS（www.xiaohe.com）、网站（80 端口）和 HTTPS（443 端口）。203.0.113.0/24 是专门留给文档和示例使用的地址段（RFC 5737），不对应互联网上的真实主机。

| 文件 | 帧数 | 内容 | 使用章节 |
|---|---|---|---|
| `web_visit.pcap` | 18 | 打开一个网页的全过程：ARP → DNS 查询与响应 → TCP 三次握手 → HTTP 请求与响应 → 四次挥手 | 第 2、4、5、6、9、10 章 |
| `ping_trace.pcap` | 14 | `ping` 和 `traceroute`：ICMP 回送请求与回答、TTL 超时报文 | 第 7、8 章 |
| `dhcp_arp.pcap` | 12 | 电脑开机自动获取地址：DHCP 四个报文、ARP 请求与响应、ping 网关 | 第 8 章 |
| `tcp_udp_chat.pcap` | 18 | 同样两句话分别用 TCP 和 UDP 发送，对比握手、确认和挥手 | 第 9 章 |
| `http_vs_https.pcap` | 37 | 同一个登录页面分别用 HTTP 和 HTTPS 提交：HTTP 中能直接看到用户名和密码，HTTPS 只能看到 TLS 握手和密文 | 第 11 章 |
| `vlan_trunk.pcap` | 12 | 两台交换机之间 Trunk 链路上的帧，带 VLAN 10 和 VLAN 20 的 802.1Q 标签 | 第 4、5 章 |

`http_vs_https.pcap` 里的用户名、密码是编者为演示虚构的，HTTPS 用的是编者自签的证书。

## 网站文件 `site/`

录制抓包时服务器上的小网站：`index.html`（首页）和 `login.html`（登录页）。

## 脚本（编者用，学生不需要运行）

| 文件 | 作用 |
|---|---|
| `make_pcaps.sh` | 在 Linux 中用网络命名空间搭出上面的小网络，依次录制前五个抓包文件（需要 root 权限和 iproute2、tcpdump、dnsmasq 等工具） |
| `make_vlan_pcap.py` | 用 scapy 生成 `vlan_trunk.pcap`（录制环境的内核不支持 VLAN 接口） |
| `tiny_server.py` | 录制时运行在服务器上的小网站，支持 HTTP 和 HTTPS |
| `fetch.py` | 录制时在 PC 上模拟浏览器访问网站 |
| `chat_demo.py` | 录制时自动发送两句话的 TCP / UDP 聊天程序 |

重新运行 `make_pcaps.sh` 会得到端口号、序号不同的新文件，与教材中引用的数值对不上，所以**不要覆盖**仓库里的抓包文件。
