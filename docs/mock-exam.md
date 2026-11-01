---
title: 闭卷模拟卷
description: 按期末闭卷考试的题型和分值组成的两套模拟卷，含选择、判断、填空、子网计算、抓包分析、简答和配置补全，可以直接作答并查看解析
---

# 闭卷模拟卷

本课程期末为**闭卷考试**（占总评 50%）。下面两套模拟卷按期末考试的题型和分值组成，覆盖全书 12 章。选择、判断和简答题从各章课后练习中抽取，填空、子网计算、抓包分析和配置补全题为新编题目：

| 题型 | 题数 | 分值 | 合计 |
|---|---|---|---|
| 单项选择题 | 20 | 每题 1 分 | 20 |
| 多项选择题 | 5 | 每题 2 分 | 10 |
| 判断题 | 10 | 每题 1 分 | 10 |
| 填空题 | 10 空 | 每空 1 分 | 10 |
| 子网计算题 | 1 | 10 分 | 10 |
| 抓包分析题 | 1 | 10 分 | 10 |
| 简答题 | 3 | 每题 6 分 | 18 |
| 配置补全题 | 1 | 12 分 | 12 |
| **合计** | | | **100** |

建议限时 100 分钟，**不看书、不用计算器**独立做完一整套，再展开“答案与解析”核对。子网计算要求手算，草稿纸上写出过程。选择题和判断题可以直接点击作答；每道题解析下方的“回看”链接可以跳回对应章节复习。

!!! tip "闭卷复习建议"
    重点记牢：五层模型各层的作用和设备；MAC 地址、IP 地址、端口号的作用；常用端口号；子网划分的方法（块大小法）；交换机学习与转发、路由表查找（最长前缀匹配）；ARP、DHCP、NAT 的过程；TCP 与 UDP 的区别、三次握手和四次挥手、拥塞窗口的变化；DNS 的查询方式、HTTP 状态码；加密、签名、证书的区别；ACL 的匹配规则和通配符掩码；故障排查六步法。各章“本章小结”和[学习图谱](learning-graph/index.md)可以帮你串起全书。

## 模拟卷一

**一、单项选择题**（每题 1 分，共 20 分）

<div class="quiz" data-answer="C" markdown>

**1.** 下列关于计算机网络的说法，正确的是（　　）。

- A. 联网的计算机必须由一台主机统一控制
- B. 只有台式电脑和服务器才算网络中的“计算机”
- C. 联网的计算机功能独立，按共同的规则交换数据、共享资源
- D. 计算机网络只能在一栋楼内使用

</div>

