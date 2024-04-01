#Artur Kazukevich
#Homework-4
#12.03.2024
#Grodno-IT-Academy-Python 3.10

# теперь тесты написаны с использованием библиотеки pytest
# нам нужно ее установить: pip install pytest
# и запустить как обычный файл: pytest test_Homework4.py
# Теперь вы будете знакомы со вторым инструментом для тестирования


#Выведите n-ое число Фибоначчи, используя только временные переменные, циклические операторы и условные операторы. n - вводится.
def fibonacci(n):
    if n <= 0:
        return None
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a = 0
        b = 1
        for _ in range(2, n):
            fib = a + b
            a = b
            b = fib
        return fib


#Определите, является ли число палиндромом (читается слева направо и справа налево одинаково). Число положительное целое, произвольной длины. Задача требует работать только с числами (без конвертации числа в строку или что-нибудь еще).
def palindrome(n):
    if n < 0:
        return False
    temp = n
    rev = 0
    while temp > 0:
        rev = rev * 10 + temp % 10
        temp = temp // 10
    return n == rev


#Напишите генератор, который возвращает цифры от S до N, но вместо чисел, кратных 3 пишет Fizz, вместо чисел кратный 5 пишет Buzz, а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz.
def fizz_buzz(S, N):
    if S <= N:
        for i in range(S, N + 1):
            if i % 3 == 0 and i % 5 == 0:
                yield 'FizzBuzz'
            elif i % 3 == 0:
                yield 'Fizz'
            elif i % 5 == 0:
                yield 'Buzz'
            else:
                yield str(i)
    else:
        for i in range(S, N - 1, -1):
            if i % 3 == 0 and i % 5 == 0:
                yield 'FizzBuzz'
            elif i % 3 == 0:
                yield 'Fizz'
            elif i % 5 == 0:
                yield 'Buzz'
            else:
                yield str(i)
