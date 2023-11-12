#1 Задана матрица порядка n и число к. Разделить элементы k-й строки на диагональный элемент, расположенный в этой строке
n = int(input("Введите размер матрицы: ")) 
k = int(input("Введите номер строки: "))
A = [] 
for i in range(n): 
    b=[]
    for i in range(n):
       b.append(int(input('введите элемент матрицы ')))
    A.append(b)
print('изначальная матрица')
for i in range(len(A)):
    print(A[i])
def f(A, k): 
    dg = A[k-1][k-1]
    for j in range(len(A[k-1])):
        A[k-1][j] /= dg
    return A
print("изменённая матрица ")
i=f(A,k)
for i in range(len(A)):
    print(A[i])
#2 Задана квадратная матрица. Получить транспонированную матрицу (перевернутую относительно главной диагонали) и вывести на экран.
m = [[3, 1, 4],
     [5, 5, 7],
     [5, 4, 8]]
print('изначальная матрица')
for i in m:
    print(i)
print()
n = 3
t = []
for i in range(n):
    t.append([0] * n) 
for i in range(n):
    for j in range(n):
        t[j][i] = m[i][j] 
print("изменённая матрица ")
for i in range(len(t)):
    print(t[i])