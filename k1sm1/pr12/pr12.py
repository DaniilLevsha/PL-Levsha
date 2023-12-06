from tkinter import *
import json
import requests

def g():
    n = e.get()
    url = f'https://api.github.com/repos/kubernetes/{n}'
    z = requests.get(url)
    z=z.json()
    k = ('company', 'created_at', 'email', 'id', 'name', 'url')
    sl = dict()
    for j in k:
        sl[j] = z.get(j,'None')
    with open('C:/Users/Admin/Desktop/cods/PL-Levsha/k1sm1/pr12/vivod.json', 'w') as f:
        f.write(json.dumps(sl, indent=1))

app = Tk()
app.title('LevshaDaniil')
app.geometry('720x480')

l = Label(app, text="Введите имя репозитория:")
l.pack(pady=10)

e = Entry(app)
e.pack(pady=10)

b = Button(app, text="Получить информацию", command=g)
b.pack(pady=10)

app.mainloop()