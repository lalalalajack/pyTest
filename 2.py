'''
Author: cwj
Date: 2023-04-17 23:13:59
LastEditors: cwj
LastEditTime: 2023-04-17 23:14:11
Introduce: 
'''
#在上一关的基础上，对自变量X中的数值变量（x1~x6）作均值-方差标准化处理
# 需要注意的是x7~x15名义变量不需要作标准化处理
# 返回结果X1
def return_values():
    import numpy as np
    X=np.load('X.npy')
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    scaler.fit(X[:,:6]) 
    X_1=scaler.transform(X[:,:6])
    X1=np.hstack((X_1,X[:,6:]))
    return X1


#********** End **********#

