"""生成第 9 章交互动画“增强现实贴图”的背景图（编者用）。在仓库根目录运行。"""
from pathlib import Path

import cv2

ROOT = Path(__file__).resolve().parents[2]
img = cv2.imread(str(ROOT / "labs/data/images/marker_road.jpg"))
crop = img[340:700, 320:960]                     # 640×360，标记码在下方中间
cv2.imwrite(str(ROOT / "docs/sims/ar-homography/img/road.jpg"), crop, [cv2.IMWRITE_JPEG_QUALITY, 85])
corners, ids, _ = cv2.aruco.ArucoDetector(cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)).detectMarkers(crop)
print("标记码四角（动画里用）：", corners[0].reshape(4, 2).round().astype(int).tolist())
