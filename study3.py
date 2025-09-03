#解析


#xpath解析
"""
先导入:from lxml import etree
本地文件:etree.parse()
服务器响应的数据:response.read().decode('utf-8')
              etree.HTML()


本地:
    tree=etree.parse('study1.html')
    *再通过xpath方法来解析页面
    tree.xpath('xpath路径')       xpath路径正确则可解析所有内容


xpath的基本语法：
    1.路径查询：//查询子孙节点，/只查询直接的子节点
        li_list=tree.xpath('//body/ul/li')
    2.谓词查询://路径[@id]  用于查询该路径下存在id属性的标签；//路径[@id="id_name"]     用于查询该路径下id为id_name的标签
        li_list=tree.xpath('//body/ul/li[@id]/text()')              输出路径下的id所在标签的文本值
        li_list=tree.xpath('//body/ul/li[@id="id_name"]/text()')    输出id为id_name的标签的文本值
    3.属性查询://@class     查找标签的class的属性值
        list=tree.xpath('//body/ul/li[@id="id_name"]/@class')
    4.模糊查询://路径[contains(@id,"str")]        路径下id中含有str的标签
             //路径[starts-with(@id,"str")]     路径下id中以str为开头的标签
        li_list=tree.xpath('//body/ul/li[contains(@id,"l")]/text()')        返回id中含有l的标签的文本值
    5.逻辑运算:返回逻辑和  //路径[@id="id_name" and @class="class_name"]        查询id为id_name和class为class_name的标签
             返回逻辑或  //路径1[@id="id_name1"]  |  路径2[@id="id_name2"]]     查询两个路径下id为id_name1或id_name2的标签








"""


#xpath.HTML()的使用
"""
HTML方法主要用于解析网页响应的文件，这意味着方法内参数应该是网页源码

即：
import urllib.request
from lxml import etree
request=urllib.request.Request()
response=urllib.request.urlopen(request)
content=response.read().decode('utf-8')
tree=etree.HTML(content)
result=tree.xpath('//body/ul/li/text()')

需要注意的是,xpath的返回值是列表类型,如果要显示具体文本需要根据列表下标进行索引

"""

#另一种解析方法:JsonPath
"""
jsonpath用于解析json数据，只能解析本地文件

import json
import jsonpath

打开json文件:obj=json.load(open('文件名','打开方式',encoding='utf-8'))
jsonpath语句:name=jsonpath.jsonpath(obj,'jsonpath语句')

jsonpath与xpath语句的区别：
xpath       jsonpath                description
  /           $                       表示根元素
  .           @                       表示当前元素
  //          ..                      递归下降
  @           n/a                     属性访问字符
  []          []                      子元素操作符
  *           *                       通配符，表示所有元素
  
  
举例：
/store/book/author              $.store.book[*].author          书店所有书的作者
//author                        $..author                       所有的作者
/store/*                        $.store.*                       书店内所有的元素
/store//price                   $.store..price                  书店内所有元素的价格
//book[3]                       $..book[2]                      书店内第三本书
//book[last()]                  $..book[(@.length-1)]           最后一本书（这里的length就是length不代指长度）
//*                             $..*                            全部元素

带冒号的请求头一般是不需要使用的

"""



#BeautifulSoup/bs4的使用
"""
bs4的基本语法：
    from bs4 import BeautifulSoup
    打开本地文件：soup=BeautifulSoup(open('本地文件名',encoding='utf-8'),'lxml')
               soup=BeautifulSoup(open('study3.html',encoding='utf-8'),'lxml')
    *打开本地文件的方法默认打开编码为gbk，需要手动指定编码格式
    
    根据标签名查找节点(查找第一个符合要求的数据):soup.节点名        soup.a
    获取标签的属性和属性值:    soup.节点名.attrs                soup.a.attrs


    bs4的一些函数：
    find:soup.find('节点名')    返回第一个符合条件的数据    soup.find('a',title='a2') ; soup.find('a',class_='a1') (查找class时，要在后面加_)
    
    find_all:soup.find_all('节点名')   返回所有符合条件的数据,返回值是列表类型，如果有多个条件进行查询，查询条件需要是列表类型(和运算)    soup.find_all(['a',title='a1']) 
             soup.find_all('节点名',limit=n)       查询前n个数据  
    select:推荐,返回多个值,类型为列表**
        通过标签来查询对象:soup.select('元素名')        soup.select('.class对应的名字')          soup.select('#id对应的名字')    
        属性选择器:  查找对应标签里含有某种属性    li=soup.select('标签[属性]')
                   查找对应标签里含具体属性      li=soup.select('标签[属性="属性名"]')
        层级选择器:  后代选择器:找到某个标签下的标签->soup.select('父标签 子/孙标签')
                   子代选择器:找到某标签下的第一级子标签->soup.select('父标签 > 子标签 > 孙标签')      尽量在>两侧加空格
                            找到两个/多个标签(或运算)->soup.select('标签1,标签2')
        获取节点内容:obj=soup.select('元素名/.class对应的名字/#id对应的名字')[n]       由于select返回的是列表，需要在后面进行索引,再使用string()方法或get_text()方法获取内容
                            优先使用get_text()方法     string方法只能获取对应标签下是纯文本而不含有其他标签
        获取节点的属性:obj=soup.select('元素名/.class对应的名字/#id对应的名字')[n]      该方法返回的是含有节点及其对应值的字典,需要使用attrs和get方法来获取具体字典值
                    obj=soup.select('#p1')[0]       obj.attrs.get('class')
                    


"""