# -*- coding: UTF-8 -*-

# Filename : 14-family-name.py
# author by : （学员ID)

# 要点：初步理解元组

import sys
import io
import random

# 解决输出显示汉字乱码的问题
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
#print (sys.stdout.encoding)  # 确认当前的控制台显示字符的编码

# 练习一， 指定挑选一个姓并显示
family_words = ("赵","钱","孙","李","周","吴","郑","王")
print("%s" % (family_words[0]))

pos = 5 # 位置
print("我要第 (%d) 个姓，它是 %s" % (pos + 1, family_words[pos])) # 要注意以 0 开头

# 练习二： 遍历所有的姓
for name in family_words:
    print("%s " % name, end="")

# 练习三：随机挑选一个姓，产生10遍以上
for i in range(3):
    pos = random.randint(0, 7)
    print("随机产生第 (%d) 个姓，它是 %s" % (i, family_words[pos])) # 要注意以 0 开头

# 练习四：随机组合姓名
family_words = ( "赵","钱","孙","李","周","吴","郑","王" )

print(len(family_words))
for i in range(3):
    pos = random.randint(0, len(family_words))
    print("百家姓第 (%d) 个姓，它是 %s" % (i, family_words[pos])) # 要注意以 0 开头
