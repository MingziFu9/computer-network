---
title: 附录 D 术语表
description: 本书主要术语的中英文名称、简明定义和例子，按章节顺序排列
---

# 附录 D 术语表

本表按章节顺序列出本书的主要术语，每个术语给出英文名称、简明定义和例子。正文中带虚线下划线的术语，把鼠标停在上面就能看到定义，点击可以跳到本表。

通用术语（如“协议”“带宽”）的译名和定义以本系列教材共用的《系列公共术语表》为准，各书保持一致。

## 第 1 章 认识计算机网络

| 术语 | 英文 | 定义 | 例子 |
|---|---|---|---|
| <span id="g-计算机网络"></span>计算机网络 | Computer Network | 用通信线路和网络设备把多台功能独立的计算机连接起来，按共同规则交换数据、共享资源的系统 | 小禾工作室 5 台电脑和 1 台打印机连成的办公网 |
| <span id="g-互连网"></span>互连网 | internet | 把多个网络连接起来形成的“网络的网络” | 把公司北京、广州两地的网络连在一起 |
| <span id="g-互联网"></span>互联网 | Internet | 全球范围内采用 TCP/IP 协议、由大量网络互连而成的最大的计算机网络，也叫因特网 | 平时说的“上网” |
| <span id="g-端系统"></span>端系统 | End System | 连在网络边缘、产生和使用数据的设备，也叫主机 | 电脑、手机、服务器、网络摄像头 |
| <span id="g-通信链路"></span>通信链路 | Communication Link | 在设备之间传输数据的通道 | 网线、光纤、WiFi 无线信道 |
| <span id="g-网络设备"></span>网络设备 | Network Device | 在链路交汇处转发或转换数据的设备 | 交换机、路由器、光猫、无线接入点 |
| <span id="g-边缘部分"></span>边缘部分 | Edge Part | 互联网中由所有端系统组成、用户直接使用的部分 | 家里的电脑和视频网站的服务器 |
| <span id="g-核心部分"></span>核心部分 | Core Part | 互联网中由大量网络和路由器组成、为边缘部分提供连通服务的部分 | 运营商的骨干网 |
| <span id="g-客户—服务器方式"></span>客户—服务器方式 | Client-Server Model | 一方请求服务、另一方提供服务的通信方式 | 浏览器（客户）访问网站服务器 |
| <span id="g-光猫"></span>光猫 | Optical Network Terminal, ONT | 运营商安装在用户家里、把光纤中的光信号与网线中的电信号相互转换的设备 | 宽带师傅装在弱电箱里的小盒子 |
| <span id="g-局域网"></span>局域网 | Local Area Network, LAN | 覆盖一栋楼或一个园区、通常由单位自己建设管理的网络 | 学校机房、工作室办公网 |
| <span id="g-广域网"></span>广域网 | Wide Area Network, WAN | 覆盖城市、国家乃至全球，通常由运营商建设的网络 | 运营商的全国骨干网 |
| <span id="g-拓扑"></span>拓扑 | Topology | 网络中设备和链路连接的几何形状，只看谁和谁相连 | 办公网是星形拓扑 |
| <span id="g-交换"></span>交换 | Switching | 中间设备把数据从一条链路转送到另一条链路的过程 | 路由器把收到的分组转发到通往目的地的接口 |
| <span id="g-电路交换"></span>电路交换 | Circuit Switching | 通信前先建立专用通路、通信期间一直独占、结束后释放的交换方式 | 老式固定电话通话 |
| <span id="g-报文交换"></span>报文交换 | Message Switching | 把整份报文存储后再转发给下一节点的交换方式 | 早期的电报网 |
| <span id="g-分组交换"></span>分组交换 | Packet Switching | 把数据切成带首部的小分组，逐个存储转发、共享线路的交换方式 | 互联网传输网页和视频 |
| <span id="g-分组"></span>分组 | Packet | 分组交换中传送的数据单元，由首部和一段数据组成，也叫数据包 | 一段视频被切成的每个小包 |
| <span id="g-存储转发"></span>存储转发 | Store and Forward | 节点先完整收下分组、检查后再转发出去的工作方式 | 路由器收下分组，查表后从另一个接口发出 |
| <span id="g-速率"></span>速率 | Data Rate | 数据在链路上每秒传送的比特数，单位 bit/s | 千兆网卡的速率是 1 Gbit/s |
| <span id="g-带宽"></span>带宽 | Bandwidth | 在计算机网络中通常指链路能达到的最高速率；在通信中指信号的频率范围 | “300 兆宽带”指最高 300 Mbit/s |
| <span id="g-吞吐量"></span>吞吐量 | Throughput | 单位时间内实际通过某个网络或接口的数据量 | 1 Gbit/s 链路上实际只跑了 200 Mbit/s |
| <span id="g-瓶颈链路"></span>瓶颈链路 | Bottleneck Link | 一条路径上速率最低、限制了端到端吞吐量的那段链路 | 有线 300 Mbps、WiFi 只有 20 Mbps 时 WiFi 是瓶颈 |
| <span id="g-时延"></span>时延 | Delay | 数据从网络一端传到另一端所需的时间，由发送、传播、处理、排队四部分组成 | ping 显示的时间反映往返时延 |
| <span id="g-发送时延"></span>发送时延 | Transmission Delay | 把一个分组的全部比特推上链路所需的时间，等于数据长度除以发送速率 | 10 MB 文件以 10 Mbit/s 发送需 8 秒 |
| <span id="g-传播时延"></span>传播时延 | Propagation Delay | 信号在链路上从一端传到另一端所需的时间，等于链路长度除以传播速度 | 1 000 km 光纤的传播时延约 5 ms |
| <span id="g-排队时延"></span>排队时延 | Queuing Delay | 分组在路由器缓存中等待被发送的时间，随网络拥挤程度变化 | 晚高峰时 ping 值明显变大 |
| <span id="g-往返时间"></span>往返时间 | Round-Trip Time, RTT | 从发出数据到收到对方确认所经历的总时间 | ping 网关显示“时间=3ms” |
| <span id="g-丢包率"></span>丢包率 | Packet Loss Rate | 一段时间内丢失的分组数占发出分组总数的比例 | 发 4 个收回 3 个，丢包率 25% |
| <span id="g-RFC"></span>RFC | Request for Comments | 互联网工程任务组发布的互联网标准文档系列 | IP 协议由 RFC 791 定义 |

