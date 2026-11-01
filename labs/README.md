# 实验文件

按章存放，`chNN/` 对应第 NN 章，每个文件夹里的 `README.md` 列出本章三个实验分别用到哪些文件。公共的抓包文件和编者录制用的脚本放在 `data/`，见 [data/README.md](data/README.md)。

## 需要准备什么

| 工具 | 用在哪些章 | 获取 |
|---|---|---|
| Windows 命令提示符 | 全书（`ipconfig`、`ping`、`tracert`、`nslookup` 等） | 系统自带 |
| Wireshark | 第 2、4、5、8、9、10、11 章 | <https://www.wireshark.org> |
| Cisco Packet Tracer | 第 4、5、6、7、8、10、11、12 章 | <https://www.netacad.com>（免费注册） |
| Python 3.10 以上（推荐 Thonny） | 第 1、3、4、5、6、7、8、9、10、11、12 章的少量程序 | <https://thonny.org> |

所有 Python 程序都**只用 Python 自带的标准库**，不需要 `pip install` 任何东西。详细说明见教材附录 B。

## 运行

**进入程序所在的文件夹再运行**，因为有的程序要按相对路径读取 `../data/pcap/` 中的抓包文件：

```bash
cd ch06
python lab6_1_subnet.py
```

用 Thonny 时直接打开 `.py` 文件，点绿色的“运行”按钮即可。

第 9 章的聊天程序和第 10 章的网站要开两个窗口：先运行服务器端，再运行客户端。

## 结果说明

书中 Python 程序的运行结果是编者用 Python 3.13 实际运行得到的；抓包文件是编者在真实的小网络中录制的，书中引用的端口号、序号等都来自这些文件。Packet Tracer 和 Windows 命令的显示结果标为“输出格式示意”，具体数值在你的电脑上会不同。

## 安全提醒

只能在自己的电脑、自己管理的网络或经授权的实验环境中抓包和扫描。`python -m http.server` 会把当前目录中的文件全部公开，不要在含有私人文件的目录中运行，也不要用于正式网站。
