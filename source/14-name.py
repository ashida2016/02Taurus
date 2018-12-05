# -*- coding: UTF-8 -*-

# Filename : 14-name.py
# author by : （学员ID)

# 要点：初步理解元组和列表

import sys
import io

# 解决输出显示汉字乱码的问题
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
print (sys.stdout.encoding)



family_name = ("赵","钱","孙","李","周","吴","郑","王")
#family_name = ('a','b','c')
print("%s" % (family_name[0]))
