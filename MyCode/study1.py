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
for i in range(0, 20):
    for j in range(0, 33):
        k = 100 - i - j
        if i * 5 + j * 3 + k / 3 == 100:
            print(f'公鸡{i},母鸡{j},小鸡{k}')
