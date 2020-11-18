# 2020年11月17日14:23:31   定义函数

# 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程 ax^2+bx+c=0ax2+bx+c=0 的两个解。

import math


def quadratic(a, b, c):
    s = b*b-4*a*c
    s1 = math.sqrt(s)
    x = 2*a
    print(s1, x)

# 笔记
# 1.方法用def 声明
# 2.函数体内部可以用return随时返回函数结果；
# 3.函数执行完毕也没有return语句时，自动return None。
# 4.函数可以同时返回多个值，但其实就是一个tuple。