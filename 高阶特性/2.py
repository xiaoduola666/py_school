# 2020年11月19日11:01:16   迭代

# d = {'a': 1, 'b': 2, 'c': 3}
# for key in d:
#     print(key)
#
# for value in d.values():
#     print(value)

# enumerate函数可以把一个list变成索引-元素对
# for i, value in enumerate(['A', 'B', 'C']):
#     print(i, value)

# 请使用迭代查找一个list中最小和最大值，并返回一个tuple：


def find_Min_And_Max(L):
    max = 0
    for number in L:
        if number > max:
            max = number

    min = 100
    for numbers in L:
        if numbers < min:
            min = numbers

    return max, min


list = [1,2,3,4,5,6,7]
print(find_Min_And_Max(list))



# 笔记
# 1.Python内置的enumerate函数可以把一个list变成索引-元素对
# 2.Python的for循环不仅可以用在list或tuple上
# 3. for key in dict:
# 4. for value in dict.values():
