# 1 Вычислить число π c заданной точностью d
# *Пример:* 
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# k = 1
# x = 0
# for k in range(1, 1000000):
#     x = x+4*((-1)**(k+1))/(2*k-1)
# d = int(input('Задайте точность: '))
# print(round(x, d))



# 2 Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.
# *Пример*
# - при N=236 -> [2, 2, 59]

# def factor(n):
#     data = []
#     d = 2
#     while d * d<= n:
#         if n % d == 0:
#             data.append(d)
#             n //= d
#         else:
#             d += 1
#     if n > 1:
#         data.append(n)
#     return data

# n = int(input('Введите число N: '))
# print(f'при N = {n} -> ', factor(n))



# 3 Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.
# *Пример*
# - при [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]  -> [2, 4, 5, 9]


# data = [int(value) for value in input('Введите числа последовательно через пробел: ').split()]
# new_data = []
# a = [int(i) for i in data]
# for i in range(len(a)):
#    flag = 1
#    for j in range(len(a)):
#       if a[i] == a[j] and i != j:
#         flag = 0
#         break
#    if flag:
#       new_data.append(a[i])
# print(f'при {data} -> {new_data}')



# 4 Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# *Пример:* 
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# from random import *

# k = 2

# a = round(random()*10, )
# b = round(random()*10, )
# c = round(random()*10, )
# print(a, b, c)
# result = ''
# if b == 0: results = f"{a}*x**{k} + {c}*x**{k-2} = 0"
# if b == 0 and c == 0: result = f"{a}*x**{k} = 0"
# else: result = f"{a}*x**{k} + {b}*x**{k-1} + {c}*x**{k-2} = 0"

# with open("polynomial.txt", "w") as data:
#     data.write(result)



# 5 Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.
# Коэффициенты могут быть как положительными, так и отрицательными. Степени многочленов могут отличаться.

# import re
# import itertools


# file1 = 'polynom1.txt'
# file2 = 'polynom2.txt'
# file_sum = 'sum_polynom.txt'

# # Получение данных из файла

# def read_pol(file):
#     with open(str(file), 'r') as data:
#         pol = data.read()
#     return pol

# # Получение списка кортежей каждого (<коэффициент>, <степень>)

# def convert_pol(pol):
#     pol = pol.replace('= 0', '')
#     pol = re.sub("[*|^| ]", " ", pol).split('+')
#     pol = [char.split(' ') for char in pol]
#     pol = [[x for x in list if x] for list in pol]
#     for i in pol:
#         if i[0] == 'x': i.insert(0, 1)
#         if i[-1] == 'x': i.append(1)
#         if len(i) == 1: i.append(0)
#     pol = [tuple(int(x) for x in j if x != 'x') for j in pol]
#     return pol

# # Получение списка кортежей суммы (<коэф1 + коэф2>, <степень>)

# def fold_pols(pol1, pol2):   
#     x = [0] * (max(pol1[0][1], pol2[0][1] + 1))
#     for i in pol1 + pol2:        
#         x[i[1]] += i[0]
#     res = [(x[i], i) for i in range(len(x)) if x[i] != 0]
#     res.sort(key = lambda r: r[1], reverse = True)
#     return res

# # Составление итогового многочлена

# def get_sum_pol(pol):
#     var = ['*x^'] * len(pol)
#     coefs = [x[0] for x in pol]
#     degrees = [x[1] for x in pol]
#     new_pol = [[str(a), str(b), str(c)] for a, b, c in (zip(coefs, var, degrees))]
#     for x in new_pol:
#         if x[0] == '0': del (x[0])
#         if x[-1] == '0': del (x[-1], x[-1])
#         if len(x) > 1 and x[0] == '1' and x[1] == '*x^': del (x[0], x[0][0])
#         if len(x) > 1 and x[-1] == '1': 
#             del x[-1]
#             x[-1] = '*x'
#         x.append(' + ')
#     new_pol = list(itertools.chain(*new_pol))
#     new_pol[-1] = ' = 0'
#     return "".join(map(str, new_pol))

# def write_to_file(file, pol):
#     with open(file, 'w') as data:
#         data.write(pol)

# pol1 = read_pol(file1)
# pol2 = read_pol(file2)
# pol_1 = convert_pol(pol1)
# pol_2 = convert_pol(pol2)

# pol_sum = get_sum_pol(fold_pols(pol_1, pol_2))
# write_to_file(file_sum, pol_sum)

# print(pol1)
# print(pol2)
# print(pol_sum)