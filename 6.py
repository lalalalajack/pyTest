'''
Author: cwj
Date: 2023-04-17 23:15:09
LastEditors: cwj
LastEditTime: 2023-04-17 23:15:20
Introduce: 
'''
#**********Begin**********#
#在发电场中电力输出（PE）与AT（温度）、V（压力）、AP（湿度）、RH（压强）有关，
# 相关测试数据见“发电场数据.xlsx”文件，请完成以下任务：
# 1)求出PE与AT、V、AP、RH之间的线性回归关系式系数向量,用列表b表示，其元素依次为常数项、对应变量系数
# 2)求出回归方程的拟合优度（判定系数），用变量r表示
# 3)今有某次测试数据AT=28.4、V=50.6、AP=1011.9、RH=80.54，试利用构建的线性回归模型预测其PE值
# -*- coding: utf-8 -*-
def return_values():
    import pandas as pd
    data=pd.read_excel('发电场数据.xlsx')
    x=data.iloc[:,0:4].values
    y=data.iloc[:,4].values
    from sklearn.linear_model import LinearRegression as LR
    lr=LR()
    lr.fit(x,y)
    r=lr.score(x,y)
    c_x=lr.coef_
    c_b=lr.intercept_
    b=[c_b,c_x[0],c_x[1],c_x[2],c_x[3]]
    import numpy as np
    x1=np.array([28.4,50.6,1011.9,80.54])
    x1=x1.reshape(1,4)
    PE=lr.predict(x1)
    return(b,r,PE)

#**********End**********#

