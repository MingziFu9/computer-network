# 第 5 章两个动画的数据（编者用）：KITTI 三张照片的人工标注 + yolo26n 的全部候选框
import json, shutil
from pathlib import Path
from ultralytics import YOLO
R = Path(__file__).resolve().parents[2]
RAW = R / "labs/data/kitti_raw"           # 由 get_kitti_small.py 下载解压
OUT = R / "docs/sims/confidence-threshold"
KITTI = {0: "car", 1: "car", 2: "car", 3: "person", 5: "person"}
COCO = {"car": "car", "bus": "car", "truck": "car", "person": "person"}
model = YOLO(str(R / "labs/ch05/yolo26n.pt"))
data = {}
for key, stem, src in [("crossing", "004747", "street_crossing.jpg"), ("city", "005356", "drive_city.jpg"), ("junction", "000380", None)]:
    img = R / "labs/data/images" / src if src else R / "labs/data/kitti_sample/000380.jpg"
    shutil.copy(img, OUT / "img" / f"{key}.jpg")
    import cv2
    H, W = cv2.imread(str(img)).shape[:2]
    truth = []
    for line in (RAW / "labels/train" / f"{stem}.txt").read_text().splitlines():
        c, x, y, w, h = map(float, line.split())
        if int(c) in KITTI:
            truth.append([KITTI[int(c)], round((x - w / 2) * W), round((y - h / 2) * H), round((x + w / 2) * W), round((y + h / 2) * H)])
    r = model(str(img), conf=0.05, verbose=False)[0]
    preds = [[COCO[r.names[int(c)]], round(float(s), 3), *[round(v) for v in b]]
             for c, s, b in zip(r.boxes.cls, r.boxes.conf, r.boxes.xyxy.tolist()) if r.names[int(c)] in COCO]
    data[key] = {"w": W, "h": H, "truth": truth, "preds": preds}
    print(key, W, H, len(truth), len(preds))
(OUT / "data.json").write_text(json.dumps(data))
