# -*- codeing = utf-8 -*-
# @Time : 2022/4/4 20:41
# @Author : yolo
# @File : 2022.4.4.选择数据.py
# @Software: PyCharm
import pandas as pd
import numpy as np

dates=pd.date_range('20130101',periods=6)
df=pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['a','b','c','d'])
print(df)
print(df.a)
print(df[0:3],df['20120102':'20130104'])
print(df.loc['20130102'])
print(df.loc['20130102',['a','b']])


print(df.iloc[3,1])
print(df.ix[:3,['a','c']])
print(df[df.A>8])