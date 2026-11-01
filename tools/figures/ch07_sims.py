"""生成第 7 章“动作是一段时间”动画的数据（编者用）：俯卧撑视频每一帧的缩略图和右臂关键点。
在仓库根目录运行：python tools/figures/ch07_sims.py
"""
import json
from pathlib import Path

import cv2
from ultralytics import YOLO

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "docs/sims/action-timeline"
model = YOLO(ROOT / "labs/ch07/yolo26n-pose.pt")
frames, kps = [], []
for r in model(str(ROOT / "labs/data/videos/pushup_2s.mp4"), stream=True, verbose=False):
    img = r.orig_img[:, 170:470]                       # 只留中间有人的部分（300×360）
    img = cv2.resize(img, (240, 288))
    k = r.keypoints.xy[0].tolist()
    kps.append([[round((x - 170) * 0.8, 1), round(y * 0.8, 1)] for x, y in (k[6], k[8], k[10], k[12], k[16])])
    frames.append(img)
sheet = cv2.hconcat(frames)                             # 60 帧拼成一长条，网页里按位置截取
cv2.imwrite(str(OUT / "img/sheet.jpg"), sheet, [cv2.IMWRITE_JPEG_QUALITY, 70])
(OUT / "data.json").write_text(json.dumps({"n": len(frames), "w": 240, "h": 288, "fps": 30, "reps": 5, "kp": kps}))
print(len(frames), sheet.shape)
