#Selenium
"""
Selenium:
    是一个用于web应用程序测试的工具；其测试是直接运行在浏览器中；支持无界面浏览器操作
    模拟浏览器，自动执行网页的js代码，实现动态加载
"""


#创建浏览器、设置、打开
"""
先导包:
    from selenium import webdriver                              用于操作浏览器
    from selenium.webdriver.chrome.options import Options       用于设置谷歌浏览器
    from selenium.webdriver.chrome.service import Service       
    from selenium.webdriver.edge.service import Service
    from selenium.webdriver.edge.options import Options


创建设置浏览器对象:
    q1=Options()
    q1.add_argument('--no sandbox')     禁用沙盒模式,提高系统兼容性
    q1.add_experimental_option('detach',True)       保持浏览器打开状态，默认是代码执行完毕自动关闭浏览器,此时被修改为一直打开
    
创建并启动浏览器：
    a1=webdriver.Chrome(service=Service('chromedriver.exe'),options=q1)
    a2=webdriver.Edge(service=Service('msedgedriver.exe'),options=q1)
    
    
"""


#打开网页，关闭当前标签页，关闭浏览器
"""

打开网页:打开指定网址——>a1.get('网址')
关闭当前标签页:a1.close()      
退出浏览器:a1.quit()

"""

#浏览器的最大化和最小化
"""
最大化:a1.maximize_window()
最小化:a1.minimize_window()

"""
#浏览器的打开位置和尺寸
"""
浏览器打开位置:a1.set_window_position(x,y)    (0,0)是在左上角
浏览器打开尺寸:a1.set_window_size(width,height)    
"""

#浏览器截图和刷新
"""
截图:a1.get_screenshot_as_file('截图名.后缀')
刷新:a1.refresh()
"""



#元素定位
"""
定位一个元素:a1.find_element(By.ID/By.CLASS/...,value)        找到的话会返回结果
定位多个元素:a1.find_elements(By.ID/By.CLASS/...,value)        找到的话会返回列表,找不到会返回空列表



根据id定位:button=a1.find_element(By.ID,value)      ID定位比较准确，但并不是所有元素都有ID
根据标签属性的属性值定位:button=a1.find_element(By.NAME,value)      Name定位比较准确，但并不是所有元素都有,name的使用频率比id低
根据Class_Name进行定位:a1.find_element（s）(By.CLASS_NAME,value)       class值不能有空格，否则会报错；class重复值很多，如果返回多个元素时需要索引操作定位
                                                                    class的值可能是随机的

根据xpath语句定位:button=a1.find_element（s）(By.XPATH,'xpath语句')     谷歌浏览器支持复制(如果标签头内容随机会导致不准确),可以通过复制Xpath的完整路径来解决

根据标签名来获取对象:button=a1.find_element（s）(By.TAG_NAME,'tag name')   这个查找的是标签的名字,比如是input,a等;重复的很多，需要索引处理

根据bs4语句来获取对象:button=a1.find_element(By.CSS_SELECTOR,'bs4语句')
                  #id/.class/不加修饰符是搜索标签头/任意标签类型定位:"[类型='精确值']"/任意标签类型定位:"[类型*='模糊值']"/任意标签类型定位:"[类型^='开头值']"/任意标签类型定位:"[类型$='结尾值']"
                  谷歌浏览器支持右键复制选项里能够复制selector的专属值

根据精准链接文本获取对象:button=a1.find_element（s）(By.LINK_TEXT,value)      默认搜索a标签(超链接标签)，value值是a标签下的文本值;a标签下的文本可能有重复的,需要索引
根据模糊链接文本获取对象:button=a1.find_element（s）(By.PARTIAL_LINK_TEXT,value)      


"""

#元素交互:元素点击/元素输入/元素清空
"""
元素输入:a2=a1.find_elements(By.ID/By.CLASS/...,value)
       a2.send_keys('输入内容')     向a2的元素中输入内容,例如a2是输入框
       
元素点击:a2=a1.find_elements(By.ID/By.CLASS/...,value)
        a2.click()      点击a2代表的元素
        
元素清空:a2.clear()     清空元素内内容，例如清空输入框内文本


"""


#元素定位隐性等待
"""
小型网站打开瞬间加载未完成来进行定位会报错，可以通过sleep函数来设置等待时间解决

为了能提高处理速度减少多余等待时间,可以使用元素定位隐性等待
    a1.implicitly_wait(n)       n秒内能找到元素会直接执行，也就是说即使只需要0.01秒进行反应也会直接运行
    a1.find_elements(By.ID/By.CLASS/...,value).click()

"""

#单选,多选,下拉元素交互
"""
多选就是多个单选，下拉是需要先进行下拉来展示所有选项再进行定位,定位后用click()函数就行
"""

#日期，评星，上传元素交互
"""
填写日期：需要先判断日期的最大值，即每个空能填写多少数字，再根据最大值进行元素输入
a1.find_elements(By.ID/By.CLASS/...,value).send_keys('0020250831')
评星：找到对应星级所在的位置，再使用click函数
上传:找到上传按钮所对于位置，不需要点击，直接上传文件，需要注意的是，上传的文件需要是绝对路径，并在路径前加r
a1.find_elements(By.ID/By.CLASS/...,value).send_keys(r'D:/wd/pic.png')

"""


#获取句柄，切换标签页
"""
获取全部标签页句柄:
page_name_list=a1.window_handles        该方法返回的是列表,列表值是标签页的名字对应的编码值
获取当前标签页句柄:page_now=a1.current_window_handle

获取后一般要关闭原页面，即a1.close()
再切换标签页:a1.switch_to.window(page_name[1])

"""


#警告框元素交互
"""
点击弹窗确定按钮:
a1.switch_to.alert.accept()
获取弹窗文本内容:
a1.switch_to.alert.text
print(a1.switch_to.alert.text)


"""
#确认框元素交互
"""
点击弹窗确认按钮:a1.switch_to.alert.accept()
点击弹窗取消按钮:a1.switch_to.alert.dismiss()

"""

#提示框元素交互
"""
先获取元素位置进行定位，再使用send_keys方法来输入

"""

#iframe嵌套页面的进入与退出
"""
iframe是网页下的小网页

先获取iframe元素,再进入嵌套页面
    获取:a2=a1.find_elements(By.ID/By.CLASS/...,value)
    进入:a1.switch_to.frame(a2)

退出(返回到默认页面):a1.switch_to.default_content()
"""
#获取元素文本内容/元素是否可见
"""
获取文本：text()
        a2=a1.find_elements(By.ID/By.CLASS/...,value).text()
是否可见:is_displayed()     如果可见返回True,不可见返回False
        a2=a1.find_elements(By.ID/By.CLASS/...,value).is_displayed()

"""

#网页的前进与后退
"""
后退：a1.back()
前进:a1.forward()
"""
