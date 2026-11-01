---
title: 附录 B 实验环境与资源说明
description: Cisco Packet Tracer、Wireshark、Python 和 Thonny 的获取与安装，本书配套抓包文件、实验程序和交互动画清单
---

# 附录 B 实验环境与资源说明

本书的实验只需要一台能上网的 Windows 电脑（macOS 也可以，命令写法见附录 A），用到三类工具：Windows 自带的命令行、Wireshark 抓包软件和 Cisco Packet Tracer 模拟器；少数实验用到 Python。所有工具都可以免费获取。

## B.1 Cisco Packet Tracer { #b1 }

Packet Tracer 是思科公司为网络教学开发的模拟器，可以在电脑上“拖设备、连网线、敲命令”，模拟交换机、路由器、服务器、电脑和无线设备，第 4、5、7、8、10、11、12 章的实验都用它完成。

**获取方法**：

1. 打开思科网络技术学院网站 <https://www.netacad.com>，注册一个免费账号（也可以用谷歌等账号登录）；
2. 登录后在资源（Resources）中找到 Packet Tracer 的下载页面，下载与你的系统对应的安装包。编写本书时的最新正式版为 9.0；本书的实验在 8.x 版本中同样可以完成；
3. 安装后第一次打开时，用同一个账号登录。

!!! warning "请从官方网站下载"
    网上有很多“破解版”“汉化版”下载站，可能捆绑恶意程序。Packet Tracer 本身是免费的，请只从思科网络技术学院官方网站下载。

**基本操作**：

| 操作 | 方法 |
|---|---|
| 放置设备 | 在窗口左下角选择设备类型（如 Network Devices → Switches），把型号（如 2960）拖到工作区 |
| 连线 | 选择闪电图标中的连线类型（不确定时选“自动选择”），先点一台设备选接口，再点另一台设备选接口 |
| 配置电脑 | 点电脑 → Desktop → IP Configuration 设置地址；Command Prompt 中可以用 ping、ipconfig 等命令 |
| 配置交换机、路由器 | 点设备 → CLI 选项卡，在命令行中输入命令 |
| 配置服务器 | 点服务器 → Services 选项卡，开启 HTTP、DNS、EMAIL、DHCP 等服务 |
| 模拟模式 | 右下角从 Realtime 切换到 Simulation，可以一步步观察数据包在网络中的传送 |
| 保存 | File → Save，文件扩展名为 `.pkt` |

**本书中常用的设备型号**：二层交换机 2960，三层交换机 3560，路由器 2911（也可以用 1941、4321），服务器 Server-PT，无线路由器 WRT300N 或 Home Router。

**学校使用华为设备的**，可以用华为 eNSP 模拟器完成同样的实验，命令对照见[附录 C](c-huawei.md)。

## B.2 Wireshark { #b2 }

Wireshark 是免费、开源的抓包和协议分析软件，第 2、4、5、8、9、10、11 章的实验都用它打开本书的抓包文件。

1. 打开官方网站 <https://www.wireshark.org>，在 Download 页面下载 Windows 安装包（Windows x64 Installer）；
2. 安装时保持默认选项；如果提示安装 Npcap（抓包驱动），选择安装，这样才能抓本机的包；
3. 打开本书的抓包文件：菜单“文件 → 打开”，选择 `labs/data/pcap/` 中的 `.pcap` 文件。

