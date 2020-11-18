# 2020年11月17日14:52:53  函数的参数

# 可变参数
# 加一个* 号可以把list 、 tuple的元素变成参数传递过去


def calc(*kw):
    print(kw)


calc(12, 3, 4, 5, 6, 7, 8, 9, )


# 关键字参数
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。而关键字参数允许你传入0个或任意个含参数名的参数，
# 这些关键字参数在函数内部自动组装为一个dict

# def person(name, page, **kw):
#     print(name, page, kw)
#
#
# person(1, 2, a=3, b=4, c=5, d=6)



#命名关键词参数
# 命名关键字参数，如果想调用，一定要用参数全程，不然会报错
def person(name, *, page ,xxkw):
    print(name, page, xxkw)

person(1,page=2,xxkw=3,)



# 总结：
# *args是可变参数，args接收的是一个tuple；
#
# **kw是关键字参数，kw接收的是一个dict。
