# -*- coding: utf-8 -*-
# @Time    : 2020-02-07 13:05
# @Author  : Arrow and Bullet
# @FileName: phonenumber.py
# @Software: PyCharm
import random
# 自动生成电话号码

def random_phone():
    list = ['131', '132', '135', '156', '157', '158', '187', '189', '181', '187']
    shou = random.choice(list)
    str = "0123456789"
    haom = ''
    haom1 = []
    for i in range(8):
        haom1.append(random.choice(str))
        haom = ''.join(haom1)

    number=shou+haom
    return number

for i in range(30):
    print(random_phone())

