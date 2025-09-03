#requests库

#requests库的一个类型和六个属性
"""
用requests库获取的网页响应:
import requests
url=''
response = requests.get(url)


response类型为requests.models.Response

属性:
    以字符串来返回网页源码:response.text
    设置response的编码格式：response.encoding='utf-8'
    返回response的url:response.url
    返回response的二进制数据:response.content
    返回响应的状态码:response.status_code
    返回响应头:response.headers
"""


#requsets的get请求
"""
requests库的get请求方法:response=requests.get(url=url,params=data,headers=headers)

其中，url是响应网址,params代表的是参数，也就是get请求中的参数(网址中?后的内容),headers就是请求头
requests中，参数不需要urlencode编码，也不需要进行请求对象的定制，响应网址url的?可以删去

"""

#requests的post请求
"""
import requests

url=''
headers={ua}
data={}         传参
response=requests.get(url=url,headers=headers,data=data)
        #url是请求地址，data是请求参数,headers是字典
content=response.text
import json
obj=json.loads(content,encoding='utf-8')     用loads方法，因为loads方法内参数是字符串，load方法参数是文档     


具体而言，data是网址中wd的内容，在requests库中不需要再编码，而又因为url里是urlencode编码，所以data内数据不能放在url里，需要单独用data并传参
params/data是网址中截去的内容，headers是ua、ip等内容

"""

#requests代理
"""
代理:proxy={'http':'ip地址:端口号'}
把proxy放到headers参数里就行w

"""


#破解验证码
"""



"""