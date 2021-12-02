"""
Identificador de Maior ou Menor número
"""
from tkinter import StringVar, Label, Entry, Tk, Button
app = Tk()
app.title('Maior e Menor')
app.geometry('300x200')


def imprimir_resultado():
    """
    :return: Recebe os números das entradas, faz a comparação
             um do outro e retorna se são iguais, ou se um
             número é menor ou maior que o outro.
    """
    numero1 = entrada1.get()
    numero2 = entrada2.get()
    if not numero1 or not numero2:
        textolabel.set('')
    elif numero1 > numero2:
        textolabel.set('Número 1 é maior.')
    elif numero2 > numero1:
        textolabel.set('Número 2 é maior.')
    else:
        textolabel.set('Ambos são iguais.')


textolabel = StringVar()

Label(text='Número 1', bg='white', relief='groove').grid(column=0, row=0)
Label(text='Número 2', bg='white', relief='groove').grid(column=1, row=0, padx=50)

entrada1 = Entry()
entrada1.grid(column=0, row=1, padx=10)

entrada2 = Entry()
entrada2.grid(column=1, row=1)

Button(text='Verificar', command=imprimir_resultado)\
    .place(x=118, y=80, width=60, height=30)

Label(textvariable=textolabel, bg='white', relief='flat',
      font='Arial 9').place(x=100, y=130, width=105, height=30)

app.mainloop()
