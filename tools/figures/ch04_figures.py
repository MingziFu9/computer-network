# 第 4 章配图（编者用）：先运行 labs/ch04 的实验，再运行本脚本
import csv, cv2, numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path
plt.rcParams["font.sans-serif"] = ["WenQuanYi Zen Hei"]; plt.rcParams["axes.unicode_minus"] = False
R = Path(__file__).resolve().parents[2]; O = R / "docs/chapters/04-classification/images"
CN = {"car": "轿车", "van": "厢式车", "truck": "卡车", "pedestrian": "行人", "cyclist": "骑车人"}
# 1 数据集样例
fig, ax = plt.subplots(5, 6, figsize=(10, 8.5))
for r, n in enumerate(CN):
    fs = sorted((R / "labs/data/road_objects/train" / n).glob("*.jpg"))[:6]
    for c, f in enumerate(fs):
        a = ax[r, c]; a.imshow(cv2.cvtColor(cv2.imread(str(f)), cv2.COLOR_BGR2RGB)); a.set_xticks([]); a.set_yticks([])
        if c == 0: a.set_ylabel(f"{CN[n]}\n{n}", fontsize=12)
plt.tight_layout(); plt.savefig(O / "dataset.jpg", dpi=100); plt.close()
# 2 训练曲线
rows = list(csv.DictReader(open(R / "labs/ch04/runs/road5/results.csv")))
ep = [int(x["epoch"]) for x in rows]
fig, ax = plt.subplots(1, 2, figsize=(11, 3.6))
ax[0].plot(ep, [float(x["train/loss"]) for x in rows], "o-", label="训练损失"); ax[0].plot(ep, [float(x["val/loss"]) for x in rows], "s-", label="验证损失")
ax[0].set_xlabel("轮次"); ax[0].set_ylabel("损失（越小越好）"); ax[0].legend(); ax[0].grid(alpha=.3)
ax[1].plot(ep, [float(x["metrics/accuracy_top1"]) * 100 for x in rows], "o-", color="#43a047")
ax[1].set_xlabel("轮次"); ax[1].set_ylabel("验证集 Top-1 准确率（%）"); ax[1].grid(alpha=.3)
plt.tight_layout(); plt.savefig(O / "train_curve.png", dpi=100); plt.close()
# 3 迁移学习对比
labels = ["从零训练\n128 像素", "预训练\n64 像素", "预训练\n128 像素", "预训练\n224 像素"]
acc = [44.2, 79.9, 81.4, 83.9]; sec = [59, 32, 66, 146]
fig, ax = plt.subplots(figsize=(8, 3.4))
b = ax.bar(labels, acc, color=["#bdbdbd", "#90caf9", "#3f51b5", "#1a237e"])
for x, a, s in zip(b, acc, sec): ax.text(x.get_x() + x.get_width() / 2, a + 1, f"{a}%\n约 {s} 秒", ha="center", fontsize=10)
ax.set_ylim(0, 100); ax.set_ylabel("验证集准确率（%）"); ax.set_title("同样训练 10 轮（4 核 CPU）", fontsize=12)
plt.tight_layout(); plt.savefig(O / "transfer.png", dpi=100); plt.close()
# 4 认错的例子
wrong = [("van", "003993_182.jpg", "truck", 98), ("van", "007403_185.jpg", "car", 93), ("car", "000424_174.jpg", "van", 90),
         ("pedestrian", "001454_195.jpg", "cyclist", 94), ("truck", "006219_179.jpg", "cyclist", 96), ("car", "000424_173.jpg", "cyclist", 96)]
fig, ax = plt.subplots(1, 6, figsize=(13, 3))
for a, (t, f, p, c) in zip(ax, wrong):
    a.imshow(cv2.cvtColor(cv2.imread(str(R / "labs/data/road_objects/val" / t / f)), cv2.COLOR_BGR2RGB)); a.axis("off")
    a.set_title(f"真实 {CN[t]}\n认成 {CN[p]} {c}%", fontsize=11)
plt.tight_layout(); plt.savefig(O / "wrong.jpg", dpi=100); plt.close()
