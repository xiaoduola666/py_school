# 2020年12月21日15:22:00
# 定制类


class Fib(object):

    def __getitem__(self, item):
        a, b = 1, 1
        for x in range(item):
            a, b = b, a+b
            return a

    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a+self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a


for i in Fib():
    print(i)
print(Fib()[1])


# 定制类 后面有很多可以处理各种情况的方法，后续用到请再查询