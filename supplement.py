"""
输出格式的补充:
1. print方法:
    print("Python", "is", "awesome", sep="-", end="!")  # Python-is-awesome!
2.格式化输出:
    print("Hello, %s" % "world")  # Hello, world

    print(f"Hello, {'world'}")  # Hello, world                推荐使用


        print("My name is {} and I am {} years old.".format(name, age))  # My name is John and I am 21 years old.    name和age是变量
            **隐式索引,按照变量在format中的顺序进行索引
        print("My name is {0} and I am {1} years old.".format(name, age))  # My name is John and I am 21 years old.    name和age是变量
            **显式索引,按照数字进行索引,0表示第一个变量,1表示第二个变量
        print("My name is {name} and I am {age} years old.".format(name="John", age=21))  # My name is John and I am 21 years old.
            **关键字索引,按照关键字进行索引

3.输出到文件:
    with open("output.txt", "w") as f:
        print("Hello, File!", file=f)




输入格式的补充:
    1. input方法:
        name = input("What is your name? ")  # What is your name? John
        print(name)  # John
    2. eval方法:
        a=eval(input("请输入您的年龄:"))           #输入的是数字,但是在程序里是字符串,使用eval可以将其转为整形或者浮点型
        eval函数类似于强转,例如a=int(input("请输入您的年龄:"))
        但是eval函数可以将输入的内容转为列表、元组、字典等数据类型。
    3.split方法:
        split方法可以将输入的一行字符串按空格 拆分成多个值;用于分割字符串,返回一个列表,默认以空格分割,也可以指定分隔符。
        示例：
            x, y = float, input("请输入两个小数（用逗号分隔）: ").split(',')
    4.多行输入:
        可以使用for循环来实现多行输入;或者是使用sys.stdin.read()方法(使用时需引入sys模块)
            import sys
            data = sys.stdin.read()
            print("输入的内容是:")
            print(data)
    5.文件输入:
        f.read()方法可以读取文件的内容
            with open("input.txt", "r") as f:
                data = f.read()
                print("输入的内容是:")
                print(data)
    6.逐个输入:
        逐个输入可以使用for循环,或者是使用sys.stdin.read(1)方法(使用时需引入sys模块)
            import sys
            ch = sys.stdin.read(1)  # 读取一个字符
            print("你输入的字符是:", ch)
"""