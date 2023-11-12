#1
n=int(input('введите n ' ))
sp = [ int(input('введите числа массива ')) for i in range(n) ] 
print(sp.index(min(sp))) #определение минимального элемента и вывод его индекса
#2
sp1=[1,343,-1,-5,543,222,-44]
sp2=[];sp3=[] 
for i in sp1: 
    if i>0:
        sp2.append(i)
    elif i<0:
        sp3.append(i)
print(sp2)
print(sp3)