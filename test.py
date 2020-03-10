#coding:utf8

# =========================================================================
tsr = ''' ==>测试itertools.product 打印3个列表的某一元素，这三个元素的总各是12 '''
from itertools import product
# product 乘积， 结果
num1 = [1, 2, 3, 4, 5, 6]
num2 = [7, 8, 9, 10, 11, 12]
num3 = [4, 1, 0, -2, 9]

print tsr
for i in num1:
    for j in num2:
        for m in num3:
            if i + j + m == 12:
                print i, j, m, ' | ',
print '-' * 12
for i, j, m in product(num1, num2, num3):
    if i + j + m == 12:
        print i, j, m, ' | ',
# =========================================================================
tsr = '''==>只打打印奇数行 '''
filename = "abc.txt"


def print_uneven_line(file_path):
    with open(file_path) as fp:
        for i, line in enumerate(fp):
            if i % 2 == 0:
                yield line.strip()


''' 使用 islice 实现循环内隔行处理
    islice(seq, start, end, step)
    如果需要在循环内部进行隔行处理的话，只要设置第三个递进步长参数 step 值为 2 即可（默认为 1）
     '''
from itertools import islice


def print_uneven_line2(file_path):
    with open(file_path) as fp:
        for line in islice(fp, 0, None, 2):
            yield line.strip()


print
print tsr
# print print_uneven_line(filename)
# print print_uneven_line2(filename)

# =========================================================================
tsr = '''==> 使用 takewhile 替代 break 语句
'''
print tsr

from itertools import takewhile


def is_gt5(a):
    return True if a < 5 else False


lit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 16]
for i in takewhile(is_gt5, lit):  # 如果里面的函数返回假， 则停止循环
    print i,
print

# =========================================================================
tsr = '''== > 使用生成器编写自己的修饰函数
除了 itertools 提供的那些函数外，我们还可以非常方便的使用生成器来定义自己的循环修饰函数 '''
print tsr
# 过滤偶数
lit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 16]


def filter_0_gen(lit):
    for i in lit:
        if i % 2 != 0:
            yield i


for i in filter_0_gen(lit):
    print i,
print

# =========================================================================
tsr = '''==>建议2：按职责拆解循环体内复杂代码块 '''
print tsr

from datetime import date, timedelta
def last30day():
    days = 30
    for day_delta in range(days):
        day_30 = date.today() - timedelta(day_delta)
        if day_30.weekday()  in (5,6):
            print day_30
            
last30day()


# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
# =========================================================================
