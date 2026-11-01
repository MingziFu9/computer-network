---
title: 在线模拟卷
description: 按期末开卷考试的题型和分值，从各章课后练习中组成的两套在线模拟卷，可以直接作答并查看解析
---

# 在线模拟卷

本课程期末为开卷考试，题目侧重理解和应用。下面两套模拟卷按期末考试的题型和分值，从各章课后练习中抽题组成，覆盖全书 9 章：

| 题型 | 题数 | 每题分值 | 合计 |
|---|---|---|---|
| 单项选择题 | 20 | 2 | 40 |
| 多项选择题 | 5 | 4 | 20 |
| 判断题 | 10 | 1 | 10 |
| 简答题 | 2 | 10 | 20 |
| 实操题 | 1 | 10 | 10 |

建议限时 90 分钟，先独立做完一整套，再展开“答案与解析”核对。简答题和实操题按参考答案的要点自评。实操题要在电脑上运行代码完成。选择题和判断题可以直接点击作答；每道题解析下方的“回看”链接可以跳回对应章节复习。

## 模拟卷一

**一、单项选择题**（每题 2 分）

<div class="quiz" data-answer="B" markdown>

**1.** 小林想知道一张路口照片里“有几个行人、分别在哪里”，应该选用哪种视觉任务？（　　）

- A. 图像分类
- B. 目标检测
- C. 图像生成
- D. 灰度转换

</div>

