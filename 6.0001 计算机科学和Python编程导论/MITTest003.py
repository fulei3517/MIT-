# -*-  coding: utf-8 -*-
# 2.4 迭代 练习2

# 编写一个程序，要求用户输入10个整数，然后输出其中最大的奇数。如果用户没有输入奇数，则输出一个消息进行说明
times = 0
temp = 0

# 1 一个循环让用户 循环输入10次
# 2 判断用户输入的值 是不是奇数 如果是奇数就将该数值与 temp 比较
# 3 将比较出来的大奇数 赋值给 temp
# 4 如果 temp >0 就将 temp 输出 否者就输出 没有奇数的提示

while (times < 10):
    times += 1
    num = int(input("请输入第 %d 个数字" % times))
    if num % 2 != 0 and num > temp:
        temp = num
if temp > 0:
    print("最大的奇数是 %d " % temp)
else:
    print("没有奇数")
