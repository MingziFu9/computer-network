# 实验 6-2：检查一份地址规划表有没有错（《计算机网络》第 6 章）
import ipaddress, itertools

total = ipaddress.ip_network("192.168.8.0/24")
plan = {"设计部": ("192.168.8.0/26", 50), "财务部": ("192.168.8.64/27", 20),     # ← 改这里
        "访客区": ("192.168.8.96/27", 20), "服务器": ("192.168.8.128/29", 5)}   # 部门: (网段, 需要的地址数)
nets = {k: ipaddress.ip_network(v[0]) for k, v in plan.items()}   # 网络地址写错会在这里报错
for name, n in nets.items():
    need = plan[name][1]
    ok = n.subnet_of(total) and n.num_addresses - 2 >= need       # 在总网段内，且够用
    print(f"{name}: {n}  可用 {n.num_addresses - 2}，需要 {need}", "✓" if ok else "✗ 不够或越界")
for a, b in itertools.combinations(nets, 2):                      # 两两比较
    if nets[a].overlaps(nets[b]):
        print("✗ 重叠：", a, b)
