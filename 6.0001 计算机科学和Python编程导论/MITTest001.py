# 2.2 程序分支 练习题
# 检查3个变量 x,y,z 输出其中最大的奇数。如果其中没有奇数，就输出一个消息进行说明

x = int(input("请输入 x = "))
y = int(input("请输入 y = "))
z = int(input("请输入 z = "))

print("x = %s y = %s z = %s" % (x, y, z))
print(type(z))
# 如果 x
# if x > y and x > z:
#     if x % 2 != 0:
#         print("x = %s 为最大的奇数" % x)
#     elif y > z:
#         if y % 2 != 0:
#             print("y = %s 为最大的奇数" % y)
#         elif z % 2 != 0:
#             print("y = %s 为最大的奇数" % y)
#         else:
#             print("没有奇数")
#     elif z % 2 != 0:
#         print("y = %s 为最大的奇数" % y)
#     else:
#         print("没有奇数")
# elif y > z:
#     if y % 2 != 0:
#         print("y = %s 为最大的奇数" % y)
#     elif z > x and z % 2 != 0:
#         print("z = %s 为最大的奇数" % z)
#     elif x % 2 != 0:
#         print("x = %s 为最大的奇数" % x)
#     else:
#         print("没有奇数")
# elif z % 2 != 0:
#     print("z = %s 为最大的奇数" % z)
# elif y % 2 != 0:
#     print("y = %s 为最大的奇数" % y)
# elif x % 2 !=0:
#     print("x = %s 为最大的奇数" % x)
# else:
#     print("没有奇数")


if x > y and x > z and x % 2 != 0:
    print("x = %s 为最大的奇数" % x)
elif y > z and y % 2 != 0:
    print("y = %s 为最大的奇数" % y)
elif z % 2 != 0:
    print("z = %s 为最大的奇数" % z)
elif y % 2 != 0:
    print(" = %s 为最大的奇数" % y)
elif x % 2 != 0:
    print("x = %s 为最大的奇数" % x)
else:
    print("没有奇数")
