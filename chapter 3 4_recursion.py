def countdown(i): #рекурсивная функция обратного отсчета
    print i
    if i<=1:
        return
    else:
        countdown(i-1)

def fact(x): #рекурсивная функция факториал
    if x == 1:
        return 1
    else:
        return x * fact(x-1)
    
def sum(list): #рекурсивная функция суммы
    if list == []:
        return 0
    return list[0] + sum(list[1:])

def count(list): #рекурсивная функция подсчета элементов в списке
    if list == []:
        return 0
    return 1 + count(list[1:])

def max(list): #рекурсивная функция поиска максимального числа в списке
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    sub_max = max(list[1:])
    return list[0] if list[0] > sub_max else sub_max

def fib(n): #рекурсивная функция числа Фибоначчи
    fib0, fib1, fib2 = 0, 1, 1
    if n == 0:
        return fib0
    elif n == 1:
        return fib1
    elif n == 2:
        return fib2
    return fib(n-1)+fib(n-2)

def quicksort(array): #быстрая сортировка
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i < pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + pivot + quicksort(greater)

def power(a, n): #рекурсивная функция возведения в степень
    if n == 0:
        return 1
    return a * power(a, n-1)

def reversal(): #рекурсивная функция разворота последовательности
    x = int(input())
    if x == 0:
        return print (x)
    else:
        reversal()
    return print(x) 