---
title: 附录 C Cisco 与华为命令对照
description: 实验所需的软硬件、安装步骤、云端 Notebook 用法、模型下载、数据集来源与许可、需要 GPU 或待实测的实验清单，以及学时安排建议
---

# 附录 C Cisco 与华为命令对照

## C.1 软硬件要求 { #c1 }

本书 36 个实验中，除第 8 章的 Stable Diffusion（实验 8-3、8-4）外，都能在普通电脑的 CPU 上完成。编者的编写环境是 4 核 CPU、没有显卡，书中所有“运行结果”都在这个环境中实际运行得到。

| 项目 | 最低 | 建议 |
|---|---|---|
| 操作系统 | Windows 10、macOS 12、Ubuntu 20.04 及以上 | — |
| 内存 | 8 GB | 16 GB |
| 硬盘 | 5 GB 空闲（Python、PyTorch、模型和数据） | 10 GB |
| 显卡 | 不需要 | 第 8 章生成实验需要 NVIDIA 显卡，显存 4 GB 以上（或用云端 GPU） |
| 网络 | 第一次运行时下载模型 | — |

做实验有两种方式（见 [1.6.1 节](../chapters/01-intro/index.md#161)）：

| 方式 | 适合 | 说明 |
|---|---|---|
| 云端 Notebook（推荐） | 大部分实验，尤其是第 8 章 | 魔搭社区（ModelScope）、飞桨 AI Studio 等平台提供浏览器里的 Notebook，有的送免费 GPU 时长。把 `labs` 文件夹打包上传即可 |
| 本机 | 全部 CPU 实验；第 9 章网页实验最方便 | 按 C.2 安装 |
| 课堂演示 | 第 8 章生成实验 | 教师在学校 A40 服务器上演示 |

## C.2 在本机安装 { #c2 }

1. **安装 Python 3.12**：从 python.org 或国内镜像下载安装包。Windows 安装时**勾选“Add Python to PATH”**。
2. **下载配套资源**：从课程网站或仓库下载整个 `labs` 文件夹。
3. **安装工具库**：打开命令行，进入 `labs` 文件夹，运行

    ```bash
    pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
    ```

    `-i` 后面是清华大学镜像，下载更快。PyTorch 比较大（几百 MB），请耐心等待。没有 NVIDIA 显卡的电脑可以先单独装 CPU 版 PyTorch，体积小得多：

    ```bash
    pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
    ```

4. **自检**：进入 `labs/ch01`，运行 `python lab1_4_check_env.py`（实验 1-4），每一项都显示“已安装”即可。
5. **打开 Notebook**：在 `labs` 文件夹里运行 `jupyter lab`（需要先 `pip install jupyterlab`），或用 VS Code 打开 `.ipynb` 文件。

编者实测通过的版本（`labs/requirements.txt`）：

| 库 | 版本 | 用于 |
|---|---|---|
| Python | 3.12.3 | — |
| opencv-python | 5.0.0 | 全书 |
| numpy | 2.5.4 | 全书 |
| matplotlib | 3.11.2 | 显示图片、画曲线 |
| ultralytics | 8.4.194 | 第 1、3～7、9 章 |
| torch / torchvision | 2.15.0 / 0.29.2 | Ultralytics 和超分辨率模型的底层 |
| lap | 0.5.13 | 目标跟踪（第 7 章） |
| gradio | 6.31.0 | 网页（第 9 章） |
| pillow | 12.3.0 | PIL 图片（第 8 章） |
| diffusers、transformers、accelerate | 编者未实测 | 图像生成（实验 8-3、8-4，GPU 环境） |

!!! note "OpenCV 4 和 OpenCV 5 的两处不同"
    本书按 OpenCV 5 编写。如果你的电脑上是 OpenCV 4.x，绝大部分代码一样能运行，只有两处不同：① `cv2.HoughLinesP` 返回值的形状不同，书中统一写 `lines.reshape(-1, 4)`，两个版本都适用；② OpenCV 5 去掉了 Haar 级联人脸检测（`cv2.CascadeClassifier`），本书只在 3.5.3 节讲它的原理，实验不用它。

## C.3 模型下载 { #c3 }

Ultralytics 的模型第一次使用时会从 GitHub 自动下载，放在运行代码的文件夹里，下次直接使用。

| 模型文件 | 大小 | 用于 |
|---|---|---|
| `yolo26n.pt` | 5.5 MB | 检测（第 1、3、5、7、9 章） |
| `yolo26n-cls.pt` | 5.8 MB | 分类（第 1、4 章） |
| `yolo26n-seg.pt` | 6.7 MB | 实例分割（第 1、6 章） |
| `yolo26n-pose.pt` | 7.9 MB | 姿态估计（第 1、7 章） |
| `yolo26n-sem.pt` | 3.5 MB | 道路语义分割（第 6、9 章） |
| `yolo26n-depth.pt` | 13.0 MB | 深度估计（第 6、9 章） |
| `mobile_sam.pt` | 40.7 MB | 分割一切（第 6 章） |
| `realesr-general-x4v3.pth` | 4.9 MB | 超分辨率（第 8 章，`sr_model.py` 自动下载） |
| Stable Diffusion 1.5 | 约 4 GB | 图像生成（第 8 章，Hugging Face 或魔搭社区） |

如果下载失败（常见于访问 GitHub 不稳定的网络）：

- 换个时间重试，或请老师把模型文件拷贝给你，放进对应的 `labs/chNN/` 文件夹；
- Stable Diffusion 等 Hugging Face 上的模型，可以在命令行先执行 `export HF_ENDPOINT=https://hf-mirror.com`（Windows 用 `set HF_ENDPOINT=https://hf-mirror.com`）使用国内镜像，或从魔搭社区下载。

## C.4 数据集与素材 { #c4 }

全部数据仅用于教学，请遵守原项目的许可。仓库里已带好大部分数据（约 14 MB），只有第 5 章的 KITTI 检测小样本需要运行脚本下载生成。

| 文件 | 内容 | 来源与许可 | 用于 |
|---|---|---|---|
| `images/drive_highway.jpg`、`lane_white.jpg`、`lane_yellow.jpg` | 高速公路行车照片 | Udacity 自动驾驶课程视频截图，MIT 许可 | 第 1～3、6、9 章 |
| `images/drive_city.jpg`、`street_crossing.jpg` | 城市街道、行人过马路 | KITTI 数据集，CC BY-NC-SA 3.0（非商业） | 全书 |
| `images/drive_night.jpg` | 模拟夜间画面 | 编者把 `drive_city.jpg` 调暗、加噪声生成 | 第 2 章 |
| `images/pills.jpg` | 桌面上的白色药片 | 编者用程序绘制 | 第 3 章 |
| `images/portrait_blue.jpg` | 蓝底卡通头像 | 编者用程序绘制，不含真人 | 第 2 章 |
| `images/old_photo.jpg`、`old_photo_mask.png` | 带划痕的“老照片”和划痕遮罩 | 编者用 KITTI 照片加泛黄、划痕生成 | 第 8 章 |
| `images/marker_road.jpg` | 路面上平放的 ArUco 标记码 | 编者用 `drive_highway.jpg` 合成 | 第 9 章 |
| `videos/highway_12s.mp4`、`lane_8s.mp4` | 行车视频（剪短、缩小） | Udacity，MIT 许可 | 第 3、7 章 |
| `videos/people_2s.mp4`、`pushup_2s.mp4` | 行人、俯卧撑视频 | Ultralytics 示例视频（AGPL-3.0） | 第 7 章 |
| `videos/pushup_5reps.mp4` | 连续 5 个俯卧撑 | 编者把 `pushup_2s.mp4` 重复拼接 | 第 7 章 |
| `road_objects/` | 车辆行人类型小图，5 类，训练 799 张、验证 199 张 | 从 KITTI 标注框裁出，CC BY-NC-SA 3.0 | 第 4 章 |
| `kitti_small/` | 道路目标检测小样本，4 类，训练 400 张、验证 100 张 | KITTI（Ultralytics 转换版），运行 `get_kitti_small.py` 生成（下载约 390 MB） | 第 5 章 |
| `kitti_sample/` | 一张 KITTI 图片和它的 YOLO 标注 | KITTI | 第 5 章 |

各文件的生成脚本：`make_images.py`（示例图片）、`make_marker_scene.py`（标记码合成图）、`make_pushup_video.py`（俯卧撑视频）、`get_kitti_small.py`（KITTI 小样本）、`get_videos.py`（完整原始视频，可选）。

!!! tip "用自己的素材"
    很多实验的第三档鼓励用自己拍的照片和视频。请只拍自己、或者征得同意的同学，不要拍陌生人的脸和车牌；用完不要上传到网上。行车途中**不要**为了做实验而操作手机。

## C.5 需要 GPU 或标为“待实测”的实验 { #c5 }

编写环境无法运行以下部分，代码已检查过语法和参数，书中标为“待实测”，用记录表代替运行结果。使用本书的老师请在课前先运行一遍。

| 实验 | 待实测的部分 | 需要什么 | 建议 |
|---|---|---|---|
| 实验 7-4 驾驶员分心提醒 | 第 3 步用自录视频测试 | 学生自己录的视频 | 第 1、2 步已实测；第 3 步结果因人而异，本来就由学生记录 |
| 实验 8-3 提示词练习 | 全部 | GPU（显存 4 GB 以上）、下载 Stable Diffusion 1.5 | 云端 Notebook 的 GPU 环境，或改用国产在线文生图平台 |
| 实验 8-4 图生图与局部重绘 | 全部 | 同上 | 线下课由教师在 A40 服务器上演示 |
| 实验 9-4 让程序跑得更快 | 第 4 步导出 ONNX 并测速 | 联网安装 onnx、onnxruntime | 第 1～3 步已实测 |

## C.6 学时安排建议 { #c6 }

全书 72 学时 = 线上理论 22 + 线下理论 14 + 线上实验 36。每章理论 4 学时、实验 4 学时（4 个实验各约 1 学时）。

| 章 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 合计 |
|---|---|---|---|---|---|---|---|---|---|---|
| 线上理论 | 3 | 3 | 3 | 3 | 2 | 2 | 2 | 2 | 2 | 22 |
| 线下理论 | 1 | 1 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 14 |
| 线上实验 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 36 |

第 5～9 章是全书的重点（检测、分割、视频、生成、综合项目），各安排 2 个线下学时，用于讲解难点、演示 GPU 实验和项目答辩。实验 9-3 综合项目建议提前两周布置，最后一次线下课进行现场演示。
