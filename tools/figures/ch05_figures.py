# 第 5 章配图（编者用）：先运行 labs/ch05 的实验 5-1、5-3
import json, cv2, numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path
plt.rcParams["font.sans-serif"] = ["WenQuanYi Zen Hei"]; plt.rcParams["axes.unicode_minus"] = False
R = Path(__file__).resolve().parents[2]; O = R / "docs/chapters/05-detection/images"
D = json.loads((R / "docs/sims/confidence-threshold/data.json").read_text())["junction"]
img = cv2.cvtColor(cv2.imread(str(R / "labs/data/kitti_sample/000380.jpg")), cv2.COLOR_BGR2RGB)
fig, ax = plt.subplots(3, 1, figsize=(11, 10.5))
for a, th in zip(ax, [0.1, 0.25, 0.5]):
    a.imshow(img); a.axis("off")
    for t in D["truth"]:
        a.add_patch(plt.Rectangle((t[1], t[2]), t[3] - t[1], t[4] - t[2], fill=False, ec="white", ls="--", lw=1.5))
    kept = [p for p in D["preds"] if p[1] >= th]
    for p in kept:
        c = "#e53935" if p[0] == "person" else "#1e88e5"
        a.add_patch(plt.Rectangle((p[2], p[3]), p[4] - p[2], p[5] - p[3], fill=False, ec=c, lw=2))
        a.text(p[2], p[3] - 3, f"{p[1]:.2f}", color="white", fontsize=8, bbox=dict(fc=c, ec="none", pad=1))
    a.set_title(f"门槛 {th}：显示 {len(kept)} 个框（白色虚线是人工标注的 9 个物体）", fontsize=12)
plt.tight_layout(); plt.savefig(O / "thresholds.jpg", dpi=90); plt.close()
for src, dst in [("labs/ch05/lab5_1_city.jpg", "detect_city.jpg"), ("labs/ch05/lab5_3_city.jpg", "kitti_city.jpg")]:
    if (R / src).exists():
        cv2.imwrite(str(O / dst), cv2.imread(str(R / src)), [cv2.IMWRITE_JPEG_QUALITY, 88])
run = R / "labs/ch05/runs/kitti20"
if (run / "results.csv").exists():
    import csv
    rows = list(csv.DictReader(open(run / "results.csv")))
    rows = [{k.strip(): v for k, v in r.items()} for r in rows]
    ep = [int(r["epoch"]) for r in rows]
    fig, ax = plt.subplots(1, 2, figsize=(11, 3.6))
    ax[0].plot(ep, [float(r["train/box_loss"]) for r in rows], "o-", label="训练：框的损失")
    ax[0].plot(ep, [float(r["val/box_loss"]) for r in rows], "s-", label="验证：框的损失")
    ax[0].set_xlabel("轮次"); ax[0].legend(); ax[0].grid(alpha=.3)
    ax[1].plot(ep, [float(r["metrics/mAP50(B)"]) for r in rows], "o-", label="mAP50")
    ax[1].plot(ep, [float(r["metrics/mAP50-95(B)"]) for r in rows], "s-", label="mAP50-95")
    ax[1].set_xlabel("轮次"); ax[1].legend(); ax[1].grid(alpha=.3)
    plt.tight_layout(); plt.savefig(O / "train_curve.png", dpi=100); plt.close()