Wireshark 的界面分为三部分：上面是**分组列表**（每行一帧），中间是**分组详情**（按层展开的首部字段），下面是**分组字节**（原始的十六进制数据）。常用的显示过滤器见[附录 A](a-commands.md#a4)。

## B.3 Python 与 Thonny { #b3 }

第 1、3、4、5、6、7、8、9、10、11、12 章有少量 Python 程序，都只使用 Python 自带的标准库（`ipaddress`、`socket`、`http.server`、`hashlib` 等），**不需要安装任何第三方库**。

推荐初学者使用 **Thonny**：它自带 Python，安装后就能用。从 <https://thonny.org> 下载 Windows 安装包，安装后打开 `.py` 文件，点绿色的“运行”按钮即可。已经按《Python 编程》课程安装了 Python 的同学，也可以在命令提示符中进入程序所在的文件夹，执行 `python 文件名.py`。

本书的程序在 Python 3.10 及以上版本中运行；书中的运行结果是编者用 Python 3.13 实际运行得到的。

## B.4 配套资源清单 { #b4 }

配套资源放在本书代码仓库的 `labs/` 目录中，按章存放。

**抓包文件**（`labs/data/pcap/`）：编者在一台 Linux 电脑上用网络命名空间搭建了一个隔离的实验网络（电脑 192.168.1.10、路由器 192.168.1.1、服务器 203.0.113.10），在其中录制。地址都是私有地址或专供文档使用的地址，账号密码都是实验专用的，不涉及任何真实用户的数据。录制脚本是 `labs/data/make_pcaps.sh`。

| 文件 | 帧数 | 内容 | 用到的章节 |
|---|---|---|---|
| `web_visit.pcap` | 18 | 浏览器访问 `http://www.xiaohe.com`：ARP → DNS → TCP 三次握手 → HTTP → 四次挥手 | 第 2、4、6、9、10 章 |
| `dhcp_arp.pcap` | 12 | 电脑开机用 DHCP 获取地址（四步），然后 ARP 并 ping 网关 | 第 8 章 |
| `ping_trace.pcap` | 14 | ping 服务器 4 次，然后 traceroute（ICMP 方式） | 第 1、7、8 章 |
| `tcp_udp_chat.pcap` | 18 | 一次 TCP 聊天（第 1～14 帧）和一次 UDP 聊天（第 15～18 帧） | 第 9 章 |
| `http_vs_https.pcap` | 37 | 同一个登录表单用 HTTP（明文）和 HTTPS（TLS 1.3 加密）各提交一次 | 第 11 章 |
| `vlan_trunk.pcap` | 12 | Trunk 链路上带 802.1Q 标签的帧（用 scapy 按标准构造） | 第 5 章 |

**实验程序**：

| 章 | 程序 | 内容 |
|---|---|---|
| 第 1 章 | `ch01/lab1_3_speed.py` | 网速单位换算 |
| 第 3 章 | `ch03/lab3_3_download_time.py` | 计算下载时间 |
| 第 4 章 | `ch04/crc_demo.py`、`ch04/lab4_1_frames.py` | CRC 检错演示、统计帧 |
| 第 5 章 | `ch05/lab5_2_vlan_count.py` | 统计各 VLAN 的帧数 |
| 第 6 章 | `ch06/lab6_1_subnet.py`、`lab6_2_check_plan.py`、`lab6_3_ipv6.py` | 子网计算、检查地址规划、IPv6 地址 |
| 第 7 章 | `ch07/longest_match.py` | 最长前缀匹配 |
| 第 8 章 | `ch08/lab8_1_dhcp_steps.py` | 列出 DHCP 四步 |
| 第 9 章 | `ch09/lab9_2_tcp_server.py` 等 4 个 | TCP、UDP 聊天程序 |
| 第 10 章 | `ch10/lab10_1_url_parts.py`、`lab10_3_client.py`、`mysite/` | 拆分网址、HTTP 客户端、示例网站 |
| 第 11 章 | `ch11/lab11_1_hash.py` | 哈希的“指纹”特性 |
| 第 12 章 | `ch12/lab12_3_check.py` | 网络巡检小工具 |

**交互动画**：全书 26 个交互动画都可以在浏览器中直接打开，不需要安装，目录见网站的“交互动画”页面。

**Packet Tracer 拓扑文件**：本书的 Packet Tracer 实验都给出了完整的拓扑、地址规划和参考配置，学生按步骤自己搭建。书中 Packet Tracer 的显示均为输出格式示意，教师可按自己使用的版本实测后，把完成的 `.pkt` 文件作为参考答案分发。
