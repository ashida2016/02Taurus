# -*- coding: UTF-8 -*-

# Filename : 14-name.py
# author by : （学员ID)

# 要点：初步理解元组和列表
import os
import sys
import codecs
import io

#print (family_name[0].encode('utf-8'))
#sys.stdout = codecs.getwriter('gb2312')(sys.stdout)
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb2312')
print (sys.stdout.encoding)



family_name = ("赵","钱","孙","李","周","吴","郑","王")
#family_name = ('a','b','c')
print("%s" % (family_name[0]))
