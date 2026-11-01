"""生成第 9 章配图（编者用）。先在 labs/ch09 中运行实验 9-2，再在仓库根目录运行本脚本。
图 9-? gradio_app.jpg 是实验 9-1 网页的截图（浏览器截屏后裁去下方示例区），不由本脚本生成。
"""
from pathlib import Path

import cv2
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
L = ROOT / "labs/ch09"
OUT = ROOT / "docs/chapters/09-applications/images"


def save(name, img):
    cv2.imwrite(str(OUT / name), img, [cv2.IMWRITE_JPEG_QUALITY, 88])
    print(name, img.shape)


# 实验 9-2 三步：找到标记码 → 透视贴图 → 不做透视的对比（都裁出路面中间一块）
tiles = []
for f, label in [("lab9_2_detected.jpg", "1 find marker"), ("lab9_2_ar.jpg", "2 homography"), ("lab9_2_flat.jpg", "3 no perspective")]:
    t = cv2.imread(str(L / f))[400:700, 420:900].copy()
    cv2.putText(t, label, (8, 28), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
    tiles.append(t)
save("ar_steps.jpg", np.hstack(tiles))
