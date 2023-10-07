from tkinter import *

janela = Tk()
janela.title("Calculadora")
janela.geometry("460x620")


numero1 = ""
numero2 = ""
operacao = ""
resultado = 0



def registrar_operacao(op):
    global operacao
    operacao = op
    resultado_tela.config(text=f"{numero1}{operacao}")




def registrar_numero(numero):
    global numero1
    global numero2
    if operacao == "":
        numero1 = f"{numero1}{numero}"
        resultado_tela.config(text=numero1)
    else:
        numero2 = f"{numero2}{numero}"
        resultado_tela.config(text=f"{numero1}{operacao}{numero2}")


def calcular():
    global resultado
    global numero1
    global numero2

    numero1_sem_espaco = numero1.strip()
    numero1_float = float(numero1_sem_espaco)

    numero2_sem_espaco = numero2.strip()
    numero2_float = float(numero2_sem_espaco)

    if operacao == "/":
        resultado = numero1_float / numero2_float
    elif operacao == "*":
        resultado = numero1_float * numero2_float
    elif operacao == "+":
        resultado = numero1_float + numero2_float
    elif operacao == "-":
        resultado = numero1_float - numero2_float
    resultado_tela.config(text=resultado)



resultado_tela = Label(text="", height=6, bg="#0efff9", width=20, font=('Ivy 20 bold'))
resultado_tela.grid(row=0, column=0, columnspan=4)

botao7 = Button(janela, text="7", width=15, height=5, command= lambda : registrar_numero("7"))
botao7.grid(row=1, column=0)
botao8 = Button(janela, text="8", width=15, height=5, command= lambda : registrar_numero("8"))
botao8.grid(row=1, column=1)
botao9 = Button(janela, text="9", width=15, height=5, command= lambda : registrar_numero("9"))
botao9.grid(row=1, column=2)
botaoDiv = Button(janela, text="/", width=15, height=5, command= lambda : registrar_operacao("/"))
botaoDiv.grid(row=1, column=3)

botaoIgual = Button(janela, text="=", width=15, height=5, command=calcular)
botaoIgual.grid(row=2, column=0)


janela.mainloop()