# 2. Напишите программу, которая принимает на вход число N и выдает 
# набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

N = int(input('Введите число N: '))

def Factorial(n):
    i = 1
    multi = 1
    while i < n + 1:
        multi *= i
        print(multi, end=' ')
        i += 1

Factorial(N)