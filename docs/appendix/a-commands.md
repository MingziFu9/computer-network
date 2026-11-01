---
title: 附录 A 常用网络命令速查
description: 本书实验用到的约 16 个 Python 知识点：变量、列表、字典、判断、循环、函数、导入库、文件路径、NumPy 数组与切片、布尔索引、BGR 与 RGB、try 和读懂报错，每个都配可运行的小例子和练习
---

# 附录 A 常用网络命令速查

本附录把全书实验用到的 Python 知识集中讲一遍。它不是完整的 Python 教程，只讲本书真正用到的写法，每个知识点都配一段能直接运行的小例子。建议：

- 第 1 章之前先读 A.1～A.3，其余的在正文“Python 小课堂”遇到时再回来查；
- 把例子复制到 Notebook 的单元格里运行一遍，再改一改数字，看结果怎么变；
- 做完每节后面的小练习，答案在本附录最后。

| 知识点 | 本书第一次用到 |
|---|---|
| A.1 运行代码、print、注释 | 第 1 章 |
| A.2 变量和数据类型 | 第 1 章 |
| A.3 列表 | 第 1 章 |
| A.4 字典 | 第 4 章 |
| A.5 if 判断 | 第 3 章 |
| A.6 for 循环 | 第 2 章 |
| A.7 while 循环 | 第 7 章 |
| A.8 函数 | 第 2 章 |
| A.9 导入库 | 第 1 章 |
| A.10 文件和路径 | 第 2 章 |
| A.11 NumPy 数组：图片就是数组 | 第 1 章 |
| A.12 布尔索引：用掩膜挑像素 | 第 6 章 |
| A.13 BGR、RGB 和 PIL 图片 | 第 1、8 章 |
| A.14 集合 | 第 7 章 |
| A.15 try：出错了也不中断 | 第 9 章 |
| A.16 读懂报错 | 全书 |

## A.1 运行代码、print、注释 { #a1 }

在 Notebook 里选中一个单元格，按 **Shift + Enter** 运行。`print` 把结果显示出来；`#` 后面是注释，给人看的，程序会跳过。

```python
print("你好，计算机视觉")      # 显示一行字
print(1280 * 720)            # 也可以显示算式的结果：921600
```

Notebook 有一个方便的地方：单元格的**最后一行**如果是一个值，不用 `print` 也会显示出来。

## A.2 变量和数据类型 { #a2 }

变量就是给一个值起个名字，用 `=` 把右边的值“装进”左边的名字里。

```python
width = 1280            # 整数 int
height = 720
ratio = width / height  # 小数 float：1.777...
name = "drive_city.jpg" # 字符串 str：用引号括起来
is_night = False        # 布尔值 bool：True 或 False
print(type(ratio), type(name))
```

**f-string**：在字符串前加 `f`，就能把变量“填”进去；`:.2f` 表示保留两位小数，`:.0%` 表示显示成百分数。

```python
conf = 0.8734
print(f"找到一辆车，置信度 {conf:.2f}")     # 找到一辆车，置信度 0.87
print(f"路面占 {0.163:.0%}")               # 路面占 16%
```

**小练习 A-1**：一张图片宽 640、高 480，用变量算出它一共有多少个像素，用 f-string 打印“共 307200 个像素”。

## A.3 列表 { #a3 }

列表用方括号，把多个值按顺序放在一起。**下标从 0 开始**，`-1` 表示最后一个。

```python
names = ["car", "truck", "pedestrian", "cyclist"]
print(names[0], names[-1])     # car cyclist
print(len(names))              # 4 个
names.append("van")            # 在末尾加一个
print(names[1:3])              # 切片：取第 1、2 个（不含 3）→ ['truck', 'pedestrian']
print("bus" in names)          # 判断在不在里面 → False
```

切片 `[开始:结束]` 包含开始、**不包含**结束。这个规则和后面 NumPy 裁剪图片完全一样。

