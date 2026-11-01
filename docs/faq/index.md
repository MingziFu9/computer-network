---
title: 常见问题
description: 按类别整理的常见问题，每个答案都链接回教材正文
---

# 常见问题

这里按类别整理了学习本课程时最常遇到的问题。点开问题查看简短的回答，想深入了解，就顺着链接回到正文对应的小节。

| 类别 | 问题数 |
|---|---|
| [课程与学习方法](#faq-1) | 6 |
| [实验环境与安装](#faq-2) | 8 |
| [图片与 OpenCV](#faq-3) | 6 |
| [模型、训练与评估](#faq-4) | 8 |
| [视频、生成与应用](#faq-5) | 6 |
| [安全、伦理与法规](#faq-6) | 5 |

## 课程与学习方法 { #faq-1 }

??? question "我完全没学过编程，能学会这门课吗？"

    能。本书按零基础编写：每个实验都给出完整代码，代码每段不超过 15 行、逐行中文注释，要改的地方标着“← 改这里”。你的任务是读懂、运行、改参数、解释结果，而不是从零写程序。第 1～4 章各有一个“Python 小课堂”，[附录 A](../appendix/a-python.md) 集中讲了全书用到的 Python 知识。

??? question "这门课和《机器学习》《人工智能开发框架技术》有什么关系？"

    本课是检测、分割、视频分析的“主讲课”，重点是**用**视觉模型解决问题。卷积神经网络的原理只讲直观（[3.6 节](../chapters/03-features/index.md#36)），更深入的内容在《机器学习》；PyTorch 等框架的用法在《人工智能开发框架技术》。

??? question "实验分三档，我都要做吗？"

    第一档“跑通”和第二档“改一改”是必做的，一般 45 分钟内能完成；第三档“挑战”是选做的，做了可以加分。★ 实验是必做实验，☆ 实验是选做实验。详见[附录 E](../appendix/e-project.md)。

??? question "书上标着“待实测”的实验是什么意思？"

    这些部分需要 GPU 或特殊的网络条件，编者的编写环境无法运行，所以没有给出运行结果，而是附了记录表，请你运行后自己填写。清单见[附录 C.5](../appendix/c-environment.md#c5)。

??? question "期末考试考什么？可以带书吗？"

    期末是开卷考试，题型有单选、多选、判断、简答和实操，侧重看代码说意思、填参数、看检测结果和指标回答问题、按要求改代码。可以先做[在线模拟卷](../mock-exam.md)熟悉题型。

??? question "怎样用学习图谱复习？"

    [学习图谱](../learning-graph/index.md)把全书 137 个概念和它们的先修关系画在一张图上。点一个概念，橙色的是要先掌握的概念，蓝色的是以它为基础的后续概念。期末复习时，从第 9 章的概念出发顺着箭头往回梳理，就能把全书串起来。

## 实验环境与安装 { #faq-2 }

??? question "没有显卡能做实验吗？"

    能。除第 8 章的 Stable Diffusion（实验 8-3、8-4）外，全部实验都能在普通电脑的 CPU 上完成，编者就是在没有显卡的 4 核 CPU 上运行的。最慢的是实验 5-3 训练检测器，约 40 分钟。详见[附录 C.1](../appendix/c-environment.md#c1)。

??? question "用云端 Notebook 还是在自己电脑上装？"

    推荐先用云端 Notebook（魔搭社区、飞桨 AI Studio 等），打开就能用，不用安装。第 9 章做网页时在本机运行更方便。两种方式的比较见 [1.6.1 节](../chapters/01-intro/index.md#161)，本机安装步骤见[附录 C.2](../appendix/c-environment.md#c2)。

??? question "pip install 很慢或者失败怎么办？"

    加上清华镜像：`pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple`。PyTorch 体积很大，没有显卡的电脑可以先装 CPU 版，见[附录 C.2](../appendix/c-environment.md#c2)。

??? question "第一次运行时卡在下载模型，或者下载失败？"

    Ultralytics 的模型第一次使用时从 GitHub 自动下载，每个 5～40 MB。网络不稳定时多试几次，或请老师把模型文件拷贝给你，放进运行代码的那个 `labs/chNN/` 文件夹。模型清单见[附录 C.3](../appendix/c-environment.md#c3)。

??? question "报错 FileNotFoundError，或者 cv2.imread 得到 None？"

    几乎都是路径问题：实验代码要在 `labs/chNN/` 文件夹里运行，数据路径写的是 `../data/...`（上一级的 data 文件夹）。检查当前所在的文件夹和文件名拼写。见[附录 A.10](../appendix/a-python.md#a10)。

??? question "我的电脑装的是 OpenCV 4，和书上的 OpenCV 5 有区别吗？"

    绝大部分代码一样。书中 `HoughLinesP` 的结果统一写成 `lines.reshape(-1, 4)`，两个版本都能用；Haar 级联人脸检测在 OpenCV 5 中被去掉了，本书只讲原理。见[附录 C.2](../appendix/c-environment.md#c2)。

??? question "实验跑出来的数字和书上不完全一样，正常吗？"

    正常。不同电脑、不同版本的速度、置信度、训练结果会有小的差别，照实记录即可。差别很大时，先检查图片路径和参数有没有改错。

??? question "第 9 章的网页在云端 Notebook 里打不开？"

    云端 Notebook 不能直接访问 `127.0.0.1`。把 `demo.launch()` 改成 `demo.launch(share=True)`，用终端里显示的临时公开链接打开。见[实验 9-1](../chapters/09-applications/index.md#9-1)。

## 图片与 OpenCV { #faq-3 }

??? question "为什么用 Matplotlib 显示的图片颜色怪怪的，红蓝颠倒？"

    OpenCV 读进来的图片是 BGR 顺序，Matplotlib、Gradio、PIL 都按 RGB 显示。显示前用 `cv2.cvtColor(img, cv2.COLOR_BGR2RGB)` 转一下。见 [1.3.2 节](../chapters/01-intro/index.md#132)和[附录 A.13](../appendix/a-python.md#a13)。

??? question "裁剪图片时为什么是 img[y1:y2, x1:x2]，先 y 后 x？"

    图片是一张“行 × 列”的数字表，先写行（上下，即 y），再写列（左右，即 x）。而 `cv2.resize`、`cv2.rectangle` 等函数里的坐标和大小是先 x（宽）后 y（高）。两种顺序都要记住。见 [1.3.4 节](../chapters/01-intro/index.md#134)。

??? question "两张图相减或者调亮之后，出现了奇怪的颜色？"

    图片的数字类型是 `uint8`（0～255），超出范围会“绕圈”：250 + 10 变成 4。计算前先 `astype(int)` 或 `astype(np.float32)`，算完用 `np.clip(..., 0, 255)` 限制范围再转回 `uint8`。见[附录 A.11](../appendix/a-python.md#a11)。

??? question "为什么找车道线要先转 HSV，而不是直接用 RGB？"

    在 RGB 里，同一种黄色在阴影和阳光下三个数都会变；HSV 把“什么颜色”（色调 H）和“多亮”（亮度 V）分开了，按色调找黄色、按“不鲜艳且很亮”找白色，受光照影响小得多。见第 2 章和[实验 2-3](../chapters/02-image-processing/index.md#2-3)。

??? question "Canny 的两个门槛怎么定？"

    高门槛决定哪些是“肯定的边缘”，低门槛决定哪些弱边缘能被连上。常用低:高 = 1:2 或 1:3，比如 50 和 150。可以在“Canny 双门槛”动画里拖动体会。见 [3.2.3 节](../chapters/03-features/index.md#323)。

??? question "掩膜到底是什么？"

    掩膜是一张和原图一样大的黑白图（或 True/False 数组），白色（True）表示“要处理的像素”。按颜色找车道线、抠图、修补划痕、统计路面占比，都是先得到掩膜再处理。见 [6.2 节](../chapters/06-segmentation/index.md#62)和[附录 A.12](../appendix/a-python.md#a12)。

## 模型、训练与评估 { #faq-4 }

??? question "yolo26n.pt 里的 26 和 n 是什么意思？"

    26 是版本（2026 年 1 月发布的 YOLO26），n 是大小（nano，最小最快）。还有 s、m、l、x，越大越准越慢。换成 YOLO11（`yolo11n.pt`）代码完全一样。见 [1.6.2 节](../chapters/01-intro/index.md#162)和 [5.3.3 节](../chapters/05-detection/index.md#533)。

??? question "预训练模型能直接用，为什么还要自己训练？"

    预训练模型只认识它训练时见过的类别（COCO 的 80 类），认不出“cyclist 骑车人”“安全帽”这类自己需要的类别，在特定场景下也可能不够准。用自己的数据在预训练模型基础上继续训练（迁移学习），少量数据就能有不错的效果。见 [4.5 节](../chapters/04-classification/index.md#44)和[实验 5-3](../chapters/05-detection/index.md#5-3)。

??? question "训练时 loss 越来越小，但验证集准确率不升反降，是怎么回事？"

    这是过拟合：模型把训练图片“背”下来了，换新图就不行。办法：增加数据、做数据增强、减少训练轮次、用验证集上最好的那一版（`best.pt`）。见第 4 章。

??? question "精确率和召回率哪个更重要？"

    看场合。辅助驾驶提醒行人、医疗筛查更看重召回率（宁可多报，不能漏）；报警系统误报太多会让人烦，也要兼顾精确率。调置信度门槛可以在两者之间取舍。见 [5.4 节](../chapters/05-detection/index.md#54)和 [9.1.2 节](../chapters/09-applications/index.md#912)。

??? question "mAP50 和 mAP50-95 有什么区别？"

    mAP50 只要求框和正确答案的交并比达到 0.5 就算对；mAP50-95 把交并比门槛从 0.5 到 0.95 都算一遍取平均，要求框画得更准，所以数值更低。见 [5.4.3 节](../chapters/05-detection/index.md#543)。

??? question "分割和检测我该选哪个？"

    只需要知道“有什么、在哪里、有几个”，用检测；需要精确轮廓（抠图、算面积、算路面占比），用分割。分割更慢、标注也更费工夫。见 [6.1 节](../chapters/06-segmentation/index.md#61)。

??? question "深度估计算出来的距离准吗？能用来开车吗？"

    单目深度估计是模型从一张照片“猜”出来的远近，只能作为参考，误差可能有几米。真实车辆用雷达、多个摄像头等多种传感器互相校验。本书的距离只用于学习，不能用于真实驾驶。见 [6.5 节](../chapters/06-segmentation/index.md#65)。

??? question "模型在 CPU 上太慢了，怎么办？"

    选更小的模型、缩小输入尺寸（`imgsz=320`）、跳帧处理、导出 ONNX 等推理格式。每种办法都有代价，见 [9.6 节](../chapters/09-applications/index.md#96)和[实验 9-4](../chapters/09-applications/index.md#9-4)。

## 视频、生成与应用 { #faq-5 }

??? question "跟踪时号码牌老是变，一辆车被数成好几辆？"

    这叫 ID 切换，常由遮挡和漏检引起。跟踪器“记住”目标几帧、并预测它的位置，可以减少换号。另外，同一个模型连续跟踪两段视频时号码会接着编，换视频要重新加载模型。见 [7.3 节](../chapters/07-video/index.md#73)和“跟踪号码牌”动画。

??? question "为什么动作识别不能只看一帧？"

    俯卧撑撑到一半和压到一半，单看一帧可能一模一样；“低头看一眼”和“一直低头看手机”也只能从持续时间区分。动作是一段时间里的变化，要看一串帧。见 [7.5 节](../chapters/07-video/index.md#75)。

??? question "超分辨率能把模糊的车牌变清楚吗？"

    能让它“看起来”更清楚，但细节是模型猜出来的，可能和真实的字不一样，不能当作证据。见 [8.5.3 节](../chapters/08-generative/index.md#853)。

??? question "没有显卡，第 8 章的 Stable Diffusion 实验怎么做？"

    在云端 Notebook 的 GPU 环境中运行，或者用国产在线文生图平台（通义万相、即梦、可图等）完成提示词练习。线下课由老师在 A40 服务器上演示。见第 8 章和[附录 C.5](../appendix/c-environment.md#c5)。

??? question "增强现实一定要用标记码吗？"

    不一定。标记码最简单可靠，适合入门；手机 AR 和汽车 AR-HUD 用的是无标记的方法：跟踪关键点找出平面、估计相机的移动。见 [9.2 节](../chapters/09-applications/index.md#92)。

??? question "综合项目可以自己选题吗？"

    可以，需要老师同意。自选题同样要按“需求 → 数据 → 模型 → 训练 → 评估 → 部署 → 合规检查”的流程完成，并填写合规自查表。见[实验 9-3](../chapters/09-applications/index.md#9-3)和[附录 E](../appendix/e-project.md)。

## 安全、伦理与法规 { #faq-6 }

??? question "本书的“智能辅助驾驶助手”能装到车上用吗？"

    不能。它只是学习用的示例，只做“看懂和提醒”，没有经过任何道路测试。即使是市面上的 2 级辅助驾驶，驾驶员也必须手握方向盘、眼睛看路，对行车安全负全责。见 [1.5.1 节](../chapters/01-intro/index.md#151)和 [9.1.3 节](../chapters/09-applications/index.md#913)。

??? question "我可以用路上拍的视频做实验吗？"

    行车视频会拍到路人的脸和车牌，它们属于个人信息。自己学习使用可以，但发到网上或交给别人之前要打码（实验 3-4），不要保存和传播他人的清晰人脸。行车途中不要为了拍视频而操作手机。见 [3.5.3 节](../chapters/03-features/index.md#353)和 [9.7 节](../chapters/09-applications/index.md#97)。

??? question "为什么人脸属于“敏感个人信息”？"

    人脸是生物识别信息，一旦泄露无法像密码一样更换，还可能被用来冒充身份、追踪行踪。《个人信息保护法》要求处理敏感个人信息必须有特定目的和充分必要性，并取得个人单独同意。见 [9.7.1 节](../chapters/09-applications/index.md#971)。

??? question "小区、单位只允许刷脸进门，合规吗？"

    按照 2025 年 6 月 1 日施行的《人脸识别技术应用安全管理办法》，有其他方式能达到同样目的时，不得把人脸识别作为唯一的验证方式；个人不同意刷脸的，应当提供其他合理、便捷的方式。见 [9.7.2 节](../chapters/09-applications/index.md#972)。

??? question "用 AI 生成的图片发到网上，需要注意什么？"

    按《人工智能生成合成内容标识办法》要加“AI 生成”等标识；不要用他人照片做换脸等深度合成；注意模型的使用许可。见 [8.6 节](../chapters/08-generative/index.md#86)。
