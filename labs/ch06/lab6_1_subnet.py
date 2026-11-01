# 实验 6-1：用 Python 自带的 ipaddress 模块核对子网划分（《计算机网络》第 6 章）
import ipaddress

net = ipaddress.ip_network("192.168.8.0/24")       # ← 改这里：要划分的网段
for sub in net.subnets(new_prefix=26):              # ← 改这里：划分后的前缀长度
    hosts = list(sub.hosts())                       # 所有可用的主机地址
    print(sub, "掩码", sub.netmask,
          "可用", hosts[0], "～", hosts[-1],
          "广播", sub.broadcast_address, "共", len(hosts), "台")
