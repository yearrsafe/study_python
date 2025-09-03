
# matplotlib
"""
图像类型：
    折线图（plot），条形图（bar），饼图（pie），散点图（scatter），箱线图（boxplot），多个图表，组合图等


绘制折线图：
    先导入matplotlib.pyplot as plt
    由于plt中中文输出问题，需要再从中导入rcParams:from matplotlib import rcParams        用于控制汉字字体
    修改中文输出：rcRarams['font.family']='SimHei'  或者   rcParams['font.sans-serif']='SimHei'
    创建图表，设置大小：plt.figure(figsize=(long,wide)

    ****以上内容是每次都需要使用的，每种图都适用


    提供图表的数据
    添加标题(所有图都适用)：plt.title('str',color='col',fontsize=n)        str为标题,col为颜色，n为字体大小
    添加坐标轴标签:plt.xlabel('str',fontsize=n)        设置x轴标签
                plt.ylabel('str',fontsize=n)        设置y标签
    添加图例：plt.legend(loc='location')              图例位置:upper left/upper right等
    添加网格线：plt.grid(True/axis='x'/axis='y'，alpha=n，color='col',linestyle='--/-')      True会在x,y轴均添加网格线，x只添加垂直于x的线;alpha是决定了网格线的颜色深浅，0.5就比较深了
                                                                                          linestyle会修改网格线形状，--代表是虚线，-是实线
    自定义刻度：plt.xticks(rotation=m,fontsize=n)
             plt.yticks(rotation=m,fontsize=n)          ratation控制旋转角度，当x/y轴的刻度较长，组合起来较密集，可以旋转使其斜着看，fontsize控制刻度的字体大小

    设置y轴范围：plt.ylim(start,end)

    设置数据点可视化：for x,y in zip(x_name,y_name):
                      plt.text(x+m,y+n,str(x/y),ha='center',va='bottom',fontsize=8)       x,y固定,m和n是代表数据点相对于折线的距离，str是想可视化的数据点，
                                                                                          ha是控制对齐（center代表居中对齐，left左对齐,right是右对齐）
                                                                                          va控制对齐（bottom是底部对齐）

    绘制折线图：plt.plot(x,y,label='name'，color='col',linewidth=n,linestyle='--',marker='o')     x是横坐标的数据,y是纵坐标的数据,label是图例名字
                                                                                               linewidth控制线条粗细，marker会控制实心点等


    显示图表：plt.show()




"""


