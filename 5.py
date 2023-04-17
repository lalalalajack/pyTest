'''
Author: cwj
Date: 2023-04-17 23:14:55
LastEditors: cwj
LastEditTime: 2023-04-17 23:15:07
Introduce: 
'''
#********** Begin **********#
#在上一关基础，对经过缺失值填充、数值变量标准化后的数据集，取前600条记录作为训练数据，后90条记录作为测试数据
#构建神经网络分类模型，返回计算结果模型准确率rv和预测准确率r
def return_values():
    import numpy as np
    from sklearn.exceptions import ConvergenceWarning
    from sklearn.neural_network import MLPClassifier
    import warnings
    
    # 忽略收敛警告
    warnings.filterwarnings("ignore", category=ConvergenceWarning)
    
    X1 = np.load('X1.npy') # 经过缺失值填充、数值变量标准化后的数据集，numpy数组690*15
    Y = np.load('Y.npy')   # 因变量，numpy数组，690个元素
    x = X1[:600, :]
    y = Y[:600]
    x1 = X1[600:, :]
    y1 = Y[600:]
    
    clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5,2), random_state=1, max_iter=10000)
    clf.fit(x, y)
    
    rv = clf.score(x, y)
    R1 = clf.predict(x1)
    Z = R1 - y1
    r = len(Z[Z == 0]) / len(Z)
    
    return(rv, r)


#********** End **********#

