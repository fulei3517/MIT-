# -*-  coding: utf-8 -*-

# 假设s 是包含多个小数的字符串，由逗号隔开，如 s = '1.23,2.4,3.123' .编写一个程序，输出s中的说有数值的和

s = '1.23,2.4,3.123'
# 循环字符串中的所有字符
# 如果 字符不是‘，’ 就将字符拼接 如果是‘，’ 就将之前拼接的字符 转换为float 并累加到 total变量
# 最后因为最后面一个数字后面没有‘，’了 所以再把最后面一个数值加入就行了
total = 0.0  # 总和
temp = ""  # 临时保存数据
for item in s:
    if item == ",":
        total += float(temp)
        temp = ""
    else:
        temp += item

total += float(temp)
print("所有数值的和是 %s" % total)
