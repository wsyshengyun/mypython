# coding:utf8


def count_abc():
    count = 0
    with open('abc.txt') as fp:
        for line in fp:
            count += line.count('w')
    return count


import itertools
''' 使用 read 方法分块读取
    为了解决这个问题，我们需要暂时把这个“标准做法”放到一边，使用更底层的 file.read() 方法。与直接循环迭代文件对象不同，
    每次调用 file.read(chunk_size) 会直接返回从当前位置往后读取 chunk_size 大小的文件内容，不必等待任何换行符出现。
 '''


def chunked_file_reader(fp, fsize=10 * 8):
    for i in itertools.count(1):
        print i
        chun = fp.read(fsize)
        if not chun: break
        yield chun


def count_abc3(fname):
    count = 0
    with open(fname) as fp:
        for chunk in chunked_file_reader(fp):
            count += chunk.count('w')
    return count


def count_abc2():
    '''
    计算文件里包含多少个数字 '9'，每次读取 8kb
    '''
    count1 = 0
    block_size = 10 * 8
    with open('abc.txt') as fp:
        # while True:
        for i in itertools.count(1):
            print i
            chun = fp.read(block_size)
            if not chun:
                break
            count1 += chun.count('w')
    return count1


print count_abc3('abc.txt')
