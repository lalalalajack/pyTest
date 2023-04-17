'''
Author: cwj
Date: 2023-04-17 23:15:23
LastEditors: cwj
LastEditTime: 2023-04-17 23:15:39
Introduce: 
'''
# -*- coding: utf-8 -*-
#基于上一关的数据集，构建神经网络回归模型，返回计算结果模型准确率r，
#并针对测试数据AT=28.4、V=50.6、AP=1011.9、RH=80.54，预测其PE值。
def return_values():
    import pandas as pd
    data = pd.read_excel('发电场数据.xlsx')
    x=data.iloc[:,:4].values
    y=data.iloc[:,4].values
    from sklearn.neural_network import MLPRegressor
    clf = MLPRegressor(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=8, random_state=1)
    clf.fit(x,y)
    r=clf.score(x,y)
    import numpy as np
    x1=np.array([28.4,50.6,1011.9,80.54])
    x1=x1.reshape(1,4)
    PE=clf.predict(x1)
    return(r,PE)