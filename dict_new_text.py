# -*- encoding: utf-8 -*-
'''
@File    :   dict_new_text.py
@Time    :   2020/02/22 09:46:41
'''

#============================================================================
# 升级
dit = {'a':1}
dit.update({'a':2})
dit.update({'b':1})
dit.update(c=3, d=4)
print(dit)


# 1创建空字典
dit0 ={}
print(type(dit0)) 

# 2直接赋值创建 
dit0 = {'a':1, 'b':2, 'c':3}
print(dit0)

# 3通过关键字dict和关键字参数创建
dit0 = dict(a=1,b=2,c=3)
print(dit0)

# 4通过二元组列表创建
lit = [('a', 1), ('b', 2), ('c', 3)]
dit0 = dict(lit)
print(dit0)

# 5dict和zip组合创建
dit0 = dict(zip('abc', [1,2,3]))
print(dit0)

# 6通过字典推导式创建
dit0 = {i:2*i for i in range(3)}
print(dit0)

# 7通过dict.fromkeys()创建
dit0 = dict.fromkeys(range(3), 'x')
print(dit0)

# 8,其它
lit = ['x', 1, 'y',2, 'z', 3]
dit0 = dict(zip(lit[::2], lit[1::2]))
print(dit0)

