# -*- codeing = utf-8 -*-
# @Time : 2022/4/4 20:28
# @Author : yolo
# @File : 2022.4.4.pandas.basic.py
# @Software: PyCharm
import  pandas as pd
import  numpy as np
s=pd.Series([1,3,6,np.nan,44,1])
print(s)
dates=pd.date_range('2022.4.4',periods=6)
df=pd.DataFrame(np.random.randn(6,4),index=dates,columns=['a','b','c','d'])
print(dates)
df1=pd.DataFrame(np.arange(12).reshape(3,4))
print(df1)
df2=pd.DataFrame({'A':1.,'B':pd.Timestamp('20130102'),'C':pd.Series(1,index=list(range(4)),dtype='float32')})
print(df.index)
print(df.columns)
print(df.values)
print(df.describe())#功能
print(df.T)
print(df.sort_index(axis=1,ascending=False))