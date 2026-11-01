# 第 4 章“CNN 逐层看到了什么”动画的数据（编者用）：用 yolo26n-cls 提取各层特征图，存成拼图
import json, cv2, numpy as np, torch
from pathlib import Path
from ultralytics import YOLO
R = Path(__file__).resolve().parents[2]
OUT = R / "docs/sims/cnn-layers/img"
model = YOLO(str(R / "labs/ch04/yolo26n-cls.pt"))
net = model.model.eval()
img = cv2.imread(str(R / "labs/data/images/drive_city.jpg"))
lane = cv2.imread(str(R / "labs/data/images/lane_white.jpg"))
kitti = cv2.imread(str(R / "labs/data/kitti_sample/000380.jpg"))
srcs = {"van": img[150:240, 385:530], "ped": kitti[160:255, 985:1045], "lane": lane[300:540, 200:760]}
LAYERS = [0, 2, 4, 6, 8]
feats = {}
hooks = [net.model[i].register_forward_hook(lambda m, a, o, i=i: feats.__setitem__(i, o.detach())) for i in LAYERS]
meta = {}
for key, im in srcs.items():
    x = cv2.resize(cv2.cvtColor(im, cv2.COLOR_BGR2RGB), (224, 224))
    cv2.imwrite(str(OUT / f"{key}_input.jpg"), cv2.cvtColor(x, cv2.COLOR_RGB2BGR))
    t = torch.from_numpy(x).permute(2, 0, 1).float().unsqueeze(0) / 255
    with torch.no_grad():
        p = net(t)
    p = p[0] if isinstance(p, (list, tuple)) else p
    top = torch.topk(p[0], 3)
    meta[key] = {"top": [[model.names[int(i)], round(float(v), 3)] for v, i in zip(top.values, top.indices)], "layers": {}}
    for i in LAYERS:
        f = feats[i][0]
        C, H, W = f.shape
        idx = torch.argsort(f.abs().mean((1, 2)), descending=True)[:16]     # 最活跃的 16 个通道
        tiles = []
        for c in idx:
            a = f[c].numpy(); a = (a - a.min()) / (a.max() - a.min() + 1e-6) * 255
            tiles.append(cv2.resize(a.astype(np.uint8), (96, 96), interpolation=cv2.INTER_NEAREST))
        rows = [np.hstack(tiles[r * 4:(r + 1) * 4]) for r in range(4)]
        cv2.imwrite(str(OUT / f"{key}_L{i}.jpg"), np.vstack(rows), [cv2.IMWRITE_JPEG_QUALITY, 85])
        meta[key]["layers"][str(i)] = [C, H, W]
for h in hooks: h.remove()
(OUT / "meta.json").write_text(json.dumps(meta, ensure_ascii=False))
print(json.dumps(meta, ensure_ascii=False)[:600])
