---
title: 学习图谱
description: 全书核心概念及其先修关系，点一个概念就能看到学习路径
---

# 学习图谱

学习图谱把全书的核心概念和它们之间的“先修关系”画在一张图上：要理解一个概念，得先懂哪些更基础的概念；顺着箭头往回找，就是一条学习路径。

<iframe class="sim-frame" src="main.html" height="900" loading="lazy" title="学习图谱"></iframe>

[全屏打开](main.html){ target=_blank }

## 怎样使用

- **预习**：学新的一章前，点开本章的概念，看看橙色的先修概念自己是否都掌握了，没掌握的先回去复习；
- **复习**：期末复习时，从最后几章的概念出发，顺着学习路径往回梳理，就能把全书串起来；
- **查漏补缺**：做练习时遇到不懂的概念，在搜索框里输入它，看它依赖哪些更基础的概念。

<!-- graph:start -->

图谱共有 **292 个概念、361 条先修关系**，概念按章排列，颜色表示 8 个类别（网络基础、体系结构、物理层、链路层与局域网、网络层、运输层、应用层、安全与管理）。概念的定义都来自[附录 D 术语表](../appendix/glossary.md)，先修关系由编者根据各章内容整理。

## 文字版

下面按章列出每个概念的直接先修概念，便于打印或用读屏软件阅读。

