'''1. Вводим последовательность натуральных чисел (одно число в строке),
завершающаяся числом 0. Определите наибольшее значение числа в этой
последовательности. В этой задаче нельзя использовать глобальные
переменные и передавать какие-либо параметры в рекурсивную функцию.
Функция получает данные, считывая их с клавиатуры. Функция
возвращает единственное значение: максимум считанной
последовательности. Гарантируется, что последовательность содержит
хотя бы одно число (кроме нуля).'''
def f():
    a=int(input('введите число поледовательности '))
    if a==0: return 0
    else: maxn=max(a,f())
    return maxn
print(f())