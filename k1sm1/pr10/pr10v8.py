#1 Задана матрица порядка n и число к. Разделить элементы k-й строки на диагональный элемент, расположенный в этой строке
with open('C:/Users/Admin/Desktop/cods/PL-Levsha/k1sm1/pr10/levshadaniil_ub32_vvod_v8.txt') as f:
    k=int(f.readline())
    A = []
    n=3
    c=0
    while c<3:
        for line in f:
            B=list(map(int,line.split()))
            A.append(B)
        c+=1
    def l(A, k): 
        dg = A[k-1][k-1]
        for j in range(len(A[k-1])):
            A[k-1][j] /= dg
        return A
    l(A,k)
    with open('C:/Users/Admin/Desktop/cods/PL-Levsha/k1sm1/pr10/levshadaniil_ub32_vivod_v8.txt', 'w') as g:
        for i in range(n):
            for j in range(n):
                g.write(' ')
                g.write(str(A[i][j]))
            g.write('\n')
#2 Задана квадратная матрица. Получить транспонированную матрицу (перевернутую относительно главной диагонали) и вывести на экран.
with open('C:/Users/Admin/Desktop/cods/PL-Levsha/k1sm1/pr10/levshadaniil_ub32_vvod_v8.txt') as f:
    f.seek(24)
    m=[]
    for line in f:
            B=list(map(int,line.split()))
            m.append(B)
    n = 3
    t = []
    for i in range(n):
        t.append([0] * n) 
    for i in range(n):
        for j in range(n):
            t[j][i] = m[i][j] 
    with open('C:/Users/Admin/Desktop/cods/PL-Levsha/k1sm1/pr10/levshadaniil_ub32_vivod_v8.txt', 'a') as g:
        g.write('\n')
        for i in range(n):
            for j in range(n):
                g.write(' ')
                g.write(str(t[i][j]))
            g.write('\n')