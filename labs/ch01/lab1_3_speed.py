"""实验 1-3 ☆ 测网速：把 Mbps 换算成 MB/s，估算下载时间"""
rate_mbps = 300                    # ← 改这里：你测到的下载速率，单位 Mbps
file_gb = 4                        # 电影大小，单位 GB（按 1 GB = 10^9 字节）

rate_mb_s = rate_mbps / 8          # 1 字节 = 8 比特，换算成 MB/s
seconds = file_gb * 1000 / rate_mb_s
print(f"{rate_mbps} Mbps ≈ {rate_mb_s:.1f} MB/s")
print(f"下载 {file_gb} GB 理想情况下需要 {seconds:.0f} 秒，约 {seconds / 60:.1f} 分钟")
for eff in (0.9, 0.7):             # 实际效率按 90% 和 70% 估计
    print(f"  按实际效率 {eff:.0%} 计算：约 {seconds / eff / 60:.1f} 分钟")
