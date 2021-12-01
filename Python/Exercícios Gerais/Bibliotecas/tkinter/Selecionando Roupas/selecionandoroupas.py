"""
Selecionando Roupas
"""
from tkinter import Label, Tk, StringVar, Radiobutton, Button
app = Tk()
app.title('Botões-rádio')
app.geometry('500x300')

Label(text='Roupas').grid(row=1, column=0)
Label(text='Cores').grid(row=1, column=2)


def imprimir_resultado():
    """
    :return: Configura o valor da variável "vroupa" e "vcor" na variável "textolabel".
    """
    textolabel.set(vroupa.get() + ' ' + vcor.get())


vroupa = StringVar()
vcor = StringVar()
textolabel = StringVar()

rb_futebol = Radiobutton(app, text='Camiseta', value='Camiseta', variable=vroupa)
rb_futebol.grid(row=2, column=0, padx=120)
rb_volei = Radiobutton(app, text='Calça', value='Calça', variable=vroupa)
rb_volei.grid(row=3, column=0)
rb_basquete = Radiobutton(app, text='Sandália', value='Sandália', variable=vroupa)
rb_basquete.grid(row=4, column=0)

Radiobutton(app, text='Vermelho', value='vermelha',
                          variable=vcor).grid(row=2, column=2, padx=0)

Radiobutton(app, text='Verde', value='verde',
                       variable=vcor).grid(row=3, column=2, padx=0)

botao = Button(app, text='Botão', command=imprimir_resultado)
botao.place(x=200, y=150, width=120, height=20)

Label(textvariable=textolabel, bg='white',
                  font='Arial 13').place(x=190, y=200, width=150, height=30)

app.mainloop()
