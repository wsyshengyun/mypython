# -*- encoding: utf-8 -*-
'''
@File    :   csvtest.py
@Time    :   2020/02/20 17:00:45
'''


import csv  
data = ['a', 'b','c']
datau=  ['你好', '再见', '不好']
data_o= ['不是吧', 'h', '没有', '==']
data_num = ['1', '333', '555']


file_path = 'BasePython\\testcsv.csv'

# 写测试
def write_test():
    with open(file_path, 'a+', newline='', encoding='utf8') as fp:
        writer = csv.writer(fp)
        writer.writerow(data)
        writer.writerows([datau, data_o, data_num])
        print('write successful~')

# write_test()

# 读测试
def read_test():
    with open(file_path, 'r', encoding='utf-8') as fp:
        reader = csv.reader(fp)
        for row in reader:
            print(','.join(row))

read_test() 
    




    


