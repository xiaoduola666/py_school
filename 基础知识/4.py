# 2020年11月16日18:44:24  判断条件

# 练习
# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
#
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖
# 用if-elif判断并打印结果：


a = float(input('请输入身高'))
b = float(input('请输入体重'))
c = b/(a*a)
c = round(c,2)
print(f'{c:.2f}')
if c < 18.5:
    print('过于轻了')
elif 18.5 <= c < 25:
    print('正常')
elif 25 <= c < 28:
    print('过重')
elif 28 <= c <32:
    print('肥胖')
elif 32 <= c:
    print('严重肥胖')
else:
    print('输入错误')


#笔记
# 1. round 可以直接把参数格式化成小数点几位数
# 2. 需要熟练账务哦字符串打印
# 3. input输入的类型为str ，str不能直接进行计算
