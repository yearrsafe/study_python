#urllib库的使用
"""
1.先定义一个url,url代表你目标的地址      url="http://www.baidu.com"
2.模拟浏览器向服务器发送请求：
    导入urllib模块,使用request()方法：import urllib.request       response=urllib.request.urlopen(url)
3.根据对应规则进行接收目标数据,使用read()方法
    read()方法会返回字节形式的二进制数据，需要进行转换,即解码(decode('编码格式'))
    content=response.read().decode('utf-8')


4.打印数据：
    print(content)

"""


#urllib库中的1个类型和6个方法
"""
类型：
    response是request.urlopen(url)的返回值，其类型为HTTPResponse
    print(type(response))
方法:
    read()方法:content=response.read(n)       读取n个字节
    readline()方法:content=response.readline()        只能读取一行
    readlines()方法:content=response.readlines()      全部读取
    
*****以上方法都需要使用decode('')方法解码为字符串
    getcode()方法:返回状态码,如果返回值是200,则没有问题    response.getcode()
    geturl()方法:返回访问的url地址
    getheaders()方法:返回状态信息 如时间等
    


"""



#urllib的下载
"""
先导入urllib.request
下载(下载到的文件名需要有对应的后缀):
    网页:url_page='网址'     urllib.request.urlretrieve(url,filename)        url代表网址,filename代表要下载到的文件名
    图片:url_img='图片地址'   urllib.request.urlretrieve(url,filename)        url代表网址,filename代表要下载到的文件名
    视频:url_video='视频地址'    urllib.request.urlretrieve(url,filename)        url代表网址,filename代表要下载到的文件名

"""


#urllib请求对象的定制——UA反爬
"""
url的组成:
    http/https(协议)+主机+端口号+路径(s)+参数(?后的内容)+锚点

UA反爬:UA反爬就是通过识别和分析请求头中的User-Agent字符串来判断是否为爬虫，并对非法的User-Agent请求进行拦截或返回虚假数据。
    简单来说，在爬虫之前浏览器会进行分析是否为合法爬虫程序，如果非法则返回错误或者返回虚假数据
    为了避免，需要设定特殊的UA字符串来绕过目标浏览器的分析,这里提供大致过程
    
    *先找到自己电脑对应的ua参数,修改为字典类型:
    url_0='网址'
    
    user-agent
    Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0
    
    header_0={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0"}

    *根据urlopen()方法可知，该方法内的参数不包括字典类型，因此需要将其转为request类型：
    request_0=urllib.request.Request(url=url_0,headers=header_0)        这里采取的是显式参数传递，因为url和headers参数的顺序问题，如果采取值传递会导致参数读取的错误
        
    *再套入之前的urllib.request.urlopen()方法,此时这里urlopen()方法内参数需要改为新的request类型的参数：
    response=urllib.request.urlopen(request_0)
    content=response.read().decode('utf-8')
    
    
"""




#get请求的quote()方法
"""
目标：获取指定网址下的网页源码

import urllib.request
url_0='网址'

模拟浏览器向服务器发送请求:
response=urllib.request.urlopen(url_0)
content=response.read().decode('utf-8')

其中如果有ua反爬，使用请求对象定制来解决反爬


上述过程结束后若返回ASCII码的问题，需要进行改进:
    该问题在于url_0中的参数不是url编码，需要手动获得编码后内容
    import urllib.parse
    name=urllib.parse.quote(参数)
    
    此时name会返回参数对应的url编码，再对url_0进行拼接：
    url_0=url_0+name
    
    再进行上述步骤就行了


"""


#get请求的urlencode方法
"""
urlencode方法的适用场景：多个参数
    import urllib.parse
    
    将对应的多个参数设置成一个字典:
    data={
        "wd"="****",
        "label2"="name2"
    }
    
    a=urllib.parse.urlencode(data)
    此时a是多个参数的通过&来链接的url字符串，再将a与网址进行拼接



"""


#post请求
"""
post请求和get请求的区别:
    已知get请求中，网址?后的参数为url编码的字符串，如果该字符串字节数过大，则不适合进行请求，这里提出post请求来解决这个问题

大致步骤:
    *导入包:
    import urllib.request
    import urllib.parse
    import json
    
    *提供数据，该数据需要以字典的形式存储,再将其转换为url编码并解码
    data={
        'label1':'name1',
        'label2':'name2'
    }
    data_n=url.parse.urlencode(data).encode('utf-8')
    
    *给定目标url并提出请求
    url_0='网址'
    request=url.request.Request(url=url_0,data=data_n)
    response=urllib.request.urlopen(request)
    content=response.read().decode('utf-8')
    
    *返回的是json型数据，需要进行解码
    content_n=json.loads(content)
    print(content_n)

"""

#ajax的get请求
"""
ajax的get请求是指在不刷新页面的前提下，通过url向服务器请求数据

import urllib.request
url_0='网址'
headers_0={
    'ua'='.....'
}
request=urllib.request.Request(url=url_0,headers=headers_0)
response=urllib.request.urlopen(request)
content=response.read().decode('utf-8')

*再下载到本地
with open('文件地址','w',encoding='utf-8') as f:
    f.write(content)
    



***************************
需要注意的是，网址和get/post请求的要求是由接口的标头处有提醒

"""


#ajax的post请求
"""
ajax的判定:响应头处有XMLHttpRequest

"""
#异常
"""
包括URLError和HTTPError两种，其中，http是url异常的子类
处理方式:
try:
    尝试代码
except urllib.error.HTTPError:
    提醒
except urllib.error.URLError:
    提醒
"""



#cookie登录
"""
适用场景：绕过登录来获取信息
与之前相比，cookie登录将请求头内的所有内容全部打包到headers参数里，且该请求头的cookie是登录之后的请求头的数据


"""
print('qq空间的cookie登录')



#Handler处理器
"""
使用handler来访问百度

import urllib.request
url_0='百度网址'
headers_0={
    'ua'='.....'
}
request=urllib.request.Request(url=url_0,headers=headers_0)


*********handler的使用:handler,build_open,open
1)获取handler对象
    handler=urllib.request.HTTPHandler()
2)获取opener对象
opener=urllib.request.build_opener(handler)
3)调用open方法
response=opener.open(request)


content=response.read().decode('utf-8')
"""

#代理
"""
用代理ip访问网址
import urllib.request
url_0='百度网址'
headers_0={
    'ua'='.....'
}
request=urllib.request.Request(url=url_0,headers=headers_0)

*********使用ip代理来访问
proxies={
'http':'ip地址:端口'
}
handler=urllib.request.ProxyHandler(proxies=proxies)
opener=urllib.request.build_opener(handler)
response=opener.open(request)
content=response.read().decode('utf-8')



代理ip的生成:快代理

"""
#代理池
"""
proxies_pool=[
    {'http':'ip地址：端口'},
    {'http':'ip地址：端口'},
    {'http':'ip地址：端口'},
    .....
]

import random
proxy=random.choice(proxies_pool)

handler=urllib.request.ProxyHandler(proxies=proxy)
opener=urllib.request.build_opener(handler)
response=opener.open(request)
content=response.read().decode('utf-8')


"""

