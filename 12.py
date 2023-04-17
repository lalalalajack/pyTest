'''
Author: cwj
Date: 2023-04-17 23:16:44
LastEditors: cwj
LastEditTime: 2023-04-17 23:16:56
Introduce: 
'''
#针对以下布尔数据集(已用一个“test12.xlsx”表格来存取，直接读取即可，字段名称为A、B、C，“#”号非表格数据):
#   A    B    C
#   1    1    0
#   0    1    1
#   1    0    0
#   1    1    1
#   1    1    1
#   1    0    0
#   1    1    1
#   0    1    1
#   1    0    0
#   1    1    1
#   1    1    0
#   1    1    1
#   1    1    0
##请编程计算规则“A->B”和“A,B->C”的支持度和置信度，分别用sp1和co1,sp2和co2来表示
def return_values():
    import pandas as pd
    data=pd.read_excel('test12.xlsx')
    I1=data['A'].values==1
    I2=data['B'].values==1
    I3=data['C'].values==1
    sp1=len(data.iloc[I1&I2,:])/len(data['A'])#A->B的支持度
    co1=len(data.iloc[I1&I2,:])/len(data.iloc[I1,:])#A->B的置信度
    sp2=len(data.iloc[I1&I2&I3,:])/len(data['A'])#A,B->C的支持度
    co2=len(data.iloc[I1&I2&I3,:])/len(data.iloc[I1&I2,:])#A,B->C的置信度
    return (sp1,co1,sp2,co2) 
