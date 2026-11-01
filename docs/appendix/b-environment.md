---
title: 附录 B 实验环境与资源说明
description: 本书实验用到的 OpenCV、Ultralytics YOLO、Gradio 等工具的常用写法速查，每条都注明书中第一次用到的位置
---

# 附录 B 实验环境与资源说明

本附录只收录书中实验真正用到的写法，按“要做什么”分类，方便做实验和开卷考试时查找。`img` 表示 OpenCV 读入的图片（NumPy 数组，BGR 顺序），`model` 表示 Ultralytics 的模型，`r` 表示一张图的结果。

## B.1 安装

```bash
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

`labs/requirements.txt` 列出了本书用到的全部库和编者实测的版本，详见附录 C。单独安装某个库：

| `import` 写法 | `pip install` 的名字 | 用于 |
|---|---|---|
| `import cv2` | `opencv-python` | 读写、处理图片和视频 |
| `import numpy as np` | `numpy` | 数组运算 |
| `import matplotlib.pyplot as plt` | `matplotlib` | 显示图片、画曲线 |
| `from ultralytics import YOLO` | `ultralytics` | 分类、检测、分割、姿态、跟踪、深度 |
| `import gradio as gr` | `gradio` | 做网页（第 9 章） |
| `from PIL import Image` | `pillow` | PIL 图片（第 8 章） |
| `from diffusers import ...` | `diffusers transformers accelerate` | 图像生成（第 8 章，需要 GPU） |

## B.2 OpenCV：读写与显示

| 写法 | 作用 | 首次出现 |
|---|---|---|
| `img = cv2.imread("a.jpg")` | 读图，得到 (高, 宽, 3) 的 BGR 数组；路径错了返回 `None` | 实验 1-1 |
| `gray = cv2.imread("a.jpg", 0)` | 读成灰度图，形状 (高, 宽) | 实验 2-1 |
| `cv2.imwrite("b.jpg", img)` | 存图，后缀决定格式 | 实验 1-1 |
| `h, w = img.shape[:2]` | 取高和宽 | 实验 1-2 |
| `img[y1:y2, x1:x2]` | 裁剪（先行后列） | 实验 1-2 |
| `cv2.cvtColor(img, cv2.COLOR_BGR2RGB)` | BGR 转 RGB（给 Matplotlib、Gradio、PIL） | 实验 1-1 |
| `cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)` | 转灰度 | 实验 2-1 |
| `cv2.cvtColor(img, cv2.COLOR_BGR2HSV)` | 转 HSV | 实验 2-1 |
| `cv2.resize(img, (宽, 高))` | 缩放到指定大小（注意先宽后高） | 实验 2-1 |
| `cv2.resize(img, None, fx=4, fy=4)` | 按比例缩放 | 实验 8-1 |
| `cv2.resize(..., interpolation=cv2.INTER_CUBIC)` | 指定插值：`INTER_NEAREST` 最近邻、`INTER_CUBIC` 双三次、`INTER_AREA` 缩小时用 | 实验 8-1 |
| `plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))` | 在 Notebook 里显示图片 | 实验 1-1 |

## B.3 OpenCV：视频

```python
cap = cv2.VideoCapture("../data/videos/highway_12s.mp4")   # 打开视频（写 0 是打开摄像头）
fps = cap.get(cv2.CAP_PROP_FPS)                            # 帧率
n = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))                 # 总帧数
w, h = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
writer = cv2.VideoWriter("out.mp4", fourcc, fps, (w, h))   # 写视频：文件名、编码、帧率、(宽, 高)
while True:
    ok, frame = cap.read()                                 # 读一帧；读完了 ok 为 False
    if not ok:
        break
    writer.write(frame)                                    # 写一帧（大小必须和 (w, h) 一致）
