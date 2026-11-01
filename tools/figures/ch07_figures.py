"""生成第 7 章配图（编者用）。先在 labs/ch07 中运行实验 7-1～7-3，再在仓库根目录运行本脚本。"""
import json
from pathlib import Path

import cv2
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from ultralytics import YOLO
from ultralytics.utils import ASSETS

ROOT = Path(__file__).resolve().parents[2]
L = ROOT / "labs/ch07"
OUT = ROOT / "docs/chapters/07-video/images"
plt.rcParams["font.sans-serif"] = ["SimHei", "Microsoft YaHei", "PingFang SC", "WenQuanYi Zen Hei"]
plt.rcParams["axes.unicode_minus"] = False


def frame(video, i):
    cap = cv2.VideoCapture(str(video))
    cap.set(cv2.CAP_PROP_POS_FRAMES, i)
    ok, f = cap.read()
    return f


def save(name, img):
    cv2.imwrite(str(OUT / name), img, [cv2.IMWRITE_JPEG_QUALITY, 88])
    print(name, img.shape)


# 图 7-1 视频就是一串图片：0、3、6、9 秒
fs = [cv2.resize(frame(L / "lab7_1_out.mp4", s * 25), (320, 180)) for s in (0, 3, 6, 9)]
save("frames.jpg", np.hstack(fs))

# 图 7-2 跟踪：第 150、200、230 帧
fs = [cv2.resize(frame(L / "lab7_2_highway.mp4", i), (427, 240)) for i in (150, 200, 230)]
save("track.jpg", np.hstack(fs))

# 图 7-3 区域闯入
save("zone.jpg", frame(L / "lab7_2_zone.mp4", 45))

# 图 7-4 关键点 + 角度曲线
save("pose.jpg", cv2.imread(str(L / "lab7_3_pose.jpg")))
d = json.loads((ROOT / "docs/sims/action-timeline/data.json").read_text())


def ang(a, b, c):
    ba, bc = np.array(a) - np.array(b), np.array(c) - np.array(b)
    return np.degrees(np.arccos(np.clip(ba @ bc / np.linalg.norm(ba) / np.linalg.norm(bc), -1, 1)))


a = [ang(*d["kp"][i % 60][:3]) for i in range(300)]
t = np.arange(300) / 30
fig, ax = plt.subplots(figsize=(8, 2.6), dpi=130)
ax.plot(t, a, color="#1565c0", lw=1.6, label="右肘角度")
ax.axhline(140, color="#2e7d32", ls="--", lw=1, label="撑起门槛 140°")
ax.axhline(100, color="#c62828", ls="--", lw=1, label="压下门槛 100°")
for k, x in enumerate([2, 4, 6, 8, 10]):
    ax.annotate(f"第 {k + 1} 个", (x - 0.03, 150), fontsize=9, ha="right", color="#2e7d32")
ax.set_xlabel("时间（秒）")
ax.set_ylabel("角度（度）")
ax.set_ylim(50, 185)
ax.legend(loc="upper center", bbox_to_anchor=(0.5, 1.22), fontsize=8, ncol=3, frameon=False)
fig.tight_layout()
fig.savefig(OUT / "angles.png")

# 图 7-5 头部状态：bus.jpg 中两个人
m = YOLO(L / "yolo26n-pose.pt")
r = m(ASSETS / "bus.jpg", verbose=False)[0]
img = r.plot()
save("head.jpg", cv2.resize(img[300:950, :], None, fx=0.6, fy=0.6))
