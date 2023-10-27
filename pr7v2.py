#номер 1
def s3(a):return(3**0.5*a*a)/4 # функция поиска площади треугольника
a=int(input('введите а: '))
print(round(6*s3(a),2))
#номер 2
i=0
while i<3:
    print('введите стороны прямоугольника')
    a, b = map(float, input().split())
    i+=1
    print(a*b)