## 第 2 章 网络体系结构：分层与协议

| 术语 | 英文 | 定义 | 例子 |
|---|---|---|---|
| <span id="g-网络协议"></span>网络协议 | Network Protocol | 为网络中的数据交换而建立的规则、标准或约定，简称协议 | 浏览器和网站服务器都遵守 HTTP 协议 |
| <span id="g-语法"></span>语法 | Syntax | 协议三要素之一，规定数据的格式和结构 | 以太网帧前 6 字节是目的地址 |
| <span id="g-语义"></span>语义 | Semantics | 协议三要素之一，规定各部分数据的含义和要完成的动作 | TCP 首部 SYN 为 1 表示请求建立连接 |
| <span id="g-同步"></span>同步 | Timing | 协议三要素之一，规定事件发生的先后顺序 | 先建立连接，再传数据，最后断开 |
| <span id="g-体系结构"></span>体系结构 | Network Architecture | 计算机网络各层及其协议的集合 | TCP/IP 体系结构 |
| <span id="g-OSI-参考模型"></span>OSI 参考模型 | OSI Reference Model | 国际标准化组织提出的七层网络体系结构：物理、数据链路、网络、传输、会话、表示、应用 | “二层交换机”中的“二层”沿用 OSI 层号 |
| <span id="g-TCP-IP-体系结构"></span>TCP/IP 体系结构 | TCP/IP Architecture | 互联网实际使用的四层体系结构：应用层、运输层、网际层、网络接口层 | IP 在中间，上下可接各种应用和网络，形似沙漏 |
| <span id="g-五层模型"></span>五层模型 | Five-Layer Model | 教学中综合 OSI 和 TCP/IP 的模型：应用层、运输层、网络层、数据链路层、物理层 | 本书第 3～10 章按五层由下往上讲 |
| <span id="g-应用层"></span>应用层 | Application Layer | 为用户的应用程序提供网络服务的层 | HTTP、DNS、SMTP |
| <span id="g-运输层"></span>运输层 | Transport Layer | 为两台主机中的进程提供端到端通信的层，也叫传输层 | TCP、UDP |
| <span id="g-网络层"></span>网络层 | Network Layer | 负责分组的寻址和路由选择、把分组从源主机送到目的主机的层 | IP 协议、路由器 |
| <span id="g-数据链路层"></span>数据链路层 | Data Link Layer | 在相邻节点之间以帧为单位传送数据的层 | 以太网、交换机 |
| <span id="g-物理层"></span>物理层 | Physical Layer | 在传输介质上透明地传送比特流的层 | 网线、光纤、集线器 |
| <span id="g-封装"></span>封装 | Encapsulation | 发送方每一层在上层数据前加上本层首部（链路层还加尾部）的过程 | HTTP 请求被依次加上 TCP、IP、以太网首部 |
| <span id="g-解封装"></span>解封装 | Decapsulation | 接收方每一层读取并去掉本层首部、把数据交给上层的过程 | 服务器去掉以太网、IP、TCP 首部后得到 HTTP 请求 |
| <span id="g-首部"></span>首部 | Header | 加在数据前面、存放本层控制信息的部分 | IP 首部里有源和目的 IP 地址 |
| <span id="g-协议数据单元"></span>协议数据单元 | Protocol Data Unit, PDU | 对等层之间交换的数据单元，各层名称不同 | 应用层报文、运输层报文段、网络层分组、链路层帧 |
| <span id="g-帧"></span>帧 | Frame | 数据链路层的协议数据单元 | 以太网帧 |
| <span id="g-对等层通信"></span>对等层通信 | Peer-to-Peer Layer Communication | 通信双方同一层之间按协议交换信息，只读对方同层的首部 | 服务器的 TCP 只读电脑的 TCP 写的首部 |
| <span id="g-服务"></span>服务 | Service | 下层为相邻上层提供的功能，是垂直关系 | 运输层为应用层提供可靠传输服务 |
| <span id="g-服务访问点"></span>服务访问点 | Service Access Point, SAP | 相邻两层之间交换信息的接口 | 端口号是运输层与应用层之间的服务访问点 |
| <span id="g-Wireshark"></span>Wireshark | Wireshark | 免费开源的网络抓包和协议分析软件 | 打开 web_visit.pcap 逐层查看分组 |
| <span id="g-抓包"></span>抓包 | Packet Capture | 把流经网卡的帧记录下来以供分析 | 用 Wireshark 记录访问网站时的数据 |
| <span id="g-显示过滤器"></span>显示过滤器 | Display Filter | Wireshark 中只显示符合条件的帧的过滤表达式 | `ip.addr == 203.0.113.10` |

## 第 3 章 物理层：从比特到信号

