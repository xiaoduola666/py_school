# 2020年11月22日14:04:19   map/reduce
# Python内建了map()和reduce()函数。

#
# def f(x):
#     return x * x
#
#
# r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
# for i in r:
#     print(i)


# from functools import reduce
#
#
# def add(a,y):
#     return a+y
# print(reduce(add,[1,3,5,7,9]))


# 笔记：
# map（）第一个参数是函数本身，后面接入list每次取第一个数进行传参
# functools（）第一个参数㐊函数本身，函数必须是两个参数，后面的list每次传第一个和第二个，然后而二个和第三个；