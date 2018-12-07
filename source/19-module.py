# -*- coding: UTF-8 -*-

# Filename : 19-module.py
# author by : （学员ID)

# 要点：函数 + 元组
import sys
import io
import random

# 目的：学会调用自己写的模块
#import 17-func-family-name
import b17_family_name
import b18_given_name

# 解决输出显示汉字乱码的问题
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
#print (sys.stdout.encoding)  # 确认当前的控制台显示字符的编码

#定义选取次数
pick_times = 5

# -------------  调用函数 ---------------------------
print("任意选取 (%d) 个人物的姓，分别是：" %(pick_times), end="")
for i in range(pick_times):
    picked_name = b17_family_name.pick_family_name()
    print("(%d)- %s" % (i, picked_name))


# -------------  调用函数 ---------------------------
print("选取 (%d) 个男生的名，分别是：" %(pick_times), end="")
for i in range(pick_times):
    picked_name = b18_given_name.pick_given_name(1)
    print("%s " % (picked_name), end="")

print("\n")
print("选取 (%d) 个女生的名，分别是：" %(pick_times), end="")
for i in range(pick_times):
    picked_name = b18_given_name.pick_given_name(2)
    print("%s " % (picked_name), end="")

# -------------  调用函数 ---------------------------
pick_times = 500
print("\n-----------华丽分割线---------------")
print("选取 (%d) 个人物姓名，分别是：\n" %(pick_times), end="")

for i in range(pick_times):
    # 随机挑选姓氏
    family_name = b17_family_name.pick_family_name()
    # 随机产生性别
    sex = random.randint(1, 2)
    # 随机挑选名
    given_name = b18_given_name.pick_given_name(sex)
    # 组成全名
    full_name = family_name + given_name
    # 输出全名及性别
    print("No.(%d) 人物，性别(%d),姓名(%s)" % (i, sex, full_name))