| 术语 | 英文 | 定义 | 例子 |
|---|---|---|---|
| <span id="g-数据"></span>数据 | Data | 要传送的信息，在计算机里表示为 0 和 1 | 一张照片在硬盘上就是一长串 0 和 1 |
| <span id="g-信号"></span>信号 | Signal | 数据的电气或电磁表现，分为模拟信号和数字信号 | 网线上的电压变化、WiFi 的电磁波 |
| <span id="g-模拟信号"></span>模拟信号 | Analog Signal | 随时间连续变化的信号 | 声音的波形、老式电话线上的信号 |
| <span id="g-数字信号"></span>数字信号 | Digital Signal | 只取几个固定值的信号 | 高电平表示 1、低电平表示 0 |
| <span id="g-码元"></span>码元 | Signal Element | 信号波形中代表一个数字值的基本波形，即一个时间小格里的信号 | 一个码元有 16 种状态时可携带 4 个比特 |
| <span id="g-信道"></span>信道 | Channel | 向某一个方向传送信息的通路 | 一条网线里有发送信道和接收信道 |
| <span id="g-单工"></span>单工 | Simplex | 只能单向传送的通信方式 | 广播电台、电视 |
| <span id="g-半双工"></span>半双工 | Half Duplex | 双方都能发送但不能同时发送的通信方式 | 对讲机；WiFi 同一信道 |
| <span id="g-全双工"></span>全双工 | Full Duplex | 双方可以同时发送和接收的通信方式 | 打电话；交换机连接的以太网 |
| <span id="g-基带信号"></span>基带信号 | Baseband Signal | 来自信源、未经调制的原始数字信号 | 电脑网卡送出的 0、1 电平 |
| <span id="g-编码"></span>编码 | Encoding | 把数字信号变换成另一种数字信号，以便在线路上传输 | 以太网的曼彻斯特编码 |
| <span id="g-调制"></span>调制 | Modulation | 把数字信号装到高频载波上变成模拟信号，分调幅、调频、调相 | 光猫、WiFi 路由器都要做调制 |
| <span id="g-曼彻斯特编码"></span>曼彻斯特编码 | Manchester Encoding | 每个码元中间都有跳变的编码，本书约定向上跳为 1、向下跳为 0，自带同步 | 早期 10 Mbit/s 以太网 |
| <span id="g-码间串扰"></span>码间串扰 | Intersymbol Interference | 码元传得太快，前后码元的波形混在一起无法分辨的现象 | 奈氏准则给出了避免它的速率上限 |
| <span id="g-频带宽度"></span>频带宽度 | Bandwidth | 信道能通过的最高频率减去最低频率，单位赫兹（Hz） | 电话话音信道约 3 100 Hz |
| <span id="g-波特"></span>波特 | Baud | 码元传输速率的单位，每秒传输一个码元为 1 波特 | 一个码元带 4 比特时，1 000 波特 = 4 000 bit/s |
| <span id="g-信噪比"></span>信噪比 | Signal-to-Noise Ratio | 信号平均功率与噪声平均功率之比，常用分贝表示 | 30 dB 表示信号功率是噪声的 1 000 倍 |
| <span id="g-信道容量"></span>信道容量 | Channel Capacity | 带噪声信道的极限信息传输速率，由香农公式给出 | C = W log₂(1 + S/N) |
| <span id="g-香农公式"></span>香农公式 | Shannon Formula | C = W log₂(1 + S/N)，给出带宽和信噪比一定时的极限传输速率 | 带宽 3 000 Hz、信噪比 30 dB 时约 30 kbit/s |
| <span id="g-双绞线"></span>双绞线 | Twisted Pair | 把两根绝缘铜线按一定规律绞在一起以减少干扰的传输介质，一段最长 100 米 | 办公室的网线 |
| <span id="g-直通线"></span>直通线 | Straight-through Cable | 两端都按 T568B 线序制作的网线，用来连接不同种类设备 | 电脑连交换机 |
| <span id="g-光纤"></span>光纤 | Optical Fiber | 用光脉冲传输数据的传输介质，带宽大、损耗小、抗干扰 | 运营商骨干网、光纤到户 |
| <span id="g-单模光纤"></span>单模光纤 | Single-mode Fiber | 纤芯很细、只让一条光线直线传播的光纤，适合远距离 | 城市之间的长途光缆 |
| <span id="g-多模光纤"></span>多模光纤 | Multi-mode Fiber | 纤芯较粗、允许多条光线反射传播的光纤，适合短距离 | 机房内交换机之间的连接 |
| <span id="g-光纤到户"></span>光纤到户 | Fiber To The Home | 把光纤直接铺进用户家中的宽带接入方式，简称 FTTH | 家里的千兆宽带 |
| <span id="g-无源光网络"></span>无源光网络 | Passive Optical Network | 用无源分光器把一根光纤分给多户使用的光纤接入网，简称 PON | 光猫背后标着 PON 的接口 |
| <span id="g-复用"></span>复用 | Multiplexing | 让多路信号共享同一条传输线路的技术 | 一根光纤同时传上百路信号 |
| <span id="g-时分复用"></span>时分复用 | Time Division Multiplexing | 把时间分成时隙，各路信号轮流占用整个频带的复用方式 | 传统电话中继线 |
| <span id="g-波分复用"></span>波分复用 | Wavelength Division Multiplexing | 在一根光纤中同时传多种不同波长的光，是光的频分复用 | 运营商骨干网 |
| <span id="g-光模块"></span>光模块 | Optical Module | 在光纤两端把电信号和光信号互相转换的部件 | 插在交换机光口上的 SFP 模块 |

## 第 4 章 数据链路层与以太网交换

