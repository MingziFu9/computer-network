"""生成第 8 章配图（编者用）。先在 labs/ch08 中运行实验 8-1、8-2，再在仓库根目录运行本脚本。"""
from pathlib import Path

import cv2
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
L = ROOT / "labs/ch08"
OUT = ROOT / "docs/chapters/08-generative/images"


def save(name, img):
    cv2.imwrite(str(OUT / name), img, [cv2.IMWRITE_JPEG_QUALITY, 88])
    print(name, img.shape)


# 图 8-1 加噪过程：第 0、100、300、500、1000 步
x0 = cv2.resize(cv2.imread(str(ROOT / "labs/data/images/drive_highway.jpg")), (320, 180)).astype(np.float32) / 127.5 - 1
eps = np.random.default_rng(1).standard_normal(x0.shape).astype(np.float32)
betas = np.linspace(1e-4, 0.02, 1000)
ab = np.concatenate([[1.0], np.cumprod(1 - betas)])
tiles = []
for t in (0, 100, 300, 500, 1000):
    xt = np.sqrt(ab[t]) * x0 + np.sqrt(1 - ab[t]) * eps
    tile = np.clip((xt + 1) * 127.5, 0, 255).astype(np.uint8)
    cv2.putText(tile, f"t={t}", (6, 22), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
    tiles.append(tile)
save("noise_steps.jpg", np.hstack(tiles))

# 图 8-2 放大对比（实验 8-1）
save("sr_compare.jpg", cv2.imread(str(L / "lab8_1_compare.jpg")))

# 图 8-3 老照片修补：原图、自动找到的划痕、修补后
old = cv2.imread(str(ROOT / "labs/data/images/old_photo.jpg"))
auto = cv2.imread(str(L / "lab8_2_auto_mask.png"))
telea = cv2.imread(str(L / "lab8_2_telea.jpg"))
save("restore.jpg", np.vstack([np.hstack([old, telea]), np.hstack([auto, cv2.imread(str(L / "lab8_2_ns.jpg"))])]))
save("zoom.jpg", cv2.imread(str(L / "lab8_2_zoom.jpg")))
