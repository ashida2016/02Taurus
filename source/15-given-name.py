# -*- coding: UTF-8 -*-

# Filename : 15-given-name.py
# author by : （学员ID)

# 要点：初步理解列表，了解断行
 
import sys
import io
import random

# 解决输出显示汉字乱码的问题
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
#print (sys.stdout.encoding)  # 确认当前的控制台显示字符的编码

# 练习一， 指定挑选一个名并显示
given_words = ["致浩","明云","浩烨","兆忠","予忻","顺雨","尚扬","俊祥","语禅","予浩"]
print("%s\n" % (given_words[0]))

pos = 5 # 位置
print("我要第 (%d) 个名，它是 %s\n" % (pos + 1, given_words[pos])) # 要注意以 0 开头

# 练习二： 遍历所有的姓
print("所有的名： ", end="")
for name in given_words:
    print("%s " % name, end="")
print("\n")

# 练习三：随机挑选一个姓，产生10遍以上
for i in range(3):
    pos = random.randint(0, len(givenwords))
    print("随机产生第 (%d) 个姓，它是 %s" % (i, given_words[pos])) # 要注意以 0 开头

# 练习四，更改列表中某一个元素
given_words[0] = "改我的名"
print("所有的名： ", end="")
for name in given_words:
    print("%s " % name, end="")
print("\n")

# 练习四： 随机生成2个字的名 random.sample
given_words1 = [ \
"潮","彻","郴","琛","澈","臣","辰","晨","承","盛","程", \
"池","炽","冲","重","崇","绸","畴","酬","筹","楚","处", \
]
for generate_times in range(5):
    print("\n随机取名-第(%d)个自组名：" % (generate_times + 1), end="")
    given_name_num = random.randint(1, 2)
    """
    # 第一种方法：用 pos 定位
    for pick_times in range(given_name_num):
        pos = random.randint(1, len(given_words1))
        print("%s" % (given_words1[pos]), end="") # 要注意以 0 开头
    """

    # 第二种方法： 直接用 sample
    # random.seek()
    if given_name_num == 1:
        new_name = random.sample(given_words1, 1)
    else:
        new_name = random.sample(given_words1, 2)
    print(new_name, end="")

# 练习五：random.choice
given_words2 = [ \
"致浩","明云","浩烨","兆忠","予忻","顺雨","尚扬","俊祥","语禅","予浩", \
"童兆","可然","业尚","抒霄","如海","聿彦","德容","政斌","羽凡","沛林", \
"毅宾","晖予","运川","志双","程涵","英资","曦傲","誉冉","翊暄","兆博", \
"梓楚","祖翰","轩睿","梓哲","偌宸","炜晁","宜书","以诺","睿思","开浩", \
"峥延","灿烨","煜萧","亿鑫","家容","冬抒","谊言","凌宏","江哲","苛弈", \
"名轩","涵蓄","卫洋","洪生","鸿森","霖祥","浩广","睿才","宇琪","华瑞", \
"子櫲","羽希","梓灵","渤驰","圣彭","岩辉","寅升","思宇","艺喧","艳秋", \
"汇然","楷荣","宁彦","韵沅","君戎","学竣","宇笑","俊曦","宸源","岳楠", \
"予抒","尚寅","烨赫","宏旷","呈熙","祺然","俊麟","心逸","雨桐","晖尚", \
"炳鑫","睿炯","智笙","毓珲","廷希","章宸","玉庭","震晗","梓瑾","文悦", \
"士元","禹浩","凯文","兴睿","抒淯","煜烨","家燊","宏扬","笑书","烨毅", \
"潇育","思博","德懿","慕鑫","意佳","子烨","奕洋","华铭","旭滕","昶旭", \
"宇聪","鑫宇","桦烨","士忠","会钧","泓宁","名宁","子予","杰呈","懿敏", \
"旭鸣","景森","钦瑞","萧宸","国欣","亭钧","恩曦","雄智","天叙","君昊", \
"启纬","菁眙","龙辰","皓予","誉浛","华阳","成笑","鸣逸","阳越","疏鸣", \
"巍续","瑞奇","羽翰","岳阳","秋智","永春","苛意","欣诺","铭亿","羽盈", \
"有聪","珈毓","夙宸","致彬","佩誉","含烨","羽儒","志利","艺蕴","羽纤", \
"世方","朗贤","睿芯","语阳","硕育","彦淳","美轩","峪含","浩玮","益含", \
"泣涵","俊言","凇伯","梦熙","峻熙","胥宸","舞轩","书懿","智邦","源彬", \
"炯抒","宇齐","睿珅","晨杰","高明","雨益","尚悦","晔尚","茗钦","雪山"  \
]
for generate_times in range(5):
    print("\n随机取名-第(%d)个双名：" % (generate_times + 1), end="")
    new_name = random.choice(given_words2)
    print(new_name, end="")
