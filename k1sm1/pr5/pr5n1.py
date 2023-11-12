a=input("Введите текст: ")
s=a.split()
k= 0
for s in s:
    if s.lower().startswith('е') or s.lower().startswith('Е'):
        k+=1
print(k)
