"""
Calculadora
"""
from tkinter import Tk, StringVar, Label,\
    OptionMenu, Button, Entry
app = Tk()
app.title('Calculadora')
app.geometry('500x300')
app.configure(background='brown')


def calcular():
    """
    :return: Verifica a operação, recebe os valores de entrada, executa a
             operação e configura um valor na variável resultado.
    """
    operacao = texto.get()
    numero1 = int(entrada1.get())
    numero2 = int(entrada2.get())
    if operacao == 'Soma':
        resultado.set(numero1+numero2)
    elif operacao == 'Subtração':
        resultado.set(numero1-numero2)
    elif operacao == 'Multiplicação':
        resultado.set(numero1*numero2)
    elif operacao == 'Divisão':
        resultado.set(numero1/numero2)

calculos = ['Soma', 'Subtração', 'Multiplicação', 'Divisão']
texto = StringVar()

Label(text='CALCULADORA', bg='green', fg='black', font='Arial 15',
      relief='groove').place(x=150, y=0, width=200, height=30)
Label(text='Escolha uma operação', bg='blue',
      fg='white', relief='solid',
      font='Arial 10').place(x=260, y=50, width=200, height=30)
OptionMenu(app, texto, *calculos).place(x=300, y=85, width=120, height=30)

Label(text='Número 1').place(x=10, y=50, width=80, height=20)
entrada1 = Entry()
entrada1.place(x=100, y=50, width=80, height=20)
Label(text='Número 2').place(x=10, y=100, width=80, height=20)
entrada2 = Entry()
entrada2.place(x=100, y=100, width=80, height=20)
Button(text='Calcular', command=calcular).place(x=100, y=150, width=80, height=20)

resultado = StringVar()
Label(textvariable=resultado, bg='white', relief='solid',
      font='Arial 13').place(x=40, y=200, width=200, height=40)

app.mainloop()
