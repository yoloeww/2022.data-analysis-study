# -*- codeing = utf-8 -*-
# @Time : 2022/4/4 19:40
# @Author : yolo
# @File : 2022.4.4.矩阵运算2.py
# @Software: PyCharm

import numpy as np
#矩阵乘法
'''
a=np.array([[1,2],[3,4]])
b=np.arange(4).reshape(2,2)
c_dot=np.dot(a,b)
print(c_dot)

a2=np.random.random((2,4)) #随机生成矩阵
print(a2)
#print(np.sum(a2,axis=1))#行找
print(np.min(a2,axis=0))#列找最小
#print(np.max(a2))
'''
A=np.arange(14,2,-1).reshape((3,4))
print(np.argmin(A))
print(np.argmax(A))
print(np.mean(A))#平均值
print(np.median(A))#中位数
print(np.cumsum(A))#累加
print(np.diff(A))#累减
print(np.nonzero(A)) #输出非0行数列数
print(np.sort(A))
print(np.transpose(A))#矩阵转置
print(A.T)#转置
print((A.T).dot(A))
print(np.mean(A,axis=1)) #行
print(A)
print(np.clip(A,5,9))#大5变成9 小于五变成5 别的不变
