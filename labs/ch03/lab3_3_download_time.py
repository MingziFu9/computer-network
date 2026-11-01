# 实验 3-3：算一算下载要多久（《计算机网络》第 3 章）
# 只用 Python 自带功能，直接运行：python lab3_3_download_time.py

sizes = {"一首歌": 10e6, "一集电视剧": 1.5e9, "一部 4K 电影": 40e9}   # 单位：字节
rates = [100e6, 300e6, 1000e6]                                      # 单位：bit/s ← 改这里

def fmt(sec):                                  # 把秒数变成“几分几秒”
    m, s = divmod(round(sec), 60)
    return f"{m} 分 {s:02d} 秒" if m else f"{sec:.1f} 秒"

print("文件".ljust(10), *[f"{r / 1e6:.0f} Mbps".rjust(12) for r in rates])
for name, size in sizes.items():
    times = [fmt(size * 8 / r) for r in rates]  # 时间 = 字节 × 8 ÷ 速率
    print(name.ljust(10), *[t.rjust(12) for t in times])