**小练习 A-2**：`scores = [0.91, 0.45, 0.78, 0.30]`，打印第一个和最后一个分数，再打印列表的长度。

## A.4 字典 { #a4 }

字典用花括号，存放“键 → 值”的对应关系，通过键查值。

```python
cn = {"car": "车", "person": "行人", "bus": "大客车"}
print(cn["car"])                  # 车
cn["truck"] = "卡车"              # 加一对
print(cn.get("dog", "不认识"))     # 找不到时返回“不认识”，不报错
for en, zh in cn.items():         # 同时取出键和值
    print(en, "→", zh)
```

Ultralytics 的结果里，`r.names` 就是一个字典：`{0: 'person', 1: 'bicycle', 2: 'car', …}`，用类别编号查类别名。

**小练习 A-3**：用字典记录三种天气对应的英文：晴天 sunny、雨天 rainy、雪天 snowy，然后打印“雨天 → rainy”。

## A.5 if 判断 { #a5 }

```python
dist = 6.5
if dist < 5:
    print("太近了，请减速")
elif dist < 10:                 # 否则如果
    print("注意保持距离")
else:                           # 其他情况
    print("距离正常")
```

注意两点：条件后面有**冒号**；属于这个条件的代码要**缩进 4 个空格**。缩进不对是初学者最常见的报错之一。

比较符号：`==` 等于（两个等号！）、`!=` 不等于、`>`、`<`、`>=`、`<=`；组合条件用 `and`、`or`、`not`。

**小练习 A-4**：变量 `angle` 是肘关节角度。大于 140 打印“撑起”，小于 100 打印“压下”，其他打印“中间”。

## A.6 for 循环 { #a6 }

`for` 把列表里的东西一个一个拿出来处理。

```python
for name in ["drive_city.jpg", "drive_night.jpg"]:
    print("正在处理", name)

for i in range(3):              # range(3) 是 0、1、2
    print("第", i, "次")

for i, name in enumerate(["car", "bus"]):   # 同时拿到序号和值
    print(i, name)

for box, score in zip([[1, 2, 3, 4], [5, 6, 7, 8]], [0.9, 0.6]):   # 两个列表一起走
    print(box, score)
```

**列表推导式**：把“循环 + 放进新列表”写成一行。

```python
scores = [0.91, 0.45, 0.78, 0.30]
high = [s for s in scores if s > 0.5]   # 只留大于 0.5 的 → [0.91, 0.78]
```

**小练习 A-5**：用 for 循环算出 `[3, 5, 2, 6]` 中所有数的和。

## A.7 while 循环 { #a7 }

`while` 在条件成立时一直重复。第 7 章读视频就是这样写的：只要还读得到下一帧，就继续处理。

```python
count = 0
while count < 3:
    print("处理第", count, "帧")
    count += 1                # 等于 count = count + 1；忘了写就会永远循环下去
```

读视频的固定写法：

```python
cap = cv2.VideoCapture("../data/videos/highway_12s.mp4")
while True:
    ok, frame = cap.read()    # ok 表示有没有读到
    if not ok:
        break                 # 读完了，跳出循环
    # ……处理 frame……
cap.release()
```

## A.8 函数 { #a8 }

函数把一段代码包起来起个名字，以后一行就能调用。`def` 定义，`return` 返回结果。

```python
def area(w, h):
    return w * h

def warn(dist, near=10):        # near 有默认值 10，调用时可以不给
    return "注意" if dist < near else "正常"

print(area(1280, 720))          # 921600
print(warn(6.5), warn(12), warn(12, 15))   # 注意 正常 注意
```

**函数也可以当参数**：`gr.Interface(fn=analyze, ...)` 中 `analyze` 不加括号，表示把函数本身交给 Gradio，等用户点了按钮再由它调用（第 9 章）。

**小练习 A-6**：写一个函数 `fps(ms)`，输入每张图的毫秒数，返回每秒能处理几张（1000 ÷ ms）。

## A.9 导入库 { #a9 }

