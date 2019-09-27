# -*- coding:utf-8 -*-
import random

# 2.2 程序分支 练习题
# 检查3个变量 x,y,z 输出其中最大的奇数。如果其中没有奇数，就输出一个消息进行说明

# x = int(input("Enter x = "))
# y = int(input("Enter y = "))
# z = int(input("Enter z = "))

# 1. 需要输出的结果是奇数
# 2. 需要是最大的奇数

def testOdd(x, y, z):
    print("x = %d y = %d z = %d" % (x, y, z))
    # 首先分别判断 三个参数是不是奇数 如果不是奇数 就将它值为零
    if x % 2 == 0:
        x = 0
    if y % 2 == 0:
        y = 0
    if z % 2 == 0:
        z = 0
    if x == y == z == 0:
        print("No odd number")
    elif x > y and x > z:
        # x 为最大值
        print("x = %d is max odd" % x)
    elif y > z:
        # y是最大值
        print("y = %d is max odd" % y)
    else:
        print("z = %d is max odd" % z)


for i in range(10):
    testOdd(random.randint(0, 100), random.randint(0, 100), random.randint(0, 100))
