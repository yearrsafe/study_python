#cookie登录古诗文网

"""

__VIEWSTATE
/wEPDwUKLTU5OTg0MDIwNw8WAh4TVmFsaWRhdGVSZXF1ZXN0TW9kZQIBZGQGi0FCmPHMP+KelvQVsoBoqE2Axg==
__VIEWSTATEGENERATOR
C93BE1AE
from
http://www.gushiwen.cn/user/collect.aspx
email
15753361939
pwd
wzd200605
code
kqlq
denglu
登录


https://www.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fwww.gushiwen.cn%2fuser%2fcollect.aspx
"""


#分析
"""
以上可知，负载中需要这五个数据，其中后三个好获得
vs/vsg都是隐藏的需要去找，又知隐藏内容一般都在网页源码，故要返回到源码去找

解决完隐藏内容后解决验证码的问题，由于验证码是不可见的，故在源码中再次寻找（对验证码右键检查），找到验证码的原网址为https://www.gushiwen.cn/RandCode.ashx
由于urllib库中的retrieve方法会导致和requests库生成的请求不同，进而导致验证码会刷新，采用session方法来下载图片，并用二进制写入文件
"""


import requests
from bs4 import BeautifulSoup
session=requests.Session()

url_vs='https://www.gushiwen.cn/user/login.aspx?from=http://www.gushiwen.cn/user/collect.aspx'

headers_0={
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0'
    }
response=session.get(url=url_vs,headers=headers_0)
content=response.text
soup=BeautifulSoup(content,'lxml')
vs=soup.select('#__VIEWSTATE')[0].attrs['value']
vsg=soup.select('#__VIEWSTATEGENERATOR')[0].attrs['value']


url_code='https://www.gushiwen.cn/RandCode.ashx'

response_code=session.get(url=url_code)
content_code=response_code.content      #获取response_code的二进制数据
with open('code.png','wb')as f:
    f.write(content_code)

code_name=input('请输入验证码')

data={
    '__VIEWSTATEGENERATOR':vsg,
    '__VIEWSTATE':vs,
    'from':'http://www.gushiwen.cn/user/collect.aspx',
    'email':'15753361939',
    'pwd':'wzd200605',
    'code':code_name,
    'denglu': '登录'
}



#****这里需要注意的是，response的post方法调用对象是session而不是之前的request request是为了获取隐藏内容的
response=session.post(url=url_vs,data=data,headers=headers_0)
content=response.text
#还有要补充写入数据的编码格式
with open('response.html','w',encoding='utf-8')as f1:
    f1.write(content)

#此时已经成功登录，这时候会返回一个登录的页面，如果要进去网站需要访问进一步的网址

collect_url = "https://www.gushiwen.cn/user/collect.aspx"
res_collect = session.get(collect_url, headers=headers_0)

with open("collect.html", "w", encoding="utf-8") as f2:
    f2.write(res_collect.text)




