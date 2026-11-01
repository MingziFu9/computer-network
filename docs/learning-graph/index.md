---
title: 学习图谱
description: 全书核心概念及其先修关系，点一个概念就能看到学习路径
---

# 学习图谱

学习图谱把全书的核心概念和它们之间的“先修关系”画在一张图上：要理解一个概念，得先懂哪些更基础的概念；顺着箭头往回找，就是一条学习路径。

<iframe class="sim-frame" src="main.html" height="900" loading="lazy" title="学习图谱"></iframe>

[全屏打开](main.html){ target=_blank }

## 怎样使用

- **预习**：学新的一章前，点开本章的概念，看看橙色的先修概念自己是否都掌握了，没掌握的先回去复习；
- **复习**：期末复习时，从最后几章的概念出发，顺着学习路径往回梳理，就能把全书串起来；
- **查漏补缺**：做练习时遇到不懂的概念，在搜索框里输入它，看它依赖哪些更基础的概念。

<!-- graph:start -->

图谱共有 **137 个概念、184 条先修关系**，概念按章排列，颜色表示 8 个类别（基础与工具、图像处理、特征与卷积、识别任务、训练与评估、视频与三维、生成式视觉、应用与规范）。概念的定义都来自[附录 D 术语表](../appendix/glossary.md)，先修关系由编者根据各章内容整理。

## 文字版

下面按章列出每个概念的直接先修概念，便于打印或用读屏软件阅读。

