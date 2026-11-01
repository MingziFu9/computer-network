# 计算机网络（网络教材）

面向成人教育人工智能技术应用专业（专科）的《计算机网络》网络教材，课程代码 816，4 学分 72 学时（线上理论 46 + 线上实验 12 + 线下理论 14），第 2 学期，期末闭卷。

网页版：<https://mingzifu9.github.io/computer-network/>

## 内容

跟着“小禾设计工作室”从 5 个人发展到 3 个部门、再开一家分店的过程，一章搭一块网络，按五层模型由下往上：

| 章 | 标题 |
|---|---|
| 1 | 认识计算机网络 |
| 2 | 网络体系结构：分层与协议 |
| 3 | 物理层：从比特到信号 |
| 4 | 数据链路层与以太网交换 |
| 5 | VLAN 与无线局域网 |
| 6 | IP 地址：IPv4、子网划分与 IPv6 |
| 7 | 路由：数据包怎么找路 |
| 8 | 网络层的好帮手：ARP、ICMP、DHCP 与 NAT |
| 9 | 传输层：TCP 与 UDP |
| 10 | 应用层：域名、网页与常用服务 |
| 11 | 网络安全 |
| 12 | 网络管理、新技术与综合项目 |

每章含学习目标、情景导入、正文、本章常见问题对照、“AI 与网络”小节、3 个实验（2 个必做 ★、1 个选做 ☆）、小结、课后练习（单选、多选、判断可在线作答）和参考文献。另有附录 A～E（常用命令速查、实验环境、Cisco 与华为命令对照、术语表、实验报告模板与综合项目指南）、常见问题、学习图谱和两套闭卷模拟卷。

实验工具都免费：Windows 命令行、Wireshark（打开编者录制的抓包文件）、Cisco Packet Tracer（主线，附录 C 给出华为命令对照），以及少量只用标准库的 Python 程序。

## 目录结构

| 路径 | 内容 |
|---|---|
| `course.yml` | 课程配置：书名、学时、章节、附录。改完运行 `python tools/course.py sync` |
| `docs/chapters/` | 12 章正文 |
| `docs/sims/` | 交互动画（每个文件夹一个，`common/` 是公共样式和脚本） |
| `docs/appendix/` | 附录 |
| `docs/learning-graph/` | 学习图谱（概念和先修关系在 `data.js`，由 `tools/build_graph.py` 生成） |
| `docs/faq/`、`docs/mock-exam.md` | 常见问题、闭卷模拟卷 |
| `labs/` | 实验程序和抓包文件，见 `labs/README.md` |
| `slides/`、`lesson-plans/` | 每章课件底稿（`chNN.md`）和教案底稿（`chNN.yml`） |
| `tools/` | 维护脚本 |
| `.github/workflows/pages.yml` | 推送到 `main` 后自动发布网页 |
| `.github/workflows/exports.yml` | 手动运行，在 GitHub 上生成课件、教案和 Word/PDF 版 |

## 本地预览

```bash
pip install -r requirements-docs.txt
mkdocs serve          # 浏览器打开 http://127.0.0.1:8000
```

## 维护脚本

```bash
python tools/course.py sync                # 按 course.yml 更新导航、首页、章节骨架等
python tools/glossary_links.py anchors     # 给术语表每个术语加锚点
python tools/glossary_links.py link 03     # 第 3 章正文中的术语改成悬停可见定义的链接
python tools/glossary_links.py concepts 03 # 生成第 3 章的“本章概念清单”
python tools/build_graph.py                # 由术语表生成学习图谱数据
python tools/graph_text.py                 # 检查学习图谱并生成文字版
python tools/book_stats.py                 # 更新首页“全书概览”统计表
python tools/course.py new-sim 名称 3 "标题" # 新建第 3 章的交互动画骨架
```

## 课件、教案和 Word/PDF 版

```bash
pip install -r requirements-tools.txt
npm install && npx playwright install chromium
npm run figures                            # 把 Mermaid 图和交互动画渲染成图片

python tools/make_slides.py build all      # → build/课件/第NN章 章名.pptx
python tools/make_lesson_plan.py build all # → build/教案/第NN章 章名 教案.docx
python tools/export_docx.py --pdf          # → build/计算机网络.docx 和 .pdf（需要 pandoc 和 LibreOffice）
```

## 关于实验结果

- 抓包文件由编者在 Linux 网络命名空间搭建的小网络中录制（`labs/data/make_pcaps.sh`），正文引用的端口号、序号等都来自这些文件，请不要重新录制覆盖。
- Python 程序的输出是编者用 Python 3.13 实际运行得到的。
- Packet Tracer 和 Windows 命令的显示结果按标准格式整理，标为“输出格式示意”。编写环境装不了 Packet Tracer，建议任课教师课前在 Packet Tracer 9.0 中把各章实验走一遍。
