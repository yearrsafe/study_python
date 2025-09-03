#建议调试程序时，先把不需要的代码注释掉，然后逐步解除注释，逐步调试。
#coding=utf-8


#Numpy数组(ndarray)
"""
核心特征：
    多维性：支持0维（标量），1维（向量），2维（矩阵）及更高维
    同质性：所有元素类型必须一致（通过dtype指定）
    高效性：基于连续内存块存储，支持向量化运算


属性：
    shape:数组的形状，返回行数和列数         arr.shape
    ndim:维度数量，返回数组的维度数          arr.ndim
    size:元素个数，返回数组中所有元素的总数  arr.size
    dtype:元素类型，返回数组中元素的数据类型   arr.dtype
    T：转置，行变列，列变行                  arr.T
    itemsize:单个元素占用的内存字节数        arr.itemsize
    nbytes:数组总内存占用量,size*itemsize  arr.nbytes
    flags:内存存储方式，是否连续存储         arr.flags


创建：
    基础构造：手动构造，arr=ad.array(1)       包括手工构造，列表构造，copy构造；copy构造的数组是新数组，本质上是内存地址改变了
    预定义形状填充：用于快速初始化固定形状的数组（例如全1初始化，全0占位等）
        全0方法是zeros((line,p))->构造一个Line行p列的全0数组,如果line或p为空则为默认1，数据类型为float64
        全1方法是ones((line,p))
        全n的方法是full((l,p),n)
        随机生成未初始化生成方法为empty((l,p))
        根据已有数组的arr0的行列数生成全0数组：zeros_like(arr0)
        与之类似的还有ones_like(arr0),empty_like(arr0),full_like(arr0)
    基于数值范围生成：生成数值序列，常用于模拟时间，坐标网格等
    特殊矩阵生成：数学运算专用，如线性代数里的单位矩阵
        矩阵->二维：由行列组成，二行三列代表形状为2*3；
        0矩阵：所有元素都为0；    单位矩阵：从左上右下对角线上为1，其余为0；  对角矩阵：只有对角线上有非0值   对称矩阵：即矩阵转置

        单位矩阵：arr=np.eye(p,c,dtype)  p代表行数，c代表列数，dtype指定数据类型

        对角矩阵：arr=np.diag(arr0)      arr0为一个一维数组，根据arr0生成一个对角矩阵

    随机数组生成：模拟实验数据，初始化神经网络权重等场景
        随机数组的生成(均匀分布)：随机浮点数->生成0-1的浮点数：arr=np.random.rand(r,c)        r是目标数组的行数，c是列数
                                     ->生成其他范围的浮点数：arr=np.random.uniform(min,max,(r,c))     min和max是范围，r,c是形状
                             随机整数->arr=np.random.randint(min,max,(r,c))
        随机数组的生成(正态分布->两边小中间大):arr=np.ramdom.normal(loc,scale,size)    其中，loc为均值，也就是正态分布中最中间的值，默认值为0；scale代表规模，数值越大分布越广，默认值为1；size可以设置为数字或元组，数字代表一维数组，元组代表二维数组
        设置随机种子：rng=np.random.RandomState(num)       a=rng.rand()

    高级构造方法：用文件/字符串等或通过函数生成复杂数组

    数列构造：
    等差数列构造：arange(start,end,subs)       左开右闭，subs代表公差
    等间隔数列：linspace(start,end,num)        闭区间，num代表一共要取多少个数字，其中间隔n的算法为n=(end-start)/(num-1)
    对数间隔数列：arr=np.logspace(start,end,n,base=num)    以num为底的对数，从start开始，end结束，取n个数字；运算过程是先通过linspace计算，再将结果取以num的结果次幂



数据类型：
    布尔类型：bool(True/False)
    整型：int/unint8、16、32、64(8位、16位、32位、64位有符号整数/无符号整数)
    浮点型：float16\32\64   半精度、单精度、双精度浮点数
    复数：complex64\128        用两个32\64位浮点数表示的复数


索引与切片：
    基本索引：通过整数索引直接访问元素，从0开始           arr[num]
    行/列切片：使用冒号，切片语法选择行和列的子集          arr[:]->获取全部数据         arr[min,max]->获取从min到max的数据，左开右闭
    连续切片：从起始索引到结束索引按步长切片
    使用slice函数：通过slice(start,stop,step)进行切片      arr[slice(start,stop,step)]
    布尔索引：通过布尔条件筛选满足条件的元素，支持逻辑运算符    arr[arr>10]

      一维数组：
        基本索引：通过整数索引直接访问元素，从0开始           arr[num]
        行/列切片：使用冒号，切片语法选择行和列的子集          arr[:]->获取全部数据         arr[min,max]->获取从min到max的数据，左开右闭
        连续切片：从起始索引到结束索引按步长切片
        使用slice函数：通过slice(start,stop,step)进行切片      arr[slice(start,stop,step)]
        布尔索引：通过布尔条件筛选满足条件的元素,先生成布尔数组，再根据True进行选择性输出，支持逻辑运算符    arr[逻辑表达式]

      多维数组：
      基本索引：通过整数索引直接访问元素，从0开始           arr[r,c]
      行/列切片：使用冒号，切片语法选择行和列的子集          arr[:,:]->获取全部数据
                                                    arr[num1:num2,num3:num4]->获取从num1到num2行，num3到num4列的数据，左开右闭
      连续切片：从起始索引到结束索引按步长切片
      使用slice函数：通过slice(start,stop,step)进行切片      arr[slice_r(start,stop,step),slice_p(start,stop,step)]
      布尔索引：先进行切片，再通过布尔条件筛选满足条件的元素，支持逻辑运算符    arr[切片表达式][逻辑表达式]



运算：
    1.算术运算（加减乘除幂运算）：两个数组相加是两个数组的同一位置的元素进行算术运算
        广播机制：如果行数或者列数相同/行列数为1，则可以广播到相同形状（例如(3,3)和(1,1),(3,3)和(3,1)；(3,3)和(3,2不行)）

    2.矩阵运算：矩阵乘法-> arr1@arr2     得到一个新矩阵，新矩阵的num1行num2列的数字是数组1 num1行和数组2 num2列进行对位相乘再相加



常见函数：
    计算平方根：np.sqrt(num/arr)       计算num/arr中的每个元素的平方根
    计算指数：np.exp(num)             计算e的num次方
    计算自然对数：np.log(num)          计算ln(num)的值
    计算三角函数：np.sin/cos(num)      计算num的正弦值/余弦值(PI可以表示为np.pi)
    计算绝对值：np.abs(arr/num)
    计算幂运算:np.power(arr/num,num0) 计算arr/num的num0次方
    四舍五入：np.round(arr/num)        最近偶数舍入
    向上取整/向下取整：np.ceil(arr/num)  向上取整，原有整数会直接+1          np.floor(arr/num)   向下取整，原有整数-1
    检测缺失值：np.isnan(arr/n)         空值表示为np.nan，n为变量

统计函数：
    求和函数：np.sun(arr)        数组求和
    计算平均值：np.mean(arr)     数组求平均值
    计算中位数:np.median(arr)    求数组中位数
    计算标准差和方差：方差：np.var(arr)     标准差：np.std(arr)
    计算最大值和最小值：np.max(arr,axis=n)   np.min(arr,axis=n)         这两个方法返回的是值,n为0，是求每一列的最值，n为1，是每一行的最值
                    np.argmax(arr)  np.argmin(arr)    这两个方法返回的索引
    分位数：np.percentile(arr,num)          求数组的num分位数
    累计和/累计积：np.cumsum(arr)      累计和是返回一个数组，原数组为[num1,num2,num3]，返回数组为[num1,num1+num2,num1+num2+num3]
                np.cumprod(arr)     累计积



比较函数：
    比较是否大于：np.greater(arr,num)      判断arr中元素是否大于Num，返回布尔值数组
    是否小于：np.less(arr,num)
    是否等于:np.equal(arr,num)/np.equal(arr,arr)    数组间判断是对应位置比较
    逻辑与：np.logical_and(arr,arr)
    逻辑或：np.logical_or(arr,arr)
    逻辑非：np.logical_not(arr)
    检查元素是否至少有一个元素为真：np.any(arr)
    检查元素是否全部为真：np.all(arr)

    自定义条件(类似于if函数)：np.where(condition,y,n)   condition是自定义的条件，y代表符合条件后的输出内容，n代表不符合条件的输出内容
            自定义条件的嵌套：np.where(condition1,y,np.where(condition2,y,n))
                    嵌套的等价：np.select([condition1,condition2,condition3],[result1,result2,result3])   ->需要一一对应


排序函数：
    排序函数：arr.sort() ->会改变原有数组
            arr.sort(arr)   ->不会改变原有数组
            arr.argsort(arr)    ->返回的是排序后的索引

去重函数：arr.unique(arr,return_counts=?)        如果r_c=True,会额外返回每个元素出现了几次
数组拼接：np.concatenate(arr1,arr2)
数组的分割:np.split(arr,num)     将arr数组分为num份
         np.split(arr1,arr2)   arr2为一维数组，该方法是根据指定的arr2数组索引进行切割（如果不能被等分）
调整数组的形状：np.reshape(arr,[num1,num2]) 将原有数组调整为[num1,num2]形状，要求是调整后的元素个数与调整前形状的元素个数相等


"""





