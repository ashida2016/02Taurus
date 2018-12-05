# -*- coding: UTF-8 -*-

# Filename : 16-function.py
# author by : （学员ID)

import sys
import io
import random

# 解决输出显示汉字乱码的问题
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
# print (sys.stdout.encoding)  # 确认当前的控制台显示字符的编码

# 掌握简单的函数用法
def add(a, b):
    return (a + b)

# 调用add 函数
x = add(1, 2)
print ("调用add()函数的结果是：%d" % (x))
