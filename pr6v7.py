#номер 1
a = [1, 3, 4, 5, 25, 24, 53, 3753, 34, 23, 54, 2645]
s = 0
u = 1
for i in range(len(a)): 
    if i % 2 == 0:
        s += a[i] 
    else:
        u *= a[i]
print(s, u)
#номер 2
mas = [1, 3, 4, 26, 2, 234, 53, 25, 3, -124]
maxs = 0
mins = 0
for i in range(len(mas)):
    if mas[i] <= min(mas): 
        mins = i
    elif mas[i] >= max(mas): 
        maxs = i
mas[mins], mas[maxs] = mas[maxs], mas[mins] 
print(mas)