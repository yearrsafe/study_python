a=input("请输入性别:")
if a!="男" and a!="女":
    print("无对应公式")
elif a=="男":
    fa=int(input("请输入父亲身高:"))
    mo=int(input("请输入母亲身高:"))
    heigh=int((fa+mo)*1.08/2)
    print(f"孩子的身高为:{heigh}")
else:
    fa = int(input("请输入父亲身高:"))
    mo = int(input("请输入母亲身高:"))
    heigh = int((fa*0.923+ mo) / 2)
    print(f"孩子的身高为:{heigh}")

