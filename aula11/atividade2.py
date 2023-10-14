class Fatura():
    #metodo construtor
    #a função __init__ serve para construir o objeto
    def __init__(self, nome:str, preco:float, quantidade:int):
        self.nome = nome
        self.preco = preco
        self.quantidade =quantidade
        
    def valor(self):
        return self.preco * self.quantidade

fatura_total = {}
fatura_inicial = 0

while True:
    nome = str(input("Digite o produto: "))
    if nome == "fim":
        break
    preco = float(input("Digite o preço: "))
    quantidade = int(input("Digite a quantidade: "))

    compras = Fatura(nome=nome, preco=preco, quantidade=quantidade)
    fatura_total[nome] = compras.valor()
    fatura_inicial = fatura_inicial + compras.valor()

print(fatura_inicial)
print(fatura_total)





# fatura_total = []
# fatura_inicial = 0

# while True:
#     nome = str(input("Digite o produto: "))
#     if nome == "fim":
#         break
#     preco = float(input("Digite o preço: "))
#     quantidade = int(input("Digite a quantidade: "))

#     compras = Fatura(nome=nome, preco=preco, quantidade=quantidade)
#     fatura_total.append(compras.valor())
#     fatura_inicial = fatura_inicial + compras.valor()

# print(fatura_inicial)
# print(fatura_total)








# compras = {}

# while True:
#     nome = str(input("Digite o produto: "))
#     if nome == "fim":
#         break
#     preco = str(input("Digite o preço: "))
#     quantidade = str(input("Digite a quantidade: "))
#     compras[nome] = nome
#     compras[valor] = preco*quantidade

# print compras