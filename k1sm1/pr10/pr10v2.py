'''1 Дана целая квадратная матрица n-го порядка. Определить, является ли
она магическим квадратом, т. е. такой матрицей, в которой суммы
элементов во всех строках и столбцах одинаковы.'''
N = 3
with open('C:/Users/Admin/Desktop/cods/PL-Levsha/k1sm1/pr10/levshadaniil_ub32_vvod_v2.txt') as f:
    A=[]
    c=0
    while c<3:
        for line in f:
            B=list(map(int,line.split()))
            A.append(B)
        c+=1
    s =0
    for i in range(N):
        s += A[0][i]
    b = "да является"
    for i in range(N):
        s1 = 0
        s2 = 0
        for j in range(N):
            s1 += A[i][j]
            s2 += A[j][i]
        if s1 != s or s2 != s:
            b = "нет не является"
            break
    with open('C:/Users/Admin/Desktop/cods/PL-Levsha/k1sm1/pr10/levshadaniil_ub32_vivod_v2.txt', 'w') as g:
        g.write(b)
#2  Дана прямоугольная матрица A[N, N]. Переставить первый и последний столбцы местами и вывести на экран.
    N = 3
    M = 4
    with open('C:/Users/Admin/Desktop/cods/PL-Levsha/k1sm1/pr10/levshadaniil_ub32_vvod_v2.txt') as f:
        A=[]
        f.seek(21)
        for line in f:
            B=list(map(int,line.split()))
            A.append(B)
    for i in range(N):
        t = A[i][0]
        A[i][0] = A[i][M-1]
        A[i][M-1] = t
    with open('C:/Users/Admin/Desktop/cods/PL-Levsha/k1sm1/pr10/levshadaniil_ub32_vivod_v2.txt', 'a') as g:
        g.write('\n')
        for i in range(N):
            for j in range(M):
                g.write(' ')
                g.write(str(A[i][j]))
            g.write('\n')