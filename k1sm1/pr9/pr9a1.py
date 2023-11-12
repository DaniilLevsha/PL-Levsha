#1. Дано натуральные числа Х,N Вычислить выражение вида: x^n / n!.
def f (n):
    if (n <= 1):
        return 1
    else:
        return (n * f(n-1))
x=10
n=5
print((x**n)/f(n))