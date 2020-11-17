# 2020年11月17日10:42:00 dict and set

# d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}


# 要避免key不存在的错误，有两种办法，一是通过in判断key是否存在：
# print('wu' in d)

# 二是通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value：
# print(d.get('wu',1))

# 要删除一个key，用pop(key)方法，对应的value也会从dict中删除：
# print(d.pop('Bob'))
# print(d)


# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。

# s = {1, 2, 3,6,3,7,2}
# s1 = {1,3,4}


# sort 内置函数用作排序
# a = ['c', 'b', 'a']
# a.sort()
# print(a)


# replace 用作替换字符串里的
a = 'a23'
c = a.replace('a', 'A')
print(c)
print(a)