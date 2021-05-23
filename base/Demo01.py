# 命名关键字参数

def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)


# **kw传入参数个数不受限制，且都为命名关键字参数
# name: Jack age: 24 other: {'city': 'Beijing', 'addr': 'Chaoyang', 'zipcode': 123456}
person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)


# 与**kw不同，*后面的参数被视为命名关键字参数

def person02(name, age, *, city, job):
    print(name, age, city, job)  # zhangsan02 2 beijin chengxuyuan


person02('zhangsan02', 2, city='beijin', job='chengxuyuan ')


def person03(name, age, *args, city, job):
    print(name, age, args, city, job)  # Jack 24 ('zhangsan', 18, ('lisi', 19)) Beijing Engineer


person03('Jack', 24, 'zhangsan', 18, ('lisi', 19), city='Beijing', job='Engineer')


###################################
# 参数组合

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


# Python解释器自动按照参数位置和参数名把对应的参数传进去

f1(1, 2)  # a = 1 b = 2 c = 0 args = () kw = {}

f1(1, 2, c=3)  # a = 1 b = 2 c = 3 args = () kw = {}

f1(1, 2, 3, 'a', 'b')  # a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}

f1(1, 2, 3, 'a', 'b', x=99)  # a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}

f2(1, 2, d=99, ext=None)  # a = 1 b = 2 c = 0 d = 99 kw = {'ext': None}

# 最神奇的是通过一个tuple和dict，你也可以调用上述函数：

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)     # a = 1 b = 2 c = 3 args = (4,) kw= {'d':99, 'x': '#'}

args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)     # a = 1 b = 2 c = 3 d = 88 kw = {'x': '#'}
