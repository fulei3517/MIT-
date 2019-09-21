# -*-  coding: utf-8 -*-
# 2.4 迭代 练习2

# 编写一个程序，要求用户输入10个整数，然后输出其中最大的奇数。如果用户没有输入奇数，则输出一个消息进行说明
times = 0
temp = 0
while times < 10:
    num = int(input("Enter %d number" % times))
    if num > temp and num % 2 != 0:
        temp = num
    times += 1

if temp > 0:
    print("%d is max odd " % temp)
else:
    print("No odd number")
