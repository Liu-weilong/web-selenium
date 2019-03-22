#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2018/12/24 15:29
#@Author: liuweilong
#@File  : python_practice.py
import requests

rot = 456987
re = requests.get("https://www.baidu.com/")
print(re)

canshu3 = 'banana'
rea = canshu3.replace('a','实验')
rea1 = len(canshu3)
if(rea1 == 5):
    print('实验成功')
elif(rea1 == 6):
    print('实验失败')
else:
    print('不知道')
print(rea)
print(rea1)

ad = '152 56750385 '
print(ad.strip())

arr1 = 13.568
arr1 = round(arr1,2)
print(arr1)

arr2 = ['测试1','测试2','测试3','测试4','测试5']
print(arr2[0:2])

arr3 = 'python hello world'
print(arr3[0:15])

arr4 = 'banana'
b = arr4.count('a')
a = arr4.startswith('A')
if(a == True):
    print('正确以b开头')
else:
    print('不是以b开头')

if(b == 1):
    print('a出现1次')
elif(b == 2):
    print('出现2次')
elif(b == 3):
    print('出现3次')
elif(b == 4):
    print('出现4次')
else:
    print('不知道出现几次')

arr5 = 'apple'
arr5 = arr5.upper()
print(arr5)

arr6 = 'LIUWEILONG'
arr6 = arr6.lower()
print(arr6)

arr7 = 15.3698
print(type(arr7))

arr8 = ['1','2','3','4','5','6','7']
arr8.append('刘伟龙')
arr8.remove('5')
#arr8.insert('测试')
arr8.pop()
print(arr8)

arr9 = (90,'刘伟龙',78)
print(len(arr9))

arr10 = {'刘伟龙1':'测试1','刘伟龙2':'测试2','刘伟龙3':'测试3','刘伟龙4':'测试4','刘伟龙5':'测试5'}
del arr10['刘伟龙5']
arr10.update({'测试数据':'你好'})
arr10.update({'刘伟龙1':'这是测试的数据信息'})
print(arr10['刘伟龙1'])
print(arr10)

for w in arr10:
    print(w)

for e in range(0,5):
    if(e == 3):
        print('打印是三')
    else:
        print('打印结果不是三')





