'''
柱状图：
    先导入matplotlib.pyplot as plt
    由于plt中中文输出问题，需要再从中导入rcParams:from matplotlib import rcParams        用于控制汉字字体
    修改中文输出：rcRarams['font.family']='SimHei'  或者   rcParams['font.sans-serif']='SimHei'
    创建图表，设置大小：plt.figure(figsize=(long,wide)

    ****以上内容是每次都需要使用的，每种图都适用
    
    提供绘图的数据
    绘制柱状图：plt.bar(x,y,label='图例名字',color='col',width=n)      x和y代表绘图的数据，如果需要图例，就加label参数,n调整柱状图的柱的宽度
    添加标题(所有图都适用)：plt.title('str',color='col',fontsize=n)        str为标题,col为颜色，n为字体大小
    添加坐标轴标签:plt.xlabel('str',fontsize=n)        设置x轴标签
                plt.ylabel('str',fontsize=n)        设置y标签
    添加图例：plt.legend(loc='location')              图例位置:upper left/upper right等
    添加网格线：plt.grid(True/axis='x'/axis='y'，alpha=n，color='col',linestyle='--/-')      True会在x,y轴均添加网格线，x只添加垂直于x的线;alpha是决定了网格线的颜色深浅，0.5就比较深了
                                                                                          linestyle会修改网格线形状，--代表是虚线，-是实线
     自定义刻度：plt.xticks(rotation=m,fontsize=n)
             plt.yticks(rotation=m,fontsize=n)          ratation控制旋转角度，当x/y轴的刻度较长，组合起来较密集，可以旋转使其斜着看，fontsize控制刻度的字体大小

    设置y轴范围：plt.ylim(start,end)                                                                                   
    设置数据点可视化：for x,y in zip(x_name,y_name):
                      plt.text(x+m,y+n,str(x/y),ha='center',va='bottom',fontsize=8)       x,y固定,m和n是代表数据点相对于折线的距离，str是想可视化的数据点，
                                                                                          ha是控制对齐（center代表居中对齐，left左对齐,right是右对齐）
                                                                                          va控制对齐（bottom是底部对齐）

    自动优化排版：plt.tight_layout()
    显示：plt.show()
    
    
    
条形图：
    先导入matplotlib.pyplot as plt
    由于plt中中文输出问题，需要再从中导入rcParams:from matplotlib import rcParams        用于控制汉字字体
    修改中文输出：rcRarams['font.family']='SimHei'  或者   rcParams['font.sans-serif']='SimHei'
    创建图表，设置大小：plt.figure(figsize=(long,wide)

    ****以上内容是每次都需要使用的，每种图都适用
    
    提供绘图的数据
    绘制条形图：plt.barh(y,x,color='col')
    添加标题(所有图都适用)：plt.title('str',color='col',fontsize=n)        str为标题,col为颜色，n为字体大小
    添加坐标轴标签:plt.xlabel('str',fontsize=n)        设置x轴标签
                plt.ylabel('str',fontsize=n)        设置y标签
    添加图例：plt.legend(loc='location')              图例位置:upper left/upper right等
    添加网格线：plt.grid(True/axis='x'/axis='y'，alpha=n，color='col',linestyle='--/-')      True会在x,y轴均添加网格线，x只添加垂直于x的线;alpha是决定了网格线的颜色深浅，0.5就比较深了
                                                                                          linestyle会修改网格线形状，--代表是虚线，-是实线
     自定义刻度：plt.xticks(rotation=m,fontsize=n)
             plt.yticks(rotation=m,fontsize=n)          ratation控制旋转角度，当x/y轴的刻度较长，组合起来较密集，可以旋转使其斜着看，fontsize控制刻度的字体大小

    设置y轴范围：plt.ylim(start,end)                                                                                   
    设置数据点可视化：for x,y in zip(x_name,y_name):
                      plt.text(x+m,y+n,str(x/y),ha='center',va='bottom',fontsize=8)       x,y固定,m和n是代表数据点相对于折线的距离，str是想可视化的数据点，
                                                                                          ha是控制对齐（center代表居中对齐，left左对齐,right是右对齐）
                                                                                          va控制对齐（bottom是底部对齐）

    自动优化排版：plt.tight_layout()
    显示：plt.show()

'''
"""
绘制饼图：
    先导入matplotlib.pyplot as plt
    由于plt中中文输出问题，需要再从中导入rcParams:from matplotlib import rcParams        用于控制汉字字体
    修改中文输出：rcRarams['font.family']='SimHei'  或者   rcParams['font.sans-serif']='SimHei'
    创建图表，设置大小：plt.figure(figsize=(long,wide)

    ****以上内容是每次都需要使用的，每种图都适用
    
    提供绘图的数据
    控制颜色：color_0=['red,'blue','green']       或者是用十六进制表示['#m1m2m3','#n1n2n3','#a1a2a3']       m1,n1,a1都表示一个十六进制数字

    绘制饼图：plt.pie(percent,label=name,autopct='%.1f%%',
                    startangle=m,colors=color_0
                    ,shadow=Ture)                        percent代表的是每个内容的数据，name代表数据的名字,
                                                         autopct用于显示所占比例（.1f是控制精度，%%表示转义字符，能输出一个%）
                                                         m用于控制起始角度,shadow控制是否有阴影
    绘制环形图：plt.pie(percent,label=name,autopct='%.1f%%',
                    startangle=m,colors=color_0,
                    wedgeprops{'width':m},
                    pctdistance=n
                    )                                              m是一个小于一的数字，代表有100m%的中心区域被挖去了,n是控制显示的百分比的数字离圆心的距离
    
              在圆环中心显示文本：plt.text(0,0,'str',ha='center',va='bottom',fontsize=n)    
    
    添加标题：plt.title('str',color='col',fontsize=n)

    显示饼图:plt.show()    
    
爆炸式饼图：设置突出块
    新增参数：explode_0=[n,0,0,0,0]      参数的列表长度取决于饼图中的块数，n用于控制该块离圆心的偏移程度
    plt.pie(percent,label=name,autopct='%.1f%%',
                    startangle=m,colors=color_0,shadow=Ture
                    ,explode=explode_0)                  percent代表的是每个内容的数据，name代表数据的名字,
                                                         autopct用于显示所占比例（.1f是控制精度，%%表示转义字符，能输出一个%）
                                                         m用于控制起始角度,shadow控制是否有阴影




"""

