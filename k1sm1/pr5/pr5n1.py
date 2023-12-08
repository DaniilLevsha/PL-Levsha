a=input("Введите текст: ")
s=a.split()
k= 0
for s in s:
    if s.startswith('е') or s.startswith('Е'):
        k+=1
print(k)
