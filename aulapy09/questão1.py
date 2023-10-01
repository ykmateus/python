from tkinter import *


def checagem ():
    num1 = int(numero1_entry.get())
    num2 = int(numero2_entry.get())
    numero1_entry.delete(0, END)
    numero2_entry.delete(0, END)
    if num1 > num2:
        resposta.set((f"O {num1} é o maior."))
    else:
        resposta.set(f"O {num2} é o maior.")


janela = Tk()

titulo = Label(text="Questão 1", background="#000000", foreground="#a5a29e")
titulo.pack()

numero1_label = Label(text="Digite o primeiro número:")
numero1_label.pack()
numero1_entry = Entry()
numero1_entry.pack()

numero2_label = Label(text="Digite o segundo número:")
numero2_label.pack()
numero2_entry = Entry()
numero2_entry.pack()

resposta = StringVar()

resultado = Label(textvariable=(resposta))
resultado.pack()

botao_checar = Button(janela, text="Chacando" , command=checagem)
botao_checar.pack()

janela.mainloop()