# 2020年11月20日15:46:42   生成器


# 只要把一个列表生成式的[]改成()，就创建了一个generator
# g = (x * x for x in range(10))
# k = [x * x for x in range(10)]
# print(g,type(g), k, type(k))
#
# t = (1,2)
# print(t[0])


def fib(max):
    n,a,b = 0,1,1
    while n  < max:
        yield b
        a,b = b , a+b
        n = n+1
    return 'done'

f = fib(10)
for n in fib(10):
    print(n)


# 笔记
# 1. 只要把一个列表生成式的[]改成()，就创建了一个generator
# 2. g = (x * x for x in range(10))  k = [x * x for x in range(10)]  g是生成器，k 是列表
# 3.generator是非常强大的工具 后面再看看不懂