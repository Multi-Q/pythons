import random

num = 10

# while num > 0:
#     print(num)
#     num -= 1

"""
猜数字
"""
# real_num = random.randint(1, 100)
# while True:
#     guess_num = int(input("猜数字:"))
#     if guess_num < real_num:
#         print("小了")
#     elif guess_num > real_num:
#         print("大了")
#     elif guess_num == real_num:
#         print("恭喜你猜对了，正确答案为：%s" % real_num)
#         break

"""
九九乘法表
"""
# i = 1
# while i <= 9:
#     j = 1
#     while j <= i:
#         print("%d*%d=%2d " % (j, i, i * j), end=" ")
#         if i == j:
#             print()
#         j += 1
#     i += 1


java = "java"
for i in java:
    print(i)

for i in range(10):
    print(i, end=" ")
print()

for i in range(1, 10):
    print(i, end=" ")
print()

for i in range(1, 10, 2):
    print(i, end=" ")
print()

count = 0
for i in range(1, int(input("输入一个数")) + 1):
    if i % 2 == 0:
        count += 1
print("一共有%d个偶数" % count)