??? note "第 1 章 认识网络（30 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [计算机网络](../appendix/glossary.md#g-计算机网络) | 网络基础 | — |
    | [互连网](../appendix/glossary.md#g-互连网) | 网络基础 | [计算机网络](../appendix/glossary.md#g-计算机网络) |
    | [互联网](../appendix/glossary.md#g-互联网) | 网络基础 | [互连网](../appendix/glossary.md#g-互连网) |
    | [端系统](../appendix/glossary.md#g-端系统) | 网络基础 | [计算机网络](../appendix/glossary.md#g-计算机网络) |
    | [通信链路](../appendix/glossary.md#g-通信链路) | 网络基础 | [计算机网络](../appendix/glossary.md#g-计算机网络) |
    | [网络设备](../appendix/glossary.md#g-网络设备) | 网络基础 | [计算机网络](../appendix/glossary.md#g-计算机网络) |
    | [边缘部分](../appendix/glossary.md#g-边缘部分) | 网络基础 | [互联网](../appendix/glossary.md#g-互联网)、[端系统](../appendix/glossary.md#g-端系统) |
    | [核心部分](../appendix/glossary.md#g-核心部分) | 网络基础 | [互联网](../appendix/glossary.md#g-互联网)、[网络设备](../appendix/glossary.md#g-网络设备) |
    | [客户—服务器方式](../appendix/glossary.md#g-客户—服务器方式) | 网络基础 | [边缘部分](../appendix/glossary.md#g-边缘部分) |
    | [光猫](../appendix/glossary.md#g-光猫) | 网络基础 | [网络设备](../appendix/glossary.md#g-网络设备) |
    | [局域网](../appendix/glossary.md#g-局域网) | 网络基础 | [计算机网络](../appendix/glossary.md#g-计算机网络) |
    | [广域网](../appendix/glossary.md#g-广域网) | 网络基础 | [计算机网络](../appendix/glossary.md#g-计算机网络) |
    | [拓扑](../appendix/glossary.md#g-拓扑) | 网络基础 | [计算机网络](../appendix/glossary.md#g-计算机网络) |
    | [交换](../appendix/glossary.md#g-交换) | 网络基础 | [核心部分](../appendix/glossary.md#g-核心部分) |
    | [电路交换](../appendix/glossary.md#g-电路交换) | 网络基础 | [交换](../appendix/glossary.md#g-交换) |
    | [报文交换](../appendix/glossary.md#g-报文交换) | 网络基础 | [交换](../appendix/glossary.md#g-交换) |
    | [分组交换](../appendix/glossary.md#g-分组交换) | 网络基础 | [报文交换](../appendix/glossary.md#g-报文交换) |
    | [分组](../appendix/glossary.md#g-分组) | 网络基础 | [分组交换](../appendix/glossary.md#g-分组交换) |
    | [存储转发](../appendix/glossary.md#g-存储转发) | 网络基础 | [分组交换](../appendix/glossary.md#g-分组交换) |
    | [速率](../appendix/glossary.md#g-速率) | 网络基础 | [计算机网络](../appendix/glossary.md#g-计算机网络) |
    | [带宽](../appendix/glossary.md#g-带宽) | 网络基础 | [速率](../appendix/glossary.md#g-速率) |
    | [吞吐量](../appendix/glossary.md#g-吞吐量) | 网络基础 | [带宽](../appendix/glossary.md#g-带宽) |
    | [瓶颈链路](../appendix/glossary.md#g-瓶颈链路) | 网络基础 | [吞吐量](../appendix/glossary.md#g-吞吐量) |
    | [时延](../appendix/glossary.md#g-时延) | 网络基础 | [速率](../appendix/glossary.md#g-速率) |
    | [发送时延](../appendix/glossary.md#g-发送时延) | 网络基础 | [时延](../appendix/glossary.md#g-时延)、[带宽](../appendix/glossary.md#g-带宽) |
    | [传播时延](../appendix/glossary.md#g-传播时延) | 网络基础 | [时延](../appendix/glossary.md#g-时延) |
    | [排队时延](../appendix/glossary.md#g-排队时延) | 网络基础 | [时延](../appendix/glossary.md#g-时延)、[存储转发](../appendix/glossary.md#g-存储转发) |
    | [往返时间](../appendix/glossary.md#g-往返时间) | 网络基础 | [时延](../appendix/glossary.md#g-时延) |
    | [丢包率](../appendix/glossary.md#g-丢包率) | 网络基础 | [分组](../appendix/glossary.md#g-分组) |
    | [RFC](../appendix/glossary.md#g-RFC) | 网络基础 | [互联网](../appendix/glossary.md#g-互联网) |

??? note "第 2 章 分层与协议（24 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [网络协议](../appendix/glossary.md#g-网络协议) | 体系结构 | [计算机网络](../appendix/glossary.md#g-计算机网络) |
    | [语法](../appendix/glossary.md#g-语法) | 体系结构 | [网络协议](../appendix/glossary.md#g-网络协议) |
    | [语义](../appendix/glossary.md#g-语义) | 体系结构 | [网络协议](../appendix/glossary.md#g-网络协议) |
    | [同步](../appendix/glossary.md#g-同步) | 体系结构 | [网络协议](../appendix/glossary.md#g-网络协议) |
    | [体系结构](../appendix/glossary.md#g-体系结构) | 体系结构 | [网络协议](../appendix/glossary.md#g-网络协议) |
    | [OSI 参考模型](../appendix/glossary.md#g-OSI-参考模型) | 体系结构 | [体系结构](../appendix/glossary.md#g-体系结构) |
    | [TCP/IP 体系结构](../appendix/glossary.md#g-TCP-IP-体系结构) | 体系结构 | [体系结构](../appendix/glossary.md#g-体系结构) |
    | [五层模型](../appendix/glossary.md#g-五层模型) | 体系结构 | [OSI 参考模型](../appendix/glossary.md#g-OSI-参考模型)、[TCP/IP 体系结构](../appendix/glossary.md#g-TCP-IP-体系结构) |
    | [应用层](../appendix/glossary.md#g-应用层) | 体系结构 | [五层模型](../appendix/glossary.md#g-五层模型) |
    | [运输层](../appendix/glossary.md#g-运输层) | 体系结构 | [五层模型](../appendix/glossary.md#g-五层模型) |
    | [网络层](../appendix/glossary.md#g-网络层) | 体系结构 | [五层模型](../appendix/glossary.md#g-五层模型) |
    | [数据链路层](../appendix/glossary.md#g-数据链路层) | 体系结构 | [五层模型](../appendix/glossary.md#g-五层模型) |
    | [物理层](../appendix/glossary.md#g-物理层) | 体系结构 | [五层模型](../appendix/glossary.md#g-五层模型) |
    | [封装](../appendix/glossary.md#g-封装) | 体系结构 | [五层模型](../appendix/glossary.md#g-五层模型) |
    | [解封装](../appendix/glossary.md#g-解封装) | 体系结构 | [封装](../appendix/glossary.md#g-封装) |
    | [首部](../appendix/glossary.md#g-首部) | 体系结构 | [封装](../appendix/glossary.md#g-封装) |
    | [协议数据单元](../appendix/glossary.md#g-协议数据单元) | 体系结构 | [首部](../appendix/glossary.md#g-首部) |
    | [帧](../appendix/glossary.md#g-帧) | 体系结构 | [协议数据单元](../appendix/glossary.md#g-协议数据单元)、[数据链路层](../appendix/glossary.md#g-数据链路层) |
    | [对等层通信](../appendix/glossary.md#g-对等层通信) | 体系结构 | [五层模型](../appendix/glossary.md#g-五层模型) |
    | [服务](../appendix/glossary.md#g-服务) | 体系结构 | [五层模型](../appendix/glossary.md#g-五层模型) |
    | [服务访问点](../appendix/glossary.md#g-服务访问点) | 体系结构 | [服务](../appendix/glossary.md#g-服务) |
    | [Wireshark](../appendix/glossary.md#g-Wireshark) | 体系结构 | [协议数据单元](../appendix/glossary.md#g-协议数据单元) |
    | [抓包](../appendix/glossary.md#g-抓包) | 体系结构 | [Wireshark](../appendix/glossary.md#g-Wireshark) |
    | [显示过滤器](../appendix/glossary.md#g-显示过滤器) | 体系结构 | [抓包](../appendix/glossary.md#g-抓包) |

??? note "第 3 章 物理层（30 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [数据](../appendix/glossary.md#g-数据) | 物理层 | [物理层](../appendix/glossary.md#g-物理层) |
    | [信号](../appendix/glossary.md#g-信号) | 物理层 | [数据](../appendix/glossary.md#g-数据) |
    | [模拟信号](../appendix/glossary.md#g-模拟信号) | 物理层 | [信号](../appendix/glossary.md#g-信号) |
    | [数字信号](../appendix/glossary.md#g-数字信号) | 物理层 | [信号](../appendix/glossary.md#g-信号) |
    | [码元](../appendix/glossary.md#g-码元) | 物理层 | [数字信号](../appendix/glossary.md#g-数字信号) |
    | [信道](../appendix/glossary.md#g-信道) | 物理层 | [信号](../appendix/glossary.md#g-信号) |
    | [单工](../appendix/glossary.md#g-单工) | 物理层 | [信道](../appendix/glossary.md#g-信道) |
    | [半双工](../appendix/glossary.md#g-半双工) | 物理层 | [单工](../appendix/glossary.md#g-单工) |
    | [全双工](../appendix/glossary.md#g-全双工) | 物理层 | [半双工](../appendix/glossary.md#g-半双工) |
    | [基带信号](../appendix/glossary.md#g-基带信号) | 物理层 | [数字信号](../appendix/glossary.md#g-数字信号) |
    | [编码](../appendix/glossary.md#g-编码) | 物理层 | [基带信号](../appendix/glossary.md#g-基带信号) |
    | [调制](../appendix/glossary.md#g-调制) | 物理层 | [模拟信号](../appendix/glossary.md#g-模拟信号) |
    | [曼彻斯特编码](../appendix/glossary.md#g-曼彻斯特编码) | 物理层 | [编码](../appendix/glossary.md#g-编码) |
    | [码间串扰](../appendix/glossary.md#g-码间串扰) | 物理层 | [码元](../appendix/glossary.md#g-码元) |
    | [频带宽度](../appendix/glossary.md#g-频带宽度) | 物理层 | [信道](../appendix/glossary.md#g-信道) |
    | [波特](../appendix/glossary.md#g-波特) | 物理层 | [码元](../appendix/glossary.md#g-码元) |
    | [信噪比](../appendix/glossary.md#g-信噪比) | 物理层 | [信号](../appendix/glossary.md#g-信号) |
    | [信道容量](../appendix/glossary.md#g-信道容量) | 物理层 | [频带宽度](../appendix/glossary.md#g-频带宽度)、[信噪比](../appendix/glossary.md#g-信噪比) |
    | [香农公式](../appendix/glossary.md#g-香农公式) | 物理层 | [信道容量](../appendix/glossary.md#g-信道容量) |
    | [双绞线](../appendix/glossary.md#g-双绞线) | 物理层 | [物理层](../appendix/glossary.md#g-物理层) |
    | [直通线](../appendix/glossary.md#g-直通线) | 物理层 | [双绞线](../appendix/glossary.md#g-双绞线) |
    | [光纤](../appendix/glossary.md#g-光纤) | 物理层 | [物理层](../appendix/glossary.md#g-物理层) |
    | [单模光纤](../appendix/glossary.md#g-单模光纤) | 物理层 | [光纤](../appendix/glossary.md#g-光纤) |
    | [多模光纤](../appendix/glossary.md#g-多模光纤) | 物理层 | [光纤](../appendix/glossary.md#g-光纤) |
    | [光纤到户](../appendix/glossary.md#g-光纤到户) | 物理层 | [光纤](../appendix/glossary.md#g-光纤)、[光猫](../appendix/glossary.md#g-光猫) |
    | [无源光网络](../appendix/glossary.md#g-无源光网络) | 物理层 | [光纤到户](../appendix/glossary.md#g-光纤到户) |
    | [复用](../appendix/glossary.md#g-复用) | 物理层 | [信道](../appendix/glossary.md#g-信道) |
    | [时分复用](../appendix/glossary.md#g-时分复用) | 物理层 | [复用](../appendix/glossary.md#g-复用) |
    | [波分复用](../appendix/glossary.md#g-波分复用) | 物理层 | [复用](../appendix/glossary.md#g-复用)、[光纤](../appendix/glossary.md#g-光纤) |
    | [光模块](../appendix/glossary.md#g-光模块) | 物理层 | [光纤](../appendix/glossary.md#g-光纤) |

??? note "第 4 章 链路层（29 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [链路](../appendix/glossary.md#g-链路) | 链路层与局域网 | [数据链路层](../appendix/glossary.md#g-数据链路层)、[通信链路](../appendix/glossary.md#g-通信链路) |
    | [封装成帧](../appendix/glossary.md#g-封装成帧) | 链路层与局域网 | [帧](../appendix/glossary.md#g-帧) |
    | [透明传输](../appendix/glossary.md#g-透明传输) | 链路层与局域网 | [封装成帧](../appendix/glossary.md#g-封装成帧) |
    | [差错检测](../appendix/glossary.md#g-差错检测) | 链路层与局域网 | [帧](../appendix/glossary.md#g-帧) |
    | [零比特填充](../appendix/glossary.md#g-零比特填充) | 链路层与局域网 | [透明传输](../appendix/glossary.md#g-透明传输) |
    | [误码率](../appendix/glossary.md#g-误码率) | 链路层与局域网 | [差错检测](../appendix/glossary.md#g-差错检测) |
    | [循环冗余检验](../appendix/glossary.md#g-循环冗余检验) | 链路层与局域网 | [差错检测](../appendix/glossary.md#g-差错检测) |
    | [帧检验序列](../appendix/glossary.md#g-帧检验序列) | 链路层与局域网 | [循环冗余检验](../appendix/glossary.md#g-循环冗余检验) |
    | [PPP](../appendix/glossary.md#g-PPP) | 链路层与局域网 | [封装成帧](../appendix/glossary.md#g-封装成帧) |
    | [PPPoE](../appendix/glossary.md#g-PPPoE) | 链路层与局域网 | [PPP](../appendix/glossary.md#g-PPP) |
    | [以太网](../appendix/glossary.md#g-以太网) | 链路层与局域网 | [局域网](../appendix/glossary.md#g-局域网)、[帧](../appendix/glossary.md#g-帧) |
    | [MAC 地址](../appendix/glossary.md#g-MAC-地址) | 链路层与局域网 | [以太网](../appendix/glossary.md#g-以太网) |
    | [OUI](../appendix/glossary.md#g-OUI) | 链路层与局域网 | [MAC 地址](../appendix/glossary.md#g-MAC-地址) |
    | [广播地址](../appendix/glossary.md#g-广播地址) | 链路层与局域网 | [MAC 地址](../appendix/glossary.md#g-MAC-地址) |
    | [单播](../appendix/glossary.md#g-单播) | 链路层与局域网 | [MAC 地址](../appendix/glossary.md#g-MAC-地址) |
    | [多播](../appendix/glossary.md#g-多播) | 链路层与局域网 | [单播](../appendix/glossary.md#g-单播) |
    | [最大传送单元](../appendix/glossary.md#g-最大传送单元) | 链路层与局域网 | [以太网](../appendix/glossary.md#g-以太网) |
    | [CSMA/CD](../appendix/glossary.md#g-CSMA-CD) | 链路层与局域网 | [以太网](../appendix/glossary.md#g-以太网)、[半双工](../appendix/glossary.md#g-半双工) |
    | [争用期](../appendix/glossary.md#g-争用期) | 链路层与局域网 | [CSMA/CD](../appendix/glossary.md#g-CSMA-CD) |
    | [集线器](../appendix/glossary.md#g-集线器) | 链路层与局域网 | [CSMA/CD](../appendix/glossary.md#g-CSMA-CD) |
    | [交换机](../appendix/glossary.md#g-交换机) | 链路层与局域网 | [以太网](../appendix/glossary.md#g-以太网)、[存储转发](../appendix/glossary.md#g-存储转发) |
    | [MAC 地址表](../appendix/glossary.md#g-MAC-地址表) | 链路层与局域网 | [交换机](../appendix/glossary.md#g-交换机)、[MAC 地址](../appendix/glossary.md#g-MAC-地址) |
    | [冲突域](../appendix/glossary.md#g-冲突域) | 链路层与局域网 | [CSMA/CD](../appendix/glossary.md#g-CSMA-CD)、[集线器](../appendix/glossary.md#g-集线器) |
    | [广播域](../appendix/glossary.md#g-广播域) | 链路层与局域网 | [广播地址](../appendix/glossary.md#g-广播地址) |
    | [自学习](../appendix/glossary.md#g-自学习) | 链路层与局域网 | [MAC 地址表](../appendix/glossary.md#g-MAC-地址表) |
    | [泛洪](../appendix/glossary.md#g-泛洪) | 链路层与局域网 | [MAC 地址表](../appendix/glossary.md#g-MAC-地址表) |
    | [广播风暴](../appendix/glossary.md#g-广播风暴) | 链路层与局域网 | [泛洪](../appendix/glossary.md#g-泛洪)、[拓扑](../appendix/glossary.md#g-拓扑) |
    | [生成树协议](../appendix/glossary.md#g-生成树协议) | 链路层与局域网 | [广播风暴](../appendix/glossary.md#g-广播风暴) |
    | [RoCE](../appendix/glossary.md#g-RoCE) | 链路层与局域网 | [以太网](../appendix/glossary.md#g-以太网) |

??? note "第 5 章 VLAN 与无线（20 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [VLAN](../appendix/glossary.md#g-VLAN) | 链路层与局域网 | [广播域](../appendix/glossary.md#g-广播域)、[交换机](../appendix/glossary.md#g-交换机) |
    | [Access 口](../appendix/glossary.md#g-Access-口) | 链路层与局域网 | [VLAN](../appendix/glossary.md#g-VLAN) |
    | [Trunk 口](../appendix/glossary.md#g-Trunk-口) | 链路层与局域网 | [VLAN](../appendix/glossary.md#g-VLAN) |
    | [802.1Q](../appendix/glossary.md#g-802.1Q) | 链路层与局域网 | [Trunk 口](../appendix/glossary.md#g-Trunk-口) |
    | [VLAN 标识符](../appendix/glossary.md#g-VLAN-标识符) | 链路层与局域网 | [802.1Q](../appendix/glossary.md#g-802.1Q) |
    | [单臂路由](../appendix/glossary.md#g-单臂路由) | 链路层与局域网 | [Trunk 口](../appendix/glossary.md#g-Trunk-口)、[路由器](../appendix/glossary.md#g-路由器) |
    | [三层交换机](../appendix/glossary.md#g-三层交换机) | 链路层与局域网 | [VLAN](../appendix/glossary.md#g-VLAN)、[路由器](../appendix/glossary.md#g-路由器) |
    | [链路聚合](../appendix/glossary.md#g-链路聚合) | 链路层与局域网 | [交换机](../appendix/glossary.md#g-交换机) |
    | [无线局域网](../appendix/glossary.md#g-无线局域网) | 链路层与局域网 | [局域网](../appendix/glossary.md#g-局域网) |
    | [802.11](../appendix/glossary.md#g-802.11) | 链路层与局域网 | [无线局域网](../appendix/glossary.md#g-无线局域网) |
    | [WiFi](../appendix/glossary.md#g-WiFi) | 链路层与局域网 | [802.11](../appendix/glossary.md#g-802.11) |
    | [CSMA/CA](../appendix/glossary.md#g-CSMA-CA) | 链路层与局域网 | [CSMA/CD](../appendix/glossary.md#g-CSMA-CD)、[无线局域网](../appendix/glossary.md#g-无线局域网) |
    | [确认](../appendix/glossary.md#g-确认) | 链路层与局域网 | [CSMA/CA](../appendix/glossary.md#g-CSMA-CA) |
    | [无线路由器](../appendix/glossary.md#g-无线路由器) | 链路层与局域网 | [WiFi](../appendix/glossary.md#g-WiFi) |
    | [AP](../appendix/glossary.md#g-AP) | 链路层与局域网 | [WiFi](../appendix/glossary.md#g-WiFi) |
    | [Mesh 组网](../appendix/glossary.md#g-Mesh-组网) | 链路层与局域网 | [AP](../appendix/glossary.md#g-AP) |
    | [SSID](../appendix/glossary.md#g-SSID) | 链路层与局域网 | [WiFi](../appendix/glossary.md#g-WiFi) |
    | [WPA2](../appendix/glossary.md#g-WPA2) | 链路层与局域网 | [SSID](../appendix/glossary.md#g-SSID) |
    | [WPA3](../appendix/glossary.md#g-WPA3) | 链路层与局域网 | [WPA2](../appendix/glossary.md#g-WPA2) |
    | [访客网络](../appendix/glossary.md#g-访客网络) | 链路层与局域网 | [SSID](../appendix/glossary.md#g-SSID)、[VLAN](../appendix/glossary.md#g-VLAN) |

??? note "第 6 章 IP 地址（23 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [IP 地址](../appendix/glossary.md#g-IP-地址) | 网络层 | [网络层](../appendix/glossary.md#g-网络层) |
    | [IP 协议](../appendix/glossary.md#g-IP-协议) | 网络层 | [网络层](../appendix/glossary.md#g-网络层) |
    | [尽力而为](../appendix/glossary.md#g-尽力而为) | 网络层 | [IP 协议](../appendix/glossary.md#g-IP-协议) |
    | [IPv4 地址](../appendix/glossary.md#g-IPv4-地址) | 网络层 | [IP 地址](../appendix/glossary.md#g-IP-地址) |
    | [点分十进制](../appendix/glossary.md#g-点分十进制) | 网络层 | [IPv4 地址](../appendix/glossary.md#g-IPv4-地址) |
    | [网络号](../appendix/glossary.md#g-网络号) | 网络层 | [IPv4 地址](../appendix/glossary.md#g-IPv4-地址) |
    | [主机号](../appendix/glossary.md#g-主机号) | 网络层 | [IPv4 地址](../appendix/glossary.md#g-IPv4-地址) |
    | [网络地址](../appendix/glossary.md#g-网络地址) | 网络层 | [网络号](../appendix/glossary.md#g-网络号)、[主机号](../appendix/glossary.md#g-主机号) |
    | [环回地址](../appendix/glossary.md#g-环回地址) | 网络层 | [IPv4 地址](../appendix/glossary.md#g-IPv4-地址) |
    | [链路本地地址](../appendix/glossary.md#g-链路本地地址) | 网络层 | [IPv4 地址](../appendix/glossary.md#g-IPv4-地址) |
    | [私有地址](../appendix/glossary.md#g-私有地址) | 网络层 | [IPv4 地址](../appendix/glossary.md#g-IPv4-地址) |
    | [子网掩码](../appendix/glossary.md#g-子网掩码) | 网络层 | [网络号](../appendix/glossary.md#g-网络号) |
    | [CIDR](../appendix/glossary.md#g-CIDR) | 网络层 | [子网掩码](../appendix/glossary.md#g-子网掩码) |
    | [前缀长度](../appendix/glossary.md#g-前缀长度) | 网络层 | [CIDR](../appendix/glossary.md#g-CIDR) |
    | [块大小](../appendix/glossary.md#g-块大小) | 网络层 | [前缀长度](../appendix/glossary.md#g-前缀长度) |
    | [子网划分](../appendix/glossary.md#g-子网划分) | 网络层 | [子网掩码](../appendix/glossary.md#g-子网掩码)、[块大小](../appendix/glossary.md#g-块大小) |
    | [变长子网掩码](../appendix/glossary.md#g-变长子网掩码) | 网络层 | [子网划分](../appendix/glossary.md#g-子网划分) |
    | [路由聚合](../appendix/glossary.md#g-路由聚合) | 网络层 | [CIDR](../appendix/glossary.md#g-CIDR) |
    | [生存时间](../appendix/glossary.md#g-生存时间) | 网络层 | [IP 协议](../appendix/glossary.md#g-IP-协议) |
    | [协议](../appendix/glossary.md#g-协议) | 网络层 | [IP 协议](../appendix/glossary.md#g-IP-协议) |
    | [分片](../appendix/glossary.md#g-分片) | 网络层 | [最大传送单元](../appendix/glossary.md#g-最大传送单元)、[IP 协议](../appendix/glossary.md#g-IP-协议) |
    | [IPv6](../appendix/glossary.md#g-IPv6) | 网络层 | [IP 地址](../appendix/glossary.md#g-IP-地址) |
    | [冒号十六进制](../appendix/glossary.md#g-冒号十六进制) | 网络层 | [IPv6](../appendix/glossary.md#g-IPv6) |

??? note "第 7 章 路由（22 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [路由器](../appendix/glossary.md#g-路由器) | 网络层 | [网络层](../appendix/glossary.md#g-网络层)、[分组交换](../appendix/glossary.md#g-分组交换) |
    | [转发](../appendix/glossary.md#g-转发) | 网络层 | [路由器](../appendix/glossary.md#g-路由器) |
    | [路由选择](../appendix/glossary.md#g-路由选择) | 网络层 | [路由器](../appendix/glossary.md#g-路由器) |
    | [默认网关](../appendix/glossary.md#g-默认网关) | 网络层 | [路由器](../appendix/glossary.md#g-路由器)、[子网掩码](../appendix/glossary.md#g-子网掩码) |
    | [路由表](../appendix/glossary.md#g-路由表) | 网络层 | [路由选择](../appendix/glossary.md#g-路由选择) |
    | [下一跳](../appendix/glossary.md#g-下一跳) | 网络层 | [路由表](../appendix/glossary.md#g-路由表) |
    | [直接交付](../appendix/glossary.md#g-直接交付) | 网络层 | [路由表](../appendix/glossary.md#g-路由表)、[网络地址](../appendix/glossary.md#g-网络地址) |
    | [默认路由](../appendix/glossary.md#g-默认路由) | 网络层 | [路由表](../appendix/glossary.md#g-路由表) |
    | [最长前缀匹配](../appendix/glossary.md#g-最长前缀匹配) | 网络层 | [路由表](../appendix/glossary.md#g-路由表)、[前缀长度](../appendix/glossary.md#g-前缀长度) |
    | [静态路由](../appendix/glossary.md#g-静态路由) | 网络层 | [路由表](../appendix/glossary.md#g-路由表) |
    | [动态路由](../appendix/glossary.md#g-动态路由) | 网络层 | [路由表](../appendix/glossary.md#g-路由表) |
    | [距离向量](../appendix/glossary.md#g-距离向量) | 网络层 | [动态路由](../appendix/glossary.md#g-动态路由) |
    | [RIP](../appendix/glossary.md#g-RIP) | 网络层 | [距离向量](../appendix/glossary.md#g-距离向量) |
    | [跳数](../appendix/glossary.md#g-跳数) | 网络层 | [RIP](../appendix/glossary.md#g-RIP) |
    | [链路状态](../appendix/glossary.md#g-链路状态) | 网络层 | [动态路由](../appendix/glossary.md#g-动态路由) |
    | [OSPF](../appendix/glossary.md#g-OSPF) | 网络层 | [链路状态](../appendix/glossary.md#g-链路状态) |
    | [代价](../appendix/glossary.md#g-代价) | 网络层 | [OSPF](../appendix/glossary.md#g-OSPF) |
    | [最短路径算法](../appendix/glossary.md#g-最短路径算法) | 网络层 | [链路状态](../appendix/glossary.md#g-链路状态) |
    | [自治系统](../appendix/glossary.md#g-自治系统) | 网络层 | [动态路由](../appendix/glossary.md#g-动态路由) |
    | [BGP](../appendix/glossary.md#g-BGP) | 网络层 | [自治系统](../appendix/glossary.md#g-自治系统) |
    | [管理距离](../appendix/glossary.md#g-管理距离) | 网络层 | [静态路由](../appendix/glossary.md#g-静态路由)、[动态路由](../appendix/glossary.md#g-动态路由) |
    | [通配符掩码](../appendix/glossary.md#g-通配符掩码) | 网络层 | [子网掩码](../appendix/glossary.md#g-子网掩码) |

??? note "第 8 章 ARP DHCP NAT（16 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [ARP](../appendix/glossary.md#g-ARP) | 网络层 | [IP 地址](../appendix/glossary.md#g-IP-地址)、[MAC 地址](../appendix/glossary.md#g-MAC-地址) |
    | [ARP 缓存](../appendix/glossary.md#g-ARP-缓存) | 网络层 | [ARP](../appendix/glossary.md#g-ARP) |
    | [ARP 欺骗](../appendix/glossary.md#g-ARP-欺骗) | 网络层 | [ARP 缓存](../appendix/glossary.md#g-ARP-缓存) |
    | [ICMP](../appendix/glossary.md#g-ICMP) | 网络层 | [IP 协议](../appendix/glossary.md#g-IP-协议) |
    | [回送请求](../appendix/glossary.md#g-回送请求) | 网络层 | [ICMP](../appendix/glossary.md#g-ICMP) |
    | [回送回答](../appendix/glossary.md#g-回送回答) | 网络层 | [回送请求](../appendix/glossary.md#g-回送请求) |
    | [终点不可达](../appendix/glossary.md#g-终点不可达) | 网络层 | [ICMP](../appendix/glossary.md#g-ICMP) |
    | [时间超过](../appendix/glossary.md#g-时间超过) | 网络层 | [ICMP](../appendix/glossary.md#g-ICMP)、[生存时间](../appendix/glossary.md#g-生存时间) |
    | [DHCP](../appendix/glossary.md#g-DHCP) | 网络层 | [IP 地址](../appendix/glossary.md#g-IP-地址)、[默认网关](../appendix/glossary.md#g-默认网关) |
    | [地址池](../appendix/glossary.md#g-地址池) | 网络层 | [DHCP](../appendix/glossary.md#g-DHCP) |
    | [租期](../appendix/glossary.md#g-租期) | 网络层 | [DHCP](../appendix/glossary.md#g-DHCP) |
    | [DHCP 中继](../appendix/glossary.md#g-DHCP-中继) | 网络层 | [DHCP](../appendix/glossary.md#g-DHCP)、[路由器](../appendix/glossary.md#g-路由器) |
    | [NAT](../appendix/glossary.md#g-NAT) | 网络层 | [私有地址](../appendix/glossary.md#g-私有地址) |
    | [端口地址转换](../appendix/glossary.md#g-端口地址转换) | 网络层 | [NAT](../appendix/glossary.md#g-NAT)、[端口号](../appendix/glossary.md#g-端口号) |
    | [NAT 转换表](../appendix/glossary.md#g-NAT-转换表) | 网络层 | [端口地址转换](../appendix/glossary.md#g-端口地址转换) |
    | [运营商级 NAT](../appendix/glossary.md#g-运营商级-NAT) | 网络层 | [NAT](../appendix/glossary.md#g-NAT) |

??? note "第 9 章 传输层（25 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [进程](../appendix/glossary.md#g-进程) | 运输层 | [运输层](../appendix/glossary.md#g-运输层) |
    | [端口号](../appendix/glossary.md#g-端口号) | 运输层 | [进程](../appendix/glossary.md#g-进程) |
    | [熟知端口](../appendix/glossary.md#g-熟知端口) | 运输层 | [端口号](../appendix/glossary.md#g-端口号) |
    | [套接字](../appendix/glossary.md#g-套接字) | 运输层 | [端口号](../appendix/glossary.md#g-端口号)、[IP 地址](../appendix/glossary.md#g-IP-地址) |
    | [UDP](../appendix/glossary.md#g-UDP) | 运输层 | [运输层](../appendix/glossary.md#g-运输层)、[端口号](../appendix/glossary.md#g-端口号) |
    | [TCP](../appendix/glossary.md#g-TCP) | 运输层 | [运输层](../appendix/glossary.md#g-运输层)、[端口号](../appendix/glossary.md#g-端口号) |
    | [面向连接](../appendix/glossary.md#g-面向连接) | 运输层 | [TCP](../appendix/glossary.md#g-TCP) |
    | [序号](../appendix/glossary.md#g-序号) | 运输层 | [TCP](../appendix/glossary.md#g-TCP) |
    | [确认号](../appendix/glossary.md#g-确认号) | 运输层 | [序号](../appendix/glossary.md#g-序号) |
    | [SYN](../appendix/glossary.md#g-SYN) | 运输层 | [TCP](../appendix/glossary.md#g-TCP) |
    | [ACK](../appendix/glossary.md#g-ACK) | 运输层 | [确认号](../appendix/glossary.md#g-确认号) |
    | [FIN](../appendix/glossary.md#g-FIN) | 运输层 | [TCP](../appendix/glossary.md#g-TCP) |
    | [三次握手](../appendix/glossary.md#g-三次握手) | 运输层 | [SYN](../appendix/glossary.md#g-SYN)、[ACK](../appendix/glossary.md#g-ACK)、[面向连接](../appendix/glossary.md#g-面向连接) |
    | [四次挥手](../appendix/glossary.md#g-四次挥手) | 运输层 | [FIN](../appendix/glossary.md#g-FIN)、[ACK](../appendix/glossary.md#g-ACK) |
    | [捎带确认](../appendix/glossary.md#g-捎带确认) | 运输层 | [确认号](../appendix/glossary.md#g-确认号) |
    | [超时重传](../appendix/glossary.md#g-超时重传) | 运输层 | [确认号](../appendix/glossary.md#g-确认号)、[往返时间](../appendix/glossary.md#g-往返时间) |
    | [滑动窗口](../appendix/glossary.md#g-滑动窗口) | 运输层 | [超时重传](../appendix/glossary.md#g-超时重传) |
    | [流量控制](../appendix/glossary.md#g-流量控制) | 运输层 | [滑动窗口](../appendix/glossary.md#g-滑动窗口) |
    | [拥塞控制](../appendix/glossary.md#g-拥塞控制) | 运输层 | [流量控制](../appendix/glossary.md#g-流量控制)、[排队时延](../appendix/glossary.md#g-排队时延) |
    | [拥塞窗口](../appendix/glossary.md#g-拥塞窗口) | 运输层 | [拥塞控制](../appendix/glossary.md#g-拥塞控制) |
    | [慢开始](../appendix/glossary.md#g-慢开始) | 运输层 | [拥塞窗口](../appendix/glossary.md#g-拥塞窗口) |
    | [拥塞避免](../appendix/glossary.md#g-拥塞避免) | 运输层 | [慢开始](../appendix/glossary.md#g-慢开始) |
    | [快重传](../appendix/glossary.md#g-快重传) | 运输层 | [拥塞控制](../appendix/glossary.md#g-拥塞控制)、[确认号](../appendix/glossary.md#g-确认号) |
    | [快恢复](../appendix/glossary.md#g-快恢复) | 运输层 | [快重传](../appendix/glossary.md#g-快重传) |
    | [QUIC](../appendix/glossary.md#g-QUIC) | 运输层 | [UDP](../appendix/glossary.md#g-UDP)、[TCP](../appendix/glossary.md#g-TCP) |

??? note "第 10 章 应用层（28 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [客户—服务器模式](../appendix/glossary.md#g-客户—服务器模式) | 应用层 | [客户—服务器方式](../appendix/glossary.md#g-客户—服务器方式)、[应用层](../appendix/glossary.md#g-应用层) |
    | [对等网络](../appendix/glossary.md#g-对等网络) | 应用层 | [客户—服务器模式](../appendix/glossary.md#g-客户—服务器模式) |
    | [域名](../appendix/glossary.md#g-域名) | 应用层 | [应用层](../appendix/glossary.md#g-应用层)、[IP 地址](../appendix/glossary.md#g-IP-地址) |
    | [域名系统](../appendix/glossary.md#g-域名系统) | 应用层 | [域名](../appendix/glossary.md#g-域名)、[UDP](../appendix/glossary.md#g-UDP) |
    | [顶级域名](../appendix/glossary.md#g-顶级域名) | 应用层 | [域名](../appendix/glossary.md#g-域名) |
    | [根域名服务器](../appendix/glossary.md#g-根域名服务器) | 应用层 | [域名系统](../appendix/glossary.md#g-域名系统) |
    | [顶级域名服务器](../appendix/glossary.md#g-顶级域名服务器) | 应用层 | [根域名服务器](../appendix/glossary.md#g-根域名服务器)、[顶级域名](../appendix/glossary.md#g-顶级域名) |
    | [权威域名服务器](../appendix/glossary.md#g-权威域名服务器) | 应用层 | [顶级域名服务器](../appendix/glossary.md#g-顶级域名服务器) |
    | [本地域名服务器](../appendix/glossary.md#g-本地域名服务器) | 应用层 | [域名系统](../appendix/glossary.md#g-域名系统)、[DHCP](../appendix/glossary.md#g-DHCP) |
    | [递归查询](../appendix/glossary.md#g-递归查询) | 应用层 | [本地域名服务器](../appendix/glossary.md#g-本地域名服务器) |
    | [迭代查询](../appendix/glossary.md#g-迭代查询) | 应用层 | [递归查询](../appendix/glossary.md#g-递归查询)、[根域名服务器](../appendix/glossary.md#g-根域名服务器) |
    | [hosts 文件](../appendix/glossary.md#g-hosts-文件) | 应用层 | [域名系统](../appendix/glossary.md#g-域名系统) |
    | [DNS 劫持](../appendix/glossary.md#g-DNS-劫持) | 应用层 | [域名系统](../appendix/glossary.md#g-域名系统) |
    | [万维网](../appendix/glossary.md#g-万维网) | 应用层 | [应用层](../appendix/glossary.md#g-应用层) |
    | [URL](../appendix/glossary.md#g-URL) | 应用层 | [万维网](../appendix/glossary.md#g-万维网)、[域名](../appendix/glossary.md#g-域名)、[端口号](../appendix/glossary.md#g-端口号) |
    | [HTTP](../appendix/glossary.md#g-HTTP) | 应用层 | [URL](../appendix/glossary.md#g-URL)、[TCP](../appendix/glossary.md#g-TCP) |
    | [HTTPS](../appendix/glossary.md#g-HTTPS) | 应用层 | [HTTP](../appendix/glossary.md#g-HTTP)、[TLS](../appendix/glossary.md#g-TLS) |
    | [请求方法](../appendix/glossary.md#g-请求方法) | 应用层 | [HTTP](../appendix/glossary.md#g-HTTP) |
    | [状态码](../appendix/glossary.md#g-状态码) | 应用层 | [HTTP](../appendix/glossary.md#g-HTTP) |
    | [Cookie](../appendix/glossary.md#g-Cookie) | 应用层 | [HTTP](../appendix/glossary.md#g-HTTP) |
    | [Web API](../appendix/glossary.md#g-Web-API) | 应用层 | [HTTP](../appendix/glossary.md#g-HTTP) |
    | [JSON](../appendix/glossary.md#g-JSON) | 应用层 | [Web API](../appendix/glossary.md#g-Web-API) |
    | [SMTP](../appendix/glossary.md#g-SMTP) | 应用层 | [TCP](../appendix/glossary.md#g-TCP)、[应用层](../appendix/glossary.md#g-应用层) |
    | [POP3](../appendix/glossary.md#g-POP3) | 应用层 | [SMTP](../appendix/glossary.md#g-SMTP) |
    | [IMAP](../appendix/glossary.md#g-IMAP) | 应用层 | [POP3](../appendix/glossary.md#g-POP3) |
    | [FTP](../appendix/glossary.md#g-FTP) | 应用层 | [TCP](../appendix/glossary.md#g-TCP)、[应用层](../appendix/glossary.md#g-应用层) |
    | [SSH](../appendix/glossary.md#g-SSH) | 应用层 | [TCP](../appendix/glossary.md#g-TCP)、[加密](../appendix/glossary.md#g-加密) |
    | [CDN](../appendix/glossary.md#g-CDN) | 应用层 | [域名系统](../appendix/glossary.md#g-域名系统) |

??? note "第 11 章 网络安全（31 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [机密性](../appendix/glossary.md#g-机密性) | 安全与管理 | [计算机网络](../appendix/glossary.md#g-计算机网络) |
    | [完整性](../appendix/glossary.md#g-完整性) | 安全与管理 | [计算机网络](../appendix/glossary.md#g-计算机网络) |
    | [可用性](../appendix/glossary.md#g-可用性) | 安全与管理 | [计算机网络](../appendix/glossary.md#g-计算机网络) |
    | [钓鱼](../appendix/glossary.md#g-钓鱼) | 安全与管理 | [机密性](../appendix/glossary.md#g-机密性)、[URL](../appendix/glossary.md#g-URL) |
    | [勒索软件](../appendix/glossary.md#g-勒索软件) | 安全与管理 | [可用性](../appendix/glossary.md#g-可用性) |
    | [拒绝服务攻击 DDoS](../appendix/glossary.md#g-拒绝服务攻击-DDoS) | 安全与管理 | [可用性](../appendix/glossary.md#g-可用性) |
    | [中间人攻击](../appendix/glossary.md#g-中间人攻击) | 安全与管理 | [机密性](../appendix/glossary.md#g-机密性)、[完整性](../appendix/glossary.md#g-完整性) |
    | [社会工程学](../appendix/glossary.md#g-社会工程学) | 安全与管理 | [钓鱼](../appendix/glossary.md#g-钓鱼) |
    | [加密](../appendix/glossary.md#g-加密) | 安全与管理 | [机密性](../appendix/glossary.md#g-机密性) |
    | [密钥](../appendix/glossary.md#g-密钥) | 安全与管理 | [加密](../appendix/glossary.md#g-加密) |
    | [对称加密](../appendix/glossary.md#g-对称加密) | 安全与管理 | [密钥](../appendix/glossary.md#g-密钥) |
    | [非对称加密](../appendix/glossary.md#g-非对称加密) | 安全与管理 | [对称加密](../appendix/glossary.md#g-对称加密) |
    | [公钥](../appendix/glossary.md#g-公钥) | 安全与管理 | [非对称加密](../appendix/glossary.md#g-非对称加密) |
    | [私钥](../appendix/glossary.md#g-私钥) | 安全与管理 | [非对称加密](../appendix/glossary.md#g-非对称加密) |
    | [哈希](../appendix/glossary.md#g-哈希) | 安全与管理 | [完整性](../appendix/glossary.md#g-完整性) |
    | [数字签名](../appendix/glossary.md#g-数字签名) | 安全与管理 | [私钥](../appendix/glossary.md#g-私钥)、[哈希](../appendix/glossary.md#g-哈希) |
    | [数字证书](../appendix/glossary.md#g-数字证书) | 安全与管理 | [公钥](../appendix/glossary.md#g-公钥)、[数字签名](../appendix/glossary.md#g-数字签名) |
    | [证书颁发机构](../appendix/glossary.md#g-证书颁发机构) | 安全与管理 | [数字证书](../appendix/glossary.md#g-数字证书) |
    | [TLS](../appendix/glossary.md#g-TLS) | 安全与管理 | [数字证书](../appendix/glossary.md#g-数字证书)、[对称加密](../appendix/glossary.md#g-对称加密) |
    | [防火墙](../appendix/glossary.md#g-防火墙) | 安全与管理 | [端口号](../appendix/glossary.md#g-端口号)、[IP 地址](../appendix/glossary.md#g-IP-地址) |
    | [包过滤防火墙](../appendix/glossary.md#g-包过滤防火墙) | 安全与管理 | [防火墙](../appendix/glossary.md#g-防火墙) |
    | [状态检测防火墙](../appendix/glossary.md#g-状态检测防火墙) | 安全与管理 | [包过滤防火墙](../appendix/glossary.md#g-包过滤防火墙)、[TCP](../appendix/glossary.md#g-TCP) |
    | [访问控制列表](../appendix/glossary.md#g-访问控制列表) | 安全与管理 | [包过滤防火墙](../appendix/glossary.md#g-包过滤防火墙) |
    | [隐含拒绝](../appendix/glossary.md#g-隐含拒绝) | 安全与管理 | [访问控制列表](../appendix/glossary.md#g-访问控制列表) |
    | [标准 ACL](../appendix/glossary.md#g-标准-ACL) | 安全与管理 | [访问控制列表](../appendix/glossary.md#g-访问控制列表) |
    | [扩展 ACL](../appendix/glossary.md#g-扩展-ACL) | 安全与管理 | [标准 ACL](../appendix/glossary.md#g-标准-ACL)、[端口号](../appendix/glossary.md#g-端口号) |
    | [入侵检测系统](../appendix/glossary.md#g-入侵检测系统) | 安全与管理 | [防火墙](../appendix/glossary.md#g-防火墙) |
    | [入侵防御系统](../appendix/glossary.md#g-入侵防御系统) | 安全与管理 | [入侵检测系统](../appendix/glossary.md#g-入侵检测系统) |
    | [VPN](../appendix/glossary.md#g-VPN) | 安全与管理 | [加密](../appendix/glossary.md#g-加密) |
    | [双因素认证](../appendix/glossary.md#g-双因素认证) | 安全与管理 | [钓鱼](../appendix/glossary.md#g-钓鱼) |
    | [网络安全等级保护制度](../appendix/glossary.md#g-网络安全等级保护制度) | 安全与管理 | [机密性](../appendix/glossary.md#g-机密性) |

??? note "第 12 章 管理与项目（14 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [故障管理](../appendix/glossary.md#g-故障管理) | 安全与管理 | [计算机网络](../appendix/glossary.md#g-计算机网络) |
    | [配置管理](../appendix/glossary.md#g-配置管理) | 安全与管理 | [故障管理](../appendix/glossary.md#g-故障管理) |
    | [性能管理](../appendix/glossary.md#g-性能管理) | 安全与管理 | [吞吐量](../appendix/glossary.md#g-吞吐量)、[往返时间](../appendix/glossary.md#g-往返时间) |
    | [安全管理](../appendix/glossary.md#g-安全管理) | 安全与管理 | [访问控制列表](../appendix/glossary.md#g-访问控制列表) |
    | [计费管理](../appendix/glossary.md#g-计费管理) | 安全与管理 | [性能管理](../appendix/glossary.md#g-性能管理) |
    | [SNMP](../appendix/glossary.md#g-SNMP) | 安全与管理 | [UDP](../appendix/glossary.md#g-UDP)、[性能管理](../appendix/glossary.md#g-性能管理) |
    | [陷阱](../appendix/glossary.md#g-陷阱) | 安全与管理 | [SNMP](../appendix/glossary.md#g-SNMP) |
    | [由下往上](../appendix/glossary.md#g-由下往上) | 安全与管理 | [五层模型](../appendix/glossary.md#g-五层模型)、[故障管理](../appendix/glossary.md#g-故障管理) |
    | [QoS](../appendix/glossary.md#g-QoS) | 安全与管理 | [排队时延](../appendix/glossary.md#g-排队时延) |
    | [软件定义网络 SDN](../appendix/glossary.md#g-软件定义网络-SDN) | 安全与管理 | [转发](../appendix/glossary.md#g-转发)、[路由选择](../appendix/glossary.md#g-路由选择) |
    | [VPC](../appendix/glossary.md#g-VPC) | 安全与管理 | [子网划分](../appendix/glossary.md#g-子网划分)、[私有地址](../appendix/glossary.md#g-私有地址) |
    | [5G](../appendix/glossary.md#g-5G) | 安全与管理 | [无线局域网](../appendix/glossary.md#g-无线局域网) |
    | [物联网](../appendix/glossary.md#g-物联网) | 安全与管理 | [IPv6](../appendix/glossary.md#g-IPv6) |
    | [智能运维](../appendix/glossary.md#g-智能运维) | 安全与管理 | [故障管理](../appendix/glossary.md#g-故障管理) |

<!-- graph:end -->