cap.release()
writer.release()
```

首次出现：实验 7-1。

## B.4 OpenCV：调色、去噪、二值化

| 写法 | 作用 | 首次出现 |
|---|---|---|
| `cv2.convertScaleAbs(img, alpha=1.5, beta=30)` | 调对比度（乘 alpha）和亮度（加 beta） | 实验 2-2 |
| `cv2.equalizeHist(gray)` | 直方图均衡化（灰度图） | 实验 2-2 |
| `cv2.GaussianBlur(img, (5, 5), 0)` | 高斯滤波，窗口必须是奇数 | 第 2 章、实验 3-1 |
| `cv2.medianBlur(img, 5)` | 中值滤波，去椒盐噪声 | 实验 2-2 |
| `_, binary = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY)` | 二值化：大于 140 变 255，否则 0 | 实验 3-4 |
| `cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)` | 自动选门槛（大津法） | 实验 3-1 |
| `mask = cv2.inRange(hsv, 下限, 上限)` | 按颜色范围找像素，得到掩膜 | 实验 2-1 |
| `cv2.bitwise_and(a, b)` | 两张黑白图都为白的地方才留下（只看感兴趣区域） | 实验 3-3 |
| `cv2.countNonZero(mask)` | 数掩膜里非零像素的个数 | 实验 2-1 |
| `k = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))` | 生成形态学运算的窗口 | 实验 3-4 |
| `cv2.morphologyEx(binary, cv2.MORPH_CLOSE, k)` | 闭运算把断开的白色区域连起来；`MORPH_OPEN` 开运算去小白点；`MORPH_TOPHAT` 顶帽找细小亮物 | 实验 3-4、8-2 |
| `cv2.dilate(mask, k)` | 膨胀：白色区域向外扩 | 实验 8-2 |
| `cv2.inpaint(img, mask, 3, cv2.INPAINT_TELEA)` | 图像修复，遮罩为单通道 uint8 | 实验 8-2 |

## B.5 OpenCV：边缘、直线、轮廓、卷积

| 写法 | 作用 | 首次出现 |
|---|---|---|
| `cv2.Canny(gray, 50, 150)` | Canny 边缘检测，低门槛、高门槛 | 实验 3-3 |
| `lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, minLineLength=40, maxLineGap=20)` | 霍夫变换找线段；OpenCV 5 中用 `lines.reshape(-1, 4)` 得到每条线的 x1, y1, x2, y2 | 实验 3-3 |
| `contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)` | 找外轮廓 | 实验 3-1 |
| `cv2.contourArea(c)` | 轮廓面积 | 实验 3-1 |
| `x, y, w, h = cv2.boundingRect(c)` | 外接矩形 | 实验 3-1 |
| `cv2.pointPolygonTest(区域, (x, y), False)` | 点在多边形内为正数、外为负数（区域闯入） | 实验 7-2 |
| `cv2.filter2D(gray, -1, kernel)` | 用自己写的卷积核做卷积 | 实验 3-2 |
| `cv2.Laplacian(gray, cv2.CV_64F).var()` | 拉普拉斯方差，衡量清晰度 | 实验 8-1 |

## B.6 OpenCV：画图

| 写法 | 作用 |
|---|---|
| `cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)` | 画矩形：左上角、右下角、颜色 (B, G, R)、线宽（-1 为填充） |
| `cv2.putText(img, "car", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)` | 写字（只支持英文和数字） |
| `cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3)` | 画线 |
| `cv2.circle(img, (x, y), 5, (0, 255, 255), -1)` | 画圆 |
| `cv2.polylines(img, [pts], True, (0, 255, 0), 2)` | 画多边形边框 |
| `cv2.fillPoly(img, [pts], (0, 220, 255))` | 填充多边形 |
| `cv2.applyColorMap(gray, cv2.COLORMAP_JET)` | 把灰度图（如深度图）上色 |

画图函数会**直接改动**原图，想保留原图先 `out = img.copy()`。

## B.7 OpenCV：透视变换与标记码（第 9 章）

```python
H = cv2.getPerspectiveTransform(src4, dst4)          # 四对点 → 3×3 单应性矩阵（float32）
warped = cv2.warpPerspective(img, H, (宽, 高))        # 按 H 变形
M = np.float32([[sx, 0, tx], [0, sy, ty]])           # 只缩放平移的 2×3 矩阵
moved = cv2.warpAffine(img, M, (宽, 高))
aruco = cv2.aruco
dictionary = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
marker = aruco.generateImageMarker(dictionary, 7, 240)           # 生成 7 号码
detector = aruco.ArucoDetector(dictionary, aruco.DetectorParameters())
corners, ids, rejected = detector.detectMarkers(img)            # 找码；没找到时 ids 为 None
```

## B.8 Ultralytics YOLO：模型

| 文件名 | 任务 | 首次出现 |
|---|---|---|
| `yolo26n-cls.pt` | 图像分类（ImageNet 1000 类） | 实验 1-3、4-1 |
| `yolo26n.pt` | 目标检测（COCO 80 类：person、car、bus、truck……） | 实验 1-3、5-1 |
| `yolo26n-seg.pt` | 实例分割 | 实验 1-3、6-1 |
| `yolo26n-pose.pt` | 姿态估计（17 个人体关键点） | 实验 1-3、7-3 |
| `yolo26n-sem.pt` | 道路语义分割（Cityscapes 19 类，0 号是路面） | 实验 6-2 |
| `yolo26n-depth.pt` | 单目深度估计 | 实验 6-4 |
| `mobile_sam.pt` | 分割一切（`from ultralytics import SAM`） | 实验 6-3 |

模型第一次使用时自动下载。`n` 可以换成 `s`、`m`、`l`、`x`，越往后越大、越准、越慢；`26` 可以换成 `11`（YOLO11），写法相同。

## B.9 Ultralytics YOLO：运行与结果

```python
from ultralytics import YOLO
model = YOLO("yolo26n.pt")
r = model("../data/images/drive_city.jpg", conf=0.25, imgsz=640, verbose=False)[0]   # 一张图取 [0]
```

| 参数 | 作用 | 首次出现 |
|---|---|---|
| `conf=0.25` | 置信度门槛，低于它的框不要 | 实验 5-2 |
| `imgsz=640` | 输入尺寸，越小越快、小目标越容易漏 | 实验 9-4 |
| `classes=[0, 2]` | 只要指定类别（0 是 person，2 是 car） | 实验 3-4 |
| `retina_masks=True` | 实例分割掩膜与原图同样大小 | 实验 6-1 |
| `verbose=False` | 不在终端打印每张图的信息 | 实验 5-1 |

| 结果 | 内容 | 任务 |
|---|---|---|
| `r.names` | 字典：类别编号 → 类别名 | 全部 |
| `r.plot()` | 画好框（或掩膜、骨架）的 BGR 图 | 全部 |
| `r.probs.top1`、`r.probs.top1conf`、`r.probs.top5` | 最可能的类别编号、它的置信度、前 5 个类别编号 | 分类 |
| `r.boxes.xyxy` | 每个框的左上角和右下角 (x1, y1, x2, y2) | 检测、分割、姿态 |
| `r.boxes.cls`、`r.boxes.conf` | 每个框的类别编号、置信度 | 检测 |
| `r.boxes.id` | 每个框的号码牌（跟踪时才有） | 跟踪 |
| `r.masks.data` | 每个目标的掩膜，形状 (目标数, 高, 宽) | 实例分割 |
| `r.keypoints.xy` | 每个人 17 个关键点的坐标，形状 (人数, 17, 2) | 姿态 |
| `r.semantic_mask.data` | 每个像素的类别编号图 | 语义分割 |
| `r.depth.data` | 每个像素的估计深度（约为米） | 深度估计 |

结果大多是 PyTorch 张量，转成 NumPy 或 Python 列表：`.cpu().numpy()`、`.tolist()`、`.int().tolist()`。

## B.10 Ultralytics YOLO：训练、验证、跟踪、导出

```python
model = YOLO("yolo26n.pt")                                     # 从预训练模型开始（迁移学习）
model.train(data="kitti_small.yaml", epochs=20, imgsz=640, batch=16, device="cpu")
best = YOLO("runs/kitti20/weights/best.pt")                    # 训练中验证集上最好的一版
m = best.val(data="kitti_small.yaml")
print(m.box.map50, m.box.map, m.box.mp, m.box.mr)              # mAP50、mAP50-95、精确率、召回率
for r in model.track("video.mp4", stream=True, persist=True, verbose=False):   # 逐帧跟踪
    ids = r.boxes.id                                           # 号码牌；没有目标时为 None
model.export(format="onnx")                                    # 导出 ONNX；还可以 "ncnn"、"paddle"、"openvino" 等
```

分类模型 `data=` 填数据集文件夹（里面有 train、val，每类一个子文件夹），验证结果用 `metrics.top1`、`metrics.top5`（实验 4-3）。分割一切模型：`SAM("mobile_sam.pt")(img, points=[[x, y]], labels=[1])` 或 `bboxes=[[x1, y1, x2, y2]]`（实验 6-3）。

## B.11 Gradio（第 9 章）

```python
import gradio as gr
demo = gr.Interface(fn=analyze,                                       # 函数本身，不加括号
                    inputs=[gr.Image(type="numpy"), gr.Slider(5, 30, value=10)],   # 对应函数的参数
                    outputs=[gr.Image(), gr.Textbox()],               # 对应函数的返回值
                    examples=[["../data/images/drive_city.jpg", 10]])
demo.launch()                       # 本机；share=True 生成临时公开链接；server_name="0.0.0.0" 局域网访问
```

常用组件：`gr.Image`、`gr.Video`、`gr.Slider`、`gr.Textbox`、`gr.Number`、`gr.Dropdown`。`gr.Image(type="numpy")` 给函数的是 **RGB** 数组。