??? note "第 1 章 走进视觉（18 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [计算机视觉](../appendix/glossary.md#g-计算机视觉) | 基础与工具 | — |
    | [像素](../appendix/glossary.md#g-像素) | 基础与工具 | [计算机视觉](../appendix/glossary.md#g-计算机视觉) |
    | [分辨率](../appendix/glossary.md#g-分辨率) | 基础与工具 | [像素](../appendix/glossary.md#g-像素) |
    | [RGB](../appendix/glossary.md#g-RGB) | 基础与工具 | [像素](../appendix/glossary.md#g-像素) |
    | [通道](../appendix/glossary.md#g-通道) | 基础与工具 | [RGB](../appendix/glossary.md#g-RGB) |
    | [灰度图](../appendix/glossary.md#g-灰度图) | 基础与工具 | [通道](../appendix/glossary.md#g-通道) |
    | [图像分类](../appendix/glossary.md#g-图像分类) | 识别任务 | [计算机视觉](../appendix/glossary.md#g-计算机视觉) |
    | [目标检测](../appendix/glossary.md#g-目标检测) | 识别任务 | [图像分类](../appendix/glossary.md#g-图像分类) |
    | [图像分割](../appendix/glossary.md#g-图像分割) | 识别任务 | [目标检测](../appendix/glossary.md#g-目标检测)、[像素](../appendix/glossary.md#g-像素) |
    | [目标跟踪](../appendix/glossary.md#g-目标跟踪) | 识别任务 | [目标检测](../appendix/glossary.md#g-目标检测) |
    | [图像生成](../appendix/glossary.md#g-图像生成) | 识别任务 | [计算机视觉](../appendix/glossary.md#g-计算机视觉) |
    | [姿态估计](../appendix/glossary.md#g-姿态估计) | 识别任务 | [目标检测](../appendix/glossary.md#g-目标检测) |
    | [驾驶自动化分级](../appendix/glossary.md#g-驾驶自动化分级) | 应用与规范 | [计算机视觉](../appendix/glossary.md#g-计算机视觉) |
    | [高级驾驶辅助系统](../appendix/glossary.md#g-高级驾驶辅助系统) | 应用与规范 | [驾驶自动化分级](../appendix/glossary.md#g-驾驶自动化分级) |
    | [Notebook](../appendix/glossary.md#g-Notebook) | 基础与工具 | — |
    | [OpenCV](../appendix/glossary.md#g-OpenCV) | 基础与工具 | [Notebook](../appendix/glossary.md#g-Notebook) |
    | [预训练模型](../appendix/glossary.md#g-预训练模型) | 训练与评估 | [图像分类](../appendix/glossary.md#g-图像分类) |
    | [多模态大模型](../appendix/glossary.md#g-多模态大模型) | 生成式视觉 | [预训练模型](../appendix/glossary.md#g-预训练模型) |

??? note "第 2 章 图像处理（19 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [图像处理](../appendix/glossary.md#g-图像处理) | 图像处理 | [OpenCV](../appendix/glossary.md#g-OpenCV)、[像素](../appendix/glossary.md#g-像素) |
    | [感兴趣区域](../appendix/glossary.md#g-感兴趣区域) | 图像处理 | [图像处理](../appendix/glossary.md#g-图像处理)、[分辨率](../appendix/glossary.md#g-分辨率) |
    | [插值](../appendix/glossary.md#g-插值) | 图像处理 | [分辨率](../appendix/glossary.md#g-分辨率) |
    | [颜色空间](../appendix/glossary.md#g-颜色空间) | 图像处理 | [RGB](../appendix/glossary.md#g-RGB) |
    | [HSV](../appendix/glossary.md#g-HSV) | 图像处理 | [颜色空间](../appendix/glossary.md#g-颜色空间) |
    | [掩膜](../appendix/glossary.md#g-掩膜) | 图像处理 | [HSV](../appendix/glossary.md#g-HSV)、[二值化](../appendix/glossary.md#g-二值化) |
    | [对比度](../appendix/glossary.md#g-对比度) | 图像处理 | [灰度图](../appendix/glossary.md#g-灰度图) |
    | [直方图](../appendix/glossary.md#g-直方图) | 图像处理 | [灰度图](../appendix/glossary.md#g-灰度图) |
    | [直方图均衡化](../appendix/glossary.md#g-直方图均衡化) | 图像处理 | [直方图](../appendix/glossary.md#g-直方图)、[对比度](../appendix/glossary.md#g-对比度) |
    | [噪声](../appendix/glossary.md#g-噪声) | 图像处理 | [像素](../appendix/glossary.md#g-像素) |
    | [滤波](../appendix/glossary.md#g-滤波) | 图像处理 | [噪声](../appendix/glossary.md#g-噪声) |
    | [中值滤波](../appendix/glossary.md#g-中值滤波) | 图像处理 | [滤波](../appendix/glossary.md#g-滤波) |
    | [高斯滤波](../appendix/glossary.md#g-高斯滤波) | 图像处理 | [滤波](../appendix/glossary.md#g-滤波) |
    | [阈值](../appendix/glossary.md#g-阈值) | 图像处理 | [灰度图](../appendix/glossary.md#g-灰度图) |
    | [二值化](../appendix/glossary.md#g-二值化) | 图像处理 | [阈值](../appendix/glossary.md#g-阈值) |
    | [图像预处理](../appendix/glossary.md#g-图像预处理) | 图像处理 | [图像处理](../appendix/glossary.md#g-图像处理)、[滤波](../appendix/glossary.md#g-滤波)、[插值](../appendix/glossary.md#g-插值) |
    | [函数](../appendix/glossary.md#g-函数) | 基础与工具 | [Notebook](../appendix/glossary.md#g-Notebook) |
    | [循环](../appendix/glossary.md#g-循环) | 基础与工具 | [函数](../appendix/glossary.md#g-函数) |
    | [列表](../appendix/glossary.md#g-列表) | 基础与工具 | [Notebook](../appendix/glossary.md#g-Notebook) |

??? note "第 3 章 图像特征（15 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [特征](../appendix/glossary.md#g-特征) | 特征与卷积 | [图像处理](../appendix/glossary.md#g-图像处理) |
    | [手工特征](../appendix/glossary.md#g-手工特征) | 特征与卷积 | [特征](../appendix/glossary.md#g-特征) |
    | [边缘](../appendix/glossary.md#g-边缘) | 特征与卷积 | [特征](../appendix/glossary.md#g-特征)、[灰度图](../appendix/glossary.md#g-灰度图) |
    | [边缘检测](../appendix/glossary.md#g-边缘检测) | 特征与卷积 | [边缘](../appendix/glossary.md#g-边缘)、[高斯滤波](../appendix/glossary.md#g-高斯滤波) |
    | [霍夫变换](../appendix/glossary.md#g-霍夫变换) | 特征与卷积 | [边缘检测](../appendix/glossary.md#g-边缘检测) |
    | [轮廓](../appendix/glossary.md#g-轮廓) | 特征与卷积 | [二值化](../appendix/glossary.md#g-二值化) |
    | [外接矩形](../appendix/glossary.md#g-外接矩形) | 特征与卷积 | [轮廓](../appendix/glossary.md#g-轮廓) |
    | [卷积](../appendix/glossary.md#g-卷积) | 特征与卷积 | [卷积核](../appendix/glossary.md#g-卷积核) |
    | [卷积核](../appendix/glossary.md#g-卷积核) | 特征与卷积 | [滤波](../appendix/glossary.md#g-滤波) |
    | [关键点](../appendix/glossary.md#g-关键点) | 特征与卷积 | [手工特征](../appendix/glossary.md#g-手工特征) |
    | [模板匹配](../appendix/glossary.md#g-模板匹配) | 特征与卷积 | [手工特征](../appendix/glossary.md#g-手工特征) |
    | [人脸检测](../appendix/glossary.md#g-人脸检测) | 特征与卷积 | [手工特征](../appendix/glossary.md#g-手工特征) |
    | [个人信息](../appendix/glossary.md#g-个人信息) | 应用与规范 | [人脸检测](../appendix/glossary.md#g-人脸检测) |
    | [卷积神经网络](../appendix/glossary.md#g-卷积神经网络) | 特征与卷积 | [卷积](../appendix/glossary.md#g-卷积)、[手工特征](../appendix/glossary.md#g-手工特征) |
    | [条件判断](../appendix/glossary.md#g-条件判断) | 基础与工具 | [列表](../appendix/glossary.md#g-列表) |

??? note "第 4 章 图像分类（17 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [置信度](../appendix/glossary.md#g-置信度) | 识别任务 | [图像分类](../appendix/glossary.md#g-图像分类) |
    | [准确率](../appendix/glossary.md#g-准确率) | 训练与评估 | [图像分类](../appendix/glossary.md#g-图像分类) |
    | [Top-5 准确率](../appendix/glossary.md#g-Top-5-准确率) | 训练与评估 | [准确率](../appendix/glossary.md#g-准确率)、[置信度](../appendix/glossary.md#g-置信度) |
    | [卷积层](../appendix/glossary.md#g-卷积层) | 特征与卷积 | [卷积神经网络](../appendix/glossary.md#g-卷积神经网络) |
    | [池化层](../appendix/glossary.md#g-池化层) | 特征与卷积 | [卷积层](../appendix/glossary.md#g-卷积层) |
    | [参数](../appendix/glossary.md#g-参数) | 特征与卷积 | [卷积层](../appendix/glossary.md#g-卷积层) |
    | [迁移学习](../appendix/glossary.md#g-迁移学习) | 训练与评估 | [预训练模型](../appendix/glossary.md#g-预训练模型)、[参数](../appendix/glossary.md#g-参数) |
    | [训练集](../appendix/glossary.md#g-训练集) | 训练与评估 | [图像分类](../appendix/glossary.md#g-图像分类) |
    | [验证集](../appendix/glossary.md#g-验证集) | 训练与评估 | [训练集](../appendix/glossary.md#g-训练集) |
    | [轮次](../appendix/glossary.md#g-轮次) | 训练与评估 | [训练集](../appendix/glossary.md#g-训练集) |
    | [批大小](../appendix/glossary.md#g-批大小) | 训练与评估 | [轮次](../appendix/glossary.md#g-轮次) |
    | [损失](../appendix/glossary.md#g-损失) | 训练与评估 | [参数](../appendix/glossary.md#g-参数) |
    | [欠拟合](../appendix/glossary.md#g-欠拟合) | 训练与评估 | [损失](../appendix/glossary.md#g-损失)、[验证集](../appendix/glossary.md#g-验证集) |
    | [过拟合](../appendix/glossary.md#g-过拟合) | 训练与评估 | [损失](../appendix/glossary.md#g-损失)、[验证集](../appendix/glossary.md#g-验证集) |
    | [数据增强](../appendix/glossary.md#g-数据增强) | 训练与评估 | [过拟合](../appendix/glossary.md#g-过拟合)、[图像预处理](../appendix/glossary.md#g-图像预处理) |
    | [混淆矩阵](../appendix/glossary.md#g-混淆矩阵) | 训练与评估 | [准确率](../appendix/glossary.md#g-准确率) |
    | [字典](../appendix/glossary.md#g-字典) | 基础与工具 | [列表](../appendix/glossary.md#g-列表) |

??? note "第 5 章 目标检测（14 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [边界框](../appendix/glossary.md#g-边界框) | 识别任务 | [目标检测](../appendix/glossary.md#g-目标检测)、[外接矩形](../appendix/glossary.md#g-外接矩形) |
    | [交并比](../appendix/glossary.md#g-交并比) | 训练与评估 | [边界框](../appendix/glossary.md#g-边界框) |
    | [非极大值抑制](../appendix/glossary.md#g-非极大值抑制) | 识别任务 | [交并比](../appendix/glossary.md#g-交并比)、[置信度](../appendix/glossary.md#g-置信度) |
    | [两阶段检测器](../appendix/glossary.md#g-两阶段检测器) | 识别任务 | [目标检测](../appendix/glossary.md#g-目标检测)、[卷积神经网络](../appendix/glossary.md#g-卷积神经网络) |
    | [一阶段检测器](../appendix/glossary.md#g-一阶段检测器) | 识别任务 | [两阶段检测器](../appendix/glossary.md#g-两阶段检测器) |
    | [置信度门槛](../appendix/glossary.md#g-置信度门槛) | 训练与评估 | [置信度](../appendix/glossary.md#g-置信度) |
    | [误检](../appendix/glossary.md#g-误检) | 训练与评估 | [置信度门槛](../appendix/glossary.md#g-置信度门槛) |
    | [漏检](../appendix/glossary.md#g-漏检) | 训练与评估 | [置信度门槛](../appendix/glossary.md#g-置信度门槛) |
    | [精确率](../appendix/glossary.md#g-精确率) | 训练与评估 | [误检](../appendix/glossary.md#g-误检)、[混淆矩阵](../appendix/glossary.md#g-混淆矩阵) |
    | [召回率](../appendix/glossary.md#g-召回率) | 训练与评估 | [漏检](../appendix/glossary.md#g-漏检)、[混淆矩阵](../appendix/glossary.md#g-混淆矩阵) |
    | [平均精度](../appendix/glossary.md#g-平均精度) | 训练与评估 | [精确率](../appendix/glossary.md#g-精确率)、[召回率](../appendix/glossary.md#g-召回率)、[交并比](../appendix/glossary.md#g-交并比) |
    | [数据配置文件](../appendix/glossary.md#g-数据配置文件) | 训练与评估 | [训练集](../appendix/glossary.md#g-训练集)、[验证集](../appendix/glossary.md#g-验证集) |
    | [标注工具](../appendix/glossary.md#g-标注工具) | 训练与评估 | [边界框](../appendix/glossary.md#g-边界框) |
    | [开放词汇检测](../appendix/glossary.md#g-开放词汇检测) | 识别任务 | [目标检测](../appendix/glossary.md#g-目标检测)、[多模态大模型](../appendix/glossary.md#g-多模态大模型) |

??? note "第 6 章 图像分割（14 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [语义分割](../appendix/glossary.md#g-语义分割) | 识别任务 | [图像分割](../appendix/glossary.md#g-图像分割)、[掩膜](../appendix/glossary.md#g-掩膜) |
    | [实例分割](../appendix/glossary.md#g-实例分割) | 识别任务 | [语义分割](../appendix/glossary.md#g-语义分割)、[目标检测](../appendix/glossary.md#g-目标检测) |
    | [全景分割](../appendix/glossary.md#g-全景分割) | 识别任务 | [实例分割](../appendix/glossary.md#g-实例分割) |
    | [羽化](../appendix/glossary.md#g-羽化) | 识别任务 | [掩膜](../appendix/glossary.md#g-掩膜)、[高斯滤波](../appendix/glossary.md#g-高斯滤波) |
    | [多边形标注](../appendix/glossary.md#g-多边形标注) | 训练与评估 | [标注工具](../appendix/glossary.md#g-标注工具)、[轮廓](../appendix/glossary.md#g-轮廓) |
    | [编码器-解码器](../appendix/glossary.md#g-编码器-解码器) | 识别任务 | [卷积神经网络](../appendix/glossary.md#g-卷积神经网络)、[语义分割](../appendix/glossary.md#g-语义分割) |
    | [平均交并比](../appendix/glossary.md#g-平均交并比) | 训练与评估 | [交并比](../appendix/glossary.md#g-交并比)、[语义分割](../appendix/glossary.md#g-语义分割) |
    | [分割一切模型](../appendix/glossary.md#g-分割一切模型) | 识别任务 | [实例分割](../appendix/glossary.md#g-实例分割)、[预训练模型](../appendix/glossary.md#g-预训练模型) |
    | [提示](../appendix/glossary.md#g-提示) | 识别任务 | [分割一切模型](../appendix/glossary.md#g-分割一切模型) |
    | [深度估计](../appendix/glossary.md#g-深度估计) | 视频与三维 | [像素](../appendix/glossary.md#g-像素) |
    | [深度图](../appendix/glossary.md#g-深度图) | 视频与三维 | [深度估计](../appendix/glossary.md#g-深度估计) |
    | [单目深度估计](../appendix/glossary.md#g-单目深度估计) | 视频与三维 | [深度图](../appendix/glossary.md#g-深度图) |
    | [场景重建](../appendix/glossary.md#g-场景重建) | 视频与三维 | [单目深度估计](../appendix/glossary.md#g-单目深度估计) |
    | [布尔索引](../appendix/glossary.md#g-布尔索引) | 基础与工具 | [掩膜](../appendix/glossary.md#g-掩膜)、[条件判断](../appendix/glossary.md#g-条件判断) |

??? note "第 7 章 视频分析（12 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [帧](../appendix/glossary.md#g-帧) | 视频与三维 | [像素](../appendix/glossary.md#g-像素) |
    | [帧率](../appendix/glossary.md#g-帧率) | 视频与三维 | [帧](../appendix/glossary.md#g-帧) |
    | [压缩](../appendix/glossary.md#g-压缩) | 视频与三维 | [帧](../appendix/glossary.md#g-帧) |
    | [ID](../appendix/glossary.md#g-ID) | 视频与三维 | [目标跟踪](../appendix/glossary.md#g-目标跟踪) |
    | [ID 切换](../appendix/glossary.md#g-ID-切换) | 视频与三维 | [ID](../appendix/glossary.md#g-ID) |
    | [越线计数](../appendix/glossary.md#g-越线计数) | 视频与三维 | [ID](../appendix/glossary.md#g-ID) |
    | [区域闯入](../appendix/glossary.md#g-区域闯入) | 视频与三维 | [ID](../appendix/glossary.md#g-ID)、[感兴趣区域](../appendix/glossary.md#g-感兴趣区域) |
    | [人体关键点](../appendix/glossary.md#g-人体关键点) | 视频与三维 | [姿态估计](../appendix/glossary.md#g-姿态估计)、[关键点](../appendix/glossary.md#g-关键点) |
    | [动作识别](../appendix/glossary.md#g-动作识别) | 视频与三维 | [人体关键点](../appendix/glossary.md#g-人体关键点)、[帧率](../appendix/glossary.md#g-帧率) |
    | [驾驶员监测系统](../appendix/glossary.md#g-驾驶员监测系统) | 视频与三维 | [动作识别](../appendix/glossary.md#g-动作识别)、[高级驾驶辅助系统](../appendix/glossary.md#g-高级驾驶辅助系统) |
    | [集合](../appendix/glossary.md#g-集合) | 基础与工具 | [列表](../appendix/glossary.md#g-列表) |
    | [端到端](../appendix/glossary.md#g-端到端) | 视频与三维 | [目标跟踪](../appendix/glossary.md#g-目标跟踪)、[高级驾驶辅助系统](../appendix/glossary.md#g-高级驾驶辅助系统) |

??? note "第 8 章 生成式视觉（14 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [文生图](../appendix/glossary.md#g-文生图) | 生成式视觉 | [扩散模型](../appendix/glossary.md#g-扩散模型)、[提示词](../appendix/glossary.md#g-提示词) |
    | [图生图](../appendix/glossary.md#g-图生图) | 生成式视觉 | [文生图](../appendix/glossary.md#g-文生图) |
    | [局部重绘](../appendix/glossary.md#g-局部重绘) | 生成式视觉 | [图生图](../appendix/glossary.md#g-图生图)、[掩膜](../appendix/glossary.md#g-掩膜) |
    | [图像修复](../appendix/glossary.md#g-图像修复) | 生成式视觉 | [掩膜](../appendix/glossary.md#g-掩膜) |
    | [超分辨率](../appendix/glossary.md#g-超分辨率) | 生成式视觉 | [插值](../appendix/glossary.md#g-插值)、[卷积神经网络](../appendix/glossary.md#g-卷积神经网络) |
    | [生成对抗网络](../appendix/glossary.md#g-生成对抗网络) | 生成式视觉 | [图像生成](../appendix/glossary.md#g-图像生成) |
    | [扩散模型](../appendix/glossary.md#g-扩散模型) | 生成式视觉 | [图像生成](../appendix/glossary.md#g-图像生成)、[噪声](../appendix/glossary.md#g-噪声) |
    | [潜空间](../appendix/glossary.md#g-潜空间) | 生成式视觉 | [扩散模型](../appendix/glossary.md#g-扩散模型) |
    | [提示词](../appendix/glossary.md#g-提示词) | 生成式视觉 | [多模态大模型](../appendix/glossary.md#g-多模态大模型) |
    | [反向提示词](../appendix/glossary.md#g-反向提示词) | 生成式视觉 | [提示词](../appendix/glossary.md#g-提示词) |
    | [引导强度](../appendix/glossary.md#g-引导强度) | 生成式视觉 | [提示词](../appendix/glossary.md#g-提示词)、[扩散模型](../appendix/glossary.md#g-扩散模型) |
    | [随机种子](../appendix/glossary.md#g-随机种子) | 生成式视觉 | [扩散模型](../appendix/glossary.md#g-扩散模型) |
    | [顶帽运算](../appendix/glossary.md#g-顶帽运算) | 图像处理 | [滤波](../appendix/glossary.md#g-滤波) |
    | [深度合成](../appendix/glossary.md#g-深度合成) | 应用与规范 | [图像生成](../appendix/glossary.md#g-图像生成)、[个人信息](../appendix/glossary.md#g-个人信息) |

??? note "第 9 章 应用实战（14 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [增强现实](../appendix/glossary.md#g-增强现实) | 视频与三维 | [计算机视觉](../appendix/glossary.md#g-计算机视觉) |
    | [标记码](../appendix/glossary.md#g-标记码) | 视频与三维 | [轮廓](../appendix/glossary.md#g-轮廓)、[增强现实](../appendix/glossary.md#g-增强现实) |
    | [单应性矩阵](../appendix/glossary.md#g-单应性矩阵) | 视频与三维 | [标记码](../appendix/glossary.md#g-标记码)、[插值](../appendix/glossary.md#g-插值) |
    | [多视角三维重建](../appendix/glossary.md#g-多视角三维重建) | 视频与三维 | [场景重建](../appendix/glossary.md#g-场景重建)、[关键点](../appendix/glossary.md#g-关键点) |
    | [神经辐射场](../appendix/glossary.md#g-神经辐射场) | 视频与三维 | [多视角三维重建](../appendix/glossary.md#g-多视角三维重建) |
    | [三维高斯泼溅](../appendix/glossary.md#g-三维高斯泼溅) | 视频与三维 | [神经辐射场](../appendix/glossary.md#g-神经辐射场) |
    | [鸟瞰图](../appendix/glossary.md#g-鸟瞰图) | 视频与三维 | [场景重建](../appendix/glossary.md#g-场景重建)、[单应性矩阵](../appendix/glossary.md#g-单应性矩阵) |
    | [占用网络](../appendix/glossary.md#g-占用网络) | 视频与三维 | [鸟瞰图](../appendix/glossary.md#g-鸟瞰图) |
    | [文字识别](../appendix/glossary.md#g-文字识别) | 应用与规范 | [目标检测](../appendix/glossary.md#g-目标检测) |
    | [模型部署](../appendix/glossary.md#g-模型部署) | 应用与规范 | [预训练模型](../appendix/glossary.md#g-预训练模型) |
    | [ONNX](../appendix/glossary.md#g-ONNX) | 应用与规范 | [模型部署](../appendix/glossary.md#g-模型部署) |
    | [量化](../appendix/glossary.md#g-量化) | 应用与规范 | [模型部署](../appendix/glossary.md#g-模型部署)、[参数](../appendix/glossary.md#g-参数) |
    | [敏感个人信息](../appendix/glossary.md#g-敏感个人信息) | 应用与规范 | [个人信息](../appendix/glossary.md#g-个人信息) |
    | [偏见](../appendix/glossary.md#g-偏见) | 应用与规范 | [训练集](../appendix/glossary.md#g-训练集)、[召回率](../appendix/glossary.md#g-召回率) |

<!-- graph:end -->
