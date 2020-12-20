# 2020年12月20日15:34:19
# 访问权限


class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_scort(self):
        print("%s, %s" % (self.__name, self.__score))

    # 重写一个方法访问内部变量
    def get_neme(self):
        return self.__name

    # 重写一个方法访问内部变量
    def get_score(self):
        return self.__score

    # 重写一个方法带参数，判断后修改内部变量
    def set_scort(self,score):
        if 0 <= score <= 100:
            self.__score = score
            print(score)
        else:
            raise ValueError('bad score')


bart = Student('wutianle', 22)
print(bart.set_scort(11))
print(bart.print_scort())