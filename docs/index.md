# 计算机网络

**面向成人教育人工智能技术应用专业（专科）的《计算机网络》教材**

<!-- 书名、课程信息框和“目录与实验”表由 python tools/course.py sync 根据 course.yml 生成；全书概览表由 python tools/book_stats.py 生成 -->

<!-- course:start -->
!!! abstract "课程信息"
    4 学分 · 72 学时（理论 60 学时 + 实验 12 学时） · 第 2 学期 · 12 章 · 36 个实验 · 期末闭卷
<!-- course:end -->

## 这本书讲什么

刷短视频、扫码付款、视频会议、调用大模型，背后都是计算机网络。数据怎样从你的手机走到千里之外的服务器？家里 WiFi 为什么时快时慢？一家公司的网络该怎么规划、出了故障从哪里查起？这些就是本书要回答的问题。

本书面向零基础的同学，跟着“小禾设计工作室”从 5 个人发展到 3 个部门、再开一家分店的过程，一章搭一块网络：先认识网络的组成和分层（第 1～2 章），再从物理层一层层往上，学网线和无线、交换机和 VLAN（第 3～5 章），IP 地址、子网划分和路由（第 6～8 章），TCP 和 UDP（第 9 章），域名、网页和邮件（第 10 章），最后学网络安全、网络管理和故障排查，完成一份完整的组网方案（第 11～12 章）。

## 本书的特点

- **通俗易懂**：用寄快递、写信封、打电话这些生活比喻讲清原理，计算只保留闭卷常考的几类，都配“算一算”例题；
- **三种工具，都免费**：Windows 命令行看自己的网络，Wireshark 打开编者录好的抓包文件看数据长什么样，Cisco Packet Tracer 拖设备、连网线、敲命令搭网络（附录 C 给出华为命令对照）；
- **结果真实**：抓包文件由编者在真实的小网络里录制，Python 程序的输出都是实际运行得到的；Packet Tracer 的配置按标准 Cisco IOS 命令编写，建议任课教师课前在 Packet Tracer 中走一遍；
- **在线练习**：每章课后的单选、多选和判断题可以在网页上直接作答并查看解析，另有两套闭卷模拟卷；
- **AI 与网络**：每章最后一节联系人工智能，看看大模型的训练、部署和调用离不开哪些网络技术。

## 全书概览

<!-- stats:start -->

| 章 | 正文字数 | 实验 | 课后练习<br>（可在线作答） | 术语 | 参考文献 | 交互动画 |
|---|---|---|---|---|---|---|
| [第 1 章](chapters/01-intro/index.md) | 0.9 万 | 3 | 20（16） | 30 | 5 | 2 |
| [第 2 章](chapters/02-architecture/index.md) | 0.7 万 | 3 | 20（16） | 24 | 5 | 2 |
| [第 3 章](chapters/03-physical/index.md) | 0.8 万 | 3 | 20（16） | 30 | 5 | 3 |
| [第 4 章](chapters/04-datalink/index.md) | 0.1 万 | 3 | 5（3） | 0 | 1 | 0 |
| [第 5 章](chapters/05-vlan-wlan/index.md) | 0.1 万 | 3 | 5（3） | 0 | 1 | 0 |
| [第 6 章](chapters/06-ip-address/index.md) | 0.1 万 | 3 | 5（3） | 0 | 1 | 0 |
| [第 7 章](chapters/07-routing/index.md) | 0.1 万 | 3 | 5（3） | 0 | 1 | 0 |
| [第 8 章](chapters/08-arp-dhcp-nat/index.md) | 0.1 万 | 3 | 5（3） | 0 | 1 | 0 |
| [第 9 章](chapters/09-transport/index.md) | 0.1 万 | 3 | 5（3） | 0 | 1 | 0 |
| [第 10 章](chapters/10-application/index.md) | 0.1 万 | 3 | 5（3） | 0 | 1 | 0 |
| [第 11 章](chapters/11-security/index.md) | 0.1 万 | 3 | 5（3） | 0 | 1 | 0 |
| [第 12 章](chapters/12-management/index.md) | 0.1 万 | 3 | 5（3） | 0 | 1 | 0 |
| **合计** | **3.1 万** | **36** | **105（75）** | **84** | **24** | **7** |

