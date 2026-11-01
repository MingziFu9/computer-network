# 第 4 章“混淆矩阵读图”动画的数据（编者用）：先运行实验 4-3，再运行本脚本
import json, shutil
from pathlib import Path
from ultralytics import YOLO
R = Path(__file__).resolve().parents[2]
OUT = R / "docs/sims/confusion-matrix"
model = YOLO(str(R / "labs/ch04/runs/road5/weights/best.pt"))
names = ["car", "cyclist", "pedestrian", "truck", "van"]
items = []
for t in names:
    for f in sorted((R / "labs/data/road_objects/val" / t).glob("*.jpg")):
        r = model(str(f), imgsz=128, verbose=False)[0]
        p = r.names[r.probs.top1]
        items.append({"f": f"{t}_{f.name}", "t": t, "p": p, "c": round(float(r.probs.top1conf), 3)})
        shutil.copy(f, OUT / "img" / f"{t}_{f.name}")
(OUT / "data.json").write_text(json.dumps({"names": names, "items": items}, ensure_ascii=False))
print(len(items), sum(i["t"] == i["p"] for i in items))
