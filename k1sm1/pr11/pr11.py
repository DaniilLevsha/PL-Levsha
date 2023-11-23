from tkinter import *
from tkinter import messagebox
from tkinter import filedialog 
from tkinter import scrolledtext
from tkinter.ttk import *

def click1():
    t = int(txt.get())
    t1 = int(txt1.get())
    c = sp.get()
    if c == '+':
        Label(tab1, text=t + t1).grid(column=7, row=2)
    elif c == '-':
        Label(tab1, text=t - t1).grid(column=7, row=2)
    elif c == '*':
        Label(tab1, text=t * t1).grid(column=7, row=2)
    elif c == '/':
        Label(tab1, text=t / t1).grid(column=7, row=2)

def bc():
    messagebox.showinfo('','вы выбрали вариант: '+str(selected.get()))


def f():
    file = filedialog.askopenfilename()
    if file:
        with open(file, 'r') as f:
            content = f.read()
        text_area = scrolledtext.ScrolledText(tab3, width=40, height=10)
        text_area.insert('1.0', content)
        text_area.grid(column=0, row=0)
    
app = Tk()
app.title('LevshaDaniil')
app.geometry('720x480')
tab_control = Notebook(app)
tab1 = Frame(tab_control)
tab2 = Frame(tab_control)
tab3 = Frame(tab_control)
tab_control.add(tab1, text='1')
tab_control.add(tab2, text='2')
tab_control.add(tab3, text='3')
tab_control.pack(expand=1, fill='both')

Label(tab1, text='калькулятор', font=20).grid(column=4, row=0)
txt = Entry(tab1, width=5)
txt.grid(column=3, row=2)
sp = Combobox(tab1, values=('+', '-', '*', '/'))
sp.grid(column=4, row=2)
txt1 = Entry(tab1, width=5)
txt1.grid(column=5, row=2)
Label(tab1, text='=').grid(column=6, row=2)
k = Button(tab1, text='рассчитать', command=click1)
k.grid(column=4, row=3)

Label(tab2, text='выберите', font=20).grid(column=2, row=0)
selected = IntVar()
ck1 = Radiobutton(tab2, text='один', value=1, variable=selected).grid(column=1, row=2)
ck2 = Radiobutton(tab2, text='два', value=2, variable=selected).grid(column=2, row=2)
ck3 = Radiobutton(tab2, text='три', value=3, variable=selected).grid(column=3, row=2)
b = Button(tab2, text='Тык', command=bc).grid(column=2, row=3)

menu = Menu(tab3)
new_item = Menu(menu, tearoff=0)
new_item.add_command(label='Новый', command=f)
menu.add_cascade(label='Файл', menu=new_item)
app.config(menu=menu)

app.mainloop()


