def fun1(*args):
    print(args)


def fun2(**kwargs):
    print(kwargs)


if __name__ == '__main__':
    fun1(['zhangsan'], {'password': '123456'}, 'str123')
    fun2(username='lisi', age=19)
