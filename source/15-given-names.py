# -*- coding: UTF-8 -*-

# Filename : 15-given-name.py
# author by : （学员ID)

# 要点：初步理解列表

import sys
import io
import random

# 解决输出显示汉字乱码的问题
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
#print (sys.stdout.encoding)  # 确认当前的控制台显示字符的编码

# 练习一， 指定挑选一个名并显示
given_names = ["致浩","明云","浩烨","兆忠","予忻","顺雨","尚扬","俊祥","语禅","予浩"]
print("%s\n" % (given_names[0]))

pos = 5 # 位置
print("我要第 (%d) 个名，它是 %s\n" % (pos + 1, given_names[pos])) # 要注意以 0 开头

# 练习二： 遍历所有的姓
print("所有的名： ", end="")
for name in given_names:
    print("%s " % name, end="")
print("\n")

# 练习三：随机挑选一个姓，产生10遍以上
for i in range(3):
    pos = random.randint(0, 9)
    print("随机产生第 (%d) 个姓，它是 %s" % (i, given_names[pos])) # 要注意以 0 开头

# 练习四，更改列表中某一个元素
given_names[0] = "改我的名"
print("所有的名： ", end="")
for name in given_names:
    print("%s " % name, end="")
print("\n")

# 练习四： 随机生成2个字的名 random.sample
given_names1 = [ \
"潮","彻","郴","琛","澈","臣","辰","晨","承","盛","程", \
"池","炽","冲","重","崇","绸","畴","酬","筹","楚","处", \
"棰","锤","淳","赐","聪","璁","丛","淙","琮","璀","村", \
"达","大","代","岱","玳","单","郸","石","当","铛","党", \
"祷","道","得","德","地","灯","登","迪","狄","笛","柢", \
"递","谛","滇","巅","典","淀","雕","顶","鼎","东","栋", \
"笃","度","端","缎","煅","锻","敦","铎","恩","发","法", \
"凯","志","明","伟","嘉","东","建","文","子","云","杰", \
"兴","友","才","振","辰","航","达","鹏","宇","衡","佳", \
"强","宁","丰","波","森","学","民","永","翔","鸿","海", \
"文","军","明","贵","藏","操","焯","晁","朝","驰","川", \
"义","生","凡","连","良","乐","勇","辉","龙","川","宏", \
"达","安","岩","中","茂","进","林","有","诚","先","敬", \
"震","振","正","永","辉","波","涛","超","强","文","军", \
"明","周","贵","友","鹏","勋","宁","元","栋","嘉","哲", \
"俊","博","彬","富","顺","信","子","杰","涛","昌","豪", \
"邦","承","乐","绍","浩","俊","泽","嘉","杰","宇","涵", \
"博","思","哲","家","正","永","辉","波","涛","超","强", \
"魄","檗","卜","步","埔","瓿","才","材","财","参","灿", \
"策","曾","差","察","昌","长","昶","畅","倡","绰","超", \
"帆","藩","杠","巩","贡","钩","加","家","嘉","见","将", \
"凡","飞","斐","奋","丰","风","枫","峰","烽","锋","逢", \
"福","阜","复","奖","强","金","津","竟","靖","镜","镌", \
"赋","富","盖","溉","概","甘","刚","岗","钢","罡","港", \
"高","诰","革","葛","铬","根","庚","耿","功","宫","恭", \
"构","故","顾","观","冠","莞","管","光","广","归","圭", \
"贵","桂","过","纪","技","系","季","际","继","绩","稷", \
"谦","锋","霆","玉","智","名","进","德","聚","军","兵", \
"忠","廷","先","江","昌","政","君","泽","超","信","恒", \
"礼","元","磊","阳","洋","恩","迅","富","胜","震","福", \
"传","创","存","锉","宕","导","岛","砥","斗","督","顿", \
"瀚","瑞","朔","荣","为","诚","斌","广","庆","成","峰", \
"可","健","英","功","锦","立","平","旭","同","全","豪", \
"源","安","顺","帆","向","雄","利","希","风","林","奇", \
"易","来","启","坤","昊","朋","和","纪","艺","昭","映", \
"威","奎","帅","星","春","章","伦","城","钊","刚","洲", \
"家","晗","浩","景","珂","策","皓","栋","棠","登","越", \
"盛","语","钧","亿","基","理","纶","维","瑜","齐","琛", \
"毅","谊","贤","逸","卫","万","臻","儒","洁","霖","隆", \
"远","聪","耀","誉","继","哲","岚","康","星","光","天", \
"甲","价","驾","架","稼","尖","坚","间","俭","检","简", \
"饯","建","剑","健","漳","谏","践","镜","鉴","键","江", \
"交","佼","皎","觉","教","阶","节","杰","解","介","界", \
"进","近","劲","晋","京","经","荆","景","敬","径","竞", \
"炯","赳","九","韭","京","居","驹","枸","举","巨","炬", \
"隽","决","诀","军","均","君","钧","俊","郡","峻","浚", \
"骏","竣","开"
]
for generate_times in range(5):
    print("\n随机取名-第(%d)个自组名：" % (generate_times + 1), end="")
    given_name_num = random.randint(1, 2)
    """
    # 第一种方法：用 pos 定位
    for pick_times in range(given_name_num):
        pos = random.randint(1, len(given_names1))
        print("%s" % (given_names1[pos]), end="") # 要注意以 0 开头
    """

    # 第二种方法： 直接用 sample
    # random.seek()
    if given_name_num == 1:
        #new_name = random.choice(given_names1)
        new_name = random.sample(given_names1, 1)
    else:
        new_name = random.sample(given_names1, 2)
    print(new_name, end="")

# 练习五：random.choice
given_names2 = [ \
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
    new_name = random.choice(given_names2)
    print(new_name, end="")