| 术语 | 英文 | 定义 | 例子 |
|---|---|---|---|
| <span id="g-链路"></span>链路 | Link | 从一个节点到相邻节点的一段物理线路，中间没有任何其他交换节点 | 电脑到交换机的一根网线 |
| <span id="g-封装成帧"></span>封装成帧 | Framing | 在一段数据的前后加上首部和尾部构成帧，并标出帧的开始和结束 | 写信时开头写称呼、结尾写落款 |
| <span id="g-透明传输"></span>透明传输 | Transparent Transmission | 无论数据中出现什么比特组合都能原样传过去，数据链路层好像“看不见” | PPP 用字节填充实现透明传输 |
| <span id="g-差错检测"></span>差错检测 | Error Detection | 接收方检查收到的帧在传输中是否出错 | 以太网用 CRC 做差错检测 |
| <span id="g-零比特填充"></span>零比特填充 | Zero-bit Stuffing | 发送方每遇到连续 5 个 1 就插入一个 0，接收方再删掉，避免数据中出现帧标志 | HDLC、同步传输的 PPP |
| <span id="g-误码率"></span>误码率 | Bit Error Rate | 传错的比特数占传输总比特数的比例 | 误码率 10⁻¹⁰ 表示平均一百亿个比特错一个 |
| <span id="g-循环冗余检验"></span>循环冗余检验 | Cyclic Redundancy Check | 用约定的除数对数据做除法得到余数作为检验值，接收方重算比对来发现错误，简称 CRC | 以太网帧末尾的 4 字节 CRC-32 |
| <span id="g-帧检验序列"></span>帧检验序列 | Frame Check Sequence | 附在帧末尾的检验值，简称 FCS | 以太网帧的最后 4 个字节 |
| <span id="g-PPP"></span>PPP | Point-to-Point Protocol | 点对点协议，用于点对点链路，只做差错检测、出错丢弃，可进行身份认证 | 早年电话拨号上网 |
| <span id="g-PPPoE"></span>PPPoE | PPP over Ethernet | 在以太网上运行的 PPP，家庭宽带拨号上网常用 | 路由器里填的宽带账号和密码 |
| <span id="g-以太网"></span>以太网 | Ethernet | 由 IEEE 802.3 标准规定的局域网技术，今天局域网的绝对主流 | 办公室网线连接的网络 |
| <span id="g-MAC-地址"></span>MAC 地址 | MAC Address | 固化在网卡中的 48 位硬件地址，前 24 位是厂商编号 | 00:e0:4c:68:01:0a |
| <span id="g-OUI"></span>OUI | Organizationally Unique Identifier | IEEE 分配给厂商的 24 位编号，即 MAC 地址的前 24 位 | 00:e0:4c 属于瑞昱半导体 |
| <span id="g-广播地址"></span>广播地址 | Broadcast Address | 表示发给本网络所有主机的地址：MAC 广播地址是 48 位全 1；IP 广播地址是主机号全 1 的地址（第 6 章） | ff:ff:ff:ff:ff:ff；192.168.8.0/24 的广播地址 192.168.8.255 |
| <span id="g-单播"></span>单播 | Unicast | 发给某一个特定接收方的通信方式 | 电脑把网页请求发给路由器 |
| <span id="g-多播"></span>多播 | Multicast | 发给一组接收方的通信方式，也叫组播 | IPTV、视频会议 |
| <span id="g-最大传送单元"></span>最大传送单元 | Maximum Transmission Unit | 帧的数据部分允许的最大长度，简称 MTU，以太网为 1500 字节 | IP 数据报超过 1500 字节要分片 |
| <span id="g-CSMA-CD"></span>CSMA/CD | Carrier Sense Multiple Access with Collision Detection | 载波监听多点接入 / 碰撞检测：先听后说、边说边听、碰撞后随机退避 | 早期总线式和集线器以太网 |
| <span id="g-争用期"></span>争用期 | Contention Period | 信号在总线上往返一次的时间，10 Mbit/s 以太网为 51.2 微秒 | 决定了最短帧长 64 字节 |
| <span id="g-集线器"></span>集线器 | Hub | 对比特放大后从所有其他接口发出的设备，工作在物理层 | 已基本淘汰的“八口 HUB” |
| <span id="g-交换机"></span>交换机 | Switch | 根据目的 MAC 地址转发帧的设备，工作在数据链路层 | 办公室机柜里的 24 口交换机 |
| <span id="g-MAC-地址表"></span>MAC 地址表 | MAC Address Table | 交换机记录“哪个 MAC 地址在哪个接口”的表，靠自学习建立 | show mac address-table 显示的内容 |
| <span id="g-冲突域"></span>冲突域 | Collision Domain | 同一时间只能有一台设备发送、否则会发生碰撞的范围 | 集线器所有接口同属一个冲突域 |
| <span id="g-广播域"></span>广播域 | Broadcast Domain | 一个广播帧能到达的所有设备组成的范围 | 交换机所有接口同属一个广播域，路由器隔离广播域 |
| <span id="g-自学习"></span>自学习 | Self-learning | 交换机把收到的帧的源 MAC 地址和接收接口记入地址表的过程 | 交换机插上就能用 |
| <span id="g-泛洪"></span>泛洪 | Flooding | 交换机把帧从除接收接口以外的所有接口发出 | 目的地址未知或广播时 |
| <span id="g-广播风暴"></span>广播风暴 | Broadcast Storm | 网络存在环路时广播帧无休止地循环、越来越多，导致网络瘫痪 | 一根网线两头插在同一台交换机上 |
| <span id="g-生成树协议"></span>生成树协议 | Spanning Tree Protocol | 交换机自动阻塞环路中的某些接口以消除环路的协议，简称 STP | Packet Tracer 中接口刚连上时的橙灯 |
| <span id="g-RoCE"></span>RoCE | RDMA over Converged Ethernet | 在以太网上实现远程直接内存访问的技术，AI 集群常用 | GPU 服务器之间交换训练数据 |

