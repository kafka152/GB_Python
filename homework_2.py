# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 0,56 -> 11


num_to_sum = input('Введите вещественное число: ')
sum = 0
for i in num_to_sum:
    if i.isdigit():
        sum += int(i)
print(sum)


# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def count_factorial(n): 
    if n==1:
        return 1
    else:
        return n * count_factorial(n - 1)

fact_num = int(input('Введите число: '))
result = []
while fact_num >= 1:
    result.append(count_factorial(fact_num))
    fact_num -= 1

result.reverse()
print(result)

# Задайте список из k чисел последовательности (1 + 1\k)^k и выведите на экран их сумму.

k_num = int(input('Введите число: '))
k = 1
while k <= k_num:
    print(f'{k}:',(1 + 1/k) ** k)
    k += 1

# Задайте список из N элементов, заполненных числами из промежутка [-N, N].

n = int(input('Введите число: '))

rang_step = len(range(-n, n+1)) // n
numbers_list = list(range(-n, n+1, rang_step))
numbers_list.pop((len(numbers_list)//2))

print(numbers_list)

# Найдите произведение элементов на указанных пользователем через пробел позициях.

user_list = input('Введите список индексов для перемножения: ')
result = 1
for i in user_list.split(' '):
    result *= numbers_list[int(i)]

print(result)

# Реализуйте алгоритм перемешивания списка.

import random


list = input('Введите элементы массива через пробел: ').split(' ')

list_len=len(list)
for i in range(list_len):
    rand_item = random.randint(0, list_len-1)
    item=list.pop(rand_item)
    list.append(item)

print(list)
