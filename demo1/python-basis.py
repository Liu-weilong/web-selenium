#!/usr/bin/python
# -*- coding: UTF-8 -*-
# def
import keyword
import sys
import mysql.connector
import pymysql
import requests
import re
import csv
#import python-practice


'''

Python 教程笔记

'''

#print(python-practice.rot)
#换行操作  \是程序里面的换行操作  \n是输出程序的换行操作
print("你好这是一个简单的测试的一段话，但是\n我要换行操作。")
print(round(10.658,2)) #四舍五入   保留两位小数
print(abs(-98.5)) #绝对值取整

#字符串的链接
d = 'a '+ 'b'
print(d)

#字符串的取值
arr3 = 'python'
print(arr3[0:5])
print(arr3[-2])

#字符串函数
#strip()去除空格  lstrip() 去除左边的空格  rstrip() 去除右边的空格
ad = 'nihao    '
print(ad.strip())
print(ad.strip('n'))

#startswith('参数') 判断以什么为开头   endswith('参数')判断以什么为结尾    结果为TRUE或FALSE
canshu1 = 'apple'.startswith('a')
canshu2 = 'apple'.endswith('d')
print(canshu1)
print(canshu2)

#replace(‘老的’，‘新的’)字符串替换
#len() 返回字符串的长度  count('canshu')查找字符串出现的次数  upper()字符串小写字符转化为大写
#lower() 字符串大写字母转为小写
canshu3 = 'banana'.replace('a','刘伟龙')
print(canshu3)
canshu4 = len('apple')
print(canshu4)
canshu5 = 'apple'.count('p')
print(canshu5)
canshu6 = 'apple'.upper()
print(canshu6)
canshu7 = 'APPle'.lower()
print(canshu7)
canshu8 = 'apple'.center(7,'/')  #返回以/来补充
print(canshu8)

#python数字类型 整型（int）浮点型（float）复数（complex）布尔型（bool）
#type（）查看数字的类型
print(type(10))
print(type(5.296))
#布尔类型是判断条件是否成立的 只有TRUE或FALSE两种返回值
#当布尔类型为0 none 空值的时候 布尔返回类型为FALSE

#python列表和操作
arr4 = ['1','2','3','4','5'] #* 2 #支持相加和相乘操作
arr4.append('9')
print(arr4)
arr4.extend(['8','9'])
arr4.remove('9')
arr4.reverse()
arr4.sort(reverse=True)
print(arr4)
#arr4.count('1') #统计1出现的次数 不存在返回0
#arr4.append('w') #向列表尾部追加w
#arr4.extend('d') #向列表尾部追加一个列表
#arr4.index('a') #返回参数a在列表中的序号 不存在报错
#arr4.insert(3,'s') #向列表指定位置插入数据(3表示位置)
#arr4.pop('d') #默认删除列表中的尾部成员 并返回删除的成员
#arr4.remove('d') #删除列表中指定成员 不存在报错
#arr4.reverse() #将列表的成员顺序颠倒
#arr4.sort() #将列表中的成员排序

#python元祖及其操作
#元祖的基本形式是（）括号 他是一种特殊的列表  里面的元素是不可变的
arr5 = (85,6.5,9) #空元祖
print(arr5[1])
print(arr5)
print(len(arr5)) #返回元祖的数量
print(max(arr5)) #返回元祖的最大值
print(min(arr5)) #返回元祖的最小值

#python字典及其操作
#字典是python常用的数据类型成员以键值对的形式存在
#基本格式：{}大括号的数据集合
#字典是无序的是通过键值对访问成员
#字典的键值是不可变的 键值最好是唯一 如果同一个键值被赋值多次 最后一个值会被记住
arr6 = {'name':'刘伟龙','apple':'测试','age':'27'}
arr6['tud'] = '数据信息' #这是添加字典数据
arr6['apple'] = '测试修改信息' #这是字典的修改数据
print(arr6)
print(arr6['name'])
del arr6['name'] #删除字典指定成员
#arr6.clear() #清空字典的所有成员
arr6.copy() #复制字典
#arr6.get('apple',default=None) #获取key对应的值
#arr6.pop('a',default=None) #删除字典指定的值 不存在返回default
arr6.update({'ceshi':'89'}) #更新字典  没有则创建
print(arr6)

#python Set集合类型
#集合是一个无序的不重复的数据集合
#与字典比较类似都是无序的数据集合 字典通过键值访问成员 集合无法通过键值访问
#可以使用大括号{}或者set()函数创建集合
arr7 = set()
arr8 = {1,1,2,3,4,5,6,7,8,9,0}
arr9 = {5,6}
print(arr7)
print(len(arr8)) #求出集合的长度
print(arr8 - arr9) #q求出集合的差集
print(arr8 & arr9) #求出集合的交集
print(arr8 | arr9) #求出集合的并集