??? tip "答案与解析"
    **答案：C**

    计算机网络连接的是功能独立的计算机，按协议通信。A 错，网络中的计算机不是谁的附属；B 错，手机、摄像头等都算；D 错，广域网可以覆盖全球。

    考查：计算机网络的定义 · 认知层次：理解 · [回看 1.1.2](chapters/01-intro/index.md#112)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**2.** 协议三要素中，规定“数据的格式和结构”的是（　　）。

- A. 语义
- B. 语法
- C. 同步
- D. 接口

</div>

??? tip "答案与解析"
    **答案：B**

    语法管“怎么写”（格式），语义管“什么意思”，同步管“什么时候做”。接口不是协议的要素。

    考查：协议三要素 · 认知层次：记忆 · [回看 2.1.2](chapters/02-architecture/index.md#212)
    { .quiz-meta }

<div class="quiz" data-answer="C" markdown>

**3.** 对讲机通话时双方都能说话但不能同时说，这种通信方式是（　　）。

- A. 单工
- B. 全双工
- C. 半双工
- D. 复用

</div>

??? tip "答案与解析"
    **答案：C**

    双方都能发但不能同时发是半双工；只能单向是单工；能同时双向是全双工。

    考查：通信方式 · 认知层次：理解 · [回看 3.1.3](chapters/03-physical/index.md#313)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**4.** 数据链路层要解决的三个基本问题是（　　）。

- A. 编码、调制、复用
- B. 封装成帧、透明传输、差错检测
- C. 路由选择、拥塞控制、流量控制
- D. 域名解析、地址分配、网络地址转换

</div>

??? tip "答案与解析"
    **答案：B**

    A 是物理层的内容；C 主要是网络层和运输层的内容；D 是第 8、10 章的内容。

    考查：数据链路层的三个基本问题 · 认知层次：记忆 · [回看 4.1.1](chapters/04-datalink/index.md#411)
    { .quiz-meta }

<div class="quiz" data-answer="C" markdown>

**5.** 划分 VLAN 的主要作用是（　　）。

- A. 隔离冲突域
- B. 提高网线的传输速率
- C. 隔离广播域
- D. 代替路由器连接互联网

</div>

??? tip "答案与解析"
    **答案：C**

    每个 VLAN 是一个独立的广播域。隔离冲突域靠的是交换机的每个接口；VLAN 不能代替路由器连接不同网络。

    考查：VLAN 的作用 · 认知层次：理解 · [回看 5.1.2](chapters/05-vlan-wlan/index.md#512)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**6.** 二进制数 `11100000` 换算成十进制是（　　）。

- A. 192
- B. 224
- C. 240
- D. 248

</div>

??? tip "答案与解析"
    **答案：B**

    128 + 64 + 32 = 224。192 是 2 个 1，240 是 4 个 1，248 是 5 个 1。

    考查：二进制转十进制 · 认知层次：应用 · [回看 6.2.2](chapters/06-ip-address/index.md#622)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**7.** 路由器转发数据报的依据是（　　）。

- A. 目的 MAC 地址
- B. 目的 IP 地址
- C. 源 IP 地址
- D. 端口号

</div>

??? tip "答案与解析"
    **答案：B**

    路由器工作在网络层，根据目的 IP 地址查路由表转发；交换机根据目的 MAC 地址转发。

    考查：路由器的工作 · 认知层次：记忆 · [回看 7.1.1](chapters/07-routing/index.md#711)
    { .quiz-meta }

<div class="quiz" data-answer="A" markdown>

**8.** ARP 协议的作用是（　　）。

- A. 由 IP 地址查找 MAC 地址
- B. 由 MAC 地址查找 IP 地址
- C. 由域名查找 IP 地址
- D. 自动分配 IP 地址

</div>

??? tip "答案与解析"
    **答案：A**

    ARP 已知同一网段内主机的 IP 地址，查出它的 MAC 地址。C 是 DNS（第 10 章），D 是 DHCP。

    考查：ARP 的作用 · 认知层次：记忆 · [回看 8.1.1](chapters/08-arp-dhcp-nat/index.md#811)
    { .quiz-meta }

<div class="quiz" data-answer="C" markdown>

**9.** 运输层为（　　）之间提供通信服务。

- A. 相邻的两个节点
- B. 两台主机
- C. 两台主机上的进程
- D. 两个路由器

</div>

??? tip "答案与解析"
    **答案：C**

    数据链路层管相邻节点，网络层管主机到主机，运输层管进程到进程。

    考查：运输层的作用 · 认知层次：理解 · [回看 9.1.1](chapters/09-transport/index.md#911)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**10.** DNS 的主要作用是（　　）。

- A. 为主机自动分配 IP 地址
- B. 把域名转换为 IP 地址
- C. 把 IP 地址转换为 MAC 地址
- D. 把私有地址转换为公网地址

</div>

??? tip "答案与解析"
    **答案：B**

    A 是 DHCP，C 是 ARP，D 是 NAT。

    考查：DNS 的作用 · 认知层次：记忆 · [回看 10.2.1](chapters/10-application/index.md#1021)
    { .quiz-meta }

<div class="quiz" data-answer="C" markdown>

**11.** 黑客控制大量设备同时访问工作室网站，使正常用户无法打开网站。这主要破坏了信息安全的（　　）。

- A. 机密性
- B. 完整性
- C. 可用性
- D. 不可否认性

</div>

??? tip "答案与解析"
    **答案：C**

    这是拒绝服务攻击（DDoS），让有权限的人无法正常使用服务，破坏的是可用性。

    考查：安全目标与威胁 · 认知层次：理解 · [回看 11.1.1](chapters/11-security/index.md#1111)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**12.** 网络管理员定期备份交换机和路由器的配置，并记录每次配置修改，这属于网络管理中的（　　）。

- A. 故障管理
- B. 配置管理
- C. 性能管理
- D. 计费管理

</div>

??? tip "答案与解析"
    **答案：B**

    记录、修改、备份设备配置属于配置管理。

    考查：网络管理五大功能 · 认知层次：理解 · [回看 12.1.1](chapters/12-management/index.md#1211)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**13.** 主机 192.168.8.150/26 所在网络的网络地址是（　　）。

- A. 192.168.8.0
- B. 192.168.8.128
- C. 192.168.8.150
- D. 192.168.8.192

</div>

??? tip "答案与解析"
    **答案：B**

    /26 的掩码最后一组为 192，块大小 64。150 落在 128～191 这一块，网络地址为 192.168.8.128，广播地址为 192.168.8.191。

    考查：求网络地址 · 认知层次：应用 · [回看 6.4.3](chapters/06-ip-address/index.md#643)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**14.** RIP 协议认为不可达的跳数是（　　）。

- A. 15
- B. 16
- C. 255
- D. 30

</div>

??? tip "答案与解析"
    **答案：B**

    RIP 跳数最大 15，16 表示不可达；30 是 RIP 的更新周期（秒）。

    考查：RIP · 认知层次：记忆 · [回看 7.4.1](chapters/07-routing/index.md#741)
    { .quiz-meta }

<div class="quiz" data-answer="C" markdown>

**15.** 主机 A 向主机 B 发送了一个 TCP 报文段，序号为 200，携带 100 字节数据。B 正确收到后，发回的确认号是（　　）。

- A. 200
- B. 299
- C. 300
- D. 301

</div>

??? tip "答案与解析"
    **答案：C**

    数据是第 200～299 字节，确认号 = 200 + 100 = 300，表示期望下一次从第 300 字节开始。

    考查：序号与确认号 · 认知层次：应用 · [回看 9.4.2](chapters/09-transport/index.md#942)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**16.** 用户在网页上填写登录表单并提交时，通常使用的 HTTP 请求方法是（　　）。

- A. GET
- B. POST
- C. HEAD
- D. DELETE

</div>

??? tip "答案与解析"
    **答案：B**

    POST 用于向服务器提交数据，数据放在正文中；GET 的参数会出现在地址栏中，不适合传密码。

    考查：请求方法 · 认知层次：理解 · [回看 10.3.3](chapters/10-application/index.md#1033)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**17.** 交换机收到一个帧，在 MAC 地址表中查不到它的目的地址，交换机会（　　）。

- A. 丢弃这个帧
- B. 从除接收接口以外的所有接口发出
- C. 把这个帧退回给发送方
- D. 等待目的主机先发送数据

</div>

??? tip "答案与解析"
    **答案：B**

    查不到目的地址时交换机泛洪；同时它会把源地址和接收接口记入地址表。

    考查：交换机的转发与泛洪 · 认知层次：理解 · [回看 4.6.2](chapters/04-datalink/index.md#462)
    { .quiz-meta }

<div class="quiz" data-answer="A" markdown>

**18.** DHCP 分配地址的四个步骤，正确的顺序是（　　）。

- A. 发现、提供、请求、确认
- B. 请求、提供、发现、确认
- C. 发现、请求、提供、确认
- D. 提供、发现、确认、请求

</div>

??? tip "答案与解析"
    **答案：A**

    Discover、Offer、Request、ACK，简记 DORA。

    考查：DHCP 四步 · 认知层次：记忆 · [回看 8.3.2](chapters/08-arp-dhcp-nat/index.md#832)
    { .quiz-meta }

<div class="quiz" data-answer="C" markdown>

**19.** HTTPS 默认使用的端口号和在 HTTP 下面增加的协议分别是（　　）。

- A. 80，SSH
- B. 8080，TLS
- C. 443，TLS
- D. 443，IPsec

</div>

??? tip "答案与解析"
    **答案：C**

    HTTPS = HTTP + TLS，默认端口 443。

    考查：HTTPS · 认知层次：记忆 · [回看 11.3.1](chapters/11-security/index.md#1131)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**20.** 路由器主要工作在五层模型的（　　）。

- A. 物理层
- B. 网络层
- C. 运输层
- D. 应用层

</div>

??? tip "答案与解析"
    **答案：B**

    路由器根据 IP 地址转发分组，工作在网络层。交换机工作在数据链路层，集线器工作在物理层。

    考查：设备所在的层 · 认知层次：理解 · [回看 2.4.2](chapters/02-architecture/index.md#242)
    { .quiz-meta }

**二、多项选择题**（每题 2 分，共 10 分；多选、少选、错选均不得分）

<div class="quiz quiz-multi" data-answer="ABD" markdown>

**21.** 与集线器相比，交换机的特点有（　　）。

- A. 能根据目的 MAC 地址转发帧
- B. 每个接口独享带宽
- C. 能隔离广播域
- D. 每个接口是一个独立的冲突域

</div>

??? tip "答案与解析"
    **答案：ABD**

    交换机隔离冲突域，但不隔离广播域，广播帧仍会被泛洪到所有接口；能隔离广播域的是路由器（以及下一章的 VLAN）。

    考查：集线器与交换机 · 认知层次：分析 · [回看 4.5.3](chapters/04-datalink/index.md#453)
    { .quiz-meta }

<div class="quiz quiz-multi" data-answer="ACD" markdown>

**22.** 网络 192.168.8.96/27 中，下列地址可以分配给主机使用的有（　　）。

- A. 192.168.8.97
- B. 192.168.8.127
- C. 192.168.8.110
- D. 192.168.8.126

</div>

??? tip "答案与解析"
    **答案：ACD**

    这个子网的网络地址是 .96，广播地址是 .127，可用地址 .97～.126。B 是广播地址，不能分配。

    考查：可用地址范围 · 认知层次：应用 · [回看 6.4.3](chapters/06-ip-address/index.md#643)
    { .quiz-meta }

<div class="quiz quiz-multi" data-answer="ABD" markdown>

**23.** 与 UDP 相比，TCP 的特点有（　　）。

- A. 面向连接
- B. 提供可靠传输
- C. 支持广播和多播
- D. 有流量控制和拥塞控制

</div>

??? tip "答案与解析"
    **答案：ABD**

    TCP 只能一对一通信，不支持广播和多播；需要广播的 DHCP 用的是 UDP。

    考查：TCP 与 UDP 的区别 · 认知层次：理解 · [回看 9.3.1](chapters/09-transport/index.md#931)
    { .quiz-meta }

<div class="quiz quiz-multi" data-answer="ABD" markdown>

**24.** 下列关于 DNS 的说法，正确的有（　　）。

- A. DNS 查询通常使用 UDP，服务器端口为 53
- B. 根域名服务器只告诉查询者下一步该去问哪个顶级域名服务器
- C. 全世界所有域名都保存在根域名服务器中
- D. 本地域名服务器会把查询结果缓存一段时间

</div>

??? tip "答案与解析"
    **答案：ABD**

    DNS 是分布式的，根服务器只知道顶级域名服务器在哪里，具体主机的地址保存在各自的权威域名服务器中。

    考查：DNS 的工作方式 · 认知层次：理解 · [回看 10.2.3](chapters/10-application/index.md#1023)
    { .quiz-meta }

<div class="quiz quiz-multi" data-answer="ABD" markdown>

**25.** 数字证书中通常包含（　　）。

- A. 持有者的名称（如网站域名）
- B. 持有者的公钥
- C. 持有者的私钥
- D. 有效期和颁发机构的签名

</div>

??? tip "答案与解析"
    **答案：ABD**

    私钥只能由持有者自己保管，绝不会出现在公开的证书里。

    考查：数字证书 · 认知层次：理解 · [回看 11.2.4](chapters/11-security/index.md#1124)
    { .quiz-meta }

**三、判断题**（每题 1 分，共 10 分）

<div class="quiz quiz-judge" data-answer="×" markdown>

**26.** Internet（首字母大写）泛指任意多个网络互相连接而成的网络。（　　）

</div>

??? tip "答案与解析"
    **答案：×**

    首字母大写的 Internet 专指全球最大的、采用 TCP/IP 的互联网；泛指多个网络互连的是 internet（小写）。

    考查：互联网与互连网 · 认知层次：记忆 · [回看 1.1.4](chapters/01-intro/index.md#114)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="×" markdown>

**27.** 互联网实际使用的体系结构是 OSI 七层模型。（　　）

</div>

??? tip "答案与解析"
    **答案：×**

    互联网使用 TCP/IP 体系结构，它是事实上的国际标准；OSI 是法律上的国际标准，没有在实际中普及。

    考查：OSI 与 TCP/IP · 认知层次：记忆 · [回看 2.3.2](chapters/02-architecture/index.md#232)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="×" markdown>

**28.** 双绞线、光纤等传输介质属于物理层。（　　）

</div>

??? tip "答案与解析"
    **答案：×**

    传输介质在物理层的下面，不属于物理层；物理层规定的是怎样在介质上传送比特。

    考查：物理层的任务 · 认知层次：理解 · [回看 3.1.1](chapters/03-physical/index.md#311)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="√" markdown>

**29.** 交换机是根据收到的帧的源 MAC 地址来学习，根据目的 MAC 地址来转发的。（　　）

</div>

??? tip "答案与解析"
    **答案：√**

    记源地址（学习）、查目的地址（转发），这是交换机工作的核心规则。

    考查：交换机自学习 · 认知层次：理解 · [回看 4.6.1](chapters/04-datalink/index.md#461)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="×" markdown>

**30.** 帧从交换机的 Access 口发给电脑时，仍然带着 802.1Q 标签。（　　）

</div>

??? tip "答案与解析"
    **答案：×**

    标签只在 Trunk 链路上出现。帧从 Access 口发给电脑前，交换机会把标签去掉，电脑收到的是普通以太网帧。

    考查：802.1Q 标签 · 认知层次：理解 · [回看 5.2.3](chapters/05-vlan-wlan/index.md#523)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="√" markdown>

**31.** 路由器在查路由表时，如果有多条路由都匹配目的地址，会选择前缀最长的一条。（　　）

</div>

??? tip "答案与解析"
    **答案：√**

    这就是最长前缀匹配，前缀越长，路由越具体。

    考查：最长前缀匹配 · 认知层次：理解 · [回看 7.2.3](chapters/07-routing/index.md#723)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="×" markdown>

**32.** ARP 请求可以经过路由器转发到其他网段。（　　）

</div>

??? tip "答案与解析"
    **答案：×**

    ARP 请求是广播，路由器不转发广播，ARP 只在同一网段内使用。

    考查：ARP 的使用范围 · 认知层次：理解 · [回看 8.1.2](chapters/08-arp-dhcp-nat/index.md#812)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="×" markdown>

**33.** 路由器转发数据报时要查看 TCP 首部中的端口号。（　　）

</div>

??? tip "答案与解析"
    **答案：×**

    运输层只在通信两端的主机上运行，路由器只处理到网络层（做 NAT 时例外）。

    考查：运输层的端到端特性 · 认知层次：理解 · [回看 9.1.1](chapters/09-transport/index.md#911)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="×" markdown>

**34.** 浏览器地址栏显示了锁形图标，说明这个网站是正规可信的网站。（　　）

</div>

??? tip "答案与解析"
    **答案：×**

    锁只说明通信是加密的、网站拥有这个域名的证书；钓鱼网站也可以申请证书。判断真假要看域名。

    考查：HTTPS 的局限 · 认知层次：评价 · [回看 11.3.3](chapters/11-security/index.md#1133)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="√" markdown>

**35.** 排查网络故障时，由下往上（从物理层开始）的顺序不容易遗漏问题，适合初学者。（　　）

</div>

??? tip "答案与解析"
    **答案：√**

    下层不通，上层一定不通；从下往上逐层确认，每一步都有明确结论。

    考查：排查思路 · 认知层次：理解 · [回看 12.2.1](chapters/12-management/index.md#1221)
    { .quiz-meta }

**四、填空题**（每空 1 分，共 10 分）

**36.** 填空：

(1) 五层模型从下到上依次是物理层、数据链路层、____①____、运输层和应用层。

(2) 以太网的 MAC 地址长 ____②____ 位。

(3) 交换机根据帧的 ____③____ 地址学习（记入 MAC 地址表），根据帧的 ____④____ 地址转发。

(4) 802.1Q 标签长 ____⑤____ 字节，其中 VLAN 标识符占 ____⑥____ 位。

(5) 前缀长度 /27 对应的子网掩码是 ____⑦____。

(6) DNS 服务器使用的熟知端口号是 ____⑧____。

(7) HTTP 状态码 ____⑨____ 表示服务器上找不到请求的资源。

(8) TCP 三次握手中，服务器发出的第二个报文段带有 ____⑩____ 标志位。

??? tip "答案与解析"
    **参考答案：** ① 网络层；② 48；③ 源 MAC　④ 目的 MAC；⑤ 4　⑥ 12；⑦ 255.255.255.224；⑧ 53；⑨ 404；⑩ SYN 和 ACK

    各空对应的章节：第 2 章 · [回看 2.4](chapters/02-architecture/index.md#24)；第 4 章 · [回看 4.3](chapters/04-datalink/index.md#43)；第 4 章 · [回看 4.5](chapters/04-datalink/index.md#45)；第 5 章 · [回看 5.2.2](chapters/05-vlan-wlan/index.md#522)；第 6 章 · [回看 6.4](chapters/06-ip-address/index.md#64)；第 9 章 · [回看 9.1.3](chapters/09-transport/index.md#913)；第 10 章 · [回看 10.3.4](chapters/10-application/index.md#1034)；第 9 章 · [回看 9.4.1](chapters/09-transport/index.md#941)。

    考查：基本概念与数据 · 认知层次：记忆
    { .quiz-meta }

**五、子网计算题**（10 分）

**37.** 某公司分到地址块 172.16.10.0/24，要分给三个部门和一条路由器互联链路：A 部门 100 台主机，B 部门 50 台，C 部门 20 台，互联链路 2 个地址。请用变长子网掩码，按“先大后小”的顺序从 172.16.10.0 开始依次分配，写出每个子网的网络地址/前缀、子网掩码、可用地址范围和广播地址。

??? tip "答案与解析"
    **参考答案：**

    | 子网 | 网络地址/前缀 | 子网掩码 | 可用地址范围 | 广播地址 |
    |---|---|---|---|---|
    | A（100 台） | 172.16.10.0/25 | 255.255.255.128 | 172.16.10.1～172.16.10.126 | 172.16.10.127 |
    | B（50 台） | 172.16.10.128/26 | 255.255.255.192 | 172.16.10.129～172.16.10.190 | 172.16.10.191 |
    | C（20 台） | 172.16.10.192/27 | 255.255.255.224 | 172.16.10.193～172.16.10.222 | 172.16.10.223 |
    | 互联链路 | 172.16.10.224/30 | 255.255.255.252 | 172.16.10.225～172.16.10.226 | 172.16.10.227 |

    思路：100 台需要 2⁷ − 2 = 126 ≥ 100，主机位 7 位，前缀 /25，块大小 128；50 台需要 2⁶ − 2 = 62，前缀 /26，块大小 64；20 台需要 2⁵ − 2 = 30，前缀 /27，块大小 32；2 个地址用 /30，块大小 4。评分：每个子网 2 分（网络地址与掩码 1 分，范围与广播地址 1 分），思路 2 分。

    考查：变长子网划分 · 认知层次：应用 · [回看 6.5](chapters/06-ip-address/index.md#65)
    { .quiz-meta }

**六、抓包分析题**（10 分）

**38.** 下面是本书抓包文件 `web_visit.pcap` 的部分帧（小林的电脑访问内部网站）：

    帧  源 → 目的                     协议  信息
    3   192.168.1.10 → 203.0.113.10   DNS   Standard query 0x85d7 A www.xiaohe.com
    5   203.0.113.10 → 192.168.1.10   DNS   Standard query response 0x85d7 A www.xiaohe.com A 203.0.113.10
    7   192.168.1.10 → 203.0.113.10   TCP   35070 → 80 [SYN] Seq=0
    8   203.0.113.10 → 192.168.1.10   TCP   80 → 35070 [SYN, ACK] Seq=0 Ack=1
    9   192.168.1.10 → 203.0.113.10   TCP   35070 → 80 [ACK] Seq=1 Ack=1
    10  192.168.1.10 → 203.0.113.10   HTTP  GET / HTTP/1.1
    14  203.0.113.10 → 192.168.1.10   HTTP  HTTP/1.1 200 OK (text/html)

已知第 10 帧的以太网目的地址是 00:e0:fc:12:34:01，这是网关 192.168.1.1 的 MAC 地址。请回答：（1）DNS 查询使用的运输层协议和服务器端口号是什么？查询结果是什么？（2）浏览器使用的源端口和目的端口各是多少？（3）哪几帧是三次握手？（4）第 14 帧的状态码是什么意思？（5）第 10 帧的目的 IP 地址是服务器，目的 MAC 地址却是网关，为什么？

??? tip "答案与解析"
    **参考答案：**

    （1）UDP，服务器端口 53；www.xiaohe.com 对应的地址是 203.0.113.10。（2 分）（2）源端口 35070（客户端随机选的），目的端口 80（HTTP 的熟知端口）。（2 分）（3）第 7、8、9 帧：SYN → SYN+ACK → ACK。（2 分）（4）200 OK 表示请求成功，服务器返回了网页（text/html）。（2 分）（5）服务器 203.0.113.10 不在本网段，电脑要先把帧交给默认网关，所以以太网目的地址填网关的 MAC 地址；IP 目的地址始终是最终的服务器。每经过一台路由器，MAC 地址都会换，IP 地址不变。（2 分）

    考查：抓包分析 · 认知层次：分析 · [回看 10.4](chapters/10-application/index.md#104)
    { .quiz-meta }

**七、简答题**（每题 6 分，共 18 分）

**39.** 用“打电话”的比喻描述 TCP 三次握手的过程，写出每个报文段的标志位，以及序号和确认号的关系（设客户端初始序号为 x，服务器初始序号为 y）。为什么不能只握手两次？

??? tip "答案与解析"
    **参考答案：** ① 客户端发 SYN，seq = x（“喂，听得到吗？”）；② 服务器回 SYN + ACK，seq = y，ack = x + 1（“听得到，你听得到我吗？”）；③ 客户端发 ACK，seq = x + 1，ack = y + 1（“听得到，开始吧”）。只握手两次，服务器无法确认客户端能收到自己的报文；同时，网络中滞留的旧连接请求到达服务器时，服务器会误以为是新连接而白白分配资源。第三次握手让双方都确认了收发能力，也能识别过期的请求。

    考查：三次握手 · 认知层次：理解 · [回看 9.4.1](chapters/09-transport/index.md#941)
    { .quiz-meta }

**40.** 用“打听一家店”的比喻说明递归查询和迭代查询的区别，并说明为什么根域名服务器一般不提供递归查询。

??? tip "答案与解析"
    **参考答案：** 递归查询像你问秘书，秘书负责替你问到底，最后直接告诉你答案；迭代查询像秘书去问服务台，服务台不知道就只告诉秘书“下一步去问谁”，由秘书自己一站一站接着问。全世界的查询都可能经过根服务器，如果根服务器还要替每个查询者跑完全程，负担太重，所以根服务器和顶级域名服务器只“指路”（迭代），跑腿由离用户近的本地域名服务器完成。

    考查：递归与迭代查询 · 认知层次：理解 · [回看 10.2.4](chapters/10-application/index.md#1024)
    { .quiz-meta }

**41.** 说明 HTTPS 是怎样综合运用数字证书、非对称加密和对称加密来保证安全的。为什么不全部使用非对称加密？

??? tip "答案与解析"
    **参考答案：** ① 服务器把数字证书发给浏览器，浏览器用预装的 CA 公钥验证证书的签名、域名和有效期，确认对方确实是这个网站，防止中间人冒充；② 双方用非对称的方法协商出一把只有双方知道的对称密钥，路上的人无法算出；③ 之后的 HTTP 请求和响应都用这把对称密钥加密，并带有完整性校验。不全部用非对称加密，是因为它计算量大、速度慢，不适合加密大量数据；对称加密速度快，但需要安全地交换密钥，两者配合正好取长补短。

    考查：HTTPS 原理 · 认知层次：理解 · [回看 11.3.2](chapters/11-security/index.md#1132)
    { .quiz-meta }

**八、配置补全题**（12 分）

**42.** 工作室出口路由器 R1 的内部接口 Gig0/0 连接设计部（192.168.8.0/26，网关 192.168.8.1），外部接口 Gig0/1 是唯一的公网地址。请补全下面的 DHCP 和 NAT 配置（每空 2 分）：

    R1(config)#ip dhcp excluded-address 192.168.8.1 192.168.8.10
    R1(config)#ip dhcp ____①____ DESIGN
    R1(dhcp-config)#network 192.168.8.0 ____②____
    R1(dhcp-config)#____③____ 192.168.8.1
    R1(dhcp-config)#dns-server 192.168.8.130
    R1(dhcp-config)#exit
    R1(config)#access-list 1 permit 192.168.8.0 ____④____
    R1(config)#ip nat inside source list 1 interface gig0/1 ____⑤____
    R1(config)#interface gig0/0
    R1(config-if)#ip nat ____⑥____
    R1(config-if)#interface gig0/1
    R1(config-if)#ip nat outside

??? tip "答案与解析"
    **参考答案：**

    ① `pool`；② `255.255.255.192`（/26 的子网掩码）；③ `default-router`（告诉客户机默认网关）；④ `0.0.0.63`（/26 的通配符掩码 = 255.255.255.255 − 255.255.255.192）；⑤ `overload`（多台主机共用一个公网地址，即 PAT）；⑥ `inside`（Gig0/0 是内部接口）。

    考查：DHCP 与 NAT 配置 · 认知层次：应用 · [回看实验 8-2](chapters/08-arp-dhcp-nat/index.md#8-2)
    { .quiz-meta }

## 模拟卷二

**一、单项选择题**（每题 1 分，共 20 分）

<div class="quiz" data-answer="B" markdown>

**1.** 小禾工作室的光猫、无线路由器属于网络组成中的（　　）。

- A. 端系统
- B. 网络设备
- C. 通信链路
- D. 应用软件

</div>

??? tip "答案与解析"
    **答案：B**

    光猫、路由器、交换机在链路的交汇处转发或转换数据，属于网络设备。端系统是电脑、手机、服务器等；通信链路是网线、光纤、无线信道。

    考查：网络的组成 · 认知层次：理解 · [回看 1.2.1](chapters/01-intro/index.md#121)
    { .quiz-meta }

<div class="quiz" data-answer="C" markdown>

**2.** OSI 参考模型从下往上的第三层是（　　）。

- A. 数据链路层
- B. 传输层
- C. 网络层
- D. 会话层

</div>

??? tip "答案与解析"
    **答案：C**

    物理（1）、数据链路（2）、网络（3）、传输（4）、会话（5）、表示（6）、应用（7）。

    考查：OSI 七层 · 认知层次：记忆 · [回看 2.3.1](chapters/02-architecture/index.md#231)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**3.** 关于曼彻斯特编码，下列说法正确的是（　　）。

- A. 连续的 1 没有电平跳变
- B. 每个码元的中间都有一次跳变，可以从信号中提取时钟
- C. 所需的频带宽度是不归零编码的一半
- D. 只能用于光纤

</div>

??? tip "答案与解析"
    **答案：B**

    曼彻斯特编码每个码元中间都有跳变，自带同步；代价是所需频带宽度是不归零编码的 2 倍。A 描述的是不归零编码的缺点。

    考查：曼彻斯特编码 · 认知层次：理解 · [回看 3.2.1](chapters/03-physical/index.md#321)
    { .quiz-meta }

<div class="quiz" data-answer="C" markdown>

**4.** 以太网的 MAC 地址长度是（　　）。

- A. 16 位
- B. 32 位
- C. 48 位
- D. 128 位

</div>

??? tip "答案与解析"
    **答案：C**

    MAC 地址 48 位（6 字节）。32 位是 IPv4 地址的长度，128 位是 IPv6 地址的长度，第 6 章学习。

    考查：MAC 地址 · 认知层次：记忆 · [回看 4.2.2](chapters/04-datalink/index.md#422)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**5.** 802.1Q 标签的长度是（　　）。

- A. 2 字节
- B. 4 字节
- C. 6 字节
- D. 12 字节

</div>

??? tip "答案与解析"
    **答案：B**

    802.1Q 标签 4 字节，插在源地址和类型字段之间；其中 VLAN 标识符占 12 位。

    考查：802.1Q 标签 · 认知层次：记忆 · [回看 5.2.3](chapters/05-vlan-wlan/index.md#523)
    { .quiz-meta }

<div class="quiz" data-answer="C" markdown>

**6.** IP 地址 150.20.30.40 属于（　　）。

- A. A 类
- B. C 类
- C. B 类
- D. D 类

</div>

??? tip "答案与解析"
    **答案：C**

    第一个八位组 150 在 128～191 之间，是 B 类地址。

    考查：分类 IP 地址 · 认知层次：理解 · [回看 6.3.2](chapters/06-ip-address/index.md#632)
    { .quiz-meta }

<div class="quiz" data-answer="D" markdown>

**7.** 数据报从源主机经过两台路由器到达目的主机，下列说法正确的是（　　）。

- A. 源 IP 地址每经过一台路由器改变一次
- B. 目的 MAC 地址始终是目的主机的 MAC 地址
- C. TTL 保持不变
- D. 源 IP 地址和目的 IP 地址始终不变

</div>

??? tip "答案与解析"
    **答案：D**

    不考虑 NAT 时，IP 地址全程不变；MAC 地址每一段链路都会改变；TTL 每经过一个路由器减 1。

    考查：跨网络时地址的变化 · 认知层次：理解 · [回看 7.1.3](chapters/07-routing/index.md#713)
    { .quiz-meta }

<div class="quiz" data-answer="C" markdown>

**8.** ARP 请求和 ARP 响应分别采用（　　）方式发送。

- A. 单播、单播
- B. 广播、广播
- C. 广播、单播
- D. 单播、广播

</div>

??? tip "答案与解析"
    **答案：C**

    请求不知道对方的 MAC，只能广播；响应者已从请求中知道提问者的 MAC，直接单播回复。

    考查：ARP 的工作过程 · 认知层次：理解 · [回看 8.1.2](chapters/08-arp-dhcp-nat/index.md#812)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**9.** HTTPS 默认使用的端口号是（　　）。

- A. 80
- B. 443
- C. 53
- D. 25

</div>

??? tip "答案与解析"
    **答案：B**

    HTTP 80、HTTPS 443、DNS 53、SMTP 25。

    考查：常用端口号 · 认知层次：记忆 · [回看 9.1.3](chapters/09-transport/index.md#913)
    { .quiz-meta }

<div class="quiz" data-answer="C" markdown>

**10.** 在域名 `www.xiaohe.com` 中，顶级域名是（　　）。

- A. www
- B. xiaohe
- C. com
- D. xiaohe.com

</div>

??? tip "答案与解析"
    **答案：C**

    域名从右往左级别降低，最右边的 com 是顶级域名，xiaohe.com 是二级域名。

    考查：域名的层次结构 · 认知层次：理解 · [回看 10.2.2](chapters/10-application/index.md#1022)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**11.** 下列关于对称加密的说法，正确的是（　　）。

- A. 加密和解密使用一对不同的密钥
- B. 加密和解密使用同一把密钥，速度快
- C. 公钥可以公开发布，解决了密钥分发问题
- D. 典型算法是 RSA 和 SM2

</div>

??? tip "答案与解析"
    **答案：B**

    A、C、D 描述的都是非对称加密。对称加密的典型算法是 AES、SM4。

    考查：对称加密 · 认知层次：理解 · [回看 11.2.1](chapters/11-security/index.md#1121)
    { .quiz-meta }

<div class="quiz" data-answer="C" markdown>

**12.** SNMP 中，运行在被管理设备上、负责回答管理站查询的程序叫（　　）。

- A. 管理站
- B. MIB
- C. 代理
- D. 陷阱

</div>

??? tip "答案与解析"
    **答案：C**

    管理站在管理员电脑上，代理在被管理设备上，MIB 规定能查询哪些信息，陷阱是代理主动发出的报告。

    考查：SNMP · 认知层次：记忆 · [回看 12.1.2](chapters/12-management/index.md#1212)
    { .quiz-meta }

<div class="quiz" data-answer="C" markdown>

**13.** 一个子网需要容纳 25 台主机（含网关），最合适的子网掩码是（　　）。

- A. 255.255.255.192
- B. 255.255.255.240
- C. 255.255.255.224
- D. 255.255.255.248

</div>

??? tip "答案与解析"
    **答案：C**

    2⁵ − 2 = 30 ≥ 25，主机号 5 位，前缀 /27，掩码 255.255.255.224。/26 也够但浪费；/28 只有 14 个可用地址，不够。

    考查：按主机数选掩码 · 认知层次：应用 · [回看 6.5.2](chapters/06-ip-address/index.md#652)
    { .quiz-meta }

<div class="quiz" data-answer="D" markdown>

**14.** 关于 OSPF，下列说法错误的是（　　）。

- A. 属于链路状态路由协议
- B. 每台路由器用最短路径算法计算路由
- C. 用代价衡量路径好坏
- D. 每 30 秒把整张路由表发给相邻路由器

</div>

??? tip "答案与解析"
    **答案：D**

    D 描述的是 RIP。OSPF 只在网络变化时通告变化的链路状态，平时用 Hello 报文维持邻居关系。

    考查：OSPF · 认知层次：理解 · [回看 7.4.2](chapters/07-routing/index.md#742)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**15.** TCP 的流量控制是通过（　　）实现的。

- A. 拥塞窗口
- B. 接收方在确认中通告的窗口大小
- C. 三次握手
- D. 校验和

</div>

??? tip "答案与解析"
    **答案：B**

    流量控制由接收方通过窗口字段告诉发送方自己还能接收多少；拥塞窗口用于拥塞控制。

    考查：流量控制 · 认知层次：理解 · [回看 9.5.3](chapters/09-transport/index.md#953)
    { .quiz-meta }

<div class="quiz" data-answer="C" markdown>

**16.** 用户代理把邮件发送到邮件服务器使用的协议是（　　）。

- A. POP3
- B. IMAP
- C. SMTP
- D. HTTP

</div>

??? tip "答案与解析"
    **答案：C**

    SMTP 负责发送（推），POP3 和 IMAP 负责从信箱接收（拉）。网页邮箱中浏览器和服务器之间用 HTTP，但题目问的是用户代理发送邮件的标准协议。

    考查：电子邮件协议 · 认知层次：记忆 · [回看 10.6.2](chapters/10-application/index.md#1062)
    { .quiz-meta }

<div class="quiz" data-answer="A" markdown>

**17.** 集线器工作在（　　）。

- A. 物理层
- B. 数据链路层
- C. 网络层
- D. 运输层

</div>

??? tip "答案与解析"
    **答案：A**

    集线器只对比特做放大和转发，不识别帧和地址，工作在物理层；交换机工作在数据链路层；路由器工作在网络层。

    考查：集线器 · 认知层次：记忆 · [回看 4.5.1](chapters/04-datalink/index.md#451)
    { .quiz-meta }

<div class="quiz" data-answer="C" markdown>

**18.** 客户机发出 DHCP 发现报文时，IP 首部的源地址和目的地址分别是（　　）。

- A. 192.168.1.1 和 255.255.255.255
- B. 0.0.0.0 和 192.168.1.1
- C. 0.0.0.0 和 255.255.255.255
- D. 127.0.0.1 和 255.255.255.255

</div>

??? tip "答案与解析"
    **答案：C**

    客户机还没有地址，源地址用 0.0.0.0；不知道服务器在哪，目的地址用受限广播 255.255.255.255。

    考查：DHCP 报文的地址 · 认知层次：理解 · [回看 8.3.2](chapters/08-arp-dhcp-nat/index.md#832)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**19.** 网段 192.168.8.64/27 在 ACL 中对应的通配符掩码是（　　）。

- A. 255.255.255.224
- B. 0.0.0.31
- C. 0.0.0.63
- D. 0.0.0.32

</div>

??? tip "答案与解析"
    **答案：B**

    /27 的子网掩码是 255.255.255.224，通配符掩码 = 255.255.255.255 − 255.255.255.224 = 0.0.0.31。

    考查：通配符掩码 · 认知层次：应用 · [回看 11.4.2](chapters/11-security/index.md#1142)
    { .quiz-meta }

<div class="quiz" data-answer="C" markdown>

**20.** 下列协议中，属于运输层的是（　　）。

- A. HTTP
- B. IP
- C. UDP
- D. DNS

</div>

??? tip "答案与解析"
    **答案：C**

    运输层有 TCP 和 UDP。HTTP、DNS 属于应用层，IP 属于网络层。

    考查：各层代表协议 · 认知层次：记忆 · [回看 2.4.1](chapters/02-architecture/index.md#241)
    { .quiz-meta }

**二、多项选择题**（每题 2 分，共 10 分；多选、少选、错选均不得分）

<div class="quiz quiz-multi" data-answer="BC" markdown>

**21.** 与 2.4 GHz 相比，5 GHz 频段的 WiFi（　　）。

- A. 覆盖范围更大、穿墙能力更强
- B. 速率更高
- C. 可用信道更多、干扰更少
- D. 和手机的 5G 移动通信是同一种技术

</div>

??? tip "答案与解析"
    **答案：BC**

    5 GHz 频率高，速率高、信道多、干扰少，但覆盖近、穿墙弱。WiFi 的“5G”指 5 GHz 频段，和 5G 移动通信无关。

    考查：2.4 GHz 与 5 GHz · 认知层次：理解 · [回看 5.5.2](chapters/05-vlan-wlan/index.md#552)
    { .quiz-meta }

<div class="quiz quiz-multi" data-answer="AB" markdown>

**22.** 路由表中的路由可能来自（　　）。

- A. 接口配置 IP 地址并启用后自动产生的直连路由
- B. 管理员手工配置的静态路由
- C. 交换机自学习得到的 MAC 地址表
- D. ARP 缓存

</div>

??? tip "答案与解析"
    **答案：AB**

    另外还有路由协议学到的动态路由。MAC 地址表和 ARP 缓存都不是路由表的来源。

    考查：路由的来源 · 认知层次：理解 · [回看 7.2.1](chapters/07-routing/index.md#721)
    { .quiz-meta }

<div class="quiz quiz-multi" data-answer="AC" markdown>

**23.** 关于 NAT，下列说法正确的有（　　）。

- A. 可以让使用私有地址的主机访问互联网
- B. 外网主机可以随时主动访问内网中的任何主机
- C. 能节省公网 IP 地址
- D. 可以完全代替防火墙

</div>

??? tip "答案与解析"
    **答案：AC**

    外网不能主动访问 NAT 后面的主机（除非设置端口映射）；NAT 不是专门的安全设备，不能代替防火墙。

    考查：NAT 的好处与麻烦 · 认知层次：理解 · [回看 8.4.3](chapters/08-arp-dhcp-nat/index.md#843)
    { .quiz-meta }

<div class="quiz quiz-multi" data-answer="BC" markdown>

**24.** 下列协议中，用于接收电子邮件的有（　　）。

- A. SMTP
- B. POP3
- C. IMAP
- D. FTP

</div>

??? tip "答案与解析"
    **答案：BC**

    POP3 把邮件下载到本机，IMAP 在服务器上管理邮件、多设备同步。

    考查：电子邮件协议 · 认知层次：记忆 · [回看 10.6.2](chapters/10-application/index.md#1062)
    { .quiz-meta }

<div class="quiz quiz-multi" data-answer="ACD" markdown>

**25.** 设计部所有电脑都不能访问服务器区，但设计部内部互访正常，可能的原因有（　　）。

- A. 设计部 VLAN 的网关接口被关闭
- B. 某一台设计部电脑的网线松了
- C. 三层交换机没有开启 ip routing
- D. ACL 中有拒绝设计部访问服务器区的规则

</div>

??? tip "答案与解析"
    **答案：ACD**

    影响整个部门、且只影响跨网段访问，说明问题在网关、路由或 ACL；一台电脑的网线问题只影响那一台。

    考查：缩小故障范围 · 认知层次：分析 · [回看 12.2.1](chapters/12-management/index.md#1221)
    { .quiz-meta }

**三、判断题**（每题 1 分，共 10 分）

<div class="quiz quiz-judge" data-answer="√" markdown>

**26.** 电路交换在通话期间始终占用端到端的通信资源。（　　）

</div>

??? tip "答案与解析"
    **答案：√**

    电路交换建立连接后，通路被双方独占，直到释放连接。

    考查：电路交换 · 认知层次：理解 · [回看 1.4.1](chapters/01-intro/index.md#141)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="√" markdown>

**27.** 接收方逐层去掉首部，把数据交给上一层的过程叫解封装。（　　）

</div>

??? tip "答案与解析"
    **答案：√**

    发送时加首部是封装，接收时去首部是解封装。

    考查：解封装 · 认知层次：记忆 · [回看 2.5.2](chapters/02-architecture/index.md#252)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="√" markdown>

**28.** 统计时分复用按需动态分配时隙，比普通时分复用的线路利用率高。（　　）

</div>

??? tip "答案与解析"
    **答案：√**

    普通时分复用中没有数据的用户的时隙会空着浪费，统计时分复用谁有数据给谁。

    考查：时分复用 · 认知层次：理解 · [回看 3.5.1](chapters/03-physical/index.md#351)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="×" markdown>

**29.** 普通交换机必须由管理员手工输入每台电脑的 MAC 地址后才能工作。（　　）

</div>

??? tip "答案与解析"
    **答案：×**

    交换机的 MAC 地址表是自学习得到的，即插即用，不需要手工配置。

    考查：交换机自学习 · 认知层次：理解 · [回看 4.6.1](chapters/04-datalink/index.md#461)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="×" markdown>

**30.** IP 协议能够保证数据报可靠、按顺序地到达目的主机。（　　）

</div>

??? tip "答案与解析"
    **答案：×**

    IP 提供尽力而为的服务，不保证可靠和顺序，可靠性由运输层的 TCP 负责。

    考查：IP 协议的服务 · 认知层次：理解 · [回看 6.1.2](chapters/06-ip-address/index.md#612)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="×" markdown>

**31.** 距离向量路由协议中，每台路由器都掌握整个网络的拓扑结构。（　　）

</div>

??? tip "答案与解析"
    **答案：×**

    距离向量协议只和邻居交换“到各网络的距离”，不知道全网拓扑；掌握全网地图的是链路状态协议。

    考查：距离向量与链路状态 · 认知层次：理解 · [回看 7.4.1](chapters/07-routing/index.md#741)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="√" markdown>

**32.** ping 不通某台服务器，并不一定说明网络有故障。（　　）

</div>

??? tip "答案与解析"
    **答案：√**

    很多服务器和电脑的防火墙默认不回复 ICMP 回送请求。

    考查：ping 的原理 · 认知层次：理解 · [回看 8.2.2](chapters/08-arp-dhcp-nat/index.md#822)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="√" markdown>

**33.** TCP 释放连接需要四次挥手，是因为 TCP 是全双工的，两个方向要分别关闭。（　　）

</div>

??? tip "答案与解析"
    **答案：√**

    一方发完数据只关闭自己的发送方向，另一方可能还有数据要发，所以 FIN 和 ACK 要在两个方向上各来一次。

    考查：四次挥手 · 认知层次：理解 · [回看 9.4.3](chapters/09-transport/index.md#943)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="√" markdown>

**34.** 电脑在查询 DNS 之前会先查看 hosts 文件，hosts 文件中的对应关系优先于 DNS。（　　）

</div>

??? tip "答案与解析"
    **答案：√**

    所以 hosts 文件被篡改也可能导致访问到假网站。

    考查：hosts 文件 · 认知层次：记忆 · [回看 10.2.5](chapters/10-application/index.md#1025)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="√" markdown>

**35.** 数字签名用发送方的私钥生成，接收方用发送方的公钥验证。（　　）

</div>

??? tip "答案与解析"
    **答案：√**

    只有发送方有私钥，所以签名能证明来源；验证时算出的哈希值一致，说明内容没被改过。

    考查：数字签名 · 认知层次：理解 · [回看 11.2.4](chapters/11-security/index.md#1124)
    { .quiz-meta }

**四、填空题**（每空 1 分，共 10 分）

**36.** 填空：

(1) 发送时延 = 数据长度 ÷ ____①____。

(2) 制作直通线时，两端都按 ____②____ 标准排列线序。

(3) 以太网帧末尾的 FCS 用循环冗余检验（CRC）实现 ____③____。

(4) 已知 IP 地址求 MAC 地址的协议是 ____④____。

(5) DHCP 获取地址的四个报文依次是 Discover、____⑤____、Request、ACK。

(6) 慢开始门限为 16，拥塞窗口从 1 开始，没有发生拥塞时第 5 轮的拥塞窗口为 ____⑥____。

(7) HTTPS 默认使用的端口号是 ____⑦____。

(8) Cisco 设备上编号为 100～199 的 ACL 是 ____⑧____ ACL。

(9) SNMP 代理在发生重要事件时主动向管理站发送的报告叫 ____⑨____。

(10) IPv6 地址的长度是 ____⑩____ 位。

??? tip "答案与解析"
    **参考答案：** ① 发送速率（带宽）；② T568B（两端相同的 T568A 也可以）；③ 差错检测；④ ARP；⑤ Offer；⑥ 16（1、2、4、8、16）；⑦ 443；⑧ 扩展；⑨ 陷阱（Trap）；⑩ 128

    各空对应的章节：第 1 章 · [回看 1.5.3](chapters/01-intro/index.md#153)；第 3 章 · [回看 3.4](chapters/03-physical/index.md#34)；第 4 章 · [回看 4.2](chapters/04-datalink/index.md#42)；第 8 章 · [回看 8.1](chapters/08-arp-dhcp-nat/index.md#81)；第 8 章 · [回看 8.3](chapters/08-arp-dhcp-nat/index.md#83)；第 9 章 · [回看 9.6.2](chapters/09-transport/index.md#962)；第 10 章 · [回看 10.3.6](chapters/10-application/index.md#1036)；第 11 章 · [回看 11.4.2](chapters/11-security/index.md#1142)；第 12 章 · [回看 12.1.2](chapters/12-management/index.md#1212)；第 6 章 · [回看 6.7](chapters/06-ip-address/index.md#67)。

    考查：基本概念与数据 · 认知层次：记忆
    { .quiz-meta }

**五、子网计算题**（10 分）

**37.** （1）某主机的地址为 192.168.20.77/28，求它所在子网的子网掩码、网络地址、广播地址、可用地址范围和可用主机数。主机 192.168.20.90/28 和它在同一个子网吗？（6 分）

（2）把 192.168.20.0/24 平均划分为 8 个子网，每个子网的前缀长度是多少？每个子网最多有多少台主机？写出前 3 个子网的网络地址。（4 分）

??? tip "答案与解析"
    **参考答案：**

    （1）/28 的子网掩码为 255.255.255.240，块大小 16。77 落在 64～79 之间，所以网络地址 192.168.20.64，广播地址 192.168.20.79，可用地址 192.168.20.65～192.168.20.78，可用主机数 2⁴ − 2 = 14。192.168.20.90 落在 80～95 的子网里，与它**不在**同一个子网。

    （2）8 = 2³，借 3 位，前缀 /27（子网掩码 255.255.255.224），每个子网最多 2⁵ − 2 = 30 台主机。前 3 个子网：192.168.20.0/27、192.168.20.32/27、192.168.20.64/27。

    考查：子网计算 · 认知层次：应用 · [回看 6.5](chapters/06-ip-address/index.md#65)
    { .quiz-meta }

**六、抓包分析题**（10 分）

**38.** 下面是本书抓包文件 `tcp_udp_chat.pcap` 中一次 TCP 聊天的部分帧（相对序号；“长度”是 TCP 数据长度）：

    帧  方向           标志       序号  确认号  长度
    1   43108 → 9000   SYN        0     —       0
    2   9000 → 43108   SYN, ACK   0     ①       0
    4   43108 → 9000   PSH, ACK   1     1       21
    5   9000 → 43108   ACK        1     ②       0
    6   9000 → 43108   PSH, ACK   1     22      30
    7   43108 → 9000   ACK        22    ③       0
    8   43108 → 9000   PSH, ACK   22    31      18
    9   9000 → 43108   PSH, ACK   31    40      27
    11  9000 → 43108   FIN, ACK   58    40      0
    12  43108 → 9000   ACK        40    ④       0

请回答：（1）填出 ①～④ 的确认号；（2）哪一方是服务器？哪一方先发起释放连接？（3）第 9 帧体现了什么机制？（4）同一文件第 15～18 帧是一次 UDP 聊天，它和 TCP 聊天相比，在抓包中最明显的区别是什么？

??? tip "答案与解析"
    **参考答案：**

    （1）① 1（SYN 占一个序号，0 + 1）；② 22（1 + 21）；③ 31（1 + 30）；④ 59（FIN 占一个序号，58 + 1）。（每空 1 分，共 4 分）（2）端口 9000 一方是服务器（客户端从随机端口 43108 连到 9000）；第 11 帧由服务器发出 FIN，是服务器先释放连接。（2 分）（3）捎带确认：服务器在发送自己的数据（27 字节）的同时，把对第 8 帧的确认号 40 带上。（2 分）（4）UDP 没有三次握手和四次挥手，直接发送数据，也没有序号和确认号。（2 分）

    考查：TCP 序号与确认号 · 认知层次：分析 · [回看 9.4](chapters/09-transport/index.md#94)
    { .quiz-meta }

**七、简答题**（每题 6 分，共 18 分）

**39.** 网络中有 4 台路由器 A、B、C、D，链路代价为：A–B 1，A–C 4，B–C 2，B–D 6，C–D 1。用最短路径算法求 A 到其他路由器的最短路径和代价，写出每一步。

??? tip "答案与解析"
    **参考答案：** 开始：A 为 0；B 1（经 A），C 4（经 A），D ∞。第 1 步确定 B（1）：经 B 到 C 为 1 + 2 = 3 < 4，C 更新为 3（经 B）；经 B 到 D 为 1 + 6 = 7，D 更新为 7（经 B）。第 2 步确定 C（3）：经 C 到 D 为 3 + 1 = 4 < 7，D 更新为 4（经 C）。第 3 步确定 D（4）。结果：A→B 代价 1；A→B→C 代价 3；A→B→C→D 代价 4。A 去往 B、C、D 的下一跳都是 B。

    考查：最短路径算法 · 认知层次：应用 · [回看 7.4.3](chapters/07-routing/index.md#743)
    { .quiz-meta }

**40.** 新电脑接入工作室网络后，从“没有地址”到能 ping 通网关，会依次发生哪些协议交互？请结合 `dhcp_arp.pcap` 的 12 帧说明。

??? tip "答案与解析"
    **参考答案：** ① 第 1～4 帧是 DHCP：电脑广播 Discover（源 0.0.0.0、目的 255.255.255.255）；服务器 192.168.1.1 回 Offer，提供 192.168.1.181；电脑广播 Request 表示接受；服务器回 ACK 确认，同时告知掩码 255.255.255.0、网关 192.168.1.1、DNS 和租期 12 小时。② 第 5、6 帧是 ARP：电脑广播询问“谁是 192.168.1.1”，网关单播回答自己的 MAC 地址 00:e0:fc:12:34:01。③ 第 7～12 帧是 ICMP：电脑向网关发送 3 次回送请求，网关逐一回送回答。

    考查：DHCP、ARP、ICMP 综合 · 认知层次：分析 · [回看 8.3.2](chapters/08-arp-dhcp-nat/index.md#832)
    { .quiz-meta }

**41.** 一台 Windows 电脑上不了网，请按顺序写出六步排查法，并说明每一步不正常时说明了什么问题。

??? tip "答案与解析"
    **参考答案：** ① 看网线、指示灯、WiFi 连接：不正常说明物理层问题；② `ipconfig`：地址为 169.254.x.x 说明 DHCP 没分到地址，网段、网关不对说明配置错误；③ `ping 127.0.0.1`：不通说明本机协议有问题；④ `ping 网关`：不通说明本地网络问题（网线、交换机、VLAN、网关地址）；⑤ `ping 外网 IP`：不通说明出口问题（路由、NAT、运营商线路），可用 tracert 看断在哪里；⑥ `nslookup 域名`：失败说明 DNS 问题。六步都正常而网页仍打不开，是应用层问题（代理设置、网站故障、被防火墙拦截等）。

    考查：故障排查六步法 · 认知层次：应用 · [回看 12.2.2](chapters/12-management/index.md#1222)
    { .quiz-meta }

**八、配置补全题**（12 分）

**42.** 在 3560 三层交换机 S1 上，财务部 PC 接 Fa0/2（VLAN 20，网段 192.168.8.64/27，网关 192.168.8.65），Gig0/1 连接另一台交换机并需要传送多个 VLAN，财务服务器 192.168.8.131 在 VLAN 40。要求只有财务部能访问财务服务器。请补全配置（每空 2 分）：

    S1(config)#vlan 20
    S1(config-vlan)#interface fa0/2
    S1(config-if)#switchport mode ____①____
    S1(config-if)#switchport access vlan 20
    S1(config-if)#interface gig0/1
    S1(config-if)#switchport mode ____②____
    S1(config-if)#interface vlan 20
    S1(config-if)#ip address 192.168.8.65 ____③____
    S1(config-if)#exit
    S1(config)#ip ____④____
    S1(config)#access-list 110 permit ip 192.168.8.64 ____⑤____ host 192.168.8.131
    S1(config)#access-list 110 deny ip any host 192.168.8.131
    S1(config)#access-list 110 permit ip any any
    S1(config)#interface vlan 40
    S1(config-if)#ip access-group 110 ____⑥____

??? tip "答案与解析"
    **参考答案：**

    ① `access`（接电脑的接口）；② `trunk`（交换机之间传送多个 VLAN）；③ `255.255.255.224`（/27）；④ `routing`（开启三层交换机的路由功能）；⑤ `0.0.0.31`（/27 的通配符掩码）；⑥ `out`（数据从 VLAN 40 接口离开交换机、进入服务器区时检查）。注意第三条 `permit ip any any` 不能少，否则隐含拒绝会拦掉去服务器区的其他流量。

    考查：VLAN 与 ACL 配置 · 认知层次：应用 · [回看实验 11-2](chapters/11-security/index.md#11-2)
    { .quiz-meta }
