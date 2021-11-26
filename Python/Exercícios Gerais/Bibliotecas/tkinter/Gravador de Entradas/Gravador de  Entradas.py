from tkinter import *
app = Tk()
app.title('Gravador de Entradas')
app.geometry('800x500')
app.configure(background='#008')

cd = 'entradas.txt'

try:
    arquivo = open(cd, 'r')
except FileNotFoundError:
    arquivo = open(cd, 'x', encoding='utf8')

def impDados():
    arquivo = open(cd, 'a', encoding='utf8')
    arquivo.write(f'Nome: {entrada.get()}')
    arquivo.write('\n')
    arquivo.write(f'Telefone: {entrada2.get()}')
    arquivo.write('\n')
    arquivo.write(f'Observação: {entradatexto.get("1.0", END)}')
    arquivo.write('\n')
    arquivo.write('\n')
    arquivo.close()

txt1=Label(app, text= 'Nome', background='#fff', foreground='#008', anchor=W).place(x=10, y=20, width=150, height=30)
entrada = Entry(app)
entrada.place(x=10, y=60, width=150, height=20)

txt2=Label(app, text= 'Telefone', background='#fff', foreground='#008', anchor=W).place(x=10, y=130, width=150, height=30)
entrada2 = Entry(app)
entrada2.place(x=10, y=170, width=150, height=20)


txt3=Label(app, text= 'Observação', background='#fff', foreground='#008', anchor=W).place(x=10, y=220, width=150, height=30)
entradatexto= Text(app)
entradatexto.place(x=10, y=260, width=300, height=50)

Button(app, text='Gravar', command=impDados).place(x=10, y=350, width=270, height=20)


app.mainloop()