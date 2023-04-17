'''
Author: cwj
Date: 2023-04-17 23:14:14
LastEditors: cwj
LastEditTime: 2023-04-17 23:14:25
Introduce: 
'''
#********** Begin **********#
#在上一关基础，对经过缺失值填充、数值变量标准化后的数据集，取前600条记录作为训练数据，后90条记录作为测试数据
#构建支持向量机模型，返回计算结果模型准确率rv和预测准确率r
# -*- coding: utf-8 -*-
def return_values():
    import numpy as np
    X1=np.load('X1.npy')
    Y=np.load('Y.npy')
    x_train=X1[:600,:]
    y_train=Y[:600]
    x_test=X1[600:,:]
    y0=Y[600:]
    from sklearn import svm
    clf = svm.SVC()  
    clf.fit(x_train, y_train) 
    rv=clf.score(x_train, y_train);
    R=clf.predict(x_test)
    z=y0-R
    t=z[z==0]
    r=len(t)/len(z)
    return (rv,r)

#********** End **********#
