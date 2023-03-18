"""温度转换"""
# f = float(input('请输入华氏温度:'))
# c = (f - 32) / 1.8
# print(f'华氏温度为{f:.1f},摄氏度为{c:.1f}')

"""计算圆的周长和面积"""
# import cmath
# r = float(input('请输入圆的半径:'))
# d = 2 * cmath.pi * r
# s = cmath.pi * r * r
# print(f'圆的周长={d:.2f},面积={s:.2f}')

"""算闰年"""
# year = int(input('年'))
# if year%4 == 0 and year%100 != 0 or year%400 == 0:
#     print(f'{year}是闰年')
# else:
#     print(f'{year}不是闰年')

"""判断成绩等级"""
# grade = float(input('请输入成绩：'))
# if grade >= 90:
#     scare = 'A'
# elif grade >=80:
#     scare = 'B'
# elif grade >= 70:
#     scare = 'C'
# elif grade >= 60:
#     scare = 'D'
# else:
#     scare = 'E'
# print(f'成绩{grade},等级{scare}')

"""计算三角形面积和周长"""
# a = float(input('a='))
# b = float(input('b='))
# c = float(input('c='))
# if a + b > c and a + c > b and b + c > a:
#     d = a + b+ c
#     p = d / 2
#     s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
#     print(f'周长{d},面积{s:.2f}')
# else:
#     print('无法构成三角形')

"""99乘法表"""
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print('%d*%d=%d' % (i, j, i * j), end='\t')
#     print()

"""打印**"""
# row = int(input('请输入行数: '))
# for i in range(row):
#     for _ in range(i + 1):
#         print('*', end='')
#     print()
#
#
# for i in range(row):
#     for j in range(row):
#         if j < row - i - 1:
#             print(' ', end='')
#         else:
#             print('*', end='')
#     print()
#
# for i in range(row):
#     for _ in range(row - i - 1):
#         print(' ', end='')
#     for _ in range(2 * i + 1):
#         print('*', end='')
#     print()


"""寻找水仙花数"""
# for num in range(100,1000):
#     a = num // 100   # //是整除取商，%是取余数
#     b = num // 10 % 10
#     c = num % 10
#     if a ** 3 + b ** 3 + c ** 3 == num:
#         print(num)

"""公鸡5元一只，母鸡3元一只，小鸡1元三只，用100块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只？"""
# for i in range(0, 20):
#     for j in range(0, 33):
#         k = 100 - i - j
#         if i * 5 + j * 3 + k / 3 == 100:
#             print(f'公鸡{i},母鸡{j},小鸡{k}')

"""赌博游戏"""

# money = 1000
# while money > 0:
#     need_go_on = False
#     print('你的总资产为:', money)
#     while True:
#         debt = int(input('押注'))
#         if 0 < debt <= money:
#             break
#     firstNum = random.randint(1, 6) + random.randint(1, 6)
#     print(f'第1次点数{firstNum}')
#     if firstNum == 7 or firstNum == 11:
#         print(f'{firstNum}点，玩家胜')
#         money += debt
#     elif firstNum == 2 or firstNum == 3 or firstNum == 12:
#         print(f'{firstNum}点，庄家胜')
#         money -= debt
#     else:
#         need_go_on = True
#         n = 1
#         while need_go_on:
#             n += 1
#             need_go_on = False
#             Num = random.randint(1, 6) + random.randint(1, 6)
#             print(f'第{n}次点数{Num}')
#             if Num == 7:
#                 print(f'{Num}点,庄家胜')
#                 money -= debt
#             elif Num == firstNum:
#                 print(f'{Num}点,玩家胜')
#                 money += debt
#             else:
#                 need_go_on = True
# print('破产')
# import flag
# import random
# import math


"""WYS发我的竞赛题"""
# flag = '02}8c ms13'
# length = len(flag)
# print(length)
# temp = [i for i in range(length)]
# result = ''
# for j in range(0, 15):
#     for i in range(1, length):
#         temp[(2 * i) % length] = flag[i]
#     flag = temp[:]
# print(temp)
# out = ''
# for i in range(len(temp)):
#     out += str(temp[i])
# print(out[:10])
# b = random.randint(0, length)
# while True:
#     a = random.randint(0, length)
#     if math.gcd(a, length) == 1:
#         break
# print(a, b)
# cipher = []
# for i in out:
#     c = (ord(i) * a + b)
#     cipher.append(c)
# print(cipher)


def foo():
    pass


def bar():
    pass


# __name__是Python中一个隐含的变量它代表了模块的名字
# 只有被Python解释器直接执行的模块的名字才是__main__
if __name__ == '__main__':
    print('call foo()')
    foo()
    print('call bar()')
    bar()

