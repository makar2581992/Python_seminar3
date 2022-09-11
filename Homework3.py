# 1 Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint
list = []
for i in range(6):
   list.append(randint(0, 10))
print(list)
total = 0
for i in range(len(list)):
   if i%2 != 0:  
       total += list[i]
print(total)        





# 2.Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# from random import randint
# list = []
# for i in range(6):
#    list.append(randint(0, 10))
# print(list)
# def mult_list(list):
#    l = len(list)//2 + 1 if len(list) % 2 != 0 else len(list)//2
#    new_list = [list[i]*list[len(list)-i-1] for i in range(l)]
#    print(new_list)
# mult_list(list)





# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19




# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# n = int(input('Введите число десятичное число: '))
# b = ''
# while n > 0:
#     b = str(n % 2) + b
#     n = n // 2
# print(f'В двоичной системе: {b}')





# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

#n = int(input('Введите число: '))

#def get_fibonacci(n):
#    fibo_nums = []
#    a, b = 1, 1
#    for i in range(n-1):
#        fibo_nums.append(a)
#        a, b = b, a + b
#    a, b = 0, 1
#    for i in range (n):
 #       fibo_nums.insert(0, a)
#        a, b = b, a - b
#    return fibo_nums

#fibo_nums = get_fibonacci(n)
#print(get_fibonacci(n))