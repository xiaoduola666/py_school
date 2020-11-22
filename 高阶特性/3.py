# 2020年11月20日15:00:53   列表生成式
# L = []
# for i in range(1, 11):
#     s = "%s * %s" % (i, i)
#     L.append(s)
# print(L)
#

# 写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来，十分有用，多写几次，很快就可以熟悉这种语法。
# print([x * x for x in range(1,11) if x % 2 == 0])


# 还可以使用两层循环，可以生成全排列
# print([m + n for m in 'ABC' for n in 'XYZ'])

# import os
# os.listdir可以列出文件和目录 listdir 在当前路径下找相对路径
# print([d for d in os.listdir('../')])



# 笔记
# 1. x+x for x in range(1,10):
# 2. dict的items() 返回可遍历的(键, 值) 元组数组
# 3. isinstance函数可以判断一个变量是不是字符串,lower() 转换字符串中所有大写字符转换小写
