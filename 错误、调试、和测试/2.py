# 2020年12月21日15:48:50
# 调试

# 1.第一种方法，没步用print
# 2.第二种方法 用 assert 来代替
# 3.第三种方法 用logging
# 4.第四种方法 用pdb

# def index(a):
#     assert a != 0, 'erro '
#
#
# index(0)


#


import pdb

s = '0'
n = int(s)
pdb.set_trace() # 运行到这里会自动暂停
print(10 / n)