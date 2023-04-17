#********** Begin **********#
#读取“农村居民人均可支配收入来源2016.xlsx”数据表，其中数据来源于2016年《中国统计年鉴》，
#首先，对指标数据进行均值方差标准化处理
#其次，其次对标准化处理后的指标数据作主成分分析，要求提前累计贡献率在95%以上
#再次，基于提取的主成分计算综合得分，综合得分=提取的各主成分与对应贡献率之和
#最后，基于综合得分获得各地区的排名，得分按从高到低排序，用一个序列Rs来表示，其中index为地区名称，值为综合得分
# -*- coding: utf-8 -*-
def return_values():
    import pandas as pd
    Data=pd.read_excel('农村居民人均可支配收入来源2016.xlsx')
    X=Data.iloc[:,1:]
    # 数据规范化处理
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    scaler.fit(X) 
    X=scaler.transform(X)
    from sklearn.decomposition import PCA
    pca=PCA(n_components=0.95) 
    pca.fit(X)
    Y=pca.transform(X)
    gxl=pca.explained_variance_ratio_ 
    F=gxl[0]*Y[:,0]+gxl[1]*Y[:,1]+gxl[2]*Y[:,2]  #综合得分=各个主成分×贡献率之和
    dq=list(Data['地区'].values)         #提取地区
    Rs=pd.Series(F,index=dq)             #以地区作为index,综合得分为值,构建序列
    Rs=Rs.sort_values(ascending=False) #按综合得分降序进行排序
    return Rs

#********** End **********#

