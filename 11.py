'''
Author: cwj
Date: 2023-04-17 23:16:24
LastEditors: cwj
LastEditTime: 2023-04-17 23:16:43
Introduce: 
'''
#********** Begin **********#
##将以下超市的购买记录（已用一个"超市购买记录.txt"来存放，读取该文件即可）
##注意：文件内容存放与下列展示一致，即顿号分隔，“##”号不是文件内容，文件编码为utf-8）：
##  I1、西红柿、排骨、鸡蛋、毛巾、水果刀、苹果
##  I2、西红柿、茄子、水果刀、香蕉
##  I3、鸡蛋、袜子、毛巾、肥皂、苹果、水果刀
##  I4、西红柿、排骨、茄子、毛巾、水果刀
##  I5、西红柿、排骨、酸奶、苹果
##  I6、鸡蛋、茄子、酸奶、肥皂、苹果、香蕉
##  I7、排骨、鸡蛋、茄子、水果刀、苹果
##  I8、土豆、鸡蛋、袜子、香蕉、苹果、水果刀
##  I9、西红柿、排骨、鞋子、土豆、香蕉、苹果
## 将其转换为布尔数据集，其中数据集用数据框Data来表示，数据框中的字段名称即为商品名称，如果商品在某个购买记录中出现用1来表示，否则为0
def return_values():
    tiem=['西红柿','排骨','鸡蛋','茄子','袜子','酸奶','土豆','鞋子']
    import pandas as pd
    import numpy as np
    data=pd.read_table('超市购买记录.txt',sep='、',header=None,encoding='utf-8',engine='python')
    data=data.iloc[:,1:]
    D=dict()
    for i in range(len(tiem)):
        z=np.zeros(len(data))
        l=list()
        for k in range(len(data.iloc[0,:])):
            s=data.iloc[:,k]==tiem[i]
            l.extend(list(s[s.values==True].index))
        z[l]=1
        D.setdefault(tiem[i],z)
    Data=pd.DataFrame(D)
    return Data


#********** End **********#

