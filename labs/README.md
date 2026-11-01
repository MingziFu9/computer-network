# 实验代码

按章存放，`chNN/` 对应第 NN 章，文件名为 `labN_M_英文短名.py`（第 N 章实验 N-M），每个 `.py` 都有一个内容相同的 `.ipynb`（由 `tools/py2nb.py` 生成，单元格按 `# %%` 切分）。公共数据放在 `data/`，见 `data/README.md`。

## 安装

```bash
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

详细步骤（含 CPU 版 PyTorch、云端 Notebook 用法）见教材附录 C。

## 运行

**每个实验都要进入它所在的文件夹再运行**，例如：

```bash
cd ch05
python lab5_1_detect.py
```

代码里的数据路径写成 `../data/...`。第一次运行时会自动下载用到的模型（5～40 MB），放在当前文件夹。

| 章 | 实验 | 说明 |
|---|---|---|
| 第 1 章 | 1-1～1-4 | 1-4 是环境自检 |
| 第 2 章 | 2-1～2-4 | |
| 第 3 章 | 3-1～3-4 | `lab3_3b_lane_video.py` 是 3-3 的视频版（第三档） |
| 第 4 章 | 4-1～4-4 | 4-3 训练 10 轮约 1 分钟（4 核 CPU） |
| 第 5 章 | 5-1～5-4 | 5-3 先在 `data/` 运行 `get_kitti_small.py`；训练 20 轮约 40 分钟（CPU） |
| 第 6 章 | 6-1～6-4 | 6-3 的“分割一切”约 3 分钟 |
| 第 7 章 | 7-1～7-4 | 7-4 第 3 步需要自己录的视频 `my_drive.mp4` |
| 第 8 章 | 8-1～8-4 | 8-3、8-4 需要 GPU，待实测 |
| 第 9 章 | 9-1～9-4 | 9-1、9-3 会打开网页，按 Ctrl+C 结束；9-4 第 4 步（ONNX）待实测 |

所有“运行结果”都是编者在 4 核 CPU、无显卡的环境中实际运行得到的（Python 3.12，版本见 `requirements.txt`）。
