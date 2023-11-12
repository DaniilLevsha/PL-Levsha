a=int(input('введите число: '))
b=int(input('введте число: '))
for i in range(a,b-1,-1):
    if i%2!=0:
        print(i)