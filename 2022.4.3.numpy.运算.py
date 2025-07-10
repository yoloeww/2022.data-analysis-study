# -*- codeing = utf-8 -*-
# @Time : 2022/4/3 22:09
# @Author : yolo
# @File : 2022.4.3.numpy.运算.py
# @Software: PyCharm
import numpy as np
a=np.array([10,20,30,40])
b=np.arange(4)
print(a,b)
c=b**2
print(c)
c=10*np.sin(a)
print(c)
# 新的功能
print(b)
print(b<3)
print(b==3)
a=np.array([[1,1],[2,3]])
print(a)
b=np.arange(4).reshape((2,2))
c=a*b
c_dot=np.dot(a,b)
print(c)
print(c_dot) #矩阵运算dot
