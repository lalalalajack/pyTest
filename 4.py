'''
Author: cwj
Date: 2023-04-17 23:14:41
LastEditors: cwj
LastEditTime: 2023-04-17 23:14:53
Introduce: 
'''
#********** Begin **********#
#在上一关基础，对经过缺失值填充、数值变量标准化后的数据集，取前600条记录作为训练数据，后90条记录作为测试数据
#构逻辑回归模型，返回计算结果模型准确率rv和预测准确率r
def return_values():
    import numpy as np
    from sklearn.linear_model import LogisticRegression as LR
    
    # Load data
    X1 = np.load('X1.npy') # Preprocessed data (690*15 numpy array)
    Y = np.load('Y.npy')   # Target variable (690-element numpy array)
    
    # Split data into train and test sets
    x_train = X1[:600,:]
    y_train = Y[:600]
    x_test = X1[600:,:]
    y_test = Y[600:]
    
    # Create and fit logistic regression model
    lr = LR(max_iter=10000) # Increase the maximum number of iterations
    lr.fit(x_train, y_train)
    
    # Compute model accuracy on the train set
    train_accuracy = lr.score(x_train, y_train)
    
    # Compute model accuracy and error rate on the test set
    test_accuracy = lr.score(x_test, y_test)
    test_predictions = lr.predict(x_test)
    test_error_rate = 1 - (test_predictions == y_test).mean()
    
    return train_accuracy, test_accuracy, test_error_rate


#********** End **********#