正文字数只统计汉字，不含代码和课后练习；单选、多选和判断题可以在网页上直接作答。配套学习资源：[交互动画](sims/index.md) 7 个 · [学习图谱](learning-graph/index.md) 137 个概念 · [常见问题](faq/index.md) 0 问 · [术语表](appendix/glossary.md) 84 条。

<!-- stats:end -->

## 目录与实验

<!-- toc:start -->
| 章节 | 实验 |
|---|---|
| [第 1 章 认识计算机网络](chapters/01-intro/index.md) | 实验 1-1 ★ 摸清我的网络：ipconfig 与网络草图<br>实验 1-2 ★ 用 ping 测往返时间和丢包率<br>实验 1-3 ☆ 测网速，换算 Mbps 与 MB/s |
| [第 2 章 网络体系结构：分层与协议](chapters/02-architecture/index.md) | 实验 2-1 ★ 安装 Wireshark，打开抓包文件看五层<br>实验 2-2 ★ 抓自己的包，用过滤器找 DNS 和 HTTPS<br>实验 2-3 ☆ 协议和设备对号入座 |
| [第 3 章 物理层：从比特到信号](chapters/03-physical/index.md) | 实验 3-1 ★ 认识网线和接口，排出 T568B 线序<br>实验 3-2 ★ 看懂无线信号：信号强度、信道和速率<br>实验 3-3 ☆ 带宽与下载时间：算一算再测一测 |
| [第 4 章 数据链路层与以太网交换](chapters/04-datalink/index.md) | 实验 4-1 ★ 在抓包里看以太网帧<br>实验 4-2 ★ Packet Tracer 第一次组网<br>实验 4-3 ☆ 用模拟模式看帧怎么走 |
| [第 5 章 VLAN 与无线局域网](chapters/05-vlan-wlan/index.md) | 实验 5-1 ★ 按部门划分 VLAN<br>实验 5-2 ★ 两台交换机之间的 Trunk，看 802.1Q 标签<br>实验 5-3 ☆ 设置无线路由器 |
| [第 6 章 IP 地址：IPv4、子网划分与 IPv6](chapters/06-ip-address/index.md) | 实验 6-1 ★ 子网划分练习<br>实验 6-2 ★ 为工作室规划 IP 地址<br>实验 6-3 ☆ 认识 IPv6 |
| [第 7 章 路由：数据包怎么找路](chapters/07-routing/index.md) | 实验 7-1 ★ 实验名称<br>实验 7-2 ★ 实验名称<br>实验 7-3 ★ 实验名称 |
| [第 8 章 网络层的好帮手：ARP、ICMP、DHCP 与 NAT](chapters/08-arp-dhcp-nat/index.md) | 实验 8-1 ★ 实验名称<br>实验 8-2 ★ 实验名称<br>实验 8-3 ★ 实验名称 |
| [第 9 章 传输层：TCP 与 UDP](chapters/09-transport/index.md) | 实验 9-1 ★ 实验名称<br>实验 9-2 ★ 实验名称<br>实验 9-3 ★ 实验名称 |
| [第 10 章 应用层：域名、网页与常用服务](chapters/10-application/index.md) | 实验 10-1 ★ 实验名称<br>实验 10-2 ★ 实验名称<br>实验 10-3 ★ 实验名称 |
| [第 11 章 网络安全](chapters/11-security/index.md) | 实验 11-1 ★ 实验名称<br>实验 11-2 ★ 实验名称<br>实验 11-3 ★ 实验名称 |
| [第 12 章 网络管理、新技术与综合项目](chapters/12-management/index.md) | 实验 12-1 ★ 实验名称<br>实验 12-2 ★ 实验名称<br>实验 12-3 ★ 实验名称 |

附录：[A 常用网络命令速查](appendix/a-commands.md) · [B 实验环境与资源说明](appendix/b-environment.md) · [C Cisco 与华为命令对照](appendix/c-huawei.md) · [D 术语表](appendix/glossary.md) · [E 实验报告模板与综合项目指南](appendix/e-project.md)
<!-- toc:end -->

## 配套资源

- [交互动画](sims/index.md)、[学习图谱](learning-graph/index.md)、[常见问题](faq/index.md)
- 实验代码与数据：仓库中的 `labs/` 目录
- 课件、教案和 Word/PDF 版教材：见仓库的 Releases 页面
