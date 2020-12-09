# Python内建的filter()函数用于过滤序列。
# 和map()类似，filter()也接收一个函数和一个序列。
# 和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
# filter() 可以将函数进行筛选


list = ['A', '', 'B', None, 'C', '  ']
# for i in list:
#     if i is None:
#         print(0)
#     elif i.split():
#         print(1)
#     else:
#         print(2)
        
f = filter(None,list)
print(f)