"""生成第 6 章配图（编者用）。先在 labs/ch06 中运行实验 6-1～6-4，再在仓库根目录运行本脚本。"""
from pathlib import Path

import cv2
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
L = ROOT / "labs/ch06"
OUT = ROOT / "docs/chapters/06-segmentation/images"
OUT.mkdir(parents=True, exist_ok=True)
SIM = ROOT / "docs/sims/seg-types/img"
PAL = [[128,64,128],[244,35,232],[70,70,70],[102,102,156],[190,153,153],[153,153,153],[250,170,30],[220,220,0],[107,142,35],[152,251,152],[70,130,180],[220,20,60],[255,0,0],[0,0,142],[0,0,70],[0,60,100],[0,80,100],[0,0,230],[119,11,32]]
IC = [[230,25,75],[60,180,75],[255,225,25],[0,130,200],[245,130,48],[145,30,180],[70,240,240],[240,50,230],[210,245,60],[250,190,212],[0,128,128]]


def save(name, img):
    cv2.imwrite(str(OUT / name), img, [cv2.IMWRITE_JPEG_QUALITY, 88])
    print(name, img.shape)


def label(img, text):
    img = img.copy()
    cv2.rectangle(img, (0, 0), (12 + 13 * len(text), 30), (0, 0, 0), -1)
    cv2.putText(img, text, (6, 22), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    return img


# 图 6-1 三种分割（标签用英文，图注里写中文）
photo = cv2.imread(str(SIM / "city.jpg"))
sem = cv2.imread(str(SIM / "city_sem.png"), 0)
ins = cv2.imread(str(SIM / "city_inst.png"), 0)
pal = np.array(PAL, np.uint8)[:, ::-1]                       # RGB → BGR
ic = np.array(IC, np.uint8)[:, ::-1]
sem_c = pal[sem]
ins_c = np.where(ins[..., None] > 0, ic[(ins.astype(int) - 1) % len(IC)], (photo * 0.35).astype(np.uint8))
pan_c = np.where(ins[..., None] > 0, ic[(ins.astype(int) - 1) % len(IC)], sem_c)
mix = lambda c: cv2.addWeighted(photo, 0.4, c.astype(np.uint8), 0.6, 0)
grid = np.vstack([np.hstack([label(photo, "photo"), label(mix(sem_c), "semantic")]),
                  np.hstack([label(mix(ins_c), "instance"), label(mix(pan_c), "panoptic")])])
save("seg_types.jpg", cv2.resize(grid, None, fx=0.6, fy=0.6))

# 图 6-2 掩膜：原图、掩膜、蓝底
seg = cv2.imread(str(L / "lab6_1_seg.jpg"))
mask = cv2.cvtColor(cv2.imread(str(L / "lab6_1_mask.png"), 0), cv2.COLOR_GRAY2BGR)
newbg = cv2.imread(str(L / "lab6_1_newbg.jpg"))
h = 480
row = [cv2.resize(x, (int(x.shape[1] * h / x.shape[0]), h)) for x in [seg, mask, newbg]]
save("mask_cutout.jpg", np.hstack(row))

# 图 6-3 可行驶路面
save("road.jpg", cv2.imread(str(L / "lab6_2_road.jpg")))
save("sem_city.jpg", cv2.imread(str(L / "lab6_2_sem.jpg")))

# 图 6-4 SAM 点与框
a = cv2.imread(str(L / "lab6_3_point.jpg")); b = cv2.imread(str(L / "lab6_3_det_sam.jpg"))
save("sam.jpg", cv2.resize(np.vstack([a, b]), None, fx=0.5, fy=0.5))

# 图 6-5 深度图与远近
c = cv2.imread(str(L / "lab6_4_color.jpg")); n = cv2.imread(str(L / "lab6_4_near.jpg"))
save("depth.jpg", np.vstack([c, n]))
