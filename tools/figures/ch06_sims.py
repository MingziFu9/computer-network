"""生成第 6 章两个动画的数据（编者用，学生不用运行）。

seg-types：同一张行车照片的语义分割、实例分割、全景分割；
sam-click：MobileSAM “分割一切”的结果，点哪块亮哪块。
在仓库根目录运行：python tools/figures/ch06_sims.py（需要 labs/ch06 中的模型文件）
"""
import json
from pathlib import Path

import cv2
import numpy as np
from ultralytics import SAM, YOLO

ROOT = Path(__file__).resolve().parents[2]
IMG = ROOT / "labs/data/images"
W = ROOT / "labs/ch06"
SIMS = ROOT / "docs/sims"

ZH = ["路面", "人行道", "建筑", "墙", "栅栏", "杆子", "红绿灯", "交通标志", "植被", "草地", "天空",
      "行人", "骑车人", "轿车", "卡车", "公交车", "火车", "摩托车", "自行车"]
INST_ZH = {"person": "人", "bicycle": "自行车", "car": "车", "motorcycle": "摩托车", "bus": "大客车", "truck": "卡车"}


def seg_types():
    out = SIMS / "seg-types"
    sem_m, ins_m = YOLO(W / "yolo26n-sem.pt"), YOLO(W / "yolo26n-seg.pt")
    data = {"names": ZH, "things": list(range(11, 19)), "imgs": {}}
    for key, name in [("city", "drive_city"), ("crossing", "street_crossing")]:
        img = cv2.imread(str(IMG / f"{name}.jpg"))
        h, w = img.shape[:2]
        sem = sem_m(img, verbose=False)[0].semantic_mask.data.cpu().numpy().astype(np.uint8)
        r = ins_m(img, retina_masks=True, conf=0.3, verbose=False)[0]
        inst = np.zeros((h, w), np.uint8)
        items = []
        order = np.argsort(r.boxes.conf.cpu().numpy())          # 置信度低的先画，高的盖在上面
        for i in order:
            c = r.names[int(r.boxes.cls[i])]
            if c not in INST_ZH:
                continue
            items.append([INST_ZH[c], round(float(r.boxes.conf[i]), 2)])
            inst[r.masks.data[i].cpu().numpy() > 0] = len(items)
        cv2.imwrite(str(out / f"img/{key}.jpg"), img, [cv2.IMWRITE_JPEG_QUALITY, 85])
        cv2.imwrite(str(out / f"img/{key}_sem.png"), sem)
        cv2.imwrite(str(out / f"img/{key}_inst.png"), inst)
        data["imgs"][key] = {"w": w, "h": h, "inst": items}
        print(key, "实例", len(items), "语义类别", np.unique(sem).tolist())
    (out / "data.json").write_text(json.dumps(data, ensure_ascii=False))


def sam_click():
    out = SIMS / "sam-click"
    (out / "img").mkdir(parents=True, exist_ok=True)
    sam = SAM(W / "mobile_sam.pt")
    data = {}
    for key, name in [("highway", "drive_highway"), ("city", "drive_city")]:
        img = cv2.imread(str(IMG / f"{name}.jpg"))
        h, w = img.shape[:2]
        r = sam(img, verbose=False)[0]                           # 不给提示 = 分割一切
        masks = r.masks.data.cpu().numpy() > 0
        areas = masks.reshape(len(masks), -1).sum(1)
        lab = np.zeros((h, w), np.uint16)
        regs = []
        for i in np.argsort(-areas):                             # 大块先画，小块盖在上面
            if areas[i] < 150:
                continue
            regs.append(round(float(areas[i]) / (h * w) * 100, 2))
            lab[masks[i]] = len(regs)
        lab8 = np.dstack([(lab & 255).astype(np.uint8), (lab >> 8).astype(np.uint8), np.zeros_like(lab, np.uint8)])
        cv2.imwrite(str(out / f"img/{key}.jpg"), img, [cv2.IMWRITE_JPEG_QUALITY, 85])
        cv2.imwrite(str(out / f"img/{key}_lab.png"), lab8[:, :, ::-1])   # R=低 8 位，G=高 8 位
        data[key] = {"w": w, "h": h, "n": len(regs), "area": regs}
        print(key, "区域数", len(regs))
    (out / "data.json").write_text(json.dumps(data, ensure_ascii=False))


if __name__ == "__main__":
    import sys
    if "sam" in sys.argv:
        sam_click()
    else:
        seg_types()
