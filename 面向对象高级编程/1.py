# 2020年12月21日14:49:27
# 使用__slots__
from types import MethodType


class Student(object):
    __slots__ = ("name", "age")

    def __init__(self):
        pass


def set_age(self,age):
    self.age = age


s = Student()

#
# s.set_age = MethodType(set_age, s)
# s.set_age(25)
# print(s.age)
#
#
# s1 = Student()
# print(s1.set_age(25))


s.name = 'wutianle'
Student.names = 'liandgliadnf'
# s.HUO = '123'

print(type(Student.name),type(Student.names))


# slots 限制实例属性