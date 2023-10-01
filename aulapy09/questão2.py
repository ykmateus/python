from tkinter import *

def calcular_media():
    nota1 = int(nota1_entry.get())
    nota2 = int(nota2_entry.get())
    nota3 = int(nota3_entry.get())
    nota4 = int(nota4_entry.get())
    media = (nota1 + nota2 + nota3 + nota4) / 4

    if media >= 6:
        resultado.config(text= f"{nome_entry.get()} foi aprovado com média {media}", fg="green")
    else:
        resultado.config(text= f"{nome_entry.get()} foi reprovado com média {media}", fg="red")

        

janela = Tk()

titulo = Label(text="Boletim do aluno")
titulo.pack()

nome_label = Label(text="Nome").pack()
nome_entry = Entry()
nome_entry.pack()


nota1_label = Label(text="Nota1").pack()
nota1_entry = Entry()
nota1_entry.pack()

nota2_label = Label(text="Nota2").pack()
nota2_entry = Entry()
nota2_entry.pack()

nota3_label = Label(text="Nota3").pack()
nota3_entry = Entry()
nota3_entry.pack()

nota4_label = Label(text="Nota4").pack()
nota4_entry = Entry()
nota4_entry.pack()


botao_calcular = Button(janela, text="Calcular", command=calcular_media).pack()

resultado = Label(text="")
resultado.pack()

janela.mainloop()
