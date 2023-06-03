import os, time


print("欢迎来到万能计算器")
time.sleep(1.5)
os.system("cls")
while True:
    print("1.常规运算 2.面积运算 3.货币换算")
    mode = input("")
    if mode == "1":
        os.system("cls")
        ques = input("")
        ans = eval(ques, None, None)
        print(ans)
        time.sleep(1.5)
        os.system("cls")
    elif mode == "2":
        os.system("cls")
        print("1.长方形（包括正方形） 2.三角形")
        grap = input("")
        if grap == "1":
            width0 = int(input("长："))
            height0 = int(input("宽："))
            rs = width0 * height0
            print(str(rs))
            time.sleep(1.5)
            os.system("cls")
        elif grap == "2":
            width1 = int(input("底："))
            height1 = int(input("高"))
            ts = width1 * height1 / 2
            print(str(ts))
            time.sleep(1.5)
            os.system("cls")
