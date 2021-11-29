"""
Clássico da Média
"""
from tkinter import Tk, Label, Button, Entry, W


def imprimir_dados():
    """
    :return: Faz a entrada das notas, o cálculo da média e cria a label que
             mostrará o resultado.
    """
    nota1 = float(entrada1.get())
    nota2 = float(entrada2.get())
    media = (nota1+nota2) / 2
    Label(app, text=media, background='white',
                   foreground='black', anchor=W).place(x=30, y=200, width=100, height=30)


app = Tk()
app.title('Clássico da Média')
app.geometry('500x300')

Label(app, text='Nota 1').place(x=10, y=10, width=100, height=30)
entrada1 = Entry(app)
entrada1.place(x=30, y=35, width=200, height=20)
Label(app, text='Nota 2').place(x=10, y=70, width=100, height=30)
entrada2 = Entry(app)
entrada2.place(x=30, y=100, width=200, height=20)

Button(app, text='Calcular Média', command=imprimir_dados).place(x=30, y=150, width=100, height=20)
Button(app, text='Encerrar Programa', command=exit).place(x=200, y=150, width=120, height=20)

app.mainloop()
