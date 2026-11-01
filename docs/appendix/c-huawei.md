---
title: 附录 C Cisco 与华为命令对照
description: 本书实验中用到的 Cisco IOS 命令与华为 VRP 命令对照：基本操作、VLAN、Trunk、静态路由、OSPF、DHCP、NAT、ACL、SSH
---

# 附录 C Cisco 与华为命令对照

本书的实验以 Cisco Packet Tracer 为主线。使用华为设备或华为 eNSP 模拟器的学校，可以按下表把 Cisco 命令换成华为命令。两家的思路完全相同，只是写法不同。

!!! warning "使用说明"
    下表的华为命令按 VRP 系统常见的写法整理，不同型号（如 S 系列交换机、AR 系列路由器）和不同软件版本的命令可能略有差异，接口名称也要按实际设备填写（华为接口常写作 `GigabitEthernet0/0/1`）。编者没有在华为真机上逐条实测，使用前请以设备的官方文档为准，或在设备上输入 `?` 查看可用的命令。

## C.1 基本操作 { #c1 }

| 作用 | Cisco | 华为 |
|---|---|---|
| 进入配置模式 | `enable`，再 `configure terminal` | `system-view` |
| 返回上一级 / 返回用户视图 | `exit` / `end` | `quit` / `return` |
| 改设备名 | `hostname R1` | `sysname R1` |
| 进入接口 | `interface gig0/0` | `interface GigabitEthernet0/0/0` |
| 配置接口地址 | `ip address 192.168.8.1 255.255.255.192` | `ip address 192.168.8.1 255.255.255.192`（或 `ip address 192.168.8.1 26`） |
| 开启接口 | `no shutdown` | `undo shutdown`（华为接口一般默认开启） |
| 取消某条命令 | 在命令前加 `no` | 在命令前加 `undo` |
| 查看当前配置 | `show running-config` | `display current-configuration` |
| 查看接口简要状态 | `show ip interface brief` | `display ip interface brief` |
| 查看路由表 | `show ip route` | `display ip routing-table` |
| 查看 MAC 地址表 | `show mac address-table` | `display mac-address` |
| 保存配置 | `copy running-config startup-config` | `save` |
| 查看帮助 | `?` | `?` |

## C.2 VLAN 与 Trunk（第 5 章） { #c2 }

| 作用 | Cisco | 华为 |
|---|---|---|
| 创建 VLAN | `vlan 10` | `vlan 10`；批量创建 `vlan batch 10 20 30` |
| 接口设为 Access 并划入 VLAN | `switchport mode access`<br>`switchport access vlan 10` | `port link-type access`<br>`port default vlan 10` |
| 接口设为 Trunk | `switchport mode trunk` | `port link-type trunk` |
| Trunk 允许通过的 VLAN | `switchport trunk allowed vlan 10,20` | `port trunk allow-pass vlan 10 20` |
| 查看 VLAN | `show vlan brief` | `display vlan` |
| 查看 Trunk | `show interfaces trunk` | `display port vlan` |

## C.3 VLAN 间路由（第 7 章） { #c3 }

| 作用 | Cisco（3560 三层交换机） | 华为（S 系列三层交换机） |
|---|---|---|
| 开启路由功能 | `ip routing` | 默认开启，不需要 |
| 进入 VLAN 接口 | `interface vlan 10` | `interface Vlanif 10` |
| 配置网关地址 | `ip address 192.168.8.1 255.255.255.192` | `ip address 192.168.8.1 26` |

## C.4 静态路由与 OSPF（第 7 章） { #c4 }

| 作用 | Cisco | 华为 |
|---|---|---|
| 静态路由 | `ip route 192.168.9.0 255.255.255.0 10.0.12.2` | `ip route-static 192.168.9.0 24 10.0.12.2` |
| 默认路由 | `ip route 0.0.0.0 0.0.0.0 198.51.100.1` | `ip route-static 0.0.0.0 0 198.51.100.1` |
| 启动 OSPF | `router ospf 1` | `ospf 1` |
| 宣告网段 | `network 192.168.8.0 0.0.0.255 area 0` | `area 0`<br>`network 192.168.8.0 0.0.0.255` |
| 查看邻居 | `show ip ospf neighbor` | `display ospf peer brief` |