## 第 5 章 VLAN 与无线局域网

| 术语 | 英文 | 定义 | 例子 |
|---|---|---|---|
| <span id="g-VLAN"></span>VLAN | Virtual LAN | 虚拟局域网：在交换机上把一个物理局域网按逻辑划分成多个广播域的技术 | 设计部 VLAN 10、财务部 VLAN 20 |
| <span id="g-Access-口"></span>Access 口 | Access Port | 只属于一个 VLAN 的交换机接口，一般连接电脑，收发普通以太网帧 | switchport mode access |
| <span id="g-Trunk-口"></span>Trunk 口 | Trunk Port | 可以同时传送多个 VLAN 帧的交换机接口，一般用于交换机之间，帧带 802.1Q 标签 | switchport mode trunk |
| <span id="g-802.1Q"></span>802.1Q | IEEE 802.1Q | 规定 VLAN 标签格式的 IEEE 标准：在源地址和类型之间插入 4 字节标签 | Wireshark 中的 802.1Q Virtual LAN |
| <span id="g-VLAN-标识符"></span>VLAN 标识符 | VLAN Identifier | 802.1Q 标签中 12 位的 VLAN 号，简称 VID，可用 1～4094 | ID: 10 |
| <span id="g-单臂路由"></span>单臂路由 | Router on a Stick | 路由器用一个物理接口连到交换机 Trunk 口，划分子接口实现 VLAN 间通信 | 小网络中让财务部和设计部互通 |
| <span id="g-三层交换机"></span>三层交换机 | Layer 3 Switch | 能在内部完成 VLAN 之间转发的交换机，兼具交换和路由功能 | 企业网的核心交换机 |
| <span id="g-链路聚合"></span>链路聚合 | Link Aggregation | 把多根物理链路捆绑成一条逻辑链路，叠加带宽并互为备份 | 两根千兆线当两千兆用 |
| <span id="g-无线局域网"></span>无线局域网 | Wireless LAN | 通过无线电波接入的局域网，简称 WLAN | 办公室的 WiFi |
| <span id="g-802.11"></span>802.11 | IEEE 802.11 | 无线局域网的 IEEE 标准系列 | 802.11ax 即 WiFi 6 |
| <span id="g-WiFi"></span>WiFi | Wi-Fi | 基于 802.11 标准的无线局域网的通称，新一代用数字代号命名 | WiFi 6、WiFi 7 |
| <span id="g-CSMA-CA"></span>CSMA/CA | Carrier Sense Multiple Access with Collision Avoidance | 载波监听多点接入 / 碰撞避免：先听、随机退避、发送后等确认 | WiFi 的介质访问方式 |
| <span id="g-确认"></span>确认 | Acknowledgement | 接收方正确收到数据后发回的回复，简称 ACK | 802.11 每收到一帧都要确认 |
| <span id="g-无线路由器"></span>无线路由器 | Wireless Router | 集成了路由器、交换机和无线接入点功能的设备 | 家里的 WiFi 路由器 |
| <span id="g-AP"></span>AP | Access Point | 无线接入点，把无线设备接入有线网络的设备 | 企业每个房间天花板上的吸顶 AP |
| <span id="g-Mesh-组网"></span>Mesh 组网 | Mesh Networking | 多台路由器互相连接组成一个无线网络，名字密码相同、自动切换 | 大户型住宅的子母路由 |
| <span id="g-SSID"></span>SSID | Service Set Identifier | 无线网络的名字 | 手机 WiFi 列表里的 Xiaohe-Office |
| <span id="g-WPA2"></span>WPA2 | Wi-Fi Protected Access 2 | 使用 AES 加密的无线安全标准，目前广泛使用，需配合强密码 | WPA2-PSK（个人版） |
| <span id="g-WPA3"></span>WPA3 | Wi-Fi Protected Access 3 | 新一代无线安全标准，用 SAE 改进密码交换，更难被暴力破解 | 新路由器的 WPA3 选项 |
| <span id="g-访客网络"></span>访客网络 | Guest Network | 单独的 SSID 和密码，只能上网、不能访问内部网络的无线网络 | 给来访客户用的 WiFi |

## 第 6 章 IP 地址：IPv4、子网划分与 IPv6

