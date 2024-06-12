<p style="font-weight: bolder;font-size: 40px;line-height: 40px;">Python入门学习</p>


# 一、Python安装

官网：https://www.python.org/

# 二、Python数据类型与变量

## 2.1 字面量

在代码中，被写下来的固定的值。

常用的6种数据类型：<br>

|       类型       |                       描述                        | 说明                                                         |
| :--------------: | :-----------------------------------------------: | :----------------------------------------------------------- |
|   数字(Number)   | 支持：整数int、浮点数float、复数complex、布尔bool | 整数：如10、-10；<br>浮点数：如13.14、-13.14；<br>复数：如4+3j，以j结尾表示复数；<br>布尔：表示生活中的逻辑，即真和假True表示真，False表示假 |
|  字符串(String)  |              描述文本的一种数据类型               | 字符串有人以数量的字符组成                                   |
|    列表(List)    |                `有序的` `可变序列`                | Python中使用最频繁的数据类型，可有序记录一堆数据             |
|   元组(Tuple)    |               `有序的` `不可变序列`               | 可有序记录一堆不可变的Python数据集合                         |
|    集合(Set)     |                `无序` `不重复`集合                | 可无序记录一堆不重复的Python数据集合                         |
| 字典(Dictionary) |                `无序`Key-Value集合                | 可无序记录一堆Key-Value型的Python数据集合                    |

```python
print(6666)
print("白马程序员")
```

## 2.2 注释

注释的分类：<br>
* 单行注释：以 **#开头**，#右边的所有文字当做说明
* 多行注释：以 **“”“开头 """结尾**，一般用于解释在整个Python代码文件、类或方法。

```python
# 单行注释
print(6666)

"""
多行注释
注释内容
"""
def hello(arg):
    print(arg)

```

## 2.3 变量

在程序运行时，能存储计算结果或能表示值的抽象概念。

格式：变量名称=变量的值

```python
money=10

print("你有",money,"块钱")

```

## 2.4 数据类型

* 如何验证变量的数据类型？
使用type(变量名)

```python
age = 10
height = 1.78

print(type(age))
print(type(height))

```

## 2.5 数据类型转换

常见的转换语句：

|函数|说明|
|:----:|:---:|
|int(x)|将x转换成一个整数|
|float(y)|将y转换成一个浮点数|
|str(x)|将对象转换成字符串|

```python
x = 13.14
y = 10

print(int(x))

print(float(y))

print(type(y), str(y))

```

## 2.6 标识符

如变量的名字、方法的名字、类的名字等。

## 2.7 变量名命名规范

* 见名知意。
* 多个单词组合的变量名，使用下划线分割。
* 英文字母全小写

```python
person_name="张三"

def say_hello():
    print("Hello World")

def find_element_by_id(user_id):
    print(user_id)
```

## 2.8 算术运算符

+、-、*、/、//(取整运算符）、%(取模运算符)、**(指数)

+=、-=、*=、/=、%=、**=、//=

```python
print(1 + 1)
print(1 - 1)
print(1 * 9)
print(4 / 2)
print(9 % 2)
print(8 // 3)
print(2 ** 3)

c = 4
c += 1
print(c)

```

## 2.9 字符串扩展
 
字符串三种定义方式：<br>
* 单引号定义法 name='白马'
* 双引号定义法 name="白马"
* 三引号定义法 name="""白马""

字符串拼接：通过+来拼接 print("白马"+"王子")。

字符串格式化：<br>
* %s ， %表示占位，s表示将变量变成字符串放入占位的地方。
* f"内容{变量名}"

```python
name = "白马王子"
message = "学IT就来%s" % name

print(message)

age = 18
sex = "男"
message1 = "张三年龄%d,性别%s" % (age, sex)
print(message1)

math_score=90
stu_name="zs"
print(f"{stu_name}的数学成绩为{math_score}")

```

格式精度：<br>
格式：%m.nd。m表示控制宽度，n表示控制小数点精度

```python
num = 12.345
print("%3.2f" % num)
```

## 2.10 数据输入

使用input()

```python
name = input()
print(name)

age = input("你的年龄：")
print(age)

```

# 三、条件与循环

## 3.1 条件判断

* if 条件:
* if 条件: else ...
* if 条件: elif 条件:  
* if 条件: elif 条件: else ....

```python
age = 12

if age < 12:
    print("age小于12")
else:
    print("age等于12")

score = 90
if score < 80:
    print("c")
elif score < 90:
    print("b")
else:
    print("a")
```

## 3.2 循环
* while 条件:
* for i in range(start,end,step): 或 for i in 字符串变量名

循环中断:break continue

break和continue的区别：<br>
break会退出循环<br>
continue只会终止当前循环，然后进入下一轮循环

```python
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

```