"""
绘制散点图：
    先导入matplotlib.pyplot as plt
    由于plt中中文输出问题，需要再从中导入rcParams:from matplotlib import rcParams        用于控制汉字字体
    修改中文输出：rcRarams['font.family']='SimHei'  或者   rcParams['font.sans-serif']='SimHei'
    创建图表，设置大小：plt.figure(figsize=(long,wide)

    ****以上内容是每次都需要使用的，每种图都适用


    提供图表的数据
    绘制散点图：plt.scatter(x,y,color='col',alpha=m,s=n,label='name')      alpha控制透明度，s控制点的大小,label控制图例名
    添加坐标轴标签：plt.xlabel('str',fontsize=n)
                 plt.ylabel('str',fontsize=n)
                 
    添加网格线：plt.grid(True/axis='x'/axis='y'，alpha=n，color='col',linestyle='--/-')      True会在x,y轴均添加网格线，x只添加垂直于x的线;alpha是决定了网格线的颜色深浅，0.5就比较深了
                                                                                          linestyle会修改网格线形状，--代表是虚线，-是实线
    自定义刻度:plt.xticks(rotation=m,fontsize=n)
             plt.yticks(rotation=m,fontsize=n)          ratation控制旋转角度，当x/y轴的刻度较长，组合起来较密集，可以旋转使其斜着看，fontsize控制刻度的字体大小
    
    设置y轴范围：plt.ylim(start,end)

    设置数据点可视化：for x,y in zip(x_name,y_name):
                      plt.text(x+m,y+n,str(x/y),ha='center',va='bottom',fontsize=8)       x,y固定,m和n是代表数据点相对于折线的距离，str是想可视化的数据点，
                                                                                          ha是控制对齐（center代表居中对齐，left左对齐,right是右对齐）
                                                                                          va控制对齐（bottom是底部对齐）
    
    设置回归线：plt.plot([x1,y1],[x2,y2],color='col',alpha=m,linestyle='--')


"""


"""
绘制箱线图：主要看数据分布，异常
    先导入matplotlib.pyplot as plt
    由于plt中中文输出问题，需要再从中导入rcParams:from matplotlib import rcParams        用于控制汉字字体
    修改中文输出：rcRarams['font.family']='SimHei'  或者   rcParams['font.sans-serif']='SimHei'
    创建图表，设置大小：plt.figure(figsize=(long,wide)

    ****以上内容是每次都需要使用的，每种图都适用


    提供图表的数据(data
    
    
    plt.figure(figsize=(long,wide))
    plt.title('str',color='col',fontsize=n)
    plt.xlabel('str',fontsize=n)
    plt.ylabel('str',fontsize=n)
    plt.boxplot(data.values(),tick_labels=data.keys())            data可能为列表，适用values()方法和keys()方法分别是取列表的值和名字
    plt.grid(True/axis='y'/axis='x',linestyle='--',alpha=0.5)
    plt.show()



"""


"""
多图的绘制：
    先导入matplotlib.pyplot as plt
    由于plt中中文输出问题，需要再从中导入rcParams:from matplotlib import rcParams        用于控制汉字字体
    修改中文输出：rcRarams['font.family']='SimHei'  或者   rcParams['font.sans-serif']='SimHei'
    
    *创建图表：f1=plt.subplot(m,n,subs)         m，n代表图表的长宽，subs是当前图表的索引，表示当前图是哪个图，需要一个参数进行继承方法的返回
             在分别绘制图表时，只需要将原方法的plt改为f1（继承的参数）就行
    
    
    
    
    
    

"""