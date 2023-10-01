from tkinter import *

def saudacao():
    print(f"Seja bem vindo, {nome_entrada.get()}!")
    nome_entrada.delete(0, END)

janela = Tk()

titulo = Label(text="Bem vindo", background="#051c1d", foreground="#b1aaaa")
titulo.pack()

nome_texto = Label(text="Nome:")
nome_texto.pack()

nome_entrada = Entry()
nome_entrada.pack()

botao_enviar = Button(janela, text="Enviar", command=saudacao)
botao_enviar.pack()

janela.mainloop()