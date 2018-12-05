# -*- coding: UTF-8 -*-

# Filename : 16-function.py
# author by : （学员ID)

import sys
import io
import random

# 解决输出显示汉字乱码的问题
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
# print (sys.stdout.encoding)  # 确认当前的控制台显示字符的编码

"""
# 练习一：
# 掌握简单的函数用法
def add(a, b):
    sum = a + b
    return (sum)

# 调用add 函数
x = add(1, 2)
print ("调用add()函数的结果是：%d" % (x))
"""

# 练习二：将求三角形面积函数化
def triangle_area(a, b, c):
    # 依据海伦公式求任意三角形面积
    # 已知三角形三边a,b,c,半周长p,则S＝ √[p(p - a)(p - b)(p - c)] （海伦公式）（p=(a+b+c)/2）
    # 计算半周长
    p = (a + b + c) / 2

    # 计算面积
    # 掌握 python 开根号的写法
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    return area

a = float(input('输入三角形第一边长: '))
b = float(input('输入三角形第二边长: '))
c = float(input('输入三角形第三边长: '))
area = triangle_area(a, b, c)
print('三角形面积为 %0.2f' % area)
