"""
Verificador de Número Primos
"""
from tkinter import Label, Scale, HORIZONTAL, Button, StringVar, Tk
app = Tk()
app.title('Números primos')
app.geometry('500x300')


def verificar_numero():
    """
    Checa os divisores de um número da escala.
    Se a quantidade de divisores for 2, o número é primo.
    :return: Configura a variável texto para "Sim!" ou "Não!".
    """
    divisores = int()
    num = definidor.get()
    for contador in range(1, num + 1):
        if num % contador == 0:
            divisores = divisores + 1
    if divisores == 2:
        return texto.set('Sim!')
    return texto.set('Não!')

Label(text='Valor', bg='white', foreground='black',
      relief='groove').pack(padx=0, pady=10, ipadx=30, ipady=0)

definidor = Scale(app, from_=0, to=100, orient=HORIZONTAL)
definidor.set(50)
definidor.pack(padx=50, pady=10, ipadx=100, ipady=0, side='top')

Button(text='Verificar', command=verificar_numero)\
      .pack(padx=3, pady=0, ipadx=10, ipady=10)

Label(text='É número primo?', bg='white', relief='flat')\
      .pack(padx=0, pady=30, ipadx=20, ipady=0)

texto = StringVar()
Label(textvariable=texto, bg='white', fg='black',
                  relief='solid').pack(padx=0, pady=0, ipadx=20, ipady=0)

app.mainloop()
