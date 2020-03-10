# coding:utf8

# =========================================================================
tsr = '''==> chain : 参数是可迭代的对象都可以拼接； 返回一个迭代器
    chain本质返回一个生成器，所以它实际上是一次读入一个元素到内存，所以做到最高效地节省内存
    '''
print tsr 
import itertools  
jj =  itertools.chain([1,23], (1,5,6))
print jj, type(jj)
# 生成器无法  进行  len  

# =========================================================================
# =========================================================================
''' 2 逐个累积
    返回列表的累积汇总值，原型：
    accumulate(iterable[, func, *, initial=None])
    应用如下：
    In [36]: list(accumulate([1,2,3,4,5,6],lambda x,y: x*y))
    Out[36]: [1, 2, 6, 24, 120, 720] '''
# =========================================================================
'''3 漏斗筛选
    它是compress 函数，功能类似于漏斗功能，所以我称它为漏斗筛选，原型：
    compress(data, selectors)
    In [38]: list(compress( abcdefg ,[1,1,0,1]))
    Out[38]: [ a ,  b ,  d ]  '''
# =========================================================================
''' 4 段位筛选
    扫描列表，不满足条件处开始往后保留，原型如下：
    dropwhile(predicate, iterable) '''
# =========================================================================
''' 5 段位筛选2
    扫描列表，只要满足条件就从可迭代对象中返回元素，直到不满足条件为止，原型如下：
    takewhile(predicate, iterable) '''
# =========================================================================
''' 6次品筛选
    扫描列表，只要不满足条件都保留，原型如下：
    dropwhile(predicate, iterable)  '''
# =========================================================================
'''7 切片筛选
     islice(iterable, start, stop[, step]) '''
# =========================================================================
''' 8细胞分裂
    tee函数类似于我们熟知的细胞分裂，它能复制原迭代器n个
    tee(iterable, n=2)
    应用如下，可以看出复制出的两个迭代器是独立的
    a = tee([1,3,4], 2)
    a = tuple(1,2)
    a[0] 和 a[1] 是相同的且独立的两个迭代器
 '''
# =========================================================================
''' 9 map变体
    starmap可以看做是map的变体，它能更加节省内存，同时iterable的元素必须也为可迭代对象，原型如下：
    starmap(function, iterable) '''
# =========================================================================
''' 11 笛卡尔积
    produce(iterA, iterB)
    笛卡尔积实现的效果同下： ((x,y) for x in A for y in B)
    In [187]: itertools.product('abc', 'cd')
    Out[187]: <itertools.product at 0x40c4a20>
    In [188]: print_iter(_)
    ('a', 'c') ('a', 'd') ('b', 'c') ('b', 'd') ('c', 'c') ('c', 'd')
 '''
# =========================================================================
''' 12 加强版zip
        组合值。若可迭代对象的长度未对齐，将根据 fillvalue 填充缺失值，注意：迭代持续到耗光最长的可迭代对象，效果如下
        zip_longest( ABCD ,  xy , fillvalue= - )
        ************ 报错没有此函数， 可能不在python2版本吧*************
         '''
        
# =========================================================================
''' repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数：
    >>> ns = itertools.repeat('A', 10)
    >>> for n in ns:
    ...     print n
    打印10次'A' '''
# =========================================================================
''' itertools提供的几个“无限”迭代器：
    >>> natuals = itertools.count(1)
    >>> for n in natuals:
    ...     print n
    ...
    1
    2
    3
    >>> import itertools
    >>> cs = itertools.cycle('ABC') # 注意字符串也是序列的一种
    >>> for c in cs:
    ...     print c
    ...
    'A'
    'B'
    'C'
    'A'
    'B'
    'C'

 '''
# =========================================================================
    
