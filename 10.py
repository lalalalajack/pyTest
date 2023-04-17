#********** Begin **********#
#读取“农村居民人均可支配收入来源2016.xlsx”数据表，数据来源于2016年《中国统计年鉴》，
# 首先，对指标数据作均值-方差标准化处理，注意首列为地区名称，不用标准化
# 其次，对标准化后的指标数据，作K-均值聚类分析（K=4），
# 最后，给出聚类分析结果，用一个序列Fs来表示，其中index为地区名称，值为所属类别的标签值（0、1、2、3）。
def return_values():
    import pandas as pd
    data=pd.read_excel('农村居民人均可支配收入来源2016.xlsx')
    X=data.iloc[:,1:]
    from sklearn.preprocessing import StandardScaler  
    scaler = StandardScaler()
    scaler.fit(X) 
    X=scaler.transform(X) 
    from sklearn.cluster import KMeans   
    model = KMeans(n_clusters = 4, random_state=0, max_iter = 500) 
    model.fit(X) 
    c=model.labels_
    Fs=pd.Series(c,index=data['地区'])
    Fs=Fs.sort_values(ascending=True)
    return Fs
#********** End **********#

