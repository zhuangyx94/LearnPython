# coding:utf8
"""
1. python的注释#号后跟文字内容要空一格

"""


def checker(a):
    def _checker(func):
        def __checker(*args, **kwargs):
            for k in args:
                if k < 0:
                    return 0
            for k in kwargs.values():
                 if k < 0:
                     return 0
            return func(*args, **kwargs) + a
        return __checker
    return _checker


@checker(3)
def add(b, c):
    return b + c


if __name__ == '__main__':
    print add(1, 2)    
	

