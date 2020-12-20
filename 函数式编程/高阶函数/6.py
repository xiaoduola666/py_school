# 2020年12月09日18:06:59
# 装饰器

# def log(func):
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper


# def log(text):
#     def decorator(func):
#         def wrapper(*args, **kw):
#             print('%s %s():' % (text, func.__name__))
#             return func(*args, **kw)
#         return wrapper
#     return decorator
#
#
# @log()
# def now():IDE Eval Reset
#     print('2015-3-25')
#
# now()


def head(i):
    def s(*a, **aw):
        print('方法名称', i.__name__, a, aw)

    return s


@head
def on(a, b):
    print('on  内部打印', a, b)


on(1, 2)
