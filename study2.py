#数据分析的完整流程

"""
数据收集->数据清洗->数据分析->数据可视化
"""


"""
数据导入：
    pd.read_?('路径')         ?代表数据原存入的文档类型，路径为软路径
数据导出：
    df.to_?('路径')           ?代表数据原存入的文档类型，路径为软路径
    
json文件的数据导入:
    导入json库打开json文件，再将数据加载，最后将数据加载到DataFrame中
    例如：
        import json
        with open('data/test.json') as f:      
            data = json.load(f)
        print(type(data))               //此时，data的数据类型为字典
        df=pd.DataFrame(data['users'])      
        print(df)
"""


"""
数据缺失值的处理：
    缺失值：np.nan,None,pd.NA
检查是否是缺失值：Series:s.isna()或s.isnull()
              DataFrame:df.isna()或df.isnull()  
查看缺失值个数：
    Series:s.isna().sum()       默认的返回数值是按列的求和，如果按行计算的话需要改为sum(axis=1)
    DataFrame:df.isna().sum()       
删除缺失值： 
    Series:s.dropna()    
    DataFrame:df.dropna()       如果存在缺失值，会直接删除整行数据；
              df.dropna(how='all')      当所有数据均为缺失值才删除整行
              df.dropna(thresh=n)       当有至少n个不是缺失值时，保留
              df.dropna(subset=['列名'])      只检查对应多列名是否有缺失值，如果有，删除改缺失值所对应的整行数据
    将dropna()改为dropna(axis=1)       剔除整列的数据
    
    
填充缺失值：
    df.fillna({'列名':value,'name2':value})       用字典填充
    df.fillna(df[[name1,name2]].method)         用统计值填充，其中method代表某一个算数方法
    df.ffill()           使用前面的相邻值填充
    df.bfill()           用后面的相邻值填充
    
去除重复值：
    df.drop_duplicates(subset=['列名'，'列名'], inplace=?,keep=?)        inplace默认为False，修改为True会返回新的修改后的df对象
                                                                       keep的意思为保留，当值为'last'时，会保留位置靠后的相同项
                                                                       


数据类型的转换：
    查看数据类型：df.types
    转换数据类型：df['列名'].astype('数据类型名')         将列名的数据类型修改为后面的数据类型
    如果存在多个数据且数据种类较少，可以将数据类型修改为‘分类’，查看数据时只输出种类：df['列名'].astype('category')
        例如存在男女性别，使用category就会只输出男女性
"""


"""
数据变形：
    df.T        行列转置
    pd.melt(目标df变量名,id_vars=['列名1'，'列名2'],var_name=['变化后的列名']，value_name='变化列名对应数值的新列名')       宽表转长表
                        其中，id_vars参数是不变的列名，var_name是变化的列名,value_name是变化列名的数值所对应的新的列名        四个参数中，第一个是目标数据，剩下的对象都是列名
                        
    pd.pivot(目标df变量名,index=['name1','name2'],columns='name3',values='name4')        index是不变列的列名，columns是新增列的列名，values是新增列的数值的列名
    
    
    分列：df['name1'].str.split("X",expand=?)      其中，name1是原有数据目标列名，str将其作为字符串对象，X代表分割标志，expand的值为布尔值，True是分为多列
                                                  这个方法会返回分裂后的dataframe表格，需要接收
"""


"""
数据分箱：pd.cut(x,bins=n,labels)
    x是需要分箱的对象,一般是表格中的一列数据；bins是分箱的区间；labels是一个列表，用于指定分箱区间的名字
    n代表区间的数量，2就是分为两个区间,划分依据是端点值近似为最值，每个区间内的最大值和最小值的差约相等
    

数据分箱后统计：
    pd.cut(x,bins=n,labels=labels).value_counts()      统计每个区间内的对象的数量
    
自定义区间的数据分析：
    pd.cut(x,bins=[n1,n2,n3,n4],labels=['name1'],['name2'],['name3'])
    该方法会返回序号所对应的labels值，需要在原df中新开一列进行接收
    

等频率分割：将人数进行平均分
    pd.qcut(x,n)    其中,n是每个区间的人数
    
数据统计流程：
    字符串数据类型->类别型数据类型->统计
    数值型->数据分箱->统计
    
    
    
重置/修改列名与索引名：
    df.rename(columns={'name0':'name1'},index={'name2':'name3'})                          修改列名或索引名，将name0修改为name1(列名）,index是索引名
    df.set_index('列名',inplace=?)        修改索引，将对应列的数值作为索引；inplace的值为布尔值，True会在原来的df上进行修改
    df.reset_index(inplace=?)            上个方法的反操作
    df.index=[name1,name2,name3]         修改索引名，需要写全索引(适用于索引的全部修改)
    df.columns=[name1,name2,name3]       修改列名
           

"""


'''
时间数据的处理：
    时间戳：d=pd.Timestamp('y-m-d h-m-s')   数据类型为Timestamp
    取年月日时分秒：d.year/d.month/d.day/d.hour/d.minute/d.second
    取季度：d.quarter
    是否为月初/月末/年初/年末/季度初/季度末..:d.is_month_start/d.is_month_end/d.is_quarter_start/d.is_quarter_end
    判断周几：d.day_name()
    转换为天/季度/年度/月份/周：d.to_period('D')/d.to_period('Q')/d.to_period('Y')/d.to_period('M')/d.to_period('W')
        周维度会返回该周的时间跨度
        
    字符串转换为时间类型：pd.to_datetime('str')
    DataFrame转换为时间类型：df['列名']=pd.to_datetime('str')
            需要注意的是，在dataframe中使用时间类的方法时，要在中间加个dt；例如：df['week']=df['datetime'].dt.day_name()
            
            
    csv中的日期转换：df=pd.read_csv('文件路径',parse_dates=['列名']) 将列名中的数据转换为时间类型
    
    日期数据作为索引：df.set_index('时间类列名',inplace=?)    
    
    
时间间隔：
    两个时间戳相减，数据类型为Timedelta
    利用时间间隔切片：df.loc['时间间隔1':"时间间隔2"]    
时间序列：
    pd.date_range('时间戳1'，'时间戳2'，freq='W/D/Y')   计算两个时间戳之内的时间，freq代表取值单位  
    pd.date_range('时间戳1',periods=n,freq='W/D/YE(YS)')    从时间戳1取n个数据(YE代表从时间戳往前取，YS代表从时间戳往后取)
    
    
重新采样：
    df[['name1','name2']].resample('YE/YS/ME/MS...').method()
        name1、2代表所要查看的列；resample方法能够将之前采样的数据用新的维度进行输出;method是某一个数学方法，代表新维度的方法输出

'''



'''
分组聚合：
    df.groupby('分组的列名')['聚合的字段'].聚合函数()
    df.groupby().groups         查看所有的分组
    df.groupby().get_groups('分组名')       查看具体的某个分组数据
    
    根据多个列名进行分组：df.groupby(['列名1','列名2'])
    
    

精度控制：
    数学方法().round(2)         保留两位小数
    df['列名']=df['列名'].round(2)      保留两位小数
    


'''