别人写好的工具放在“库”里，用之前要导入。

```python
import cv2                        # 导入整个库，用 cv2.imread(...)
import numpy as np                # 导入并起个短名字，用 np.array(...)
from ultralytics import YOLO      # 只导入库里的一样东西，直接用 YOLO(...)
from pathlib import Path
```

报 `ModuleNotFoundError: No module named 'xxx'`，说明这个库没装，在命令行运行 `pip install xxx`。注意几个名字不一样的：`import cv2` 要装 `opencv-python`，`from PIL import Image` 要装 `pillow`。

## A.10 文件和路径 { #a10 }

实验代码都要在 `labs/chNN/` 文件夹里运行，数据在上一级的 `data` 文件夹，所以路径写成 `../data/...`。`..` 表示“上一级文件夹”。

```python
from pathlib import Path
p = Path("../data/images/drive_city.jpg")
print(p.exists(), p.name, p.stem, p.suffix)   # 文件在不在、文件名、不带后缀的名字、后缀
for f in sorted(Path("../data/images").glob("*.jpg")):   # 找出所有 jpg 文件（第 2 章批量处理）
    print(f.name)
Path("output").mkdir(exist_ok=True)           # 建一个文件夹，已经有了也不报错
```

报 `FileNotFoundError` 或 `cv2.imread` 返回 `None`，几乎都是路径不对：检查是不是在正确的文件夹里运行、文件名有没有拼错。

## A.11 NumPy 数组：图片就是数组 { #a11 }

OpenCV 读进来的图片是一个 NumPy 数组，形状是 **(高, 宽, 3)**。

```python
import cv2
img = cv2.imread("../data/images/drive_city.jpg")
print(img.shape, img.dtype)      # (375, 1242, 3) uint8：高 375、宽 1242、3 个通道，每个数 0～255
print(img[100, 200])             # 第 100 行、第 200 列的像素：[蓝 绿 红] 三个数
crop = img[150:300, 400:700]     # 裁剪：先行（y）后列（x），和列表切片规则一样
small = img[::2, ::2]            # 每隔一个取一个：宽高都缩小一半
```

常用的数组运算：

```python
import numpy as np
a = np.array([10, 200, 250], dtype=np.uint8)
print(a + 10)                       # [ 20 210   4]：uint8 超过 255 会“绕圈”！
b = a.astype(int) + 10              # 先换成普通整数再算 → [ 20 210 260]
print(np.clip(b, 0, 255))           # 限制在 0～255 → [ 20 210 255]
print(b.mean(), b.max(), b.min())   # 平均、最大、最小
```

`uint8` 的“绕圈”是很多奇怪结果的原因：两张图相减、调亮度之前，先用 `astype(int)` 或 `astype(np.float32)` 换成更大的类型，算完再 `clip` 并换回 `uint8`。

**小练习 A-7**：读入 `drive_city.jpg`，打印它的高和宽，再裁出左上角 100×100 的一块，打印这一块的形状。

## A.12 布尔索引：用掩膜挑像素 { #a12 }

对数组做比较，得到一个同样形状的 True/False 数组（掩膜）。用它当下标，就能一次挑出所有满足条件的像素（第 6 章）。

```python
import numpy as np
gray = np.array([[10, 200], [180, 30]])
mask = gray > 100                 # [[False  True] [ True False]]
print(mask.sum())                 # True 的个数：2
print(mask.mean())                # True 的比例：0.5
print(gray[mask])                 # 挑出来的值：[200 180]
gray[mask] = 255                  # 把满足条件的都改成 255
```

两个条件组合要用 `&`（且）、`|`（或），并且每个条件加括号：`(gray > 50) & (gray < 200)`。

## A.13 BGR、RGB 和 PIL 图片 { #a13 }

