"""生成第 8 章两个动画的图片（编者用）。在仓库根目录运行：python tools/figures/ch08_sims.py"""
import sys
from pathlib import Path

import cv2

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "labs/ch08"))
from sr_model import upscale  # noqa: E402

IMG = ROOT / "labs/data/images"
OUT = ROOT / "docs/sims"
scenes = {"street": cv2.imread(str(IMG / "drive_city.jpg"))[160:320, 300:700],
          "crossing": cv2.imread(str(IMG / "street_crossing.jpg"))[170:330, 400:800]}
for key, big in scenes.items():
    h, w = big.shape[:2]
    small = cv2.resize(big, (w // 4, h // 4), interpolation=cv2.INTER_AREA)
    outs = {"original": big, "small": small,
            "nearest": cv2.resize(small, (w, h), interpolation=cv2.INTER_NEAREST),
            "bicubic": cv2.resize(small, (w, h), interpolation=cv2.INTER_CUBIC),
            "sr": upscale(small)}
    for k, im in outs.items():
        cv2.imwrite(str(OUT / f"sr-compare/img/{key}_{k}.png"), im)
    print(key, big.shape, small.shape)

road = cv2.resize(cv2.imread(str(IMG / "drive_highway.jpg")), (320, 180), interpolation=cv2.INTER_AREA)
cv2.imwrite(str(OUT / "diffusion-noise/img/road.png"), road)
