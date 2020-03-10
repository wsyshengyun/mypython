# -*- coding: utf-8 -*-
'''
@File    :   jisuanDate.py
@Time    :   2020/03/02 11:10:23
'''

import datetime as dt

tsr = "2020-03-02 11:03:04"
date, time = tsr.split(' ')
date_list = map(lambda x: int(x), date.split('-'))
time_list = map(lambda x:int(x),time.split(':'))
temobj = dt.datetime(*date_list, *time_list)
print(temobj.date())

for _ in range(6):
    delatt = 90
    delattrObj = dt.timedelta(delatt)
    newdt = temobj-delattrObj
    print(newdt.date())
    temobj = newdt
