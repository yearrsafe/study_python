money = 10000
name = ''
def putin():
    global money
    supplement = eval(input("请输入存入金额:"))
    money += supplement
    print("存入了{}元,账户余额为{}元\n".format(supplement, money))


def outm():
    global money
    outmoney = eval(input("请输取出金额："))
    money -= outmoney
    print("取出了{}元,账户余额为{}元\n".format(outmoney, money))


def find():
    global money
    print("您的姓名为{},您当前账户的余额为{}元\n".format(name, money))

name = input("请输入账户姓名:")
choice = eval(input("请选择操作内容:\n查询余额请输入1\n存款请输入2\n取款请输入3\n"))
match choice:
    case 1:
        find()
    case 2:
        putin()
    case 3:
        outm()



