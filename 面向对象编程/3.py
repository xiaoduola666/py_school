# 2020年12月20日15:50:25
# 继承和多态


class Animal(object):
    def run(self):
        print('Animal is running....')


class Dog(Animal):

    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')


class Cat(Animal):
    def run(self):
        print('Cat is running...')


Cat().run()
Dog().run()
