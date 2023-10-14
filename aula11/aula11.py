class Carro():
    #metodo construtor
    #a função __init__ serve para construir o objeto
    def __init__(self, marca:str, modelo:str, ano:int, cor:str):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
    
    def acelerar(self):
        return f"Acelerou o {self.marca}"
    


marca = str(input("Digite a marca: "))
modelo = str(input("Digite o modelo: "))
ano = int(input("Digite o ano: "))
cor = str(input("Digite a cor: "))

carro1 = Carro(marca=marca, modelo=modelo, ano=ano, cor=cor)

print(carro1.acelerar())