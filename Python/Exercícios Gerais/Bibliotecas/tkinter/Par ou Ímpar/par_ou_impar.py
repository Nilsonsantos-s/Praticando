"""
Par ou Ímpar
"""
from tkinter import Tk, Label, Button, Entry, StringVar
app = Tk()
app.title('Par ou Ímpar')
app.geometry('400x200')
app.configure(bg='brown')


def par_ou_impar():
    """
    :return: Recebe a entrada.
             Se resto do número divido por 2 for 0, a função vai configurar "Par" na variável resultado.
             Do contrário, vai configurar "Ímpar".
    """
    numero = int(entrada.get())
    if numero % 2 == 0:
        resultado.set('Par')
    else:
        resultado.set('Ímpar')

Label(text='Número', bg='white', fg='black', relief='groove').pack(ipadx=0, ipady=0)

entrada = Entry(app)
entrada.pack(ipadx=0, ipady=0, pady=10)
Button(text='Verificar', command=par_ou_impar,
       relief='groove', cursor='dot').pack(ipadx=0, ipady=0, padx=10, pady=10)
resultado = StringVar()
label_da_resposta = Label(textvariable=resultado, bg='white', fg='black',
                          font='Arial 15', relief='groove')
label_da_resposta.pack(ipadx=20, ipady=0, padx=10, pady=30)

app.mainloop()