| 工具 | 颜色顺序 | 说明 |
|---|---|---|
| OpenCV（`cv2.imread`） | **BGR**（蓝、绿、红） | 本书大部分代码 |
| Matplotlib（`plt.imshow`） | RGB | 显示前要转换，否则红蓝颠倒 |
| Gradio（`gr.Image(type="numpy")`） | RGB | 第 9 章 |
| PIL（`Image.open`） | RGB | diffusers 等库用它（第 8 章） |

```python
import cv2
import matplotlib.pyplot as plt
img = cv2.imread("../data/images/drive_city.jpg")        # BGR
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))         # 转成 RGB 再显示
plt.axis("off")
plt.show()
```

## A.14 集合 { #a14 }

集合用花括号（但不是“键: 值”），里面的东西**不重复**。第 7 章用它记“已经数过的号码牌”。

```python
seen = set()                     # 空集合（不能写成 {}，那是空字典）
for track_id in [1, 2, 1, 3, 2]:
    seen.add(track_id)
print(seen, len(seen))           # {1, 2, 3} 3：重复的只算一次
print(2 in seen)                 # True
```

## A.15 try：出错了也不中断 { #a15 }

```python
try:
    x = 10 / 0                   # 这里会出错
except Exception as e:           # 出错就跳到这里
    print("出错了：", e)          # 出错了： division by zero
print("程序继续运行")
```

`try` 适合“可能失败但不影响大局”的步骤，比如联网下载、导出模型（第 9 章）。不要用它把所有报错都藏起来，否则真正的问题就看不到了。

## A.16 读懂报错 { #a16 }

Python 出错时会显示一大段红字（Traceback）。**只看最后一行**：冒号前是错误类型，冒号后是原因；再往上找带 `<module>` 或你自己文件名的那一行，那是出错的位置。

| 错误类型 | 意思 | 常见原因 |
|---|---|---|
| `SyntaxError` | 语法错误 | 少了冒号、括号或引号没配对、用了中文标点 |
| `IndentationError` | 缩进错误 | 该缩进的没缩进，或空格和 Tab 混用 |
| `NameError: name 'xxx' is not defined` | 名字没定义 | 变量拼错；前面定义变量的单元格没运行 |
| `ModuleNotFoundError` | 库没装 | 运行 `pip install` |
| `FileNotFoundError` | 文件找不到 | 路径不对、不在正确的文件夹运行 |
| `AttributeError: 'NoneType' object has no attribute 'shape'` | 对“空”取属性 | `cv2.imread` 没读到图（路径错了），返回了 `None` |
| `IndexError` | 下标超出范围 | 列表只有 3 个却取第 5 个；没检测到东西却取第 0 个 |
| `KeyError` | 字典里没有这个键 | 键拼错，或用 `.get()` 代替 `[]` |
| `TypeError` | 类型不对 | 字符串和数字直接相加；参数个数不对 |
| `ValueError` | 值不对 | 比如把 `"abc"` 转成整数 |

每章正文都有一张“本章常见报错对照”表，列出该章实验最容易遇到的报错。

## 小练习答案

**A-1**

```python
w, h = 640, 480
print(f"共 {w * h} 个像素")
```

**A-2**

```python
scores = [0.91, 0.45, 0.78, 0.30]
print(scores[0], scores[-1], len(scores))     # 0.91 0.3 4
```

**A-3**

```python
weather = {"晴天": "sunny", "雨天": "rainy", "雪天": "snowy"}
print("雨天 →", weather["雨天"])
```

**A-4**

```python
angle = 120
if angle > 140:
    print("撑起")
elif angle < 100:
    print("压下")
else:
    print("中间")
```

**A-5**

```python
total = 0
for x in [3, 5, 2, 6]:
    total += x
print(total)          # 16；也可以直接写 sum([3, 5, 2, 6])
```

**A-6**

```python
def fps(ms):
    return 1000 / ms
print(fps(250))       # 4.0
```

**A-7**

```python
import cv2
img = cv2.imread("../data/images/drive_city.jpg")
h, w = img.shape[:2]
print(h, w)                   # 375 1242
print(img[:100, :100].shape)  # (100, 100, 3)
```