| 术语 | 英文 | 定义 | 例子 |
|---|---|---|---|
| <span id="g-IP-地址"></span>IP 地址 | IP Address | 网络层给主机或路由器接口分配的地址，IPv4 为 32 位，IPv6 为 128 位 | 192.168.8.11 |
| <span id="g-IP-协议"></span>IP 协议 | Internet Protocol | 网际协议，互联网网络层的核心协议，提供尽力而为的数据报服务 | IPv4、IPv6 |
| <span id="g-尽力而为"></span>尽力而为 | Best Effort | 尽最大努力交付，但不保证可靠、不保证顺序、不保证不重复的服务方式 | IP 协议的服务 |
| <span id="g-IPv4-地址"></span>IPv4 地址 | IPv4 Address | 32 位的 IP 地址，用点分十进制书写 | 203.0.113.10 |
| <span id="g-点分十进制"></span>点分十进制 | Dotted Decimal Notation | 把 32 位地址分成 4 组、每组写成十进制、用点隔开的写法 | 11000000 10101000 ... 写成 192.168.... |
| <span id="g-网络号"></span>网络号 | Network ID | IP 地址中标识主机所在网络的部分 | 192.168.8.0/24 中的 192.168.8 |
| <span id="g-主机号"></span>主机号 | Host ID | IP 地址中标识网络中某一台主机的部分 | 192.168.8.11/24 中的 11 |
| <span id="g-网络地址"></span>网络地址 | Network Address | 主机号全 0 的地址，代表网络本身，不能分配给主机 | 192.168.8.96/27 |
| <span id="g-环回地址"></span>环回地址 | Loopback Address | 发给本机自己的地址，IPv4 为 127 开头，IPv6 为 ::1 | ping 127.0.0.1 |
| <span id="g-链路本地地址"></span>链路本地地址 | Link-local Address | 只在本链路有效的地址：IPv4 为 169.254.x.x，IPv6 为 fe80:: 开头 | 获取不到 DHCP 地址时出现 169.254.x.x |
| <span id="g-私有地址"></span>私有地址 | Private Address | 可在内部网络自由使用、不能直接在互联网上使用的地址：10.0.0.0/8、172.16.0.0/12、192.168.0.0/16 | 家里的 192.168.1.x |
| <span id="g-子网掩码"></span>子网掩码 | Subnet Mask | 与 IP 地址配合、用 1 标出网络号、0 标出主机号的 32 位数 | 255.255.255.224 |
| <span id="g-CIDR"></span>CIDR | Classless Inter-Domain Routing | 无分类域间路由：取消 A、B、C 类，网络前缀可为任意长度，用斜线记法表示 | 192.168.8.0/24 |
| <span id="g-前缀长度"></span>前缀长度 | Prefix Length | 斜线记法中斜线后的数字，即网络号的位数 | /27 表示网络号 27 位 |
| <span id="g-块大小"></span>块大小 | Block Size | 一个子网包含的地址数，在最后一个非 255 的八位组上等于 256 减去掩码值 | /27 的块大小为 32 |
| <span id="g-子网划分"></span>子网划分 | Subnetting | 从主机号中借位作为子网号，把一个网络分成多个子网 | 把 /24 分成 4 个 /26 |
| <span id="g-变长子网掩码"></span>变长子网掩码 | Variable Length Subnet Mask | 同一网络中的各子网使用不同长度的前缀、按需分配，简称 VLSM | 设计部 /26、服务器 /29 |
| <span id="g-路由聚合"></span>路由聚合 | Route Aggregation | 把多个连续的网络合并成一个更大的网络来表示，减少路由表项 | 192.168.8.0/24 和 192.168.9.0/24 合并为 192.168.8.0/23 |
| <span id="g-生存时间"></span>生存时间 | Time To Live | IP 首部中限制数据报最多经过多少个路由器的字段，简称 TTL，每过一个路由器减 1 | Linux 默认 64，Windows 默认 128 |
| <span id="g-协议"></span>协议 | Protocol（IP 首部字段） | IP 首部中指出数据部分交给哪个上层协议的字段：1 ICMP、6 TCP、17 UDP | Protocol: TCP (6) |
| <span id="g-分片"></span>分片 | Fragmentation | IP 数据报大于链路 MTU 时被切成几片分别传送、到目的主机再重组 | 首部的 Don't fragment 标志 |
| <span id="g-IPv6"></span>IPv6 | Internet Protocol version 6 | 下一代 IP 协议，地址 128 位，首部固定 40 字节 | 我国推进 IPv6 规模部署 |
| <span id="g-冒号十六进制"></span>冒号十六进制 | Colon Hexadecimal Notation | IPv6 地址的写法：8 组、每组 4 个十六进制数，用冒号隔开 | 2001:db8::ff00:42:8329 |

## 第 7 章 路由：数据包怎么找路

| 术语 | 英文 | 定义 | 例子 |
|---|---|---|---|
| <span id="g-路由器"></span>路由器 | Router | 连接不同网络、根据目的 IP 地址查路由表转发数据报的设备，工作在网络层 | 总部与分店之间的 R1、R2 |
| <span id="g-转发"></span>转发 | Forwarding | 路由器收到数据报后查路由表、从合适接口送出的过程（交换机按 MAC 地址表转发帧也叫转发） | 每个数据报都要做，必须很快 |
| <span id="g-路由选择"></span>路由选择 | Routing | 决定到各网络的路径、建立和更新路由表的过程 | OSPF 计算最短路径 |
| <span id="g-默认网关"></span>默认网关 | Default Gateway | 主机上配置的本网段路由器接口地址，发往其他网段的数据都交给它 | 192.168.8.1 |
| <span id="g-路由表"></span>路由表 | Routing Table | 路由器中记录“去往某网络从哪里走”的表，核心是目的网络、下一跳和出接口 | show ip route 的输出 |
| <span id="g-下一跳"></span>下一跳 | Next Hop | 去往目的网络时，下一个路由器的接口地址 | via 10.0.12.2 |
| <span id="g-直接交付"></span>直接交付 | Direct Delivery | 目的网络就连在本路由器上，不经其他路由器直接送达 | C 开头的直连路由 |
| <span id="g-默认路由"></span>默认路由 | Default Route | 目的网络为 0.0.0.0/0、匹配所有地址的路由，查不到更具体路由时使用 | ip route 0.0.0.0 0.0.0.0 10.0.12.1 |
| <span id="g-最长前缀匹配"></span>最长前缀匹配 | Longest Prefix Match | 多条路由都匹配时选前缀最长（最具体）的一条 | /25 优先于 /24 |
| <span id="g-静态路由"></span>静态路由 | Static Route | 管理员手工配置的路由 | ip route 192.168.9.0 255.255.255.0 10.0.12.2 |
| <span id="g-动态路由"></span>动态路由 | Dynamic Routing | 路由器之间运行路由协议自动交换信息、计算和更新的路由 | OSPF 学到的 O 开头路由 |
| <span id="g-距离向量"></span>距离向量 | Distance Vector | 路由器只和邻居交换“到各网络的距离”的路由方式 | RIP |
| <span id="g-RIP"></span>RIP | Routing Information Protocol | 路由信息协议，距离向量协议，以跳数为度量，最大 15 跳 | 小型网络 |
| <span id="g-跳数"></span>跳数 | Hop Count | 数据报经过的路由器个数，RIP 用它衡量距离 | 16 跳表示不可达 |
| <span id="g-链路状态"></span>链路状态 | Link State | 每台路由器向全网通告自己的链路信息、建立全网拓扑后计算路由的方式 | OSPF |
| <span id="g-OSPF"></span>OSPF | Open Shortest Path First | 开放最短路径优先，链路状态协议，用代价度量，收敛快，可分区域 | 实验 7-2 的三台路由器 |
| <span id="g-代价"></span>代价 | Cost | OSPF 衡量路径好坏的数值，通常由接口带宽算出，越小越好 | 千兆链路代价为 1 |
| <span id="g-最短路径算法"></span>最短路径算法 | Shortest Path Algorithm | 由近及远逐个确定节点最短距离的算法，即迪杰斯特拉算法 | OSPF 用它计算路由 |
| <span id="g-自治系统"></span>自治系统 | Autonomous System | 由一个机构独立管理的网络，有自己的编号，简称 AS | 中国电信 ChinaNet 是 AS4134 |
| <span id="g-BGP"></span>BGP | Border Gateway Protocol | 边界网关协议，自治系统之间交换路由信息的协议 | 运营商之间互联 |
| <span id="g-管理距离"></span>管理距离 | Administrative Distance | 思科设备表示路由来源可信度的数值，越小越可信 | 直连 0、静态 1、OSPF 110、RIP 120 |
| <span id="g-通配符掩码"></span>通配符掩码 | Wildcard Mask | 子网掩码按位取反的结果，用于 OSPF 的 network 命令等 | /26 的通配符掩码为 0.0.0.63 |