## C.5 DHCP（第 8 章） { #c5 }

| 作用 | Cisco | 华为 |
|---|---|---|
| 开启 DHCP 功能 | 默认开启 | `dhcp enable` |
| 排除地址 | `ip dhcp excluded-address 192.168.8.1 192.168.8.10` | 在地址池中：`excluded-ip-address 192.168.8.2 192.168.8.10` |
| 创建地址池 | `ip dhcp pool DESIGN` | `ip pool DESIGN` |
| 分配的网段 | `network 192.168.8.0 255.255.255.192` | `network 192.168.8.0 mask 255.255.255.192` |
| 网关 | `default-router 192.168.8.1` | `gateway-list 192.168.8.1` |
| DNS 服务器 | `dns-server 192.168.8.130` | `dns-list 192.168.8.130` |
| 让接口使用全局地址池 | 不需要 | 在接口下：`dhcp select global` |
| 查看分配情况 | `show ip dhcp binding` | `display ip pool name DESIGN used` |
| DHCP 中继 | 在接口下：`ip helper-address 服务器地址` | 在接口下：`dhcp select relay`<br>`dhcp relay server-ip 服务器地址` |

## C.6 NAT（第 8 章） { #c6 }

| 作用 | Cisco | 华为 |
|---|---|---|
| 定义要转换的内部地址 | `access-list 1 permit 192.168.8.0 0.0.0.63` | `acl number 2000`<br>`rule 5 permit source 192.168.8.0 0.0.0.63` |
| 配置 PAT（共用外部接口地址） | `ip nat inside source list 1 interface gig0/1 overload`<br>并在内、外接口分别配置 `ip nat inside`、`ip nat outside` | 在外部接口下：`nat outbound 2000`（不需要区分 inside、outside） |
| 查看转换表 | `show ip nat translations` | `display nat session all` |

## C.7 ACL（第 11 章） { #c7 }

| 作用 | Cisco | 华为 |
|---|---|---|
| 编号范围 | 标准 1～99，扩展 100～199 | 基本 ACL 2000～2999，高级 ACL 3000～3999 |
| 扩展（高级）ACL 规则 | `access-list 110 permit ip 192.168.8.64 0.0.0.31 host 192.168.8.131` | `acl number 3000`<br>`rule 5 permit ip source 192.168.8.64 0.0.0.31 destination 192.168.8.131 0` |
| 拒绝规则 | `access-list 110 deny ip any host 192.168.8.131` | `rule 10 deny ip destination 192.168.8.131 0` |
| 规则末尾的默认动作 | 隐含拒绝 deny any | 没有匹配任何规则时，按应用 ACL 的功能决定（用于报文过滤时通常是放行），所以需要拒绝的流量要明确写出 |
| 应用到接口 | `ip access-group 110 out` | `traffic-filter outbound acl 3000` |
| 查看 | `show access-lists` | `display acl 3000` |

注意最后一行之前的“默认动作”：Cisco 的 ACL 末尾隐含拒绝，而华为的报文过滤在规则都不匹配时通常是放行。从 Cisco 移植 ACL 到华为时，需要在最后补上 `rule deny ip`（或按需求明确写出拒绝的规则）。

## C.8 SSH 远程管理（第 12 章） { #c8 }

| 作用 | Cisco | 华为 |
|---|---|---|
| 生成密钥 | `ip domain-name xiaohe.com`<br>`crypto key generate rsa` | `rsa local-key-pair create` |
| 创建管理员账号 | `username admin secret 密码` | `aaa`<br>`local-user admin password irreversible-cipher 密码`<br>`local-user admin service-type ssh` |
| 开启 SSH 服务 | 生成密钥后自动开启 | `stelnet server enable` |
| 远程登录线路只允许 SSH | `line vty 0 4`<br>`login local`<br>`transport input ssh` | `user-interface vty 0 4`<br>`authentication-mode aaa`<br>`protocol inbound ssh` |
