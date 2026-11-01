# 第 3 章配图（编者用）：先运行 labs/ch03 的实验，再运行本脚本
import cv2, numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path
plt.rcParams["font.sans-serif"] = ["WenQuanYi Zen Hei"]; plt.rcParams["axes.unicode_minus"] = False
R = str(Path(__file__).resolve().parents[2]) + "/"
D = R + "labs/data/images/"; L = R + "labs/ch03/"; O = R + "docs/chapters/03-features/images/"
rgb = lambda im: cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
def grid(ims, titles, path, rows, cols, size):
    fig, ax = plt.subplots(rows, cols, figsize=size)
    for a, im, t in zip(np.ravel(ax), ims, titles):
        a.imshow(im, cmap="gray", vmin=0, vmax=255) if im.ndim == 2 else a.imshow(rgb(im))
        a.set_title(t, fontsize=12); a.axis("off")
    plt.tight_layout(); plt.savefig(O + path, dpi=110, bbox_inches="tight"); plt.close()
# 1 kernels
g = cv2.imread(D + "drive_city.jpg", 0)
grid([g] + [cv2.imread(L + f"lab3_2_{n}.jpg", 0) for n in ["blur", "sharpen", "edge_v", "edge_h"]] + [cv2.Canny(cv2.GaussianBlur(g, (5, 5), 0), 50, 150)],
     ["原图（灰度）", "平均核：模糊", "锐化核：更清楚", "竖直边缘核（Sobel）", "水平边缘核（Sobel 转置）", "Canny 边缘（50, 150）"], "kernels.jpg", 3, 2, (13, 7.2))
# 2 canny thresholds
lane = cv2.imread(D + "lane_white.jpg"); lb = cv2.GaussianBlur(cv2.cvtColor(lane, cv2.COLOR_BGR2GRAY), (5, 5), 0)
ts = [(10, 30), (50, 150), (150, 300)]
grid([cv2.Canny(lb, a, b) for a, b in ts], [f"低 {a}、高 {b}：{cv2.countNonZero(cv2.Canny(lb, a, b))} 个边缘像素" for a, b in ts], "canny.jpg", 1, 3, (15, 3.2))
# 3 lane pipeline
h, w = lb.shape; top = int(h * 0.6)
e = cv2.Canny(lb, 50, 150); m = np.zeros_like(e)
cv2.fillPoly(m, np.array([[(int(w * .1), h), (int(w * .45), top), (int(w * .55), top), (int(w * .95), h)]]), 255)
roi = cv2.bitwise_and(e, m); mk = cv2.addWeighted(cv2.cvtColor(e, cv2.COLOR_GRAY2BGR), 1, cv2.cvtColor(m, cv2.COLOR_GRAY2BGR) // 4 * np.array([0, 1, 1], np.uint8), 1, 0)
grid([e, mk, roi, cv2.imread(L + "lab3_3_lanes.jpg")], ["① Canny 边缘", "② 梯形感兴趣区域（黄色）", "③ 只留梯形里的边缘", "④ 霍夫直线：红为左、绿为右"], "lane_pipeline.jpg", 2, 2, (12, 7))
# 4 pills
grid([cv2.imread(D + "pills.jpg"), cv2.imread(L + "lab3_1_pills.jpg")], ["药片照片", "11 个轮廓，第 7 个面积约是一颗的 2 倍"], "pills_count.jpg", 1, 2, (12, 4.6))
# 5 ORB + template
cap = cv2.VideoCapture(R + "labs/data/videos/highway_12s.mp4"); fr = []
for i in range(60):
    ok, f = cap.read()
    if i in (0, 59): fr.append(f)
orb = cv2.ORB_create(500)
k1, d1 = orb.detectAndCompute(fr[0], None); k2, d2 = orb.detectAndCompute(fr[1], None)
ms = sorted(cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True).match(d1, d2), key=lambda m: m.distance)[:40]
vis = cv2.drawMatches(fr[0], k1, fr[1], k2, ms, None, flags=2)
fig, ax = plt.subplots(figsize=(13, 3.8)); ax.imshow(rgb(vis)); ax.axis("off")
ax.set_title(f"ORB 关键点匹配：相隔 59 帧的两幅画面，各找 {len(k1)}、{len(k2)} 个关键点，画出最像的 40 对", fontsize=12)
plt.tight_layout(); plt.savefig(O + "orb.jpg", dpi=100, bbox_inches="tight"); plt.close()
print("orb", len(k1), len(k2))
# 6 privacy
grid([cv2.imread(D + "drive_city.jpg"), cv2.imread(L + "lab3_4_privacy.jpg")], ["原图", "两块车牌、一位行人的头部打上马赛克"], "privacy.jpg", 2, 1, (12, 7.5))