## 第 8 章 网络层的好帮手：ARP、ICMP、DHCP 与 NAT

| 术语 | 英文 | 定义 | 例子 |
|---|---|---|---|
| <span id="g-ARP"></span>ARP | Address Resolution Protocol | 地址解析协议：已知同一网段内主机的 IP 地址，查出它的 MAC 地址 | “谁是 192.168.1.1？请告诉 192.168.1.181” |
| <span id="g-ARP-缓存"></span>ARP 缓存 | ARP Cache | 主机保存的 IP 地址与 MAC 地址对照表，条目过几分钟自动删除 | arp -a 的输出 |
| <span id="g-ARP-欺骗"></span>ARP 欺骗 | ARP Spoofing | 攻击者发送伪造的 ARP 响应冒充他人，截获或篡改通信的攻击 | 冒充网关的中间人攻击 |
| <span id="g-ICMP"></span>ICMP | Internet Control Message Protocol | 网际控制报文协议：报告 IP 传输中的差错或询问情况，装在 IP 数据报中传送 | ping、tracert 用到的协议 |
| <span id="g-回送请求"></span>回送请求 | Echo Request | ICMP 类型 8，询问对方是否可达 | ping 发出的请求 |
| <span id="g-回送回答"></span>回送回答 | Echo Reply | ICMP 类型 0，对回送请求的回复 | ping 收到的 Reply |
| <span id="g-终点不可达"></span>终点不可达 | Destination Unreachable | ICMP 类型 3，路由器找不到路或目的主机无对应服务时发出 | 路由表中没有匹配路由 |
| <span id="g-时间超过"></span>时间超过 | Time Exceeded | ICMP 类型 11，数据报 TTL 减到 0 被丢弃时发出 | “TTL 传输中过期” |
| <span id="g-DHCP"></span>DHCP | Dynamic Host Configuration Protocol | 动态主机配置协议：自动为主机分配 IP 地址、掩码、网关和 DNS 服务器 | 笔记本插上网线就有了地址 |
| <span id="g-地址池"></span>地址池 | Address Pool | DHCP 服务器可以分配出去的一组地址 | 192.168.8.11～192.168.8.62 |
| <span id="g-租期"></span>租期 | Lease Time | DHCP 分配的地址可以使用的期限，过半时客户机申请续租 | 12 小时（43 200 秒） |
| <span id="g-DHCP-中继"></span>DHCP 中继 | DHCP Relay | 路由器把 DHCP 广播转发给其他网段的 DHCP 服务器，使一台服务器服务多个网段 | 三层交换机上的 ip helper-address |
| <span id="g-NAT"></span>NAT | Network Address Translation | 网络地址转换：在出口路由器把私有地址替换为公网地址 | 家里所有设备共用一个公网地址上网 |
| <span id="g-端口地址转换"></span>端口地址转换 | Port Address Translation | 同时转换 IP 地址和端口号的 NAT，一个公网地址可供多台主机使用，简称 PAT 或 NAPT | ip nat inside source ... overload |
| <span id="g-NAT-转换表"></span>NAT 转换表 | NAT Translation Table | NAT 路由器记录内部地址端口与公网地址端口对应关系的表 | show ip nat translations 的输出 |
| <span id="g-运营商级-NAT"></span>运营商级 NAT | Carrier-Grade NAT | 运营商在其网络出口为大量用户统一做的 NAT | 手机上网拿到 100.64.x.x 地址 |

## 第 9 章 传输层：TCP 与 UDP

