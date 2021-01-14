#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021-01-14 14:56
# @Author : chentuliu
# @Email : chentuliu@126.com
# @File : 根据出生日期判断星座.py
# @Project : Python-100-example
'''
实例描述：
    两千多年前希腊的天文学家希巴克斯为标识太阳在黄道上运行的位置，将黄道分为十二个区段，依次为
白羊、金牛、双子、巨蟹、狮子、处女、天秤、射手、摩羯、水平、双鱼是十二个星群。在地球运转到每个
星群所占时段出生的婴儿，也就对应了相应的星座

核心技术：
    星座判断程序的关键是简历星座、星座符号、与日期对应的列表，然后根据输入的日期对应列表中的对应关系
计算属于哪个星座。
'''

sdate = [20, 19, 21, 20, 21, 22, 23, 23, 23, 24, 23, 22]  # 星座判断列表
conts = ['摩羯座', '水瓶座', '双鱼座', '白羊座', '金牛座', '双子座', '巨蟹座', '狮子座', '处女座', '天秤座', '天蝎座', '射手座', '摩羯座']
signs = ['♑', '♒', '♓', '♈', '♉', '♊', '♋', '♌', '♍', '♎', '♏', '♐', '♑']
type=['务实本分']

# 输入生日，输出星座
birth = input('请输入你的出生年月日，格式为2001-02-21或2001-2-21\n').strip(' ')  # str.strip(' ') 去除开头和结尾的空格
cbir = birth.split('-')  # 分隔年、月、日到列表
cmonth = str(cbir[1])  # 提取月数据
cdate = str(cbir[2])  # 提取日数据


# 判断星座函数
def sign(cmonth, cdate):
    if int(cdate) < sdate[int(cmonth) - 1]:  # 如果日数据早于对应月列表中对应的日期
        print(conts[int(cmonth) - 1])  # 直接输出星座列表对应月对应的星座名称
        print(signs[int(cmonth) - 1])  # 直接输出星座列表对应月对应的星座符号
    else:
        print(conts[int(cmonth)])  # 否则输出星座列表下一月对应的星座名称
        print(signs[int(cmonth)])  # 否则输出星座列表下一个对应的星座符号


sign(cmonth, cdate)
