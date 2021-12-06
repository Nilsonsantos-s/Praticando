"""
Caixa de Mensagem
"""
from tkinter import Tk, StringVar, Entry, Button, messagebox
app = Tk()
app.title('Mensagem')
app.geometry('500x300')
app.configure(bg='orange')


def mostrar_mensagem():
    """
    Pega o dado da entrada, armazena uma string na variável mensagem e,
    utilizando condições, mostra uma mensagem na tela.
    """
    dado = entrada1.get()
    mensagem = 'Python/Tkinter'
    if dado == '1':
        messagebox.showinfo(title='Aviso', message=mensagem)
    elif dado == '2':
        messagebox.showwarning(title='Atenção', message=mensagem)
    else:
        messagebox.showerror(title='Erro', message='Valores aceitos: 1, 2')


def resetar():
    """
    Mostra uma mensagem com duas opções na tela. Se o usuário digitar "Resetar",
    será configurado na variável texto o valor '1'.
    """
    resposta = messagebox.askyesno('Resetar', 'Confirma o reset do Textbox?')
    if resposta is True:
        texto.set('1')

texto = StringVar()

entrada1 = Entry(textvariable=texto)
entrada1.pack()
Button(text='Pressionar', command=mostrar_mensagem).pack()
Button(text='Resetar', command=resetar).pack(pady=20)

app.mainloop()
