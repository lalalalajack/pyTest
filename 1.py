#********** Begin **********#
# 读取“银行贷款审批数据.xlsx”表，自变量为x1~x15，决策变量为y（1-同意贷款，0-不同意贷款）
# 其中x1~x6为数值变量，x7~x15为名义变量
# 请对x1~x6中存在的缺失值用均值策略填充，x7~x15用最频繁值策略填充
# 最后返回填充处理后的X（即x1~x15），以及决策变量Y(即y)
def return_values():
    import pandas as pd
    import numpy as np
    from sklearn.impute import SimpleImputer
    
    A=pd.read_excel('银行贷款审批数据.xlsx')
    A1=A.iloc[:,:6]
    A2=A.iloc[:,6:-1]
    
    imp = SimpleImputer(missing_values=np.nan, strategy='mean')
    imp.fit(A1)
    a1_1=imp.transform(A1)
    imp = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
    imp.fit(A2)
    a2_1=imp.transform(A2)

    X=np.hstack((a1_1,a2_1))
    Y=A['y'].values
    
    return(X,Y)



#********** End **********#

