# -*-  coding: utf-8 -*-

# 2.4 迭代 练习
# 1。 使用while 替换下面代码中的注释内容
numXs = int(input("How many times should I print the letter X?"))
toPrint = ""
# concatenate X to toPrint numXs times 使用while 替换这里的内容
while abs(numXs) > 0:
    toPrint += "X"
    numXs = abs(numXs) - 1
print(toPrint)