??? tip "答案与解析"
    **答案：B**

    目标检测给每个东西一个框，数框就知道有几个、在哪里。分类只给整张照片一个答案；图像生成是画新图；灰度转换是图像处理，不是识别任务。

    考查：五类视觉任务 · 认知层次：应用 · [回看 1.2.2](chapters/01-intro/index.md#122)
    { .quiz-meta }

<div class="quiz" data-answer="C" markdown>

**2.** 要把一张照片缩放成宽 640、高 360，正确的写法是（　　）。

- A. `cv2.resize(img, (360, 640))`
- B. `img[640, 360]`
- C. `cv2.resize(img, (640, 360))`
- D. `img.shape = (360, 640, 3)`

</div>

??? tip "答案与解析"
    **答案：C**

    `cv2.resize` 的尺寸是先宽后高。A 把宽高写反了，会得到竖着的图；B 是取一个像素；D 不能直接改形状来缩放。

    考查：缩放 · 认知层次：应用 · [回看 2.2.2](chapters/02-image-processing/index.md#222)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**3.** 图片中的“边缘”指的是（　　）。

- A. 图片最外面一圈像素
- B. 亮度变化剧烈的地方
- C. 颜色最鲜艳的地方
- D. 亮度最高的地方

</div>

??? tip "答案与解析"
    **答案：B**

    边缘是亮度突变的地方，通常对应物体的边界。A 是图片的边框；C、D 是颜色和亮度本身，不是“变化”。

    考查：边缘 · 认知层次：记忆 · [回看 3.2.1](chapters/03-features/index.md#321)
    { .quiz-meta }

<div class="quiz" data-answer="C" markdown>

**4.** 一个分类模型对某张图的 Top-5 结果依次是：卡车、厢式车、轿车、公交车、房车。这张图的真实类别是“轿车”，那么（　　）。

- A. Top-1 和 Top-5 都算认对
- B. Top-1 和 Top-5 都算认错
- C. Top-1 算认错，Top-5 算认对
- D. Top-1 算认对，Top-5 算认错

</div>

??? tip "答案与解析"
    **答案：C**

    Top-1 只看排第一的“卡车”，不对；Top-5 只要正确答案在前 5 名里，“轿车”排第 3，算对。

    考查：Top-1 与 Top-5 · 认知层次：应用 · [回看 4.1.2](chapters/04-classification/index.md#412)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**5.** 与图像分类相比，目标检测多回答了哪个问题？（　　）

- A. 图片是什么颜色
- B. 每个物体在图中的什么位置
- C. 图片拍摄的时间
- D. 图片有多少个像素

</div>

??? tip "答案与解析"
    **答案：B**

    分类只回答“是什么”，检测还回答“在哪里”，用边界框表示位置，并能数出有几个。

    考查：检测与分类的区别 · 认知层次：理解 · [回看 5.1.2](chapters/05-detection/index.md#512)
    { .quiz-meta }

<div class="quiz" data-answer="C" markdown>

**6.** 要算出行车画面中“路面”占多大比例，最合适的是（　　）。

- A. 图像分类
- B. 目标检测
- C. 语义分割
- D. 实例分割

</div>

??? tip "答案与解析"
    **答案：C**

    路面没有固定形状、也数不清“几个”，语义分割给每个像素一个类别，数一数路面像素即可（实验 6-2）。检测只能给框；实例分割只管人、车这些数得清的物体。

    考查：三种分割的用途 · 认知层次：应用 · [回看 6.1.2](chapters/06-segmentation/index.md#612)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**7.** 一段视频帧率 30 fps，共 900 帧，时长是（　　）。

- A. 900 秒
- B. 30 秒
- C. 27 秒
- D. 3 秒

</div>

??? tip "答案与解析"
    **答案：B**

    时长 = 总帧数 ÷ 帧率 = 900 ÷ 30 = 30 秒。

    考查：帧与帧率 · 认知层次：应用 · [回看 7.1.1](chapters/07-video/index.md#711)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**8.** 把一张晴天的行车照片改成雪天，同时保留道路和车辆的位置，最合适的是（　　）。

- A. 文生图
- B. 图生图
- C. 超分辨率
- D. 传统图像修复

</div>

??? tip "答案与解析"
    **答案：B**

    图生图在原图基础上加一部分噪声再按提示词去噪，能保留构图、改变天气等内容。

    考查：生成式视觉的任务 · 认知层次：应用 · [回看 8.1.1](chapters/08-generative/index.md#811)
    { .quiz-meta }

<div class="quiz" data-answer="C" markdown>

**9.** 小区周界的闯入报警系统，最可能用到的步骤组合是（　　）。

- A. 图像分类 → 超分辨率
- B. 文生图 → 局部重绘
- C. 检测人 → 跟踪 → 判断是否进入区域
- D. 深度估计 → 三维高斯泼溅

</div>

??? tip "答案与解析"
    **答案：C**

    闯入报警要知道“有人”（检测）、“是同一个人”（跟踪）、“进了区域”（规则判断），对应第 5、7 章。

    考查：行业案例拆解 · 认知层次：应用 · [回看 9.1.1](chapters/09-applications/index.md#911)
    { .quiz-meta }

<div class="quiz" data-answer="C" markdown>

**10.** 一张彩色图片用 OpenCV 读入后，`img.shape` 是 `(720, 1280, 3)`，下面说法正确的是（　　）。

- A. 图片宽 720 像素、高 1280 像素
- B. 图片一共有 720 × 1280 = 921600 个数字
- C. 图片高 720 像素、宽 1280 像素，每个像素有 3 个数
- D. 3 表示图片有 3 种物体

</div>

??? tip "答案与解析"
    **答案：C**

    形状的顺序是（高, 宽, 通道数）。A 把高宽写反了；B 漏乘了通道数 3，实际有 2764800 个数字；D 把通道数理解错了。

    考查：图片的形状 · 认知层次：理解 · [回看 1.3.4](chapters/01-intro/index.md#134)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**11.** 图片 `img` 的形状是 `(540, 960, 3)`，`img[320:, :]` 取出的是（　　）。

- A. 左边 320 列
- B. 第 320 行到最后一行、所有列，即画面下面的 220 行
- C. 上面 320 行
- D. 第 320 个像素

</div>

??? tip "答案与解析"
    **答案：B**

    切片先写行、后写列。`320:` 表示从第 320 行到最后，`:` 表示所有列，得到 540 − 320 = 220 行，形状 `(220, 960, 3)`，也就是实验 2-3 的感兴趣区域。

    考查：裁剪与感兴趣区域 · 认知层次：理解 · [回看 2.2.4](chapters/02-image-processing/index.md#224)
    { .quiz-meta }

<div class="quiz" data-answer="C" markdown>

**12.** `cv2.Canny(blur, 50, 150)` 中，一个变化强度为 100 的像素，最终会不会成为边缘？（　　）

- A. 一定会，因为大于 50
- B. 一定不会，因为小于 150
- C. 要看它是否和强度大于 150 的边缘相连
- D. 要看它的颜色

</div>

??? tip "答案与解析"
    **答案：C**

    强度介于两个门槛之间的是“弱边缘”，只有连到强边缘（大于高门槛）才保留，孤立的就丢掉。这就是双门槛的作用。

    考查：Canny 双门槛 · 认知层次：理解 · [回看 3.2.3](chapters/03-features/index.md#323)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**13.** 用 ImageNet 预训练的分类模型识别一张行人照片，结果是“防弹背心”，最主要的原因是（　　）。

- A. 照片太大
- B. 模型学过的 1000 类里没有“人”这一类
- C. 模型没有联网
- D. 照片是彩色的

</div>

??? tip "答案与解析"
    **答案：B**

    分类模型只能从学过的类别里挑一个最像的，ImageNet 的 1000 类里没有“人”。要认行人，就要用包含行人类别的数据重新训练。

    考查：预训练模型的类别 · 认知层次：理解 · [回看 4.1.3](chapters/04-classification/index.md#413)
    { .quiz-meta }

<div class="quiz" data-answer="C" markdown>

**14.** 两个框的交集面积是 30，各自的面积分别是 50 和 40，它们的交并比是（　　）。

- A. 0.6
- B. 0.75
- C. 0.5
- D. 0.33

</div>

??? tip "答案与解析"
    **答案：C**

    并集 = 50 + 40 − 30 = 60，交并比 = 30 ÷ 60 = 0.5。A 是 30 ÷ 50；B 是 30 ÷ 40；都没有用并集。

    考查：交并比计算 · 认知层次：应用 · [回看 5.2.1](chapters/05-detection/index.md#521)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**15.** 路边并排停着两辆车，语义分割的结果是（　　）。

- A. 两辆车各一种颜色，能分开
- B. 两辆车都是“轿车”这一种颜色，连成一片
- C. 两辆车都不显示
- D. 只显示置信度高的那一辆

</div>

??? tip "答案与解析"
    **答案：B**

    语义分割只回答“是什么类别”，不区分是第几个。要分开两辆车，需要实例分割或全景分割。

    考查：语义分割与实例分割的区别 · 认知层次：理解 · [回看 6.1.2](chapters/06-segmentation/index.md#612)
    { .quiz-meta }

<div class="quiz" data-answer="C" markdown>

**16.** 创建 `cv2.VideoWriter` 时，第 4 个参数应写成（　　）。

- A. `frame.shape`
- B. `(高, 宽)`
- C. `(宽, 高)`
- D. `(高, 宽, 3)`

</div>

??? tip "答案与解析"
    **答案：C**

    `VideoWriter` 的尺寸是 `(宽, 高)`，和 `frame.shape` 的 `(高, 宽, 3)` 顺序相反。写错会得到打不开的视频。

    考查：写视频 · 认知层次：记忆 · [回看 7.2.2](chapters/07-video/index.md#722)
    { .quiz-meta }

<div class="quiz" data-answer="C" markdown>

**17.** 扩散模型训练时，模型要学会的是（　　）。

- A. 给图片分类
- B. 找出图中的物体
- C. 看一张带噪声的图，猜出加进去的噪声
- D. 把图片放大 4 倍

</div>

??? tip "答案与解析"
    **答案：C**

    训练时给照片加上某一步的噪声，让模型猜噪声；生成时用学到的本领从纯噪声一步步去噪。

    考查：扩散模型原理 · 认知层次：理解 · [回看 8.2.1](chapters/08-generative/index.md#821)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**18.** 用 `cv2.getPerspectiveTransform` 计算单应性矩阵，至少需要（　　）对对应点。

- A. 2
- B. 4
- C. 8
- D. 100

</div>

??? tip "答案与解析"
    **答案：B**

    单应性矩阵由四对对应点决定，`getPerspectiveTransform` 正好接收两组各四个点。标记码的四个角正好提供四对点。

    考查：单应性矩阵 · 认知层次：记忆 · [回看 9.2.3](chapters/09-applications/index.md#923)
    { .quiz-meta }

<div class="quiz" data-answer="A" markdown>

**19.** 非极大值抑制（NMS）的作用是（　　）。

- A. 去掉同一个物体上重复的框
- B. 提高图片亮度
- C. 把框放大一圈
- D. 增加训练数据

</div>

??? tip "答案与解析"
    **答案：A**

    NMS 保留置信度最高的框，删掉与它交并比过大的其他框，避免一辆车被数成好几辆。

    考查：非极大值抑制 · 认知层次：记忆 · [回看 5.2.2](chapters/05-detection/index.md#522)
    { .quiz-meta }

<div class="quiz" data-answer="A" markdown>

**20.** 一张 100×200 的图片，某人的掩膜中有 2000 个 1，这个人占画面（　　）。

- A. 10%
- B. 20%
- C. 2%
- D. 1%

</div>

??? tip "答案与解析"
    **答案：A**

    整张图 100 × 200 = 20 000 个像素，2000 ÷ 20 000 = 10%。代码中写 `mask.mean()` 就能直接得到 0.1。

    考查：掩膜面积 · 认知层次：应用 · [回看 6.2.1](chapters/06-segmentation/index.md#621)
    { .quiz-meta }

**二、多项选择题**（每题 4 分）

<div class="quiz quiz-multi" data-answer="ABD" markdown>

**1.** 下列属于计算机视觉应用的有（　　）。

- A. 停车场自动识别车牌抬杆
- B. 健身 App 数深蹲个数
- C. 手机语音助手听懂“明天天气怎么样”
- D. 相册按人物自动分组

</div>

??? tip "答案与解析"
    **答案：ABD**

    C 是语音识别和自然语言处理，不处理图片。

    考查：身边的计算机视觉 · 认知层次：理解 · [回看 1.1.2](chapters/01-intro/index.md#112)
    { .quiz-meta }

<div class="quiz quiz-multi" data-answer="ABC" markdown>

**2.** 实验 3-3 的车道线检测流程中，用到了下列哪些操作？（　　）

- A. 高斯滤波去噪
- B. Canny 边缘检测
- C. 梯形感兴趣区域
- D. 按 HSV 颜色选像素

</div>

??? tip "答案与解析"
    **答案：ABC**

    流程是灰度 → 高斯去噪 → Canny → 梯形区域 → 霍夫直线 → 按斜率分左右。按颜色选像素是第 2 章实验 2-3 的方法。

    考查：车道线检测流程 · 认知层次：记忆 · [回看 3.3.2](chapters/03-features/index.md#332)
    { .quiz-meta }

<div class="quiz quiz-multi" data-answer="ABD" markdown>

**3.** 每个检测结果框都包含的信息有（　　）。

- A. 边界框的位置
- B. 类别
- C. 物体的精确轮廓
- D. 置信度

</div>

??? tip "答案与解析"
    **答案：ABD**

    精确轮廓是第 6 章图像分割的输出，检测只给矩形框。

    考查：检测的输出 · 认知层次：记忆 · [回看 5.1.1](chapters/05-detection/index.md#511)
    { .quiz-meta }

<div class="quiz quiz-multi" data-answer="ABC" markdown>

**4.** 让视频处理达到实时的办法有（　　）。

- A. 跳帧处理
- B. 缩小图片尺寸
- C. 选更小的模型
- D. 提高视频帧率

</div>

??? tip "答案与解析"
    **答案：ABC**

    提高帧率意味着每秒要处理更多帧，更难实时。

    考查：处理速度 · 认知层次：应用 · [回看 7.2.3](chapters/07-video/index.md#723)
    { .quiz-meta }

<div class="quiz quiz-multi" data-answer="ABD" markdown>

**5.** 让检测模型跑得更快的办法有（　　）。

- A. 换成更小的 n 号模型
- B. 缩小输入尺寸
- C. 把置信度门槛调高
- D. 导出为 ONNX 等推理格式或进行量化

</div>

??? tip "答案与解析"
    **答案：ABD**

    置信度门槛只决定保留哪些框，模型的计算量不变，几乎不影响速度。

    考查：提速办法 · 认知层次：理解 · [回看 9.6.2](chapters/09-applications/index.md#962)
    { .quiz-meta }

**三、判断题**（每题 1 分）

<div class="quiz quiz-judge" data-answer="√" markdown>

**1.** 每个像素的红、绿、蓝数值都在 0～255 之间。

</div>

??? tip "答案与解析"
    **答案：√**

    每个数用 8 位（1 个字节）存，能表示 256 个数，即 0～255。

    考查：RGB · 认知层次：记忆 · [回看 1.3.2](chapters/01-intro/index.md#132)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="×" markdown>

**2.** `cv2.imread` 读取一个不存在的文件时，会立即报错提示“文件不存在”。

</div>

??? tip "答案与解析"
    **答案：×**

    `imread` 找不到文件时**不报错**，只返回 `None`，要等到后面使用这张图（如 `img.shape`、`cvtColor`）时才报错。所以读图后最好先 `print(img.shape)` 确认一下。

    考查：读图 · 认知层次：记忆 · [回看 2.1.2](chapters/02-image-processing/index.md#212)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="√" markdown>

**3.** 夜间画面整体变暗时，适当降低 Canny 的两个门槛，仍然可以找到车道线的边缘。

</div>

??? tip "答案与解析"
    **答案：√**

    画面变暗后，车道线和路面的亮度差变小，但仍比周围的变化大。编者把车道照片压暗到 35%，门槛从 (50, 150) 降到 (20, 60) 后，车道线又完整了。

    考查：边缘的抗光照能力 · 认知层次：分析 · [回看 3.2.3](chapters/03-features/index.md#323)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="×" markdown>

**4.** 分类模型遇到没见过的东西时，会回答“我不知道”。

</div>

??? tip "答案与解析"
    **答案：×**

    分类模型总是从学过的类别里挑一个“最像的”，不会说“不知道”。所以要先确认要认的东西在不在它的类别表里。

    考查：分类模型的输出 · 认知层次：理解 · [回看 4.1.3](chapters/04-classification/index.md#413)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="√" markdown>

**5.** 交并比等于 1，说明两个框完全重合。

</div>

??? tip "答案与解析"
    **答案：√**

    完全重合时交集等于并集，交并比 = 1；完全不挨着时交并比 = 0。

    考查：交并比 · 认知层次：理解 · [回看 5.2.1](chapters/05-detection/index.md#521)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="√" markdown>

**6.** 分割模型输出的掩膜和原图一样大，每个像素对应一个答案。

</div>

??? tip "答案与解析"
    **答案：√**

    实例分割加 `retina_masks=True` 时，掩膜就是原图大小；语义分割和深度估计的结果也都和原图一样大。

    考查：掩膜 · 认知层次：记忆 · [回看 6.2.1](chapters/06-segmentation/index.md#621)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="√" markdown>

**7.** 视频文件经过压缩，但用 OpenCV 读出来的每一帧都是完整的图片。

</div>

??? tip "答案与解析"
    **答案：√**

    压缩只影响文件大小；`cap.read()` 返回的 `frame` 是完整的数字表，可以像处理照片一样处理。

    考查：视频压缩 · 认知层次：理解 · [回看 7.1.1](chapters/07-video/index.md#711)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="×" markdown>

**8.** 用超分辨率把监控中模糊的车牌放大后，就可以作为认定车辆的证据。

</div>

??? tip "答案与解析"
    **答案：×**

    超分辨率补出的细节是模型猜的，可能和真实情况不同，不能当作证据。

    考查：超分辨率的局限 · 认知层次：评价 · [回看 8.5.3](chapters/08-generative/index.md#853)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="×" markdown>

**9.** 生成标记码用 `DICT_4X4_50`，检测时用 `DICT_5X5_50` 也能找到。

</div>

??? tip "答案与解析"
    **答案：×**

    生成和检测必须用同一个字典，就像用同一本密码本。实验 9-2 中换成 `DICT_5X5_50` 后找到的码是 `None`。

    考查：标记码字典 · 认知层次：应用 · [回看 实验 9-2](chapters/09-applications/index.md#9-2)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="×" markdown>

**10.** 在辅助驾驶的行人提醒功能中，应该把置信度门槛设得尽量高，宁可漏报也不能误报。

</div>

??? tip "答案与解析"
    **答案：×**

    漏掉行人可能导致事故，误报只是让司机多看一眼，所以行人提醒宜偏低门槛、保证召回率。需要谨慎的是会直接控制车辆的功能（如紧急刹车）。

    考查：门槛选择 · 认知层次：评价 · [回看 5.4.2](chapters/05-detection/index.md#542)
    { .quiz-meta }

**四、简答题**（每题 10 分）

**1.** 用自己的话说明精确率和召回率的区别，并分别举一个“更看重精确率”和“更看重召回率”的视觉应用。

??? tip "答案与解析"
    **参考答案：** 精确率看“报出来的有多少是真的”，衡量乱报；召回率看“真的找出来了多少”，衡量漏报。更看重召回率：辅助驾驶的行人提醒、安防中发现可疑人员、医学影像中找可疑病灶，漏掉的代价很大。更看重精确率：自动紧急刹车的触发、自动给违章车辆开罚单、商品推荐，误报的代价很大。

    考查：精确率与召回率 · 认知层次：理解 · [回看 5.4.2](chapters/05-detection/index.md#542)
    { .quiz-meta }

**2.** 某商场想在入口安装摄像头，用人脸识别统计“老顾客回头率”。请从法规角度分析这个方案存在的问题，并提出一个更合适的做法。

??? tip "答案与解析"
    **参考答案：**

    问题：人脸是生物识别信息，属于敏感个人信息，处理需要特定目的、充分必要并取得个人单独同意；公共场所安装人脸识别设备应当为维护公共安全所必需，统计回头率是商业目的，不符合要求；顾客也无法选择不被识别。更合适的做法：只用检测加跟踪统计客流人数，不识别身份、不保存人脸；或者通过会员卡、扫码等顾客主动参与的方式统计回头客，并明确告知。

    评分要点：指出敏感个人信息 2 分，指出公共场所和目的问题 2 分，合理替代方案 2 分。

    考查：伦理与法规 · 认知层次：评价 · [回看 9.7](chapters/09-applications/index.md#97)
    { .quiz-meta }

**五、实操题**（每题 10 分）

**1.** 修改实验 6-4 的代码：只对类别是 `person` 的目标估计距离，如果最近的行人在 15 米以内，打印“前方有行人，注意避让”，否则打印“附近没有行人”。用 `drive_city.jpg` 和 `street_crossing.jpg` 各运行一次，记录结果。

??? tip "答案与解析"
    **参考做法：**

    ```python
    people = [t for t in items if t[1] == "person"]     # 只留下行人
    if people and people[0][0] < 15:                    # items 已按距离排好，第一个最近
        print("前方有行人，注意避让，约", round(people[0][0], 1), "米")
    else:
        print("附近没有行人")
    ```

    `drive_city.jpg` 中行人约 11.2 米，会提醒。`street_crossing.jpg` 中最近的行人约 8.4 米（编者运行结果），也会提醒。注意先判断 `people` 是否为空，否则没有行人时 `people[0]` 会报 `IndexError`。

    评分要点：正确筛选行人（2 分）；判断空列表（1 分）；两张照片的结果（2 分）。

    考查：深度估计与检测结合 · 认知层次：应用 · [回看 实验 6-4](chapters/06-segmentation/index.md#6-4)
    { .quiz-meta }

## 模拟卷二

**一、单项选择题**（每题 2 分）

<div class="quiz" data-answer="D" markdown>

**1.** 关于灰度图，下列说法正确的是（　　）。

- A. 灰度图的每个像素有 3 个数
- B. 灰度值越大，像素越暗
- C. 彩色转灰度就是把红、绿、蓝三个数平均
- D. 找边缘、找车道线这类只关心亮暗的任务，常先把图片转成灰度图

</div>

??? tip "答案与解析"
    **答案：D**

    灰度图只有一个通道（A 错）；0 是黑、255 是白，数越大越亮（B 错）；转灰度按人眼感觉加权，绿色权重最大（C 错）。

    考查：灰度图 · 认知层次：理解 · [回看 1.3.3](chapters/01-intro/index.md#133)
    { .quiz-meta }

<div class="quiz" data-answer="A" markdown>

**2.** 用 HSV 找白色车道线，最合适的条件是（　　）。

- A. 饱和度 S 很低，亮度 V 很高
- B. 色调 H 在 20～35 之间
- C. 饱和度 S 很高，亮度 V 很低
- D. 色调 H 等于 0

</div>

??? tip "答案与解析"
    **答案：A**

    白色的红绿蓝三个数差不多，所以不鲜艳（S 低）而且很亮（V 高），色调没有意义。B 是黄色的条件；C 是深色鲜艳的颜色；D 是红色。

    考查：HSV 选颜色 · 认知层次：应用 · [回看 2.3.2](chapters/02-image-processing/index.md#232)
    { .quiz-meta }

<div class="quiz" data-answer="D" markdown>

**3.** 霍夫变换找到一条线段，端点是 (200, 500) 和 (400, 300)（图片坐标，y 轴向下），按实验 3-3 的规则它是（　　）。

- A. 右车道线
- B. 太平的线，丢掉
- C. 竖直的线，丢掉
- D. 左车道线

</div>

??? tip "答案与解析"
    **答案：D**

    斜率 = (300 − 500) ÷ (400 − 200) = −1，小于 −0.5，是左车道线（在画面中从左下往右上斜）。

    考查：按斜率分左右 · 认知层次：应用 · [回看 3.3.2](chapters/03-features/index.md#332)
    { .quiz-meta }

<div class="quiz" data-answer="D" markdown>

**4.** 一张 224×224×3 的图片经过一个有 32 个卷积核、步长为 2 的卷积层，输出的形状是（　　）。

- A. 224×224×32
- B. 112×112×3
- C. 224×224×3
- D. 112×112×32

</div>

??? tip "答案与解析"
    **答案：D**

    步长 2 让宽高减半：224 ÷ 2 = 112；通道数等于卷积核个数 32。

    考查：特征图的形状 · 认知层次：应用 · [回看 4.2.2](chapters/04-classification/index.md#422)
    { .quiz-meta }

<div class="quiz" data-answer="D" markdown>

**5.** 辅助驾驶中多采用 YOLO 这类一阶段检测器，主要原因是（　　）。

- A. 一阶段检测器不需要训练数据
- B. 一阶段检测器只能检测车辆
- C. 两阶段检测器不能输出边界框
- D. 一阶段检测器速度快，能满足实时要求

</div>

??? tip "答案与解析"
    **答案：D**

    一阶段检测器看一遍图就输出所有框，速度快。车以 60 千米/时行驶每秒前进约 16.7 米，检测必须足够快。

    考查：一阶段与两阶段 · 认知层次：理解 · [回看 5.3.1](chapters/05-detection/index.md#531)
    { .quiz-meta }

<div class="quiz" data-answer="D" markdown>

**6.** 换背景公式“新图 = 原图 × 掩膜 + 新背景 × (1 − 掩膜)”中，某个边缘像素的掩膜值是 0.3，则新图这个像素（　　）。

- A. 完全等于原图
- B. 完全等于新背景
- C. 原图占 70%，新背景占 30%
- D. 原图占 30%，新背景占 70%

</div>

??? tip "答案与解析"
    **答案：D**

    原图乘 0.3，新背景乘 1 − 0.3 = 0.7。羽化后的边缘像素就是这样按比例混合的。

    考查：掩膜换背景与羽化 · 认知层次：应用 · [回看 6.2.2](chapters/06-segmentation/index.md#622)
    { .quiz-meta }

<div class="quiz" data-answer="D" markdown>

**7.** 目标跟踪和目标检测相比，多给出了（　　）。

- A. 框的位置
- B. 类别
- C. 置信度
- D. 跨帧不变的号码牌（ID）

</div>

??? tip "答案与解析"
    **答案：D**

    检测每一帧只给框、类别和置信度；跟踪在此基础上给每个目标一个跨帧保持的号码牌。

    考查：跟踪的作用 · 认知层次：理解 · [回看 7.3.1](chapters/07-video/index.md#731)
    { .quiz-meta }

<div class="quiz" data-answer="D" markdown>

**8.** 引导强度设得过高，最可能出现的情况是（　　）。

- A. 画面完全不听提示词
- B. 生成速度变快
- C. 图片尺寸变小
- D. 颜色过饱和、画面生硬

</div>

??? tip "答案与解析"
    **答案：D**

    引导强度表示多听提示词的话。太低容易跑题，太高则颜色过饱和、生硬，一般用 7～8。

    考查：引导强度 · 认知层次：理解 · [回看 8.3.1](chapters/08-generative/index.md#831)
    { .quiz-meta }

<div class="quiz" data-answer="A" markdown>

**9.** 下面关于 `gr.Interface(fn=analyze, inputs=[图片, 滑块], outputs=[图片, 文本框])` 的说法，正确的是（　　）。

- A. `analyze` 应该有两个参数，返回两个值
- B. `analyze` 应该有一个参数，返回四个值
- C. `analyze` 后面必须加括号写成 `analyze()`
- D. 上传的图片交给 `analyze` 时是 BGR 顺序

</div>

??? tip "答案与解析"
    **答案：A**

    `inputs` 有几个，函数就有几个参数；`outputs` 有几个，函数就返回几个值。`fn=analyze` 是把函数本身交给 Gradio，不加括号。`gr.Image(type="numpy")` 给的是 RGB。

    考查：Gradio 用法 · 认知层次：应用 · [回看 9.5.1](chapters/09-applications/index.md#951)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**10.** 实验 1-3 中，分类模型把“行人过马路”的照片认成了“泳帽”，最主要的原因是（　　）。

- A. 模型太小，换大模型就能认对
- B. 分类模型只会给整张照片一个答案，不适合内容很多的街景
- C. 照片分辨率太低
- D. 模型没有联网

</div>

??? tip "答案与解析"
    **答案：B**

    分类模型学的是“一张照片一样主要东西”，面对满是行人、车辆的街景，只能硬挑一个最像的类别。这是任务选错了，换成检测模型就能正确找出 12 个人。

    考查：任务的选择 · 认知层次：分析 · [回看 1.2.1](chapters/01-intro/index.md#121)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**11.** 一张图片的直方图几乎全部挤在左边（亮度 0～50），说明这张图（　　）。

- A. 过曝，太亮
- B. 整体偏暗
- C. 对比度很高
- D. 颜色很鲜艳

</div>

??? tip "答案与解析"
    **答案：B**

    直方图的横轴是亮度，从左（0，黑）到右（255，白）。柱子挤在左边，说明大部分像素都很暗，典型场景是夜间画面。

    考查：直方图 · 认知层次：理解 · [回看 2.4.2](chapters/02-image-processing/index.md#242)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**12.** 下面的 3×3 灰度小块与卷积核做卷积，中间位置的输出是（　　）。

小块：第一行 10 10 10，第二行 10 10 10，第三行 50 50 50；卷积核：第一行 −1 −2 −1，第二行 0 0 0，第三行 1 2 1。

- A. 0
- B. 160
- C. −160
- D. 40

</div>

??? tip "答案与解析"
    **答案：B**

    上一行：10×(−1) + 10×(−2) + 10×(−1) = −40；中间一行全乘 0；下一行：50×1 + 50×2 + 50×1 = 200。合计 −40 + 200 = 160。这是水平边缘核，下面比上面亮，输出是大正数。

    考查：卷积计算 · 认知层次：应用 · [回看 3.4.1](chapters/03-features/index.md#341)
    { .quiz-meta }

<div class="quiz" data-answer="C" markdown>

**13.** 下列做法中，属于迁移学习的是（　　）。

- A. 用随机参数的模型从零开始训练
- B. 只用预训练模型直接识别，不做任何训练
- C. 从 ImageNet 预训练模型出发，换掉分类层，用自己的五类数据继续训练
- D. 把训练集复制一份当验证集

</div>

??? tip "答案与解析"
    **答案：C**

    迁移学习是把预训练模型学到的“本事”迁移到新任务上，再用少量新数据训练。A 是从零训练；B 没有训练；D 是错误做法。

    考查：迁移学习 · 认知层次：理解 · [回看 4.4.1](chapters/04-classification/index.md#441)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**14.** 把检测的置信度门槛从 0.25 调到 0.6，通常会（　　）。

- A. 框变多，误检增加
- B. 框变少，漏检增加
- C. 框的位置变得更准
- D. 模型需要重新训练

</div>

??? tip "答案与解析"
    **答案：B**

    门槛提高，只留下更有把握的框，误检减少，但一些真实物体（远处的、被挡住的）因置信度不够被漏掉。门槛不影响框的位置，也不需要重新训练。

    考查：置信度门槛 · 认知层次：理解 · [回看 5.4.1](chapters/05-detection/index.md#541)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**15.** U-Net 中“跳跃连接”的作用是（　　）。

- A. 让模型跑得更快
- B. 把压缩时丢掉的细节直接送给解码层，使边缘更准
- C. 跳过不重要的图片
- D. 减少训练数据

</div>

??? tip "答案与解析"
    **答案：B**

    编码器把图片压小时会丢掉边缘细节，跳跃连接把对应大小的特征直接传给解码器，所以 U-Net 描边很准。

    考查：U-Net 结构 · 认知层次：理解 · [回看 6.3.1](chapters/06-segmentation/index.md#631)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**16.** 一辆车在桥下被挡住 40 帧后重新出现，要让它保持原来的号码牌，跟踪器“丢失后记住”的帧数应该（　　）。

- A. 设为 0
- B. 大于 40
- C. 小于 10
- D. 和帧率相等

</div>

??? tip "答案与解析"
    **答案：B**

    记住的时间比遮挡时间长，车重新出现时号码牌还在，才能配上。“跟踪号码牌”动画中，最慢的车穿过桥约 32 帧，记住 20 帧会换号，45 帧就不会。

    考查：遮挡与 ID 切换 · 认知层次：应用 · [回看 7.3.2](chapters/07-video/index.md#732)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**17.** Stable Diffusion 在“潜空间”里做扩散，主要好处是（　　）。

- A. 生成的图更大
- B. 计算量小得多，普通显卡也能跑
- C. 不需要提示词
- D. 不需要随机种子

</div>

??? tip "答案与解析"
    **答案：B**

    512×512 的图压成 64×64 的潜空间表示再扩散，计算量小了几十倍。

    考查：潜空间 · 认知层次：理解 · [回看 8.2.3](chapters/08-generative/index.md#823)
    { .quiz-meta }

<div class="quiz" data-answer="C" markdown>

**18.** 一个程序处理一张图要 250 毫秒，它每秒能处理（　　）张。

- A. 0.25
- B. 2.5
- C. 4
- D. 25

</div>

??? tip "答案与解析"
    **答案：C**

    每秒张数 = 1000 ÷ 每张毫秒数 = 1000 ÷ 250 = 4。

    考查：速度换算 · 认知层次：应用 · [回看 9.6.1](chapters/09-applications/index.md#961)
    { .quiz-meta }

<div class="quiz" data-answer="C" markdown>

**19.** 判断行人是否进入危险区域，通常用框的哪个点？（　　）

- A. 左上角
- B. 中心
- C. 底边中点（脚下）
- D. 右上角

</div>

??? tip "答案与解析"
    **答案：C**

    人站在地面上，看他走进了哪块地面要看脚的位置。框的中心在腰部，人到区域边缘时容易误判。

    考查：区域闯入 · 认知层次：理解 · [回看 7.4.1](chapters/07-video/index.md#741)
    { .quiz-meta }

<div class="quiz" data-answer="C" markdown>

**20.** 实验 8-1 中，超分辨率的清晰度远高于双三次，平均误差却更大，原因是（　　）。

- A. 超分辨率程序出错了
- B. 清晰度的算法不对
- C. 超分辨率补出的细节是模型猜的，和原图并不一致
- D. 双三次插值使用了原图

</div>

??? tip "答案与解析"
    **答案：C**

    超分辨率让边缘锐利、细节丰富，但这些细节来自模型的经验，和原图对不上，所以误差反而更大。

    考查：清楚不等于真实 · 认知层次：分析 · [回看 8.5.3](chapters/08-generative/index.md#853)
    { .quiz-meta }

**二、多项选择题**（每题 4 分）

<div class="quiz quiz-multi" data-answer="ACD" markdown>

**1.** 找车道线之前先裁出画面下半部分（感兴趣区域），好处有（　　）。

- A. 排除天空、广告牌等干扰
- B. 让车道线的颜色更鲜艳
- C. 要处理的像素少了，速度更快
- D. 车道线只出现在路面上，不会漏掉

</div>

??? tip "答案与解析"
    **答案：ACD**

    裁剪只改变处理的范围，不改变像素的颜色，B 错误。感兴趣区域的两个好处是排除干扰和加快速度；因为车道线只在路面上，所以裁掉上半部分不会漏掉它。

    考查：感兴趣区域 · 认知层次：理解 · [回看 2.2.4](chapters/02-image-processing/index.md#224)
    { .quiz-meta }

<div class="quiz quiz-multi" data-answer="AC" markdown>

**2.** 把训练参数 `imgsz` 从 128 改成 224，可能出现的变化有（　　）。

- A. 训练变慢
- B. 类别数变多
- C. 准确率可能提高
- D. 数据集的图片数量增加

</div>

??? tip "答案与解析"
    **答案：AC**

    图片放大后细节更多，准确率可能提高（编者实测 81.4% → 83.9%），但计算量变大，训练变慢（约 66 秒 → 146 秒）。类别数和图片数量都不变。

    考查：训练参数 · 认知层次：分析 · [回看 4.6.1](chapters/04-classification/index.md#461)
    { .quiz-meta }

<div class="quiz quiz-multi" data-answer="AC" markdown>

**3.** 关于全景分割，正确的有（　　）。

- A. 每个像素都有类别
- B. 只分割人和车，路面、天空不管
- C. 人、车等物体还能区分是第几个
- D. 就是语义分割的另一个名字

</div>

??? tip "答案与解析"
    **答案：AC**

    全景分割 = 语义分割（每个像素有类别）+ 实例分割（物体分得清第几个）。B 说的是实例分割。

    考查：全景分割 · 认知层次：理解 · [回看 6.1.2](chapters/06-segmentation/index.md#612)
    { .quiz-meta }

<div class="quiz quiz-multi" data-answer="ABD" markdown>

**4.** 做参数对比实验时，正确的做法有（　　）。

- A. 固定随机种子
- B. 一次只改一个参数
- C. 每次同时改提示词和步数，节省时间
- D. 记录每张图的全部参数

</div>

??? tip "答案与解析"
    **答案：ABD**

    同时改两个参数，就分不清变化是哪个参数引起的。这是“控制变量”的基本要求。

    考查：控制变量 · 认知层次：应用 · [回看 8.3.2](chapters/08-generative/index.md#832)
    { .quiz-meta }

<div class="quiz quiz-multi" data-answer="ABC" markdown>

**5.** 下列信息中，属于敏感个人信息的有（　　）。

- A. 清楚的人脸照片
- B. 一个人连续多日的行踪轨迹
- C. 银行卡账户信息
- D. 一段只有路面、没有人和车的行车视频

</div>

??? tip "答案与解析"
    **答案：ABC**

    生物识别、行踪轨迹、金融账户都属于敏感个人信息。只有路面的视频不能识别特定的人。

    考查：敏感个人信息 · 认知层次：理解 · [回看 9.7.1](chapters/09-applications/index.md#971)
    { .quiz-meta }

**三、判断题**（每题 1 分）

<div class="quiz quiz-judge" data-answer="×" markdown>

**1.** 市面上的 2 级辅助驾驶已经可以让驾驶员在高速公路上放开方向盘看手机。

</div>

??? tip "答案与解析"
    **答案：×**

    2 级是组合驾驶辅助，驾驶员仍是开车的人，必须保持注意力、随时控制车辆，对安全负全责。

    考查：驾驶自动化分级 · 认知层次：评价 · [回看 1.5.1](chapters/01-intro/index.md#151)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="×" markdown>

**2.** 用颜色找车道线的方法，白天和夜间用同一组 HSV 门槛效果一样好。

</div>

??? tip "答案与解析"
    **答案：×**

    实验 2-3 中，画面压暗后同样的门槛一个车道线像素也找不到，因为车道线的亮度 V 掉到了门槛以下。颜色方法对光照很敏感。

    考查：颜色方法的局限 · 认知层次：分析 · [回看实验 2-3](chapters/02-image-processing/index.md#2-3)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="×" markdown>

**3.** 模板匹配可以找出画面中任意大小、任意角度的同类物体。

</div>

??? tip "答案与解析"
    **答案：×**

    模板匹配只能找“长得一模一样”的东西，物体变大变小、转角度、换光照就不灵了。

    考查：模板匹配 · 认知层次：理解 · [回看 3.5.2](chapters/03-features/index.md#352)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="×" markdown>

**4.** 训练结束后保存的 `best.pt` 一定是最后一轮的模型。

</div>

??? tip "答案与解析"
    **答案：×**

    `best.pt` 是验证准确率最高的那一轮，`last.pt` 才是最后一轮。实验 4-3 中第 9 轮最高（81.4%），第 10 轮是 79.4%。

    考查：训练结果 · 认知层次：记忆 · [回看 4.6.2](chapters/04-classification/index.md#462)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="×" markdown>

**5.** 在 COCO 上 mAP 更高的模型，在 KITTI 小样本上的 mAP 也一定更高。

</div>

??? tip "答案与解析"
    **答案：×**

    指标只在同一个数据集上可比。数据集的类别、场景、难度不同，排名可能不同，要在自己的验证集上实际测。

    考查：评估指标 · 认知层次：评价 · [回看 5.4.3](chapters/05-detection/index.md#543)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="√" markdown>

**6.** 先用 YOLO 检测出框，再把框交给 SAM，可以同时得到物体的类别和精确轮廓。

</div>

??? tip "答案与解析"
    **答案：√**

    类别来自 YOLO，轮廓来自 SAM。这也是很多标注工具“AI 辅助标注”的做法。

    考查：检测 + SAM · 认知层次：理解 · [回看 6.4.2](chapters/06-segmentation/index.md#642)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="×" markdown>

**7.** 框的面积在 1 秒内变大了 3 倍，一定说明这辆车在快速靠近。

</div>

??? tip "答案与解析"
    **答案：×**

    车刚从画面边缘进入时，框被画面切掉一部分，面积会“暴涨”（实验 7-2 中黑车 ×3.76）。贴着画面边缘的框不能直接用来判断远近。

    考查：变近变远的判断 · 认知层次：分析 · [回看 7.4.2](chapters/07-video/index.md#742)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="×" markdown>

**8.** 图生图的 strength 越大，生成的图越像原图。

</div>

??? tip "答案与解析"
    **答案：×**

    strength 越大，加的噪声越多，改动越大，越不像原图。

    考查：图生图 · 认知层次：理解 · [回看 8.3.3](chapters/08-generative/index.md#833)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="×" markdown>

**9.** 用 `demo.launch(share=True)` 生成的公开链接只有自己能打开，所以不用考虑别人上传照片里的个人信息。

</div>

??? tip "答案与解析"
    **答案：×**

    `share=True` 生成的链接任何拿到的人都能打开。别人上传的照片可能含有人脸、车牌，如果程序保存了它们，就是在收集他人的个人信息。

    考查：网页发布与个人信息 · 认知层次：评价 · [回看 9.5.2](chapters/09-applications/index.md#952)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="√" markdown>

**10.** 被身体挡住的关节，姿态估计给出的关键点可能不可靠。

</div>

??? tip "答案与解析"
    **答案：√**

    实验 7-3 中左臂被挡住，肘角最小只到 92 度，结果一个都没数出来；换成对着镜头的右臂就数对了。

    考查：关键点的可靠性 · 认知层次：理解 · [回看 实验 7-3](chapters/07-video/index.md#7-3)
    { .quiz-meta }

**四、简答题**（每题 10 分）

**1.** 用自己的话说明跟踪器的“预测、配对、记住”三件事，并说明为什么遮挡会导致 ID 切换。

??? tip "答案与解析"
    **参考答案：**

    预测：根据目标过去的运动推算它这一帧的位置；配对：把预测位置和这一帧的检测框按交并比配对，配上的继续用原号码；记住：没配上框的号码牌暂时保留几帧，等目标重新出现。遮挡时检测器看不见目标，如果遮挡时间超过“记住”的时间，号码牌被删除，目标重新出现时就被当成新目标，发一个新号码，造成 ID 切换。

    评分要点：三件事各 1 分；遮挡导致换号的原因 2 分。

    考查：跟踪原理 · 认知层次：理解 · [回看 7.3.2](chapters/07-video/index.md#732)
    { .quiz-meta }

**2.** 用自己的话说明增强现实把一张导航箭头“贴”到路面上的三个步骤，并说明为什么不能只把箭头缩放后贴上去。

??? tip "答案与解析"
    **参考答案：**

    三个步骤：① 在画面中找到标记码（或路面平面），得到它的四个角在照片里的坐标；② 用箭头图上对应的四个点和照片上的四个角，算出单应性矩阵 H；③ 用 H 把箭头图变形（`warpPerspective`），叠加到照片上。只缩放、平移不能表现“近大远小”的透视，箭头看起来像立在路上，而不是躺在路面上。

    评分要点：三个步骤各 1.5 分，透视的解释 1.5 分。

    考查：增强现实原理 · 认知层次：理解 · [回看 9.2](chapters/09-applications/index.md#92)
    { .quiz-meta }

**五、实操题**（每题 10 分）

**1.** 修改实验 3-1 的代码：只统计面积小于 2000 像素的“小药片”有几颗，并把它们的外接矩形画成红色、其余画成绿色。

??? tip "答案与解析"
    **参考代码：**

    ```python
    small = 0
    for c in pills:
        x, y, w, h = cv2.boundingRect(c)
        if cv2.contourArea(c) < 2000:
            small += 1
            color = (0, 0, 255)                  # 红色（蓝, 绿, 红）
        else:
            color = (0, 255, 0)                  # 绿色
        cv2.rectangle(show, (x, y), (x + w, y + h), color, 2)
    print("小药片：", small, "颗")               # 面积 1438、1706、1708 三颗
    ```

    从实验 3-1 输出的面积列表可以直接数出：小于 2000 的有 1438、1706、1708 三个。

    考查：轮廓面积与 if 判断 · 认知层次：应用 · [回看 3.3.3](chapters/03-features/index.md#333)
    { .quiz-meta }
