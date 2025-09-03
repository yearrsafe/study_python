#文件的打开与关闭/文件的读写/文件的序列化和反序列化/异常

"""
打开文件：打开或创建文件
    f=open('文件路径',访问格式)      示例：open('路径','w'/'r')       w:可写  r:可读  a:追加
写文件：f.write('str')      将str写入文件f

关闭文件：f.close()




写入数据：
    f.write('str')           如果打开方式为w,会先清空原有内容，再加入str;访问格式是a才能追加

读取数据：
    打开方式是r,再用一个变量接收读取的数据,使用read()方法或readline()方法
    二者区别在于read()方法是逐字节读取，readline()每次可以读取一行，但只能读一行
    content=f.read()        print(content)
    content=f.readline()

    可以使用readlines()方法读取多行，读完会返回一个列表，列表中的元素是每一行的内容




文件的序列化和反序列化：使用json模块
    序列化：将内存中的数据（如字典，元组等）转换为字符串，保存到文件；
    反序列化：将文件中的字节序列恢复到内存里


序列化的两种方式:
    dumps():
        示例：import json
            list=['s','d','f']
            s_list=json.dumps(list)
            f=open('test.txt','w')
            f.write(s_list)
            f.close()
    注意：写入的数据是列表形式，带有[]和''

    dump():dump方法会在转换为字符串的同时，指定一个文件，将该字符串写入文件
        示例：import json
            list=['s','d','f']
            s_list=json.dumps(list)
            f=open('test.txt','w')
            json.dump(s_list,f)
            f.close()



反序列化：
    loads()方法:方法内参数是字符序列
        示例：import json
             f=open('test.txt','r')
             content=f.read()
             result=json.loads(content)
             print(result)


    load()方法：方法内参数是文件
        示例：import json
             f=open('test.txt','r')
             result=json.load(f)
             print(result)





异常：
    格式：try:
            可能出现异常的代码
        except 异常类型:
            提示说明


"""