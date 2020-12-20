# 2020年12月20日15:01:04
# 偏函数


import functools

int2 = functools.partial(int, base=10)

print('1000000 =', int2('1000000'))
print('1010101 =', int2('1010101'))