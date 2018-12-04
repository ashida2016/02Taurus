# Filename : 11-if.py
# author by : （学员ID)

# Python 判断奇数偶数
# 如果是偶数除于 2 余数为 0
# 如果余数为 1 则为奇数
num = int(input("输入一个整数: "))
if (num % 2) == 0:
    # print("%d 是偶数" % num)
    print("%s 是偶数" % str(num))
    # print("{0} 是偶数".format(num))
else:
    print("%d 是奇数" % num)
    # print("{0} 是奇数".format(num))

# 判断是否为闰年
# 闰年条件：闰年条件, 满足年份模400为0, 或者模4为0但模100不为0.
year = int(input("输入一个年份: "))
if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print("{0} 是闰年".format(year))  # 整百年能被400整除的是闰年
        else:
            print("{0} 不是闰年".format(year))
    else:
        print("{0} 是闰年".format(year))  # 非整百年能被4整除的为闰年
else:
    print("{0} 不是闰年".format(year))

# 判断输入的三个数字是否为正常的三角形三边长
#   如果是则计算其面积
#   如果否则输出错误信息

a = float(input('输入三角形第一边长 a=: '))
b = float(input('输入三角形第二边长 b= : '))
c = float(input('输入三角形第三边长 c=: '))

if (a + b) >= c:
    if (a + c) >= b:
        if (b + c) >= a:
            if abs(a - b) < c:
                if abs(a - c) < b:
                    if abs(b - c) <a:
                        # 计算半周长
                        p = (a + b + c) / 2
                        # 计算面积
                        # 掌握 python 开根号的写法
                        area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
                        print('正确！三角形面积为 %0.2f' % area)
                    else:
                        print("错误！b-c<a 无法组成三角形")
                else:
                    print("错误！a-c<b 无法组成三角形")
            else:
                print("错误！a-b<c 无法组成三角形")
        else:
            print("错误！b+c<a 无法组成三角形")
    else:
        print("错误！a+c<b 无法组成三角形")
else:
    print("错误！a+b<c 无法组成三角形")
