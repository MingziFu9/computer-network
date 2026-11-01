# 4.1.3 节示例：改动一个比特，CRC 校验值就完全不同（《计算机网络》第 4 章）
import zlib                                   # Python 自带，以太网用的就是 CRC-32

a = "小禾设计工作室".encode()                   # 原始数据
b = bytearray(a)
b[0] ^= 1                                     # 把第 1 个字节的最后一位翻转（0 变 1 或 1 变 0）
print("原始数据的 CRC-32：", hex(zlib.crc32(a)))
print("错一位后的 CRC-32：", hex(zlib.crc32(bytes(b))))