#pytohn变量  是存储在电脑内存中的值
#常见的运算符 算数运算符 赋值运算符 比较运算符 逻辑运算符 成员运算符 身份运算符 位运算符
c = 1 + 3
print(c)
d = 7==6
print(d)
#算数 + — * /
#赋值 = += -+ *= /+
#比较 == != > < <= >=
#逻辑  and  or not
#c成员运算符  in   not in
#身份运算符  is  is not

#python  循环控制语句语法
a = 2
b = 3
if(a == b):
    print('执行这个操作')
print('没有执行这个操作')
if(a < b):
    print('执行这个语句')
#print("没有执行")
ages = 89
if(ages > 80):
    print('第一步操作')
else:
    print('第二部操作')
wea = 'nihao'
#wea = int(wea)
if(wea == 1):
    print('这是1')
elif(wea == 2):
    print('这是2')
elif(wea == 3):
    print('这是3')
else:
    print('请输入1--3的数字')

#for循环/while循环
words = 'I am lenmmo'
word = ['fuit','orange','bannan','apple']
for w in words:
    print(w,end='')

for i in word:
    print(i)

for e in range(0,5):
    print(e)

arr10 = ['测试1','测试2','测试3','测试4','测试5','测试6','测试7','测试8']
for d in arr10:
    if(d == '测试4'):
        #continue 跳过循环
        break #停止循环
    print(d)

a=0
while a<5:
    print(a)
    a = a+1
else:
    print('结束')


#python函数的特点

def test():
    print('函数测试')
test()

def add(x,y):
    result = x + y
    return result
print(add(2,5))

def test1(apple,lenmo=2):
    print('调用')
test1(4,7)

def test2(name,age,sex='male',nation='china'):
    print('名字：'+ str(name))
    print('年龄：' + str(age) + '岁')
    print('性别：' + str(sex))
    print('国家：' + str(nation))
test2('liuweilong1',26)
test2('liuweilong2',78,sex='falme',nation='美国')

#变量的引用
leng = 19
def test3():
    #leng = 12
    print(leng)
test3()
# global 声明为全局变量

#return 的用法  大多数情况下用return会跳出这个语句   支持返回多个结果但是要写在同一行上
def test4():
    s = 1
    return s
    print('ddd')
print(test4())

#python面向对象的知识点
#封装性 继承性 多态性
class Man():
    height = 172

    def think(self):
        print('实验')

    def sep(self):
        print('实验2')

    @staticmethod
    def jin():
        print('静态方法 与类对象没有太大关系的时候 可以使用该方法')

    def __siyou(self):#这是私有方法 在方法名前面加上两个下划线
        __weight = 65 #('这是私有属性  是不能访问的 也是在属性前面加上两个下划线')
        print('这是私有方法 在方法名前面加上两个下划线')

class Wman(Man):#这样就直接继承了Man的属性和方法
    print('类得继承性')

arr11 = Man()
arr12 = Wman()
d = arr11.think()
e = arr12.sep()
#__init__构造函数  可以初始化对象的特征  在实例化的类的时候自动调用这个函数
#public 公开性 外部可以访问相关的变量和方法
#private 私有性 外部不可访问相关的变量和方法


#python的正则表达式
arr13 = 'abc | asc | avc | axc | sdc'
#re.findall('abc',arr12)
#常见的元字符 数字字符
# \d匹配一个数字字符  \D匹配一个非数字字符
#单词字符
# \w匹配一个包括下划线的单词字符  \W匹配一个非包括下划线的单词字符
#空白字符
# \s匹配一个空白字符 如空格 制表符 换页符 \S匹配一个非空白字符
#贪婪是倾向于最大长度的匹配  非贪婪倾向于最小长度的匹配
#次数匹配
# *代表匹配前面的字符零次或多次  {0，}
# +代表匹配前面的字符一次或多次  {1，}
# ？代表匹配前面的字符零次或一次 {0,1}
#re.match() 从字符串首字母开始匹配 若首字符不匹配则返回none 若匹配则返回第一个匹配对象
#re.search() 搜索整个字符串 若全部不匹配 则返回none 若匹配则返回第一个匹配对象

#__init__.py文件特点 1.声明一个文件夹为一个包 2.import包 3.该模块名为一个包名 4.自定义哪些包可以导入
#__name__的应用


#con = input('请输入')
#print('你输入的是'+ str(con))

#这是文本文档的读   ctrl+/ 多行注释
with open("D:/pycharm/demo1/test.txt",'r',encoding ='utf-8') as data:
    arr13 = data.read()
print(arr13)

#这是csv文档的读
csvrt = csv.reader(open('D:/pycharm/demo1/intet.csv','r',encoding='utf-8'))
for ayt in csvrt:
    print(ayt)

#进程：计算机中程序关于数据集合上的一次运行活动，是系统进行资源分配和调度的基本单位
#线程：是程序执行的最小单元，是进程中的一个实体是被系统独立调度和分派的基本单位，一个进程可以包含多个线程
#但是线程不能包含多个进程，线程自己不拥有系统资源，在单个程序中同时运行多个线程完成不同的工作 称为多线程







