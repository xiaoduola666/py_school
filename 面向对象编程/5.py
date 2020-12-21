# 2020-12-21 14:43:27
# 实例属性和类属性


class Student(object):
    name = 'wutianle'

s = Student()
s.name = 'lol'
print(s.name)

# 实例属性要比类属性优先级高，所以不要轻易重名