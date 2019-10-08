# -*-  coding: utf-8 -*-

# 3.1 穷举法 实际练习
'''
    编写一个程序，要求用户输入一个整数，然后输出两个整数 root 和 pwr ,满足 0 < pwr < 6
并且 root ** pwr 等于用户输入的整数。如果不存在这样的一个整数，则输出一条消息进行说明
'''

# 0 < pwr < 6
# root ** pwr == num  root <= num

num = int(input("请输入一个整数:"))
is_num = False  # 标记是否含有这样的整数
for pwr in range(1, 6):
    root = 0
    while root <= num:
        if root ** pwr == num:
            print("num = %d 时 root = %d, pwr = %d " % (num, root, pwr))
            is_num = True
            break
        root += 1

if not is_num:
    print("不存在这样的数")
