

#图片下载_站长素材
"""
网页1：https://sc.chinaz.com/tupian/beijingtupian.html
网页2：https://sc.chinaz.com/tupian/beijingtupian_2.html

"""


import urllib.request
from lxml import etree


def get_url(page):
    if page==1 :
        url='https://sc.chinaz.com/tupian/beijingtupian.html'
    else:
        url='https://sc.chinaz.com/tupian/beijingtupian'+str(page)+'.html'
    return url



def get_content(url_0):
    headers_0 = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0'
    }
    request=urllib.request.Request(url=url_0,headers=headers_0)
    response=urllib.request.urlopen(request)
    content=response.read().decode('utf-8')
    return content


def download(content):
    tree=etree.HTML(content)
    #此外这里还产生一个问题，xpath helper在name_list的路径里返回的是文本值，但在python中返回的仍然是path节点，需要使用text()函数来获取纯文本值
    name_list=tree.xpath('//div[@class="container"]//a[@class="name"]/text()')
    src_list=tree.xpath('//div[@class="container"]//@data-original')
    for i in range(len(name_list)):
        name = name_list[i]
        src = 'https:' + src_list[i]
        #下载到指定文件夹,格式为filename='./文件夹名/'+文件名+'后缀名'
        urllib.request.urlretrieve(url=src,filename='./pictures/'+name+'.png')




page_s=int(input('请输入起始页码'))
page_e=int(input('请输入结束页码'))

for i in range(page_e,page_s+1):
    url=get_url(i)
    content=get_content(url)
    download(content)
