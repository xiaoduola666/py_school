# 2020年12月20日15:04:20
# 使用模块


import sys
a = 10
b = 100


def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello, world!',args)
    elif len(args) == 2:
        print('Hello, %s!' % args)
    else:
        print('Too many arguments!')


if __name__ == '__main__':
    test()
