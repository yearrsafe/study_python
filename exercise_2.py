#爬取前十页豆瓣电影



import urllib.request
import urllib.parse


#请求对象的定制
def url_make(page):
    url_base="https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&"
    data={
        'start':(page-1)*20,
        'limit':20
    }
    url_change=urllib.parse.urlencode(data)
    url_new=url_base+url_change
    return url_new

#获取网页源码
def requestion(url_new):
    headers_0={
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0'
    }

    request=urllib.request.Request(url=url_new,headers=headers_0)
    response=urllib.request.urlopen(request)
    content=response.read().decode('utf-8')
    return content

#下载
def download_page(content,page):
    with open('loading'+str(page)+'.json','w',encoding='utf-8') as f:
        f.write(content)








page_s=int(input('请输入起始页码'))
page_e=int(input('请输入截止页码'))

for page in range(page_s,page_e+1):
    url=url_make(page)
    content=requestion(url)
    download_page(content,page)



