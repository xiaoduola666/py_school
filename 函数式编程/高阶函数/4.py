# 2020年12月08日11:44:58
# 返回函数

def calc_sum(args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax


lists = (1, 2, 3, 4)
f = calc_sum(lists)
print(f)

