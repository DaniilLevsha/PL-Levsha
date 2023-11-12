'''1. Два натуральных числа называются «дружественными», если каждое из них
равно сумме всех делителей (кроме его самого) другого (например, числа 220 и
284). Найти все пары «дружественных» чисел, которые не больше данного
числа N.'''
def f(z):
    for i in range(z, 1, -1): 
        k = 0
        n = 0
        for x in range(1, i): 
            if i % x == 0:
                k += x
        for j in range(1, k): 
            if k % j == 0:
                n += j
        if i == n and i != k and i == min(i, k): 
            print(i, k)
n=int(input('введите n>=300 '))
f(n)
'''2. Даны длины сторон треугольника a, b, c. Найти медианы треугольника,
сторонами которого являются медианы исходного треугольника. Для
вычисления медианы проведенной к стороне а, использовать формулу
Вычисление медианы оформить в виде процедуры.'''
def f2(m, n, k): 
    global a, b, c
    a = (2 * (n ** 2 + k ** 2) - m ** 2) ** 0.5 / 2 
    b = (2 * (m ** 2 + k ** 2) - n ** 2) ** 0.5 / 2
    c = (2 * (m ** 2 + n ** 2) - k ** 2) ** 0.5 / 2

print('введите стороны треугольника')
a, b, c = map(int, input().split()) 
if a < b + c and b < a + c and c < a + b:
    f2(a, b, c)
    f2(a, b, c)
    print(round(a, 2), round(b, 2), round(c, 2))
else:
    print('треугольник с такими сторонами не существует')