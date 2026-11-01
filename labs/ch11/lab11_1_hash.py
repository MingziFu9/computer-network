# 实验 11-1 第三档：哈希的“指纹”特性
import hashlib                                  # Python 自带的哈希工具

def fingerprint(text):
    """返回一段文字的 SHA-256 哈希值（64 个十六进制字符）"""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

a = "本月工资明细：小林 6800 元"                  # ← 改这里，换成别的文字
b = "本月工资明细：小林 8800 元"                  # 只改了一个字
print("原文 A：", a)
print("指纹 A：", fingerprint(a))
print("原文 B：", b)
print("指纹 B：", fingerprint(b))
print("指纹长度：", len(fingerprint(a)), "个字符；再算一次 A：", fingerprint(a) == fingerprint(a))
