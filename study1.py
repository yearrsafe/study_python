#建议调试程序时，先把不需要的代码注释掉，然后逐步解除注释，逐步调试。
#coding=utf-8


#pandas：数据读取，清洗，分析，统计，输出，可视化
"""
Pandas包括Series和DataFrame
    Series是一维，索引方式为单索引，数据存储是同质化数据类型，类似于Excel的单列，创建方式为pd.Series([1,2,3],index=['a','b','c'],name='')
    DataFrame是二维，索引方式为行索引+列名，各列可以存储不同的数据类型，类似于整张表格，创建方式为pd.DateFrame({'col':[1,2,3]})



Series的创建：
    pd.Series([1,2,3],index=['a','b','c'],name='')

Series的属性：
    index:Series的索引对象
    values:Series的值
    dtype或dtypes：元素的数据类型
    shape:Series的形状
    ndim:Series的维度
    size:Series的元素个数
    name:Series的名称
    loc[]:显示索引，根据标签索引或切片
    iloc[]:隐式索引，按位置索引或切片
    at[]:使用标签访问单个元素
    iat[]:使用位置访问单个元素


Series访问数据：
    直接访问：s[0]   ->不推荐
    标签访问：s["a"]
    条件访问:s[s<5]
    访问前n行数据：s.head(n)[['name1','name2']]           如果n为空，则默认为5      name1，name2是访问的具体的列名
    访问末尾n行数据：s.tail(n)


Series的常用方法：
    isin():判断元素是否在参数集合中
    isna()：判断是否为缺失值
    sum()：求和，自动忽略缺失值
    mean()：平均值
    min()：最小值
    max():最大值
    var():方差
    std():标准差
    median():中位数
    mode():众数，可能会返回多个
    quantile(q):分位数，q取0-1之间
    describe():常见统计信息（count,mean,std,min,25%,50%,75%,max)
    value_counts():每个唯一值的出现次数
    count():非缺失值数量
    nunique():唯一值个数（去重）
    unique():获取去重后的值数组
    drop_duplicates():去除重复项
    sample():随机抽样
    sort_index():按索引排序
    sort_value():按值排序
    replace():替换值
    keys():返回Series的索引对象



"""



"""
DataFrame的创建:
    通过series创建：s1=pd.Series([1,2,3])
                  s2=pd.Series([4,5,6])
                  df=pd.DataFrame({"第一列":s1,"第二列":s2})
    通过字典进行创建：
    df=pd.DataFrame(
    {
    "id":[1,2,3,4,5]
    "name":['a','b','c','d','e']
    "age":[12,13,14,15,16]
    "score":[10.0,56.2,80,42.5,99.6]
    }
    index=[1,2,3,4,5],
    columns=["id","name","age","score"],                columns参数顺序决定了表格列的顺序，可以通过改变columns的参数顺序进行修改列的顺序
    )  
    

DataFrame的属性:
    index:DataFrame的行索引
    values:DataFrame的值
    dtypes:DataFrame的数据类型
    shape:DataFrame的形状
    ndim:维度
    size:元素个数
    columns:DataFrame的列标签
    loc[r1:r2,c1:c2]:显式索引，按行标签索引或切片,返回r1到r2行标签，c1到c2列标签的数据
    iloc[]：隐式索引，按行列位置索引或切片
    at[index1,index2]:使用行列标签访问单个元素  index1代表行标签，index2代表列标签
    iat[r1,c1]:使用行列位置访问单个元素
    T:行列转置

访问DataFrame的数据：
    获取某列：df.[列名]/df.列名        获取df的对应列名的单列数据
    获取多列数据：df.[[c1,c2]]        获取c1和c2列数据,c1和c2是列名
    数据筛选(布尔索引)：df.[条件]               例如：df.[df.score>70] 
    随机抽样：df.sample(n)           随机取n条数据，空为1
    

DataFrame的方法：            
    head(n)：查看前n行数据
    tail(n):查看后n行数据
    isin():判断元素是否在参数集合中     会查找所有元素进行匹配，返回一个布尔的多维数组
    isna()：判断是否为缺失值           
    sum()：求和，自动忽略缺失值         一般是取单独一列出来进行求和，例如：df['score'].sum()或者df.score.sum()
    mean()：平均值                      
    min()：最小值
    max():最大值
    var():方差
    std():标准差
    median():中位数
    mode():众数，可能会返回多个
    quantile(q):分位数，q取0-1之间
    describe():常见统计信息（count,mean,std,min,25%,50%,75%,max)
    value_counts():每个唯一值的出现次数
    count():非缺失值数量
    duplicated(subset=[列名]):判断某一列是否重复          返回布尔值
    drop_duplicates():去除重复项
    sample():随机抽样
    sort_index(ascending=?):按索引排序               若？为True，则为升序，False为降序
    sort_value(by=列名):按值排序                      按该列名的大小排序；例如：df.sort_values(by=['score','age'],ascending=[False,True])
    replace():替换值
    nlargest(n,columns=列名):返回某列最大的N条数据          例：df.nlargest(2,columns=['score','age'])
    nsmallest(n):返回某列最小的n条数据
    







"""