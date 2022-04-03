# -*- codeing = utf-8 -*-
# @Time : 2022/4/3 21:57
# @Author : yolo
# @File : 2022.4.3.numpy数组.py
# @Software: PyCharm

import numpy as np
a=np.array([2,3,4],dtype=np.int64)
print(a.dtype)
a=np.array([[2,3,4],[2,34,6]]) #二维矩阵
print(a)
a=np.zeros((3,4))#三行四列矩阵
print(a)
a=np.ones((3,4),dtype=np.int16)#三行四列矩阵
print(a)
a=np.empty((3,4))#三行四列矩阵
print(a)
a=np.arange(10,20,2) #步长为2
print(a)
a=np.arange(12).reshape((3,4))
print(a)
a=np.linspace(1,10,20).reshape(4,5) #一段线段
print(a)