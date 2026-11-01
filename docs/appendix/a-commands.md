---
title: 附录 A 常用网络命令速查
description: Windows、macOS、Linux 常用网络命令对照，打开命令行的方法，常用 Wireshark 过滤器
---

# 附录 A 常用网络命令速查

本书的命令行实验以 Windows 为主。本附录给出打开命令行的方法、常用命令在三种系统中的写法和作用，以及常用的 Wireshark 显示过滤器。命令的输出因电脑和网络而异，书中给出的输出均为**输出格式示意**。

## A.1 打开命令行 { #a1 }

| 系统 | 方法 |
|---|---|
| Windows 10 / 11 | 按 <kbd>Win</kbd>+<kbd>R</kbd>，输入 `cmd` 回车，打开“命令提示符”；或在开始菜单搜索“命令提示符”“终端”“PowerShell”。本书的命令在命令提示符和 PowerShell 中都能用 |
| macOS | 打开“启动台 → 其他 → 终端”，或按 <kbd>Command</kbd>+<kbd>空格</kbd> 搜索“终端” |
| Linux（Ubuntu） | 按 <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>T</kbd> 打开终端 |

部分命令需要管理员权限：Windows 中右击“命令提示符”选“以管理员身份运行”；macOS、Linux 中在命令前加 `sudo`。

## A.2 常用命令对照 { #a2 }

| 作用 | Windows | macOS | Linux | 本书章节 |
|---|---|---|---|---|
| 查看本机 IP 地址、掩码、网关 | `ipconfig` | `ifconfig`（或在“系统设置 → 网络”中查看） | `ip addr`、`ip route` | 第 1、6 章 |
| 查看详细信息（含 MAC、DNS、DHCP） | `ipconfig /all` | `ifconfig`、`scutil --dns` | `ip addr`、`resolvectl status` | 第 4、8 章 |
| 重新获取 DHCP 地址 | `ipconfig /release` 后 `ipconfig /renew` | 系统设置中“续租 DHCP” | `sudo dhclient -r` 后 `sudo dhclient`（或在网络设置中重连） | 第 8 章 |
| 测试连通性 | `ping 地址`（默认 4 次） | `ping 地址`（一直 ping，按 <kbd>Ctrl</kbd>+<kbd>C</kbd> 停止） | 同 macOS；`ping -c 4 地址` 指定次数 | 第 1、8 章 |
| 指定 ping 次数 / 包大小 | `ping -n 10 地址`、`ping -l 1000 地址` | `ping -c 10 地址`、`ping -s 1000 地址` | 同 macOS | 第 1、6 章 |
| 追踪路由 | `tracert 地址` | `traceroute 地址` | `traceroute 地址`（可能需安装）或 `tracepath 地址` | 第 7、8 章 |
| 查询域名 | `nslookup 域名` | `nslookup 域名`、`dig 域名` | 同 macOS | 第 10 章 |
| 查看 / 清除 DNS 缓存 | `ipconfig /displaydns`、`ipconfig /flushdns` | `sudo dscacheutil -flushcache` | `resolvectl flush-caches` | 第 10 章 |
| 查看 ARP 缓存 | `arp -a` | `arp -a` | `ip neigh` | 第 8 章 |
| 清除 ARP 缓存 | `arp -d`（管理员） | `sudo arp -a -d` | `sudo ip neigh flush all` | 第 8 章 |
| 查看路由表 | `route print` | `netstat -rn` | `ip route` | 第 7 章 |
| 查看网络连接和端口 | `netstat -an`；`netstat -ano` 显示进程号 | `netstat -an` | `ss -tuna` | 第 9 章 |
| 只看某个端口 | `netstat -an \| findstr 9000` | `netstat -an \| grep 9000` | `ss -tuna \| grep 9000` | 第 9 章 |
| 查看网卡 MAC 地址 | `getmac` 或 `ipconfig /all` | `ifconfig` | `ip link` | 第 4 章 |
| 测试某个 TCP 端口是否能连通 | PowerShell：`Test-NetConnection 地址 -Port 80` | `nc -vz 地址 80` | `nc -vz 地址 80` | 第 9、12 章 |
| 用命令行访问网页 | `curl -I http://地址`（Windows 10 以后自带） | `curl -I http://地址` | 同 macOS | 第 10 章 |
| 用 Python 临时开一个网站 | `python -m http.server 8000` | `python3 -m http.server 8000` | 同 macOS | 第 10 章 |

!!! tip "命令行小技巧"
    - 按 <kbd>↑</kbd> 键可以调出上一条命令，不用重新输入；
    - 按 <kbd>Tab</kbd> 键可以自动补全文件名；
    - 命令输出太多时，Windows 中可以在命令后加 `| more` 分页显示，或加 `> 结果.txt` 保存到文件；
    - 命令提示符中显示中文乱码时，可以先执行 `chcp 65001` 切换为 UTF-8。

## A.3 Cisco 设备常用命令 { #a3 }

| 命令 | 作用 |
|---|---|
| `enable` | 进入特权模式（提示符由 `>` 变为 `#`） |
| `configure terminal`（可简写 `conf t`） | 进入全局配置模式 |
| `interface gig0/0` | 进入接口配置模式 |
| `no shutdown` | 开启接口 |
| `exit` / `end` | 返回上一级 / 直接返回特权模式 |
| `show running-config` | 查看当前配置 |
| `show ip interface brief` | 查看接口地址和状态 |
| `show vlan brief` | 查看 VLAN |
| `show ip route` | 查看路由表 |
| `copy running-config startup-config`（或 `write`） | 保存配置 |
| `?` | 在任何位置输入问号，显示可用的命令或参数 |

更多命令及华为对照见[附录 C](c-huawei.md)，故障排查时用到的命令见[第 12 章 12.2.2 节](../chapters/12-management/index.md#1222)。

## A.4 常用 Wireshark 显示过滤器 { #a4 }

| 过滤器 | 只显示 | 本书用到的地方 |
|---|---|---|
| `arp` | ARP 报文 | 实验 8-1 |
| `icmp` | ping 和 tracert 的 ICMP 报文 | 实验 8-3 |
| `dhcp` | DHCP 报文（旧版本写 `bootp`） | 实验 8-1 |
| `dns` | DNS 报文 | 实验 10-1 |
| `tcp` / `udp` | TCP / UDP 报文 | 实验 9-1、9-3 |
| `tcp.port == 80` | 源或目的端口为 80 的 TCP 报文 | 第 10 章 |
| `tcp.flags.syn == 1` | 带 SYN 标志的报文（三次握手） | 实验 9-1 |
| `http` | HTTP 报文 | 第 10 章 |
| `http.request.method == "POST"` | 提交数据的 HTTP 请求 | 实验 11-1 |
| `tls` | TLS 报文（HTTPS） | 实验 11-1 |
| `ip.addr == 192.168.1.10` | 源或目的地址为该地址的报文 | 第 6 章 |
| `vlan` | 带 802.1Q 标签的帧 | 实验 5-2 |
| `frame contains "Xh2026"` | 内容中包含这段文字的帧 | 实验 11-1 |

过滤器之间可以用 `and`、`or`、`not` 组合，例如 `tcp and ip.addr == 203.0.113.10`。输入过滤器后，输入框变绿表示语法正确，变红表示有错误。

!!! danger "只抓自己有权限的网络"
    Wireshark 抓包只能用于自己的设备、本书的抓包文件或得到授权的网络。在公共场所或他人网络中抓取别人的通信数据是违法行为（第 11 章 11.6 节）。
