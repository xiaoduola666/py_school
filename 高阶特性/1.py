# 2020年11月19日10:06:57   切片

l = list(range(100))
# print(l)
# print(l[:10])
# print(l[3:10])
print(l[-1:])
print(l)
print(l[:1])
print(l[1:])

# 前10个数，每两个取一个：
# print(l[:10:2])

# 所有数，每5个取一个：
# print(l[::5])

# 甚至什么都不写，只写[:]就可以原样复制一个list：
# print(l[:])


# tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple：

# t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(t[:3])
# print(t[:7:2])
# print(t[::2])


# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
def trim(s):
    if len(s) == 0:
        return s
    while s[:1] == ' ':
        s = s[1:]
    while s[-1:] == ' ':
        s = s[:-1]
    return s

print(trim('   1233   '))