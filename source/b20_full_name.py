# -*- coding: UTF-8 -*-

# Filename : 19-module.py
# author by : （学员ID)

# 要点：函数 + 元组
import sys
import io
import random
import json

# 目的：学会调用自己写的模块
#import 17-func-family-name
import b17_family_name
import b18_given_name

# 目的：加深对 list 的操作（去重，追加，调用）
#       JSON 文件格式初步

# 解决输出显示汉字乱码的问题
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
#print (sys.stdout.encoding)  # 确认当前的控制台显示字符的编码

# 生成 n 个人物姓名并放置到一个 list 中去

# -------------  调用函数 ---------------------------
pick_times = 5000

# 列表的追加
character_names = []
character_sexs = []
for i in range(pick_times):
    # 随机挑选姓氏
    family_name = b17_family_name.pick_family_name()

    # 随机产生性别
    sex = random.randint(1, 2)
    character_sexs.append(sex)

    # 随机挑选名
    given_name = b18_given_name.pick_given_name(sex)

    # 组成全名
    full_name = family_name + " " + given_name
    # 输出全名及性别
    #print("No.(%d) 人物，性别(%d),姓名(%s)" % (i, sex, full_name))
    character_names.append(full_name)

print("选取了 (%d) 个人物姓名，分别是：\n" %(pick_times), end="")
for i in range(len(character_sexs)):
    print(" 人物Id(%d)，性别(%d),姓名(%s)" % (i, character_sexs[i], character_names[i]))

# 列表的去重
character_names_no_repeated =[]
for name in character_names:
    if name not in character_names_no_repeated:
        character_names_no_repeated.append(name)

print("去重前的名字列表有(%d)个，去重后的名字列表有(%d)个，去除了重复的(%d)个名字" % (    \
    len(character_names),                                                           \
    len(character_names_no_repeated),                                               \
    len(character_names) - len(character_names_no_repeated)                         \
    ))