| 术语 | 英文 | 定义 | 例子 |
|---|---|---|---|
| <span id="g-运输层"></span>运输层 | Transport Layer | 也叫传输层，在两台主机的进程之间提供端到端的通信服务，主要协议是 TCP 和 UDP | 网页、聊天、下载的数据都要经过运输层 |
| <span id="g-进程"></span>进程 | Process | 正在运行的程序，是运输层通信的真正双方 | 同时打开的浏览器和微信是两个进程 |
| <span id="g-端口号"></span>端口号 | Port Number | 16 位的编号（0～65535），用来区分同一台主机上的不同进程，相当于公司的分机号 | 网页服务器默认用 80 端口 |
| <span id="g-熟知端口"></span>熟知端口 | Well-known Port | 0～1023 号端口，固定分配给常用的服务器程序 | HTTP 80、HTTPS 443、DNS 53 |
| <span id="g-套接字"></span>套接字 | Socket | IP 地址加端口号，唯一标识网络中的一个通信端点；也指程序进行网络通信的编程接口 | 192.168.1.10:43108 |
| <span id="g-UDP"></span>UDP | User Datagram Protocol | 用户数据报协议，无连接、不保证可靠交付、首部只有 8 字节，简单快速 | DNS 查询、视频会议常用 UDP |
| <span id="g-TCP"></span>TCP | Transmission Control Protocol | 传输控制协议，面向连接、可靠、面向字节流，提供流量控制和拥塞控制 | 网页浏览、文件下载用 TCP |
| <span id="g-面向连接"></span>面向连接 | Connection-oriented | 通信前先建立连接、通信后释放连接的工作方式 | TCP 先三次握手再传数据 |
| <span id="g-序号"></span>序号 | Sequence Number | TCP 首部字段，表示本报文段数据第一个字节的编号；TCP 对每个字节编号 | 第 4 帧序号为 1，表示从第 1 个字节开始 |
| <span id="g-确认号"></span>确认号 | Acknowledgment Number | TCP 首部字段，表示期望收到对方下一个字节的编号，即之前的数据都已收到 | 确认号 22 表示前 21 个字节都收到了 |
| <span id="g-SYN"></span>SYN | Synchronize | TCP 标志位，置 1 表示请求建立连接 | 三次握手的第一个报文段只带 SYN |
| <span id="g-ACK"></span>ACK | Acknowledgment | TCP 标志位，置 1 表示确认号字段有效；连接建立后的报文段 ACK 都为 1 | 三次握手的第三个报文段是纯 ACK |
| <span id="g-FIN"></span>FIN | Finish | TCP 标志位，置 1 表示本方数据已发送完毕，请求释放这个方向的连接 | 四次挥手的第一个报文段带 FIN |
| <span id="g-三次握手"></span>三次握手 | Three-way Handshake | TCP 建立连接的过程：SYN、SYN+ACK、ACK 三个报文段 | tcp_udp_chat.pcap 第 1～3 帧 |
| <span id="g-四次挥手"></span>四次挥手 | Four-way Wave | TCP 释放连接的过程：两个方向各发一个 FIN 并各得到一个确认 | tcp_udp_chat.pcap 第 11～14 帧 |
| <span id="g-捎带确认"></span>捎带确认 | Piggybacking | 在发送数据的同时把确认号一起带上，不单独发确认报文 | tcp_udp_chat.pcap 第 9 帧 |
| <span id="g-超时重传"></span>超时重传 | Retransmission on Timeout | 发送方在规定时间内没有收到确认，就重新发送该报文段 | 挂号信过期没收到回执就再寄一封 |
| <span id="g-滑动窗口"></span>滑动窗口 | Sliding Window | 允许连续发送窗口内的多个报文段而不必逐个等待确认，收到确认后窗口向前滑动 | 窗口为 4 时可连发 4 个报文段 |
| <span id="g-流量控制"></span>流量控制 | Flow Control | 接收方通过窗口字段限制发送方的速率，防止接收缓存溢出 | 接收方把窗口减为 0，让发送方暂停 |
| <span id="g-拥塞控制"></span>拥塞控制 | Congestion Control | 发送方根据网络拥堵情况调整发送速率，防止过多数据注入网络 | 发生超时后拥塞窗口重置为 1 |
| <span id="g-拥塞窗口"></span>拥塞窗口 | Congestion Window (cwnd) | 发送方根据网络情况维护的变量，实际发送窗口取它和接收窗口中较小的一个 | cwnd 为 8 表示一轮最多发 8 个报文段 |
| <span id="g-慢开始"></span>慢开始 | Slow Start | 拥塞窗口从 1 开始、每个往返时间翻倍增长，直到达到慢开始门限 | 1、2、4、8、16 |
| <span id="g-拥塞避免"></span>拥塞避免 | Congestion Avoidance | 拥塞窗口达到门限后每个往返时间只加 1，缓慢增长 | 16、17、18、19 |
| <span id="g-快重传"></span>快重传 | Fast Retransmit | 连续收到 3 个重复确认时立即重传丢失的报文段，不等计时器超时 | 收到 3 个确认号都是 5 的确认，马上重传 5 号 |
| <span id="g-快恢复"></span>快恢复 | Fast Recovery | 快重传后把门限减为当前拥塞窗口的一半，拥塞窗口直接设为新门限，进入拥塞避免 | cwnd 12 时收到 3 个重复确认，门限和 cwnd 都变为 6 |
| <span id="g-QUIC"></span>QUIC | QUIC | 基于 UDP、在应用层实现可靠传输和加密的新型运输协议，是 HTTP/3 的基础 | 在浏览器开发者工具中能看到 h3 协议 |

## 第 10 章 应用层：域名、网页与常用服务

| 术语 | 英文 | 定义 | 例子 |
|---|---|---|---|

## 第 11 章 网络安全

| 术语 | 英文 | 定义 | 例子 |
|---|---|---|---|

## 第 12 章 网络管理、新技术与综合项目

| 术语 | 英文 | 定义 | 例子 |
|---|---|---|---|
